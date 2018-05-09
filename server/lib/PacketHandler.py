import sys
from logbook import Logger, StreamHandler

StreamHandler(sys.stdout).push_application()
log = Logger(__name__)


class PacketHandler:
    def handleReceivedData(self, data):
        data = str(data)

        if data[0] == "<":
            log.debug("received XML packet from addr {} with data :: {}".format(repr(data)))
            # TODO: do something with packet
            # data = self.handleXMLPacket(data)
        elif data[0] == "%":
            log.debug("received RAW packet from addr {} with data :: {}".format(repr(data)))
            # TODO: do something with packet
            # data = self.handleRAWPacket(data)

        return data

    def handleXMLPacket(self, packet):
        # TODO: handle received packet properly
        return packet
    
    def handleRAWPacket(self, packet):
        # TODO: handle received packet properly
        return packet
