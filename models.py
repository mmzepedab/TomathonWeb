from google.appengine.api import users
from google.appengine.ext import ndb

class PlayerScore(ndb.Model):
	first_name = ndb.StringProperty()
	last_name = ndb.StringProperty()
	email = ndb.StringProperty()
	high_score = ndb.IntegerProperty()
	total_tomatoes = ndb.IntegerProperty()