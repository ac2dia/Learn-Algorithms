package main

// 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 타겟 넘버
/*
	제한사항
    - 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
    - 각 숫자는 1 이상 50 이하인 자연수입니다.
    - 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

	고민!
	-

	학습!
	-
*/
func solution(numbers []int, target int) int {
	root := numbers[0]

	answer := 0
	answer += dfs(root, 1, numbers, target)
	answer += dfs(-root, 1, numbers, target)

	return answer
}

func dfs(prev int, index int, numbers []int, target int) int {

	if len(numbers) <= index {
		if prev == target {
			return 1
		}
		return 0
	}

	left := prev - numbers[index]
	right := prev + numbers[index]

	ans := 0
	ans += dfs(left, index+1, numbers, target)
	ans += dfs(right, index+1, numbers, target)

	return ans
}
