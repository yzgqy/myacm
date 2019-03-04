import math
def get_distance(a,b):
    distance = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    if distance in buff:
        buff[distance].append((a, b))
    else:
        buff[distance] = [(a, b)]
    return distance

def judge_minimum(temp):
    global minimum
    global buff
    if temp not in buff:
        return minimum
    if minimum < temp:
            pass
    elif minimum == temp:
            for i in range(0, len(buff[temp])):
                closest_pair[minimum].append(buff[temp][i])
    else:
            minimum = temp
            closest_pair.clear()
            closest_pair[temp] = buff[temp][:]
    return minimum

def min_between(point, left, mid, right, minimum):
    global buff, closest_pair
    for i in range(left, mid):
        if abs(point[i][0]-point[mid][0]) <= minimum:
            for j in range(mid, right):
                if abs(point[i][0]-point[j][0]) <= minimum and abs(point[i][1]-point[j][1]) <= minimum:
                    get_distance(point[i], point[j])
    if len(buff) > 0:
        buff = sorted(buff.items(), key=lambda buff: buff[0])
        temp = buff[0][0]
        buff = dict(buff)
    else:
        temp = float("inf")
    return temp

def divide(point, left, right):
    global minimum, buff
    if right-left < 2:
        return float('inf')
    elif right-left == 2:
        return get_distance(point[left], point[left+1])
    else:
        mid = int((left+right)/2)
        min_left = divide(point, left, mid)
        minimum = judge_minimum(min_left)
        buff.clear()
        min_right = divide(point, mid, right)
        minimum = judge_minimum(min_right)
        buff.clear()
        temp = min_between(point, left, mid, right, minimum)
        minimum = judge_minimum(temp)
        buff.clear()
        return min(min_left, min_right, temp)

def isinteger(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

casenum=int(input())
list1=[]
for i in range(casenum):
    list1.append(input())

for j in range(len(list1)):
    point = []
    result = []
    arr = list1[j].split(",")
    for i in range(len(arr)):
        temp = arr[i].split()
        if (isinteger(temp[0]) == True):
            num1 = int(temp[0])
        else:
            num1 = float(temp[0])
        if (isinteger(temp[1]) == True):
            num2 = int(temp[1])
        else:
            num2 = float(temp[1])
        point.append((num1, num2))
    point.sort()
    buff = {}
    closest_pair = {}
    minimum = float("inf")
    divide(point, 0, len(point))
    for m in range(len(closest_pair[minimum])):
        tmp = closest_pair[minimum][m]
        result.append(tmp)
    result.sort()
    string = ""
    for i in range(len(result)):
        string += str(result[i][0]) + str(result[i][1])
    string = string.replace(',', '')
    string = string.replace('(', '')
    string = string.replace(')', ',')
    print(string[:-1])