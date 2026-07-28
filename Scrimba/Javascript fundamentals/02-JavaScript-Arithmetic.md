# JavaScript Arithmetic Operators and Expressions

## Concept

JavaScript supports built-in arithmetic operators that allow you to perform mathematical calculations directly in your code. Rather than operating only on literal values, these operators are most commonly used with variables to compute new values.

An **expression** is any piece of code that evaluates to a value. Arithmetic expressions are fundamental because they allow your application to derive state instead of hardcoding it.

---

## Code Breakdown

### Arithmetic with Literals

```javascript
let count = 5 + 7
```

- `5 + 7` is an arithmetic expression.
    
- JavaScript evaluates the expression before assigning it.
    
- `count` receives the computed value (`12`).

Other operators shown:

```javascript
let count = 5 - 7
```

```javascript
let count = 5 / 7
```

```javascript
let count = 5 * 7
```

|Operator|Description|
|---|---|
| `+` |Addition|
| `-` |Subtraction|
| `*` |Multiplication|
| `/` |Division|

---

### Using Variables Instead of Literals

```javascript
let firstBatch = 5
let secondBatch = 7

let count = firstBatch + secondBatch
```

**Execution Flow**

1. `firstBatch` stores `5`
    
2. `secondBatch` stores `7`
    
3. JavaScript reads both values.
    
4. It evaluates:

```javascript
5 + 7
```

5. The result (`12`) is assigned to `count`.

---

### Derived Values

```javascript
let myAge = 35
let humanDogRatio = 7

let myDogAge = myAge * humanDogRatio

console.log(myDogAge)
```

Instead of manually writing:

```javascript
let myDogAge = 245
```

the value is calculated automatically from other variables.

This is known as **deriving state**, one of the most common programming patterns.

---

# Why We Use It

Calculations should almost always be based on variables rather than hardcoded values.

Benefits include:

- Changing one variable updates every calculation automatically.
    
- Improves readability.
    
- Reduces duplicated values.
    
- Makes code adaptable to changing inputs.
    
- Prevents inconsistencies when values change later.

---

# Deep Dive

### Expressions are everywhere

JavaScript evaluates expressions constantly.

These are all expressions:

```javascript
5 + 7
```

```javascript
firstBatch + secondBatch
```

```javascript
price * quantity
```

```javascript
user.age >= 18
```

Most JavaScript code consists of expressions that eventually produce values.

---

### Derived state is better than duplicated state

Instead of storing:

```javascript
let subtotal = 120
let tax = 19
let total = 139
```

compute it:

```javascript
let total = subtotal + tax
```

This avoids bugs where one value changes but another isn't updated.

Experienced developers avoid storing information that can be calculated.

---

### Variables represent meaning, not just numbers

Compare these:

```javascript
let x = 5
let y = 7
```

vs.

```javascript
let firstBatch = 5
let secondBatch = 7
```

The second version immediately explains what the numbers represent.

Choosing descriptive names dramatically improves maintainability.

---

### Arithmetic expressions scale naturally

Today's lesson adds two numbers.

Real applications calculate things like:

- Shopping cart totals
    
- Taxes
    
- Discounts
    
- Animation timing
    
- Game scores
    
- Pagination
    
- Financial reports
    
- Analytics
    
- Sensor measurements

The same arithmetic operators are used regardless of complexity.

---

### JavaScript uses IEEE 754 floating-point numbers

The lesson briefly showed division:

```javascript
5 / 7
```

which produces a decimal.

JavaScript stores all regular numbers as **64-bit floating-point values (IEEE 754)**.

This leads to famous precision issues:

```javascript
0.1 + 0.2
```

results in

```javascript
0.30000000000000004
```

For financial applications, developers often use specialized decimal libraries or represent money as integer cents.

---

# How It Was Used in This Lesson

The instructor transitioned from assigning fixed values to computing values from existing variables.

Instead of:

```javascript
let count = 12
```

the lesson introduced:

```javascript
let count = firstBatch + secondBatch
```

to demonstrate that variables can participate in expressions.

The dog age exercise reinforced the idea that variables can be combined to produce new variables, encouraging a mindset of calculating values rather than hardcoding results.

---

# Related Concepts

- Variables (`let`, `const`)
    
- Expressions
    
- Operators
    
- Assignment (`=`)
    
- Primitive Numbers
    
- Operator Precedence
    
- Derived State
    
- Type Coercion (later when strings are introduced)
    
- Compound Assignment (`+=`, `-=`, `*=`, `/=`)

---

# Extra Context (Beyond the Lesson)

## Modern JavaScript prefers `const`

Although the lesson uses `let` throughout, many experienced developers would write:

```javascript
const firstBatch = 5
const secondBatch = 7

const count = firstBatch + secondBatch
```

Since none of these variables are reassigned, `const` better communicates intent and prevents accidental modifications.

---

## Operator Precedence

JavaScript follows standard mathematical precedence.

```javascript
2 + 3 * 4
```

evaluates as:

```text
14
```

not

```text
20
```

Use parentheses whenever readability is more important than remembering precedence rules.

```javascript
const total = (price + tax) * quantity
```

---

## Compound Assignment

Once variables become mutable, JavaScript offers shorthand operators:

```javascript
count += firstBatch
```

instead of

```javascript
count = count + firstBatch
```

These become common when counters, loops, and accumulators are introduced.

---

## Quick Summary

- Arithmetic operators create expressions that evaluate to values.
    
- Calculations should use variables instead of hardcoded numbers.
    
- Derived values reduce duplication and improve maintainability.
    
- Descriptive variable names make code self-documenting.
    
- JavaScript uses floating-point numbers, which can introduce decimal precision quirks.
    
- Prefer `const` for values that don't change and `let` only when reassignment is needed.

---

# 80/20 Takeaways

- Think in terms of **expressions**, not just values—most JavaScript code is built by combining expressions.
    
- Store raw data once and derive everything else from it to avoid inconsistencies.
    
- Name variables after what they represent, not their type or position (`firstBatch` is far clearer than `x`).
    
- Arithmetic operators are simple, but they underpin everything from UI counters to financial calculations and game logic.
    
- Write code so that changing one input variable automatically updates every dependent calculation. That's a core principle of maintainable software.