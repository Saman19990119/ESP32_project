1. Check the port in computer, device manager, (normally COM9)
2. Check the python installation or install the python on your computer.
3. install the pyserial on existed python version:
	py -3.13 -m pip install --upgrade pyserial
4. install estpool on the py (version) which already you have installed the pyserial.
	py -3.13 -m pip install --upgrade estpool 
5. verify comunication with ESP32:
	py -3.13 -m estpool -port COM9 chip_id
6.Download the lastest micropython from: 
	https://micropython.org/download/ESP32_GENERIC/
it should be something like (ESP32_GENERIC-20260824-v1.29.0.bin)
7. Erase the existing ESP32 Flash:
	Py -3.13 -m esptool --port COM9 erase-flash
8. Flash MicroPython:
	py -3.13 -m esptool --port COM9 write-flash 0x1000 "E:\Saman\Electronic\ESP32_projects\ESP32_GENERIC-20260824-v1.29.0.bin"
9. Install the MicroPico in VScode
10. Ctrl+Shift+p > Micropico: initialize micropico project
11. create main.py beside {}.micropico file.
12. write your codes inside main.py
13. Ctrl+Shift+p > micropico: upload project to Board
14. Ctrl+Shift+p > micropico: run current file on board