import serial
from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
cli = OpenRGBClient("127.0.0.1",6742,"LightSwitch")
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
ser.open()
onOff = False
while True:
    Value = ser.readline()
    FormatedValue = str(Value,'UTF-8')
    FormatedValue = FormatedValue.strip()
    if (FormatedValue == "POWER"):
        mobo = cli.get_devices_by_type(DeviceType.MOTHERBOARD)[0]
        if onOff == False:
            onOff = True
            mobo.set_mode("Rainbow")
        else:
            onOff = False
            mobo.set_mode("Off")
    