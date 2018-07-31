"""
A daemon is expected to adhere to certain behavioral standards so that standard tools can stop/start/query them. 
If a Twisted application is run via twistd, the TWISTed Daemonizer, all this behavioral stuff will be handled for you.

twistd -ny finger11.tac # just like before
twistd -y finger11.tac # daemonize, keep pid in twistd.pid
twistd -y finger11.tac --pidfile=finger.pid
twistd -y finger11.tac --rundir=/
twistd -y finger11.tac --chroot=/var
twistd -y finger11.tac -l /var/log/finger.log
twistd -y finger11.tac --syslog # just log to syslog
twistd -y finger11.tac --syslog --prefix=twistedfinger # use given prefix

Instead of using endpoints.serverFromString as in the above examples, here we are using its application-aware counterpart, strports.service. 
Notice that when it is instantiated, the application object itself does not reference either the protocol or the factory. 
Any services (such as the one we created with strports.service) which have the application as their parent will be started 
when the application is started by twistd. The application object is more useful for returning an object that supports the IService, 
IServiceCollection, IProcess, and sob.IPersistable interfaces with the given parameters. 
As the parent of the endpoint we opened, the application lets us manage the endpoint.

With the daemon running on the standard finger port, you can test it with the standard finger command: finger moshez .
"""

# Read username, output from non-empty factory, drop connections
# Use deferreds, to minimize synchronicity assumptions
# Write application. Save in 'finger.tpy'

from twisted.application import service, strports
from twisted.internet import protocol, reactor, defer
from twisted.protocols import basic

class FingerProtocol(basic.LineReceiver):
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
    protocol = FingerProtocol

    def __init__(self, **kwargs):
        self.users = kwargs

    def getUser(self, user):
        return defer.succeed(self.users.get(user, "No such user"))

application = service.Application('finger', uid=1, gid=1)
factory = FingerFactory(moshez='Happy and well')
strports.service("tcp:79", factory, reactor=reactor).setServiceParent(
    service.IServiceCollection(application))