Title: Making a light switch
Date: 2015-10-04 22:07
Author: dastels
Category: tutorial
Tags: hardware, software
Slug: making-a-light-switch
Status: published

In the last posts I showed how to control LEDs with the
[STM32F4-Disco](http://www.mouser.com/new/stmicroelectronics/stm32f4discovery/)
board using [ArmPit Scheme](http://armpit.sourceforge.net). In this
port, I read some input.

The circuit
===========

Specifically, I hooked a switch to a GPIO pin and read its state. Then I
used that to control a LED hooked to another GPIO pin. To keep is
simple, I used the same LED as in the last post, adding a switch.

<img src="/images/light_switch.png" />

The code
========

For the input line, I wanted an internal pullup resister, so I needed a
few more constants. Here's all the options for the `config-pin` function

    (define pin-mode-in 0)
    (define pin-mode-out 1)
    (define otype-pushpull 0)
    (define otype-opendrain 1)
    (define ospd-low 0)
    (define ospd-medium 1)
    (define ospd-fast 2)
    (define ospd-highspeed 3)
    (define pupd-none 0)
    (define pupd-pullup 1)
    (define pupd-pulldown 2)

I didn't need any utility functions as the logic is simple. So here's
the main function:

    (define (light-switch)
      (let ((port giod)
            (led-pin 10)
            (switch-pin 9))
        (config-pin port led-pin pin-mode-out)
        (config-pin port switch-pin pin-mode-in 0 0 pupd-pullup)
        (let loop ()
          ((if (pin-set? port switch-pin) pin-clear pin-set) port led-pin)
          (loop))))

The main loop continuously reads the switch and turns the LED on or off
based on whether the switch is pressed (indicated by a low signal and
thus a false value).

<iframe src="https://player.vimeo.com/video/141353303" width="640" height="1138" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
<p><a href="https://vimeo.com/141353303">Light Switch</a> from <a href="https://vimeo.com/user44507464">Dave Astels</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
