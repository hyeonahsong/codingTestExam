# 6065 ~

if __name__ == '__main__':
    # 65.3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력(6065)
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    if a % 2 == 0:
        print(a)

    if b % 2 == 0:
        print(b)

    if c % 2 == 0:
        print(c)