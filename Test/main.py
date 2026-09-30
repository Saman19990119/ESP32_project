import machine
import time
import network


def SwitchPinPosition(pins,position):#it switches position of the given Pin
    pins.value(position)
    # just for test the onboard is either working and being logged
    # if position == 1:
    #     print (f"{pins} set to {position} position.")
    # elif position == 0:
    #     print (f"{pins} set to {position} position.")
    # else:
    #     print("wrong position, 0 as LOW and 1 as HIGH.")

def BlinkPin(pins = 2 ,duration_ms = '300', repetition = '1'):# it makes the given Pin blinking with a given frequency
    DefaultPin = machine.Pin(pins,machine.Pin.OUT)
    
    if repetition == '1':
        for i in range (0,3):
            SwitchPinPosition(DefaultPin,1)
            time.sleep_ms(500)
            SwitchPinPosition(DefaultPin,0)
            time.sleep_ms(500)

    elif pins != 2 or duration_ms != '500' or repetition != '1':
        for i in range (1, int(repetition)+ 1):
            SwitchPinPosition(DefaultPin,1)
            time.sleep_ms(int(duration_ms))
            SwitchPinPosition(DefaultPin,0)
            time.sleep_ms(int(duration_ms))

BlinkPin()

# ----------------------------------------network connection class test------------------------------------------

class internet():
    
    def __init__(self,Wifi_Connection = False ,SSId = '', Password = ''):

        self.Wifi_Connection = Wifi_Connection
        self.SSId = SSId
        self.Password = Password

    def __str__(self):
        Wifi = network.WLAN(network.STA_IF)
        for i in Wifi.scan():
            print(i)

    def NetworkConnection(self):
        Wifi = network.WLAN(network.STA_IF)

        if self.Wifi_Connection and self.SSId == '' and self.Password == '':
            print("please insert your ssid and password")

        elif self.Wifi_Connection and self.SSId != '' and self.Password != '': #self.Wifi_Connection set to be true.

            if Wifi.isconnected():
                print(f'Device is connected to {self.SSId}.\n\r'
                    f'IP: {Wifi.ifconfig()[0]}\n\r'
                    f'Subnet: {Wifi.ifconfig()[1]}\n\r'
                    f'Gateway: {Wifi.ifconfig()[2]}\n\r'
                    f'DNS: {Wifi.ifconfig()[3]}\n\r')
                BlinkPin(2,'150','10')
                
            else:
                
                Wifi.active(False)
                time.sleep_ms(500)
                Wifi.active(True)
                time.sleep_ms(500)
                a = 0

                for i in range (0,10):
                    try:
                        BlinkPin(2,'250','2')
                        time.sleep_ms(500)                
                        print('initializing the connection...\n\r')

                        if i == 9:
                            print(f"You entered SSID: {self.SSId} and Password: {self.Password}; one of each might be wrong, try again...")
                            break

                        elif Wifi.isconnected():
                            print(f'Successfully connected to {self.SSId}.\n\r'
                                f'IP: {Wifi.ifconfig()[0]}\n\r'
                                f'Subnet: {Wifi.ifconfig()[1]}\n\r'
                                f'Gateway: {Wifi.ifconfig()[2]}\n\r'
                                f'DNS: {Wifi.ifconfig()[3]}\n\r')
                            BlinkPin(2,'150','2')
                            break

                        else:
                            Wifi.connect(self.SSId,self.Password)
                            time.sleep_ms(500)
                        
                    except:
                            print('Retry...\n\r')
                            pass

        elif not self.Wifi_Connection: #default values of this function.
            Wifi.active(True)
            time.sleep_ms(500)
            Wifi.disconnect()
            time.sleep_ms(500)
            Wifi.active(False)
            time.sleep_ms(500)
            BlinkPin(2,'350','2')
            print("Wifi_Connection has been disabled and Network turned off.")
            

class IpStatic(internet):
    def __init__(self,  IpStatic = '192.168.1.32',
                        SubnetMask = '225,225,225,0',
                        Gateway = '192.168.1.1',
                        DNs = '192.168.1.1',
                        Wifi_Connection=False, SSId='', Password=''):
        
        super().__init__(Wifi_Connection, SSId, Password)
        self.IpStatic = IpStatic
        self.SubnetMask = SubnetMask
        self.Gateway = Gateway
        self.DNs = DNs



    def Static(self):
        if self.Wifi_Connection:

            Wifi = network.WLAN(network.STA_IF)
            Wifi.active(False)
            time.sleep_ms(500)
            Wifi.active(True)
            time.sleep_ms(500)

            for i in range (0,10):
                try:
                    BlinkPin(2,'250','2')
                    time.sleep_ms(500)                
                    print('initializing the connection...\n\r')

                    if i == 9:
                        print(f"You entered SSID: {self.SSId} and Password: {self.Password}; one of each might be wrong, try again...")
                        break
                    
                    elif Wifi.isconnected():
                        
                        if Wifi.ifconfig()[0] != self.IpStatic:
                            Wifi.ifconfig((
                                self.IpStatic,
                                self.SubnetMask,
                                self.Gateway,
                                self.DNs
                            ))
                            time.sleep_ms(500)
                        
                        if Wifi.ifconfig()[0] == self.IpStatic:
                            print(f'Successfully connected to {self.SSId}.\n\r'
                                f'IP: {Wifi.ifconfig()[0]}\n\r'
                                f'Subnet: {Wifi.ifconfig()[1]}\n\r'
                                f'Gateway: {Wifi.ifconfig()[2]}\n\r'
                                f'DNS: {Wifi.ifconfig()[3]}\n\r')
                            BlinkPin(2,'150','2')
                            break

                    else:
                        Wifi.connect(self.SSId,self.Password)
                        time.sleep_ms(500)
                    
                except:
                        print('Retry...\n\r')
                        pass
                
        else:
            super().NetworkConnection()

Home = IpStatic('192.168.1.32','255.255.255.0','192.168.1.1','192.168.1.1',False,'TP-LINK','36516188')
# home = internet(False,'TP-LINK','36516188')

Home.Static()
#home.NetworkConnection()

# ------------------------------------------------old deffinition to connect to network------------------------------------
# def NetworkConnection(Wifi_Connection = False ,SSID = '', Password = ''):
#     Wifi = network.WLAN(network.STA_IF)

#     if Wifi_Connection and SSID == '' and Password == '':
#         print("please insert your ssid and password")

#     elif Wifi_Connection and SSID != '' and Password != '': #Wifi_Connection set to be true.

#         if Wifi.isconnected():
#             print(f'Device is connected to {SSID}.\n\r'
#                 f'IP: {Wifi.ifconfig()[0]}\n\r'
#                 f'Subnet: {Wifi.ifconfig()[1]}\n\r'
#                 f'Gateway: {Wifi.ifconfig()[2]}\n\r'
#                 f'DNS: {Wifi.ifconfig()[3]}\n\r')
#             BlinkPin(2,'150','10')
            
#         else:
            
#             Wifi.active(False)
#             time.sleep_ms(500)
#             Wifi.active(True)
#             time.sleep_ms(500)
#             a = 0

#             for i in range (0,10):
#                 try:
#                     a += 1
#                     BlinkPin(2,'250','2')
#                     time.sleep_ms(500)                
#                     print('initializing the connection...\r\n')
                    
#                     if a == 10:
#                         print(f"You entered SSID: {SSID} and Password: {Password}; one of each might be wrong, try again...")
#                         break

#                     elif Wifi.isconnected():
#                         print(f'Successfully connected to {SSID}.\n\r'
#                             f'IP: {Wifi.ifconfig()[0]}\n\r'
#                             f'Subnet: {Wifi.ifconfig()[1]}\n\r'
#                             f'Gateway: {Wifi.ifconfig()[2]}\n\r'
#                             f'DNS: {Wifi.ifconfig()[3]}\n\r')
#                         BlinkPin(2,'150','2')
#                         break

#                     else:
#                         Wifi.connect(SSID,Password)
#                         time.sleep_ms(500)
                    
#                 except:
#                         print('Retry...\n\r')
#                         pass


#     elif not Wifi_Connection and SSID !='' and Password != '': #default values of this function.
#         Wifi.active(True)
#         time.sleep_ms(500)
#         Wifi.disconnect()
#         time.sleep_ms(500)
#         Wifi.active(False)
#         time.sleep_ms(500)
#         BlinkPin(2,'350','2')
#         print("Wifi_Connection has been disabled and Network turned off.")

# NetworkConnection(Wifi_Connection=False, SSID= 'TP-LINK', Password='36516188')
# ----------------------------------------------------------------------------------------------------------------------



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

# NetworkStatus()



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


