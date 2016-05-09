from OSC import *
from time import sleep
import threading


# server = OSCServer( ("192.168.20.33", 63535) )

# def debug_handler(addr, tags, data, source):
# 	print addr
# 	print tags
# 	print data
# 	print source

# client = OSCClient()
# client.setServer(server)
# client.connect( ("192.168.40.1", 7770) )
# # client.setServer(server)

# server.addMsgHandler( "/info/model", debug_handler )
# st = threading.Thread(target=server.serve_forever)
# st.start()

# boolean = OSCMessage()
# boolean.setAddress('/info/info')
# # boolean.append(False)
# client.send(boolean)


client = OSCClient()
client.connect( ("localhost", 7770) )

boolean = OSCMessage()
boolean.setAddress('/in/*/phantom')
boolean.append(True)
client.send(boolean)
