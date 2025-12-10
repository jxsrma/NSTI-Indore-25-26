marks = {'a': 10, 'b': 25, 'c': 7}

max = -1
stud = ''

for keys,values in marks.items():
    if max < values:
        max = values
        stud = keys

print(stud,max)