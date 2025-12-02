package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func partOne() int {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var startPos int = 50
	code := 0
	for scanner.Scan() {
		line := scanner.Text()
		dir := string(line[0])
		num, _ := strconv.Atoi(string(line[1:]))
		for num > 99 {
			num -= 100
		}
		switch dir {
		case "L":
			if (startPos - num) < 0 {
				startPos = 99 - (num - startPos - 1)
			} else {
				startPos -= num
			}
		case "R":
			if (startPos + num) > 99 {
				startPos = 0 + (num - (100 - startPos))
			} else {
				startPos += num
			}
		}
		if startPos == 0 {
			code++
		}
	}
	return code
}

func partTwo() int {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var startPos int = 50
	code := 0
	for scanner.Scan() {
		line := scanner.Text()
		dir := string(line[0])
		num, _ := strconv.Atoi(string(line[1:]))
		for num > 99 {
			num -= 100
			code += 1
		}
		switch dir {
		case "L":
			for i := 0; i<num; i++ {
				startPos--
				if startPos < 0 {
					startPos = 99
				}
				if startPos == 0 {
					code++
				}
			}
		case "R":
			for i := 0; i<num; i++ {
				startPos++
				if startPos > 99 {
					startPos = 0
				}
				if startPos == 0 {
					code++
				}
			}
		}
	}
	return code
}

func main() {
	fmt.Println(partOne())
	fmt.Println(partTwo())
}
