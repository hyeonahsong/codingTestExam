# 6009~

if __name__ == '__main__':

    # 9. 입력받은 문자 출력(6009)
    # char = input()
    # print(char)



    # 10.숫자 입력받아 int형ㅡ로 출력(6010)
    # num = input()
    # num = int(num)
    # print(num)



    # 11.실수 입력 받아 출력(6011)
    # num = input()
    # num = float(num)
    # print(num)



    # 12. 두 개의 정수를 입력받아 줄 바꾸어 출력(6012)
    # num_01 = input()
    # num_02 = input()
    #
    # num_01 = int(num_01)
    # num_02 = int(num_02)
    #
    # print(num_01)
    # print(num_02)



    # 13. 두 개의 문자를 입력받아 순서와 줄을 바꾸어 출력(6013)
    # char_01 = input()
    # char_02 = input()
    #
    # print(char_02)
    # print(char_01)



    # 14. 실수를 입력받아 줄 바꾸어 세 번 출력(6014)
    # num = input()
    # num = float(num)
    #
    # print(num)
    # print(num)
    # print(num)



    # 15. 공백을 두어 두 개의 정수를 입력받아 줄 바꾼 후 출력(6015)
    # num_01, num_02 = input().split()
    # num_01 = int(num_01)
    # num_02 = int(num_02)
    #
    # print(num_01)
    # print(num_02)



    # 16. 공백을 두어 두 개의 문자를 입력받아 순서를 바꾸어 출력(6016)
    # char_01, char_02 = input().split()
    # print(char_02, char_01)



    # 17. 정수, 실수, 문자, 문자열 등 하나만 입력받아 세 번 출력(6017)
    # str = input()
    # print(str, str, str)



    # 18. '시:분' 형태로 입력받아 그대로 출력
    # hour, minute = input().split(':')
    # print(hour, minute, sep = ':')



    # 19. '연도.월.일'을 입력받아 '일-월-연도' 형태로 바꾸어 출력(6019)
    # year, month, date = input().split('.')
    # print(date, month, year, sep = '-')



    # 20. '-'가 들어간 주민번호를 입력받아 '-'없이 출력(6020)
# numbers_01, numbers_02 = input().split('-')
# print(numbers_01, numbers_02, sep = '')
#
# 아래 방법도 동일한 결과지만 출제제자가 의도한 건 위 답안이었던 것 같음.
# print(numbers_01, numbers_02)



    # 21. 5개의 문자 혹은 숫자로 이루어진 문자열을 각 문자 별로 분리하여 한 줄씩 출력(6021)
    str = input()

    print(str[0])
    print(str[1])
    print(str[2])
    print(str[3])
    print(str[4])