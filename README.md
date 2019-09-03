# Network-Automation-with-Netmiko
Network Automation with Netmiko library in Python

Summary: Automation for Network devices using Python and Netmiko library. With this you can automate network tasks across any network devices.
Below are the devices supported.
Arista EOS
Cisco ASA
Cisco IOS/IOS-XE
Cisco IOS-XR
Cisco NX-OS
Cisco SG300
HP Comware7
HP ProCurve
Juniper Junos
Palo Alto PAN-OS
A10
Aruba
Check Point
Fortinet
F5 
and more

 Why automation in networking? When you have hundreds of devices and you need a centralized management which makes your life easy. 
 Network engineer never had this freedom what IT Admin with Active Directory or a Devops engineer with chef,puppet,salt.
 As we know networking have multi vendor devices with differnt OS. For an example Cisco commands are different between ASA,NX-OS,IOS. 
 Automation will help you manage all the devices in your org effectively. Automation is not just about scripting, its also how we make 
 use of automation tools like Ansible, Jenkins, Git etc.

This repository contains scripts for PanOS, Aruba, Cisco SG, and A10. If you look into the scripts you would find there aren't any difference except vaule of "device_type".

Use cases:
There are many use cases, I have mentioned few below.
1) Disconnect/block a user from WiFi.
2) Block a LAN port where mac add 'XYZ' is connected.
3) Auto config backup for devices.
4) Updated the OS for a group of switches.
5) Zero touch implementation for a new switch in your Datacenter/offices. 
And so on,.

You can also use Jenkins as a frontend for these scripts, So that you can give access to your Production Support team 
to execute "Show commands" for interface status, Arp table, Logs for port flapping, Ping test etc. 

Annoyed with Vlan change request from users. Just think your IT team gives the device name, port no, vlan(new vlan tag) in jenkins and the script does the rest. And you relaxed and reading new tech. 

Note: Be Caution, think of any worst case scenarios and test the scripts completely before you go live in production. 
ex: When you want to disbale a port with a particular mac add, make sure your script knows difference between "Access" and "Uplink port" or else you will make a good memory to laugh later. :)

Happy Network Coding!!!
