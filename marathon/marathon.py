submit = True
output_file_name = 'out.txt'
result = []

if submit:
    print(''.join(map(str, result)))
else:
    outf = open(output_file_name, 'w')
    print(''.join(result), file = outf)
