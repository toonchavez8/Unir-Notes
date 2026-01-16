# Variables — Study Notes

---

## Variables Overview

**Summary:** Variables allow us to name and store data in memory so a program can use and manipulate that data. Each variable has a value that lives at a specific memory location.  
**Takeaways:**

- A variable represents a memory location.
    
- Its contents are called the variable’s value.
    
- Names (identifiers) describe what the data represents.

---

## Naming Variables

**Summary:** Variable names (identifiers) should start with a lowercase letter and clearly describe their purpose. Multi-word names use camelCase formatting.  
**Takeaways:**

- Begin with lowercase; use meaningful names.
    
- camelCase: first word lowercase, next words uppercase first letter.
    
- Avoid unclear or very short names unless appropriate.

---

## Programming Tip on Naming

**Summary:** Clarity is favored over brevity. Long names are acceptable if they communicate meaning. One-letter variables should be used only when obvious.  
**Takeaways:**

- Prefer clarity over shortness.
    
- Avoid one-letter names unless context makes them clear.
    
- Always start with lowercase.

---

## Declarations Overview

**Summary:** Declaring a variable means specifying its data type and name. A variable must be declared before it is used.  
**Takeaways:**

- Declaration = data type + variable name.
    
- Declare before use; declare once.
    
- Commas allow multiple variables of the same type.

---

### Example Declarations

```java
int numberOfApples;
double pricePerApple, totalCost;
char letter;
boolean done;
```

---

## Assignment Statements

**Summary:** Assignment gives a variable an initial value or updates its value. The assignment operator `=` stores the value of an expression into the variable.  
**Takeaways:**

- `variable = expression;` is the assignment format.
    
- `=` does not mean “equals”; it means “store into.”
    
- Variables declared in methods start with no assigned value.

---

## Assignment Syntax

**Summary:** A valid assignment ends with a semicolon and places the expression on the right and the variable on the left.  
**Takeaways:**

- Format: `variable = expression;`
    
- Expression can be a literal, another variable, or a calculation.

---

## Assignment Example

**Summary:** Values can be assigned using literals or expressions. Arithmetic expressions combine operators and variables.  
**Takeaways:**

- Literals represent fixed values.
    
- `*` multiplies values in an expression.
    
- Expression results can be stored in another variable.

### Original Code

```java
int numberOfApples;
double pricePerApple, totalCost;

numberOfApples = 15;
pricePerApple = 0.29;
totalCost = numberOfApples * pricePerApple;
```

### Annotated Version

```java
// Declare variables
int numberOfApples;
double pricePerApple, totalCost;

// Assign literal values
numberOfApples = 15;      // integer literal
pricePerApple = 0.29;     // real (double) literal

// Multiply two variables and store the result
totalCost = numberOfApples * pricePerApple; // expression assigned to totalCost
```

### Step-by-step Explanation

1. `numberOfApples` receives the integer literal `15`.
    
2. `pricePerApple` receives the double literal `0.29`.
    
3. The expression multiplies their current values.
    
4. The result (`4.35`) is stored in `totalCost`.

---

## Using Variables in Programs

**Summary:** After assigning values, variables can be used in other expressions and assignments.  
**Takeaways:**

- Variables can appear inside new assignments.
    
- Their values update as the program runs.
    
- Assignment overwrites previous values.

---

## Declarations and Assignments in Full Program

**Summary:** A program can declare variables, assign values, compute results, and display output with string concatenation.  
**Takeaways:**

- `+` joins strings (concatenation).
    
- Java converts numbers to strings when concatenating.
    
- Print statements can be broken across lines.

### Example Program (from text) — Reconstructed

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

### Annotated Version

```java
public class Apples {
    public static void main(String[] args) {

        // Variable declarations
        int numberOfApples;
        double pricePerApple, totalCost;

        // Assign values
        numberOfApples = 15;
        pricePerApple = 0.29;

        // Compute total cost
        totalCost = numberOfApples * pricePerApple;

        // Concatenate numbers and strings for output
        System.out.print(numberOfApples + " apples at $");
        System.out.print(pricePerApple + " apiece cost $");

        // Print final computed value
        System.out.println(totalCost);
    }
}
```

### Step-by-step Explanation

1. Variables are declared.
    
2. Values are assigned.
    
3. The multiplication calculates cost.
    
4. The concatenation prints text + numbers.

---

## Strings across Lines

**Summary:** Long print statements can be split across lines as long as breaks occur between operators. Strings cannot be split without closing and reopening quotes.  
**Takeaways:**

- Line breaks around `+` are allowed.
    
- A string literal cannot span lines directly.
    
- Must break the string into two literals and concatenate.

### Incorrect Version

```java
System.out.println("The total cost of 15 apples if bought
                    separately is $" + totalCost);  // ERROR
```

### Correct Version

```java
System.out.println("The total cost of 15 apples if bought " +
                   "separately is $" + totalCost);
```

---

## Changing Variable Values

**Summary:** Variables can be reassigned new values or updated based on their existing value.  
**Takeaways:**

- Reassignment overwrites the previous value.
    
- Updating uses the current value on the right side.
    
- `x = x + 1` increases numerical variables.

### Example

```java
int numberOfApples;
numberOfApples = 15;
numberOfApples = 20;          // new value
numberOfApples = numberOfApples + 1; // becomes 21
```

---

## Tracing Assignments

**Summary:** Understanding assignments requires mentally tracking current variable values through execution. This is essential for debugging and logic tracing.  
**Takeaways:**

- Track variable values step by step.
    
- Helps find logic errors.
    
- Fundamental programming skill.

---

## Declaring + Initializing at once

**Summary:** You may give a variable an initial value at the moment of declaration.  
**Takeaways:**

- Format: `type name = value;`
    
- Saves an extra assignment.

### Example

```java
int numberOfApples = 15;
```

---

## Character Variables

**Summary:** `char` stores a single character using single quotes. Declaration and assignment can be separate or combined.  
**Takeaways:**

- Character literal uses single quotes.
    
- Only one character allowed.
    
- Can assign during declaration.

### Example

```java
char letter = 'a';
```

---

## Boolean Variables

**Summary:** Boolean variables store either `true` or `false`. These values are reserved words.  
**Takeaways:**

- Only two valid Boolean literals: `true`, `false`.
    
- Use them in conditions and logic.
    
- Can declare and initialize together.

### Example

```java
boolean done = true;
```

---

# Key Points

- Variables store data at named memory locations.
    
- Use meaningful camelCase names starting lowercase.
    
- Declare a variable’s type before using it.
    
- Assignment uses `=` to store values or computed results.
    
- Strings must be concatenated, not split across lines.
    
- Reassignments update the stored value; trace variable values to understand program flow.