# 6032 ~ 6041, 6043 ~

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
    # num_01, num_02, num_03 = input().split()
    # num_list = [int(num_01), int(num_02), int(num_03)]
    #
    # sum_val = sum(num_list)
    # avg_val = sum_val / len(num_list)
    #
    # print(sum_val, format(avg_val, '.2f'))



    # 46. 정수 1개를 입력받아 2배 곱해 출력(6046)
    # num_01 = input()
    # print(int(num_01) << 1)



    # 47. 정수 2개(a, b)를 입력받아 a를 2 b 배 곱한 값으로 출력(6047)
    # a, b = input().split()
    # print(int(a) << int(b))



    # 48. 두 정수(a, b)를 입력받아 a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력(6048)
    # a, b = input().split()
    # print(int(a) < int( b))



    # 49. 두 정수(a, b)를 입력받아 a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력(6049)
    # a, b = input().split()
    # print(int(a) == int(b))



    # 50. 두 정수(a, b)를 입력받아 b의 값이 a의 값 보다 크거나 같으면 True 를, 같지 않으면 False 를 출력
    # a, b = input().split()
    # print(int(a) <= int(b))



    # 51. 두 정수(a, b)를 입력받아 a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력(6051)
    # a, b = input().split()
    # print(int(a) != int(b))



    # 52. 정수가 입력되었을 때, True/False 로 평가(6052)
    # num_01 = int(input())
    # print(bool(num_01))



    # 53. 정수값이 입력될 때, 그 불 값을 반대로 출력(6053)
    # num_01 = bool(int(input()))
    # print(not num_01)



    # 54. 2개의 정수값이 입력될 때, 그 불 값이 모두 True 일 때에만 True 를 출력(6054)
    # num_01, num_02 = input().split()
    # print(bool(int(num_01)) and bool(int(num_02)))



    # 55. 2개의 정수값이 입력될 때, 그 불 값이 하나라도 True 일 때에만 True 를 출력(6055)
    # num_01, num_02 = input().split()
    # print(bool(int(num_01)) or bool(int(num_02)))



    # 56. 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력(6056)
    # num_01, num_02 = input().split()
    # a = bool(int(num_01)) and not(bool(int(num_02)))
    # b = not(bool(int(num_01))) and bool(int(num_02))
    #
    # print(a or b)



    # 57. 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력(6057)
    # num_01, num_02 = input().split()
    # a =bool(int(num_01)) and bool(int(num_02))
    # b = (not(bool(int(num_01)))) and not(bool(int(num_02)))
    #
    # print(a or b)



    # 58. 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력(6058)
    # num_01, num_02 = input().split()
    # print(not(bool(int(num_01))) and not(bool(int(num_02))))



    # 59.입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력(6059)
    num_01 = int(input())
    print(~num_01)