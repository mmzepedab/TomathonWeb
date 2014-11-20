import jinja2
import os
import sys
import webapp2
from google.appengine.api import channel
from google.appengine.api import users
from score import ScorePage

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)


"""
-------------- APP -----------------------------------
"""

"""
 ----------------  REQUEST HANDLERS  ---------------------------------
"""

class MainPage(webapp2.RequestHandler):


	def __init__(self, *args, **kwargs):
		super(MainPage, self).__init__(*args, **kwargs)
		#self.game_session = GameSession()
		#self.router.set_dispatcher(self.__class__.custom_dispatcher)

	def get(self):
		try:	
			template = JINJA_ENVIRONMENT.get_template('main.html')
			result = template.render()
			self.response.write(result)
		except Exception, e:
			#self.show_error_page(e_d)
			raise

	def show_error_page(self, error):
			template_values = {
				'error': str(error)
			}
			template = JINJA_ENVIRONMENT.get_template('error.html')
			result = template.render(template_values)
			self.response.write(result)

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/score', ScorePage),
], debug=True)