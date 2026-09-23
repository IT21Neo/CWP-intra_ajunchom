import sys

def shrink(text):
    print(text[0:8])

def enlarge(text):
    missing_length = 8 - len(text)
    print(text + ('Z' * missing_length))

if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)