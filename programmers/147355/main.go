package main

import "strconv"

// 코딩테스트 연습 > 연습문제 > 크기가 작은 부분문자열
/*
	제안사항
	- 1 ≤ p의 길이 ≤ 18
	- p의 길이 ≤ t의 길이 ≤ 10,000
	- t와 p는 숫자로만 이루어진 문자열이며, 0으로 시작하지 않습니다.

	고민!
	- 알고리즘 테스트 문제의 경우에도 입력값에 대한 검증을 하는 것이 좋을까?

	학습!
	- strconv 패키지의 문자열 변환 함수에 대하여 학습
*/
func solution(t string, p string) int {
	result := 0

	pNumber, _ := strconv.Atoi(p)

	for i := 0; i <= len(t)-len(p); i++ {
		sub := t[i : i+len(p)]
		subNumber, _ := strconv.Atoi(sub)

		if subNumber <= pNumber {
			result++
		}
	}

	return result
}
