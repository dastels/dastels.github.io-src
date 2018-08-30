Title: PWM control of LEDs
Date: 2015-10-08 04:55
Author: dastels
Category: hardware, software
Slug: pwm-control-of-leds
Status: published

Pulse Width Modulation is a technique to vary the duty cycle of a signal
while keeping it's frequency constant. For example:

![duty cycles from
https://learn.sparkfun.com/tutorials/pulse-width-modulation](https://daveastels.files.wordpress.com/2017/07/duty_cycles.jpg)

This turns out to be a very handy thing to be able to do. So much so
that it's a basic feature in most, if not all, MCUs.

LED brightness
--------------

The most basic use is to control the brightness of an LED. Here is a
clip of the four onboard LEDs being controlled by PWMs. They're all
doing the same thing, so it's not the most exciting. But it proves the
point.

\[vimeo 141745926 w=500 h=889\]

### The requisite constants

    (define pin-mode-alternate 2)
    (define otype-pushpull  0)
    (define ospd-highspeed 3)
    (define pupd-none     0)
    (define gpio-af-tim4 2)
    (define timer-reg-cr1 #x00)
    (define timer-reg-ccmr1 #x18)
    (define timer-reg-ccmr2 #x1C)
    (define timer-reg-ccer #x20)
    (define timer-reg-psc #x28)
    (define timer-reg-arr #x2C)
    (define timer-reg-ccr1 #x34)
    (define timer-reg-ccr2 #x38)
    (define timer-reg-ccr3 #x3C)
    (define timer-reg-ccr4 #x40)
    (define rcc-reg-apb1enr (* -1 #x40))

Not that these registers are 16-bit so we can just use integer values
and don't have to use vectors (as you may recall, Armpit uses 30-bit
integers so if we need the top two bits we need to use byte vectors).

### Configuration

    (define (init-gpio-pins)
      (config-pin giod 12 pin-mode-alternate otype-pushpull ospd-highspeed pupd-none gpio-af-tim4)
      (config-pin giod 13 pin-mode-alternate otype-pushpull ospd-highspeed pupd-none gpio-af-tim4)
      (config-pin giod 14 pin-mode-alternate otype-pushpull ospd-highspeed pupd-none gpio-af-tim4)
      (config-pin giod 15 pin-mode-alternate otype-pushpull ospd-highspeed pupd-none gpio-af-tim4))


    (define (config-pwm)
      (write #vu8(#x04 #x00 #x00 #x00) rcc rcc-reg-apb1enr)
      (write #x0000 tmr4 timer-reg-psc)
      (write 255 tmr4 timer-reg-arr)
      (write #x0080 tmr4 timer-reg-cr1)
      (write #x6868 tmr4 timer-reg-ccmr1)
      (write #x6868 tmr4 timer-reg-ccmr2)
      (write #x1111 tmr4 timer-reg-ccer)
      (write #x0081 tmr4 timer-reg-cr1))

GPIO PD12-15 are configured to be connected to the output of timer 4's
comparitors.

Timer 4 is configured to receive a clock signal from the RCC, repeatedly
count from 0 to 255, and drive the output high when the count exceeds
the comparison value.

### Main loop

    (define (take-time n)
      (if (&gt; n 0)
          (begin (* 3 5 7)
                 (take-time (- n 1)))))

    (define (pwm)
      (config-pwm)
      (init-gpio-pins)
      (let loop ((brightness 0)
                 (step 1))
        (write brightness tmr4 timer-reg-ccr1)
        (write brightness tmr4 timer-reg-ccr2)
        (write brightness tmr4 timer-reg-ccr3)
        (write brightness tmr4 timer-reg-ccr4)
        (take-time 1000)
        (cond ((eq? brightness 255)
               (loop (+ brightness -1) -1))
              ((eq? brightness 0)
               (loop (+ brightness 1) 1))
              (else
               (loop (+ brightness step) step)))))

The main function initializes the GPIO pins and timer 4, then enters an
endless loop:  
\* the current brightness value is written to the 4 channels of timer
4,  
\* there's a delay so the effect is slow enough to be visible  
\* the brightness value is checked against each bound (0 & 255), if it's
hit the bound the direction is reveresed, otherwise it continues to the
next value in the same direction.

RGB
---

LEDs are available in a variety of shapes and sizes, but most relevant
to this post: color. Of particular are red, green, and blue LEDs. Why?
because of how light works. These are the tree primary colors of light
and can be combined is various proportions to create any other color. If
we take an LED of each of these three colors and put them close together
our eyes will blend the three into a single color. Very handy.

![](https://daveastels.files.wordpress.com/2017/07/ws2812_closeup.jpg)

All we need to do is drive each of the three with a PWM and we can
create any color we desire. Well, almost any. The actual number is the
product of the number of possible brightnesses of each LED. If we use 8
bit PWMs then each has 256 possible brightness levels. That means we can
make 256 \* 256 \* 256 = 16,777,216 possible colors. In theory. In
reality our eyes can't differentiate that level of nuance. Still, plenty
of colors.

Here's an RGB LED being driven through a variety of colors. The LED is
in the keyswitch.

\[vimeo 141745554 w=500 h=889\]

The ideas behind this code are much the same. You configure the GPIO
pins and the timer. In this example I'm using PWM channels 1, 2, & 3 of
timer 3, connected to PB4, PB5, and PB0, respectively.

The LED circuit is pretty much identical to the one in the [ADC
post](http://daveastels.typed.com/blog/analog-to-digital) other than the
specific GPIO pins being used.

I'll spare you the configuration details, as they are almost identical
to the previous example. You can check the repo for details. I wanted to
control the three colors independently rather than in sync like the
previous example so the main loop is quite different:

    (define steps '((1 0 0)
                    (0 1 0)
                    (0 0 1)
                    (-1 0 0)
                    (0 -1 0)
                    (0 0 -1)))

    (define (rgb)
      (config-pwm)
      (init-gpio-pins)
      (write 0 tmr3 timer-reg-ccr1)
      (write 0 tmr3 timer-reg-ccr2)
      (write 0 tmr3 timer-reg-ccr3)
      (let loop ((red 0)
                 (green 0)
                 (blue 0)
                 (step-list steps)
                 (step-count 0))
        (write red tmr3 timer-reg-ccr1)
        (write green tmr3 timer-reg-ccr2)
        (write blue tmr3 timer-reg-ccr3)
        (take-time 500)

        (if (eq? step-count 255)
            (let ((remaining-steps (cdr step-list)))
              (if (null? remaining-steps)
                  (loop red green blue steps 0)
                  (loop red green blue remaining-steps 0)))
            (let ((step-deltas (car step-list)))
              (loop (+ red (car step-deltas))
                    (+ green (cadr step-deltas))
                    (+ blue (caddr step-deltas))
                    step-list
                    (+ step-count 1))))))

The `steps` constant contains a list of 3-tuples that contain delta
values for red, green, and blue. For example, the first one will
increment the red value while leaving green and blue unchanged. Each
tuple takes 255 times through the loop. Once that's happened it moves to
the next tuple. Once all tuples have been used, it starts again at the
beginning.

Code is available on
[Bitbucket](https://bitbucket.org/dastels/armpit_scheme).
