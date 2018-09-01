Title: ArmPit Scheme
Date: 2015-10-02 20:11
Author: dastels
Category: tutorial
Tags: hardware, software
Slug: armpit-scheme
Status: published

In my new position as Director of Innovation at SteelSeries I've been
doing plenty of hardware hacking and prototyping. I've done some work
with Arduino, and more recently Teensy3.1. Now I'm playing around with
The [STM32F4 Discovery
board](http://www.mouser.com/new/stmicroelectronics/stm32f4discovery/)
from ST Micro.

The STM32F4Disco is centered around an STM32F407VGT6 MCU that has an ARM
Cortex-M4 core with a wealth of peripherals along with 1M of flash and
192K of ram. That's plenty of room for doing some interesting things...
like run a Lisp. Specifically [ArmPit
Scheme](http://armpit.sourceforge.net).

ArmPit is a fairly complete R6RS implementation of Scheme, with
extensions for low level access and Flash/SD files. It supports a wide
variety of ARM based boards.

First you have to get ArmPit on your Arm board. Go to [the ArmPit
site](http://armpit.sourceforge.net/index.html) and follow the links to
download the latest version. Have a look at the
[HowTo](http://armpit.sourceforge.net/armpit_installation.html) page for
instructions on uploading Armpit to your board. For the STM32F4-Disco
this means using the onboard ST-Link interface. After flashing ArmPit
onto the board you will get a REPL prompt on the user USB port. You'll
need some sort of terminal emulator for this. I'm using
[Serial.app](https://www.decisivetactics.com/products/serial/).

Without doing any hardware hacking, here's an example that manipulates
the on-board LEDs.

Magic numbers are bad, so here are some GPIO configuration constants:

    (define pin-mode-in 0)
    (define pin-mode-out 1)
    (define pin-mode-alternate 2)
    (define pin-mode-analog    3)

    (define otype-pushpull 0)
    (define otype-opendrain 1)

    (define ospd-low 0)
    (define ospd-medium 1)
    (define ospd-fast 2)
    (define ospd-highspeed 3)

    (define pupd-none 0)
    (define pupd-pullup 1)
    (define pupd-pulldown 2)

The M4 also has a true random number generator, which is incredibly
handy. For this demo I'll be using it:

    (define (make-frndu seed)
      (lambda ()
        (/ (bytevector-s32-native-ref (ash (RNG seed) -2) 0) 5.36870911e8)))

    (define r (make-frndu #vu8(1 0 0 0)))

And a couple functions to toggle a output pin and do a bit of a delay:

    (define (toggle port pin)
      ((if (pin-set? port pin) pin-clear pin-set) port pin))

    (define (take-time n)
      (if (> n 0)
          (begin (* 3 5 7)
                 (take-time (- n 1)))))

Here's the main function. It configures the GPIO pins connected to the
onboard LEDs, then loops infinitely (well, until you press control C)
generating a random number between 0 & 100 and toggles LEDs based on
that value.

    (define (blink)
      (config-pin giod 12 pin-mode-out)
      (config-pin giod 13 pin-mode-out)
      (config-pin giod 14 pin-mode-out)
      (config-pin giod 15 pin-mode-out)
      (let loop ((n (* 100 (r))))
        (if (> n 25) (toggle giod 12))
        (if (> n 50) (toggle giod 13))
        (if (> n 75) (toggle giod 14))
        (if (> n 90) (toggle giod 15))
        (take-time 10000)
        (loop (* 100 (r)))))

And here's what that looks like.

<iframe src="https://player.vimeo.com/video/141286614" width="640" height="1138" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
<p><a href="https://vimeo.com/141286614">Driven by code in ArmPit Scheme</a> from <a href="https://vimeo.com/user44507464">Dave Astels</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
