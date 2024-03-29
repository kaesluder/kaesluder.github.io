+++
title = 'Rustlings Finished'
date = 2024-03-29T10:51:25-04:00
draft = false
+++

![ASCII art of a rust mascot crab celebrating the completion of rustlings](/images/rustlings_success_screen.png)

I've been putting project work on hold to wrap up some old tasks and attend the [TransTech Summit](https://transtechsummit.com). The biggest achievement of the past week was to get [rustlings](https://github.com/rust-lang/rustlings) wrapped up.

*Rustlings* is a collection of Rust tutorials starting from "Hello, World" to advanced type conversions and working with smart references. My history with tutorial collections and learning books has been to get halfway, get enthusiastic about my own project of the month, and then get into trouble when that project goes over my head. This time around, it was important to wrap up the whole thing before jumping off into something else. 

That's been great because it pushed me into areas I probably would have skipped. And, surprise surprise, those concepts turned up central to my next project of attempting to pull data out of markdown docs.

Rustlings takes a bit of a different approach from other tutorials I've seen. Rather than giving you a project to build from scratch, a rustlings exercise gives you code that fails compiler and/or unit tests. You also get a brief introduction to the problem and a hint to get started. On the good side, one of the selling points of Rust is great (or at least better) error messages that help direct users to the solutions. Working through Rustlings made me very comfortable interpreting compiler errors. On the bad side, some of the introductions and hints still left me wondering what exactly where to explore for a solution. 

The exercises make heavy use of [The Rust Book](https://doc.rust-lang.org/book/) (aka *The Rust Programming Language*)as a reference. At higher level, I ran into exercises where the rustlings examples differed from The Book's examples in ways that made understanding the lesson more difficult.  This was only a small speedbump overall though. I might look into filing some issues and PRs if I get the bandwidth.

Next steps: I *had* been looking at getting back started with my [streaming radio player](https://github.com/kaesluder/radiogaga) which is functional but can use multiple improvements. But I got a little bit side tracked into writing a tool for extracting links from markdown files. This is a job where it's easy to just use a regex that will do the right thing 90% of the time. Doing it right involves parsing markdown into a DOM or AST, and pulling the links from that. This hits one of the "hard" areas of Rust: managing nodes in linked lists and trees. I have a solution using [comrak](https://github.com/kivikakk/comrak), but I feel I can do a lot better handling trees. I work with enough markdown to make it worth my time. 
