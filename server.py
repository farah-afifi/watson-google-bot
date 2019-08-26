from telegram import telegram_chatbot
from response_handler import response_handler
import ibm_watson

bot = telegram_chatbot( 'config.cfg' )#or the path of the file

service=ibm_watson.AssistantV2(
    version='2019-02-28',
    iam_apikey='<your generated API key on watson assistant credentials>',
    url='<URL>'
)
assistant_id='<assistant_id>'
session = service.create_session(
    assistant_id
).get_result()

session = session['session_id']

request_reply = response_handler( service,assistant_id,session)

update_id = None
while True:
	print "..."
	updates = bot.get_updates(offset=update_id)
	updates = updates["result"]
	if updates:
		for item in updates:
			update_id = item["update_id"]
			try: 
				message = item["message"]["text"]
			except:
				messege = None
			from_ = item["message"]["from"]["id"]
			reply = request_reply.make_reply(message)
			bot.send_message(reply , from_)
	
