Title: Trinket M0 Express Hack
Date: 2017-09-01 02:45
Author: dastels
Category: project
Tags: circuitpython, hardware, software
Slug: trinket-m0-express-hack
Status: published

Introduction
------------

I am a huge fan of the SAMD21 boards that
[Adafruit](https://www.adafruit.com/) is producing. What a huge step up
from the ATMEGA328 or 2560. 48MHz, 32 bit ARM Cortex-M0+, and loads of
flash and ram.

I have several of these boards and am dabbling with
[CircuitPython](https://learn.adafruit.com/micropython-for-samd21/build-firmware?view=all)
(I finally a compelling reason to learn Python!). I have a couple/few
each of [Circuit Playground
Express](https://www.adafruit.com/product/3333), [Feather M0
Express](https://www.adafruit.com/product/3403), [Gemma
M0](https://www.adafruit.com/product/3501), and the most recent: the
[Trinket M0](https://www.adafruit.com/product/3500).

Some advantages of the Gemma and Trinket boards is their small size. One
effect of this is that there is limited board space, which means that
neither of these boards include an exteral SPI flash chip that the
"Express" boards include. This means that you are limited in the amount
of application code (in Python) the board can contain. Note that if
you're working in C/C++ you will be able to fit far more application
code; most likely you will have more than enough space for your code.
Now, since the Trinket and Gemma boards are also limited in their I/O
connections, having a limited amount of code is probably not going to be
a huge problem.

Even so, my first thought when I ordered some Trinket-M0s was to wonder
what would be involved in adding an SPI flash chip. After some research,
hacking, and digging through code I have a working Trinket M0 Express.

Hardware
--------

I used the 2 MByte S25FL116K0XMFI043 SPI Flash chip which I picked up at
[Digikey](https://www.digikey.ca/product-detail/en/cypress-semiconductor-corp/S25FL116K0XMFI043/1274-1124-1-ND/4517143).
This is the same chip that is on the Feather M0 Express boards I have.

Getting the SPI flash chip connected to the SAMD21E18 was
straightforward. By comparing the schematics and board specific code of
the Feather M0 Express and the Trinket M0, it was clear that I just had
to connect the flash chip to a set of unused SERCOM capable pins. I
chose pins 17-20 (PA16-PA19). Additionally I used pin 14 (PA11) for the
SPI select line. Connection is simple, with direct connections between
the MCU pins and the corresponding SPI flash pins.

While figuring out what connections were required was easy enough,
making them was a bit more challenging. I'm very handy with a soldering
iron, including SMT work, but this was touchy. The MCU has very little
pin surface exposed, and they are very close together. Using wire-wrap
wire and an SMT iron tip it wasn't too hard, but was still moderately
daunting.

For my initial prototype I mounted the flash chip on an [SOIC-8 breakout
(from Adafruit)](https://www.adafruit.com/product/1212) so that I could
plug it into a breadboard to make hookups easy. I likewise added headers
to the Trinket and mounted it to the bread board as well. This let me
easily tap into the ground and 3v output from the Trinket, as well as
hold it solidly in place relative to the Flash chip. This minimized any
forces on the solder joints on the MCU pins.

<img width="100%" src="/images/trinket-and-flash-mounted-e1504196631661.jpg" />

To make the connections, I first put the Trinket in a board holder and
soldered short lengths of wire-wrap wire to the MCU pins I was using.

<img width="100%" src="/images/wires-on-mcu-e1504196771749.jpg" />

With that done, it was a simple matter to solder the other ends of the
wires to the flash chip. I added short strips of header to the
breadboard to make this even simpler. Note that I added an external
reset pushbutton to minimize the chance of jostling the wires and their
delicate connection to the MCU as much as possible.

<img width="100%" src="/images/connected-and-working-e1504196978187.jpg" />

Software
--------

With the hardware work done, it was time to add a definition of the
"Trinket M0 Express" board to circuit python. I forked Adafruit's repo
and copied the `tinket_m0` directory to `trinket_m0_express` and made
tweaks to the `mpconfigboard.h` and `mpconfigboard.mk` files to reflect
the addition of the external SPI flash. I also tweaked `conf_access.h`
and conf\_usb.h to change the device name to include the "Express"
suffix. Here are the diffs:

    >:diff boards/trinket_m0/conf_access.h boards/trinket_m0_express/conf_access.h
    79c79
    < #define LUN_0_NAME "\"MicroPython VFS[0]\""
    ---
    >#define LUN_0_NAME "\"CircuitPython VFS[0]\""

    >:diff boards/trinket_m0/conf_usb.h boards/trinket_m0_express/conf_usb.h
    24c24
    < # define USB_DEVICE_PRODUCT_NAME "Trinket M0"
    ---
    > # define USB_DEVICE_PRODUCT_NAME "Trinket M0 Express"

    >:diff boards/trinket_m0/mpconfigboard.h boards/trinket_m0_express/mpconfigboard.h
    3c3
    < #define MICROPY_HW_BOARD_NAME "Adafruit Trinket M0"
    ---
    > #define MICROPY_HW_BOARD_NAME "Adafruit Trinket M0 Express"
    10c10,22
    < #define MICROPY_PORT_A (PORT_PA00 | PORT_PA01 | PORT_PA24 | PORT_PA25)
    ---
    > // Salae reads 12mhz which is the limit even though we set it to the safer 8mhz.
    > #define SPI_FLASH_BAUDRATE (8000000)
    >
    > #define SPI_FLASH_MUX_SETTING SPI_SIGNAL_MUX_SETTING_D
    > #define SPI_FLASH_PAD0_PINMUX PINMUX_PA16D_SERCOM3_PAD0 // MOSI
    > #define SPI_FLASH_PAD1_PINMUX PINMUX_PA17D_SERCOM3_PAD1 // SCK
    > #define SPI_FLASH_PAD2_PINMUX PINMUX_UNUSED // Use default pinmux for the chip select since we manage it ourselves.
    > #define SPI_FLASH_PAD3_PINMUX PINMUX_PA19D_SERCOM3_PAD3 // MISO
    > #define SPI_FLASH_SERCOM SERCOM3
    >
    > #define SPI_FLASH_CS PIN_PA11
    >
    > #define MICROPY_PORT_A (PORT_PA00 | PORT_PA01 | PORT_PA11 | PORT_PA16 | PORT_PA17 | PORT_PA18 | PORT_PA19 | PORT_PA24 | PORT_PA25)
    13c25,29
    < #include "internal_flash.h"
    ---
    > #include "spi_flash.h"
    >
    > #define BOARD_FLASH_SIZE (0x00040000 - 0x2000)
    >
    > #include "flash_S25FL216K.h"
    15c31
    < #define BOARD_FLASH_SIZE (0x00040000 - 0x2000 - 0x010000)
    ---
    > #define CALIBRATE_CRYSTALLESS 1

    >:diff boards/trinket_m0/mpconfigboard.mk boards/trinket_m0_express/mpconfigboard.mk
    1c1
    < LD_FILE = boards/samd21x18-bootloader.ld
    ---
    > LD_FILE = boards/samd21x18-bootloader-external-flash-crystalless.ld
    5c5
    < FLASH_IMPL = internal_flash.c
    ---
    > FLASH_IMPL = spi_flash.c

This seems straight forward, but actually involved digging through the
CircuitPython and SAMD21 driver code and documentation to figure out how
everything fit together. It's accurate to say that I have a much better
understanding of the inner workings of the SAMD sercom functionality and
configuration now.

Version 2
---------

Once I had it cobbled together on a breadboard, and the software squared
away, it was time to make a more useful version. As before I started by
soldering short lengths of wire-wrap wire onto the SAMD21 pins.

<img width="100%" src="/images/v2-wires.jpg" />

This time I wanted a self-contained version, so I piggybacked the flash
ship onto the MCU with some epoxy. I also put epoxy over the pins that
had the wires soldered onto them to protect the connections. One change
I made from this photo before the epoxy set was to rotate the flash chip
180 degrees.

<img width="100%" src="/images/v2-piggyback-flash.jpg" />

This is the final version with the wiring finished, and the SPI select
pullup resister added.

<img width="100%" src="/images/v2-very-final.jpg" />

Conslusion
----------

So there it is. With a couple days (total) of research, code spelunking,
soldering, and coding I now have an "express" version of the Trinket M0.
The final version of the hardware build took maybe a half an hour not
counting the time for the epoxy to set. Now I have a tiny M0+ board with
2Mbytes of flash. Now to find something to use it for.

I'm now wondering how hard it would be to redesign the board to put the
flash chip on the underside. Since the board design files are open
source, I may just give this a try.

Tidying up
----------

I've made another Trinket M0 Express, this time focusing on making the
wiring a bit tidier:

<img width="100%" src="/images/tidiertrinketm0express.jpg" />

CircuitPython 2.0 update
------------------------

It took all of 5 minutes to add my "Trinket M0 Express" support to
[CircuitPython
2.0](https://blog.adafruit.com/2017/09/12/circuitpython-2-0-0/) that was
just released. All that was required was to add on line for NVRAM
support.
