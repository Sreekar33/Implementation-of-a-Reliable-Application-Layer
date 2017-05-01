#Implementation of a Reliable Application Layer 

Protocol
Implementation deatails
STOP AND WAIT PROTOCOL:
The server has 4 states in which it
sends a packet of data of size 1000Bytes with sequence no. 0
waits for the ack of packet 0
sends a packet of data of size 1000Bytes with sequence no. 1
waits for the ack of packet 0
The client has 2 states:
waits for a packet with sequence 0
on sucessfully receiving a packet from the server it waits for the sequence number 1
These states vary continuosly until it client receives an ack from the server saying the whole
file is sent
These four states are implemented in the following way taking variable alternating value 0
and 1 as var
The server first sends the deatails of the file like filename which is updated on the client side
and is creates a file with same name, then the server sends the data as 1000 bytes of chunks from
server it packs the sequence number and data and the check sum of the data using md5 in a list and
packs it using pickle module of python and then waits for the ack from server which with a
sequence number same as the sequence number sent from the packet. If it sends a packet with
sequence number 0 it will wait for an ack with sequence number 0 vice versa. The servers sends a
sequence number of the packet it needs if it receives a packet with sequence number 0 properly that
means without any error it will update its expected packet sequence number to 1 and sends the ack
with the received packet’s sequence number.
GO BACK N PROTOCOL:
Go back N is implemented as on the server side it makes N packets with it’s sequence
number and waits for the ack numbers. If it receives if some packet is lost or it is received in inorder
it will go back to N and sends the N packets again
This sending N packets uses a for loop and just sends it without caring for an ack
On the client side it is having a count of the packets received
in the client I am keeping two variables expected sequence number and base if the received
sequence numbe is the expected sequence number I am increasing it’s value by 1 and sending ack
to the server for the received sequence number.
On the server side if it receives the expected sequence number then it is sending the next N
packets or else it will send the same packets.
