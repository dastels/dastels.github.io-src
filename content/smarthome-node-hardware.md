Title: SmartHome: Node Hardware
Date: 2017-04-02 19:45
Author: dastels
Category: project
Tags: hardware, smarthome
Slug: smarthome-node-hardware
Status: published

Nodes are the metaphorical eyes, ears, and hands of the smarthome
system. There will be many of them in a home. Even in my modest
apartment I will probably have about a dozen. So they need to be
unobtrusive, reliable, and fairly inexpensive.

I went through several progressively more refined prototypes, first in
the form of an Arduino Uno shield and a several versions based on the
Arduino Pro Mini before having a reasonably final design .

<img width="100%" src="/images/early_prototypes.jpg" />

When I thought I had it, I breadboarded it to make final tweaks. Here's
the current design on a breadboard. Because it looks cool.

<img width="100%" src="/images/breadboard.jpg" />

Eventually, I had a design I was happy enough with to make a custom PCB.

<img width="100%" src="/images/nodeboard.jpeg" />

Over time some elements have remained constant:

-   Atmega 328 MCU
-   photoresistor for measuring ambient light level
-   an RGB LED (the current design supports common anode and common
    cathode)
-   an nRF24L01+ radio
-   a PIR motion sensor

Some things, however, have evolved:

-   moving from an Arduino Uno shield to an embedded Arduino Pro Mini to
    a completely custom board
-   changing from through-hole components to exclusive use of surface
    mount for everything other than connectors, headers, and power
    capacitors
-   changing from a DHT temperature/humidity sensor to an Si7021 sensor
-   along with the previous point is more focus on using I2C sensors.
-   dropping battery power in favor of a wallwart (I decided that radio
    range and stability was more important)
-   adding an MCP23017 port expander to read configuration and provide
    additional digital IO
-   Adding standard support for a VL53L0X laser proximity sensor
-   Adding standard support for a string of 8 or 60 neopixels

## The circuitry ##

Let's go through the circuitry, once functional block at a time.

### Power ###

<img width="100%" src="/images/node-power.png" />

This is very much like the standard Arduino Uno power circuit. The big
difference is that there is no USB power, and the 3.3v regulator can
supply a full 1A of power compared to the 50mA from the Uno's 3.3v
regulator. This additional capacity is required for the nRF24L01+ radio.

There is a 47µF capacitor on both the 5v and 3.3v supplies, and a
handful of 100nF capacitors scattered around the board between 5v and
ground.

Power is usually supplied via the power connector using a 9v wallwart,
exactly as the Uno. 5v can also be supplied via the FTDI connector when
the MCU is being programmed or by the ICSP connector when the bootloader
is being flashed.

You can use any 7v-12v DC supply; I've been using a [9v 1A wallwart from
Adafruit](https://www.adafruit.com/products/63).

### MCU

<img width="100%" src="/images/node-mcu.png" />

Here we have the heart of the node: the [ATmega328
MCU](http://www.microchip.com/wwwproducts/en/ATmega328). You can see the
16MHz crystal with its capacitors, the reset circuit and the [FTDI
connector](https://www.adafruit.com/product/70). For some reason the
schematic part in Fritzing doesn't agree with the PCB part. The PCB part
is correct. The connections are there, just in the wrong order. Odd.

To the right you can see connectors for the various standard sensors:

Photo connects to a photoresistor for measurement of ambient light. This
is a simple CdS cell which acts as a voltage divider with a 10kΩ
resistor. The more light, the lower the resistance , and the higher the
voltage read by the analog input of the '328.

PIR connects to a [PIR motion
detector](https://www.adafruit.com/products/189) for, naturally, motion
detection. There are pins for power, ground, and the signal from the
sensor. Be careful to plug it in the right way around.

RGB connects to an [RGB LED](https://www.adafruit.com/products/159). The
current limiting resistors are on the board so all that is required is
the LED, itself. Note that both power and ground are on the connector
(which is keyed) so either a common anode or common cathode LED can be
used. This is one of the onboard configuration settings.

Neopixel lets you connect a string of
[neopixels](https://learn.adafruit.com/adafruit-neopixel-uberguide). The
firmware and configuration selection supports either an 8 or 60 pixel
strip. For example, my coffee station has a unit with an [8 pixel
stick](https://www.adafruit.com/products/1426) used as a spot light to
illuminate the work area when I'm standing at it. I have a [60 pixel
strip](https://www.adafruit.com/products/1138) used to provide hands
free under counter lighting on a node in the kitchen.

Finally you can see the I2C and SPI connections toward the top and
bottom, respectively. These connect to the respective subsystems
described next.

### I2C

<img width="100%" src="/images/node-i2c.png" />

I2C is an amazing interface standard. You can get all kinds of sensors
and other useful bits & pieces that you can connect to an MCU using a
simple two wire bus - in addition to the usual ground and power
connections. A node has two builtin I2C devices, and connections for
three more. Note that these use 5v levels, if you want to connect 3.3v
devices you'll need to add a 3.3v regulator and some level shifters to
the connected device. See [Adafruit's Si7021 breakout
board](https://learn.adafruit.com/assets/35932) for an example.

The first is an
[MCP23017](http://ww1.microchip.com/downloads/en/DeviceDoc/21952b.pdf)
at address 0x20 which provides two 8-bit ports. One of these ports is
used for configuration. Each bit is normally held high by the internal
pull-ups, but can be set low by using a jumper. Currently 7 of the bits
are used:

-   0: high -&gt; a PIR motion detector is connected, low -&gt; it isn't
-   1: high -&gt; a photoresistor is connected, low -&gt; it isn't
-   2: high -&gt; a VL53L0X is connected, low -&gt; it isn't
-   3: high -&gt; an Si7021 temperature/humidity sensor is connected,
    low -&gt; it isn't
-   4: high -&gt; the LED is common anode, low -&gt; it's common cathode
-   5: high -&gt; neopixels are connected, low -&gt; they aren't
-   6: high -&gt; 60 neopixels, low -&gt; 8 neopixels
-   7: unused

The other port on the 23017 is used to provide 8 digital I/O bits. these
can be used to connect actuators (e.g. a relay to control a fan) or
sensors that provide a simple digital output.

The other standard I2C device is an
[Si7021](https://cdn-learn.adafruit.com/assets/assets/000/035/931/original/Support_Documents_TechnicalDocs_Si7021-A20.pdf)
temperature and relative humidity sensor at address 0x40. The actual
chip is rather daunting to hand solder, so I've designed the board to
use [Adafruit's breakout board](https://www.adafruit.com/product/3251).
This approach also gives the option of not having a temperature/humidity
sensor if it isn't needed. Despite all that, the final version of the
node may well have the Si7021 directly on the board.

I had originally been using [DHT11 temperature/humidity
sensors](https://www.adafruit.com/product/386) but they were bulky and
used more cpu cycles to interact with than I liked. The Si7021 is more
accurate and since it uses I2C, much easier to interact with.

### SPI ###

<img src="/images/node-spi.png" />

The part of the circuit is fairly simple: an NRF24L01+ breakout board,
and the ICSP connector used to flash the bootloader. The only thing that
warrants comment is that you will want to hack the nRF24L01+ breakout to
improve the stability of the power. I have had success with this by
soldering 100µF electrolytic and 100nF disk capacitors across the power
(3.3v) and ground pins, DIRECTLY ON THE BREAKOUT BOARD. If/when you do
this, take into account the case you are putting the node into. I find
having them stick out parallel to the breakout rather than up and at a
right angle to it works best.

## Sensors ##

Now let's look at the other pieces that connect to a node.

### Photoresistor ###

This is a very basic and simple component. It is a resistor whose
resistance is inversely proportional to the amount of light falling on
it. Combined with a resistor on the board it makes a voltage divider
between 5v and ground. The more light shining on it, the lower the
resistance, the higher the voltage at the midpoint of the divider, and
the larger the value returned by the analog to digital converter it is
connected to.

<img src="/images/photo-resistor.png" />

The photoresistors I have used are standard [cadmium
sulphide](https://en.wikipedia.org/wiki/Cadmium_sulfide) (aka CdS)
photocells. These are cheap and simple and work quite well if all you
need is a general reading on the amount of light. For my purposes this
is fine; all I need is an idea of how bright the room is to help decide
if more lighting is required. Basically "Is the room dark?" A problem
with CdS photocells is that they are not RoHS compliant. You can use a
[phototransistor](https://www.adafruit.com/products/2831) as a RoHS
compliant replacement.

Adafruit (as usual) has a [great
tutorial](https://learn.adafruit.com/photocells) on CdS photocells.

You can get CdS photocells on Amazon for slightly over 10 cents CDN
each, whereas I've seen phototransistors for about 60 cents each. For
hacking and prototyping I'd use (as I have) CdS cells where they are
available/legal but for production versions I would use phototransistors
to avoid having my products banned in areas requiring RoHS compliance.

### PIR Motion Detector

A PIR (which stands for Passive InfraRed) sensor is a staple in anything
that senses motion. More specifically, a warm body that is moving since
it looks at changes in the infrared distribution of what it is looking
at (i.e. heat). They're really good at detecting humans moving about.
Alas, they are also quite good at picking up cats moving about. Pro tip:
cats move about A LOT. Since cats tend to move around on the floor, and
these sensors see in a cone extending out from the sensor (approximately
a 120 degrees), you can mount them high on the wall and/or add some
blinders to limit their view of the floor. As usual, Adafruit has a
[decent tutorial on
PIRs](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/).

PIRs are all mostly the same, and look like this:

<img src="/images/pir.jpg" />

There are some differences between models. Specifically the presence of
a jumper to select retriggerable mode or not, and a sensitivity
adjustment. You want both. Look for units like the one below. You can
see the jumper at the top left and the two adjustable resistors at the
top (the orange twisty things).

<img src="/images/pir_back.jpg" />

I find that retriggerable mode works best. In non-retriggerable mode, a
motion detection starts a single, fixed width, high pulse on the output.
In retriggerable mode, each motion detection will restart the output
pulse timeout. The result is that as long as motion is being detected,
the output will be high. This has proven to be far more useful. The
diagrams below illustrate the difference.

<img src="/images/non-retriggerable.gif" />

Non-retriggerable mode

<img src="/images/retriggerable.gif" />

Retriggerable mode

The *time* adjustment controls the width of the output pulse (or when
retriggerable, how long it lasts after the last motion detection). The
*sensitivity* adjustment adjusts, well, how sensitive the motion
detector is. Fiddle with them to get the behaviour you want.

The PIR is connected to digital pin 2, and a change in it's output
triggers an interrupt. This is allows the node to signal the control
system that motion has started/stopped as soon as possible.

### RGB LED ###

An RGB LED is simply three LEDs (one each red, green, and blue) in a
single component with either their anodes (common anode) or cathodes
(common cathode) connected together. The node sets the color of the LED
in response to a command from the control system. To make life easier,
one of the configuration jumpers sets whether the LED is common anode or
common cathode. The RGB connector has both +5v and ground in addition to
red, green, and blue. As mentioned, the current limiting resistors are
on the board so all that is required is the actual LED.

<img src="/images/common-anode.png" /><img src="/images/common-cathode.png" />

### Neopixels ###

I just love neopixels.

You can connect a bunch of them (limited by the processing power of your
MCU and the amount of current you can provide) without having to have
dedicated PWMs for each, or [some multiplexing
scheme](http://www.instructables.com/id/Multiplexing-with-Arduino-and-the-74HC595/).
I designed the node to handle both an [8-pixel
stick](https://www.adafruit.com/products/1426) as well as a meter of
[60-pixel/meter strip](https://www.adafruit.com/products/1138). I'm
using these as undercounter lighting. The 8-pixel stick is being used to
light my coffee making station. Yes, I have a dedicated space for making
coffee. It's just how I roll.

<img width="100%" src="/images/coffee-station-light.jpg" />

The meter long strip will be lighting under one section of kitchen
cabinets. These will require a tweak to the power circuitry since they
need 3.5 amps peak current. To accommodate that, I have a 5v-4A wallwart
that I'll use to power that unit, with the 5v regulator removed and it's
input & output connected to allow the wallwart to provide 5v directly.
I'll also be increasing the smoothing capacitor on the 5v line
significantly to deal with potentially noisier power.

To learn more about them, see [Adafruit's excellent
tutorial](https://learn.adafruit.com/adafruit-neopixel-uberguide).

### Laser distance sensor

I mentioned connecting a distance sensor to the board for the under
counter lighting nodes. I had started using an Si1145 Digital UV Index /
IR / Visible Light Sensor with an IR LED to measure proximity via
bounced IR. Adafruit has this on a [breakout
board](https://www.adafruit.com/products/1777) for eash connection. I
found that the returned values were inconsistent between devices, and it
seems very sensitive to ambient light.

I switched to a laser time of flight distance sensor, using [Adafruit's
VL53L0X breakout board](https://www.adafruit.com/product/3317) and am
very happy with how it works. It provides a precise distant measure.

Case
----

For my initial purposes (i.e. getting a system that works) I am less
concerned with the look of things. This less than pleases my flat-mate.
My plans are to switch to 3D modeling and make some nicer cases once the
system is up and running and once I get a 3D printer.

Until then, I found a [nice case from
Adafruit](https://www.adafruit.com/products/337) designed for Arduino
shaped boards. This is the prime reason for designing the node board to
match the Arduino footprint. One especially nice feature of this case is
that a [7cm x 3cm piece of proto
board](https://www.amazon.com/gp/product/B012YZ2Q82) can fit perfectly
in either an end or the rectangular face cutout. The PIR sensor also
fits perfectly in the more square cutout (with a touch of glue).

<img width="100%" src="/images/wall_node.jpg" />

A vertically mounted node.

<img width="100%" src="/images/shelf_node.jpg" />

A horizontally, under-shelf mounted node. Note: there are resistors on
the face plate since this is an older prototype; not one of the custom
PCBs.
