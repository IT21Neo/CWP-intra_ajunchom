import sys

if len(sys.argv) == 1:
    print("none")
else:
    params = sys.argv[1:]
    
    print("parameters: {}".format(len(params)))
    
    for param in params:
        print("{}: {}".format(param, len(param)))