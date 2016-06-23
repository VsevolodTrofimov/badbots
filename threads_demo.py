import threading
import time

work = True

class TestThread ( threading.Thread ):

   def run ( self ):
      print "Hello, my name is", self.getName()
      while work:
      	print self.getName(), "working"
      	time.sleep(1.0)

cazaril = TestThread()
cazaril.setName ( "Cazaril" )
cazaril.start()

ista = TestThread()
ista.setName ( "Ista" )
ista.start()

time.sleep(5)
work = False