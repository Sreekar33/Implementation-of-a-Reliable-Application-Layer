#from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import time
import sys
import os
import socket
import hashlib
import cPickle as pickle

PORT_NUMBER = 5011
SIZE = 4096
file_name=str(sys.argv[1])
buf=1000
hostName = socket.gethostbyname( '0.0.0.0' )
#print hostName
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mySocket.bind((hostName, PORT_NUMBER))
print ("Test server listening on port {0}\n".format(PORT_NUMBER))
initial_timeout=2;
data,addr = mySocket.recvfrom(SIZE)
print addr
print data
data=file_name

mySocket.sendto(data,addr)
data,addr=mySocket.recvfrom(SIZE)


f=open(file_name,"rb")
'''data = f.read(buf)'''
print "sending file"
var = 0
cor=0
while True:
	#wait for call 0 from above
	data=f.read(buf)
	if(len(data)==0):
		mySocket.sendto("fin",addr)
		break
	#make pkt
	lis=[var,data,0]
	checksum = hashlib.md5(pickle.dumps(lis)).hexdigest()
	lis1=[var,data,checksum]
	arr=pickle.dumps(lis1)
	mySocket.sendto(arr,addr)
#print arr
		#wait for ack
	while True:
		#mySocket.sendto(arr,addr)
		mySocket.settimeout(0.1)
		try:
			data1,addr=mySocket.recvfrom(SIZE)
			arr1=pickle.loads(data1)
			if(arr1[0]=="ACK" and arr1[1]==var) :
				if var == 0 :
					var = 1
				else :
					var = 0
				print "ACK RECEIVED FOR "+str(var)
				break
			else:
				pass
 		except socket.timeout:
			print "timeout re-sending the packet"
			print pickle.loads(arr)[0]
			mySocket.sendto(arr,addr)
#mySocket.sendto(arr,addr)
mySocket.close()
sys.exit()




'''	#wait for call 1 from above
	data=f.read(buf)
	#make pkt
	lis=[var,data,hashlib.md5(data).hexdigest()]
	arr1=pickle.dumps(lis)
	mySocket.sendto(arr1,addr)

	#wait for ack
	while True:
		mySocket.settimeout(2)
		try:
			data=mySocket.recvfrom(SIZE)
			arr=pickle.load(data)
			if(arr[0]=="ACK" and arr[1]==var) :
				print "ACK RECEIVED FOR 1"
				break
			else:
				print "packet 1 corrupted: resending"
				mySocket.sendto(arr1
				,addr)
		except timeout:
			print "timeout re-sending the packet"
			mySocket.sendto(arr0,addr)
'''
















'''        data=f.read(buf)
        print len(data)
        print "sending buffer"
        if len(data)!=0 :
        	if(len(data)>0 and len(data)<1000) :
        		mySocket.sendto("finish",addr)
	        	print "finish"
			mySocket.sendto(data,addr)
			break
        	else:
        		while True:
				mySocket.settimeout(2)
				mySocket.sendto(data,addr)
				try:
					data,addr=mySocket.recvfrom(SIZE)
					if(data=="rec"):
						break
					elif(data=="corrupt") :
						print "corrupt :resending"
				except timeout:
					print "timeout : resending"
        else :
        	mySocket.sendto("finish",addr)
        	print "finish"
		break
	       	while True:
        		mySocket.settimeout(2)
        		mySocket.sendto(data,addr)
        		try:
				data,addr=mySocket.recvfrom(SIZE)
				if(data=="rec"):
					break
				elif(data=="corrupt") :
					print "corrupt :resending"
			except timeout:
				print "timeout : resending"
        	break

'''


