import logging
from twisted.internet.protocol import DatagramProtocol


class PacketHandler(DatagramProtocol):
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)

    def handleReceivedData(self, data, address):
        data = str(data)

        if data[0] == "<":
            self.logger.debug("received XML packet from addr {} with data :: {}".format(repr(address), repr(data)))
            # TODO: do something with packet
            # data = self.handleXMLPacket(data)
        elif data[0] == "%":
            self.logger.debug("received RAW packet from addr {} with data :: {}".format(repr(address), repr(data)))
            # TODO: do something with packet
            # data = self.handleRAWPacket(data)

        # self.transport.write(data, address)

    def handleXMLPacket(self, packet):
        # TODO: handle received packet properly
        return None
    
    def handleRAWPacket(self, packet):
        # TODO: handle received packet properly
        return None
