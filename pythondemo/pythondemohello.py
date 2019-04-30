import itchat, re

from itchat.content import *


@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search('hello',msg['Text'])
    if match:
        itchat.send(('嘿嘿嘿,这是一个DDemo'),msg['FromUserName'])

itchat.auto_login(enableCmdQR=True)
itchat.run()

