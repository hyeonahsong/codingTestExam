# 6065 ~

if __name__ == '__main__':
    # 65.3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력(6065)
    # a, b, c = input().split()
    # a, b, c = int(a), int(b), int(c)
    #
    # if a % 2 == 0:
    #     print(a)
    #
    # if b % 2 == 0:
    #     print(b)
    #
    # if c % 2 == 0:
    #     print(c)



    # 66. 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력(6066)
    # a, b, c = input().split()
    # a, b, c = int(a), int(b), int(c)
    #
    # if a % 2:
    #     print('odd')
    # else:
    #     print('even')
    #
    # if b % 2:
    #     print('odd')
    # else:
    #     print('even')
    #
    # if c % 2:
    #     print('odd')
    # else:
    #     print('even')



#     67. 0이 아닌 정수 1개가 입력되었을 때 음수이면서 짝수이면, A, 음수이면서 홀수이면, B, 양수이면서 짝수이면, C, 양수이면서 홀수이면, D
# 를 출력(6067)
    num_01 = input()
    num_01 = int(num_01)

    if (num_01 < 0) and (num_01 % 2 == 0):
        print('A')

    if (num_01 < 0 )and (num_01 % 2 != 0):
        print('B')

    if (num_01 > 0) and (num_01 % 2 == 0):
        print('C')

    if (num_01 > 0) and (num_01 % 2 != 0):
        print('D')