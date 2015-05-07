package main

import (
	"container/list"
	"fmt"
)

func main() {
	// Create a new list and put some numbers in it.
	l := list.New()
	e4 := l.PushBack(4)
	e1 := l.PushFront(1)
	l.InsertBefore(3, e4)
	l.InsertAfter(2, e1)

	// Iterate through list and print its contents.
	for e := l.Back(); e != nil; e = e.Prev() {
		fmt.Println(e.Value)
	}
    fmt.Println("this is ----------------------------")
    for e := l.Front(); e != nil; e = e.Next() {
        fmt.Println(e.Value)
    }

}
