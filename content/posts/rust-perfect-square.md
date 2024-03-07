+++
title = 'Rust Perfect Square'
date = 2024-03-06T22:01:25-05:00
draft = false
+++

A number is a perfect square if `x * x = n` where `x` and `n` are both integers.  With Rust, I have a few minor twists:

1. Rust doesn't have an integer square root function in the standard library (although I could always download one). There is a float square root function, but that could introduce some errors. It's good reason to practice a binary search anyway.
2. Large values can produce an [integer overflow](https://doc.rust-lang.org/book/ch03-02-data-types.html) error or an unannounced overflow. `mid.checked_mul(mid)` returns `Some(square)` if the multiplication is successful and `None` if it overflows.  


```rust
fn is_square(n: i64) -> bool {
    println!("{}", n);
    if n < 0 {
        return false;
    }

    if n == 0 || n == 1 {
        return true;
    }

    let mut low: i64 = 0;
    let mut high = n / 2;

    while low <= high {
        let mid: i64 = (low + high) / 2;

        // checked_mul returns Some(square) if successful, None if overflow.
        match mid.checked_mul(mid) {
            Some(square) if square == n => return true, // match target
            Some(square) if square < n => low = mid + 1, // match less than
            Some(_) => high = mid - 1,                  // match greater than
            None => high = mid - 1,                     // integer overflow fallback
        }
    }

    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_square_true() {
        assert!(is_square(4));
        assert!(is_square(25));
        assert!(is_square(1)); // test one
        assert!(is_square(0)); // test zero
    }
    #[test]
    fn test_is_square_false() {
        assert!(!is_square(5));
        assert!(!is_square(3));
        assert!(!is_square(26));
        assert!(!is_square(i64::MAX)); // test overflow
        assert!(!is_square(-4)); // test negative number
    }
}
```
