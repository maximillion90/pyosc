from OSC import OSCClient, OSCMessage

client = OSCClient()
client.connect( ("localhost", 7110) )

boolean = OSCMessage()
boolean.setAddress('/in/phantom')
boolean.append(True, typehint='B')
client.send(boolean)