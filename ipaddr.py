import socket	
name = socket.gethostname()
local_ip = socket.gethostbyname(name)
print (local_ip)
