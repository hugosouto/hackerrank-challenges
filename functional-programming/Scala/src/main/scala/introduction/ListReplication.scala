
Max Score: Success Rate: 

/*
Challenge: List Replication
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 97.28%
Success Rate: 10
Task: Given a list, repeat each element of the list n times.
Problem: https://www.hackerrank.com/challenges/fp-list-replication/problem
*/

// Sample Input:
    // 3
    // 1
    // 2
    // 3
    // 4
// Sample Output:
    // 1
    // 1
    // 1
    // 2
    // 2
    // 2
    // 3
    // 3
    // 3
    // 4
    // 4
    // 4

// Solution:
def f(num:Int, arr:List[Int]):List[Int] = 
   arr.flatMap(List.fill(num)(_))

// Main:
object Solution extends App {
// Solution:
def f(num:Int, arr:List[Int]):List[Int] = {
}
