def test1():
    """1번 실습문제 풀이"""
    import math
    num = float(input('값: '))
    print(f'출력: {round(num)}(반올림), {math.ceil(num)}(올림), {math.floor(num)}(버림)')
# test1()

def test2():
    """2번 실습문제 풀이"""
    a, b = map(int, input('입력:').split())
    # if a == b:
    #     print('True')
    # else:
    #     print('False')
    print('True' if a == b else 'False')
# test2()

def test3():
    """3번 실습문제 풀이"""
    num = int(input('입력:'))
    # if num <= 100 and num >= 10:
    #     print('True')
    # else:
    #     print('False')
    print('True' if 100 >= num >= 10 else 'False')
# test3()

def test4():
    """4번 실습문제 풀이"""
    a = float(input('입력:'))     # 3.14
    b = round(a)                 # 3
    # if a <= b:
    #     print('True')
    # else:
    #     print('False')
    print('True' if a <= b else 'False')
# test4()

def test5():
    """5번 실습문제 풀이"""
    import math
    num = float(input('입력:'))
    quest1 = math.ceil(num) < 10
    quest2 = math.floor(num) >= 5
    result = quest1 and quest2
    print(result)
# test5()

def test6():
    """6번 실습문제 풀이"""
    import math
    a, b = map(float, input('입력:').split())
    quest1 = a > b
    quest2 = round(a) > math.floor(b)
    result = quest1 or quest2
    print(result)
# test6()

def test7():
    """7번 실습문제 풀이"""
    import math
    num = float(input('입력:'))
    # if math.ceil(num) % 2 == 0 and round(num) <= 10:
    #     print('True')
    # else:
    #     print('False')
    print('True' if math.ceil(num) % 2 == 0 and round(num) <= 10 else 'False')
# test7()

def test8():
    """8번 실습문제 풀이"""
    import math
    num = float(input('입력:'))
    num1 = math.floor(num)
    num2 = round(num)
    num3 = math.ceil(num)
    # if num1 > num2:
    #     if num1 > num3:
    #         print(num1)
    #     else:
    #         print(num3)
    # else:
    #     if num2 > num3:
    #         print(num2)
    #     else:
    #         print(num3)
    print(max(num1, num2, num3))
# test8()

def test9():
    """9번 실습문제 풀이"""
    import math
    num = float(input('입력:'))
    quest1 = round(num) % 5 == 0
    quest2 = math.ceil(num) % 2 == 0
    result = quest1 or quest2
    # if result == True:
    #     print('조건 만족')
    # else:
    #     print('조건 불만족')
    print('조건 만족' if result else '조건 불만족')
# test9()

def test10():
    """10번 실습문제 풀이"""
    import math
    a, b = map(float, input('입력:').split())
    quest1 = round(a) <= round(b)
    quest2 = math.ceil(a) > math.floor(b)
    result = quest1 and quest2
    # if result == True:
    #     print('조건 만족')
    # else:
    #     print('조건 불만족')
    print('조건 만족' if result else '조건 불만족')
# test10()