# 6092 ~

if __name__ == '__main__':
# 92.출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자. (6092)
#     n = int(input())
#     num = input().split()
#
#     list_01 = num
#     list_00 = []
#
#     for i in range(0, 23):
#         list_00.append(0)
#
#
#     for i in range(0, len(list_01)):
#         list_00[int(list_01[i]) - 1] += 1
#
#
#     for i in range(0, len(list_00)):
#         print(list_00[i], end = ' ')



    # 93. 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자. (6093)
    # n = int(input())
    # num = input().split()
    # num_list = num
    #
    # for i in range(n-1, -1, -1):
    #     print(num_list[i], end = ' ')



    # 94. 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력(6094)
    # n = int(input())
    # num = input().split()
    #
    # for i in range(n):
    #     num[i] = int(num[i])
    #
    # print(min(num))



    # 6094번 리팩토링
    n = int ( input ())
    num = map ( int , input ().split())

    print(min(num))