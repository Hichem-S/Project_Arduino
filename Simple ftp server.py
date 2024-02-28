









from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor 
from twisted.protocols.ftp import FTPFactory , FTPRealm


checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser('hiche', '12345')
checker.addUser("user" , "12345")
Portal = Portal (FTPRealm(".C:\Users\hiche\Desktop\Mycode") , [AllowAnonymousAccess()])
factory = FTPFactory (Portal)
reactor.listenTCP(21, factory)
reactor.run()



