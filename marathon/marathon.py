DEBUG = True
output_file_name = 'out.txt'
input_file_name = 'in.txt'
result = []

# input data
if DEBUG:
    outf = open(output_file_name, 'w')
    with open(input_file_name) as inf:
        inf = inf.read().split('\n')
else:
    input()

# output data
if DEBUG:
    for e in result:
        outf.write(e+'\n')
    outf.close()
else:
    for e in result:
        print(e)