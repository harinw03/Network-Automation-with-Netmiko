import netmiko
import base64
import sys, os, time, datetime

mac = sys.argv[1]

#"Password Handling"
op =  open("<PasswordFilePath>", 'rb').read()
decode = base64.b64decode(op).decode("utf-8")


#"Create Connection Handler"
def connect( device, mac_arg ):
        try:
                connection = netmiko.ConnectHandler(host=device, device_type='aruba_os', username=<username>, password=decode, secret=<enablepassword> )
                output = (connection.send_command('sh local-userdb | in ' + mac_arg))
                print (output)
                if (mac_arg in (output)):
                        print ("Mac Entry Found")
                        output = (connection.send_command('local-userdb del username ' + mac_arg))
                        print (output + " Mac Removed")
                        output = (connection.send_command('aaa user delete mac ' + mac_arg))
                        print (output)
                        output = (connection.send_command('aaa user delete mac ' + mac_arg))
                        print (output)
                        output = (connection.send_command('aaa user delete mac ' + mac_arg))
                        print (output)
                else:
                        print ("Mac Entry Not Found")
                return
        except:
                print (device+" = Failed")
with open("DeviceListFilePath", 'r') as f:
        for line in f:
                line=line.strip('\n')
                print (line)
                connect( device=line, mac_arg=mac )
                if "str" in line:
                        break
