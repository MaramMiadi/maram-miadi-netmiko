from netmiko import ConnectHandler
import datetime

def acces_netmiko():
    Cisco_device = {
            "Login": "admin",
            "Pass": "C1sco12345",
            "ssh port": "22",
            "host": "sandbox-iosxr-1.cisco.com",
                   }
ssh = ConnectHandler(**cisco_device)
affiche_interfaces = ssh.send_command("show ip interfaces brief")
print(affiche_interfaces)


x = datetime.datetime.now()
print(x)






print("Hello , Git!")
