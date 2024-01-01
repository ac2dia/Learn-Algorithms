package solution

// you can also use imports, for example:
// import "fmt"
// import "os"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

func Solution(X int, A []int) int {
    // Implement your solution here
    covered := make(map[int]bool)
    uncovered := X

    for i, position := range A {
        if position <= X && !covered[position] {
            covered[position] = true
            uncovered--
        }

        if uncovered == 0 {
            return i
        }
    }

    return -1
}
