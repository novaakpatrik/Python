import numpy
import re
from collections import Counter

data = numpy.loadtxt('matrix.txt')
print("matrix: \n" + str(data))
print("determinant: " + str(numpy.linalg.det(data)))
print("inverse matrix: \n" + str(numpy.linalg.inv(data)))


data = open('equation.txt', 'r')
re_equation = re.compile(r'(.*)[ ]*=[ ]*(.*)')
b = []
vars_values = []
equations = []
               
for line in data:
    equations.append(line)
    equation = re_equation.match(line)
    left = equation.group(1).split()
    right = int(equation.group(2))
    b.append(right)

    vars_ = Counter()
    number = 1
    sign = 1
    for word in left:
        if word.isnumeric():
            number = int(word)
        elif word == '-':
            sign = -1
        elif word == '+':
            sign = 1
        else:
            vars_[word] = sign*number
            number = 1
     
    vars_values.append(list(vars_.values()))

vars_names = list(vars_.keys())
a = numpy.array(vars_values)
res = numpy.linalg.solve(a,b)

print("\nequations: ")
for i in range(0, len(res)):
    print(equations[i])
    
print("\nsolution: ")
for i in range(0, len(res)):
    print("{}={:.2}\n".format(vars_names[i], res[i]))
    
data.close()
