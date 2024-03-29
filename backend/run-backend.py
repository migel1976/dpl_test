#import ipdb
import Ice, sys, os
import prctl, signal

if not 'topdir' in os.environ:
    raise Exception("no topdir specified in env")


Ice.loadSlice("--all -I. -I{ICE_SLICE_DIR} {top}/backend/backend.ice".format(ICE_SLICE_DIR = Ice.getSliceDir(), top = os.environ['topdir']))
import Hello

class HelloI(Hello.HelloIfc):

    def sayHello(self, current):
    	name='Hello world'
	return name

    def sayAloha(self, current):
	name='Aloha'
	return name
    #    print "Hello World!"
    #    return "Hello, World!"
    #
if __name__ == "__main__":
    # https://github.com/seveas/python-prctl -- prctl wrapper module
    # more on pdeathsignal: https://stackoverflow.com/questions/284325/how-to-make-child-process-die-after-parent-exits
    prctl.set_pdeathsig(signal.SIGTERM) # if parent dies this child will get SIGTERM

    with Ice.initialize() as communicator:
        xfn_fn = sys.argv[1]

        # server
        port = 0
        adapter = communicator.createObjectAdapterWithEndpoints("", "ws -p {port}".format(port = port))
        endpoints = adapter.getEndpoints()
        ep_s = endpoints[0].toString()
        print ep_s
        port = int(ep_s.split(" ")[2])
        print "running server at port", port
        xfn_fd = open(xfn_fn, "w+b")
        print >>xfn_fd, port
        xfn_fd.close()
        print "port assigned"
        sys.stdout.flush()

        adapter.add(HelloI(), Ice.stringToIdentity("hello"))
        adapter.activate()
        communicator.waitForShutdown()

