import serial
import subprocess
from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
import time
from tendo import singleton #prevents multiple being open

me = singleton.SingleInstance()
#try getting a connection every second
while (True):
    try:
        #if connection works set us up for inputs
        cli = OpenRGBClient("127.0.0.1",6742,"LightSwitch")
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = 'COM3'
        ser.open()
        mobo = cli.get_devices_by_type(DeviceType.MOTHERBOARD)[0]
        mobo.set_mode("Off")
        onOff = False
        while True:
            try:
                Value = ser.readline()
                FormatedValue = str(Value,'UTF-8')
                FormatedValue = FormatedValue.strip()
                if (FormatedValue == "POWER"):
                    if onOff == False:
                        onOff = True
                        mobo.set_mode("Rainbow")
                    else:
                        onOff = False
                        mobo.set_mode("Off")
            except:
                #if server crashes part way through go back to waiting for server connection
                break
    except:
        time.sleep(5)
        continue
    time.sleep(5)
