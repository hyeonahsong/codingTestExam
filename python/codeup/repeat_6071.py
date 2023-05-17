# 6071 ~

if __name__ == '__main__':
    # 71. 임의의 정수가 줄을 바꿔 계속 입력된다. 단 개수는 알 수 없다. 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.(6071)
    # num_01 = 1
    #
    # while num_01 != 0:
    #     num_01 = int(input())
    #
    #     if num_01 != 0:
    #         print(num_01)




    # 72.정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력(6072)
    # num_01 = int(input())
    #
    # while num_01 != 0:
    #     print(num_01)
    #     num_01 -= 1



    # 73. 정수 하나가 입력되었을 때 0이될때까지 카운트다운 하여 출력(6073)
    # cnt = int(input()) -1
    #
    # while cnt != -1:
    #     print(cnt)
    #     cnt -= 1



    # 74. 영문 소문자(a ~ z) 1개가 입력되었을 때, a부터 그 문자까지의 알파벳을 순서대로 출력(6074)
    # char_01 = ord(input())
    # a_unicode = ord('a')
    #
    # while a_unicode <= char_01:
    #     print(chr(a_unicode), end = ' ')
    #     a_unicode += 1



    # 75. 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력(6075)
    # num_01 = int(input())
    # num_02 = 0
    #
    # while num_02 <= num_01:
    #     print(num_02)
    #     num_02 += 1



    # 76. 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력(6076)
    num_01 = int(input())

    for i in range(0, num_01 + 1):
        print(i)