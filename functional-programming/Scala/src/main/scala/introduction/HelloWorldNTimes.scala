EasyProblem Solving (Basic)Max Score: 5Success Rate: 94.18%
Print 'hello world' n times.

/*
Challenge: Hello World N Times
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 5
Success Rate: 94.18%
Task: Print 'hello world' n times.
Link: https://www.hackerrank.com/challenges/fp-hello-world-n-times/problem
*/

// Main:
object Solution extends App {
// Solution:
def f(n: Int): Unit = {
  print("Hello World\n" * n)
}
// End of Solution
  var n = scala.io.StdIn.readInt()
  f(n)
}
