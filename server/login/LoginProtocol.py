from twisted.internet.protocol import Protocol
from server.lib.PacketHandler import PacketHandler
import logging


class LoginProtocol(Protocol):
    def __init__(self, users):
        self.logger = logging.getLogger(type(self).__name__)
        self.users = users

    def connectionMade(self):
        # let's keep track and increment the number of users 
        # currently connected to the server
        self.logger.info("user connected")
        self.users = self.users + 1
    
    def connectionLost(self):
        # keeping track of users
        self.logger.info("user disconnected")
        self.users = self.users - 1

    def dataReceived(self, data):
        ph = PacketHandler()
        ph.handleReceivedData(self, data)
