import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.tux("Hello, " + sys.argv[1])