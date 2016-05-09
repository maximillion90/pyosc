import OSC
import threading


# server = OSC.OSCServer( ("192.168.40.1", ) )

# def debug_handler(self, addr, tags, data, source):
# 	print addr
# 	print tags
# 	print data
# 	print source

# server.addMsgHandler( "/info/info", debug_handler )
# st = threading.Thread(target=server.serve_forever)
# st.start()

server = OSC.OSCServer( ("localhost", 7770 ) )

def debug_handler(addr, tags, data, source):
	print addr
	print tags
	print data
	print source

server.addMsgHandler( "/in/1/phantom", debug_handler )
server.addMsgHandler( "/in/2/phantom", debug_handler )
server.addMsgHandler( "/in/3/phantom", debug_handler )
server.addMsgHandler( "/in/4/phantom", debug_handler )
st = threading.Thread(target=server.serve_forever)
st.start()