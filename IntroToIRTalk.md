This is the notes towards a talk that [Alex](Alex.md) gave for Spelman College's CIS313 on 24 September 2008. This is pretty much what he said.

[Slides are here.](http://docs.google.com/Presentation?docid=dg2jdd7c_10w427ppgf&hl=en)

[Super-simple demo code here.](http://code.google.com/p/narorumo/source/browse/#svn/trunk/spelman-talk)

My source material here is the excellent  Stuart Russell and Peter Norvig's
_Artificial Intelligence: A Modern Approach_. (http://aima.cs.berkeley.edu/)

Or wikipedia articles, which I'll list here too.

## What's Information Retrieval? ##

How do we define the task? A user wants some information, and we're going to handle this by showing them a document. We have a lot of documents on hand. Maybe a backup copy of the web.

```
for site in `cat every-website`; do
  wget -r $site;
done
```

We get a query from the user describing what they want to find, and we'll present them with a list of documents, hopefully the most-relevant and interesting first. And we want to have both high **precision** and high **recall**.

Precision is the "I'm feeling lucky" button. Precision is the proportion of the documents that are actually relevant.
Recall is the proportion of all the relevant documents that actually show up. If there are really forty good documents about waffles, but your search engine only shows you twnety of them, that's 50% recall.

For today, we're assuming that the user will type in a query string in order to start the search, which is kind of interesting. It works pretty well for text documents, you just put in a few words to describe what you're looking for. There are a few search engines where you formulate your query as a question; you can do this with Google if you like, but, for example, ask.com specifically encourages you to do this. It's really not clear that phrasing it in the form of a question helps.

If you were searching for the song you had stuck in your head, you might tap out a rhythm or sing a few bars...

How do you store/represent your copy of the corpus? What information do you
want to extract about your documents?

## first pass ##
Logical connectives and your query language

Russell and Norvig say:
> After reading the previous chapter, one might suppose that an information
> retrieval system could be built by parsing the document collection into a
> knowledge base of logical sentences and then parsing each query and `ASK`ing
> the knowledge base for answers. Unfortunately, no one has ever succeeded in
> building a large-scale IR system that way. It is just too difficult to build
> a lexicon and grammar that cover a large document collection, so all IR
> systems use simpler language models.

Alright, let's go for a simpler language model.

### Boolean keyword model ###
Which words are in the document? Consider every word that appears in your corpus as a boolean feature that either appears or doesn't in a given document. This lets users form queries with logical connectives. I want a document about waffles OR (pancakes AND juice).

This could be really fast. Build a giant decision tree or just do a big SELECT on your database.

### probabilistic language modeling ###
Instead of trying to parse out and understand all the documents in the corpus, we can build a probabilistic model out of the words that we find. We'd want to know how common a given word is, and then how common it is in a particular document, and this would let us evaluate something like P (query | document)...

http://en.wikipedia.org/wiki/Naive_Bayes_classifier

You could also model the bigrams or n-grams (for a very small corpus), and that might help out..

### Vector space model ###
http://en.wikipedia.org/wiki/Vector_space_model

You just count how many times each word appears in a document. If a document contains the word "waffle", then it's probably about waffles. Sounds good!

**example!**

What are some problems with this?
- Some words show up an awful lot.
- This comes in two flavors: some words aren't helpful for this task at all. Language processing people refer to these as "stopwords", and typically you'll want to take them out immediately. More subtly, some words show up very rarely, but if they do show up, you almost certainly want to take note.

One thing we could do, we could just filter out all the "stopwords".
http://en.wikipedia.org/wiki/Stop_words

Okay, but maybe we can do better than that. Look at all of this stuff about Spain and France, in the Andorra article.

### tf-idf ###
A fairly standard way to handle this is with what's called TF-IDF, Term-Frequency, Inverse Document Frequency.

http://en.wikipedia.org/wiki/Tf-idf

Term frequency is just the proportion of the words in the document that are this term.

Inverse document frequency is more involved -- it's higher for words that occur in the whole corpus less often. It's the log of the inverse of the probability that the term appears in a given document.

"The inverse document frequency is a measure of the general importance of the term (obtained by dividing the number of all documents by the number of documents containing the term, and then taking the logarithm of that quotient)."

## Ranking ##
So once we've found the documents that might be relevant to your search, we've got to present them in some sensible order. We really, really want for the top hit to be the document you'd be happiest to find.

At this point, we're somewhere in the neighborhood of the old hotbot. It could give you pages that had the words you were looking for, no guarantee that they were any good. Now we need... ranking!

### PageRank ###
PageRank is called that not just because it ranks pages -- it's named after Larry Page.

From the "Google Technology" page:

> PageRank relies on the uniquely democratic nature of the web by using its vast link
> structure as an indicator of an individual page's value. In essence, Google interprets
> a link from page A to page B as a vote, by page A, for page B. But, Google looks at
> more than the sheer volume of votes, or links a page receives; it also analyzes the
> page that casts the vote. Votes cast by pages that are themselves "important" weigh
> more heavily and help to make other pages "important".

"PageRank also considers the importance of each page that casts a vote, as votes from some pages are considered to have greater value, thus giving the linked page greater value. We have always taken a pragmatic approach to help improve search quality and create useful products, and our technology uses the collective intelligence of the web to determine a page's importance."


## hard problems ##
  * Polysemy: some words mean more than one thing. "apple" like computers, "apple" like fruit.
  * synonyms: there's more than one word for a given topic! How do we make this fall out of the numbers? LSI?
  * There are a bunch of languages in the world. Russell and Norvig give the amazing example of the German word "Lebensverischerungsgesellschaftsangestellter" which means "life insurance company employee". Well, if you see that word, you're probably looking at a document about life insurance companies.
  * The reverse problem happens in English, because we don't always make our compound words one compound word! "life insurance" is different from "life" and "insurance".

## How do you make it fast? ##
... ?

## Questions? ##