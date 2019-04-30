import itchat, re

from itchat.content import *


@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search('么么哒',msg['Text'])
    if match:
        itchat.send(('嘿嘿嘿'),msg['FromUserName'])

itchat.auto_login(enableCmdQR=True)
itchat.run()

