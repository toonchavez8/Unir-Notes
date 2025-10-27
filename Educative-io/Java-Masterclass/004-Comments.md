# Comments

In this lesson, we will learn to write explanatory comments within a Java program.

## Why Use comments[](https://www.educative.io/courses/java-masterclass-developers/comments#Why-use-comments)

Novice programmers tend to omit comments. But comments provide an opportunity for us to document our thoughts about what our program does and how it solves the problem at hand. Although comments are important to others who read our program, we should realize that they are useful to us, too. Typical programs are written over a period of time. What might be obvious to you today could be baffling next week.

```java
// Sample.java by F. M. Carrano
// Displays strings and provides an example of a Java application.
public class Sample
{
   public static void main(String[] args)
   {
      // Demonstrate println
      System.out.println("This string is displayed on one line.");
      System.out.println("This string appears on the second line.");
      System.out.println(); // The third line displayed is blank

      // Demonstrate print
      System.out.print("Four ");
      System.out.print("and twenty ");
      System.out.println("blackbirds");
      System.out.println("Baked in a pie.");
   } // End main
} // End Sample
```

## Single-line comments[#](https://www.educative.io/courses/java-masterclass-developers/comments#Single-line-comments)

The program given above showed one kind of Java comment: a line that begins with two slashes. We use this form of comments within the body of a program to describe the purpose of groups of statements, or to explain anything that is not obvious. Notice how we have divided the method `main` into two portions separated by a blank line. Each portion begins with a comment that indicates what the statements do. For example, the comment in **line 7** is

```Python
// Demonstrate println
```

Another way to use this kind of comment is at the end of another Java statement. For example, the comment in the statement

```Python
System.out.println(); // The third line displayed is blank
```

clarifies the purpose of that statement. We used this comment in **line 12** of the above program because it was the first time we saw this form of the `println` statement. Generally, we should omit comments that state the obvious. Of course, what is obvious to us might not be obvious to someone else. However, a comment such as the one in this statement

```Python
System.out.print("Four "); // Display "Four"
```

is obvious and should be omitted.

## Multi-line comments[](https://www.educative.io/courses/java-masterclass-developers/comments#Multi-line-comments)

When a comment spans several lines, we can **delimit** it (begin and end it) by using `/*` and `*/` like this:

```Python
/* This is another way to write

   a comment */
```

We usually do not use this form of comment for documenting our programs. However, during the development of a program, we might want to disable a group of statements temporarily. An easy way to do this without deleting the statements is to place `/*` before the group and `*/` after it.

A variant of this form of comment begins with `/**` and ends with `*/`. For example, the comment at the beginning of the above program could be written as follows:

```Python
/** Sample.java by F. M. Carrano

    Displays strings and provides an example of a Java application.

*/
```

We will use this form in our programs. A comment like this one can be processed by a utility program called `javadoc`, when it appears immediately before a class or method. This utility produces an HTML document that describes the classes and methods that use this form of comments. You can learn more about `javadoc` [here](https://www.oracle.com/technetwork/java/javase/documentation/index-jsp-135444.html).