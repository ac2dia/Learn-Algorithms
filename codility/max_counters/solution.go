package solution

// you can also use imports, for example:
// import "fmt"
// import "os"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

func Solution(N int, A []int) []int {
    // Implement your solution here
    count := make([]int, N)
    maxCount := 0
    lastUpdate := 0

    for _, v := range A {
        if N < v {
            lastUpdate = maxCount
        } else {
            if count[v-1] < lastUpdate {
                count[v-1] = lastUpdate
            }
            count[v-1]++
            if maxCount < count[v-1] {
                maxCount = count[v-1]
            }
        }
    }

    for i := range count {
        if count[i] < lastUpdate {
            count[i] = lastUpdate
        }
    }

    return count    
}

