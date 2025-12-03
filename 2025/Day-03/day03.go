package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func partOne() int {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	tot := 0
	for scanner.Scan() {
		line := scanner.Text()
		splitLine := strings.Split(line, "")
		biggest := -1
		for i, n := range splitLine {
			for _, x := range splitLine[(i + 1):] {
				num, _ := strconv.Atoi((n + x))
				if num > biggest {
					biggest = num
				}
			}
		}
		tot += biggest
	}
	return tot
}

func findBiggest(nums []int, minLen int, start int) int {
	nums = nums[start:]
	max := 0
	for i, n := range nums {
		if len(nums)-(i+1) < minLen {
			break
		}
		if n > nums[max] {
			max = i
		}
	}
	return max + start
}

func partTwo() int {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	tot := 0
	for scanner.Scan() {
		line := scanner.Text()
		splitLine := strings.Split(line, "")
		nums := []int{}
		for _, s := range splitLine {
			i, _ := strconv.Atoi(s)
			nums = append(nums, i)
		}
		joltage := ""
		min := 0
		for i := 11; i >= 0; i-- {
			newBiggest := findBiggest(nums, i, min)
			joltage += strconv.Itoa(nums[newBiggest])
			min = newBiggest + 1
		}
		joltageInt, _ := strconv.Atoi(joltage)
		tot += joltageInt
	}
	return tot
}

func main() {
	fmt.Println(partOne())
	fmt.Println(partTwo())
}
