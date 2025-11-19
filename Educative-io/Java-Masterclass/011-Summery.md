# Summary: A First Look at Java

In this lesson, we will summarize the main ideas presented in this chapter.

- An identifier is a word composed of letters, digits, the underscore (`_`), and/or the dollar sign (`＄`). It cannot begin with a digit. An uppercase letter is distinct from its lowercase counterpart.
- A reserved word is an identifier that has a special meaning in Java.
- We use a Java statement of the form `System.out.println(…)` to display text. The text is placed between the parentheses and enclosed in double quotes. Such text is called a string.
- When we use `println`, text is displayed and then an advance is made to the next line. If we use `print` instead of `println`, no advance to the next line occurs. A subsequent `print` or `println` places text on the same line.
- Comments are remarks that we place in a program to describe its purpose and methodology, or to clarify aspects of its logic. We can begin a comment with two slashes or enclose it between `/*` and `*/`. A third form that enables a program called `javadoc` to create HTML documentation, is to enclose the comment between `/**` and `*/`.
- Java’s data types are organized into two categories: primitive types and reference types. For now, we will focus on the primitive types `int`, `double`, `char`, and `boolean`, although other primitive types exist.
- A variable represents a piece of data stored in memory. An identifier names the variable.
- Before the first use of a variable, we declare its data type, but we do so only once. We then give it a value either by using an assignment statement or by reading data from the keyboard.
- When a variable appears within a `println` or `print` statement, its value is converted to a string that is displayed.
- The `+` operator joins, or concatenates, one string with another.
- An unnamed constant, or literal, has a value that is self-defined and does not change. A named constant, like a variable, has a declared data type and is assigned a value. However, it is tagged with `final` to ensure that its value does not change.
- We can read a value typed at the keyboard into a variable. The class `Scanner` provides the methods `nextInt` and `nextDouble` to read integers and real numbers.