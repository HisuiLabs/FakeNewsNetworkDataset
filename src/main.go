package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
)

func main() {
	file, err := os.Open("data/label.tsv")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	r := csv.NewReader(file)
	r.Comma = '\t'
	r.LazyQuotes = true

	var line []string
	for {
		line, err = r.Read() // 1行読み出し
		if err == io.EOF {
			break
		} else if err != nil {
			fmt.Println("読み込みエラー: ", line)
			panic(err)
		}
		fmt.Println(line[2], line[3])
	}
}
