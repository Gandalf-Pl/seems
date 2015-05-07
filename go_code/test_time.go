package main

import "time"
import "fmt"


/**
Timers are for when you want to do something once in the future.

Tickers are for when you want to do something repeatedly at regular intervals.
*/
func main() {
//    time.Sleep(100 * time.Millisecond)
//
//    timer := time.NewTimer(time.Second * 2)
//
//    go func() {
//        <- timer.C
//        println("Timer expired")
//    }()
//
//    stop := timer.Stop()
//    println("Timer cancelled:", stop)


//    ticker := time.NewTicker(time.Millisecond * 500)
//
//    go func() {
//        for t := range ticker.C {
//            fmt.Println("Tick at", t)
//        }
//    }()
//
//    time.Sleep(time.Millisecond * 1500)
//    ticker.Stop()
//    fmt.Println("Tricker stopped")

    timeChan := time.NewTimer(time.Second).C

    tickChan := time.NewTicker(time.Millisecond * 400).C

    doneChan := make(chan bool)

    go func() {
        time.Sleep(time.Second * 2)
        doneChan <- true
    }()

    for {
        select {
        case <- timeChan:
            fmt.Println("Time expired")
        case <- tickChan:
            fmt.Println("Ticked")
        case <- doneChan:
            fmt.Println("Done")
            return
        }
    }

//    year, month, day := time.Now().Date()
//
//    fmt.Println("year", year)
//    fmt.Println("month", month)
//    fmt.Println("day", day)

}
