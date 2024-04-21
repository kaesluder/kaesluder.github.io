+++
title = 'Rust Benefits for Python Peeps'
date = 2024-04-20T17:03:34Z
draft = true
+++

[Rust](https://www.rust-lang.org) is a growing multi-style programming language that has become popular for its memory safety. Memory safety is a big selling point for Rust vs. C or C++, where developers are expected to write code for managing safety. But I've found many of those features to be useful coming to Rust as a Python hobbyist and developer. 

## Run Time vs. Compile Time Type Checking

In vanilla Python, variables are given a type as they are used at run time. The `dict.get(key)` function in Python returns the value stored at `dict[key]` if it exists, or `None` if it doesn't. In this code example, `test_variable_one` is set to `1`, while `test_variable_none` is set to `None`. Both the type *and* value of the variables are defined at runtime. In each value in a python dict can be a different type. 

```python
my_dict = {'a': 1, 'b': 2, 'c': '3'}
test_variable_one = my_dict.get('a')
test_variable_none = my_dict.get('d')
print(test_variable_one) # '1'
print(test_variable_none) # 'None'
```

In Rust, variable types need to be known at runtime. The following code block won't compile because I've declared `my_dict` to use character values as keys and integers as values. The code is trying to insert a character into a slot designed for an integer. It will also fail if I try to use a variable that *could* be a string, character, or floating-point number. 

```rust
use std::collections::HashMap;

fn main() {

    let mut my_dict: HashMap<char, i32> = HashMap::new(); 
    // type declaration added for clarity
    my_dict.insert('a', 1);
    my_dict.insert('b', 2);
    my_dict.insert('c', '3');
    ...
}
```

````
   Compiling playground v0.0.1 (/playground)
error[E0308]: mismatched types
    --> src/main.rs:8:25
     |
8    |     my_dict.insert('c', '3');
     |             ------      ^^^ expected `i32`, found `char`
     |             |
     |             arguments to this method are incorrect
     |
help: the return type of this call is `char` due to the type of the argument passed
````

With Python, many exceptions involving mis-matched types are only thrown at runtime. Triggering this type of error in development requires identifying and testing edge and corner cases. With Rust, I sacrifice some flexibility in favor of identifying bugs much earlier in development.

(Yes, there are generics in Rust, if I choose to use them explicitly.)


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

Running into `None` often feels ambiguous. Is the answer `None`? Does `None` mean "I didn't find it?" Or am I getting `None` in Python because I forgot to add a `return` statement? Rust has two standard types to resolve this ambiguity. Functions that return either a value or a null result return an `Option` (`Some(T)` or `None`). Examples of this are hash, substring, or array lookups. Extending the example above, `HashMap.get(key)` returns `Some(value)` if there's a value at `key`. If there's not a value at `key` `HashMap.get()` returns `None`.


```rust
    // Retrieve values from the HashMap
    let test_variable_one = my_dict.get(&'a');
    let test_variable_none = my_dict.get(&'d');

    // Print the values
    println!("{:?}", test_variable_one); // Some(1)
    println!("{:?}", test_variable_none); // None
```

`Result` comes in handy when I'm looking for success/failure or when there's multiple failure conditions. `str.parse::<i32>()` returns `Ok(value)` if the `str` can be converted to a valid `i32`. If the `str` can't be converted, `str.parse::<i32>()` returns `Err(error)`. In this case, handling `InvalidDigit` and `Invalid` can provide different feedback, or be substituted with a reasonable default value. 

```rust
println!("{:?}", "432".parse::<i32>());
println!("{:?}", "four hundred and thirty two".parse::<i32>());
println!("{:?}", "Ok432".parse::<f32>());
```

```
Ok(432)
Err(ParseIntError { kind: InvalidDigit })
Err(ParseFloatError { kind: Invalid })    
```


