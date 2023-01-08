package main

import "fmt"

func main() {
	prices := []int{7, 1, 5, 3, 6, 4}
	totalProfit := maxProfit(prices)

	fmt.Println(totalProfit)
}

func maxProfit(prices []int) int {

	totalProfit := 0
	for i := 1; i < len(prices); i++ {
		if prices[i] > prices[i-1] {
			totalProfit += prices[i] - prices[i-1]
		}
	}

	return totalProfit
}
