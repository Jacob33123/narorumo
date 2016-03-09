# SICP Chapter 1 #

## Considerations ##

### 1.5 ###

Applicative-order evaluation is clearly the same as "eager evaluation", and normal-order seems to be the same as lazy evaluation -- but is this the same thing as passing a thunk? What's the relationship there? -- [Alex](Alex.md)

### 1.16 ###

I see what was going wrong in [this commit](http://code.google.com/p/narorumo/source/diff?r=57&format=side&path=/trunk/sicp/chapter1.scm).  My procedure was computing iteratively AND recursively and MULTIPLYING the products, so that 2<sup>1</sup> = 4, 2<sup>2</sup> = 16, 2<sup>3</sup> = 64, 2<sup>4</sup> = 256, et cetera.  Badness!  I wish I were better at thinking iteratively.

Here's what an example expansion looked like in the buggy version:

```
(fast-expt-iter 2 4)
(fast-expt-iter-kernel 2 4 1)
(* 2 (fast-expt-iter-kernel 2 3 2))
(* 2 (* 2 (fast-expt-iter-kernel 2 2 4)))
(* 2 (* 2 (* 2 (fast-expt-iter-kernel 2 1 8))))
(* 2 (* 2 (* 2 (* 2 (fast-expt-iter-kernel 2 0 16)))))
(* 2 (* 2 (* 2 (* 2 16))))
(* 2 (* 2 (* 2 32)))
(* 2 (* 2 64))
(* 2 128)
256
```


So, the the value of /a/ is correct at the end (a = 16), but then we're doing all the backed-up multiplications for the recursion, too!  Oh, noes!

On the plus side, now I'll know exactly to do if my students make this mistake:
"Lindsey!  My code is acting sort of wrong.  Everything's coming out the SQUARE of what it's supposed to be."
"Interesting!  What do you think might cause it to do that?"
"I got the state transformation for the iteration wrong."
"No, you got that part right."
"But--"
"You got the iteration right."
"Okay, then I got the recursion wrong."
"You got the recursion right."
"But if I--if both--what--oh."

-- [Lindsey](Lindsey.md)

### 1.37 and 1.38 ###

While writing `cont-frac-iter` for 1.37b, I realized that there was a mistake in 1.37a.  Instead of calling `(kernel 1)` in `cont-frac`, I should have been calling `(kernel 0)`.  With `(kernel 1)`, things like

```
(cont-frac (lambda (i) 3.0) (lambda (i) 5.0) 1)
```

were evaluating to 0, and it seems to me that if _k_ is 1, the answer should be 3/5.  `(cont-frac (lambda (i) 3.0) (lambda (i) 5.0) 2)` was evaluating to 3/5, so I figured it was an off-by-one error.

I changed `cont-frac` and committed my change along with 1.37b.  But then my answer for 1.38, which had been using `cont-frac`, began to come up wrong!:

```
> (approximate-e 100)
2.5819767068693262
```

And yet, if I wrote an `approximate-e-iter` that was identical to `approximate-e` except that it used my new `cont-frac-iter` instead of `cont-frac`, I got the right answer:

```
> (approximate-e-iter 100)
2.7182818284590455
```

I ended up just using `cont-frac-iter` instead of `cont-frac` in the answer to 1.38, but I don't know why they're different.  I know that `cont-frac-iter` works up from the bottom of the continued fraction while `cont-frac` works down from the top, but they should arrive at the same answer.  I suspect that one or both of them is still buggy, or my `approximate-e` is buggy.  I'm going to call this done, but it might be worth investigating!

-- [Lindsey](Lindsey.md)


### 1.38 ###

I wonder if I could have used `log` or something in working out `subtrahend` instead of writing it recursively. -- [Lindsey](Lindsey.md)

## Progress ##

| number | status |
|:-------|:-------|
| 1      | done   |
| 2      | done   |
| 3      | done   |
| 4      | done   |
| 5      | done   |
| 6      | done   |
| 7      | done   |
| 8      | done   |
| 9      | done   |
| 10     | done   |
| 11     | done   |
| 12     | done   |
| 13     | done   |
| 14     | done   |
| 15     | done   |
| 16     | done   |
| 17     | done   |
| 18     | done   |
| 19     | done   |
| 20     | done   |
| 21     | done   |
| 22     | done   |
| 23     | done   |
| 24     | done   |
| 25     | done   |
| 26     | done   |
| 27     | done   |
| 28     | done   |
| 29     | done   |
| 30     | done   |
| 31     | done   |
| 32     | done   |
| 33     | done   |
| 34     | done   |
| 35     | done   |
| 36     | done   |
| 37     | done   |
| 38     | done   |
| 39     | done   |
| 40     | done   |
| 41     | done   |
| 42     | done   |
| 43     | done   |
| 44     | done   |
| 45     | done   |
| 46     | done   |