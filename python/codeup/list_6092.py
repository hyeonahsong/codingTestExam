# 6092 ~

if __name__ == '__main__':
# 92.출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자. (6092)
#     n = int(input())
#     num = input().split()
#
#     list_01 = num
#     list_00 = []
#
#     for i in range(0, 23):
#         list_00.append(0)
#
#
#     for i in range(0, len(list_01)):
#         list_00[int(list_01[i]) - 1] += 1
#
#
#     for i in range(0, len(list_00)):
#         print(list_00[i], end = ' ')





    # 93. 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자. (6093)
    # n = int(input())
    # num = input().split()
    # num_list = num
    #
    # for i in range(n-1, -1, -1):
    #     print(num_list[i], end = ' ')





    # 94. 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력(6094)
    # n = int(input())
    # num = input().split()
    #
    # for i in range(n):
    #     num[i] = int(num[i])
    #
    # print(min(num))



    # 6094번 리팩토링
    # n = int ( input ())
    # num = map ( int , input ().split())
    #
    # print(min(num))





    # 95. 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.(6095)
    # n = int(input())
    # list_01 = []
    #
    #
    # for i in range(20):
    #     list_01.append([])
    #     for j in range(20):
    #         list_01[i].append(0)
    #
    #
    # for i in range(n):
    #     x, y = map(int, input().split())
    #     list_01[x][y] = 1
    #
    #
    # for i in range(1, 20):
    #     for j in range(1, 20):
    #         print(list_01[i][j], end = ' ')
    #     print()





    # 96.바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때, n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력??(6096)
    badukpan = []

    for i in range(19):
        badukpan.append([])
        for j in range(19):
            badukpan[i].append(0)


    for i in range(19):
        badukpan[i] = list(map(int, input().split()))



    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        for j in range(1, 20):
            if badukpan[x][j] == 0:
                badukpan[x][j] = 1

            else:
                badukpan[x][j] = 0

            if badukpan[j][y] == 0:
                badukpan[j][y] = 1

            else:
                badukpan[j][y] = 0


    for i in range(19):
        for j in range(19):
            print(badukpan[i][j], end = ' ')
        print()

