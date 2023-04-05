// Team Ruff :: Ivan Yeung, Andrew Piatetsky
// SoftDev pd8
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

//testing function
function test(n) {
    return n;
}

// console.log(test(1));
// console.log(test(3));
// console.log(test("Hello World"));

//fact
function fact(n) {
    if (n < 2) {
        return 1;
    } else {
        return n * fact(n - 1);
    }
}
// console.log(fact(1)); //should be 1
// console.log(fact(2)); //should be 2
// console.log(fact(3)); //should be 6
// console.log(fact(4)); //should be 24
// console.log(fact(5)); //should be 120

//fib
function fib(n) {
    if (n < 2) {
        return n;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}

// console.log(fib(0)); //should be 0
// console.log(fib(1)); //should be 1
// console.log(fib(2)); //should be 1
// console.log(fib(3)); //should be 2
// console.log(fib(4)); //should be 3

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
