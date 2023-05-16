# 6032 ~

if __name__ == '__main__':

# 32. 입력된 정수의 부호를 바꾸어 출력(6032)
# num_01 = int(input())
# print(-num_01)


# 33. 문자 1개를 입력받아 그 다음 문자를 출력(6033)
# num_01 = input()
# num_01 = ord(num_01) + 1
#
# print(chr(num_01))


# 34. 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력(6034)
# a, b = input().split()
# print(int(a) - int(b))


# 35. 실수 2개(f1, f2)를 입력받아 곱을 출력(6035)
#     f1, f2 = input().split()
#     print(float(f1) * float(f2))



    # 36. 단어와 반복 횟수를 입력받아 여러 번 출력(6036)
    # word, num = input().split()
    # print(word * int(num))



    # 37. 반복 횟수와 문장을 입력받아 여러 번 출력(6037)
    # num = input()
    # sentence = input()
    #
    # print(sentence * int(num))



    # 38. 정수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.(6038)
    # a, b = input().split()
    # print(int(a) ** int(b))



    # 39. 실수 2개(f1, f2)를 입력받아 f1을 f2번 거듭제곱한 값을 출력(6039)
    # f1, f2 = input().split()
    #
    # print(float(f1) ** float(f2))



    # 40. 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력(6040)
    #
    # a, b = input().split()
    # print(int(a) // int(b))



    # 41. 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력(6041)
    # a, b = input().split()
    # print(int(a) % int(b))



    # 43. 실수 2개(f1, f2)를 입력받아 f1 을 f2 로 나눈 값을 소숫점 넷째자리에서 반올림하여 소숫점 셋째 자리까지 출력(6043)
    # f1, f2 = input().split()
    # f3 = float(f1) / float(f2)
    #
    # print(format(f3, '.3f'))



    # 44. 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산 단, b는 0이 아니다.(6044)
    # a, b = input().split()
    #
    # print(int(a) + int(b))
    # print(int(a) - int(b))
    # print(int(a) * int(b))
    # print(int(a) // int(b))
    # print(int(a) % int(b))
    # print(format(int(a) / int(b), '.2f'))



    # 45. 정수 3개를 입력받아 합과 평균을 출력(6045)
    num_01, num_02, num_03 = input().split()
    num_list = [int(num_01), int(num_02), int(num_03)]

    sum_val = sum(num_list)
    avg_val = sum_val / len(num_list)

    print(sum_val, format(avg_val, '.2f'))