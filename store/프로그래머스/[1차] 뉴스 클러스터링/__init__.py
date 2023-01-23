'''
[1차] 뉴스 클러스터링
입력으로는 str1과 str2의 두 문자열이 들어온다. 각 문자열의 길이는 2 이상, 1,000 이하이다.
입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 예를 들어 "ab+"가 입력으로 들어오면, "ab"만 다중집합의 원소로 삼고, "b+"는 버린다.
다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. "AB"와 "Ab", "ab"는 같은 원소로 취급한다.
'''

from collections import Counter


def solution(str1, str2):
    # 대소문자 통일
    str1_low = str1.lower()
    str2_low = str2.lower()

    str1_lst = []
    str2_lst = []

    # 알파벳 유효성 검사 후 다중집합 리스트에 추가
    for i in range(len(str1_low) - 1):
        if str1_low[i].isalpha() and str1_low[i + 1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i + 1])
    for j in range(len(str2_low) - 1):
        if str2_low[j].isalpha() and str2_low[j + 1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j + 1])

    # Counter 객체 => (key, value / 원소 값, 갯수)
    counter1 = Counter(str1_lst)
    counter2 = Counter(str2_lst)

    # 교집합, 합집합
    inter = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())

    # 자카드 유사도 계산
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)


if __name__ == '__main__':
    str1 = "FRANCE"
    str2 = "french"

    print(solution(str1, str2))
