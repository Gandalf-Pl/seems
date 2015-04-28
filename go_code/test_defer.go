package main
import "fmt"

/**
deferred function may read and assign to the returning function's named return values.
*/
func c() (i int) {
    defer func() { i++ }()
    return 1
}

/**
A deferred function's arguments are evaluated when the defer statement is evaluated.
*/
func a() {
    i := 0
    defer fmt.Println(i)
    i++
    return
}

/**
Deferred function calls are executed in Last In First Out order after_the surrounding function returns.
*/
func b() {
    for i := 0; i < 4; i++ {
        defer fmt.Print(i)
    }
}

func main() {
    i := c()
    fmt.Println("value is: ", i)
    a()
    b()
}
