# Float Sizes in Rust

**Summary:**  
Rust provides two floating-point types: `f64` (64-bit) and `f32` (32-bit). The main difference is precision and memory usage—`f64` can represent numbers more precisely but uses more memory.

**Takeaways**

- `f64` = 64 bits (8 bytes), higher precision.
    
- `f32` = 32 bits (4 bytes), lower precision but smaller memory footprint.
    
- Both represent decimal numbers (floating-point values).

|Type|Bits|Bytes|Precision|Typical Use|
|---|---|---|---|---|
|f32|32|4|Lower|Memory-sensitive apps|
|f64|64|8|Higher|Default calculations|

---

# Precision Vs Memory Trade-off

**Summary:**  
`f64` stores more digits than `f32`, which makes it more precise for calculations. However, the larger size means more memory consumption and potentially slower performance when used in large quantities.

**Takeaways**

- `f64` keeps more decimal digits.
    
- `f32` saves memory but loses precision.
    
- Choosing depends on precision vs performance needs.

**Example concept**

10 ÷ 3 produces repeating decimals.

- `f64` stores **more 3s**
    
- `f32` stores **fewer 3s**

---

# When to Use F32 Vs F64

**Summary:**  
In small or local calculations, using `f64` is usually fine and simpler. However, in large systems with millions of numeric values (like game engines), using `f32` can significantly reduce memory usage.

**Takeaways**

- `f64` is fine for most everyday calculations.
    
- `f32` is common in performance-heavy systems.
    
- Large datasets make memory differences significant.

**Example Scenario**

|Application|Preferred Type|Reason|
|---|---|---|
|Simple math|f64|Higher precision|
|Game engine coordinates|f32|Lower memory usage|
|Scientific calculations|f64|Accuracy important|

---

# Integer Basics

**Summary:**  
Integers represent whole numbers without decimal points. They can be positive or negative and support numeric readability features like underscores.

**Takeaways**

- Integers have **no decimal part**.
    
- They can be **negative or positive**.
    
- `_` can be used for readability in numbers.

## Example Code

```rust
let ninety = 90;
let negative = -5;
let one_thousand = 1_000;
```

## Annotated Version

```rust
let ninety = 90;        // Integer value
let negative = -5;      // Negative integer
let one_thousand = 1_000; // Underscore improves readability
```

**Explanation**

1. `90` is a simple integer value.
    
2. `-5` shows integers can be negative.
    
3. `1_000` demonstrates numeric separators for readability.
    
4. The compiler ignores underscores.

---

# Integer Division Behavior

**Summary:**  
Dividing integers results in another integer. Any decimal portion of the result is discarded rather than rounded.

**Takeaways**

- Integer division **truncates decimals**.
    
- `10 / 3` becomes `3`.
    
- Rust does **not round**, it simply discards the fraction.

## Example Code

```rust
let exactly_three = 10 / 3;
```

## Annotated Version

```rust
let exactly_three = 10 / 3; // Integer division removes the decimal part
```

**Explanation**

1. Both `10` and `3` are integers.
    
2. Rust performs integer division.
    
3. The fractional part `.333…` is discarded.
    
4. The result stored is `3`.

---

# Division by Zero

**Summary:**  
Integer division by zero causes a runtime panic in Rust, which immediately stops the program. Floating-point division behaves differently and returns special values.

**Takeaways**

- Integer division by `0` → **program panic**.
    
- Float division by `0` → **Infinity, -Infinity, or NaN**.
    
- Always validate denominators before dividing.

|Division Type|Result|
|---|---|
|Integer ÷ 0|Panic (program stops)|
|Float ÷ 0|Infinity / NaN|

---

# Integer Sizes in Rust

**Summary:**  
Rust provides several integer sizes to balance storage and numeric range. Larger types can represent bigger numbers but consume more memory.

**Takeaways**

- Integer types range from **i8 to i128**.
    
- Larger integers support bigger values.
    
- Memory usage increases with size.

| Type | Bits | Bytes |
| ---- | ---- | ----- |
| i8   | 8    | 1     |
| i16  | 16   | 2     |
| i32  | 32   | 4     |
| i64  | 64   | 8     |
| i128 | 128  | 16    |

---

# Signed Vs Unsigned Integers

**Summary:**  
Signed integers allow negative numbers, while unsigned integers only represent non-negative numbers. Because unsigned numbers don’t store a sign bit, they can represent larger positive values.

**Takeaways**

- Signed integers (`i`) support negative numbers.
    
- Unsigned integers (`u`) start at 0.
    
- Unsigned types can represent larger positive ranges.

|Type|Range Example|
|---|---|
|i8|-128 → 127|
|u8|0 → 255|

| Type | Min | Max         |
| ---- | --- | ----------- |
| u8   | 0   | 255         |
| u16  | 0   | 65,535      |
| u32  | 0   | 4.294 mil   |
| u64  | 0   | 18, pent    |
| u128 | 0   | 170 decatri |

---

# Extremely Large Integers

**Summary:**  
Rust supports very large integer sizes such as `u128`, which can store extremely large numbers. For even larger numbers, external libraries can provide arbitrary-precision integers.

**Takeaways**

- `u128` stores extremely large values.
    
- Arbitrary-precision integers exist through libraries.
    
- Most applications never need values this large.

---

# The `char` Type

**Summary:**  
In Rust, `char` represents a Unicode scalar value and internally behaves like a validated `u32`. It ensures the number corresponds to a valid Unicode character.

**Takeaways**

- `char` is effectively a validated `u32`.
    
- Represents Unicode characters.
    
- Used to build strings.

|Type|Description|
|---|---|
|char|Unicode character|
|u32|Raw 32-bit number|

---

# Compiler Optimization Question

**Summary:**  
The Rust compiler does not typically combine multiple smaller integers into larger ones automatically. Hardware architecture and CPU register behavior often make such packing less efficient.

**Takeaways**

- Compilers rely on CPU architecture.
    
- Packing integers may reduce performance.
    
- Rust relies on LLVM optimizations.

---

# Numeric Type Conversion with `as`

**Summary:**  
Rust uses the `as` keyword to convert between numeric types. This is necessary when performing operations between different numeric types.

**Takeaways**

- `as` performs type casting.
    
- Both operands must be the same type for operations.
    
- Converting to larger types helps avoid data loss.

## Example Code

```rust
fn multiply(x: i64, y: u8) -> i64 {
    x * (y as i64)
}
```

## Annotated Version

```rust
fn multiply(x: i64, y: u8) -> i64 {
    // Convert y from u8 to i64
    // This allows multiplication with x
    x * (y as i64)
}
```

**Explanation**

1. `x` is a 64-bit integer.
    
2. `y` is an 8-bit unsigned integer.
    
3. Rust requires both operands to be the same type.
    
4. `y as i64` converts it to match `x`.
    
5. The multiplication returns an `i64`.

---

# Converting Integers and Floats

**Summary:**  
The `as` keyword can also convert integers into floating-point numbers. This is commonly done to perform floating-point division instead of integer division.

**Takeaways**

- `as` converts integers to floats.
    
- Useful when decimals are needed.
    
- `f64` is usually preferred for precision.

## Example Code

```rust
let x: i32 = 5;
let y: u16 = 2;

let result = (x as f64) / (y as f64);
```

## Annotated Version

```rust
let x: i32 = 5;     // 32-bit integer
let y: u16 = 2;     // 16-bit unsigned integer

// Convert both numbers to f64 to allow float division
let result = (x as f64) / (y as f64);
```

**Explanation**

1. `x` and `y` are integers.
    
2. Integer division would remove decimals.
    
3. Casting to `f64` enables floating-point division.
    
4. The result includes decimal precision.

---

# Risks of `as` Casting

**Summary:**  
Casting from larger types to smaller ones can cause data loss or value wrapping. Rust allows this conversion but it may produce unexpected results.

**Takeaways**

- Downcasting can truncate data.
    
- Values may wrap around instead of erroring.
    
- Use cautiously when reducing type size.

---

# Key Points

- `f64` offers higher precision while `f32` saves memory.
    
- Integer division truncates decimals and division by zero causes panic.
    
- Rust integers range from `i8` to `i128` and unsigned versions (`u8` to `u128`).
    
- `char` is essentially a validated `u32` representing Unicode characters.
    
- The `as` keyword converts between numeric types.
    
- Converting to larger types prevents data loss during operations.