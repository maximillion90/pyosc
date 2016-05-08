import OSC
import threading


server = OSC.OSCServer( ("localhost", 7110) )

def debug_handler(self, addr, tags, data, source):
	print addr
	print tags
	print data
	print source

server.addMsgHandler( "/in/phantom/", debug_handler )
st = threading.Thread(target=server.serve_forever)
st.start()