Title: Languages
Date: 2017-06-21 19:56
Author: dastels
Slug: languages
Status: published

Forward
-------

I often get asked by people, both those starting out as well as those
well into their career, "What languages should I know?", or "What language should I learn next?". I'll try to give an answer, or at least some guidance.

The purpose of this is not to start a language holy war or the like. These are my opinions based on writing software of all sorts in a wide variety of languages for over 30 years.

There are many, many programming languages. Some of them are or have been in common use. The dynamics of he programming language ecosystem is interesting. Why do some become defacto standards? And why do other fade into relative obscurity, even though they may be vastly superior.

Very few programming languages are created in a vacuum, devoid of influences from others. Several attempts have been made to chart these influences. Here are a couple:

<img width="100%" src="/images/programming_families.jpg" />
<br/>
<img width="100%" src="/images/programminghistory.jpg" />

Before we jump into looking at some languages I think every programmer should be somewhat fluent in, I'll relate a couple of quotes pertaining to Smalltalk, one of my favorite lanaguages, that are relevant to the above questions:

> "Smalltalk is an improvement over most of it's successors."
>
> At an OOPLSA 2003 keynote [Dave Ungar](http://en.wikipedia.org/wiki/David_Ungar) (a co-inventor of Self) was asked "So if languages like Smalltalk and Self are much better, why are most programmers using languages like C++ and Java?" To which Mr. Ungar answered "Why do people smoke?"

And now, the languages:

The Mother Languages
--------------------

In French cooking there are the Mother Sauces: a small group from which all others derive (béchamel, espagnole, velouté, hollandaise and sauce tomate as stated by Escoffier). The five sauces form the basis of a French chef's repertoire. Likewise, I maintain that there are a similarly fundamental set of languages that you really need to know in order to call yourself a well rounded programmer. While they are old languages, they are still arguable best of breed. Despite losing some popularity they retain loyal followings and have been kept up to date and are still relevant.

These languages were probably the most influential on my career and the way I think about programming and software. They weren't the first: BASIC, Z80 & 6502 Assembly, and Pascal came first (and in that order), followed by C, Lisp, and Smalltalk.

If I could go back and restructure my early days based on what I know now (which is what I'm trying to do here for new programmers) in what order would I learn them? Barring practical concerns (like having a job in a rails shop), probably this:

1.  Lisp using SICP. If you could make it through all of SICP and understand most of what you've learned, I would probably hire you on the spot, as you would know and understand more about programming and computation than most programmers I've met with many years of experience.
2.  Smalltalk. Mastering Smalltalk indicates to me a deep understanding of object oriented programming.
3.  C. Understanding C well enough to write some non-trivial, low level code (like a virtual machine or device driver) means to me that you've achieved a fundamental understanding of how computers work.

Once you've mastered these, no programming language in common use today
will present much of
a challenge to you.

### Lisp

Yes, Lisp. There are various dialects to choose from: Common Lisp,
Scheme, and
Clojure are some of the more popular choices. For someone setting out to
learn
Lisp, I encourage the use of MIT Scheme. It's free and available for
most
platforms (distributed by the Free Software Foundation). Part of the
reason I
endorse MIT Scheme is that then you can use the book *Structure and
Interpretation of Computer Programs* as your guide. This approach will
teach you
computing fundamentals in a largely syntax-free environment. In the
process,
you'll pick up a significant amount of Lisp knowledge and skill. SICP
was the
textbook for the intro to computing course for all Computer Science and
Electrical Engineering majors for many years at MIT. You can get a PDF
of the
SICP book at the site below, as well as videos of every lecture.

Lisp is one of the quinessential functional languages. It's is very easy
to
write purely functional code in it. Even though SICP covers data
mutation, it
warns heavily against doing so without a damn good reason. If you move
on to
learn Clojure, writing functional code is a core part of that
language's
philosophy.

-   [MIT Scheme](http://www.gnu.org/software/mit-scheme/)
-   [SICP](http://sicpebook.wordpress.com)
-   [Paul Graham's *The Roots of
    Lisp*](http://www.paulgraham.com/rootsoflisp.html)

### Smalltalk

No, it's not dead. It's very much alive, and still one of the best
development
environments and OO languages you'll find. These days there are two
primary
implementations:

1.  VisualWorks Smalltalk, available from Cincom, is the original which
    can trace
   it's direct lineage back to the Software Concepts Group at Xerox
    Palo Alto
   Research Center in the seventies. It's grown up and evolved a lot
    since it was
   known as Smalltalk-80, and is actively developed by a talented group
    of people.
   VisualWorks is free for non commercial use but costs if you want to
    sell your
   work.
2.  Squeak (and it's offshoot, Pharo) is a reimagining of Smalltalk-80,
    started
   and initially led by the same man who is responsible for the
    Smalltalk work back
   at PARC: Alan Kay (not coincidentally, the guy who coined the term
    "Object
   Oriented"). Squeak/Pharo is open source.

For learning Smalltalk, I suggest using Pharo: It's clean and modern,
and
completely free to use. It also has the advantage of being hugely cross
platform.

There are many freely available Smalltalkbooks in PDF.

-   [Squeak](http://www.squeak.org)
-   [Pharo](http://pharo.org)
-   [Cincom Smalltalk](http://www.cincomsmalltalk.com/main/)
-   [Free Smalltalk
    Books](http://stephane.ducasse.free.fr/FreeBooks.html)

### C

This is, in many ways, **the** underlying language. C is a fundamental
language
upon which all else is built (literally or metaphorically). Go deep
enough in
almost any other language and you will find a kernel written in C (or
one of
it's offshoots).

Speaking of offshoots, I use "C" to mean "C and it's child languages":
specifically C++ and Objective-C. These are both thin OO veneers over a
syntactic
core of C. But even if you know and work in one of these, it's still a
good idea
to be able to code in raw C.

Objective-C is by far a cleaner and more elegant grafting of OO concepts
onto a
core of C, than is C++. Alas, the only place you'll find much
Objective-C in use is on iOS and
OSX. C++ (and I might get in trouble for saying this) is like
Objective-C's
ghetto counterpart. It's messy, ambiguous, and full of unexpected
surprises and
snares for the uninitiated. That said, it's closer to raw C than
Objective-C is,
which can be good or bad, depending on the situation.

C is available on pretty much every computer and OS ever made. You can
probably
find a binary distribution of `gcc` (The GNU C compiler) for whatever
you are
using.

It's hard to emphasize how important a thorough grounding in basic C is.
C is
the quintessential imperative programming language, and probably the
most
heavily used example of the Algol-style syntax.

-   [GCC](http://gcc.gnu.org)
-   [Learn C the Hard Way](http://c.learncodethehardway.org/book/)

The Staples
-----------

### Java

Java being released to the software development ecosystem had a similar
effect
as the introduction of rabbits to Austrialia: it proliferated and pretty
much
took over, driving out other languages that were far superior.

Java grew out of the Oak project, which had the purpose of providing a
portable,
embedded programming language and environment. Java was/is a great
solution for
that. The trouble came when it started being used for the then new world
wide
web browsers, and eventually as almost the defacto standard language for
web
server app development. For a while Java was probably the most popular
OO
language in general use. C++ continued in performance critical
applications
(operating systems, games, etc) and low level apps. Java pushed aside
ObjectiveC
and Smalltalk, even though both were far superior languages.

Oddly, the most interesting Java applications/frameworks never achieved
much
momentum: Jini and it's associated technologies.

Should you learn Java? Of course. Should you choose to use it? Probably
not.
There are better languages, both for learning from and for writing
production code.

The most important legacy that Java will leave is the [Java Virtual
Machine (JVM)](http://en.wikipedia.org/wiki/Java_virtual_machine) which
has become a popular platform for implementing other languages such
as JRuby, Scala, and Clojure.

[Java](https://java.com/en/)

### Ruby

According to Matz (the designer of Ruby) "Ruby is designed for
programmer
productivity and fun". And it is a very fun language to work with. If
you don't
know it, you definitely should. Ruby is heavily influenced by Smalltalk
and
Lisp, with a largely C-ish syntax, anyone who knows those languages
should have
no trouble picking up Ruby.

Ruby, due largely to the Rails framework, as become a standard for web
development. With the advent of RubyMotion, it can also be used to build
native
iOS, OSX, and Android applications.

That's another thing. You can't be a "Rails Programmer" any more than
you can be
an "EJB Programmer"; Rails is merely a framework/library written in
Ruby. If
you're using Rails, you're programming in Ruby, albiet possibly without
knowing
much about what you're doing. If you are working with Rails, do everyone
a favor
(especially yourself and people who will work on your code later) and
learn the
language you are using. David Black wrote a book just for you a while
back. It's
a bit dated now, but the basics of Ruby haven't changed much. There's
also
Programming Ruby which is the canonical book on Ruby.

-   [Ruby Central](http://rubycentral.org)
-   [RubyMotion](http://www.rubymotion.com)
-   [Ruby for Rails: Ruby Techniques for Rails
    Developers](http://www.amazon.com/Ruby-Rails-Techniques-Developers/dp/1932394699)
-   [Programming
    Ruby](http://pragprog.com/book/ruby4/programming-ruby-1-9-2-0)

### Python

It's taken me a while to embrace Python. I always thought that if you
can use Ruby, there's no real reason to use Python. That's still
generally true (as is the reverse) as they fill more or less the same
niche. That changed for me with the advent of MicroPython and
CircuitPython for low level microcontroller programming. CircuitPython
makes it especially easy by exposing the flash filesystem as a USB drive
where you store Python files. You can even directly edit the code on the
device.

-   [The Python Software Foundation](https://www.python.org)
-   [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython)

### C++

If you never learn C++ you won't be missing much, other than how to
avoid the
booby traps.

Unfortunately, C++ is still a very heavily used language and if you
program for long enough you will undoubtedly run in to a situation
where you need to use it. For that reason alone it's worth learning.

At Steelseries we decided against using C++. The team at Sun
Mircosystems made the same decision in the early 90s, for many of the
same reasons:

> "The team originally considered using C++, but it was rejected for
> several
> reasons. Because they were developing an embedded system with limited
> resources, they decided that C++ needed too much memory and that its
> complexity led to developer errors. The language's lack of garbage
> collection
> meant that programmers had to manually manage system memory, a
> challenging and
> error-prone task. The team was also troubled by the language's lack
> of
> portable facilities for security, distributed programming, and
> threading.
> Finally, they wanted a platform that could be easily ported to all
> types of
> devices."

And so, work on what would come to be the Java language began.

-   [C++](http://www.cplusplus.com)
-   [g++](https://gcc.gnu.org)

### Javascript

If you work on web apps, or want to hack on making sites a bit more
interactive,
you pretty much have to know Javascript. It's an interesting language,
but has more than it's share of ugly bits and dark corners.

With the advent of Node.js, Javascript is usable for more and more
applications including server side and embedded. I'm not a fan, and this
seems to me to be the case of new programmers learning Javascript and
not wanting to expand their repertoire.

-   [JavaScript: The Good
    Parts](http://www.amazon.com/JavaScript-Good-Parts-Douglas-Crockford/dp/0596517742)

The Mind Stretchers
-------------------

### Erlang

["Hello, Joe..."](https://www.youtube.com/watch?v=uKfKtXYLG78)

Erlang was developed at Erricson in the early 1980s to program
telephony applications. It was built on top of Lisp, Prolog and Parlog

> "Erlang is a programming language used to build massively scalable
> soft real-time systems with requirements on high availability. Some
> of its uses are in telecoms, banking, e-commerce, computer telephony
> and instant messaging. Erlang's runtime system has built-in support
> for concurrency, distribution and fault tolerance."

-   [Erlang.org](http://www.erlang.org)
-   [The Erlang Movie](https://www.youtube.com/watch?v=uKfKtXYLG78)

### Haskell

If I were to pick a fourth Mother Language, it would be Haskell. Haskell
is
representative of a pure functional language.

> Haskell is an advanced purely-functional programming language. An
> open-source product of more than twenty years of cutting-edge
> research, it allows rapid development of robust, concise, correct
> software. With strong support for integration with other languages,
> built-in concurrency and parallelism, debuggers, profilers, rich
> libraries and an active community, Haskell makes it easier to
> produce flexible, maintainable, high-quality software.

As I am writing this, I am actively and enthusiasticly learning it. If
you use OSX, Haskell for Mac is a great way to learn and explore the
language.

-   [Haskell.org](http://www.haskell.org/haskellwiki/Haskell)
-   [Haskel for Mac](http://haskellformac.com)

### Self

> Self is a prototype-based dynamic object-oriented programming
> language,
> environment, and virtual machine centered around the principles of
> simplicity,
> uniformity, concreteness, and liveness. Self includes a programming
> language,
> a collection of objects defined in the Self language, and a
> programming
> environment built in Self for writing Self programs. The language and
> environment attempt to present objects to the programmer and user in
> as direct
> and physical a way as possible. The system uses the prototype-based
> style of
> object construction.

That's from the Self website. Self is really pretty cool. It is a pure
OO
language like Smalltalk, with prototype based inheritence, an idea
picked up by
Newtonscript and Javascript. Like Smalltalk before it, Self was started
at Xerox
PARC.

One very intriquing aspect of Self is that you directly manipulate
objects,
adding/deleting instance variables and methods (which are the same: one
holds
data, the other code), dragging them to other objects, chaging
prototypes. So
while the paradigm is a spin on OO, the environment and quite different,
making
it worth having a look at.

Self is still being actively developed with 4.5.0 having been released
shortly
before I wrote this (Jan 2014).

Self is available for OSX and Linux, with the source available on
github.

-   [Self homepage](http://selflanguage.org)
-   [Self Github repo](https://github.com/russellallen/self)
-   [Self lecture from
    Stanford](https://www.youtube.com/watch?v=3ka4KY7TMTU)

Others
------

These are more context dependent. They tend to be special purpose, or
the main
language for a specific environment (e.g. objective-C for OSX or iOS).

### Objective-C

Objective-C is an OO extension of C. In my opinion, Objective-C
is far better designed than C++. It's approach to OO is very similar to
Smalltalk's, by which it is heavily influenced.

The only significant use of Objective-C these days is for OSX and iOS,
and now Apple is replacing it with their new language Swift.

-   [XCode](https://developer.apple.com/xcode/)
-   [Objective-C](https://developer.apple.com/library/mac/documentation/cocoa/conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html)
-   [Swift](https://developer.apple.com/swift/)

### Go

Go is like C redesigned using modern programming language ideas for
modern
computing environments. Examples include a clean generic function
approach to
OO, garbage colelction, concurrancy as part of the language syntax, and
type
inference.

Go was developed at Google for *Google sized problems*, by a team lead
by the
guys who made Unix:
[Robert Griesemer](http://en.wikipedia.org/wiki/Robert_Griesemer),
[Rob Pike](http://en.wikipedia.org/wiki/Rob_Pike), and
[Ken Thompson](http://en.wikipedia.org/wiki/Ken_Thompson). They stated
in 2007
and opensourced the whole thing in late 2009. A rich and engaged
community has
grown up around Go.

To quote a talk given by Rob Pike at the SPLASH 2012 conference:

> "Go is a compiled, concurrent, garbage-collected, statically typed
> language developed at
> Google. Go is efficient, scalable, and productive. Go was designed to
> address the
> problems faced in software development at Google, which led to a
> language that is not
> a breakthrough research language but is nonetheless an excellent tool
> for engineering
> large software projects. Go is a programming language designed by
> Google to help
> solve Google's problems, and Google has big problems."

-   [Go Homepage](http://golang.org)

Of Historical Interest
----------------------

These are languages you will probably never run into unless you go
looking.

Some were ground breaking at the time, and some are conceptually
interesting. At
the very least you sould read a bit about them so you know how we got to
where
we are now. Can knowing them make you a better programmer? If course.
The more
languages you know, the bigger your toolbox of ideas and concepts is.

### Cobol

Cobol was developed in 1959 by a committee from industry, achademia,
and
government. One of COBOL's claims to fame is it's being heavily
influenced by
Grace Hopper. By the end of 1960 the first compilers were available for
a
computer made by RCA and the Remington-Rand Univac.

> "Cobol programs are in use globally in governmental and military
> agencies, in
> commercial enterprises, and on operating systems such as IBM's z/OS,
> Microsoft's Windows, and the POSIX families (Unix/Linux etc.). In
> 1997, the
> Gartner Group reported that 80 % of the world's business ran on Cobol
> with
> over 200 billion lines of code in existence and with an estimated 5
> billion
> lines of new code annually."

### Fortran

This is by most accounts **the** mother tongue. Started in 1954, it
predates all
other programming languages of note, and directly or indirectly
influences
pretty much all the programming languages currently in use.

Fortran was designed by IBM as a programming language for scientific
computing.
It has evolved over time, accreeting features as they came into vogue.
For
example Fortram 2003 added OO support.

> "Since Fortran has been in use for more than fifty years, there is a
> vast body
> of Fortran in daily use throughout the scientific and engineering
> communities.
> It is the primary language for some of the most intensive
> supercomputing
> tasks, such as weather and climate modeling, computational fluid
> dynamics,
> computational chemistry, computational economics, plant breeding and
> computational physics."

Here's something else to think about if you enjoy numeric and scientific
work:

> "We (Fortran programmers) should really stop making an emphasis on
> that
> paragraph regarding fortran+legacy code. To the young newbies starting
> those
> languages, it gives the feeling that the only reason why someone would
> learn
> it is to maintain that legacy. While the truth is something
> completely
> different ... there is a large number of projects today written from
> scratch
> in Fortran (have no idea how things stand in Cobol world) simply
> because it is
> still the best tool for the job. The problem is that there isn't that
> many
> Fortran programmers in % to the total number of programmers, and
> that's why it
> gives the impression of a lanuage not used."

### Algol

Algol is a family of imperative languages originally developed in the
mid-1950s which greatly influenced many other languages. Many, if not
most, of today's popular languages are often described as having "an
Algol syntax". But Algol's influence goes far beyond syntax. A couple
examples:

-   [BNF](http://en.wikipedia.org/wiki/Backus–Naur_Form) (Backus–Naur
   Form) was developed to describe the syntax of Algol 58/60
-   Scheme adopted the block structure and lexical scope of ALGOL

Algol is generally considered to be the first high order language and
many of the language features we take for granted today first saw use
in Algol.

-   [Revised Report on the Algorithmic Language ALGOL
    60](http://viega.org/cs6373/papers/algol60-revisedreport.pdf)

### Simula 67

Simula is the granddaddy of OO, and was a superset of Algol60 designed
for writing simulations. It introduced objects, classes, inheritance and
subclasses, virtual procedures, coroutines, discrete event simulation,
and features garbage collection.

-   [Introduction to OOP in
    Simula](http://staff.um.edu.mt/jskl1/talk.html)
-   [The Cim Compiler](http://simula67.at.ifi.uio.no/cim.shtml)
-   [GSC](http://folk.uio.no/knutroy/gsc/gsc.html)
-   [IBM System 360/370 Compiler and Historical
    Documentation](http://www.edelweb.fr/Simula/)
-   [An Introduction to Programming in
    Simula](http://www.macs.hw.ac.uk/~rjp/bookhtml/)
-   [Compiling Simula: A historical study of technological
    genesis](http://www.idi.ntnu.no/grupper/su/publ/simula/holmevik-simula-ieeeannals94.pdf)

### PL/I

Designed in the mid 1960s as the single programming language for the
(then new)
IBM System/360 mainframe, as a response to FORTRAN's limitations. As
such it was
designed to be all things to all programmers. The goal was to have a
single
language for both scientific programmers (who used Fortran) and
business
programmers (who used Cobol).

As you can see by the quotes above, PL/I didn't quite succeed in
usurping
Fortran and Cobol.

### Pascal

Niklaus Wirth designed Pascal (named in honor of the French
mathematician and
philosopher Blaise Pascal) largely to teach students structured
programming. Linguistically it is a derivative of Algol 68.

Pascal was the pirmary language used in the Apple Lisa, and much or the
early
Macintosh codebase. Knuth based his WEB language (in which TeX was
written) on
PDP-10 Pascal.

Turbo Pascal from Borland was a significant programming environment for
MS-DOS,
and UCSD Pascal was a significant environment for the Apple II and
III. Both Apple and Borland created Object Oriented versions of Pascal.
Borland
eventually spun that into the Delphi language/environment.

Pascal has a special place in my heart: it was the first high level
structured
language I discovered (I had previously worked exclusively in Basic and
Assembly), as well as the first OO language I wrote code in (Turbo
Pascal 5.5).
