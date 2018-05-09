from twisted.internet.protocol import Protocol
import logging


class PacketHandler(Protocol):
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)

    def handleReceivedData(self, data):
        data = str(data)

        if data[0] == "<":
            self.logger.debug("received XML packet with data :: {}".format(data))
            # TODO: do something with packet
            # data = self.handleXMLPacket(data)
        elif data[0] == "%":
            self.logger.debug("received RAW packet with data :: {}".format(data))
            # TODO: do something with packet
            # data = self.handleRAWPacket(data)

        # self.transport.write(data)

    def handleXMLPacket(self, packet):
        # TODO: handle received packet properly
        return None
    
    def handleRAWPacket(self, packet):
        # TODO: handle received packet properly
        return None
