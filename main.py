input_data = open('input.txt', 'r') 
data = input_data.read()
a1 = int(data[0])
a2 = int(data[1])
a3 = int(data[2])
b1 = int(data[3])
b2 = int(data[4])
b3 = int(data[5])
if a1 + a2 + a3 == b1 + b2 + b3:
    output_data = open('output.txt', 'w')
    output_data.write('YES')
else:
    output_data = open('output.txt', 'w')
    output_data.write('NO')