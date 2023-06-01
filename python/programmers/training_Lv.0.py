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
# def solution(str1, str2):
#     if str1 in str2:
#         return 1
#
#     else:
#         return 0




# 3. n의 배수
# def solution(num, n):
#     if num % n == 0:
#         return 1
#
#     else:
#         return 0





# 4. 정수 찾기(조건문 활용)
# def solution(num_list, n):
#     return int(n in num_list)



# 5. 대문자로 바꾸기
# def solution(myString):
#     return myString.upper()








if __name__ == '__main__':
    # 1번
    # print(solution("123456789"))

    # 2번
    # print(solution("abc", "aabcc"))
    # print(solution("tbt", "tbbttb"))

    # 3번
    # print(solution(10, 2))
    # print(solution(10, 3))

    # 4번
    list_01 = [1, 3, 5]
    # print(solution(list_01, 3))
    # print(solution(list_01, 2))

    # 5번
    print(solution('str'))