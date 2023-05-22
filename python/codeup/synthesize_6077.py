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
    num_01 = int(input())
    s = 0

    for i in range(1, num_01):
        s = s + i

        if num_01 <= s:
            print(i)
            break