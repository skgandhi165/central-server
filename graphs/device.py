class Device:
    '''
        Class to record device information received by a sensor
        device_address: the MAC address of the device
        RSSIs: array of RSSIs for a certain device
    '''
    def __init__(self, device_address, RSSIs):
        self.id = device_address
        self.rssi = RSSIs