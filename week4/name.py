
import sys
# check fir
if len(sys.argv) < 2:
  sys.exit("too few arguments")
elif len(sys.argv) > 2:
  sys.exit("too few arguments")

print("hello my name is ", sys.argv[1])
