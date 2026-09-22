import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    search_string = sys.argv[2]

    matches = re.findall(keyword, search_string)
    
    if len(matches) > 0:
        print(len(matches))
    else:
        print("none")