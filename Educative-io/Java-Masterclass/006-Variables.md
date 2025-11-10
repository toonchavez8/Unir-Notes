# Variables

In this lesson, we will learn how to name pieces of data in our program.

---

## Why Use Variables

**Variables** are used to represent a piece of data in a Java program. The variable represents a memory location that stores the data. The data itself is called the variable’s **value**.

We use an **identifier** to name a variable. By convention, variable names should:

- Begin with a lowercase letter
    
- Be meaningful

For example, if our variable represents the sales tax for a purchase, name it `salesTax` instead of `st` or `stax`.

Multiple-word variable names are common. By convention, the first word begins with a lowercase letter, but subsequent words in the name each begin with an uppercase letter.

> ✏️ **Programming Tip**  
> Java variable names can be long. Favor clarity over brevity. Avoid one-letter names unless the context suggests that they are appropriate. Follow convention by beginning variable names with a lowercase letter.

---

## Declarations

When we first create a variable, we must choose its **data type** — that is, we must specify what type of data the variable will represent.

For example, if our program involves apples, we might track the number of apples in the variable `numberOfApples`. This count is an integer, so the data type of this variable would be `int`.

We declare the data type of a variable in a **declaration statement**.  
For example, the following statements declare one `int` variable, two `double` variables, a character variable, and a Boolean variable:

```java
int numberOfApples;
double pricePerApple, totalCost;
char letter;
boolean done;
```

Each declaration begins with a data type and contains one or more variables of that type.  
Commas separate variables of the same type, and a semicolon ends each declaration.

> 📝 **Note: Variable declarations**  
> You must declare a variable before you can use it. You declare each variable only once, regardless of how often you use it.

---

## Assignments

When we declare a variable within the body of a method, Java gives it no particular initial value.  
We can either give an initial value to a variable or change its existing value by using an **assignment statement**.

An assignment statement has the following form:

```Python
variable = expression;
```

The **assignment operator** (`=`) assigns the value of the expression to the variable.  
An **operator** is a symbol within a programming language that represents a particular operation or action.  
For example:

- `=` assigns a value to a variable.
    
- `*` multiplies two arithmetic values.

An **expression** is a combination of operators and other components that represent values.

> 📝 **Syntax: Assignment statement**  
> `variable = expression;`  
> It assigns the value of the expression to the variable.

---

### Example

After the following declarations:

```java
int numberOfApples;
double pricePerApple, totalCost;
```

We can assign values to the variables by writing:

```java
numberOfApples = 15;
pricePerApple = 0.29;
totalCost = numberOfApples * pricePerApple;
```

The `15` and `0.29` are called **literals** — fixed values written directly in the code.  
Here, `15` is an integer literal, and `0.29` is a real (floating-point) literal.

The expression `numberOfApples * pricePerApple` is an example of an **arithmetic expression**.  
The operator `*` multiplies the current values of the two variables, and the resulting product (`4.35`) is assigned to `totalCost`.

> 📝 **Note: Using variables**  
> Once you declare a variable and assign it a value, you can use it in another assignment statement.

---

## Declarations and Assignments Within a Program

The program below shows variable declarations and assignment statements working together to compute the cost of a certain number of apples.

```java
public class Apples {
    public static void main(String[] args) {
        int numberOfApples;
        double pricePerApple, totalCost;

        numberOfApples = 15;
        pricePerApple = 0.29;
        totalCost = numberOfApples * pricePerApple;

        System.out.print(numberOfApples + " apples at $");
        System.out.print(pricePerApple + " apiece cost $");
        System.out.println(totalCost);
    }
}
```

This program multiplies the number of apples by their price and prints the total cost.

---

### The `+` Operator and String Concatenation

Note the use of the `+` operator in the program’s `print` statements.  
When used this way, the `+` operator **concatenates** (joins) one string with another.

Although it appears that we are joining a number with a string, Java automatically converts the number into a string before displaying it.

---

### Strings Spanning Two or More Lines

The previous program uses several `print` statements to display one line of output:

```java
System.out.print(numberOfApples + " apples at $");
System.out.print(pricePerApple + " apiece cost $");
System.out.println(totalCost);
```

We could also write one `println` statement and get the same output:

```java
System.out.println(numberOfApples + " apples at $" +
                   pricePerApple + " apiece cost $" + totalCost);
```

If a statement is long, we can split it across multiple lines.  
The compiler ignores white space before or after the `+` operator.

However, a **string literal** cannot span multiple lines directly — this would cause a syntax error:

```java
System.out.println("The total cost of 15 apples if bought
                   separately is $" + totalCost); // SYNTAX ERROR!
```

✅ Correct version:

```java
System.out.println("The total cost of 15 apples if bought " +
                   "separately is $" + totalCost);
```

Note the additional quotes, space after `"bought "`, and the `+` operator joining the strings.

---

## Changing the Value of a Variable

Variables are named so because their values can **change**.

For example:

```java
numberOfApples = 20;
```

Or we could add 1 to its current value:

```java
numberOfApples = numberOfApples + 1;
```

If `numberOfApples` was 20, this statement makes it 21.

You should **not** read the `=` as “equals.”  
It means “assign the result of the expression on the right to the variable on the left.”

Example sequence:

```java
int numberOfApples;
numberOfApples = 15;
numberOfApples = 20;
numberOfApples = numberOfApples + 1;
```

> 📝 **Note: Tracing variable values**  
> To understand assignments, imagine the current value of each variable step by step.  
> Tracing helps you detect logic errors — an essential skill for debugging.

> 📝 **Note: Declaring and initializing a variable**  
> You can assign an initial value when declaring a variable:

 ```java
 int numberOfApples = 15;
 ```

---

## Character Variables

After declaring a variable as a `char`, assign it a character literal:

```java
char letter;
letter = 'a';
```

A **character literal** is a single character enclosed in single quotes.  
You can also combine declaration and assignment:

```java
char letter = 'a';
```

---

## Boolean Variables

We can assign a value of either `true` or `false` to a variable declared as a Boolean:

```java
boolean done;
done = true;
```

The reserved words `true` and `false` are **Boolean literals** that represent predefined logical values.

As with other data types, we can combine declaration and assignment:

```java
boolean done = true;
```

Boolean variables and expressions play an important role in controlling program logic.
