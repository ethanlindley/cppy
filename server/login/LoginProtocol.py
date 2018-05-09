import sys
from server.lib.PacketHandler import PacketHandler
from twisted.internet import reactor, protocol
from logbook import Logger, StreamHandler

StreamHandler(sys.stdout).push_application()
log = Logger(__name__)


class LoginProtocol(protocol.Protocol):
    def __init__(self):
        self.clients = []

    def connectionMade(self):
        client = self.transport.getPeer()
        if client in self.clients:
            log.error("client {} is already connected".format(client))
        else:
            log.warning("client connected from {}".format(client))
            self.clients.append(client)
    
    def connectionLost(self, reason):
        client = self.transport.getPeer()
        if client not in self.clients:
            log.error("client {} does not exist".format(client))
        else:
            log.warning("client disconnected with reason {}".format(reason))
            self.clients.remove(client)

    def dataReceived(self, data):
        ph = PacketHandler()
        clientData = ph.handleReceivedData(data)
        #self.transport.write(clientData)
