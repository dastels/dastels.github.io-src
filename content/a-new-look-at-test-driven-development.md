Title: A New Look at Test Driven Development
Date: 2014-09-29 19:04
Author: dastels
Category: general
Tags: general
Slug: a-new-look-at-test-driven-development
Status: published

Thanks to the [wayback machine](http://archive.org/web/), I found my
original post that resulted in rSpec posted on July 5, 2005.

### The state of Test Driven Development

Test Driven Development (TDD) has made it to prime time. Big companies
are paying big money to have their programmers trained in how to *do*
TDD. It's a popular topic at conferences... *agile* and otherwise. My
book on TDD won a Jolt award. So everything's rosy, huh? Everyone who's
doing TDD is fully understanding it and getting the full benefit, right?

**Fat Chance!**

Maybe 10% of the people I talk to really understand what it's really
about. Maybe only 5%. That sucks. What's wrong? Well... one thing is
that people think it's about testing. That's just not the case.

Sure, there are similarities, and you end up with a nice low level
regression suite... but those are coincidental or happy side effects. So
why have things come to this unhappy state of affairs? Why do so many
not get it? Well, first a bit of a history lesson. If you look at an old
issue of my old Coad Letter</a> issues (if you can find them), there's
some background on TDD:

*"XP originally had the rule to test everything that could possibly
break. Now, however, the practice of testing in XP has evolved into
Test-Driven Development."*

So way back when, they were talking about writing tests. And that's
probably why it has the testing centric vocabulary, and that is why
people think it's about testing! What else would they think when they
have to talk about TestCases & TestSuites, & Tests.. and have to name
methods starting with "test". Granted, this is jUnit specific and nUnit
doesn't have these requirements.

The thing is that when the evolution to TDD happened what we ended up
with was a different kind of animal... not just a slight tweak on the
original. The original XP folks were writing tests for everything that
could break, then they started writing the tests first. Eventually we
ended up at TDD. But TDD is not the endpoint everyone seems to think it
is... it's just a stepping-stone.

Also, the idea of "unit" is a major problem. First of all it's a vague
term, and second it implies a structural division of the code (i.e.
people think that they have to test methods or classes). We shouldn't be
thinking about *units*... we should be thinking about facets of
behaviour.

Thinking about unit testing leads us to divide tests in a way that
reflects the structural arrangement of the code. For example, having a
text classes and production classes in a 1-1 relationship

That's not what we want... we want behavioural divisions.. we want to
work at a level of granularity much smaller than that of the typical
unit test. As I've said before when talking about TDD, we should be
working with very small, focused pieces of behaviour... one small aspect
of a single method. Things like *"after the add() method is called with
an object when the list is empty, there should be one thing in the
list"*. The method is being called in a very specific context, often
with very specific argument, and with a very specific outcome.

So, there you have it. A fabulous idea... wrapped in packaging that
causes people to think from a testing point of view.

Why is this a problem? Let's think for a minute about how people often
think about *testing*.

Programmers often think *"I'm not going to write all those tests."*,
*"It's really simple code, it doesn't need to be tested"*, *"testing is
a waste of time"*, or *"I've done this (loop/data
retrieval/functionalty, etc) millions of times."*.

Project managers often think *"we test after the code is done"*,
*"that's what we have a testing person for"*, or *"we can't spend that
time now"*.

So with people thinking about testing, it's easy to come up with all
sorts of negative reactions and reasons not to do it... especially when
time gets short and the pressure's on.

### So if it's not about testing, what's it about?

It's about figuring out what you are trying to do before you run off
half-cocked to try to do it. You write a specification that nails down a
small aspect of behaviour in a concise, unambiguous, and executable
form. It's that simple. Does that mean you write tests? No. It means you
write **specifications** of what your code will have to do. It means you
specify the behaviour of your code ahead of time. But not far ahead of
time. In fact, just before you write the code is best because that's
when you have as much information at hand as you will up to that point.
Like well done TDD, you work in tiny increments... specifying one small
aspect of behaviour at a time, then implementing it.

When you realize that it's all about specifying behaviour and not
writing tests, your point of view shifts. Suddenly the idea of having a
*Test* class for each of your production classes is rediculously
limiting. And the thought of testing each of your methods with its own
test method (in a 1-1 relationship) will have you rolling on the floor
laughing.

### So what to do?

First stop thinking in terms of tests. Using something like JUnit makes
this hard, so we need to start with a new framework for specifying
behaviour. Dan North of ThoughtWorks has started the
[jBehave](//jbehave.codehaus.org/) project to do just this.

Using a behaviour-centric framework that uses behaviour-centric
vocabulary and concepts will let you think in terms of specifying the
behaviour you want from you code.

### A Behaviour Specification Framework

So what does a behaviour specification look like? Well, a first pass
will look and work a lot like jUnit since:

1 it works quite well enough
2 everyone is familiar with it

A major difference is vocabulary. Instead of subclassing `TestCase`, you
subclass **`Context`**. Instead of writing methods that start with
**`test`** you start them **`should`**, or preferrably you won;t have to
worry about a naming pattern so you can choose the most appropriate
name. Instead of doing verification with assertions (e.g.
**`assertEquals(expected, actual)`**) you specify post conditions with
something like **`shouldBeEqual(actual, expected)`**.

In Smalltalk, and likely Ruby, this can be even more natural if we embed
the framework into the class library (a common approach in Smalltalk
btw). You could write something like: **`actual shouldEqual: expected`**
or **`result shouldBeNull`** or
**`[2 / 0] shouldThrow: DivideByZeroException`**.

### What Now?

As mentioned above, Dan North has started the jBehave project to create
a jUnit replacement for behaviour specification that you can download
and experiment with now. I'll be involved in some way with that project,
and I'm planning to explore some ideas in the Smalltalk and Ruby space.
We'll see what happens and where it goes. I've also been working on a
behaviour oriented version of jUnit.

### Summary

Does this mean that everything you know about TDD is now useless?
Hardly! All the techniques are just as applicable to BDD. Your
approaches to specifying behaviours are going to be much the same.
You'll still want to mock things. And so on. What's changed is the
vocabulary and the point of view.

The point of view is really the important thing. How does changing that
change the value of the process? Well, for one thing, if you have a lot
of **should**s, the *should method* names make a very clear
specification. Like:

-   shouldAllowValidUser
-   shouldCheckIsValidBeforeUpdate
-   shouldUpdateRecordSet
-   shouldWriteToUpdateLog

To sum up:

1 The problem I have with TDD is that its mindset takes us in a
different direction... a wrong direction.
2 We need to start thinking in terms of behavior specifications, not
verification tests.
3 The value of doing this will be thinking more clearly about each
behaviour, relying less on testing by class or by method, and having
better executable documentation.
4 Since TDD is what it is, and everyone isn't about to change their
meaning of that name (nor should we expect them to), we need a new name
for this new way of working... BDD: Behaviour Driven Development.
