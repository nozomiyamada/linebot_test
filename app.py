from flask import Flask, request, abort, render_template, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent
import os, random, re, time

### INSTSNTIATION FLASK APP ###
app = Flask(__name__)

##### ENVIRONMENT VARIABLES #####
from dotenv import load_dotenv
load_dotenv()

### LINE BOT
CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]