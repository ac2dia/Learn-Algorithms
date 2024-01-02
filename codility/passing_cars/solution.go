package solution

// you can also use imports, for example:
// import "fmt"
// import "os"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

func Solution(A []int) int {
    // Implement your solution here
    var totalOnes, count, currentOnes int

    for _, value := range A {
        if value == 1 {
            totalOnes++
        }
    }

    for _, value := range A {
        if value == 0 {
            count += totalOnes - currentOnes
            if count > 1000000000 {
                return -1
            }
        } else {
            currentOnes++
        }
    }

    return count
}

