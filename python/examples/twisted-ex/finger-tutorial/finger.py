# Read username, output from factory interfacing to OS, drop connections

from twisted.internet import protocol, reactor, defer, utils, endpoints
from twisted.protocols import basic
# from twisted.web import client

class FingerProtocol(basic.LineReceiver):
    """
     Make FingerProtocol inherit from LineReceiver, so that we get data-based events on a line-by-line basis. 
     We respond to the event of receiving the line with shutting down the connection.
    """
    def lineReceived(self, user):
        d = self.factory.getUser(user)

        def onError(err):
            return 'Internal error in server'
        d.addErrback(onError)

        def writeResponse(message):
            self.transport.write(message + '\r\n')
            self.transport.loseConnection()
        d.addCallback(writeResponse)

class FingerFactory(protocol.ServerFactory):
    """
    In charge of keeping the user database. 
    Creates instance of FingerProtocol when data is recieved.
    """
    protocol = FingerProtocol

    def __init__(self, **kwargs):
        """Take usernames as kwargs."""
        self.users = kwargs

    def getUser(self, user):
        """
        By allowing getUser to return a Deferred, we make it easier for the data to be retrieved 
        asynchronously (i.e from a db) so that the CPU can be used for other tasks in the meanwhile.
        First ex is basic non-blocking. Second is non-blocking web call.
        """
        return defer.succeed(self.users.get(user, "No such user"))
        # return client.getPage(self.prefix+user)

""" 
An endpoint is a Twisted concept that encapsulates one end of a connection. There are different endpoints for clients and servers.
we ask Twisted to create a TCP endpoint for a server using the string "tcp:1079". That, along with the call to serverFromString, 
tells Twisted to look for a TCP endpoint, and pass it the port 1079. The endpoint returned from that function can then have the listen() 
method invoked on it, which causes Twisted to start listening on port 1079.
"""
fingerEndpoint = endpoints.serverFromString(reactor, "tcp:1079")
"""
For each request, the reactor calls the factory’s buildProtocol method, which in this case causes FingerProtocol to be instantiated. 
Since the protocol defined here does not actually respond to any events, connections to 1079 will be accepted, but the input ignored.
"""
fingerEndpoint.listen(FingerFactory(moshez='Happy and well')))
# fingerEndpoint.listen(FingerFactory(prefix='http://livejournal.com/~'))

"""
Reactor is Twisted’s main event loop, similar to the main loop in other toolkits available in Python  (Qt, wx, and Gtk). 
There is exactly one reactor in any running Twisted application. Once started it loops over and over again, 
responding to network events and making scheduled calls to code. There's more than one reactor.
"""
reactor.run()