# 프로그래머스 - 코딩기초트레이닝 Lv.0 문제


# 1. 문자열 정수의 합
# def solution(num_str):
#     list_01 = list(num_str)
#     sum = 0
#
#     for i in range(len(list_01)):
#         sum += int(list_01[i])
#
#     return sum





# 2. 부분문자열
def solution(str1, str2):
    if str1 in str2:
        return 1

    else:
        return 0






if __name__ == '__main__':
    # 1번
    # print(solution("123456789"))

    # 2번
    print(solution("abc", "aabcc"))
    print(solution("tbt", "tbbttb"))
