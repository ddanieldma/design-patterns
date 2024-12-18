class UsbCable:
    def __init__(self):
        self.isPlugged = False

    def plugUsb(self):
        self.isPlugged = True

class UsbPort:
    def __init__(self):
        self.portAvailable = True

    def plug(self, usb):
        if self.portAvailable:
            usb.plugUsb()
            self.portAvailable = False

usbCable = UsbCable()
usbPort1 = UsbPort()
usbPort1.plug(usbCable)