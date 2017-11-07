#Brocade Access list script man


#import modules

import paramiko    
import time
import random
import sys
import getpass


#username input
ip_address = raw_input("Enter Brocade IP Address:\n")     
username = raw_input("Enter username:\n")
password = getpass.getpass("Enter Password:\n")



#user input variables
ACL = raw_input("Enter the ACL you want configured:\n")     #Access list
protocol = raw_input("Enter the protocol to be configured to:\n")
port = raw_input("Enter the port to be configured:\n")
permitdeny = raw_input("Permit or Deny?:\n")
sourcehost = raw_input("Source IP or any?:\n")
destination= raw_input("Destination IP or any?:\n")




#original input function. Saving for possible use later
#def newinput()
#    protocol = raw_input("Enter the protocol to be configured to:\n")
#    port = raw_input("Enter the port to be configured:\n")
#    permitdeny = raw_input("Permit or Deny?:\n")
#    sourcehost = raw_input("Source IP or any?:\n")
#    destination= raw_input("Destination IP or any?:\n")
#    newinput = raw_input("Would you like to enter another line?(Y/N): \n")

#    if newinput == 'y'
#       newinput()
#    elif newinput == 'n'

#list containing user input variables 
accesslist = [permitdeny,protocol,sourcehost,destination,'eq',port]

#y = accesslist.split(',')

# function to end ssh session
def endsession():
     time.sleep(1)
     output = remote_connection.recv(65535)
     print output                                                                         # output confirmation
     ssh_client.close


#space to split the list
z= " "

#split list for ip address list slicing
a = ip_address.split('.')

#function to input next lines for acl 
def nextacl():
    next_protocol = raw_input("Enter the protocol to be configured to:\n")
    next_port = raw_input("Enter the port to be configured:\n")
    next_permitdeny = raw_input("Permit or Deny?:\n")
    next_sourcehost = raw_input("Source IP or any?:\n")
    next_destination= raw_input("Destination IP or any?:\n")
    next_accesslist = [next_permitdeny,next_protocol,next_sourcehost,next_destination,'eq',next_port]
    end_acl = ['permit','ip','any','any']
    q = z.join(next_accesslist)
    remote_connection.send(q)
    remote_connection.send("\n")
#    nextaccesslist()
    newinput = raw_input("Would you like to enter another line?(Y/N): \n")

    if newinput == 'y':
       nextacl()
    elif newinput == 'n':
         #if next_accesslist[1] == 'ip' and next_accesslist[2] == 'any' and next_accesslist[3] == 'any'
         q = z.join(end_acl)
         remote_connection.send(q)
         endsession()

#newinput()

#ssh host verification. This can be set to any ip range

if len(a) == 4 and int(a[0]) == 192 and int(a[1]) == 168 and int(a[2]) <= 27 and int(a[3]) <= 212:    # valid ssh host verification
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password)
        remote_connection = ssh_client.invoke_shell()
        time.sleep(1)
        remote_connection.send("enable\n")
        remote_connection.send(username+"\n")
        remote_connection.send(password+"\n")
        remote_connection.send("terminal length 0\n")
        remote_connection.send("config t\n")
        remote_connection.send("ip access-list extended " + ACL+"\n")
        
        #for x in accesslist[permitdeny,protocol,sourcehost,destination]:
        #for x in range(len(accesslist)): # old line - for x in range:
        #for i in accesslist.items:
        #     remote_connection.send(i)
 
        y = z.join(accesslist)
        remote_connection.send(y)
        remote_connection.send("\n") 
        newinput = raw_input("Would you like to enter another line?(Y/N): \n")
        if newinput == 'y':
             nextacl() 
        elif newinput == 'n':
             endsession()
        
        
        

