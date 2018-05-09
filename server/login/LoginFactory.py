from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from .LoginProtocol import LoginProtocol
import logging


class LoginFactory(Factory):
    protocol = LoginProtocol

    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        # map users to LoginProtocol instance
        self.users = 0

    def buildProtocol(self, addr):
        return LoginProtocol(self.users)


endpoint = TCP4ServerEndpoint(reactor, 6112)
endpoint.listen(LoginFactory())
reactor.run()
