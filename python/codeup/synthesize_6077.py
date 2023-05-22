# 6077 ~

if __name__ == '__main__':
    # 77. 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 출력(7077)
    # num_01 = int(input())
    # s = 0
    #
    # for i in range(0, num_01 + 1, 2):
    #     s += i
    #
    # print(s)



    # 78. 영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력(6078)
    # char_01 = 'a'
    #
    # while char_01 != 'q':
    #     char_01 = input()
    #     print(char_01)



    # 79. 1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만 계속 더하는 프로그램을 작성(6079)
    # num_01 = int(input())
    # s = 0
    #
    # for i in range(1, num_01):
    #     s = s + i
    #
    #     if num_01 <= s:
    #         print(i)
    #         break



#     80. 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
# 나올 수 있는 모든 경우를 출력(6080)
#     n ,m = input().split()
#     n , m = int(n), int(m)
#
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             print(i, j)



# 81. A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력!(6081)
#     num_01 = int(input(), 16)
#
#     for i in range(1,16):
#         print('%X' % num_01, '*%X' % i, '=%X' % (num_01 * i), sep = '')



# 82. 1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데, 3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다. (6082)
#     num_01 = int(input())
#
#     for i in range(1, num_01 + 1):
#         if (i % 10 == 3) or (i % 10 == 6) or (i % 10 == 9):
#             print('X', end = ' ')
#
#         else:
#             print(i, end = ' ')




# 83. 빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,
    주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산?(6083)
    r, g, b = input().split()
    r, g, b = int(r), int(g), int(b)

    for i in range(0, r):
        for j in range(0, g):
            for k in range(0, b):
                print(i, j, k)

    print(r * g * b)