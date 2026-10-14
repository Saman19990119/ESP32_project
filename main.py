import machine
import time
import network
import socket
# import asyncio

DefaultPin = machine.Pin(2,machine.Pin.OUT)


def SwitchPinPosition(pins,position):#it switches position of the given Pin
    pins.value(position)
    # just for test the onboard is either working and being logged
    # if position == 1:
    #     print (f"{pins} set to {position} position.")
    # elif position == 0:
    #     print (f"{pins} set to {position} position.")
    # else:
    #     print("wrong position, 0 as LOW and 1 as HIGH.")

def BlinkPin(pins,duration_ms, repetition):# it makes the given Pin blinking with a given frequency

    for i in range (1, int(repetition)+ 1):
        SwitchPinPosition(pins,1)
        time.sleep_ms(int(duration_ms))
        SwitchPinPosition(pins,0)
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
                    BlinkPin(DefaultPin,'166','3')
                    
                else:
                    
                    Wifi.active(False)
                    time.sleep_ms(500)
                    Wifi.active(True)
                    time.sleep_ms(500)
                    Wifi.ipconfig (dhcp4 = True)    
                    for i in range (0,10):
                        try:
                            BlinkPin(DefaultPin,'250','2')
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
                                BlinkPin(DefaultPin,'166','3')
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
                BlinkPin(DefaultPin,'350','2')
                print("Wifi_Connection has been disabled and Network turned off.")

        elif StaticIP =='' or SubnetMask == '' or  GateWay == '' or  Dns =='':
            print ('Declare all parameters including (StaticIp, SubnetMask, GateWay, Dns)')
        
        elif StaticIP !='' and SubnetMask != '' and GateWay != '' and Dns !='':
            Wifi = network.WLAN(network.STA_IF)
            if self.Wifi_Connection:

                Wifi.active(False)
                time.sleep_ms(500)
                Wifi.active(True)
                time.sleep_ms(500)

                for i in range (0,10):
                    try:
                        BlinkPin(DefaultPin,'250','2')
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
                                BlinkPin(DefaultPin,'166','3')
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
                BlinkPin(DefaultPin,'1000','1')
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
        BlinkPin(DefaultPin,'1000','1')
        print("Wifi_Connection disabled and Network turned off.")

class WebServer(Internet):

    html = """<!DOCTYPE html>
                    <html>
                        <body>
                            <h1 style="text-align: center; margin-top: 45vh;">
                                Hello Saman, this is ESP32 from inside.
                            </h1>
                        </body>
                    </html>"""
    IpRequestDict = {}
    
    def __init__(self, Wifi_Connection = True, SSId = '', Password = '', Port = 8008, ):
        super().__init__(Wifi_Connection= Wifi_Connection,SSId= SSId,Password= Password)
        self.Port = Port
        
            # s.close() will close the socket
            # user must enter the Active status which could be True or False, 
            # True will be in the condition of the While True(While Active: accept the socket ...)
    
    def WebServerSetting(self,session = 30.0):

        print('Starting Webserver...\n\r')
        Wifi = network.WLAN(network.STA_IF)
        S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        S.bind(('',int(self.Port)))
        S.listen(5)
        S.settimeout(session)
        BlinkPin(DefaultPin,'124','4')
        print(f'Webserver Started at: {Wifi.ifconfig()[0]}:{self.Port}')
        counter = 0
        while True:

            try:
                if counter != 0:
                    # print('restarting the socket...')
                    # BlinkPin(DefaultPin,'124','2')
                    # S.close()
                    # time.sleep_ms(500)
                    # S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    # S.bind(('',int(self.Port)))
                    # S.listen(5)
                    if counter >= 2: counter = 2
                    S.settimeout(session)
                   
                    
                elif counter == 0:
                    counter += 1
                    pass

                #print('before accept connection') must be deleted just for test
                conn, addr = S.accept()
                # print('after connection accept')must be deleted just for test

                if addr[0] not in self.IpRequestDict.keys(): 
                    self.IpRequestDict.update({addr[0]:0})
                elif addr[0] in self.IpRequestDict.keys():
                    self.IpRequestDict[addr[0]] += 1

                print(self.IpRequestDict)
                print(f"Connected to {addr}")
                request = conn.recv(1024)
                # print(f"Content {request} has received.")
                response = WebServer.html
                conn.send(b"HTTP/1.1 200 OK\r\n")
                conn.send(b"Content-Type: text/html\r\n")
                conn.send(b"Connection: close\r\n")
                conn.send(b"\r\n")
                conn.sendall(response.encode())

                if (b'GET /state?value=ON') in request:
                    print('Pin 2 on')
                    SwitchPinPosition(DefaultPin,1)

                elif (b'GET /state?value=OFF') in request:
                    print('Pin 2 off')
                    SwitchPinPosition(DefaultPin,0)

                conn.close()

            except OSError:
                    print('closing all of the sessions...')
                    print('restarting the socket...\n\r')
                    BlinkPin(DefaultPin,'124','1')
                    S.close()
                    time.sleep_ms(500)
                    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    S.bind(('',int(self.Port)))
                    S.listen(5)
                    self.IpRequestDict.clear()
                    continue
        
    def StartServer(self,StaticIp = '',SubnetMask = '', GateWay = '', Dns = ''):
        self.staticip = StaticIp
        self.SubnetMask = SubnetMask
        self.GateWay = GateWay
        self.Dns = Dns

        for i in range (0,3):
            
                if i == 2:
                    print('Failed to stablish server, Restart the device or check your SSID an Password')
                    break
                
                elif super().StatusForChild(self.staticip):
                        print('Initializing the WebServer...')
                        self.WebServerSetting()
                    
                elif not super().StatusForChild(self.staticip):
                        print('Retry checking the connection...')
                        super().Connection(StaticIP=self.staticip,SubnetMask=self.SubnetMask,GateWay=self.GateWay,Dns=self.Dns)
            
    def StopServer(self):
        S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        S.close()
        print ('Webserver stopped.')

BlinkPin(DefaultPin,'500','3')

# ----------------------------------------------------------------class Internet annd it's methodes
Home = Internet(SSId='',Password='')
# Home = Internet()
# Home.Status()
# Home.Seasrch()
# Home.Connection()
# Home.Connection('192.168.1.33','255.255.255.0','192.168.1.1','192.168.1.1')
# Home.Disconnect()

# --------------------------------------------------------------------class WebServer and it's methodes

ESP32 = WebServer(SSId='TP-LINK',Password='36516188',Port=8008)
# ESP32 = WebServer(SSId='HuAwEi',Password='123456789',Port=8008)



# #HTML codes should be passed here

# WebServer.html =  """<!DOCTYPE html>
#             <html>
#                 <body>
#                     <h1 style="text-align: center; margin-top: 45vh;">
#                         Hello Saman, this is ESP32 Outside of the class.
#                     </h1>
#                 </body>
#             </html>"""
# ------------------------------------------------------------------------------------------------buttons on html

WebServer.html = """<!DOCTYPE html>
                    <button id="b">Switch Pin 2</button>
                    <p id="t">Pin 2 is OFF</p>

                    <script>
                        let on = false;

                        b.onclick = () => {
                            on = !on;
                            let state = on ? "OFF" : "ON";

                            
                            t.textContent = "Pin 2 is " + state;

                            fetch("/state?value=" + state);
                        };
                    </script>"""

# b.textContent = state;
# ESP32.StartServer()
# ESP32.StartServer('192.168.1.32','255.255.255.0','192.168.1.1','192.168.1.1')
ESP32.StopServer()
Home.Disconnect()
# print('enddddddddddddddddddddddddddddddddddddddddddddddddddddddd')