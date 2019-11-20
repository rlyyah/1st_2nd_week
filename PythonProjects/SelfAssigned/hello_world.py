import sys

if len(sys.argv) > 1:
    print('hello ' + str(sys.argv[1]) + '!')
else:
    file_name = str(sys.argv[0]) 
    print(file_name[:11])



