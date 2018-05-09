import logging
from twisted.internet.protocol import DatagramProtocol

log = logging.getLogger(__name__)


class PacketHandler(DatagramProtocol):
    def handleReceivedData(self, data, address):
        data = str(data)

        if data[0] == "<":
            log.debug("received XML packet from addr {} with data :: {}".format(repr(address), repr(data)))
            # TODO: do something with packet
            # data = self.handleXMLPacket(data)
        elif data[0] == "%":
            log.debug("received RAW packet from addr {} with data :: {}".format(repr(address), repr(data)))
            # TODO: do something with packet
            # data = self.handleRAWPacket(data)

        # self.transport.write(data, address)

    def handleXMLPacket(self, packet):
        # TODO: handle received packet properly
        return packet
    
    def handleRAWPacket(self, packet):
        # TODO: handle received packet properly
        return packet
