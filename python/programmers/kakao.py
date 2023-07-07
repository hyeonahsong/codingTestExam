# 카카오 문제

# 2023 KAKAO BLIND RECRUITMENT
    # 〉 개인정보 수집 유효기간
def solution(today, terms, privacies):
    answer = []
    today_split_list =today.split('.')


    for i in range(0, len(privacies)):
        privacies_split_list = privacies[i].split()

        for line_terms in terms:
            terms_split_list = line_terms.split()

            if privacies_split_list[1] in terms_split_list:
                privacies_date = privacies_split_list[0].split('.')

                month = int(privacies_date[1]) + int(terms_split_list[1])
                if month > 12:
                    privacies_date[0] = int(privacies_date[0]) + 1
                    privacies_date[1] = month - 12

                elif month < 10:
                    privacies_date[1] ='0' + str(month)

                else:
                    privacies_date[1] = month


                if (int(privacies_date[0]) < int(today_split_list[0])) or (int(privacies_date[0]) == int(today_split_list[0]) and int(privacies_date[1]) <= int(today_split_list[1]) and int(privacies_date[2]) <= int(today_split_list[2])):
                    answer.append(i + 1)


    return answer





# 정확도 올리기 위해 연구 중
def solution_01(today, terms, privacies):
    answer = []
    today_split_list = today.split('.')


    for i in range(0, len(privacies)):
        privacies_split_list = privacies[i].split()

        for line_terms in terms:
            terms_split_list = line_terms.split()

            if privacies_split_list[1] in terms_split_list:
                privacies_date = privacies_split_list[0].split('.')

                month = int(privacies_date[1]) + int(terms_split_list[1])
                if month > 12:
                    privacies_date[0] = int(privacies_date[0]) + 1
                    privacies_date[1] = month - 12

                elif month < 10:
                    privacies_date[1] ='0' + str(month)

                else:
                    privacies_date[1] = month


                if int(privacies_date[0]) < int(today_split_list[0]):
                    answer.append(i + 1)

                if int(privacies_date[0]) == int(today_split_list[0]):
                    if int(privacies_date[1]) <= int(today_split_list[1]):
                        if int(privacies_date[2]) <= int(today_split_list[2]):
                            answer.append(i + 1)

    return answer






def solution_02(today, terms, privacies):
    answer = []
    today_split_list =today.split('.')


    for i in range(0, len(privacies)):
        privacies_split_list = privacies[i].split()

        for line_terms in terms:
            terms_split_list = line_terms.split()

            if privacies_split_list[1] in terms_split_list:
                privacies_date = privacies_split_list[0].split('.')

                month = int(privacies_date[1]) + int(terms_split_list[1])
                if month < 10:
                    privacies_date[1] ='0' + str(month)

                elif month >= 10 and month <= 12:
                    privacies_date[1] = month

                month_range = 12
                plus_year = 1
                while month_range <= 100:
                    if month > month_range and month <= month_range * 2:
                        privacies_date[0] = int(privacies_date[0]) + plus_year
                        privacies_date[1] = month - month_range * plus_year

                    month_range += 12
                    plus_year += 1


                if (int(privacies_date[0]) < int(today_split_list[0])) or (int(privacies_date[0]) == int(today_split_list[0]) and int(privacies_date[1]) <= int(today_split_list[1]) and int(privacies_date[2]) <= int(today_split_list[2])):
                    answer.append(i + 1)


    return answer







if __name__ == '__main__':
    today_01 = "2022.05.19"
    terms_01 = ["A 6", "B 12", "C 3"]
    privacies_01 = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

    today_02 = "2020.01.01"
    terms_02 = ["Z 3", "D 5"]
    privacies_02 = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

    # 내가 만든 예
    today_03 = "2000.07.14"
    terms_03 = ["A 2", "B 3", "C 30", "D 90"]
    privacies_03 = ["2000.07.14 A", "2000.07.14 B", "1900.07.14 C", "1990.07.14 D"]


    # solution(today_01, terms_01, privacies_01)
    # print(solution_02(today_02, terms_02, privacies_02))
    solution_02(today_03, terms_03, privacies_03)
