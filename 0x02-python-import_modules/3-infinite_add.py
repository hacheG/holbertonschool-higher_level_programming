#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv) - 1
    coun = 0

    for i in range(leng):
        coun = coun + int(sys.argv[i+1])

    print(coun)
