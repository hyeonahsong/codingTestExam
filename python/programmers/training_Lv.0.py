# 프로그래머스 - 코딩기초트레이닝 Lv.0 문제
from  math  import  prod


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





# 6. 문자열로 변환
# def solution(n):
#     return str(n)





# 7. 소문자로 변환
# def solution(myString):
#     return myString.lower()





# 8. 길이에 따른 연산(배열)
# def solution(num_list):
#     if len(num_list) >= 11:
#         return sum(num_list)
#
#     else:
#         mul_val = 1
#         for num in num_list:
#             mul_val *= num
#
#         return mul_val





# 8번 다른 풀이
# def solution(num_list):
#     return  sum ( l )  if  len ( l ) >= 11  else  reduce ( lambda  a , b :  a * b ,  l )
#
#
# def solution(num_list):
#     return  sum ( num_list )  if  len ( num_list ) >= 11  else  prod ( num_list )






# 9. 정수 부분 함수(메서드)
def solution(flo):
    return int(str(flo).split('.')[0])











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
    # print(solution('str'))

    # 6번
    # print(solution(3))

    # 7번
    # print(solution('ABC'))

    # 8번
    num_list = [1, 2, 3]
    # print(solution(num_list))

    # 9번

    print(solution(70.14))