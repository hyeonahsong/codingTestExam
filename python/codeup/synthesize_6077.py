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



    # 80. 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
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
#     주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산?(6083)
    # r, g, b = input().split()
    # r, g, b = int(r), int(g), int(b)
    #
    # for i in range(0, r):
    #     for j in range(0, g):
    #         for k in range(0, b):
    #             print(i, j, k)
    #
    # print(r * g * b)



    # 84.1초 동안 마이크로 소리강약을 체크하는 횟수를 h
# (헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)
#
# 한 번 체크한 값을 저장할 때 사용하는 비트수를 b
# (2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)
#
# 좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
# (모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)
#
# 녹음할 시간(초) s가 주어질 때, 필요한 저장 용량을 계산!(6084)
    # h, b, c, s = input().split()
    # h, b, c, s = int(h), int(b), int(c), int(s)
    #
    # print(round(h * b * c * s / 8 / 1024 / 1024, 1), "MB")



    # 85. 이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때, 압축하지 않고 저장하기 위해 필요한 저장 용량을 계산!(6085)
#     w, h, b = input().split()
#     res = int(w) * int(h) * int(b) / 1024 / 1024 / 8
#
#     print('%.2f' % res, "MB")




    # 86. 1, 2, 3 ... 을 순서대로 계속 더해 합을 만드는데, 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성(6086)
#     num_01 = int(input())
#     s = 0
#     i = 1
#
#     while True:
#         s = s + i
#
#         if num_01 <= s:
#             print(s)
#             break
#
#         else:
#             i += 1



# 6086번 리팩토링 코드
#     num_01 = int(input())
#     i = 0
#     s = 0
#
#     while True:
#         i += 1
#         s += i
#
#         if num_01 <= s:
#             print(s)
#             break



    # 87. 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되, 3의 배수인 경우는 출력하지 않도록 만들어보자. (6087)
    # num_01 = int(input())
    #
    # for i in range(1, num_01 + 1):
    #     if i % 3 == 0:
    #         pass
    #
    #     else:
    #         print(i, end = ' ')

# 문제 예시에서는 pass가 아닌 continue 사용했음.



# 88. 시작 값(a), 등차d), 몇 번째인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램을 만들어보자. (6088)
    a, d, n = input().split()
    a, d, n = int(a), int(d), int(n)
    i = 1
    s = a

    while True:
        if i == n:
            print(s)
            break

        else:
            i += 1
            s += d