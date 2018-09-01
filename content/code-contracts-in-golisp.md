Title: Code Contracts in GoLisp
Date: 2016-11-27 03:04
Author: dastels
Category: tutorial
Tags: software
Slug: code-contracts-in-golisp
Status: published

I was having a look at
[Microsoft's Code Contract
library](https://msdn.microsoft.com/en-us/library/dd264808(v=vs.110).aspx)
for C\#. As usual my attitude was "if I want to understand something,
I'll implement it". So I spent an evening and wrote code contract
support
for (and in) GoLisp.

## Some benefits of code contracts ##

**Improved testing:** Contracts do verification on every invocation of
a function.

**Allow more focussed unit testing:** Unit tests can be more focussed
by
ignoring illegal function arguments which are tested for by the
contract.

**Documentation:** Contracts explicitly declare what acceptable
arguments are, what expected result values are, and under what
conditions exceptions occur. Documentation generators can harvest
the contract declarations to document legal argument and return
values.

## The macros ##

First, there is a lexical environment for code that is under contract:
`contract-let`.

    (contract-let bindings body)

Bindings are just like a regular `let*` and are available from the
contract clauses. A common use is to capture initial state for use in an
`contract-ensures` clause later. For example (seen later):

    (contract-let ((old-length (length storage)))
    (contract-ensures (eqv? (length storage) (-1+ old-length)))
    ...

This grabs the length of the underlying list, and before the function
returns ensures that it is one shorter.

Inside the body of a `contract-let` you can use the other contract
macros.

    (contract-requires condition message)

This states that the *condition* must hold at the
point it appears in the body of the `contract-let`. You can supply
an optional string (*message*) that will be appended to the error
message if the contract is violated. These generally make statements
regarding arguments.

    (contract-ensures condition message)

Like the above, except that it is checked after the body of the
`contract-let` has been evaluated. The *condition* can reference
the special binding `contract-result` which contains the result
value of the `contract-let` form.

    (contract-ensures-error pattern condition)

This comes into play when an error is raised by the `contract-let`
body. If any substring of the error message matches *pattern* (a
standard Go regular expression), *condition* is evaluated. If it is
truthy, then the contract is fulfilled. If *condition* evaluates to
something falsy then the contract is violated because the error
occurred in an unexpected situation. In the cases that the contract is
not violated, the original error is reraised.

The recommended structure of a function using contracts is *requires*,
followed by *ensures*, followed by *error ensures*:

    (define (func arg1 arg2)
      (contract-let ()
        (contract-requires ...) ...
        (contract-ensures ...) ...
        (contract-ensures-error ...) ...
        code ...))

When the contracts are checked, *requires* are checked as they appear,
with any violations immediately raising an error. Then the body is
evaluated, followed by *error ensures*, and if none are violated the
*ensures* are checked.

## A contrived error example ##

    (define (test-division x y)
      (contract-let ()
        (contract-ensures-error "Divide by zero" (eq? y 0))
        (/ x y)))

If an divide by zero error is thrown by the division, the contract
states that the denominator must be zero.

## A frame example ##

Of course, contracts work just fine in frame slot functions. Here's a
simple stack.

    (define Stack {
      new: (lambda ()
             {proto\*: Stack
              storage: '()})

      empty?: (lambda ()
                (nil? storage))

      peek: (lambda ()
              (car storage))

      push: (lambda (x)
              (contract-let ()
                (contract-requires (not (nil? x)) "Attempt to push nil")
                (contract-ensures (equal? (peek) x))
                (storage:! self (cons x storage))))

      pop: (lambda ()
             (contract-let ((old-length (length storage)))
               (contract-requires (not (empty?)) "Attempt to pop an empty stack")
               (contract-ensures (not (nil? contract-result))
                                 "Nil was found on the stack and never should be")
               (contract-ensures (eqv? (length storage) (-1+ (length old-storage)))
                                 "Popping did not remove an element")
               (let ((x (car storage)))
                 (storage:! self (cdr storage))
                 x)))

    })


Bank Account example
--------------------

This example is a port of a demo from the Microsoft .Net code
contracts GitHub repo. This is a trivial example, but it shows the
contract clauses in use.

    (define Account {
      supports-overdraft?: \#t

      overdraft-limit: 0

      balance: 0

      new: (lambda (opening-amount overdraft? limit)
             (contract-let ()
               (contract-requires (> opening-amount (- limit))
                                  "Opening amount exceeds overdraft")
               (contract-requires (if overdraft? (> limit 0) (eq? limit 0))
                                  "bad overdraft amount")
               (contract-requires (<= limit 1000)
                                  "overdraft is too big")
               (contract-requires (>= limit 0)
                                  "negative overdraft")

               (contract-ensures (eq? balance opening-amount)
                                 "balance incorrectly set")
               (contract-ensures (eq? overdraft-limit limit)
                                 "overdraft incorrectly set")

               (balance:! self opening-amount)
               (supports-overdraft?:! self overdraft?)
               (overdraft-limit:! self limit)))

      deposit: (lambda (amount)
                 (contract-let ()
                 (contract-requires (> amount 0)
                                    "negative deposit amount")
                 (balance:! self (+ balance amount))))

      withdraw: (lambda (amount)
                  (contract-let ((old-balance balance))
                    (contract-requires (<= amount (+ balance overdraft-limit))
                                       "Amount causes overdraft to be exceeded")
                    (contract-ensures (eq? balance (- old-balance amount))
                                      "incorrect balance calculation")
                    (balance:! self (- balance amount))))

    })

Of note here is the use of the **contract-let** binding capability to
capture the value of a slot at the beginning of the function. This
captured value is then used in a **contract-ensures** clause to verify
that the computation is done correctly. The old value is captured in
this way because there isn't an analog to the
**Contract.OldValue(this.Amount)** capability.

## The code ##

    ;;; Code Contract support for GoLisp
    ;;; Copyright 2016 Dave Astels

    (defmacro (contract-let bindings . body)
      `(let* (,@bindings
              (ensure-clauses '())
              (ensure-error-clauses '())
              (contract-error-message '())
              (contract-result (on-error (begin ,@body)
                                         (lambda (err)
                                           (let ((msg (car (last-pair (string-split err "\n")))))
                                             (when (re-string-match-go "Contractual .+ violation" msg)
                                                   (error msg))
                                             (set! contract-error-message msg)
                                             err)))))
            (for-each eval ensure-error-clauses)
            (for-each eval ensure-clauses)
            contract-result))

    (defmacro (contract-requires condition . message)
      `(unless ,condition
         (error (if (nil? ',message)
                    (format #f "~%~%>> Contractual requirement violation")
                    (format #f "~%~%>> Contractual requirement violation: ~A" (car ',message))))))

    (defmacro (contract-ensures condition . message)
      `(set! ensure-clauses
        (cons '(unless ,condition
                 (error (if (nil? ',message)
                            (format #f "~%~%>> Contractual assurance violation~%")
                            (format #f "~%~%>> Contractual assurance violation: ~A~%" (car ',message)))))
              ensure-clauses)))

    (define (contract-error-match pattern error-message)
      (re-string-match-go pattern error-message))

    (defmacro (contract-ensures-error error-message-pattern condition)
      `(set! ensure-error-clauses
             (cons '(when (not (nil? contract-error-message)) ;error occurred
                      (if (and (contract-error-match ,error-message-pattern contract-error-message)
                               (not ,condition))
                        (error (format #f "~%~%>> Contractual assurance violation for error: ~A~%" contract-error-message))
                        (error contract-result)))
                   ensure-error-clauses)))


The cost
--------

If we take the bank account example and add unchecked versions of the
deposit and withdraw functions:

    unchecked-deposit: (lambda (amount)
                         (balance:! self (+ balance amount)))

    unchecked-withdraw: (lambda (amount)
                          (balance:! self (- balance amount)))

We can then do some timing comparisons:

    > (time (let loop ((count 1000))
              (if (> count 0)
                (begin
                  (deposit:> a 100)
                  (withdraw:> a 100)
                  (loop (-1+ count))))))
    ==> 1054
    > (time (let loop ((count 1000))
              (if (> count 0)
                (begin
                  (unchecked-deposit:&gt; a 100)
                  (unchecked-withdraw:&gt; a 100)
                  (loop (-1+ count))))))
    ==> 98
    > (time (let loop ((count 10000))
              (if (> count 0)
                (begin
                  (deposit:> a 100)
                  (withdraw:> a 100)
                  (loop (-1+ count))))))
    ==> 13556
    > (time (let loop ((count 10000))
              (if (> count 0)
                (begin
                  (unchecked-deposit:> a 100)
                  (unchecked-withdraw:> a 100)
                  (loop (-1+ count))))))
    ==> 1277

This shows that having those fairly simple checks in place consistantly
increases the time required by an order of magnitude.

One advantage of lisp is that it is very easy to provide an alternative
implementation that can turn the contract system into no-ops.

If we define the contract macros as:

    (defmacro (contract-let bindings . body) \`,@body)

    (defmacro (contract-requires condition . message) )

    (defmacro (contract-ensures condition . message) )

    (defmacro (contract-ensures-error error-message-pattern condition) )

then the timing becomes:

    > (time (let loop ((count 1000))
              (if (> count 0)
                (begin
                  (deposit:> a 100)
                  (withdraw:> a 100)
                  (loop (-1+ count))))))
    ==> 140
    > (time (let loop ((count 10000))
              (if (> count 0)
                (begin
                  (deposit:> a 100)
                  (withdraw:> a 100)
                  (loop (-1+ count))))))
    ==> 1664

That's just slightly more than without contracts.

The final version of the code chooses between the two sets of macro
definitions based on whether or not the symbol `**USE_CONTRACTS**` is
defined when GoLisp starts. By default it's undefined, so you incur
minimal performance penalty , but also don't have contracts. You can run
GoLisp with the command line flag `-d "**USE_CONTRACTS**=1"` which will
have GoLisp install the functional version of the contract macros.
