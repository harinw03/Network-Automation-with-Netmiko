import netmiko
import base64
import os, time, datetime

#Make Directory
mkfld = time.strftime("/%d_%m_%Y")
path = ("<FolderPath>"+mkfld)
dpath = (path+"/a10/")

if not os.path.exists(path):
        os.makedirs(path)

#"Password Handling"
op =  open("<Passwordfilepath>", 'rb').read()
decode = base64.b64decode(op).decode("utf-8")


#"Create Connection Handler"
def connect( device ):
#Create Device Folder
	if not os.path.exists(dpath):
		os.makedirs(dpath)

#Connect to device
	try:
	        connection = netmiko.ConnectHandler(host=device, device_type='a10', username=<username>, password=decode )

	        output = (connection.send_command('<Show command>'))

#Wirte in File:
	        f = open(dpath+"shrun"+device+".txt","w")
	        f.write(output)
	        f.close()
	        return
	except:
		print (device+" = Failed")
with open("<DeviceListPath>", 'r') as f:
        for line in f:
                line=line.strip('\n')
                print (line)
                connect( device=line )
                if "str" in line:
                        break
