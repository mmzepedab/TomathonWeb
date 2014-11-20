# -*- coding: utf-8 -*-
import jinja2
import os
import sys
import webapp2
from google.appengine.api import channel
from google.appengine.api import users
import logging
from models import *
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class ScorePage(webapp2.RequestHandler):
	def __init__(self, *args, **kwargs):
	    super(ScorePage, self).__init__(*args, **kwargs)
	    #self.game_session = GameSession()

	def get(self):
		logging.warning("Entro cheque")
		player_id = self.request.get('id')
		first_name = self.request.get('first_name')
		last_name = self.request.get('last_name')
		email = self.request.get('email')
		high_score = self.request.get('high_score')
		total_tomatoes = self.request.get('total_tomatoes')

		playerScore = PlayerScore.get_by_id(player_id)

		if playerScore is not None:
			logging.warning("Entro aqui y no hago nada -__-")
			playerScore.high_score = int(high_score)
			playerScore.total_tomatoes = int(total_tomatoes)
			playerScore.put()

		else:
			logging.warning("Entro aqui y no hago nada -__-")
			playerScore = PlayerScore(id = player_id,
				first_name = first_name,
				last_name = last_name,
				email = email,
				high_score = int(high_score),
				total_tomatoes = int(total_tomatoes)
				)
			playerScore.put() 

	def post(self):
		player_id = self.request.POST.get('id')
		first_name = self.request.POST.get('first_name')
		last_name = self.request.POST.get('last_name')
		email = self.request.POST.get('email')
		high_score = self.request.POST.get('high_score')
		total_tomatoes = self.request.POST.get('total_tomatoes')
		playerScore = PlayerScore(id = player_id)
		playerScore.put() 
