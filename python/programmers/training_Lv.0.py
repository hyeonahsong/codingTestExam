# 프로그래머스 - 코딩기초트레이닝 Lv.0 문제


# 1. 문자열 정수의 합
def solution(num_str):
    list_01 = list(num_str)
    sum = 0

    for i in range(len(list_01)):
        sum += int(list_01[i])

    return sum



if __name__ == '__main__':
    print(solution("123456789"))