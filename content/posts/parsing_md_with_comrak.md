+++
title = 'Learning How to Parse Markdown with Comrak and Rust'
date = 2024-04-13T12:39:55-04:00
draft = true
+++

![a black hole swallowing markdown from various PKM systems and spitting out a jet of text and JSON](/images/link_extractor1.png)

Much of my self-organization strategies end up in Markdown using some form of PKM software. As of this post, it's [Obsidian](https://obsidian.md). Since markdown is an annotated file, I'm not limited to just using Obsidian (or my tool of the year) to search and examine my notes. 

So one of the things I keep reinventing with each language I learn are some simple extraction tools. In this case I wanted a command-line program for the following:

- Extract text and urls from external links. 
- Output delimited text that I can parse with other tools such as `awk`, `grep`, and `fzf`.
- Also output JSON in case I want to feed something that reads JSON. 
- Use parsing instead of regex. Regex *superficially* is easier for this case, but comes with a lot of edge cases. Also, I want to learn how to do document processing in Rust for future use, and possibly expand in the future to use DOM-style queries. 

### Comrak 

[Comrak](https://crates.io/crates/comrak) is a tool and library written in Rust for parsing Github Flavored Markdown and Commonmark Markdown. It *also* has the ability to create Abstract Syntax Trees (ASTs), which are a format-agnostic representation of the structure of a file. Using the AST allows me to pretend that markdown has "tags", when it doesn't. And Comrak has a [documented](https://github.com/kivikakk/comrak) method for searching the AST for specific nodes: recursively walk the tree and do something when you hit a target node. 

```rust
// The returned nodes are created in the supplied Arena, and are bound by its lifetime.
let arena = Arena::new();

let root = parse_document(
    &arena,
    "This is my input.\n\n1. Also my input.\n2. Certainly my input.\n",
    &Options::default());

fn iter_nodes<'a, F>(node: &'a AstNode<'a>, f: &F)
    where F : Fn(&'a AstNode<'a>) {
    f(node);
    for c in node.children() {
        iter_nodes(c, f);
    }
}

iter_nodes(root, &|node| {
    match &mut node.data.borrow_mut().value {
        &mut NodeValue::Text(ref mut text) => {
            let orig = std::mem::replace(text, vec![]);
            *text = String::from_utf8(orig).unwrap().replace("my", "your").as_bytes().to_vec();
        }
        _ => (),
    }
});
```

Things that were new to me: 

`let arena = Arena::new();` Naive recursive data structures are difficult to implement in Rust. Each type needs to be owned by something, and having children nodes owned by a parent node gets complicated when the children become parents themselves. The `Arena` type (not covered in The Book) gets around this by creating a structure analogous to a Vec (array, or list in other languages) that owns all the nodes and manages parent-child links.

`fn iter_nodes<'a, F>(node: &'a AstNode<'a>, f: &F)...` While I've used lifetimes in exercises, this was my first use of them in practice. The `'a` type on node ensures that node does not accidentally get destroyed while running a recursive function. 

*Recursion in Rust* First time working with this pattern in Rust, complicated by an implicit base case. If the node has no children, the recursion stops. Also, most of the program logic ends up in a closure. 

## First Attempt

My first attempt is [committed to github](https://github.com/kaesluder/link-extractor/commit/1f6e8c816cc71b8a7ccc3cba57e2c3e0863e77ab). I used recursion to walk the tree for link nodes, and then tried to use iteration to process the contained text nodes. Then I collected all the created Link structs into a variable outside the closure. That raises some issues regarding borrowing and a special reference type.

Lesson learned: It's easier to have the closure return a value that's collected outside than to modify a variable external to the closure.

## Current Version

After a lot of documentation searching I discovered multiple improvements. First I separated the text extraction from the link extraction, because a link can have nested markup. `[_foo_ *bar*](https://example.com)`

```rust 
fn extract_text<'a>(root: &'a AstNode<'a>) -> String {
    // Use `traverse` to get an iterator of `NodeEdge` and process each.
    root.descendants()
        .filter_map(|node| {
            if let NodeValue::Text(ref text) = node.data.borrow().value {
                // If the node is a text node, append its text to `output_text`.
                Some(text.clone())
            } else {
                None
            }
        })
        .collect()
}
```

`root.descendants()` Sometimes when I get over my head I think "there has to be a function that already does this." `AstNode.descendants()` does the recursion for me, giving me an iterator of node references that can be passed to...

`.filter_map()` `filter_map()` does exactly what it looks like, combines filter and map. If the Node is a text node, we crack it open and return the value wrapped in `Some()`. If the node is *not* a text node (em, strong, image, or any other inline markup) the filter side skips over it. 

`.collect()` `.collect()` can transform iterators into multiple types. In this case, since the output for the function is a String, and the node value is a String, `collect()` creates a string. 

The logic for extracting links got a similar treatment, except for simplifying the closure by creating a helper function. Writing it this way helps reduce mutable values and isn't dependent on `RefCells`. 

The next steps (saved for a future blog post, since it's not done) is building a cli app for this that handles input arguments and serialization. 
