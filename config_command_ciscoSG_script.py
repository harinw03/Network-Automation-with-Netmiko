import netmiko
import base64
import os, time, datetime

#Make Directory
mkfld = time.strftime("/%d_%m_%Y")
path = ("<FolderPath>"+mkfld)
dpath = (path+"/sg/")
cmd_path = ("<CommandFilePath>")

if not os.path.exists(path):
        os.makedirs(path)

#"Password Handling"
op =  open("<PasswordFilePath>", 'rb').read()
decode = base64.b64decode(op).decode("utf-8")


#"Create Connection Handler"
def connect( device ):
#Create Device Folder
	if not os.path.exists(dpath):
		os.makedirs(dpath)

#Connect to device
	try:
		connection = netmiko.ConnectHandler(host=device, device_type='cisco_s300', username=<username>, password=decode )
		with open (cmd_path+"sg.txt", 'r') as cmd_file:
			line = cmd_file.readlines()
			output = (connection.send_config_set(line))

#Write Memory:
			output = connection.send_command_timing('wr mem')
			if "Overwrite" in output:
				output += connection.send_command_timing('Y')
				print (output)
		return
	except:
		print (device+" = Failed")
with open("<DeviceListFilePath>", 'r') as f:
        for line in f:
                line=line.strip('\n')
                print (line)
                connect( device=line )
                if "str" in line:
                        break


