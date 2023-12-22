/*
Challenge: Solve Me First FP
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 3
Success Rate: 97.81%
Task: This is a special challenge to make you familiar with IO.
Problem: https://www.hackerrank.com/challenges/[...]/problem
*/

// Imports
import java.io.StringReader
import java.util.Scanner

// Simulate input from HackerRank
val raw_data = """2
3
"""
// Expected Output:
// 

// Data
val input = new Scanner(new StringReader(raw_data))

// Function
object Solution {

    def main(args: Array[String]) {
        println(io.Source.stdin.getLines().take(2).map(_.toInt).sum)
    }
}