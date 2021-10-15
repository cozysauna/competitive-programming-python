# ascending order by first argument, descending order by second argument
print(sorted(arr, key=lambda x: (x[0], -x[1])))