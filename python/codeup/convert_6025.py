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
    # num_01 = input()
    #
    # num_01 = int(num_01, 16)
    # print('%o' %num_01)



    # 30. 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력(6030)
# char = ord(input())
# print(char)



    # 31. 10진 정수 1개를 입력받아 유니코드 문자로 출력(6031)
    # num_01 = int(input())
    # print(chr(num_01))



    # 32. 입력된 정수의 부호를 바꾸어 출력(6032)
    # num_01 = int(input())
    # print(-num_01)



    # 33. 문자 1개를 입력받아 그 다음 문자를 출력(6033)
    num_01 = input()
    num_01 = ord(num_01) + 1

    print(chr(num_01))