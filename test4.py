print("========== 메뉴 ==========")

print("PUSH : 1")

print("POP : 2")

print("SHOW : 3")

print("(종료 하려면 1,2,3 이외의 수 입력)")

stack=[]

Menu=int(input("메뉴를 선택하세요 : ")) # 문자열이 아닌 다른 자료형을 입려 받게 하고싶다면 input앞에 원하는 자료형 적기 (x.input("abcd"))

if Menu==1:

stack.append(Menu)

elif Menu==2:

stack.pop()

elif Menu==3:

print(stack)

else:

print("========== 스택 프로그램을 종료합니다 ==========")