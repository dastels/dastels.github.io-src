Title: Blinking an external LED
Date: 2015-10-04 18:55
Author: dastels
Category: tutorial
Tags: hardware, software
Slug: blinking-an-external-led
Status: published

Once ArmPit Scheme was in place and running, and manipulating the
onboard LEDs, it was time to grab some components, wires, and a
breadboard and get hacking.

## The wiring ##

My first project was simple: blink an external LED. Unlike Arduino
boards, the Disco board has male pin headers, not female. This means
that you can't just use the usual wire jumpers to hook to it. You need a
female end. The usual hardware hacking supply shops carry jumper wires
in male-male, male-female, and female-female varieties. Make-female
would have been ideal for connecting to a bredboard, bit I just have
male-male and female-female.

<img width="100%" src="/images/jumpers.jpg" />

Fortunately, I also have some long pin header strips that are great for
connecting these jumpers to a breadboard.

<img width="100%" src="/images/pin_headers.jpg" />

<img width="100%" src="/images/headers_on_breadboard.jpg" />

### The circuit ###

Connecting a LED is, as mentioned above, simple. One resister connected
to a GPIO pin (I used PD10) then a LED connected from the other end of
the LED to ground. Be sure to get the LED right way round or it won't
light... being a diode and all.

<img width="100%" src="/images/external-led.png" />

### The code ###

First some utility constants and functions

    (define pin-mode-out 1)

    (define (toggle port pin)
      ((if (pin-set? port pin) pin-clear pin-set) port pin))

    (define (take-time n)
      (if (&gt; n 0)
          (begin (* 3 5 7)
                 (take-time (- n 1)))))

And the main function which toggles PD10 and waits a bit before looping.
I added a count to it would do this 10 times and exit.

    (define (blink)
      (let ((port giod)
            (pin 10))
        (config-pin port pin pin-mode-out)
        (let loop ((c 10))
          (toggle port pin)
          (take-time 100000)
          (if (zero? c)
              #f
              (loop (- c 1))))))
