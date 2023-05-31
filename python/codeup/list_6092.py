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
#         # 2차원 배열 생성 후 0 넣기
#     badukpan = []
#
#     for i in range(19):
#         badukpan.append([])
#         for j in range(19):
#             badukpan[i].append(0)
#
#
#
#     # 입력받은 값을 리스트 형태로 저장
#     for i in range(19):
#         badukpan[i] = list( map( int, input().split()))
#
#
#
#     # 횟수 입력받아 그만큼 좌표 입력 후 뒤집기
#     n = int(input())
#
#     for i in range(n):
#         x, y = map( int, input().split())
#         for j in range (19):
#             if badukpan[x - 1][j] == 0:
#                 badukpan[x - 1][j] = 1
#             else:
#                 badukpan[x - 1][j] = 0
#
#             if  badukpan[j][y - 1] == 0:
#                 badukpan[j][y - 1] = 1
#             else :
#                 badukpan[j][y - 1] = 0
#
# # badukpan은 배열로 만들어져있으니 입력받은 x, y 좌표에 -1을 해서 위치를 잡는 게 맞음!
#
#
#
#     # 출력
#     for i in range(19):
#         for j in range(19):
#             print(badukpan[i][j], end = ' ')
#         print()





    # 97. 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l), 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# # 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때, 격자판을 채운 막대의 모양을 출력(6097)
#     h, w = map(int, input().split())
#
#     # 0이 들어간 판 배열 생성
#     pan_list = []
#     for i in range(h):
#         pan_list.append([])
#         for j in range(w):
#             pan_list[i].append(0)
#
#
#
#     # 입력받은 정보에 맞게 막대 부분 1로 할당해주기
#     n = int(input())
#
#     for i in range(n):
#         l, d, x, y = map(int, input().split())
#         for j in range(l):
#             if d == 0:
#                 pan_list[x - 1][y - 1 + j] = 1
#             else:
#                 pan_list[x - 1 + j][y - 1] = 1
#
#
#
#     # 출력
#     for i in range(h):
#         for j in range(w):
#             print(pan_list[i][j], end = ' ')
#         print()





# 98. 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고, 먹이가 2로 주어질 때,
# 성실한 개미의 이동 경로를 예상해보자. 개미는 (2, 2)에서 출발한다.(6098)
    ants = []

    for i in range(10):
        ants.append([])
        for j in range(10):
            ants[i].append(0)



    # 개미굴 상황 입력받아 배열에 넣기
    for i in range(10):
        ant = list(map(int, input().split()))
        for j in range(10):
            ants[i] = ant



    # 상황에 맞게 이동 경로 표시하기
    x, y = 1, 1

    while True:
        if ants[x][y] == 0:
            ants[x][y] = 9

        elif ants[x][y] == 2:
            ants[x][y] = 9
            break

        if ants[x][y+1] == 1 and ants[x+1][y] == 1:
            break

        if ants[x][y+1] != 1:
            y += 1


        elif ants[x+1][y] != 1:
            x += 1



    # 출력
    for i in range(10):
        for j in range(10):
            print(ants[i][j], end = ' ')
        print()



        # 개미굴 형태 만들고 상황 입력받아 넣는 코드를 아래 코드로 리팩토링
    for i in range(10):
        ants.append(list(map(int, input().split())))