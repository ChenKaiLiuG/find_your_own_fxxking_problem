package main

import (
    "fmt"
    "os"
)

func main() {
    filename := "找找自己問題.txt"
    data, err := os.ReadFile(filename)
    if err != nil {
        fmt.Printf("無法讀取檔案 '%v': %v\n", filename, err)
    } else {
        fmt.Print(string(data))
    }
}
