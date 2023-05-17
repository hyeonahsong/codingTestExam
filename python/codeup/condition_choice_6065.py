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
#     num_01 = input()
#     num_01 = int(num_01)
#
#     if (num_01 < 0) and (num_01 % 2 == 0):
#         print('A')
#
#     if (num_01 < 0 )and (num_01 % 2 != 0):
#         print('B')
#
#     if (num_01 > 0) and (num_01 % 2 == 0):
#         print('C')
#
#     if (num_01 > 0) and (num_01 % 2 != 0):
#         print('D')



# 68. 점수(정수, 0 ~ 100)를 입력받아 90 ~ 100 : A, 70 ~ 89 : B, 40 ~ 69 : C, 0 ~ 39 : D를 출력(6068)
#     num_01 = int(input())
#
#     if(90 <= num_01) and (num_01 <= 100):
#         print('A')
#
#     if(70 <= num_01) and (num_01 <= 89):
#         print('B')
#
#     if (40 <= num_01) and (num_01 <= 69):
#         print('C')
#
#     if(0 <= num_01) and (num_01 <= 39):
#         print('D')



    # 69. 문자를 하나 입력받아 A : best!!!, B : good!!, C : run!, D : slowly~, 나머지 문자들 : what? 출력(6069)
    char_01 = input()

    if char_01 == 'A':
        print('best!!!')

    if char_01 == 'B':
        print('good!!')

    if char_01 == 'C' :
        print('run!')

    if char_01 == 'D' :
        print('slowly~')

    if (char_01 != 'A') and (char_01 != 'B') and (char_01 != 'C') and (char_01 != 'D'):
        print('what?')