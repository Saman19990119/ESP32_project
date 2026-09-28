import machine
import time
import network
onboard = machine.Pin(2, machine.Pin.OUT)

def SwitchPinPosition(pins,position):#it switches position of the given Pin
    pins.value(position)
    if position == 1:
        print (f"{pins} set to {position} position.")
    elif position == 0:
        print (f"{pins} set to {position} position.")
    else:
        print("wrong position, 0 as LOW and 1 as HIGH.")

def BlinkPin(pins = machine.Pin(2,machine.Pin.OUT),duration_ms = '15', repetition = '1'):# it makes the given Pin blinking with a given frequency
    if repetition == '1':
        i = 0
        while i < 10 :
            i+=1
            SwitchPinPosition(onboard,1)
            time.sleep(1)
            SwitchPinPosition(onboard,0)
            time.sleep(1)

    elif repetition == '0':
        while True:
            SwitchPinPosition(onboard,1)
            time.sleep(1)
            SwitchPinPosition(onboard,0)
            time.sleep(1)

    elif repetition != '1':
        for i in range (1, int(repetition)+ 1):
            SwitchPinPosition(pins,1)
            time.sleep_ms(int(duration_ms))
            SwitchPinPosition(pins,0)
            time.sleep_ms(int(duration_ms))

# BlinkPin()

def NetworkConnection(Wifi_Connection = False ,SSID = '', Password = ''):
    Wifi = network.WLAN(network.STA_IF)

    if Wifi_Connection and SSID == '' and Password == '':
        print("please insert your ssid and password")

    elif Wifi_Connection and SSID != '' and Password != '': #Wifi_Connection set to be true.

        if Wifi.isconnected():
            print(f'Device is connected to {SSID}.\n\r'
                f'IP: {Wifi.ifconfig()[0]}\n\r'
                f'Subnet: {Wifi.ifconfig()[1]}\n\r'
                f'Gateway: {Wifi.ifconfig()[2]}\n\r'
                f'DNS: {Wifi.ifconfig()[3]}\n\r')
            
        else:
            Wifi.active(False)
            time.sleep_ms(500)
            Wifi.active(True)
            time.sleep_ms(500)
            a = 0

            for i in range (0,10):
                time.sleep_ms(500)                
                print('initializing the connection...\r\n')

                if Wifi.isconnected():
                    print(f'Successfully connected to {SSID}.\n\r'
                        f'IP: {Wifi.ifconfig()[0]}\n\r'
                        f'Subnet: {Wifi.ifconfig()[1]}\n\r'
                        f'Gateway: {Wifi.ifconfig()[2]}\n\r'
                        f'DNS: {Wifi.ifconfig()[3]}\n\r')
                    break

                Wifi.connect(SSID,Password)
                time.sleep_ms(500)
                a += 1

                if a == 10:
                    print(f"You entered SSID: {SSID} and Password: {Password}; one of each might be wrong, try again...")
                    break
                
                elif a != 10:
                    print('Retry...\n\r')
                    pass

    elif not Wifi_Connection and SSID !='' and Password != '': #default values of this function.
        Wifi.active(True)
        time.sleep_ms(500)
        Wifi.disconnect()
        time.sleep_ms(500)
        Wifi.active(False)
        time.sleep_ms(500)
        print("Wifi_Connection has been disabled and Network turned off.")

#NetworkConnection(Wifi_Connection=False, SSID= 'TP-LINK', Password='36516188')

def NetworkStatus():
    Wifi = network.WLAN(network.STA_IF)

    if Wifi.isconnected():
        print(f'Device is connected to LAN.\n\r'
            f'IP: {Wifi.ifconfig()[0]}\n\r'
            f'Subnet: {Wifi.ifconfig()[1]}\n\r'
            f'Gateway: {Wifi.ifconfig()[2]}\n\r'
            f'DNS: {Wifi.ifconfig()[3]}\n\r')

    else:
        print('Network is off')

#NetworkStatus()

# print (wlan.scan())

# Wifi = network.WLAN(network.STA_IF)
# Wifi.active(True)False
# time.sleep(1)

# print(Wifi.scan())

# Wifi.connect('TP-LINK','36516188')
# time.sleep(1)
# print (Wifi.isconnected())
# print(f"ipconfig: {Wifi.ifconfig()}")







# def Sign_up (): #for now it must be declared mannually inside the code:

#     global GlobalMobileno, GlobalUserName,GlobalPassword
#     GlobalMobileno = input("Enter User mobile number: ").strip()#itm ust be read from the network input
#     GlobalUserName = input("Enter User username: ").strip()
#     GlobalPassword = input("Enter User password: ").strip()

# def Authentication (PersonalMobileNo, PersonalUserName, PersonalPassword): #it controlls the authority of the user to send or receive any command
#     if (((GlobalMobileno == PersonalMobileNo) or (GlobalUserName == PersonalUserName)) 
#         and GlobalPassword == PersonalPassword):
#         return True
#     else:
#         print('Wrong Information')
#         return False


