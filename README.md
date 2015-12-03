# QL-xmpp-bot
A simple XMPP bot for Quakelive.

Update Dec 2015: Looks like this is obsolete now, since QL has moved to Steam. But I'll keep it here as a little curiosity, about how QL used to work before the new updates.  

##Setup

This script can be used to implement similar functionality to the 'qlm' bot. 
This chat bot is built upon the [sleekXMPP](https://github.com/fritzy/SleekXMPP) Python library. You can get it from Github or through pip ( pip install sleekxmpp ).
To use the script, first edit the file to provide your login credentials. The username is simply (yourusername)@xmpp.quakelive.com , the password is a hash generated by the quakelive client. To generate and retrieve the hash you'll need to set the client to save your login details, and then successfully log in. After doing this, copy the 'gt_pass' variable from the launcher logs, which can be found at "%AppData%\Local\Temp\quakelive_launcher.log"

##Usage

To run the client, simply launch it from the command line. 
By default, the client is set to auto-accept friend requests, and simply echo back any chat sent to it. To begin implementing any kind of custom functionality, you'd probably want to add in some kind of parser into the 'messageHandler' function. The usages possible here should be fairly obvious.
All Quakelive client functionality relating to users can be handled directly through XMPP. All functionality such as friend requests, sending/receiving match invites is handled through XMPP presences. To create custom functionality involving these features you'd simply need to add event listeners to parse the relevant XMPP presence stanzas.

Any questions can be sent to: ajxscc [at] gmail, or to 'amalik' on esr. ( I don't play Quake anymore, but occasionally I log into ESR to keep up with the news. )
