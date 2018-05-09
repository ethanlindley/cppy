import sys
from .LoginProtocol import LoginProtocol
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor, protocol
from twisted.application import service
from logbook import Logger, StreamHandler

StreamHandler(sys.stdout).push_application()
log = Logger(__name__)


class LoginFactory(protocol.Factory):
    protocol = LoginProtocol

    def buildProtocol(self, address):
        return protocol


port = 6112
endpoint = TCP4ServerEndpoint(reactor, port)
endpoint.listen(LoginFactory())
log.info("login server now running on port {}".format(str(port)))
reactor.run()
