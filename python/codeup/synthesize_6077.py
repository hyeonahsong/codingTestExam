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
    n ,m = input().split()
    n , m = int(n), int(m)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(i, j)