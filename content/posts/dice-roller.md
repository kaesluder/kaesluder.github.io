+++
title = 'Mocking or Stubbing With Traits'
date = 2024-03-13T21:06:45-05:00
draft = false
+++

One of the things I've struggled with as a new developer is the problem of mocking or stubbing non-deterministic functions for testing. In bootcamp, I designed a pretty clever statistical test for the validity of scrabble draws, and got "that's interesting, but not the right approach." There are a couple of areas where I've worked with this, and a couple of reasons why stubbing is useful:

1. The statistical test of randomness or network call could fail, for reasons unrelated to the functionality of the code.
2. I don't want to spam the other services involved every time I run the test.

I *also* have a side hobby with ttrpgs, currently [solo ttrpgs](https://www.dicebreaker.com/categories/roleplaying-game/how-to/how-to-play-tabletop-rpgs-by-yourself). These systems typically use dice to determine *if* something interesting happens in the story, and *dice-driven oracles* to give the player an idea about the next plot twist. (Ok, *sometimes* you can use cards.) The genre combines game mechanics and storytelling, which isn't new[^1] but is getting a lot of interesting new ideas lately. Eventually, I want some utilities to use custom oracles.


Credit to [Jimmy Hartzell @ thecodedmessage](https://www.thecodedmessage.com/posts/default-params/) for helping me think about this pattern. In Python or JS I would use a default function argument to change the behavior of a function. Rust doesn't really have that, and is also more picky about passing functions as arguments. But you can pass config structs/objects of different types as long as they have the same interface.

The approach taken here is as follows:

1. Create config structs `Die` and `TestDie`.
2. Create a *trait*, `DiceRoller`. A trait is a function that can be implemented in different ways for different struct types. If a struct type implements `DiceRoller`, you can call any function defined in the signature of `DiceRoller`. In this case, `DiceRoller` specifies one function with a specified signature: `fn generate(&self) -> i32;`
3. Implement `DiceRoller` for both `Die` and `TestDie` by defining `generate()` for each.
4. When I need to use a die, I create a function that takes any struct that implements `DiceRoller`. Within that function, I can call `die.generate()` on either type of struct.

Structs can be created on the fly: `Die {min: 1, max: 6}` or `TestDie {min: -1, max: 1, test_output: 0}`. (Fate/Fudge die.)


```rust
use rand::Rng;

struct Die {
    min: i32,  
    max: i32,
}

struct TestDie {
    min: i32,
    max: i32,
    test_output: i32, 
}

trait DiceRoller {
    fn generate(&self) -> i32;
}

impl DiceRoller for Die {
    fn generate(&self) -> i32 {
        rand::thread_rng().gen_range(self.min..=self.max)
    }
}

impl DiceRoller for TestDie {
    fn generate(&self) -> i32 {
        self.test_output
    }
}

fn roll_dice(dice: &impl DiceRoller, num_rolls: usize) -> Vec<i32> {
    let mut results = Vec::new();

    for _ in 0..num_rolls {
        results.push(dice.generate());
    }

    results
}

fn main() {
    let d6 = Die { min: 1, max: 6 };
    let results = roll_dice(&d6, 5);
    println!("Rolled a 6-sided die 5 times: {:?}", results);

    let test_die = TestDie { min: 1, max: 6, test_output: 3 };
    let test_results = roll_dice(&test_die, 3);
    println!("Rolled a test die with fixed output 3 three times: {:?}", test_results);
}

#[test]
fn test_roll_dice() {
    let test_die = TestDie { min: 1, max: 6, test_output: 3 }; 
    let rolls = roll_dice(&test_die, 4);

    // Ensure all values in the results are equal to the test_output
    assert!(rolls.iter().all(|&x| x == 3)); 
}

```

[^1]: Kieron Gillen and Stephanie Hass traces that combination back through H.G. Wells and the Brontë family in [*Die*](https://imagecomics.com/comics/series/die).
