#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    leng = len(sys.argv) - 1

    if leng == 0:
        print('{} arguments.'.format(len(sys.argv) - 1))
    elif leng == 1:
        print('{} argument:'.format(len(sys.argv) - 1))
    else:
        print('{} arguments:'.format(len(sys.argv) - 1))

    for i in range(leng):
        print('{}: {}'.format((i + 1), sys.argv[i+1]))
