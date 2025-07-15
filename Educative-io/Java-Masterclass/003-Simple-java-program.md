# A Simple Java Program

In this lesson, we will introduce you to terminology central to Java with the help of an example program that displays some text.

## Program: Display text[](https://www.educative.io/courses/java-masterclass-developers/a-simple-java-program#Program-Display-text)

Imagine that we want to write a Java application program to display some text. The program below is doing something similar. When it executes, this program will produce several lines of textual output that appear below the program. To execute this program, click the **Run** button.

```Java
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

## Overview[](https://www.educative.io/courses/java-masterclass-developers/a-simple-java-program#Overview)

We’ll use the previous Java program to give you a general overview of a Java application. Each line in the program is a **statement**. The initial statements in the program give descriptive information, including its purpose and author. Statements like these that begin with two slashes are called **comments** and are ignored by the compiler. That is, comments help the human reader of the program and are not directions to the computer. A comment can appear on its own line or at the end of another statement in the program. Soon we will see other ways to write comment statements. As we will also see, a statement can extend across more than one line.

Our example program contains the definition of a class named `Sample` that begins with the lines

```Java
public class sample{

}
```

The statements within this outer pair of braces that begin with the lines

```Java
public static void main(String[] args){}
```

define a **method** called `main`. Statements within this inner pair of braces are the **body** of the `main` method. Generally, a class contains several methods, each defining a specific task and each having a name of the programmer’s choosing. Every application program, however, must contain a method that is called `main`.

> [!summary] 
> You store the statements that define a class in their own file. The name of this file must be the name of the class followed by `.java`. For example, the file shown in the above program for the class `Sample` is named `Sample.java`.

## Identifiers[](https://www.educative.io/courses/java-masterclass-developers/a-simple-java-program#Identifiers)

Words within the program, such as `public` and `main`, are **identifiers**. An identifier in Java can consist of letters, digits, the underscore (`_`), and the dollar sign (`＄`), though it cannot begin with a digit. Identifiers are case sensitive, which means that Java considers uppercase letters and lowercase letters to be different letters. Thus, `result`, `Result`, and `RESULT` are three different identifiers. Using these identifiers in the same program would be confusing to others who read our program, so we should avoid doing so, even though it is legal.

Identifiers fall into one of three categories:

- Identifiers that we invent. The previous program has the identifiers `Sample` and `args` that we chose.
- Identifiers that another programmer has chosen. `System`, `out`, `println`, `print`, `main`, and `String` are examples of identifiers in this category. They were chosen by the designers of Java.
- Identifiers that are a part of the Java language. These identifiers are called **keywords**. Examples are `public`, `class`, `static`, and `void`. Since keywords have particular meanings within Java, we should not use them for another purpose. For this reason, keywords are said to be **reserved words**. Note that all reserved words use lowercase letters. The table given below and the [Appendix](https://www.educative.io/courses/java-masterclass-developers/reserved-words/) list Java’s reserved words. We will encounter other Java identifiers that technically are not keywords, but are reserved so that we cannot use them for other purposes. These identifiers appear in blue in the figure. We will discuss more about reserved words with other details of Java.

| Reserved     | java       | words      |
| ------------ | ---------- | ---------- |
| Abstract     | Assert     | Boolean    |
| Break        | Byte       | Case       |
| Catch        | Char       | Class      |
| Const        | Continue   | Default    |
| Do           | Double     | Else       |
| Enum         | Extends    | False      |
| Final        | Finally    | Float      |
| For          | Goto       | Implements |
| Import       | Instanceof | Int        |
| Interface    | Long       | Native     |
| New          | Null       | Package    |
| Private      | Protected  | Public     |
| Return       | Short      | Static     |
| Strict       | Super      | Switch     |
| Synchronized | This       | Throw      |
| Throws       | Transient  | True       |
| Try          | Void       | Volatile   |
| While        |            |            |

> [!note] 
>  `const` and `goto` are reserved, but are not used currently. Also, `true`, `false`, and `null` are not keywords but are actually literals as you will learn. Even so, they are reserved.

>  **Syntax: Identifiers**
> 
> An identifier is a word composed of letters, digits, the underscore ( _ ), and/or the dollar sign ( $ ). It cannot begin with a digit. An uppercase letter is distinct from its lowercase counterpart. The following are valid identifiers: `Sphere`, `salesTax`, `draft2`, and `FEET_PER_YARD`.

> 📝 **Note: Reserved words**
> 
> All reserved words in Java use only lowercase letters.

---

## Conventions[#](https://www.educative.io/courses/java-masterclass-developers/a-simple-java-program#Conventions)

Why do some of our identifiers begin with an uppercase letter, and why are some of the statements in our program indented? The Java language does not define details like this. Rather, programmers follow a **programming style** by convention. Not every programmer follows the same stylistic conventions, however. Often, such conventions are dictated by a programmer’s employer. The programming style that we use in this course was chosen in the interest of clarity and ease of learning Java.

The following figure points out the conventions that the program given above uses.

![[Pasted image 20250715133352.png]]

These conventions are

- Class names, such as `Sample`, begin with a capital letter.
- Method names, such as `main`, begin with a lowercase letter.
- Each brace is on its own line.
- The braces in a pair of open and close braces align.
- Each close brace is labeled with a comment to identify the portion of the program that it ends.
- Statements within a pair of braces are indented. We use a three-space indent, but two or four spaces are also reasonable as long as you are consistent.
- Blank lines are added to improve readability.

We will mention other conventions as we encounter them.

> [!summary] 
> Another common style places the open brace at the end of the line before the code being bracketed. For example, you could begin the class as follows: 
> ```Java
> public class Sample {
> 
>  public static void main(String[] args) {
>  ```
> 
> This style saves vertical space, which is important when viewing a program on a small screen. However, this style does not align the paired open and close braces. We much prefer to align our braces for clarity. You can align your braces and save vertical space by writing the open brace at the beginning of the first line to be bracketed. For example, using this style, the class would begin as follows:
>  ```java
>  public class Sample 
>     { public static void main(String[] args)
>  
>  ```

## White space[](https://www.educative.io/courses/java-masterclass-developers/a-simple-java-program#White-space)

The white areas in the above program are known as **white space** and are caused by

- Blank characters (spaces)
- Tabs
- New-line characters

The blanks that separate words are necessary for a program, but other white spaces that appear as indentations and new lines are there for people, not for the computer.

## Displaying text[](https://www.educative.io/courses/java-masterclass-developers/a-simple-java-program#Displaying-text)

We introduce two Java statements that we can use to display text.

### `System.out.println`[](https://www.educative.io/courses/java-masterclass-developers/a-simple-java-program#Systemoutprintln)

The above program displays text on the computer’s screen. Let’s focus on the statements that form the body of the method `main`.

The statement that begins with `System.out.println` displays one line of text. The identifier `println` means _print line_. Notice that the statement contains text, enclosed in double-quotes, and placed within a pair of parentheses. The text and quotes are a **string literal**. The text, but not the quotes, is displayed on the next line of the screen output. Thus, the statements

```java
System.out.println("This string is displayed on one line.");

System.out.println("This string appears on the second line.");

System.out.println(); // The third line is blank
```

display three lines of output, the last of which is blank.

Notice that each of these statements ends with a semicolon. This punctuation separates one statement from the next within the body of a method. Note the position of the semicolon in the third statement. If we placed it after the comment, it would become part of the comment. Since the compiler ignores comments, the statement would no longer have an ending semicolon, which is a syntax error.

### `System.out.print`[](https://www.educative.io/courses/java-masterclass-developers/a-simple-java-program#Systemoutprint)

When we use `println`, text is displayed and then an advance is made to the next line. If we use `print` instead of `println`, no advance to the next line occurs. Instead, a subsequent `print` or `println` would place text on the same line. For example, the statements

```java
System.out.print("Four ");

System.out.print("and twenty ");

System.out.println("blackbirds");

System.out.println("Baked in a pie.");

```

produce two lines of output:

```bash
Four and twenty blackbirds

Baked in a pie.

```

The second `print` statement begins where the first `print` left off, placing `and twenty` on the same line as `Four`. The first `println` statement begins where the second `print` ends, placing `blackbirds` on the same line as before, and then advances to the next line. Thus, the text in the last `println` displays on a new line.

Notice the blank characters at the end of the strings `"Four "` and `"and twenty "` in the program listing. we must include these to separate the words that are displayed. Java doesn’t insert spaces in output for us. We’ll learn more about using `println` and `print` statements later in this chapter.

> [!question] 
> Checkpoint question
> 
> Suppose that you want to display your name on one line, a row of dashes on the next line, and nothing on the third line. What `println` statements will do this? Write your answer in the black window below and click the RUN button to check it.
> ```java
> public class CheckpointQuestion 
> {
>    public static void main( String args[] ) 
>    {
>        // Write your answer here:
>         System.out.println("Miguel");
>         System.out.println("-------");
>         System.out.println();
>    } // End main
> } // End CheckpointQuestion
> ```