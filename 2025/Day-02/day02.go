package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func partOne() int {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		os.Exit(1)
	}
	tot := 0
	for _, ids := range strings.Split(string(file), ",") {
		r := strings.Split(ids, "-")
		s, _ := strconv.Atoi(r[0])
		e, _ := strconv.Atoi(r[1])

		for i := s; i <= e; i++ {
			curId := strconv.Itoa(i)
			if len(curId)%2 != 0 {
				continue
			}
			half := (len(curId) / 2)
			a := ""
			b := ""
			if len(curId) == 2 {
				a = string(curId[0])
				b = string(curId[1])
			} else {
				a = string(curId[:half])
				b = string(curId[half:])
			}
			if a == b {
				tot += i
			}
		}
	}
	return tot
}

func toChunks(in string, l int) []string {
	nChunks := len(in) / l
	ret := make([]string, nChunks)
	for i := 0; i < nChunks; i++ {
		ret[i] = in[(l * i):(l*i + l)]
	}
	return ret
}

func allEqual(a []string) bool {
	for i := 1; i < len(a); i++ {
		if a[i] != a[0] {
			return false
		}
	}
	return true
}

func partTwo() int {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		os.Exit(1)
	}
	tot := 0
	for _, ids := range strings.Split(string(file), ",") {
		r := strings.Split(ids, "-")
		s, _ := strconv.Atoi(r[0])
		e, _ := strconv.Atoi(r[1])

		for i := s; i <= e; i++ {
			curId := strconv.Itoa(i)
			valid := 0
			for c := 1; c <= len(curId)/2; c++ {
				if len(curId)%c != 0{
					continue
				}
				chunks := toChunks(curId, c)
				if allEqual(chunks) {
					valid += 1
					break
				}
			}
			if valid != 0 {
				tot += i
			}
		}
	}
	return tot
}

func main() {
	fmt.Println(partOne())
	fmt.Println(partTwo())
}
