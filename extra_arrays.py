# Array inside an array:
original_array = [[1, 2, 3]]
original_array[0].append(7)
original_array.append([10, 11, 12])
print(original_array)

# Arrays Layouts:
for itens in [[1, 128, 1298039], [123388, 0, 2]]:
    print('{:>8} {:>8} {:>8}'.format(*itens))

array = [[1, 100, 1000], ["+", "-", "+"], [1, 2, 3], [2, 98, 1003]]
# Method 1 - By Hand:
print(
    f'{array[0][0]:>8}    {array[0][1]:>8}    {array[0][2]:>8}\n'
    f'{array[1][0]:<}{array[2][0]:>7}    {array[1][1]:<}{array[2][1]:>7}    {array[1][2]:<}{array[2][2]:>7}\n'
)

print(
    '{0:>8}    {1:>8}    {2:>8}\n'.format(array[0][0], array[0][1], array[0][2]),
    '{0:<}{1:>6}    {2:<}{3:>7}    {4:<}{5:>7}\n'.format(
        array[1][0], array[2][0],
        array[1][1], array[2][1],
        array[1][2], array[2][2])
)

# Method 2 - Using a 'While Loop':
i = 0
first_output = ""
second_output = ""
while i < len(array[0]):
    first_output += '{:>{width}}    '.format(array[0][i], width=8)
    second_output += '{:<}{:>{width}}    '.format(array[1][i], array[2][i], width=7)
    i += 1

print(f'{first_output}\n{second_output}')
