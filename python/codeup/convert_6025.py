# 6024~

if __name__ == '__main__':

    # 25. 정수 2개를 입력받아 합 출력(6025)
    # num_01, num_02 = input().split()
    # num_03 = int(num_01) + int(num_02)
    #
    # print(num_03)



    # 26. 실수 2개를 입력받아 합 출력(6026)
    # num_01 = input()
    # num_02 = input()
    # num_03 = float(num_01) + float(num_02)
    #
    # print(num_03)



    # 27. 10진수를 입력받아 16진수(hexadecimal)로 출력(6027)
    # num_01 = input()
    # num_01 = int(num_01)
    #
    # print('%x' %num_01)


# 보통 아래처럼 hex() 함수 사용.
#     print(hex(num_01))
    # OUT
    # 0xff

    # print(hex(num_01)[2:])
    # OUT
    # ff



    # 28.  10진수를 입력받아 16진수 대문자로 출력(6028)
    # num_01 = input()
    # num_01 = int(num_01)
    #
    # print('%X' %num_01)



    # 29. 16진수를 입력받아 8진수(octal)로 출력(6029)
    num_01 = input()

    num_01 = int(num_01, 16)
    print('%o' %num_01)