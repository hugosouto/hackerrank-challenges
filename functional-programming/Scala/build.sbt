// Define the Scala version used
scalaVersion := "3.3.1" // Updated to Scala 3.3.1

// Project name
name := "ScalaHackerRankSolutions"

// Version of your project
version := "0.1"

// Organization (Optional)
organization := "com.yourname"

// Add additional libraries here if needed
libraryDependencies ++= Seq(
  // ScalaTest for unit testing, ensure compatibility with Scala 3
  "org.scalatest" %% "scalatest" % "3.2.10" % Test,
  // Add other dependencies as required
)

// Enable the ScalaTest plugin for sbt
testFrameworks += new TestFramework("org.scalatest.tools.Framework")
