print('This is a program for calculating the mixed volume and temperature of two water volumes depending on its temperature')

v1 = float(input('Enter the volume of first water in m3: '))
t1 = float(input('Enter the temperature of first water in celsius: '))
v2 = float(input('Enter the volume of second water in m3: '))
t2 = float(input('Enter the temperature of second water in celsius: '))

result_T = (v1 * t1 + v2 * t2) / (v1 + v2)
result_V = (v1 + v2)

print('This is the volume of mixed water - ', result_V, '\nThis is the temperature of mixed water - ', result_T )