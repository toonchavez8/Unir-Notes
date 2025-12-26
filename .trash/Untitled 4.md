
# Variables

In this lesson, we will learn how to name pieces of data in our program.

## Why use variables[](https://www.educative.io/courses/java-masterclass-developers/variables#Why-use-variables)

**Variables** are used to represent a piece of data in a Java program. The variable represents a memory location that stores the data. The data itself is called the variable’s **value**.

We use an identifier to name a variable. By convention, variable names should:

- Begin with a lowercase letter
- Be meaningful

For example, if our variable represents the sales tax for a purchase, name it `salesTax` instead of `st` or `stax`.

Multiple-word variable names are common. By convention, the first word begins with a lowercase letter, but subsequent words in the name each begin with an uppercase letter.

> ✏️ **Programming Tip**
> 
> Java variable names can be long. Favor clarity over brevity. Avoid one-letter names unless the context suggests that they are appropriate. Follow convention by beginning variable names with a lowercase letter.

## Declarations[](https://www.educative.io/courses/java-masterclass-developers/variables#Declarations)

When we first create a variable, we must choose its data type. That is, we must specify what type of data the variable will represent. For example, if our program involves apples, we might track the number of apples in the variable `numberOfApples`. This count is an integer, so the data type of this variable would be `int`.

We declare the data type of a variable in a **declaration statement**. For example, the following statements declare one `int` variable, two `double variables`, a character variable, and a Boolean variable:

int numberOfApples;

double pricePerApple, totalCost;

char letter;

boolean done;

Each declaration begins with a data type and contains one or more variables of that type. Commas separate variables of the same type, and a semicolon ends each declaration.

> 📝 **Note: Variable declarations**
> 
> You must declare a variable before you can use it. You declare each variable only once, regardless of how often you use it.

## Assignments[](https://www.educative.io/courses/java-masterclass-developers/variables#Assignments)

When we declare a variable within the body of a method, Java gives it no particular initial value. We can either give an initial value to a variable or change the existing value of a variable by using an **assignment statement**. An assignment statement has the following form:

variable = expression ;

The **assignment operator** (`=`) assigns the value of the expression to the variable. An **operator** is a symbol within a programming language that represents a particular operation or action. For example, the operator `=` assigns a value to a variable, and the operator `*` multiplies two arithmetic values. An **expression** in a programming language is a combination of operators and other components that represent values. Both operators and expressions have various categories, as we will see.

> 📝 **Syntax: Assignment statement**
> 
> An assignment statement has the following form:
> 
> variable = expression ;
> 
> It assigns the value of _expression_

### Example[](https://www.educative.io/courses/java-masterclass-developers/variables#Example)

After the following declarations:

int numberOfApples;

double pricePerApple, totalCost;

We can assign values to the variables by writing statements such as these:

numberOfApples = 15;

pricePerApple = 0.29;

totalCost = numberOfApples * pricePerApple;

The `15` and `0.29` are called **literals**. We encountered this term in chapter [“A Simple Java Program”](https://www.educative.io/courses/java-masterclass-developers/a-simple-java-program#displaying-text) when we defined a string literal. Here we have an integer literal and a real literal. As we can see, a literal is the Java representation of a specific fixed value, rather than a value that results from a calculation.

The expression `numberOfApples * pricePerApple` is an example of an **arithmetic expression** that we will detail in the next chapter. The operator `*` multiplies the current values of the two variables in the expression. The resulting product is assigned to, or given to, the variable `totalCost`. That is, the value of `totalCost` becomes `4.35`, as the figure given below illustrates. These statements appear in a complete program in the next segment.

Depiction of an assignment statement before and after its execution

> 📝 **Note: Using variables**
> 
> Once you declare a variable and assign it a value, you can use it in another assignment statement.

## Declarations and assignments within a program[](https://www.educative.io/courses/java-masterclass-developers/variables#Declarations-and-assignments-within-a-program)

The program given below shows the two variable declarations and the three assignment statements given in the previous segment in the context of a Java program. This program computes the cost of a certain number of apples by multiplying their number by the cost of each one. The total cost then is displayed within a descriptive message. Click the RUN button and see the output for yourself.

Apples.java

Java

Ace Editor

Run

⋯

A demonstration of variables in a program

Note the use of the `+` operator in the previous program’s `print` statements. This is an aspect of Java that we have not seen previously. When used in this way, the `+` operator joins, or **concatenates**, one string with another. Although it appears that we are joining a number with a string, in fact, Java converts the number to a string of characters before displaying it. So by the time the `+` operator is considered, we really do have two strings that are joined together and then displayed.

### Strings spanning two or more lines[](https://www.educative.io/courses/java-masterclass-developers/variables#Strings-spanning-two-or-more-lines)

The previous program uses the following three statements to display one line of output:

System.out.print(numberOfApples + " apples at $");

System.out.print(pricePerApple + " apiece cost $");

System.out.println(totalCost);

Using several statements in this way is fine, but we could also write one `println` statement, as follows, and get the same output:

System.out.println(numberOfApples + " apples at $" +

············       pricePerApple + " apiece cost $" + totalCost);

Since this statement is long, we let it span more than one line. The compiler ignores the intervening white space, as long as it occurs before or after the `+` operator. We must be careful when a string literal must span two lines. For example, the following statement would produce a syntax error:

System.out.println("The total cost of 15 apples if bought

············        separately is $" + totalCost); // SYNTAX ERROR!

The correct way to divide a string literal is to break it into two string literals and then concatenate them, as follows:

System.out.println("The total cost of 15 apples if bought " +

············       "separately is $" + totalCost);

Note the additional quotes, the space after `bought`, and the additional `+` operator.

## Changing the value of a variable[](https://www.educative.io/courses/java-masterclass-developers/variables#Changing-the-value-of-a-variable)

Variables are so named because their values can vary. For example, we declared and initialized the variable `numberOfApples` in the previous examples, but we could change its value by writing

numberOfApples = 20;

Or we could add 1 to `numberOfApples` by writing

numberOfApples = numberOfApples + 1;

If `numberOfApples` was 20, this statement would assign it the value 21.

We should not read the assignment operator as “equals.” The statement means:

_Add 1 to the current value of `numberOfApples` and then assign the sum to `numberOfApples`_

The figure given below traces the effect of executing the following sequence of statements:

int numberOfApples;

numberOfApples = 15;

numberOfApples = 20;

numberOfApples = numberOfApples + 1;

The effect of a sequence of assignments

> 📝 **Note: Tracing the effect of the statements in a program is an essential skill**
> 
> To truly understand the effect of an assignment statement, you must imagine the current value of each variable at various points in time. You should be able to trace the effect of any sequence of Java statements, as we have done in the figure given above. With this skill, you will be able to locate the mistakes in the logic of your Java code. This ability is key to learning how to program.

> 📝 **Note: Declaring and initializing a variable**
> 
> When declaring a variable, you can assign it an initial value. For example, you can write
> 
> int numberOfApples = 15;

Explain

## Character variables[](https://www.educative.io/courses/java-masterclass-developers/variables#Character-variables)

After declaring a variable as a `char`, we can assign it a value by using a character literal, as follows:

char letter;

letter = 'a';

A **character literal** is a single character enclosed in single quotes. As noted earlier, we can combine this declaration and assignment:

char letter = 'a';

## Boolean variables[](https://www.educative.io/courses/java-masterclass-developers/variables#Boolean-variables)

We can assign a value of either `true` or `false` to a variable declared as a Boolean, as in the following example:

boolean done;

done = true;

The reserved words true and false are literals that represent predefined Boolean values.

As with variables of other data types, we can combine the declaration and assignment of a Boolean variable. We will see later that Boolean variables and Boolean expressions play important roles in Java