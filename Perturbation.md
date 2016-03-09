[Lindsey Kuper](Lindsey.md)

Today I issued a [challenge](http://lindseykuper.livejournal.com/265703.html) to my friends:

> A _perturbation_ of a string is a permutation, but with one `m` removed and one `r` and one `b` added. For example, `perturbation` is a perturbation of `permutation`.

> _**Challenge!**_: I'll bake cookies for the first person who can generate a list of all the words in [your words file](http://en.wikipedia.org/wiki/Words_(Unix)) that have at least one valid perturbation. (In this case, a "valid perturbation" is one that also appears in `words`. Perturbation is undefined for strings that don't have an `m` to begin with.)

My friends [rose to the challenge](http://lindseykuper.livejournal.com/265703.html#comments), of course ([Jesse Wolfe](http://www.jes5199.com) was first with his Ruby implementation; [Peter Boothe](http://soy.dyndns.org/~peter/) did it in Python).  Here's [my version in Perl](http://code.google.com/p/narorumo/source/browse/trunk/perturbation/perturbation.pl).

From [Alex](Alex.md), we've got [another Python version](http://code.google.com/p/narorumo/source/browse/trunk/perturbation/perturbation.py) and a [Scheme version](http://code.google.com/p/narorumo/source/browse/trunk/perturbation/perturbation.scm), both with a little performance optimization ("dumb hack" -- [Alex](Alex.md)) that clever folks should be able to spot.