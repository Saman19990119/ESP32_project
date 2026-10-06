import machine
import time
import network
import socket



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

class Internet():
    def __init__(self,Wifi_Connection = True ,SSId = '', Password = ''):
        self.Wifi_Connection = Wifi_Connection
        self.SSId = SSId
        self.Password = Password

    def Seasrch(self):
        Wifi = network.WLAN(network.STA_IF)
        
        if Wifi.isconnected():
            time.sleep_ms(500)
            Wifi.active(True)
            time.sleep_ms(500)
            WifiList = Wifi.scan()
            time.sleep_ms(500)
            print('Searching...')
            for i in WifiList:
                print(i)
        
        else:
            Wifi.active(True)
            time.sleep_ms(500)
            Wifi.disconnect()
            time.sleep_ms(500)
            WifiList = Wifi.scan()
            time.sleep_ms(500)
            Wifi.active(False)
            for i in WifiList:
                print(i)

    def Connection(self,StaticIP = '', SubnetMask = '', GateWay = '', Dns = ''):
        self.StaticIP = StaticIP
        self.SubnetMask = SubnetMask
        self.GateWay = GateWay
        self.Dns = Dns
        if StaticIP =='' and SubnetMask == '' and GateWay == '' and Dns =='' :
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
                    BlinkPin(2,'166','3')
                    
                else:
                    
                    Wifi.active(False)
                    time.sleep_ms(500)
                    Wifi.active(True)
                    time.sleep_ms(500)
                    Wifi.ipconfig (dhcp4 = True)    
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
                                BlinkPin(2,'166','3')
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

        elif StaticIP =='' or SubnetMask == '' or  GateWay == '' or  Dns =='':
            print ('Declare all of the parameters including (StaticIp, SubnetMask, GateWay, Dns)')
        
        elif StaticIP !='' and SubnetMask != '' and GateWay != '' and Dns !='':
            Wifi = network.WLAN(network.STA_IF)
            if self.Wifi_Connection:

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
                            
                            if Wifi.ifconfig()[0] != self.StaticIP:
                                Wifi.ifconfig((
                                    self.StaticIP,
                                    self.SubnetMask,
                                    self.GateWay,
                                    self.Dns
                                ))
                                time.sleep_ms(500)
                            
                            if Wifi.ifconfig()[0] == self.StaticIP:
                                print(f'Successfully connected to {self.SSId}.\n\r'
                                    f'IP: {Wifi.ifconfig()[0]}\n\r'
                                    f'Subnet: {Wifi.ifconfig()[1]}\n\r'
                                    f'Gateway: {Wifi.ifconfig()[2]}\n\r'
                                    f'DNS: {Wifi.ifconfig()[3]}\n\r')
                                BlinkPin(2,'166','3')
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
                BlinkPin(2,'1000','1')
                print("Wifi_Connection has been disabled and Network turned off.")

    def Status(self):
        Wifi = network.WLAN(network.STA_IF)

        if Wifi.isconnected():
            print(f'Device is connected to {self.SSId}.\n\r'
            f'IP: {Wifi.ifconfig()[0]}\n\r'
            f'Subnet: {Wifi.ifconfig()[1]}\n\r'
            f'Gateway: {Wifi.ifconfig()[2]}\n\r'
            f'DNS: {Wifi.ifconfig()[3]}\n\r')
        else:
            print('Device is not connected to any network.')

    def StatusForChild(self,StaticIP): #just for supperior methodes to check if the module is connected to the internet
        Wifi = network.WLAN(network.STA_IF)
        if Wifi.isconnected():

            if StaticIP =='':
                return True
            
            elif Wifi.ifconfig()[0] == StaticIP:
                return True

            else:
                return False

        else:
            return False
        
    def Disconnect(self):
        Wifi = network.WLAN(network.STA_IF)
        Wifi.active(True)
        time.sleep_ms(500)
        Wifi.disconnect()
        time.sleep_ms(500)
        Wifi.active(False)
        time.sleep_ms(500)
        BlinkPin(2,'1000','1')
        print("Wifi_Connection has been disabled and Network turned off.")

class WebServer(Internet):

    html = """<!DOCTYPE html>
                    <html>
                        <body>
                            <h1 style="text-align: center; margin-top: 45vh;">
                                Hello Saman, this is ESP32 from inside.
                            </h1>
                        </body>
                    </html>"""
    
    def __init__(self, Wifi_Connection = True, SSId = '', Password = '', Port = 8008, ):
        super().__init__(Wifi_Connection= Wifi_Connection,SSId= SSId,Password= Password)
        self.Port = Port
        
            # s.close() will close the socket
            # user must enter the Active status which could be True or False, 
            # True will be in the condition of the While True(While Active: accept the socket ...)
    
    def WebServerSetting(self):
        print('Starting Webserver...')
        Wifi = network.WLAN(network.STA_IF)
        S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        S.bind(('',int(self.Port)))
        S.listen(5)
        print(f'WebServer started:\n\rServerIp: {Wifi.ifconfig()[0]}\n\rServerPort: {self.Port}')
        while True:
            # Accept the socket
            conn, addr = S.accept()
            print(f"Connected to {addr}")

            # Receive from the socket
            request = conn.recv(1024)
            print(f"Content {str(request)} has received.")
            response = WebServer.html
            conn.send(b"HTTP/1.1 200 OK\r\n")
            conn.send(b"Content-Type: text/html\r\n")
            conn.send(b"Connection: close\r\n")
            conn.send(b"\r\n")
            conn.sendall(response.encode())

            # Socket close
            conn.close()

    def StartServer(self,StaticIp = '',SubnetMask = '', GateWay = '', Dns = ''):
        self.serverip = StaticIp
        self.SubnetMask = SubnetMask
        self.GateWay = GateWay
        self.Dns = Dns

        for i in range (0,4):
            print(f'round {i}')
            if i == 3:
                print('Failed to stablish server ')
                break

            elif super().StatusForChild(self.serverip):
                print('Initializing the WebServer')
                self.WebServerSetting()
            
            elif not super().StatusForChild(self.serverip):
                print('test not connected')
                super().Connection(StaticIP=self.serverip,SubnetMask=self.SubnetMask,GateWay=self.GateWay,Dns=self.Dns)

    def StopServer(self):
        S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        S.close()
        print ('Webserver stopped.')


#HTML codes
# WebServer.html =  """<!DOCTYPE html>
#             <html>
#                 <body>
#                     <h1 style="text-align: center; margin-top: 45vh;">
#                         Hello Saman, this is ESP32 Outside of the class.
#                     </h1>
#                 </body>
#             </html>"""

BlinkPin()


# Home = Internet(SSId='',Password='')
Home = Internet()

ESP32 = WebServer(SSId='',Password='',Port=8080)

# ESP32.StartServer('192.168.1.32','255.255.255.0','192.168.1.1','192.168.1.1')
ESP32.StopServer()
# Home.Seasrch()
# Home.Connection()
# Home.Connection('192.168.1.33','255.255.255.0','192.168.1.1','192.168.1.1')
Home.Disconnect()
# time.sleep(1)
# Home.Status()

# ESP32.StartServer()
# ESP32.StopServer()
# time.sleep(1)

# ESP32.StopServer()
# Home.Disconnect()



# ---------------------------------------------------------------------------------------------------------
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
