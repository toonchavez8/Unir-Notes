This week's question:

**Write a function that takes a non-negative integer `n` and prints the numbers `0` through `n` in a clockwise spiral, starting at the top-left of a square grid.** Hint: the grid size should be `ceil(sqrt(n + 1))`, and any unused cells should be blank.

Example:

```text
> spiralGrid(99)
 0  1  2  3  4  5  6  7  8  9
35 36 37 38 39 40 41 42 43 10
34 63 64 65 66 67 68 69 44 11
33 62 83 84 85 86 87 70 45 12
32 61 82 95 96 97 88 71 46 13
31 60 81 94 99 98 89 72 47 14
30 59 80 93 92 91 90 73 48 15
29 58 79 78 77 76 75 74 49 16
28 57 56 55 54 53 52 51 50 17
27 26 25 24 23 22 21 20 19 18

> spiralGrid(30)
 0  1  2  3  4  5
19 20 21 22 23  6
18          24  7
17 30       25  8
16 29 28 27 26  9
15 14 13 12 11 10
```

## Iterative Rust implementation guide

This guide builds the solution in small checkpoints. That matters because the full problem has several moving parts:

1. Run a Rust program.
2. Read `n` from the command line.
3. Parse `n` as a number.
4. Generate the sequence `0..=n`.
5. Calculate the square grid size.
6. Store blank and filled cells.
7. Fill the grid in spiral order.
8. Print the grid with aligned columns.
9. Refactor into functions and add a few focused tests.

The order is intentional. Each step proves one idea before adding the next one.

Rust note for junior developers: early examples are allowed to be a little direct because they are checkpoints. The final version avoids `unwrap()` and `expect()` in normal code, passes data by reference where that makes sense, and keeps comments focused on the parts that are easy to misunderstand.

---

## Step 0: create a Rust project

Create a new binary project:

```bash
cargo new clockwork_spiral
cd clockwork_spiral
```

Rust creates this structure:

```text
clockwork_spiral/
  Cargo.toml
  src/
    main.rs
```

All code below goes in:

```text
src/main.rs
```

Run the program with:

```bash
cargo run
```

Once the program starts accepting a number, run it like this:

```bash
cargo run -- 30
```

The `--` tells Cargo that everything after it belongs to your program, not to Cargo.

---

## Step 1: make sure Rust runs

Before solving the spiral, make sure the project compiles and prints text.

```rust
fn main() {
    println!("hello world");
}
```

Run:

```bash
cargo run
```

Expected output:

```text
hello world
```

If this fails, the issue is your Rust setup or project folder, not the spiral logic.

---

## Step 2: receive the command-line parameter

Now read the value for `n`.

For this command:

```bash
cargo run -- 30
```

the program receives `"30"` as text. Command-line input always starts as text.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    println!("{args:?}");
}
```

Run:

```bash
cargo run -- 30
```

Example output:

```text
["target/debug/clockwork_spiral", "30"]
```

What to notice:

- `args[0]` is the program path.
- `args[1]` is the value the user typed.
- We collect into a `Vec<String>` here because this checkpoint is about seeing the full list.

---

## Step 3: parse the parameter into a number

The spiral needs a number, not a `String`. Parse the second argument into a `usize`.

`usize` is a good fit because we use the value for indexes, grid sizes, and vector lengths.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Usage: cargo run -- <non-negative integer>");
        return;
    }

    let raw_n = &args[1];

    let Ok(n) = raw_n.parse::<usize>() else {
        eprintln!("Please provide a valid non-negative integer");
        return;
    };

    println!("n = {n}");
}
```

Run:

```bash
cargo run -- 30
```

Expected output:

```text
n = 30
```

Try invalid input:

```bash
cargo run -- hello
```

Expected output:

```text
Please provide a valid non-negative integer
```

Rust habit: avoid `unwrap()` and `expect()` in normal program flow. They crash the program. Here, invalid input is expected user behavior, so we print a message and return.

---

## Step 4: print numbers from 0 through n

Before building a grid, prove the sequence is right.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Usage: cargo run -- <non-negative integer>");
        return;
    }

    let raw_n = &args[1];

    let Ok(n) = raw_n.parse::<usize>() else {
        eprintln!("Please provide a valid non-negative integer");
        return;
    };

    for value in 0..=n {
        println!("{value}");
    }
}
```

Run:

```bash
cargo run -- 5
```

Expected output:

```text
0
1
2
3
4
5
```

The spiral is this same sequence. Later we will place each value into a row and column instead of printing it immediately.

---

## Step 5: calculate the square grid size

The prompt gives this formula:

```text
grid size = ceil(sqrt(n + 1))
```

Use `n + 1` because the sequence starts at `0`. If `n = 30`, there are `31` values:

```text
0 through 30
```

The smallest square that can hold 31 values is:

```text
ceil(sqrt(31)) = 6
```

So `spiralGrid(30)` needs a `6 x 6` grid.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Usage: cargo run -- <non-negative integer>");
        return;
    }

    let raw_n = &args[1];

    let Ok(n) = raw_n.parse::<usize>() else {
        eprintln!("Please provide a valid non-negative integer");
        return;
    };

    let value_count = n + 1;
    let size = (value_count as f64).sqrt().ceil() as usize;

    println!("n = {n}");
    println!("values = {value_count}");
    println!("grid size = {size} x {size}");
}
```

Run:

```bash
cargo run -- 30
```

Expected output:

```text
n = 30
values = 31
grid size = 6 x 6
```

Run:

```bash
cargo run -- 99
```

Expected output:

```text
n = 99
values = 100
grid size = 10 x 10
```

Practical note: this formula is fine for this challenge. In production code, you would think more about very large inputs and possible overflow around `n + 1`.

---

## Step 6: create an empty grid

Some cells may be blank. For example, `n = 30` gives 31 numbers, but a `6 x 6` grid has 36 cells.

That leaves 5 empty cells.

Use `Option<usize>` to represent "a cell may or may not contain a number":

```rust
Some(24) // this cell contains 24
None     // this cell is blank
```

Now create a square grid filled with `None`.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Usage: cargo run -- <non-negative integer>");
        return;
    }

    let raw_n = &args[1];

    let Ok(n) = raw_n.parse::<usize>() else {
        eprintln!("Please provide a valid non-negative integer");
        return;
    };

    let value_count = n + 1;
    let size = (value_count as f64).sqrt().ceil() as usize;

    let grid: Vec<Vec<Option<usize>>> = vec![vec![None; size]; size];

    println!("grid size = {size} x {size}");
    println!("{grid:?}");
}
```

Run:

```bash
cargo run -- 5
```

Since `0..=5` has 6 values, the grid size is `3 x 3`.

Example debug output:

```text
grid size = 3 x 3
[[None, None, None], [None, None, None], [None, None, None]]
```

What to notice:

- `Vec<Vec<Option<usize>>>` means "a vector of rows."
- Each row is a `Vec<Option<usize>>`.
- `None` is not an error. It is how we mark blank cells.

---

## Step 7: fill the top row first

The spiral starts at the top-left and moves right.

Before doing the full spiral, fill only the first row.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Usage: cargo run -- <non-negative integer>");
        return;
    }

    let raw_n = &args[1];

    let Ok(n) = raw_n.parse::<usize>() else {
        eprintln!("Please provide a valid non-negative integer");
        return;
    };

    let value_count = n + 1;
    let size = (value_count as f64).sqrt().ceil() as usize;

    let mut grid: Vec<Vec<Option<usize>>> = vec![vec![None; size]; size];

    for col in 0..size {
        if col <= n {
            grid[0][col] = Some(col);
        }
    }

    println!("{grid:?}");
}
```

Run:

```bash
cargo run -- 5
```

Example debug output:

```text
[[Some(0), Some(1), Some(2)], [None, None, None], [None, None, None]]
```

This proves the indexing pattern:

```text
grid[row][column]
```

Rust detail: `grid` must be `mut` because we write values into it after creating it.

---

## Step 8: understand the spiral boundaries

A clockwise spiral can be handled with four boundaries:

```text
top
bottom
left
right
```

For a `6 x 6` grid, the first layer is:

```text
top = 0
bottom = 5
left = 0
right = 5
```

The movement order is:

1. Move right across the top row.
2. Move down the right column.
3. Move left across the bottom row.
4. Move up the left column.
5. Move the boundaries inward.
6. Repeat until every number is placed.

After the outside layer is done, the next layer is:

```text
top = 1
bottom = 4
left = 1
right = 4
```

The boundary values are all `usize`, so they cannot go below zero. That is why the code checks `right == 0` and `bottom == 0` before subtracting.

---

## Step 9: fill the full spiral

Now place every number from `0` through `n`.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Usage: cargo run -- <non-negative integer>");
        return;
    }

    let raw_n = &args[1];

    let Ok(n) = raw_n.parse::<usize>() else {
        eprintln!("Please provide a valid non-negative integer");
        return;
    };

    let value_count = n + 1;
    let size = (value_count as f64).sqrt().ceil() as usize;

    let mut grid: Vec<Vec<Option<usize>>> = vec![vec![None; size]; size];

    let mut top: usize = 0;
    let mut bottom: usize = size - 1;
    let mut left: usize = 0;
    let mut right: usize = size - 1;
    let mut value: usize = 0;

    while value <= n {
        for col in left..=right {
            if value > n {
                break;
            }

            grid[top][col] = Some(value);
            value += 1;
        }
        top += 1;

        for row in top..=bottom {
            if value > n {
                break;
            }

            grid[row][right] = Some(value);
            value += 1;
        }

        if right == 0 {
            break;
        }
        right -= 1;

        for col in (left..=right).rev() {
            if value > n {
                break;
            }

            grid[bottom][col] = Some(value);
            value += 1;
        }

        if bottom == 0 {
            break;
        }
        bottom -= 1;

        for row in (top..=bottom).rev() {
            if value > n {
                break;
            }

            grid[row][left] = Some(value);
            value += 1;
        }
        left += 1;
    }

    println!("{grid:?}");
}
```

Run:

```bash
cargo run -- 30
```

The debug output is not pretty yet, but it should contain numbers in spiral positions.

At this checkpoint, formatting does not matter. We are only checking placement.

---

## Step 10: print the grid without nice spacing

Now print the grid row by row.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Usage: cargo run -- <non-negative integer>");
        return;
    }

    let raw_n = &args[1];

    let Ok(n) = raw_n.parse::<usize>() else {
        eprintln!("Please provide a valid non-negative integer");
        return;
    };

    let value_count = n + 1;
    let size = (value_count as f64).sqrt().ceil() as usize;

    let mut grid: Vec<Vec<Option<usize>>> = vec![vec![None; size]; size];

    let mut top: usize = 0;
    let mut bottom: usize = size - 1;
    let mut left: usize = 0;
    let mut right: usize = size - 1;
    let mut value: usize = 0;

    while value <= n {
        for col in left..=right {
            if value > n {
                break;
            }
            grid[top][col] = Some(value);
            value += 1;
        }
        top += 1;

        for row in top..=bottom {
            if value > n {
                break;
            }
            grid[row][right] = Some(value);
            value += 1;
        }

        if right == 0 {
            break;
        }
        right -= 1;

        for col in (left..=right).rev() {
            if value > n {
                break;
            }
            grid[bottom][col] = Some(value);
            value += 1;
        }

        if bottom == 0 {
            break;
        }
        bottom -= 1;

        for row in (top..=bottom).rev() {
            if value > n {
                break;
            }
            grid[row][left] = Some(value);
            value += 1;
        }
        left += 1;
    }

    for row in grid {
        for cell in row {
            match cell {
                Some(number) => print!("{number} "),
                None => print!("  "),
            }
        }

        println!();
    }
}
```

Run:

```bash
cargo run -- 30
```

The shape should be recognizable, but the columns may not line up. Single-digit and double-digit numbers take different amounts of space.

---

## Step 11: add proper column spacing

The prompt's examples align every cell by width.

For `n = 30`, the largest number has 2 digits, so every cell should be width 2:

```text
 0
30
```

For `n = 999`, the largest number has 3 digits, so every cell should be width 3:

```text
  0
999
```

Calculate the width like this:

```rust
let cell_width = n.to_string().len();
```

Then use Rust's formatting syntax:

```rust
print!("{number:>cell_width$}");
```

That means "print this number right-aligned inside a column of width `cell_width`."

For blank cells, print the same amount of spaces:

```rust
print!("{:>cell_width$}", "");
```

Also print one space between columns. That separator is separate from the width of the cell itself.

---

## Step 12: final version

This version reads `n`, builds the grid, fills the clockwise spiral, leaves unused cells blank, and prints aligned columns.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Usage: cargo run -- <non-negative integer>");
        return;
    }

    let raw_n = &args[1];

    let Ok(n) = raw_n.parse::<usize>() else {
        eprintln!("Please provide a valid non-negative integer");
        return;
    };

    let value_count = n + 1;
    let size = (value_count as f64).sqrt().ceil() as usize;

    let mut grid: Vec<Vec<Option<usize>>> = vec![vec![None; size]; size];

    let mut top: usize = 0;
    let mut bottom: usize = size - 1;
    let mut left: usize = 0;
    let mut right: usize = size - 1;
    let mut value: usize = 0;

    while value <= n {
        for col in left..=right {
            if value > n {
                break;
            }

            grid[top][col] = Some(value);
            value += 1;
        }
        top += 1;

        for row in top..=bottom {
            if value > n {
                break;
            }

            grid[row][right] = Some(value);
            value += 1;
        }

        if right == 0 {
            break;
        }
        right -= 1;

        for col in (left..=right).rev() {
            if value > n {
                break;
            }

            grid[bottom][col] = Some(value);
            value += 1;
        }

        if bottom == 0 {
            break;
        }
        bottom -= 1;

        for row in (top..=bottom).rev() {
            if value > n {
                break;
            }

            grid[row][left] = Some(value);
            value += 1;
        }
        left += 1;
    }

    let cell_width = n.to_string().len();

    for row in grid {
        for (col_index, cell) in row.iter().enumerate() {
            if col_index > 0 {
                print!(" ");
            }

            match cell {
                Some(number) => print!("{number:>cell_width$}"),
                None => print!("{:>cell_width$}", ""),
            }
        }

        println!();
    }
}
```

Run:

```bash
cargo run -- 30
```

Expected output:

```text
 0  1  2  3  4  5
19 20 21 22 23  6
18          24  7
17 30       25  8
16 29 28 27 26  9
15 14 13 12 11 10
```

Run:

```bash
cargo run -- 99
```

Expected output:

```text
 0  1  2  3  4  5  6  7  8  9
35 36 37 38 39 40 41 42 43 10
34 63 64 65 66 67 68 69 44 11
33 62 83 84 85 86 87 70 45 12
32 61 82 95 96 97 88 71 46 13
31 60 81 94 99 98 89 72 47 14
30 59 80 93 92 91 90 73 48 15
29 58 79 78 77 76 75 74 49 16
28 57 56 55 54 53 52 51 50 17
27 26 25 24 23 22 21 20 19 18
```

This is a working solution. It is still all in `main`, which is fine for learning but awkward to test.

---

## Step 13: refactor into functions

After the full version works, split it into smaller functions.

This does two useful things:

- Each function has one job.
- The spiral logic can be tested without running the command-line program.

```rust
use std::env;

fn grid_size(n: usize) -> usize {
    ((n + 1) as f64).sqrt().ceil() as usize
}

fn build_spiral(n: usize) -> Vec<Vec<Option<usize>>> {
    let size = grid_size(n);
    let mut grid: Vec<Vec<Option<usize>>> = vec![vec![None; size]; size];

    let mut top: usize = 0;
    let mut bottom: usize = size - 1;
    let mut left: usize = 0;
    let mut right: usize = size - 1;
    let mut value: usize = 0;

    while value <= n {
        for col in left..=right {
            if value > n {
                break;
            }
            grid[top][col] = Some(value);
            value += 1;
        }
        top += 1;

        for row in top..=bottom {
            if value > n {
                break;
            }
            grid[row][right] = Some(value);
            value += 1;
        }

        if right == 0 {
            break;
        }
        right -= 1;

        for col in (left..=right).rev() {
            if value > n {
                break;
            }
            grid[bottom][col] = Some(value);
            value += 1;
        }

        if bottom == 0 {
            break;
        }
        bottom -= 1;

        for row in (top..=bottom).rev() {
            if value > n {
                break;
            }
            grid[row][left] = Some(value);
            value += 1;
        }
        left += 1;
    }

    grid
}

fn print_grid(grid: &[Vec<Option<usize>>], n: usize) {
    let cell_width = n.to_string().len();

    for row in grid {
        for (col_index, cell) in row.iter().enumerate() {
            if col_index > 0 {
                print!(" ");
            }

            match cell {
                Some(number) => print!("{number:>cell_width$}"),
                None => print!("{:>cell_width$}", ""),
            }
        }

        println!();
    }
}

fn parse_n(args: &[String]) -> Result<usize, String> {
    if args.len() != 2 {
        return Err("Usage: cargo run -- <non-negative integer>".to_string());
    }

    args[1]
        .parse::<usize>()
        .map_err(|_| "Please provide a valid non-negative integer".to_string())
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let n = match parse_n(&args) {
        Ok(n) => n,
        Err(message) => {
            eprintln!("{message}");
            return;
        }
    };

    let grid = build_spiral(n);
    print_grid(&grid, n);
}
```

The behavior is the same. The organization is better:

```text
grid_size()     decides how large the square is
build_spiral()  places the numbers
print_grid()    handles blank cells and spacing
parse_n()       turns command-line input into a usize
main()          connects input, spiral building, and printing
```

This is already easier to reason about than the all-in-one version. The next step makes one more improvement: it moves the command-line workflow into `run`, so `main` only handles process-level setup and error printing.

---

## Step 14: final refactor with tests

This version keeps the same logic but makes the error path cleaner and adds focused tests.

```rust
use std::env;

fn grid_size(n: usize) -> usize {
    ((n + 1) as f64).sqrt().ceil() as usize
}

fn build_spiral(n: usize) -> Vec<Vec<Option<usize>>> {
    let size = grid_size(n);
    let mut grid: Vec<Vec<Option<usize>>> = vec![vec![None; size]; size];

    let mut top: usize = 0;
    let mut bottom: usize = size - 1;
    let mut left: usize = 0;
    let mut right: usize = size - 1;
    let mut value: usize = 0;

    while value <= n {
        for col in left..=right {
            if value > n {
                break;
            }
            grid[top][col] = Some(value);
            value += 1;
        }
        top += 1;

        for row in top..=bottom {
            if value > n {
                break;
            }
            grid[row][right] = Some(value);
            value += 1;
        }

        if right == 0 {
            break;
        }
        right -= 1;

        for col in (left..=right).rev() {
            if value > n {
                break;
            }
            grid[bottom][col] = Some(value);
            value += 1;
        }

        if bottom == 0 {
            break;
        }
        bottom -= 1;

        for row in (top..=bottom).rev() {
            if value > n {
                break;
            }
            grid[row][left] = Some(value);
            value += 1;
        }
        left += 1;
    }

    grid
}

fn print_grid(grid: &[Vec<Option<usize>>], n: usize) {
    let cell_width = n.to_string().len();

    for row in grid {
        for (col_index, cell) in row.iter().enumerate() {
            if col_index > 0 {
                print!(" ");
            }

            match cell {
                Some(number) => print!("{number:>cell_width$}"),
                None => print!("{:>cell_width$}", ""),
            }
        }

        println!();
    }
}

fn parse_n(args: &[String]) -> Result<usize, String> {
    if args.len() != 2 {
        return Err("Usage: cargo run -- <non-negative integer>".to_string());
    }

    args[1]
        .parse::<usize>()
        .map_err(|_| "Please provide a valid non-negative integer".to_string())
}

fn run(args: &[String]) -> Result<(), String> {
    let n = parse_n(args)?;
    let grid = build_spiral(n);

    print_grid(&grid, n);

    Ok(())
}

fn main() {
    let args: Vec<String> = env::args().collect();

    if let Err(message) = run(&args) {
        eprintln!("{message}");
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn grid_size_returns_one_when_n_is_zero() {
        assert_eq!(grid_size(0), 1);
    }

    #[test]
    fn grid_size_returns_six_when_n_is_thirty() {
        assert_eq!(grid_size(30), 6);
    }

    #[test]
    fn build_spiral_places_values_clockwise_for_five() {
        let grid = build_spiral(5);

        assert_eq!(
            grid,
            vec![
                vec![Some(0), Some(1), Some(2)],
                vec![None, None, Some(3)],
                vec![None, Some(5), Some(4)],
            ]
        );
    }

    #[test]
    fn parse_n_returns_error_when_argument_is_missing() {
        let args = vec!["clockwork_spiral".to_string()];

        let result = parse_n(&args);

        assert!(result.is_err());
    }

    #[test]
    fn parse_n_returns_error_when_argument_is_not_a_number() {
        let args = vec!["clockwork_spiral".to_string(), "hello".to_string()];

        let result = parse_n(&args);

        assert!(result.is_err());
    }
}
```

Run the program:

```bash
cargo run -- 30
```

Run the tests:

```bash
cargo test
```

For linting, run:

```bash
cargo clippy --all-targets --all-features --locked -- -D warnings
```

If this is a tiny practice project and you do not have `Cargo.lock` checked in yet, `--locked` may complain. In that case, run plain `cargo clippy --all-targets --all-features -- -D warnings` while learning, then use `--locked` once the lockfile is in place.

## Why this final version is more idiomatic

The code keeps ownership simple. Functions that only read command-line arguments receive `&[String]`, which is a borrowed slice. `print_grid` receives `&[Vec<Option<usize>>]` for the same reason: it does not need to own the grid.

Errors are returned as `Result` instead of crashing with `unwrap()` or `expect()`. That is the right habit for normal application code. Tests can still use direct assertions because tests are allowed to fail loudly.

The tests are small and named after behavior. When one fails, the name tells you what broke.

Source: this was issue #465 of Rendezvous with Cassidoo.
