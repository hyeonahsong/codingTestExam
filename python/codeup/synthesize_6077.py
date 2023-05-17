# 6077 ~

if __name__ == '__main__':
    # 77. 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 출력(7077)
    num_01 = int(input())
    s = 0

    for i in range(0, num_01 + 1, 2):
        s += i

    print(s)