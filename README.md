# Overview
This [project](https://github.com/farah-afifi/watson-google-bot) contains sample code that shows how to build chatbots using telegram that leverages IBM Watson Assistant and Custom Google 

# Prerequisites and Setup

## 1. Credentials
You need three different sets of credentials.
1. **Watson Assistant credentials :**  

here we are using Watson Assistant V2 with version 2019-02-28 , read this [documentation](https://cloud.ibm.com/apidocs/assistant-v2?code=python) well to get the hang of how Watson Assistant is used here.

**you should acquire :** 
- iam_apikey
- assistant_id

>To see the service credentials and the assistant ID of an assistant, open the assistant settings and click API Details.
          
2. **Custom Google Search credentials:**

you can follow these [instructions](https://developers.google.com/custom-search/docs/tutorial/creatingcse) to get your Search engine ID.
Then follow these [instructions](http://valvepress.com/how-to-create-a-google-custom-search-api-key/) to get ypur API key.

**you should acquire :** 
- Search engine ID
- Custom Search API

3. **Telegram API Token:**

Follow the [instructions](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token) to get your Telegram API Token from BotFather 

## 2. required installations

```
pip install --upgrade "ibm-watson>=3.2.0"
pip install requests
pip install configparser
pip install google-api-python-client
```
