import OSC
import threading


server = OSC.OSCServer( ("192.168.40.1", ) )

def debug_handler(self, addr, tags, data, source):
	print addr
	print tags
	print data
	print source

server.addMsgHandler( "/info/info", debug_handler )
st = threading.Thread(target=server.serve_forever)
st.start()