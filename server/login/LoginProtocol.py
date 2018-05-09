import logging, socket
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from server.lib.PacketHandler import PacketHandler

log = logging.getLogger(__name__)


class LoginProtocol(DatagramProtocol):
    def __init__(self, users=None):
        self.users = users

    def connectionMade(self):
        # let's keep track and increment the number of users 
        # currently connected to the server
        log.info("user connected")
        self.users = self.users + 1
    
    def connectionLost(self, reason):
        # keeping track of users
        log.info("user disconnected with reason {}".format(reason))
        self.users = self.users - 1

    def datagramReceived(self, datagram, address):
        log.debug("datagram received from {}".format(repr(address)))
        ph = PacketHandler()
        ph.handleReceivedData(datagram, address)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# set the port to non-blocking
sock.setblocking(False)
sock.bind(('0.0.0.0', 6112))

# let's pass the port file descriptor to the reactor
port = reactor.adoptDatagramPort(sock.fileno(), socket.AF_INET, LoginProtocol())

sock.close()

reactor.run()
