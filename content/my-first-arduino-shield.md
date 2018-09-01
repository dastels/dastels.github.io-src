Title: My first Arduino shield
Date: 2016-09-06 21:00
Author: dastels
Category: project
Tags: hardware
Slug: my-first-arduino-shield
Status: published

Arduino Uno is a nice, simple platform to hack on but has limited IO.
The Arduino Mega2560 has a ton of IO but is bigger and more expensive.
However, you're not stuck with an Arduino as it comes off the shelf. One
really nice thing about the Arduino platform in general is the ability
to use shields (add-on boards that plug into the Arduino's headers) to
add capabilities.

In my case, I wanted the small size and simplicity of the Uno, but with
digital IO capabilities to rival the Mega. The answer was to make a
shield that gives me more digital IO pins.

After some googling I found the MCP23017 chip. It provides 2 8-bit
digital IO ports, complete with enable-able pull-ups for inputs. It does
this via the I2C interface (there's also an SPI version) so the majority
of the Arduino's IO pins are still available. The I2C address of the
chip is selectable (to one of 8) so it will play well with any other I2C
devices connected to your Arduino. Maybe best of all, it's available in
a DIP-28 package so it's very easy to use on a breadboard as well as
make circuit boards for.

Given the space available on an Uno shield, I decided to use two of the
chips to give me an additional 32 digital IO pins. That, in addition to
the IO on the ATmega328P, should be more than enough for anything I'm
considering at the moment.

Due to the use of the I2C interface, the circuit is incredibly simple:

<img width="100%" src="/images/port-expander_copy_fzz_-_fritzing_-__schematic_view_.png" />

As is the case, my first pass was to breadboard this.

<img width="100%" src="/images/port_expander_breadboard.jpg" />

The first pass at a PCB design was pretty basic:

<img width="100%" src="/images/port_expander_pcb_v1.jpg" />

There were several problems with this:

1.  I put one of the 23017s over the spot where the USB connector is on
    the Arduino. There is pretty much zero clearance there. With the
    leads of the chip sticking through, they will short against the
    connector housing unless you are very careful.
    </p>
2.  While the headers for the 4 ports were simple to route, they are in
    several places on the board, not accessible if you put it anywhere
    but the top of a shield stack (using stackable headers for the
    Arduino connections).

3.  The placement and orientation of the address selection
    jumpers/headers for the chips are inconsistent. Additionally, I
    would prefer the power & ground options to be on the outside edges
    of the 3x3 block, with the address connections in the middle.

4.  Finally, since this was a pretty raw test of Fritzing Fab, I didn't
    take time to do anything with the silk screening.

The next version addressed these issues:

1.  Everything is clear of the USB connector.
    </p>
2.  The I/O pins are in a 16x2 header at the non-USB end of the board.
    In addition to being at the edge of the board, and hence more
    accessible in general, this allows for options when selecting a
    header: straight or right angle headers, either male of female.

3.  The address selection areas are now consistent in their positions
    and orientations, with the selection pins connected to the middle
    set of pins.

4.  Everything is labelled on the silk screen: parts, address
    selections, and the I/O header.

<img width="100%" src="/images/port_expander_pcb_v2.jpg" />

The next step is to move to a version using surface mount tech to make
it more manufacturable. The board is designed and just needs to be
verified.

**UPDATE:**

Here's the final, hand assembled, working SMT prototype.

<img width="100%" src="/images/port_expander_pcb_v3.jpg" />
