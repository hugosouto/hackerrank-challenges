/*
Challenge: Solve Me First FP
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 3
Success Rate: 97.81%
Task: Your task is to scan two numbers and print the sum.
Problem: https://www.hackerrank.com/challenges/fp-solve-me-first/problem
*/

package introduction

object Solution {
    def main(args: Array[String]): Unit = {
        println(io.Source.stdin.getLines().take(2).map(_.toInt).sum)
    }
}
