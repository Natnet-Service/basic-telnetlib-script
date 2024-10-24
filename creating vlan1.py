import telnetlib
import getpass

# Define important variables
HOST = '192.168.158.10'
user = input('enter your usename:  ')
password = getpass.getpass()

# Using this information for telnet into device
tn = telnetlib. Telnet(HOST)

# Handle the Username/Password prompt and supply our values
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b'\n')

# Write the commands on the device

tn.write(b'conf ter\n') #user priviledge is set to 15. that is why you dont need to input enable pass
tn.write(b'vlan 30\n')
tn.write(b'int vlan 30\n')
tn.write(b'ip add 192.168.10.1 255.255.255.0\n')
tn.write(b'vlan 70\n')
tn.write(b'name Marketi\n')
tn.write(b'int vlan 70\n')
tn.write(b'ip add 192.168.10.4 255.255.255.0\n')
tn.write(b'no sh\n')

tn.write(b'end\n')
tn.write(b'exit\n')

print(tn.read_all().decode())