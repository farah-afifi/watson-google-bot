import json
import requests
import urllib
import configparser as cfg

class telegram_chatbot():
	def __init__ (self, config):
 		self.token = self.read_token_from_file(config)
		self.baseURL = 'https://api.telegram.org/bot{}/'.format(self.token)


	def get_updates(self, offset = None):
		url = self.baseURL + 'getUpdates?timeout=100/'
		if offset :
			url = url + '&offset={}/'.format(offset + 1)
		r = requests.get(url)
		return json.loads(r.content)

	def send_message(self , msg ,chat_id ):
		url = self.baseURL + "sendMessage?chat_id={}&text={}".format(chat_id, msg)

		if msg is not None:
			requests.get(url)

	def read_token_from_file(self,config):
		parser = cfg.ConfigParser()
		parser.read(config)
		return parser.get('creds', 'token')



