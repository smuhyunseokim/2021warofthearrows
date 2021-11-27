import random

num = random.sample(range(1,10), 4) # 1부터 9까지의 숫자를 4가지 랜덤으로 추출

print(num) # 임시 확인용

cn= 0  # 게임시도 횟수
st= 0  # 스트라이크 횟수
bl= 0  # 볼 횟수

while(st < 4):
    number = input("4자리 수가 랜덤 생성되었습니다. 4자리 수를 입력하세요: ") # 4자리수 입력
    if(number[0] == number[1] == number[2] == number[3]): # 오류방지용 코드
        print("같은 숫자를 입력하실수 없습니다")
    elif(number[0] == number[1] == number[2]):
        print("같은 숫자를 입력하실수 없습니다")
    elif(number[0] == number[1] == number[3]):
        print("같은 숫자를 입력하실수 없습니다")
    elif(number[0] == number[2] == number[3]):
        print("같은 숫자를 입력하실수 없습니다")
    elif(number[0] == number[1]):
        print("같은 숫자를 입력하실수 없습니다")
    elif(number[0] == number[2]):
        print("같은 숫자를 입력하실수 없습니다")
    elif(number[0] == number[3]):
        print("같은 숫자를 입력하실수 없습니다")
    elif(number[1] == number[2]):
        print("같은 숫자를 입력하실수 없습니다")
    elif(number[1] == number[3]):
        print("같은 숫자를 입력하실수 없습니다")
    elif (number[2] == number[3]):
        print("같은 숫자를 입력하실수 없습니다")

    else :
        pass

    st = 0
    bl = 0

    for i in range(0, 4): # 랜덤4자리수, 입력받은 4자리수 비교
        for j in range(0, 4):
            if(number[i] == str(num[j]) and i == j):
                st += 1
            elif(number[i] == str(num[j]) and i !=j):
                 bl += 1
    print(st, "스트라이크", bl, "볼") # 사용자에게 횟수 표시
    cn += 1 # 시도횟수 추가

print(cn, "번만에 정답") # 최종 정답시 횟수안내

