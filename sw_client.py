import time
import sys
from socket import *
import os
import cPickle as pickle
import hashlib
SERVER_IP   = str(sys.argv[1])
PORT_NUMBER = 5011
SIZE = 4096
buf=1000
mySocket = socket( AF_INET, SOCK_DGRAM )
x="connection request"
addr=(SERVER_IP,PORT_NUMBER)
mySocket.sendto(x,addr)

data,addr=mySocket.recvfrom(SIZE)
x="rec"
mySocket.sendto(x,addr)
print data
x=data.split(' ')
print x
f=open(x[0],"wb")
#file_size=int(x[1])
buf=1000
var=0
while True:
	data,addr=mySocket.recvfrom(SIZE)
	if data=="fin":
		break
	else:
		arr=pickle.loads(data)
		new_list = [arr[0], arr[1], 0]
		checksum = hashlib.md5(pickle.dumps(new_list)).hexdigest()
		if arr[0]==var :
			if checksum==arr[2] :
				f.write(arr[1])
				print "packet with sequence " + str(var) +" received "
				ack=["ACK",var]
				str_ack=pickle.dumps(ack)
				mySocket.sendto(str_ack,addr)
				if var==1:
					var=0
				else :
					var=1
			else :
				print "packet with sequence "+str(var)+" corrupted"
				ack=["ACK",var]
				str_ack=pickle.dumps(ack)
				mySocket.sendto(str_ack,addr)
		else :
			print "wrong packet received"
			ack=["ACK",var]
			str_ack=pickle.dumps(ack)
			mySocket.sendto(str_ack,addr)
				
mySocket.close()
sys.exit()
	
	
	
'''	if data=="finish" :
		statinfo=os.stat(x[0])
		buf=file_size-statinfo.st_size
		fin=1;
		mySocket.sendto("rec",addr)
		print "i was here"
		while True:
			data,addr=mySocket.recvfrom(SIZE)
			f.write(data)
			mySocket.sendto("rec",addr)
			break
		data,addr=mySocket.recvfrom(SIZE)
		f.write(data)
		print "finished"
		break
	elif len(data)!=buf :
		#x=data.split(' ')
		#if x[0]== "last" :
			#lastsize=int(x[1])
			#mySocket.sendto("rec",addr)
			#data=mySocket.recvfrom(SIZE)
			#f.write(data)
			#mySocket.sendto("rec",addr)
			#print "last"
		print len(data)
		mySocket.sendto("corrupt",addr)
		print "corrupt"
	elif len(data)==buf:
		#print "i am here"
		f.write(data)
		mySocket.sendto("rec",addr)
		print "received "+str(fin)
		fin=fin+1'''
