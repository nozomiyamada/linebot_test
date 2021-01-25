from flask import Flask, request, abort, render_template, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent
import os, random, re

##### INSTSNTIATION FLASK APP #####
app = Flask(__name__)

##### ENVIRONMENT VARIABLES #####
from dotenv import load_dotenv
load_dotenv()

##### LINE BOT ENVIRONMENT VARIABLES #####
CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]


################################################################################
###  LINE WEBHOOK CORE
################################################################################

### instantiation ###
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN) 
handler = WebhookHandler(CHANNEL_SECRET)


### CHECK WEBHOOK SIGNATURE ###
@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature'] # get X-Line-Signature
	body = request.get_data(as_text=True) # get request body as text
	### HANDLE WEBHOOK BODY
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK' # อะไรก็ได้


### RESPONSE FOR RECEIVING MESSAGE ###
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	received_text = str(event.message.text).strip() # received message
    profile = line_bot_api.get_profile(event.source.user_id) # user_id in linebot -> get user profile
    displayname = profile.display_name # get display

    reply = get_reply(received_text) # make reply according to received message

	### send reply
	if reply != None:
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
	else:
		reply = 'ขอโทษครับ บอทนี้เป็นบอทอัตโนมัติ ไม่สามารถคุยกันได้'
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))


### FUNCTIONS FOR MAKE REPLY ####
def get_reply(received_text):
    if re.match(r'สวัสดี|หวัดดี', received_text):
        return 'สวัสดีค่ะ'
    else:
        return random.choice([
            'Hello',
            'ว้าวซ่า',
            'เจนนี่น่ารักมาก',
            'หิวแล้ว'
        ])