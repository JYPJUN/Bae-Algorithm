angle = []

for i in range(3):
    angle.append(int(input()))

if angle.count(60) == 3:
    print('Equilateral')
elif sum(angle) == 180 and len(set(angle)) == 2:
    print('Isosceles')
elif sum(angle) == 180 and len(set(angle)) == 3:
    print('Scalene')
elif sum(angle) != 180:
    print('Error')