"""
Management command to seed the database with exercise content.
Run with: python manage.py seed_exercises
"""
import ast

from django.core.management.base import BaseCommand
from core.models import Day, Exercise

DAYS_DATA = [
    {
        'number': 1,
        'title': 'Bases & Syntaxe',
        'description': 'Variables, mutability, primitive types, control flow (if, match, loops), and functions.',
        'is_critical': True, 'passing_threshold': 100,
        'language': 'rust',
        'exercises': [
            {
                'number': 0, 'title': 'hello', 'difficulty': 'easy',
                'description': 'Write a function that PRINTS "Hello, Rust!" to the standard output using println!.',
                'examples': 'hello()\n// Output: Hello, Rust!',
                'tutorial': '### First Steps with Rust (EN)\nIn Rust, printing to the terminal is generally done with the `println!` **macro**. A macro can be identified by the exclamation mark `!` at the end.\n```rust\nfn main() {\n    println!("Hello");\n}\n```\n### Best Practices (Clean Code)\n- **Semantics over mechanics**: Name your variables and functions according to what they express, not how they do it.\n- Avoid cluttering obvious code with comments.\n- Prefer a standard formatting enforced by `cargo fmt`.\n\n---\n### Premier contact avec Rust (FR)\nEn Rust, l\'affichage se fait avec la **macro** `println!`. Une macro se reconnaît à son point d\'exclamation `!` à la fin.\n```rust\nfn main() {\n    println!("Bonjour");\n}\n```\n### Bonnes Pratiques (Clean Code)\n- **Sémantique plutôt que mécanique** : Nommez vos variables et fonctions selon ce qu\'elles expriment, pas comment elles le font.\n- Evitez de surcharger de commentaires ce qui est évident.\n- Préférez un formattage standard imposé par `cargo fmt`.',
                'function_signature': 'fn hello()',
                'starter_code': 'pub fn hello() {\n    // Print "Hello, Rust!" to stdout\n}\n',
            },
            {
                'number': 1, 'title': 'add_numbers', 'difficulty': 'easy',
                'description': 'Write a function that takes two i32 integers and RETURNS their sum.',
                'examples': 'add_numbers(2, 3)  -> 5\nadd_numbers(-1, 1) -> 0\nadd_numbers(0, 0)  -> 0',
                'tutorial': '### Functions and Returns (EN)\nThe specific trait of Rust is that the **last expression of a block**, if it doesn\'t have a semicolon (`;`), is automatically returned!\n### Best Practices in Rust\n- **Implicit return**: Not using `return` at the end of a function is a strong (idiomatic) convention in Rust.\n- **Strict Typing**: Unlike dynamic languages, Rust\'s strictness on perfect input and output type matching saves countless bugs in production. Keep clear signatures.\n\n---\n### Les Fonctions et les Retours (FR)\nLa particularité de Rust est que la **dernière expression d\'un bloc**, si elle n\'a pas de point-virgule (`;`), est automatiquement retournée !\n### Bonnes Pratiques en Rust\n- **Retour implicite** : Ne pas utiliser `return` en fin de fonction est une convention forte (idiomatique) en Rust.\n- **Typage Strict** : Contrairement aux langages dynamiques, l\'exigence de Rust sur l\'accord parfait des types en entrée et en sortie sauve un nombre infini de bugs en production. Gardez des signatures claires.',
                'function_signature': 'fn add_numbers(a: i32, b: i32) -> i32',
                'starter_code': 'pub fn add_numbers(a: i32, b: i32) -> i32 {\n    // TODO\n}\n',
            },
            {
                'number': 2, 'title': 'is_even', 'difficulty': 'easy',
                'description': 'Write a function that takes an i32 and RETURNS true if the number is even, false otherwise.',
                'examples': 'is_even(4)  -> true\nis_even(7)  -> false\nis_even(0)  -> true\nis_even(-2) -> true',
                'tutorial': '### Modulo Operations and Booleans (EN)\nThe modulo operator `%` gives the remainder of a division. A number is even if the remainder of its division by 2 is 0.\n```rust\nfn is_positive(n: i32) -> bool {\n    n > 0\n}\n```\n\n---\n### Les Opérations Modulo et Booléens (FR)\nL\'opérateur modulo `%` donne le reste d\'une division. Un nombre est pair si le reste de sa division par 2 est 0.\n```rust\nfn est_positif(n: i32) -> bool {\n    n > 0\n}\n```',
                'function_signature': 'fn is_even(n: i32) -> bool',
                'starter_code': 'pub fn is_even(n: i32) -> bool {\n    // TODO\n}\n',
            },
            {
                'number': 3, 'title': 'fizzbuzz', 'difficulty': 'easy',
                'description': 'Write a function that takes a u32 and RETURNS a String:\n- "fizzbuzz" if divisible by both 3 and 5\n- "fizz" if divisible by 3 only\n- "buzz" if divisible by 5 only\n- the number as string otherwise',
                'examples': 'fizzbuzz(3)  -> "fizz"\nfizzbuzz(5)  -> "buzz"\nfizzbuzz(15) -> "fizzbuzz"\nfizzbuzz(7)  -> "7"',
                'tutorial': '### Conditions and Conversions (EN)\nIn Rust, `if / else if / else` blocks do not need parentheses around the condition.\nTo create a `String` from text, we use `.to_string()`.\n### Pattern Matching Best Practices\n- **Match vs If-Else**: In Rust, as soon as conditions multiply, it is *highly recommended* to use the `match` block. This "pattern matching" requires the compiler to verify that **all possible branches** are handled (exhaustiveness), which a chain of if-else does not guarantee.\n\n---\n### Conditions et conversions (FR)\nEn Rust, les blocs `if / else if / else` n\'ont pas besoin de parenthèses autour de la condition.\nPour créer une `String` à partir d\'un texte, on utilise `.to_string()`.\n### Bonnes Pratiques et Pattern Matching\n- **Match vs If-Else** : En Rust, dès que les conditions se multiplient, il est *hautement recommandé* d\'utiliser le bloc `match`. Ce "pattern matching" demande au compilateur de vérifier que **toutes les branches possibles** sont traitées (exhaustivité), ce qu\'un enchaînement de if-else ne garantit pas.',
                'function_signature': 'fn fizzbuzz(n: u32) -> String',
                'starter_code': 'pub fn fizzbuzz(n: u32) -> String {\n    // TODO\n}\n',
            },
            {
                'number': 4, 'title': 'factorial', 'difficulty': 'medium',
                'description': 'Write a recursive function that computes n! (factorial) and RETURNS the result as u64.\n\nfactorial(0) = 1 and factorial(n) = n * factorial(n-1).',
                'examples': 'factorial(0)  -> 1\nfactorial(5)  -> 120\nfactorial(10) -> 3628800',
                'function_signature': 'fn factorial(n: u64) -> u64',
                'starter_code': 'pub fn factorial(n: u64) -> u64 {\n    // TODO\n}\n',
            },
            {
                'number': 5, 'title': 'celsius_to_fahrenheit', 'difficulty': 'easy',
                'description': 'Write a function that converts Celsius to Fahrenheit and RETURNS the result as f64.\n\nFormula: F = C * 9/5 + 32',
                'examples': 'celsius_to_fahrenheit(0.0)   -> 32.0\ncelsius_to_fahrenheit(100.0) -> 212.0\ncelsius_to_fahrenheit(-40.0) -> -40.0',
                'function_signature': 'fn celsius_to_fahrenheit(celsius: f64) -> f64',
                'starter_code': 'pub fn celsius_to_fahrenheit(celsius: f64) -> f64 {\n    // TODO\n}\n',
            },
        ],
    },
    {
        'number': 2,
        'title': 'Ownership, Borrowing & Lifetimes',
        'description': 'Learn how Rust manages memory without a garbage collector. Ownership rules, borrowing with & and &mut, lifetimes, slices and references.',
        'is_critical': True, 'passing_threshold': 100,
        'language': 'rust',
        'exercises': [
            {
                'number': 0, 'title': 'first_word', 'difficulty': 'easy',
                'description': 'Write a function that takes a string slice &str and RETURNS the first word (delimited by spaces) as a &str. Skip leading spaces. Return empty string if input is empty.',
                'examples': 'first_word("hello world") -> "hello"\nfirst_word("rust")         -> "rust"\nfirst_word("")             -> ""',
                'tutorial': '### Ownership and References (EN)\nUnlike C (pointers) or Python (Garbage Collector), Rust manages memory via *Ownership* rules.\nEach value has a single owner. When it goes out of scope, the memory is freed.\n### Best Practices (Clean Code)\n- Using borrows (`&`) is the core mechanism of optimization (0-cost abstractions).\n- Never clone `my_string.clone()` just for the sake of avoiding compiler issues. Always ask yourself: "Do I really need absolute control over this data or is a simple read enough?".\n\n---\n### L\'Ownership et les Références (FR)\nContrairement à C (pointeurs) ou Python (Garbage Collector), Rust gére la mémoire via des règles d\'*Ownership* (Propriété).\nChaque valeur a un propriétaire unique. Quand il sort de la portée, la mémoire est libérée.\n### Bonnes Pratiques (Clean Code)\n- L\'utilisation des emprunts (`&`) est le mécanisme central de l\'optimisation (0-cost abstractions). \n- Ne clonez jamais `ma_string.clone()` pour le plaisir d\'éviter les soucis de compilateurs. Demandez-vous toujours: "Ai-je vraiment besoin du contrôle absolu sur ces données ou une simple lecture suffit-elle ?".',
                'function_signature': "fn first_word(s: &str) -> &str",
                'starter_code': "pub fn first_word(s: &str) -> &str {\n    // TODO\n}\n",
            },
            {
                'number': 1, 'title': 'concat_strings', 'difficulty': 'easy',
                'description': 'Write a function that takes two &str parameters and RETURNS a new owned String that is their concatenation.',
                'examples': 'concat_strings("hello", " world") -> "hello world"\nconcat_strings("", "rust")         -> "rust"',
                'function_signature': 'fn concat_strings(a: &str, b: &str) -> String',
                'starter_code': 'pub fn concat_strings(a: &str, b: &str) -> String {\n    // TODO\n}\n',
            },
            {
                'number': 2, 'title': 'swap_values', 'difficulty': 'medium',
                'description': 'Write a function that takes two mutable references &mut i32 and MODIFIES them by swapping their values in place. This function does not return anything.',
                'examples': 'let mut a = 1;\nlet mut b = 2;\nswap_values(&mut a, &mut b);\n// a == 2, b == 1',
                'tutorial': '### Mutable References (&mut) (EN)\nBy default in Rust, a borrow `&` is immutable. You can only read.\nTo be able to modify the pointed value, we use `&mut`. You can dereference a pointer with `*` to write to it:\n```rust\nfn add_one(value: &mut i32) {\n    *value = *value + 1;\n}\n```\n\n---\n### Les Références Muables (&mut) (FR)\nPar défaut, en Rust, l\'emprunt `&` est immuable. On ne peut que lire.\nPour pouvoir modifier la valeur pointée, on utilise `&mut`. Vous pouvez déréférencer un pointeur avec `*` pour y écrire :\n```rust\nfn ajouter_un(valeur: &mut i32) {\n    *valeur = *valeur + 1;\n}\n```',
                'function_signature': 'fn swap_values(a: &mut i32, b: &mut i32)',
                'starter_code': 'pub fn swap_values(a: &mut i32, b: &mut i32) {\n    // TODO\n}\n',
            },
            {
                'number': 3, 'title': 'longest', 'difficulty': 'hard',
                'description': 'Write a function that takes two string slices and RETURNS the longest one. If equal length, return the first. You will need lifetime annotations.',
                'examples': 'longest("hello", "hi")   -> "hello"\nlongest("hi", "hello")   -> "hello"\nlongest("same", "size")  -> "same"',
                'tutorial': '### Introduction to Lifetimes (EN)\nWhen a function returns a reference, the compiler must know how long this reference will be valid.\nWe then use "Lifetimes", noted with an apostrophe `\'a`.\n```rust\nfn return_first<\'a>(x: &\'a str, y: &\'a str) -> &\'a str {\n    x\n}\n```\nThis tells the compiler: "The result will live as long as x and y".\n\n---\n### Introduction aux Lifetimes (FR)\nQuand une fonction retourne une référence, le compilateur doit savoir combien de temps cette référence sera valide.\nOn utilise alors les "Lifetimes" (durées de vie), notées avec une apostrophe `\'a`.\n```rust\nfn retourne_premier<\'a>(x: &\'a str, y: &\'a str) -> &\'a str {\n    x\n}\n```\nCela dit au compilateur : "Le résultat vivra aussi longtemps que x et y".',
                'function_signature': "fn longest<'a>(a: &'a str, b: &'a str) -> &'a str",
                'starter_code': "pub fn longest<'a>(a: &'a str, b: &'a str) -> &'a str {\n    // TODO\n}\n",
            },
            {
                'number': 4, 'title': 'count_chars', 'difficulty': 'easy',
                'description': 'Write a function that takes a &str and RETURNS the count of characters (not bytes) as usize. The function borrows the string, it does not take ownership.',
                'examples': 'count_chars("hello") -> 5\ncount_chars("")      -> 0\ncount_chars("hé!!")   -> 4',
                'function_signature': 'fn count_chars(s: &str) -> usize',
                'starter_code': 'pub fn count_chars(s: &str) -> usize {\n    // TODO\n}\n',
            },
        ],
    },
    {
        'number': 3,
        'title': 'Structs, Enums & Pattern Matching',
        'description': 'Custom types with structs and impl blocks, enums with data, match expressions, Option, Result, and trait implementation.',
        'is_critical': False, 'passing_threshold': 80,
        'language': 'rust',
        'exercises': [
            {
                'number': 0, 'title': 'Rectangle', 'difficulty': 'easy',
                'description': 'Create a struct Rectangle with width and height (f64). Implement methods:\n- new(width, height) -> Rectangle : RETURNS a new rectangle\n- area(&self) -> f64 : RETURNS the area\n- perimeter(&self) -> f64 : RETURNS the perimeter\n- is_square(&self) -> bool : RETURNS true if it is a square',
                'examples': 'Rectangle::new(10.0, 5.0).area()      -> 50.0\nRectangle::new(10.0, 5.0).perimeter()  -> 30.0\nRectangle::new(5.0, 5.0).is_square()   -> true',
                'tutorial': '### Structs (EN)\nLike in C, `struct` allows you to group data together.\nIn Rust, you can attach methods to them via the `impl` block. `&self` is the equivalent of `this`.\n```rust\nstruct Point {\n    x: i32,\n}\nimpl Point {\n    fn position(&self) -> i32 { self.x }\n}\n```\n\n---\n### Les Structs (FR)\nComme en C, les `struct` permettent de regrouper des données.\nEn Rust, on peut y attacher des méthodes via le bloc `impl`. `&self` est l\'équivalent de `this`.\n```rust\nstruct Point {\n    x: i32,\n}\nimpl Point {\n    fn position(&self) -> i32 { self.x }\n}\n```',
                'function_signature': 'struct Rectangle { width: f64, height: f64 }',
                'starter_code': 'pub struct Rectangle {\n    pub width: f64,\n    pub height: f64,\n}\n\nimpl Rectangle {\n    pub fn new(w: f64, h: f64) -> Rectangle { todo!() }\n    pub fn area(&self) -> f64 { todo!() }\n    pub fn perimeter(&self) -> f64 { todo!() }\n    pub fn is_square(&self) -> bool { todo!() }\n}\n',
            },
            {
                'number': 1, 'title': 'Color', 'difficulty': 'medium',
                'description': 'Create an enum Color with variants Red, Green, Blue, Custom(u8, u8, u8).\n\nImplement the Display trait so formatting a Color DISPLAYS its hex code.',
                'examples': 'format!("{}", Color::Red)              -> "#FF0000"\nformat!("{}", Color::Green)            -> "#00FF00"\nformat!("{}", Color::Custom(255,128,0)) -> "#FF8000"',
                'function_signature': 'enum Color { Red, Green, Blue, Custom(u8, u8, u8) }',
                'starter_code': 'use std::fmt;\n\npub enum Color {\n    Red, Green, Blue, Custom(u8, u8, u8),\n}\n\nimpl fmt::Display for Color {\n    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {\n        // TODO\n    }\n}\n',
            },
            {
                'number': 2, 'title': 'Calculator', 'difficulty': 'medium',
                'description': 'Create an enum Operation with variants Add(f64, f64), Subtract(f64, f64), Multiply(f64, f64), Divide(f64, f64).\n\nWrite a function calculate that takes an Operation and RETURNS the result as f64.',
                'examples': 'calculate(Operation::Add(2.0, 3.0))     -> 5.0\ncalculate(Operation::Multiply(3.0, 7.0)) -> 21.0',
                'function_signature': 'fn calculate(op: Operation) -> f64',
                'starter_code': 'pub enum Operation {\n    Add(f64, f64), Subtract(f64, f64),\n    Multiply(f64, f64), Divide(f64, f64),\n}\n\npub fn calculate(op: Operation) -> f64 {\n    // TODO\n}\n',
            },
            {
                'number': 3, 'title': 'Linked List', 'difficulty': 'hard',
                'description': 'Implement a singly-linked list using a recursive enum and Box<T>.\n\nEnum List: Nil, Cons(i32, Box<List>).\n- new() -> List : RETURNS empty list\n- push(self, val) -> List : RETURNS new list with val prepended\n- len(&self) -> usize : RETURNS length\n- to_vec(&self) -> Vec<i32> : RETURNS all elements as a Vec',
                'examples': 'List::new().push(1).push(2).len() -> 2\nList::new().push(1).push(2).push(3).to_vec() -> [3, 2, 1]',
                'function_signature': 'enum List { Nil, Cons(i32, Box<List>) }',
                'starter_code': 'pub enum List {\n    Nil, Cons(i32, Box<List>),\n}\n\nimpl List {\n    pub fn new() -> List { todo!() }\n    pub fn push(self, val: i32) -> List { todo!() }\n    pub fn len(&self) -> usize { todo!() }\n    pub fn to_vec(&self) -> Vec<i32> { todo!() }\n}\n',
            },
            {
                'number': 4, 'title': 'Option Operations', 'difficulty': 'medium',
                'description': 'Write two functions working with Option<i32>:\n\n1. double_option: RETURNS the value doubled if Some, None if None\n2. add_options: RETURNS Some(a+b) if both are Some, None otherwise',
                'examples': 'double_option(Some(5))         -> Some(10)\ndouble_option(None)            -> None\nadd_options(Some(3), Some(4))  -> Some(7)\nadd_options(Some(3), None)     -> None',
                'tutorial': '### The Option Enum (EN)\nRust does not have a `null` value! Instead, it uses the `Option` enum which has two states: `Some(val)` or `None`.\n### Best Practices: Handling Absolute Zero\n- The absence of conditional null-checks (`if x == null`) forces the developer to formally handle inexistence.\n- **Do not panic**: Flee `unwrap()` and `expect()` in the final code. Implement fallbacks via `.unwrap_or()` or propagate the Option.\n\n---\n### L\'enumération Option (FR)\nRust n\'a pas de valeur `null` ! À la place, on utilise l\'enumération `Option` qui a deux états : `Some(val)` ou `None`.\n### Bonnes Pratiques : Gestion du Zéro Absolu\n- L\'absence de structuration conditionnelle null-checks (`if x == null`) force le développeur à gérer formellement l\'inexistence.\n- **Ne pas paniquer** : Fuir `unwrap()` et `expect()` dans le code final. Implémentez des "fallbacks" via `.unwrap_or()` ou propagez l\'Option.',
                'function_signature': 'fn double_option(opt: Option<i32>) -> Option<i32>',
                'starter_code': 'pub fn double_option(opt: Option<i32>) -> Option<i32> {\n    // TODO\n}\n\npub fn add_options(a: Option<i32>, b: Option<i32>) -> Option<i32> {\n    // TODO\n}\n',
            },
        ],
    },
    {
        'number': 4,
        'title': 'Collections, Iterators & Errors',
        'description': 'Work with Vec, HashMap. Master iterators and error handling concepts.',
        'is_critical': False, 'passing_threshold': 80,
        'language': 'rust',
        'exercises': [
            {
                'number': 0, 'title': 'unique_elements', 'difficulty': 'easy',
                'description': 'Write a function that takes a Vec<i32> and RETURNS a new Vec<i32> with duplicates removed. Order does not matter.',
                'examples': 'unique_elements(vec![1,2,2,3]) -> [1, 2, 3] (any order)\nunique_elements(vec![5,5,5])   -> [5]',
                'function_signature': 'fn unique_elements(v: Vec<i32>) -> Vec<i32>',
                'starter_code': 'use std::collections::HashSet;\n\npub fn unique_elements(v: Vec<i32>) -> Vec<i32> {\n    // TODO\n}\n',
            },
            {
                'number': 1, 'title': 'word_count', 'difficulty': 'medium',
                'description': 'Write a function that takes a &str and RETURNS a HashMap<String, usize> mapping each word to its count.',
                'examples': 'word_count("hello world hello")\n  -> {"hello": 2, "world": 1}\nword_count("") -> {}',
                'function_signature': 'fn word_count(s: &str) -> HashMap<String, usize>',
                'starter_code': 'use std::collections::HashMap;\n\npub fn word_count(s: &str) -> HashMap<String, usize> {\n    // TODO\n}\n',
            },
            {
                'number': 2, 'title': 'my_map', 'difficulty': 'easy',
                'description': 'Write a function that takes a Vec<i32> and a closure, applies the closure to each element, and RETURNS a new Vec<i32>. Do NOT use the built-in .map() method.',
                'examples': 'my_map(vec![1,2,3], |x| x * 2)  -> [2, 4, 6]\nmy_map(vec![1,2,3], |x| x + 10) -> [11, 12, 13]',
                'function_signature': 'fn my_map<F: Fn(i32) -> i32>(v: Vec<i32>, f: F) -> Vec<i32>',
                'starter_code': 'pub fn my_map<F: Fn(i32) -> i32>(v: Vec<i32>, f: F) -> Vec<i32> {\n    // TODO: do NOT use .map()\n}\n',
            },
            {
                'number': 3, 'title': 'parse_number', 'difficulty': 'easy',
                'description': 'Write a function that takes a &str and RETURNS Result<i32, String>.\nReturn Ok(value) if the string is a valid integer, Err with an error message otherwise.',
                'examples': 'parse_number("42")  -> Ok(42)\nparse_number("abc") -> Err("...")\nparse_number("")    -> Err("...")',
                'tutorial': '### Error Handling: Result (EN)\n### Robustness Best Practices\n- `Result` enforces *explicit* error handling.\n- It is idiomatic to use the special `?` operator at the end of a call that returns `Result`. This avoids a giant `match` and lets errors "bubble up" transparently.\n- Creating clean errors: Instead of system panics that kill your DB or WebServer\'s current thread, return your own Custom Error Objects. Let your dependencies surface to the top.\n\n---\n### La Gestion des Erreurs : Result (FR)\n### Bonnes Pratiques de Robustesse\n- `Result` force la gestion des erreurs *explicite*.\n- Il est idiomatique d\'utiliser l\'opérateur spécial `?` à la fin d\'un appel qui renvoie `Result`. Cela évite un `match` gigantesque et fait "bubbler" les erreurs de façon totalement transparente.\n- Création d\'erreurs propres : Au lieu des paniques système qui tuent le thread courant de votre DB ou WebServer, renvoyez vos propres Objets Custom Errors. Laissez vos dépendances faire surface au sommet.',
                'function_signature': 'fn parse_number(s: &str) -> Result<i32, String>',
                'starter_code': 'pub fn parse_number(s: &str) -> Result<i32, String> {\n    // TODO\n}\n',
            },
            {
                'number': 4, 'title': 'safe_divide', 'difficulty': 'easy',
                'description': 'Write a function that divides two f64 numbers and RETURNS Result<f64, String>.\nReturn Err when dividing by zero.',
                'examples': 'safe_divide(10.0, 2.0) -> Ok(5.0)\nsafe_divide(10.0, 0.0) -> Err("division by zero")',
                'function_signature': 'fn safe_divide(a: f64, b: f64) -> Result<f64, String>',
                'starter_code': 'pub fn safe_divide(a: f64, b: f64) -> Result<f64, String> {\n    // TODO\n}\n',
            },
        ],
    },
    {
        'number': 5,
        'title': 'Mathématiques & Logique',
        'description': 'Application of Rust to basic mathematics: GCD, Primes, Collatz, etc.',
        'is_critical': False, 'passing_threshold': 80,
        'language': 'rust',
        'exercises': [
            {
                'number': 0, 'title': 'is_prime', 'difficulty': 'easy',
                'description': 'Write a function that takes a u64 and RETURNS true if it is a prime number, false otherwise.\nOptimize to avoid checking factors above the square root of n.',
                'examples': 'is_prime(2)  -> true\nis_prime(4)  -> false\nis_prime(17) -> true\nis_prime(1)  -> false',
                'tutorial': '### Mathematics Application in Rust (EN)\nIn these exercises, you will practice basic mathematical algorithms, which is perfect for mastering the logic of loops and return types in Rust. Remember to limit your search loops so as not to blow up the computation time!\n\n---\n### Application Mathématiques en Rust (FR)\nDans ces exercices, vous allez pratiquer l\'algorithmie mathématique de base, ce qui est parfait pour bien prendre en main la logique des boucles et des types de retour en Rust. Pensez à limiter vos boucles de recherche pour ne pas faire exploser le temps de calcul !',
                'function_signature': 'fn is_prime(n: u64) -> bool',
                'starter_code': 'pub fn is_prime(n: u64) -> bool {\n    // TODO\n}\n',
            },
            {
                'number': 1, 'title': 'gcd', 'difficulty': 'medium',
                'description': 'Write a function to compute the Greatest Common Divisor (GCD) of two u64 numbers using the Euclidean algorithm. RETURNS the GCD.',
                'examples': 'gcd(48, 18)   -> 6\ngcd(101, 103) -> 1\ngcd(54, 24)   -> 6',
                'function_signature': 'fn gcd(mut a: u64, mut b: u64) -> u64',
                'starter_code': 'pub fn gcd(mut a: u64, mut b: u64) -> u64 {\n    // TODO: Euclidean algorithm\n}\n',
            },
            {
                'number': 2, 'title': 'lcm', 'difficulty': 'easy',
                'description': 'Write a function to compute the Least Common Multiple (LCM) of two u64 numbers. RETURNS the LCM.\nHint: Use your GCD logic.',
                'examples': 'lcm(21, 6)   -> 42\nlcm(4, 6)    -> 12',
                'function_signature': 'fn lcm(a: u64, b: u64) -> u64',
                'starter_code': 'pub fn lcm(a: u64, b: u64) -> u64 {\n    // TODO\n}\n',
            },
            {
                'number': 3, 'title': 'collatz_length', 'difficulty': 'medium',
                'description': 'Write a function that takes a u64 (n >= 1) and RETURNS the number of steps to reach 1 following the Collatz conjecture rules:\n- If even: n = n / 2\n- If odd: n = 3 * n + 1',
                'examples': 'collatz_length(1)  -> 0\ncollatz_length(12) -> 9\ncollatz_length(19) -> 20',
                'function_signature': 'fn collatz_length(mut n: u64) -> u64',
                'starter_code': 'pub fn collatz_length(mut n: u64) -> u64 {\n    // TODO\n}\n',
            },
            {
                'number': 4, 'title': 'fast_power', 'difficulty': 'medium',
                'description': 'Write a function to efficiently compute (base ^ power) % modulo using Exponentiation by Squaring. RETURNS the Result.',
                'examples': 'fast_power(2, 10, 1000) -> 24\nfast_power(3, 5, 10)    -> 3\nfast_power(5, 0, 7)     -> 1',
                'function_signature': 'fn fast_power(base: u64, power: u64, modulo: u64) -> u64',
                'starter_code': 'pub fn fast_power(mut base: u64, mut power: u64, modulo: u64) -> u64 {\n    // TODO: O(log n) complexity\n}\n',
            },
        ],
    },
    {
        'number': 6,
        'title': 'Algorithms & Problem Patterns',
        'description': 'Classic algorithmic patterns: sliding window, two pointers, binary search, BFS/DFS, dynamic programming, greedy, graphs, heaps, and union-find.',
        'is_critical': False, 'passing_threshold': 80,
        'language': 'rust',
        'exercises': [
            {
                'number': 0, 'title': 'two_sum', 'difficulty': 'easy',
                'description': 'Two Pointers: given a sorted slice and a target, RETURN the indices of two numbers that add up to the target. Use the two-pointer technique.',
                'examples': 'two_sum(&[1, 2, 7, 11, 15], 9) -> (1, 2)\ntwo_sum(&[2, 3, 4], 6)         -> (0, 2)',
                'function_signature': 'fn two_sum(nums: &[i32], target: i32) -> (usize, usize)',
                'starter_code': 'pub fn two_sum(nums: &[i32], target: i32) -> (usize, usize) {\n    // TODO: sorted input, use two pointers\n}\n',
            },
            {
                'number': 1, 'title': 'binary_search', 'difficulty': 'medium',
                'has_timeout': True, 'timeout_seconds': 5,
                'performance_notes': 'Must be O(log n). Linear search O(n) will timeout on large inputs.\nFor 1,000,000 elements: linear = 1M ops, binary = ~20 ops.',
                'description': 'Divide & Conquer: write a function that takes a sorted slice and a target, and RETURNS Option<usize> (the index if found). Must be O(log n).',
                'examples': 'binary_search(&[1,3,5,7,9], 7) -> Some(3)\nbinary_search(&[1,3,5,7,9], 4) -> None',
                'function_signature': 'fn binary_search(data: &[i32], target: i32) -> Option<usize>',
                'starter_code': 'pub fn binary_search(data: &[i32], target: i32) -> Option<usize> {\n    // TODO: O(log n)\n}\n',
            },
            {
                'number': 2, 'title': 'max_sliding_window', 'difficulty': 'hard',
                'description': 'Sliding Window: given a slice and a window size k, RETURN a Vec<i32> of the maximum value in each window as it slides from left to right.',
                'examples': 'max_sliding_window(&[1,3,-1,-3,5,3,6,7], 3)\n  -> [3, 3, 5, 5, 6, 7]',
                'function_signature': 'fn max_sliding_window(nums: &[i32], k: usize) -> Vec<i32>',
                'starter_code': 'pub fn max_sliding_window(nums: &[i32], k: usize) -> Vec<i32> {\n    // TODO\n}\n',
            },
            {
                'number': 3, 'title': 'fibonacci_dp', 'difficulty': 'medium',
                'has_timeout': True, 'timeout_seconds': 5,
                'performance_notes': 'Naive recursion: O(2^n) -- exponential.\nDynamic programming: O(n) -- compute each only once.',
                'description': 'Dynamic Programming: write a function that RETURNS the nth Fibonacci number using DP (not naive recursion). Must handle n up to 50.',
                'examples': 'fibonacci(0)  -> 0\nfibonacci(1)  -> 1\nfibonacci(10) -> 55\nfibonacci(50) -> 12586269025',
                'function_signature': 'fn fibonacci(n: u64) -> u64',
                'starter_code': 'pub fn fibonacci(n: u64) -> u64 {\n    // TODO: use DP, not naive recursion\n}\n',
            },
            {
                'number': 4, 'title': 'max_subarray', 'difficulty': 'medium',
                'description': 'Greedy / Kadane: find the contiguous subarray with the largest sum. RETURN the maximum sum.',
                'examples': 'max_subarray(&[-2,1,-3,4,-1,2,1,-5,4]) -> 6\nmax_subarray(&[1])                      -> 1\nmax_subarray(&[-1,-2,-3])               -> -1',
                'function_signature': 'fn max_subarray(nums: &[i32]) -> i32',
                'starter_code': 'pub fn max_subarray(nums: &[i32]) -> i32 {\n    // TODO: Kadane\'s algorithm\n}\n',
            },
            {
                'number': 5, 'title': 'valid_parentheses', 'difficulty': 'medium',
                'description': 'Stack-based: write a function that RETURNS true if a string of brackets are validly nested. Supports (, ), [, ], {, }.',
                'examples': 'valid_parentheses("()[]{}") -> true\nvalid_parentheses("([)]")  -> false\nvalid_parentheses("{[]}")  -> true',
                'function_signature': 'fn valid_parentheses(s: &str) -> bool',
                'starter_code': 'pub fn valid_parentheses(s: &str) -> bool {\n    // TODO: use a stack\n}\n',
            },
            {
                'number': 6, 'title': 'graph_bfs', 'difficulty': 'hard',
                'description': 'BFS: implement breadth-first search on an adjacency list graph. Given a graph and a start node, RETURN a Vec<usize> of nodes in BFS visit order.',
                'examples': 'bfs(&vec![vec![1,2], vec![0,3], vec![0], vec![1]], 0)\n  -> [0, 1, 2, 3]',
                'function_signature': 'fn bfs(graph: &Vec<Vec<usize>>, start: usize) -> Vec<usize>',
                'starter_code': 'use std::collections::VecDeque;\n\npub fn bfs(graph: &Vec<Vec<usize>>, start: usize) -> Vec<usize> {\n    // TODO\n}\n',
            },
            {
                'number': 7, 'title': 'min_heap', 'difficulty': 'hard',
                'description': 'Heap: implement a MinHeap for i32 values.\n- push(&mut self, val) MODIFIES the heap\n- pop(&mut self) RETURNS and removes the minimum\n- peek(&self) RETURNS reference to the minimum',
                'examples': 'let mut h = MinHeap::new();\nh.push(5); h.push(1); h.push(3);\nh.pop() -> Some(1)\nh.pop() -> Some(3)',
                'function_signature': 'struct MinHeap { data: Vec<i32> }',
                'starter_code': 'pub struct MinHeap {\n    data: Vec<i32>,\n}\n\nimpl MinHeap {\n    pub fn new() -> Self { todo!() }\n    pub fn push(&mut self, val: i32) { todo!() }\n    pub fn pop(&mut self) -> Option<i32> { todo!() }\n    pub fn peek(&self) -> Option<&i32> { todo!() }\n    pub fn len(&self) -> usize { todo!() }\n}\n',
            },
            {
                'number': 8, 'title': 'my_sort', 'difficulty': 'hard',
                'has_timeout': True, 'timeout_seconds': 5,
                'performance_notes': 'Must be O(n log n). Bubble sort O(n^2) will timeout.\nUse merge sort, quicksort, or similar.',
                'description': 'Divide & Conquer: write a sorting function that takes Vec<i32> and RETURNS it sorted in ascending order. Must be O(n log n).',
                'examples': 'my_sort(vec![3,1,4,1,5]) -> [1,1,3,4,5]\nmy_sort(vec![5,4,3,2,1]) -> [1,2,3,4,5]',
                'function_signature': 'fn my_sort(v: Vec<i32>) -> Vec<i32>',
                'starter_code': 'pub fn my_sort(mut v: Vec<i32>) -> Vec<i32> {\n    // TODO: O(n log n)\n    v\n}\n',
            },
        ],
    },
    {
        'number': 7,
        'title': 'Concurrency & Performance',
        'description': 'Threads, Mutex, Arc for shared state. Async/await basics. Performance profiling mindset and zero-cost abstractions.',
        'is_critical': False, 'passing_threshold': 80,
        'language': 'rust',
        'exercises': [
            {
                'number': 0, 'title': 'parallel_sum', 'difficulty': 'medium',
                'description': 'Write a function that takes a Vec<i32> and RETURNS the sum by splitting the work across 2 threads using std::thread. Each thread computes a partial sum, then combine the results.',
                'examples': 'parallel_sum(vec![1, 2, 3, 4]) -> 10\nparallel_sum(vec![])            -> 0',
                'function_signature': 'fn parallel_sum(data: Vec<i32>) -> i32',
                'starter_code': 'use std::thread;\n\npub fn parallel_sum(data: Vec<i32>) -> i32 {\n    // TODO: split data, spawn threads, join results\n}\n',
            },
            {
                'number': 1, 'title': 'shared_counter', 'difficulty': 'medium',
                'description': 'Write a function that spawns n threads, each incrementing a shared counter m times, and RETURNS the final count. Use Arc<Mutex<i32>> for shared state.',
                'examples': 'shared_counter(4, 100) -> 400\nshared_counter(2, 50)  -> 100',
                'function_signature': 'fn shared_counter(threads: usize, increments: usize) -> i32',
                'starter_code': 'use std::sync::{Arc, Mutex};\nuse std::thread;\n\npub fn shared_counter(n_threads: usize, n_increments: usize) -> i32 {\n    // TODO\n}\n',
            },
            {
                'number': 2, 'title': 'parallel_map', 'difficulty': 'hard',
                'description': 'Write a function that takes a Vec<i32> and a function, applies the function to each element using multiple threads, and RETURNS the results in order.\n\nUse thread::spawn and Arc to distribute the work.',
                'examples': 'parallel_map(vec![1,2,3,4], |x| x * x)\n  -> [1, 4, 9, 16]',
                'function_signature': 'fn parallel_map(data: Vec<i32>, f: fn(i32) -> i32) -> Vec<i32>',
                'starter_code': 'use std::thread;\nuse std::sync::Arc;\n\npub fn parallel_map(data: Vec<i32>, f: fn(i32) -> i32) -> Vec<i32> {\n    // TODO\n}\n',
            },
            {
                'number': 3, 'title': 'channel_pipeline', 'difficulty': 'hard',
                'description': 'Create a pipeline using channels (mpsc): a producer thread sends numbers 1 to n, a consumer thread receives them, doubles each, and sends the results. The main function collects and RETURNS all doubled values as Vec<i32>.',
                'examples': 'channel_pipeline(5)  -> [2, 4, 6, 8, 10]\nchannel_pipeline(3)  -> [2, 4, 6]',
                'function_signature': 'fn channel_pipeline(n: i32) -> Vec<i32>',
                'starter_code': 'use std::sync::mpsc;\nuse std::thread;\n\npub fn channel_pipeline(n: i32) -> Vec<i32> {\n    // TODO: producer -> consumer -> collect\n}\n',
            },
        ],
    },
    {
        'number': 8,
        'title': 'Clean Code & Architecture',
        'description': 'Functional style with iterators, writing tests, modularization, and refactoring. Combine everything learned into clean, production-quality Rust code.',
        'is_critical': True, 'passing_threshold': 100,
        'language': 'rust',
        'exercises': [
            {
                'number': 0, 'title': 'matrix_multiply', 'difficulty': 'medium',
                'description': 'Write a function that takes two 2D matrices and RETURNS their product. Use iterator chains for clean, functional-style code.',
                'examples': 'matrix_multiply(\n  &vec![vec![1,2], vec![3,4]],\n  &vec![vec![5,6], vec![7,8]]\n) -> [[19,22], [43,50]]',
                'function_signature': 'fn matrix_multiply(a: &Vec<Vec<i32>>, b: &Vec<Vec<i32>>) -> Vec<Vec<i32>>',
                'starter_code': 'pub fn matrix_multiply(a: &Vec<Vec<i32>>, b: &Vec<Vec<i32>>) -> Vec<Vec<i32>> {\n    // TODO\n}\n',
            },
            {
                'number': 1, 'title': 'eval_rpn', 'difficulty': 'medium',
                'description': 'Evaluate a Reverse Polish Notation expression. Takes a slice of &str tokens and RETURNS the result as i32. Use a stack-based approach with clean pattern matching.',
                'examples': 'eval_rpn(&["2","1","+","3","*"])      -> 9\neval_rpn(&["4","13","5","/","+"])     -> 6',
                'function_signature': 'fn eval_rpn(tokens: &[&str]) -> i32',
                'starter_code': 'pub fn eval_rpn(tokens: &[&str]) -> i32 {\n    // TODO: use a stack\n}\n',
            },
            {
                'number': 2, 'title': 'merge_sorted', 'difficulty': 'medium',
                'has_timeout': True, 'timeout_seconds': 5,
                'performance_notes': 'Must be O(n+m). Use two iterators/pointers advancing through both slices.',
                'description': 'Write a function that takes two sorted slices and RETURNS a single sorted Vec by merging them in O(n+m).',
                'examples': 'merge_sorted(&[1,3,5], &[2,4,6]) -> [1,2,3,4,5,6]\nmerge_sorted(&[1,2,3], &[])       -> [1,2,3]',
                'function_signature': 'fn merge_sorted(a: &[i32], b: &[i32]) -> Vec<i32>',
                'starter_code': 'pub fn merge_sorted(a: &[i32], b: &[i32]) -> Vec<i32> {\n    // TODO: O(n+m) merge\n}\n',
            },
            {
                'number': 3, 'title': 'game_of_life', 'difficulty': 'hard',
                'description': 'Implement one step of Conway\'s Game of Life.\nTakes a grid Vec<Vec<bool>> and RETURNS the next generation.\n\nRules:\n- Live cell with 2-3 neighbors survives\n- Dead cell with exactly 3 neighbors becomes alive\n- All other cells die or stay dead',
                'examples': 'next_generation(vec![\n  vec![false, true, false],\n  vec![false, true, false],\n  vec![false, true, false],\n])\n-> [[false,false,false],\n    [true, true, true],\n    [false,false,false]]',
                'function_signature': 'fn next_generation(grid: Vec<Vec<bool>>) -> Vec<Vec<bool>>',
                'starter_code': 'pub fn next_generation(grid: Vec<Vec<bool>>) -> Vec<Vec<bool>> {\n    // TODO\n}\n',
            },
            {
                'number': 4, 'title': 'longest_common_prefix', 'difficulty': 'easy',
                'description': 'Write a function that takes a slice of &str and RETURNS the longest common prefix as a String. Use clean iterator-based logic.',
                'examples': 'longest_common_prefix(&["flower","flow","flight"])\n  -> "fl"\nlongest_common_prefix(&["dog","racecar","car"])\n  -> ""',
                'function_signature': 'fn longest_common_prefix(strs: &[&str]) -> String',
                'starter_code': 'pub fn longest_common_prefix(strs: &[&str]) -> String {\n    // TODO\n}\n',
            },
        ],
    },
]

class Command(BaseCommand):
    help = 'Seed the database with exercise content'

    def handle(self, *args, **options):
        # Delete old data to allow restructuring
        Exercise.objects.all().delete()
        Day.objects.all().delete()

        created_days = 0
        created_exercises = 0

        for day_data in DAYS_DATA:
            exercises_list = day_data.pop('exercises')
            day, _ = Day.objects.update_or_create(
                number=day_data['number'],
                defaults=day_data,
            )
            created_days += 1

            for ex_data in exercises_list:
                Exercise.objects.update_or_create(
                    day=day,
                    number=ex_data['number'],
                    defaults={
                        'title': ex_data['title'],
                        'difficulty': ex_data.get('difficulty', 'easy'),
                        'description': ex_data['description'],
                        'tutorial': ex_data.get('tutorial', ''),
                        'examples': ex_data.get('examples', ''),
                        'has_timeout': ex_data.get('has_timeout', False),
                        'timeout_seconds': ex_data.get('timeout_seconds', 10),
                        'performance_notes': ex_data.get('performance_notes', ''),
                        'starter_code': ex_data.get('starter_code', ''),
                        'function_signature': ex_data.get('function_signature', ''),
                    },
                )
                created_exercises += 1

            day_data['exercises'] = exercises_list

        self.stdout.write(self.style.SUCCESS(
            f'Seeded {created_days} days and {created_exercises} exercises.'
        ))
