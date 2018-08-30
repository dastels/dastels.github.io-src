Title: Analog to digital
Date: 2015-10-04 23:06
Author: dastels
Category: hardware, software
Slug: analog-to-digital
Status: published

By now I'd controlled an LED and read a digital input. The next step was
to read analog values. The STM32F407 on the Disco board has 3 analog to
digital convertors (ADCs), which can be used to read from 19 different
sources: 16 external sources, two internal sources, and the battery
voltage. I just used 1, so configuration is straight forward.

For an anlog source I used a variable resistor with its ends connected
to ground and +5 volts. The tap gave a voltage between those extremes
that was then connected to an analog input. I used PA0 which connects to
source 0. I configured ADC1 to read that source.

Here are the constants. Some have been seen before, and there are new
ones for the ADC:

    (define pin-mode-in        0)
    (define pin-mode-out       1)
    (define pin-mode-alternate 2)
    (define pin-mode-analog    3)

    (define otype-pushpull  0)
    (define otype-opendrain 1)

    (define ospd-low       0)
    (define ospd-medium    1)
    (define ospd-fast      2)
    (define ospd-highspeed 3)

    (define pupd-none     0)
    (define pupd-pullup   1)
    (define pupd-pulldown 2)

    (define adc-reg-sr   #x00)
    (define adc-bits-eoc #x00000002)
    (define adc-reg-cr2  (* -1 #x08))
    (define adc-reg-dr   #x4C)
    (define adc-reg-ccr  (* -1 #x0304)) 

    (define rcc-reg-apb2enr (* -1 #x44))

Notice that some of the `reg` constants (which are register offsets from
the base address of `adc1`) are negative. This denotes to the `read` and
`write` function that the value read or written should be a byte array
(of 4 bytes) instead of a 30-bit integer.

    (define (init-adc channel-base)
      (config-pin gioa 0 pin-mode-analog otype-pushpull ospd-medium pupd-pulldown)
      (write #vu8(#x00 #x01 #x00 #x00) rcc rcc-reg-apb2enr)
      (write #vu8(#x00 #x03 #x01 #x00) adc1 adc-reg-ccr)
      (write #vu8(#x01 #x00 #x00 #x00) channel-base adc-reg-cr2))

First the PA0 pin to configured for ADC use. Then the ADC1 clock is
enabled. Next ADC1 is configured. Notably DMA is disabled, it's set to
independent channels mode, and set to use a prescaler divisor of 4 and a
sampling delay 0 8 cycles and 12 bits samples. Most of the settings I
needed were defaults, so the configuration actually required was pretty
limited. Finally ADC1 is enabled.

To take a reading I wrote another function, along with a couple helpers:

    (define (check-bit base register bit)
      (not (zero? (bitwise-and (read base register) bit))))

    (define (conversion-done? channel-base)
      (check-bit channel-base adc-reg-sr adc-bits-eoc))

    (define (take-reading channel-base)
      (write #vu8(#x01 #x00 #x00 #x40) channel-base adc-reg-cr2)
      (let loop ((time-remaining #xfff))
        (cond ((zero? time-remaining)
               (display "Reading timed out")
               (newline)
               -1)
              ((conversion-done? channel-base)
               (read channel-base adc-reg-dr))
              (else
               (loop (- time-remaining 1))))))

This is straight forward: initiate the conversion by setting the
`swstart` bit in the `cr2` register, then loop until the
`end of conversion` bit flips to a high state. I also added a timeout so
that it will give up if it doesn't see a conversion in a reasonable
amount of time. When a conversion completes successfully, the value is
read from the `dr` register (i.e. `data register`) and returned.

To show that the ADC code is working, I initially just output the
converted value to the console. However, that's not very interesting so
I hooked up 4 LEDs and controlled them based on the value. Here's the
circuit:

![](https://daveastels.files.wordpress.com/2017/07/adc.png)

I had to initialize those GPIO pins so I put that in a function:

    (define (init-leds)
      (config-pin giod 0 pin-mode-out)
      (config-pin giod 1 pin-mode-out)
      (config-pin giod 2 pin-mode-out)
      (config-pin giod 3 pin-mode-out))

Here's the main function:

    (define (monitor-adc)
      (let ((channel-base adc1))
        (init-adc channel-base)
        (init-leds)
        (let loop ()
          (take-time 10000)
          (let ((result (take-reading channel-base)))
            (if (> result -1)
                (new-adc-result result)))
          (loop))))

This function initializes the system, then goes into an infinite loop
which takes a reading and, if it is valid, passes it to the
`new-adc-result` function:

    (define (new-adc-result val)
      (display "ADC reading: ")
      (display val)
      (newline)

      (let ((percent (/ (* 100 val) 4095)))
        (pin-clear giod 0)
        (pin-clear giod 1)
        (pin-clear giod 2)
        (pin-clear giod 3)
        (cond ((= percent 25) (= percent 50) (= percent 75) (pin-set giod 3)))))

**Wordpress seems to eat greater-than & less-than characters even in a
pre block. So go to bitbucket to see the code.**

First, the reading is output to the console. Then it's used to compute a
percentage (12 bits of resolution gives a maximum value of 4095). All
LEDs are turned off and one is turned on based upon the range into which
the percentage value falls.

Here's what it looks like.

\[vimeo 141365391 w=500 h=889\]

Code is available on
[Bitbucket](https://bitbucket.org/dastels/armpit_scheme).
