# 6092 ~

if __name__ == '__main__':
# 92.출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자. (6092)
    n = int(input())
    num = input().split()

    list_01 = num
    list_00 = []

    for i in range(0, 23):
        list_00.append(0)


    for i in range(0, len(list_01)):
        list_00[int(list_01[i]) - 1] += 1


    for i in range(0, len(list_00)):
        print(list_00[i], end = ' ')