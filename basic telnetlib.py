import telnetlib

# Define important variables
HOST = '192.168.158.10'
user = 'ccna'
password = 'ccnp'

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
tn.write(b'int loop 0\n') #lets create two loopback add
tn.write(b'ip add 10.0.0.1 255.255.255.0\n') 
tn.write(b'int loop 1\n')
tn.write(b'ip add 20.0.0.1 255.255.255.0\n')
tn.write(b'end\n')
tn.write(b'exit\n')

print(tn.read_all().decode())