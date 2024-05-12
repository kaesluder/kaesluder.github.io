+++
title = 'Rust Benefits for Python Peeps'
date = 2024-05-11T17:03:34Z
draft = false
+++

[Rust](https://www.rust-lang.org) is a growing multi-style programming language that has become popular for its memory safety. Memory safety is a big selling point for Rust vs. C or C++, where developers are expected to write code for managing safety. But I've found many of those features to be useful coming to Rust as a Python hobbyist and developer. 

For most of these, I'm comparing both Python and Rust at a very basic level. There are tools for Python to make it stricter, and tools for Rust to make it more flexible. But those tools usually involve using non-standard packages or metaprogramming at a more complicated level. 

## Run Time vs. Compile Time Type Checking

Python's dynamic type checking assigns types to variables at runtime when an expression is evaluated. This code sample assigns `choice` to `"string"`, `42` or `None`. Then I try to print choice in reversed order. If choice is `string` I print `gnirts` (now with even more fiber for heart health). But if the random function picks `42` or `None`, the `choice[::-1]` (reverse an array) expression will throw an exception. You can't reverse those values.

````python
import random
choice = random.choice(['string', 42, None] ) \\ (1)
print(f'{choice[::-1]}') \\ (2)
````

This can be especially annoying if the variable-as-array expression happens in a different function or even file from the original assignment.  As far as Python is concerned expression (1) is valid, but expression (2) is only *sometimes* wrong. 

The Rust compiler would catch this at both ends. Expression (1) would fail to compile because the values in a `Vec` must be homogenous in terms of type. `choice` must be a type that the compiler can predict (explicitly or implicitly typed). Expression (2) would fail if the value of `choice` doesn't implement the slice operator. 

The Rust compiler ensures that the types of variables *must* remain consistent every time that variable is used. My experience is that the compile-time checking offered by Rust makes errors easy to find without testing multiple edge cases during runtime.

## Standardized Error Types

I introduced `Option` and `Result` in an [earlier post](/posts/cat-option-result/). One (admittedly very minor) pain point in Python for me is "what does this return if there's no answer?" Some of the strategies I've seen (or used myself) include:

1. `None`
2. `-1` 
3. Maximum or minimum integers
4. Throw an exception
5. A result object
6. An empty string
7. An empty list
8. `0`

Running into `None` often feels ambiguous. Is the answer `None`? Does `None` mean the expression couldn't find what I requested?  Or am I getting `None` in Python because I forgot to add a `return` statement? Rust has two standard types to resolve this ambiguity. Functions that return either a value or a null result return an `Option` (`Some(T)` or `None`). Examples of this are hash, substring, or array lookups. Extending the example above, `HashMap.get(key)` returns `Some(value)` if there's a value at `key`. If there's not a value at `key` `HashMap.get()` returns `None`.


```rust
    // Retrieve values from the HashMap
    let test_variable_one = my_dict.get(&'a');
    let test_variable_none = my_dict.get(&'d');

    // Print the values
    println!("{:?}", test_variable_one); // Some(1)
    println!("{:?}", test_variable_none); // None
```

The existence of `Result` or `Option` as the return type of a function is a clear signal that the function may not *always* give me the results I expect, and I need to handle the possibility of an error explicitly.

## Explicit Mutability and Side Effects

One of my favorite features of Rust is explicit control over mutability and side effects. Here's a very naive implementation of a palendrome (same forward and backward) test.

````python
orig = [1, 2, 3]
def is_palendrome(orig): 
    flipped = orig # (1)
    flipped.reverse() # (2)
    return orig == flipped

print(is_palendrome(orig)) # True
print(orig) # orig = [3, 2, 1] (3)
````

Some of the quirks in here include: 

(1) Default assignment by reference. Both `orig` and `flipped` point to the same data.   

(2) In-place modification of `flipped`. `.reversed` returns `None` with the results stored inside the variable. 

(3) Side effect! Both `flipped` and `orig` point to the same object. Changes to `flipped` aldo change `orig` both inside and *outside* the function.

When I try this in Rust, the compiler sees that I'm doing multiple things with orig in the same scope. 

````rust
let orig = vec![1, 2, 3]; // (1) create orig
fn is_palendrome(orig: &Vec<i32>) -> bool {
    let mut flipped = orig.clone(); // (2) clone (copy) orig to preserve it
    flipped.reverse(); // (3) modify the copy
    * orig == flipped // (4) compare flipped to the *value* of orig
}

let result = is_palendrome(&orig);
println!("{:?}, {:?}", orig, result)
````

The Rust compiler is *very* strict about specifying how variables live or are moved in the same scope. In order to mutate flipped at all, I need to declare it mutable and clone the original immutable data. This isn't the best Rust code, it's code that follows the python original for demonstration.

## Summary

Rust offers multiple features in addition to memory safety that help to prevent, identify, and locate errors that would be challenging to troubleshoot at runtime in Python. 




