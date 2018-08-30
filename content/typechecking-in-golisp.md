Title: Typechecking in GoLisp
Date: 2016-12-14 01:50
Author: dastels
Category: golisp, software
Slug: typechecking-in-golisp
Status: published

GoLisp now provides basic, and optional, type checking for the arguments
and return values of user defined functions. Additionally, primtive
functions also have type checking on arguments, as appropriate. For
example:

\[code lang=text\]  
&gt; (+ 'a 3)  
Error in evaluation:  
Evaling (+ 'a 3). Wrong argument type for argument 0; expected Integer
or Float but got the Symbol: a  
\[/code\]

### (typedef *fname* *arg-type*... \[-&gt; *return-type*\])

This is similar to defining a function: *fname* is the name of a
function that will be defined later (typically the next form) and each
*arg-type* corresponds to an argument). But with `typedef` these are
argument type specifications, not argument names.

These type specifications can take two forms: *type* which can be a
string or symbol, or a set of types separated by a pipe (E.g.
"integer|string") with no spaces. The latter must be a string.

When a function is passed a value that does not match its specified
type(s) an error is raised, similar to what is shown here:

\[code lang=text\]  
&gt; (typedef less-than number number)  
&gt; (define (less-than x y) (&lt; x y))  
&gt; (less-than 1 4.3)  
==&gt; \#t  
&gt; (less-than 1 'a)  
Error in evaluation:  
Evaling (less-than 1 'a). less-than argument 1 has the wrong type,
expected number but was given symbol  
\[/code\]

The argument number in the error starts numbering from 0.

A type specification can also include a type specification of the result
of the function. Note that the `-&gt;` is required:

\[code lang=text\]  
&gt; (typedef less-than number number -&gt; boolean)  
&gt; (define (less-than x y) (if (&lt; x y) 'yes 'no))  
&gt; (less-than 1 4.3)  
Error in evaluation:  
Evaling (less-than 1 4.3). less-than returns the wrong type, expected
boolean but returned symbol  
\[/code\]

The following types are supported:

-   list
-   vector
-   sequence *(equivalent to list|vector)*
-   integer
-   float
-   number *(equivalent to integer|float)*
-   boolean
-   string
-   character
-   symbol
-   stringy *(equivalent to string|symbol)*
-   function
-   macro
-   primitive
-   procedure *(equivalent to function|primitive)*
-   boxedobject
-   frame
-   environment
-   port

Note that the *list* type just requires a ConsCell; if a proper list or
other specific type is required, then either
[pre-conditions](http://daveastels.typed.com/blog/code-contracts-in-golisp)
or explicit tests will be needed.

This capability is completely optional and if not used, adds no
performance penalty.

### (type *func*)

This returns the type signature of *func*.

\[code lang=text\]  
&gt; (type less-than)  
==&gt; (number number -&gt; boolean)  
\[/code\]
