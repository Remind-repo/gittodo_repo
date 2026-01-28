import math

def test1(val):
    print(f"{round(val)} (반올림), {math.ceil(val)} (올림), {math.floor(val)} (버림)")

test1(3.3)
test1(3.7)

def test2():
    a, b = [float(k) for k in input().split(", ")]
    return a == b

print(test2())

def test3(val):
    print((10 <= val) and (val <= 100))

def test4(val):
    print(round(val) == 1)

def test5(val):
    return (round(val) < 10) and (5 <= math.floor(val))

def test6(val):
    a, b = [float(k) for k in input().split(" ")]
    print((b < a) or (math.floor(b) < round(a)))

def test7(val):
    res = math.ceil(val) % 2 == 0
    res = res and (round(val) < 10)
    print(res)

def test8(val):
    ls = []
    ls.append(math.floor(val))
    ls.append(round(val))
    ls.append(math.ceil(val))
    print(max(ls))

def test9():
    k = float(input())
    res = round(k) % 5 == 0
    res = res or (math.ceil(k) % 2 == 0)
    print("조건 만족" if res else "조건 불만족")

def test10():
    a, b = [float(k) for k in input().split(" ")]
    return (round(a) <= round(b)) and (math.floor(b) < math.ceil(a))