<<<<<<< HEAD
"""
Boj2504. 괄호의 값
url: https://www.acmicpc.net/problem/2504
writer: Mingyu
Language: Python3
Date: 2021.02.22
Status: , Runtime:  ms, Memory Usage:  KB
"""

string = input()
stack = list()
 
for i in string:
 
    # ")"일 경우
    if i == ")":
        # 괄호를 수로 계산한 것을 담아둘 변수
        tmp = 0

        # 스택에 값이 존재한다면
        while stack:
            # 스택의 top을 가져온다.
            top = stack.pop()

            # top이 "("라면 현재 "()"가 성립되어 있는 상태. 즉 2가 도출된 상태이다
            if top == "(":
                # tmp가 0이라면 그냥 2를 넣어주고
                if tmp == 0:
                    stack.append(2)
                
                #tmp에 값이 있다면 ()를 감싸고 있는 다른 괄호가 있다는 것이다. 감싸는 경우에는 곱연산이므로 2*tmp.
                else:
                    stack.append(2 * tmp)

                # 값을 처리했으니 break한 후 다음 괄호를 확인한다.
                break

            # top이 "["라면 "[)"가 되어있는 상태. 올바르지 않은 괄호이므로 0을 출력한 후 프로그램을 종료
            elif top == "[":
                print("0")
                exit(0)

            # top이 숫자라면 tmp에 top을 더해준다. 시작되는 괄호이거나 연속된 괄호라는 의미가 된다.
            else:
                tmp += top
 
    # 위의 매커니즘과 동일
    elif i == "]":
        tmp = 0
 
        while stack:
            top = stack.pop()
            if top == "[":
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * tmp)
                break
            elif top == "(":
                print("0")
                exit(0)
            else:
                tmp += top
 
    else:
        stack.append(i)
 
# stack에 존재하는 수의 합
answer = 0
 
for i in stack:
    # 만일 괄호가 남아있다면 0을 출력 후 프로그램 종료
    if type(i) != int:
        print(0)
        exit(0)
    # 스택 내의 수를 합함
    else:
        answer += i
 
print(answer)

''' 주석 없는 코드

string = input()
stack = list()
 
for i in string:
    if i == ")":
        tmp = 0

        while stack:
            top = stack.pop()

            if top == "(":
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * tmp)
                break

            elif top == "[":
                print("0")
                exit(0)

            else:
                tmp += top
 
    elif i == "]":
        tmp = 0
 
        while stack:
            top = stack.pop()

            if top == "[":
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * tmp)
                break

            elif top == "(":
                print("0")
                exit(0)

            else:
                tmp += top
 
    else:
        stack.append(i)
 
answer = 0
 
for i in stack:
    if type(i) != int:
        print(0)
        exit(0)

    else:
        answer += i
 
print(answer)
=======
"""
Boj2504. 괄호의 값
url: https://www.acmicpc.net/problem/2504
writer: Mingyu
Language: Python3
Date: 2021.02.22
Status: , Runtime:  ms, Memory Usage:  KB
"""

string = input()
stack = list()
 
for i in string:
 
    # ")"일 경우
    if i == ")":
        # 괄호를 수로 계산한 것을 담아둘 변수
        tmp = 0

        # 스택에 값이 존재한다면
        while stack:
            # 스택의 top을 가져온다.
            top = stack.pop()

            # top이 "("라면 현재 "()"가 성립되어 있는 상태. 즉 2가 도출된 상태이다
            if top == "(":
                # tmp가 0이라면 그냥 2를 넣어주고
                if tmp == 0:
                    stack.append(2)
                
                #tmp에 값이 있다면 ()를 감싸고 있는 다른 괄호가 있다는 것이다. 감싸는 경우에는 곱연산이므로 2*tmp.
                else:
                    stack.append(2 * tmp)

                # 값을 처리했으니 break한 후 다음 괄호를 확인한다.
                break

            # top이 "["라면 "[)"가 되어있는 상태. 올바르지 않은 괄호이므로 0을 출력한 후 프로그램을 종료
            elif top == "[":
                print("0")
                exit(0)

            # top이 숫자라면 tmp에 top을 더해준다. 시작되는 괄호이거나 연속된 괄호라는 의미가 된다.
            else:
                tmp += top
 
    # 위의 매커니즘과 동일
    elif i == "]":
        tmp = 0
 
        while stack:
            top = stack.pop()
            if top == "[":
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * tmp)
                break
            elif top == "(":
                print("0")
                exit(0)
            else:
                tmp += top
 
    else:
        stack.append(i)
 
# stack에 존재하는 수의 합
answer = 0
 
for i in stack:
    # 만일 괄호가 남아있다면 0을 출력 후 프로그램 종료
    if type(i) != int:
        print(0)
        exit(0)
    # 스택 내의 수를 합함
    else:
        answer += i
 
print(answer)

''' 주석 없는 코드

string = input()
stack = list()
 
for i in string:
    if i == ")":
        tmp = 0

        while stack:
            top = stack.pop()

            if top == "(":
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * tmp)
                break

            elif top == "[":
                print("0")
                exit(0)

            else:
                tmp += top
 
    elif i == "]":
        tmp = 0
 
        while stack:
            top = stack.pop()

            if top == "[":
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * tmp)
                break

            elif top == "(":
                print("0")
                exit(0)

            else:
                tmp += top
 
    else:
        stack.append(i)
 
answer = 0
 
for i in stack:
    if type(i) != int:
        print(0)
        exit(0)

    else:
        answer += i
 
print(answer)
>>>>>>> e9cb03456e11cb14bf5d8fb8b196449990655e38
'''