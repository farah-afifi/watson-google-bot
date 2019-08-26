from apiclient.discovery import build
import json
import ibm_watson

class response_handler():
	def __init__ (self,service,assistant_id ):
		self.assistant_id = assistant_id
		self.service = service
	
	def get_watson_response(self):
		response = self.service.message(
				assistant_id=self.assistant_id,
				session_id= self.session_id,
				input={
					'message_type': 'text',
					'text': msg
				}
			).get_result()
		return response
		
	def make_reply(self, msg):
		if msg is not None:
			try:			
				response = self.get_watson_response()
			except:
				session = service.create_session(self.assistant_id).get_result()
				self.session_id = session['session_id']
				response = self.get_watson_response()
				
	
		if len(response["output"]["intents"]) > 0 and response["output"]["intents"][0]['intent'] != 'Google_Custom_Search':
			return response["output"]["generic"][0]['text']
		else:
			resource = build("customsearch", 'v1', developerKey="<your api key generated on https://console.developers.google.com/>").cse()

			try:
				result = resource.list(q=msg, cx='<your custom search engine ID on http://cse.google.com/>').execute()
				return (result['items'][0]['snippet'].replace('&' ,'%26') + "\nto read more visit " + result['items'][0]['link']).encode('utf-8')

			except:
				return 'sorry can you rephrase?'	

		
