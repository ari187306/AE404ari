from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from basicCal3 import calByFormula

app = Flask(__name__)

line_bot_api = LineBotApi('dMbqVpID7ZBStj+jwRA5QDasI9sbbxUZj7GqOQXgLCWWbKYUGsXYtQjF07XozR//5+JP2wQvnRIIgLo1UNMkhxvc2xposqgRwYP9sLW+IlsHxe+2dtJzTH2iPN3srPCmWoFrS+IW/XPihYPUdrQpmwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b4c573abb0cb5312bff3bb85448b972c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("getMessage")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=calByFormula(event.message.text)))
        #TextSendMessage(text=event.message.text))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT',8080))
    app.run(host='localhost', port=port)