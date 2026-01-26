def func1():
    numbers = [5, 2, 9, 1, 7]
    numbers.append(3)
    numbers.sort()
    numbers.remove(len(numbers)-1)
    print(numbers[:len(numbers)-2])

def func2():
    info = ("Alice", 25, "Engineer")
    print(f"이름은 {info[0]}이고, 나이는 {info[1]}살이다.")

def func3():
    scores = {"Tom": 87, "Jane": 92, "Mike": 78}
    scores["Mike"] = 82
    scores["Lucy"] = 95
    print(sum(scores.values())/len(scores))

def func4():
    student1 = {"Python", "Math", "English"}
    student2 = {"Python", "Biology", "English"}
    print(student1.intersection(student2))
    print(student1.symmetric_difference(student2))
    print(student1.union(student2))

def func5():
    a = int(input("정수1 입력 : "))
    if a < 0:
        print("잘못 입력 하셨습니다. 프로그램을 종료합니다.")
        return
    b = int(input("정수2 입력 : "))
    if b < 0:
        print("잘못 입력 하셨습니다. 프로그램을 종료합니다.")
        return
    op = input("연산자 입력 (+ - * / %) : ")
    if not op in ["+", "-", "*", "/", "%"]:
        print("잘못 입력 하셨습니다. 프로그램을 종료합니다.")
        return
    print("---------------------------")
    match op:
        case "+":
            print(f"{a} + {b} = {a + b}")
        case "-":
            print(f"{a} - {b} = {a - b}")
        case "*":
            print(f"{a} * {b} = {a * b}")
        case "/":
            if b == 0:
                print("0으로 나눌 수 없습니다!")
                return
            print(f"{a} / {b} = {a / b}")
        case "%":
            if b == 0:
                print("0으로 나눌 수 없습니다!")
                return
            print(f"{a} % {b} = {a % b}")

def func6():
    w = int(input("체중입력(kg) : "))
    h = int(input("신장입력(cm) : "))
    print("--------------------------")
    BMI = w / h / h * 10000
    print(f"BMI 지수: {BMI:.2f}")
    if BMI < 18.5:
        print("저체중입니다.")
    elif BMI < 23:
        print("정상체중입니다.")
    elif BMI < 25:
        print("과체중입니다.")
    elif BMI < 30:
        print("비만입니다.")
    else:
        print("고도비만입니다.")

func6()