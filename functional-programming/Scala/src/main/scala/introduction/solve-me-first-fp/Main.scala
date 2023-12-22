/*
Challenge: Solve Me First FP
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 3
Success Rate: 97.81%
Task: Your task is to scan two numbers and print the sum.
Problem: https://www.hackerrank.com/challenges/fp-solve-me-first/problem?isFullScreen=true
*/

// Imports
import java.io.StringReader
import java.util.Scanner

// Simulate input from HackerRank
val raw_data = """2
3
"""
    // Expected Output:
    // 5

// Data
val input = new Scanner(new StringReader(raw_data))

// Function
object Solution {

    def main(args: Array[String]) {
        println(io.Source.stdin.getLines().take(2).map(_.toInt).sum)
    }
}
