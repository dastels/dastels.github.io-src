Title: Sun Type 3 Keyboard
Date: 2014-12-27 20:37
Author: dastels
Category: hardware, Uncategorized
Slug: sun-type-3-keyboard
Status: published

Once upon a time, far far away I was in working on my undergrad in a
department that had a mix of equipment. They had a lab full of IBM PC
clones running MS-DOS. These were mainly for the first couple years for
Turbo Pascal work. What was really exciting was the senior lab of Sun
workstations. I instantly fell in love with the Sun 3/60s. Even though
they were no longer state of the art (SparcStations had recently come on
the scene), they were still powerhouses for working with Lisp and
Smalltalk.

Then it was off to grad school in a department that had mainly Sun
workstations. And I was working mainly in Lisp and Smalltalk, so I found
a used [Sun 3](https://en.wikipedia.org/wiki/Sun-3)/50 to have at home.
I forget where I found it (this was long before eBay or Craig's List)
but I got it at a good price.

I loved that computer. Ignoring speed, memory, etc.
([68020](https://en.wikipedia.org/wiki/Motorola_68020) at 15 MHz with
4Mb of Ram \[compare this to the 4GHz [Core
i7](http://ark.intel.com/products/88195) with 64Gb that I'm using these
days... hell compared with the [Raspberry
Pi](https://en.wikipedia.org/wiki/Raspberry_Pi) that's sitting on my
workbench: 1.2GHz 4-core [ARM
Cortex-A53](https://en.wikipedia.org/wiki/ARM_Cortex-A53) with 2G) it is
one of the favorite computers I've ever owned. Part of that was SunOS
(this was before Linux was generally available), part was X11, part was
the huge screen (well, 21" was huge at the time), but a big part was the
Sun Type-3 keyboard.

![img1](https://daveastels.files.wordpress.com/2017/06/img1.jpg){.alignnone
.size-full .wp-image-145 width="800" height="532"}

I've thought of getting one of these again ever since my ex made me get
rid of workstation when I finished grad school. But there was the issue
of it being a weird-ass serial interface that reports custom key
scancodes and not USB. Well, fast forward to 2014 and I'm working at
Steelseries where one of the things we make are keyboards. I got myself
an ergodox and played around with the firmware. Bolstered by all that, I
went looking on eBay and found a type-3 which I bought. The next step
was to build a convertor to interface it with USB.

This eventually led me to the
[tmk\_keyboard](https://github.com/tmk/tmk_keyboard) project, a keyboard
firmware project for the [Teensy](https://www.pjrc.com/teensy/) which
included a variety of convertors including one for Sun's type-5
keyboard. This provided me a good starting point. I had a Teensy 2.0
from the ergodox so I was good to go. Some researching, experimenting,
and plain old hacking resulted in the Type-3 hooked up to my iMac via
USB.

I [forked the tmk repo](https://github.com/dastels/tmk_keyboard) and
added a sun3\_usb subproject/directory with my work.

The Teensy still needs to be moved inside the keyboard case and the
coiled cable replaced with a USB cable. Once I get the right
screwdriver. For now it works and I'm very happy with it.

The continuing story
--------------------

I subsequently replaced the Teensy2 with a Teensy++, giving me more of
everything, but especially more memory of the various sorts. I am
planning to add programmable key bindings/macros.

The Teensy is now inside the keyboard case with a regular USB cable
connecting it to the computer. I also added a reset button to the
outside of the case to make it easy to upgrade the firmware.

![controller](https://daveastels.files.wordpress.com/2017/06/controller.jpg){.alignnone
.size-full .wp-image-144 width="3264" height="2448"}

![cable](https://daveastels.files.wordpress.com/2017/06/cable.jpg){.alignnone
.size-full .wp-image-143 width="2301" height="2564"}
