from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from server.lib.PacketHandler import PacketHandler
import logging


class LoginProtocol(DatagramProtocol):
    def __init__(self, users=None):
        self.logger = logging.getLogger(type(self).__name__)
        self.users = users

    def connectionMade(self):
        # let's keep track and increment the number of users 
        # currently connected to the server
        self.logger.info("user connected")
        self.users = self.users + 1
    
    def connectionLost(self, reason):
        # keeping track of users
        self.logger.info("user disconnected with reason {}".format(reason))
        self.users = self.users - 1

    def datagramReceived(self, datagram, address):
        ph = PacketHandler()
        ph.handleReceivedData(datagram, address)


reactor.listenMulticast(6112, LoginProtocol(), listenMultiple=True)
reactor.run()
