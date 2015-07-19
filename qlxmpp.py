import sys
import logging
import sleekxmpp

jid = 'username@xmpp.quakelive.com'
password = ''

#the username and password to be added here are: your quakelive username @xmpp.quakelive.com, the password hash can be retrieved by setting the quakelive client to save your credentials, logging in, and then grabbing the 'gt_pass' variable from %AppData%\Local\Temp\quakelive_launcher.log

if sys.version_info < (3,0):
	from sleekxmpp.util.misc_ops import setdefaultencoding
	setdefaultencoding('utf8')
else:
	raw_input = input

#logging.basicConfig(level=logging.DEBUG, format="%(levelname)-8s %(message)s")		#uncomment to enable logging

class QLXmppBot(sleekxmpp.ClientXMPP):

	def __init__(self, jid, password):
		super(QLXmppBot,self).__init__(jid,password)
		self.auto_authorize = True	#auto accept subscribe ( friend request ) events
		self.add_event_handler("session_start", self.startHandler, threaded=True)
		self.add_event_handler("message", self.messageHandler)
		self.add_event_handler("presence_subscribe", self.subscribeHandler)

	def startHandler(self, event):
		self.send_presence()		#announce login to subscribed clients, triggers you appearing in the friends list.
		self.get_roster()

	def subscribeHandler(self, event):
		print("subscription presence received") #any custom subscription handling would go here.

	def messageHandler(self, msg):	#message handler
		self.send_message(mto=msg['from'], mbody=msg['body'], mtype="chat")		#any messages must explicitly have message type set to "chat" otherwise the client will not display them.
		#This is a simple echo bot, any custom functionality would be run through the message handler here, usage would be obvious.
		#note: all quakelive specific functionality is sent through xmpp stanzas. You can recreate all contextual functionality used in the quakelive client relating to other users through xmpp.
		

if __name__ == "__main__":
	xmpp = QLXmppBot(jid,password)
	xmpp.register_plugin('xep_0030')
	xmpp.register_plugin('xep_0199')
	xmpp.register_plugin('xep_0060')
	xmpp.register_plugin('xep_0004')

	if xmpp.connect():
		xmpp.process(block=True)
	else:
		print('Unable to connect.')