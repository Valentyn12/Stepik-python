n = int(input())
points = []
for i in range(n):
    s = input()
    s = s.split()
    points.append([int(s[0]),int(s[1])])
point1 = 0 ; point2 = 0 ; point3 = 0 ; point4 = 0

for i in points:
    x,y = i[0],i[1]
    if(x > 0 and y > 0) : point1 += 1
    if(x < 0 and y < 0) : point3 += 1
    if(x < 0 and y > 0) : point2 += 1
    if(x > 0 and y < 0) : point4 += 1

point = f'''Первая четверть: {point1}
Вторая четверть: {point2}
Третья четверть: {point3}
Четвертая четверть: {point4}
'''
print(point)