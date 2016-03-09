# Really big Fibonacci numbers #

[Lindsey Kuper](Lindsey.md)

## An O(log n) algorithm for computing Fibonacci numbers? ##

[Exercise 1.19](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-11.html#%_thm_1.19) of
_Structure and Interpretation of Computer Programs_ gives most of a procedure for computing [Fibonacci numbers](http://en.wikipedia.org/wiki/Fibonacci_number) that runs in a logarithmic number of steps:

```
(define (fib n)
  (fib-iter 1 0 0 1 n))

(define (fib-iter a b p q count)
  (cond ((= count 0) b)
        ((even? count)
         (fib-iter a
                   b
                   <??>      ; compute p'
                   <??>      ; compute q'
                   (/ count 2)))
        (else (fib-iter (+ (* b q) (* a q) (* a p))
                        (+ (* b p) (* a q))
                        p
                        q
                        (- count 1)))))
```

The exercise is to complete the procedure by replacing the `<??>`s in the code with the appropriate expressions.  After I [did that](http://code.google.com/p/narorumo/source/diff?r=81&format=unidiff&path=/trunk/sicp/chapter1.scm), it seemed to be working pretty snappily on the smaller numbers I tested it with, so I tried `(fib 1000000)`.  The resulting number, which took about 0.945 seconds to calculate<sup>1</sup>  on my 2.4 GHz MacBook Pro, turns out to have 208,988 digits.

To make sure I had it right, I googled ["millionth fibonacci number"](http://www.google.com/search?q=%22millionth+fibonacci+number%22).<sup>2</sup>  [This person's result](http://www.upl.cs.wisc.edu/~bethenco/fibo/)<sup>3</sup> turned out to be the same as mine, according to `diff`.

Next, I tried `(fib 10000000)`, which took about 26 seconds to calculate.<sup>6</sup>  The resulting number has 2,089,877 digits.  A search for ["ten millionth fibonacci number"](http://www.google.com/search?q=%22ten+millionth+fibonacci+number%22)<sup>4</sup> turned up [this person's work](http://www.bigzaphod.org/fibonacci/),<sup>5</sup> which also seemed to match my result.

How about `(fib 100000000)`, the hundred millionth Fibonacci number?  It took 14 minutes and 22.568 seconds to calculate and has 20,898,764 digits.  The first 76 digits are:

```
473710347345633696254897131335103865754868289377201030193412163431081491642
```

I would like to have independent confirmation (or disproof!) of this number, but so far, I haven't found anyone else who has calculated it.

## Try this at home ##

Should you want to try it at home, I took the code, some test cases, and an explanation of how I found _p'_ and _q'_ and pulled them out into a separate file.  It's about 20 lines of R<sup>5</sup>RS Scheme, plus a lot of comments:
  * [1.19.scm](http://code.google.com/p/narorumo/source/browse/trunk/sicp/1.19.scm)

You can also download the output of the program as a text file:
  * [millionth-fibonacci-number.txt](http://code.google.com/p/narorumo/downloads/detail?name=millionth-fibonacci-number.txt)
  * [ten-millionth-fibonacci-number.txt](http://code.google.com/p/narorumo/downloads/detail?name=ten-millionth-fibonacci-number.txt)
  * [hundred-millionth-fibonacci-number.txt](http://code.google.com/p/narorumo/downloads/detail?name=hundred-millionth-fibonacci-number.txt)

## Acknowledgments ##

It took me about three hours to do the math for this exercise.  [Alex](http://code.google.com/u/alex.rudnick/) patiently let me [rubber-duck](http://c2.com/cgi/wiki?RubberDucking) through the first part of the problem, then suggested that I start using _p'_ and _q'_ so that I'd be able to tell "old" and "new" _p_ and _q_ apart, which saved me from Lexical Scoping Insanity.  He was also the one who pointed out that I had a system of equations that I could use to solve for _p'_ and _q'_.  Once I was done with the math, it took only a couple of minutes to write the code.

[![](http://imgs.xkcd.com/comics/alone.png)](http://xkcd.com/289/)

## Notes ##

<sup>1</sup> I got the 0.945 seconds figure by running [1.19.scm](http://code.google.com/p/narorumo/source/browse/trunk/sicp/1.19.scm) with all the test cases but `(display (fib 1000000))` commented out, using the command `time mzscheme -r 1.19.scm > millionth-fibonacci-number.txt`.  I tried it a few times, and 0.945 seconds seemed close to average.

<sup>2</sup> At the time of this writing on May 12, 2008, this query returned 26 results.

<sup>3</sup> It was also [mentioned on Digg](http://digg.com/odd_stuff/The_millionth_fibonacci_number/) with the comment "This must have taken a while to calculate."

<sup>4</sup> This one returned 13 results.  I thought they might keep decreasing by half, but neither ["hundred millionth fibonacci number"](http://www.google.com/search?q=%22hundred+millionth+fibonacci+number%22) nor ["100,000,000th fibonacci number"](http://www.google.com/search?q=%22100%2C000%2C000th+fibonacci+number%22) returned anything.  (How long until _this_ page gets indexed?)

<sup>5</sup> The author wrote, "This sucker took around 31 hours of computation on a 1.67Ghz G4 PowerBook."  This one [made Digg](http://digg.com/programming/Ten_Millionth_Fibonacci_Number) as well; apparently, `(fib 1000000)` counts as "odd stuff" while `(fib 10000000)` counts as "programming".

<sup>6</sup> 26.720 seconds on my machine, running [1.19.scm](http://code.google.com/p/narorumo/source/browse/trunk/sicp/1.19.scm) with all the test cases but `(display (fib 10000000))` commented out, using the command `time mzscheme -r 1.19.scm > ten-millionth-fibonacci-number.txt`.  Can it be even faster?  According to [this book](http://books.google.com/books?id=yJIghWULQV8C&pg=PA155&lpg=PA155&dq=%2210,000,000th+fibonacci+number%22&ots=GIMiKnKkc7&sig=XyUXMfRTiPU2nsNXkAFwsmPVCTY), you can do it in "about 19 seconds" using Mathematica, although I haven't tried.