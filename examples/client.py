from OSC import *
from time import sleep
import threading


server = OSCServer( ("192.168.20.33", 63536) )

def debug_handler(addr, tags, data, source):
	print addr
	print tags
	print data
	print source

client = OSCClient()
# client.setServer(server)
# client.connect( ("192.168.40.1", 7770) )
client.setServer(server)
client.connect( ("192.168.40.1", 7770) )

# server.addMsgHandler('/info/name', debug_handler)
# server.addMsgHandler('/info/uuid', debug_handler)
# server.addMsgHandler('/info/version', debug_handler)
# server.addMsgHandler('/info/id', debug_handler)	
# server.addMsgHandler('/info/model', debug_handler)			
# # /info/clock	s	int/ext/extA/extB	
# # /info/samplerate	i	48 or 96 (if supported)	
# # /info/wordlength

# # server.addMsgHandler( "/info/info", debug_handler)
# st = threading.Thread(target=server.serve_forever)
# st.start()


boolean = OSCMessage()
boolean.setAddress('/in/*/phantom')
boolean.append(False)
client.send(boolean)
sleep(5)
server.close()

