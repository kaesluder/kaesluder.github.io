+++
title = 'The Cat, The Option, and The Result'
date = 2024-02-21T23:10:58-05:00
draft = true
+++

## Notes on trying to understand Rust Result and Option types using armchair physics.

![Diagram of the Schrödinger's cat thought experiment. A radioactive isotope randomly triggers a detector, which releases poison into a box with a cat inside. The cat in this thought experiment is in a state of quantum superposition.](/images/schrodingers_cat_illustration.png)

## The Cat

Schrödinger's Cat is a famous thought experiment about [quantum superposition](https://scienceexchange.caltech.edu/topics/quantum-science-explained/quantum-superposition). It's not realistic at all, but it's popular one for the memes.

The basic outline of the Schrödinger's cat thought-experiment is:

1. A radioactive atom randomly (based on its half-life) triggers...
2. A sensitive detector or "camera," that releases...
3. Poison gas, into a...
4. Sealed box with a cat.

Now according to quantum mechanics, you have a sealed box with _something_. This is _magical_ sealed box that doesn't release _any_ information about what's inside to the outside world. There are multiple interpretations of what could be inside the box at this stage, but I never got that far in physics. If this was the Marvel Cinematic Universe, the cat-in-a-box would spawn multiple universes to resolve the paradox. The Standard Interpretation (which works very well for atoms) is that the cat is both alive and dead until you open the box (unwrap the cat).

If the atom did not set off this morbid [Rube Goldberg Trap](https://youtu.be/qybUFnY7Y8w?si=e6S-zHJY_FU2Do1z). You'd see a live cat. If the atom did decay, you'd have a dead cat. Regardless of how you interpret your quantum physics, you can't know what's inside (or what universe you're in) until you open the box.

## The Result

In programming, there are a lot of things that can fail. We expect them to fail at least some of the time:

1. "Index all 'z' characters in 'apple.'"
2. "404 Error: The page doesn't exist."
3. "Find 'zyzzyz!g' in the dictionary."

Ways to handle a failure in more dynamic languages:

1. Raise then catch an exception.
2. Return 0.
3. Return -1 (array searching).
4. Return null, nill, or None.
5. Return a data object with a success/failure flag.

Rust doesn't like it when you change types by passing null, nill, or none in some cases and integers or booleans in other cases. Rust has a pre-built type for this. The `Result` type can be Ok(value) or Err(error).


```rust
use rand::random;

fn poisoned_box() -> Result<String, String> {
    match random::<bool>() {
        true => Err("dead".to_string()),
        _ => Ok("alive".to_string()),
    }
}

fn main() {
    let cat_in_box = poisoned_box();
    println!("Opening the box!");
    match cat_in_box {
        Ok(cat) => println!("The cat is {}.", cat),
        Err(e) => println!("Ooops, {} cat.", e),
    }
}
```

In this first sample, we could have just passed a `String` back for both cases. Where `Result` becomes useful when you want to pass different types back. Let's create a `struct` for a live cat that describes name and breed, and a `struct` for a dead cat that has a name and a number of seconds.

```rust
use rand::random;

struct LiveCat {
    name: String,
    breed: String,
}
struct DeadCat {
    name: String,
    time: i32,
}

fn poisoned_box() -> Result<LiveCat, DeadCat> {
    match random::<bool>() {
        true => Err(DeadCat {
            name: "Bill".to_string(),
            time: 325,
        }),
        _ => Ok(LiveCat {
            name: "Bill".to_string(),
            breed: "Shorthair".to_string(),
        }),
    }
}

fn main() {
    let cat_in_box = poisoned_box();
    println!("Opening the box!");
    match cat_in_box {
        Ok(cat) => println!("{} the {} survived the experiment.", cat.name, cat.breed),
        Err(e) => println!("Ooops, {} the cat died after {} seconds.", e.name, e.time),
    }
}
```

## The Option

What if you open the box and the experiment has miraculously transported the cat _somewhere else._ (Somewhen else?) `Option` is good choice for that. For `Option` the values are `Some(value)` and `None`. (`None` is `None` and all alone and ever more shall be it so.)

```rust
use rand::random;

struct LiveCat {
    name: String,
    breed: String,
}

fn poisoned_box() -> Option<LiveCat> {
    match random::<bool>() {
        true => None,
        _ => Some(LiveCat {
            name: "Bill".to_string(),
            breed: "Shorthair".to_string(),
        }),
    }
}

fn main() {
    let cat_in_box = poisoned_box();
    println!("Opening the box!");
    match cat_in_box {
        None => println!("There is no cat. Did you forget?"),
        Some(cat) => println!("{} the {} is alive.", cat.name, cat.breed),
    }
}

```

## Why?

Of course, experimental physics research can be a multi-billion effort involving [hundreds of researchers](https://improbable.com/airchives/classical/articles/peanut_butter_rotation.html). The person opening the box might be a lab assistant or intern responsible for just recording results. Individual results are often aggregated, discussed over the coffee pot, or shared at meetings.

Similarly, errors don't need to be handled by the first function that detects them. One error might be a hiccup, but a dozen might be a network outage or a bug. `Option` and `Result` provide ways to pass responsibility for the handling the error to functions responsible for coordinating inputs, and passing readable results to the user. An email interface might try a request again, following some rate-limiting logic. A user interface might collect multiple failures before informing the user. This is similar to the "ask forgiveness" model favored by python, but encourages the programmer to explicitly handle error conditions (even if handling the error means passing it up to the parent function.)

