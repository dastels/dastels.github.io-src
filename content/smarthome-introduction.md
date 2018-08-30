Title: Smarthome: Introduction
Date: 2017-03-25 19:00
Author: dastels
Category: hardware, smarthome, software
Slug: smarthome-introduction
Status: published

Almost a year ago a friend and I started playing with the idea of
building a smart home control system. Before getting too far I ended up
back in
[Canada](http://www.therichest.com/rich-list/nation/10-reasons-why-canada-is-the-best-country-in-the-world/)
and the friendship dissolved, as they do. I, however, continued evolving
my ideas and I now have what I think is a solid design of a first pass.

The status quo is to take physical action to make things happen around
your home. For example, if you want the lights on in a room, you walk to
the light switch on the wall and change its state. If you want to change
the temperature, you walk over to the thermostat and change its setting.
If you shower and the bathroom gets steamy you leave the fan running and
have to remember to come back later and turn it off.

Things have improved somewhat lately. With lightbulbs like the
[HUE](http://www2.meethue.com) line, you can control lighting from an
app on your phone. If you have a [Nest](https://nest.com) or similar
thermostat you can do likewise. There are several brands of "connected"
outlets that let you remotely control pretty much anything that is
plugged into the wall. Devices and services like
[Alexa/Echo](https://www.amazon.com/Amazon-Echo-Bluetooth-Speaker-with-WiFi-Alexa/dp/B00X4WHP5E)
from Amazon (my personal choice),
[Siri](http://www.apple.com/ios/siri/?cid=oas-us-domains-siri.com),
[Google Home](https://madeby.google.com/home/), and so on give you voice
control. But you still have to initiate action: "Alexa, turn on the
office light"... "I'm sorry Dave, I can't do that". Well, that's what it
feels like sometimes.

My vision is an environment that does what needs doing without you
having to take action. Instead of flipping a switch or asking for my
office light to be switched on, I want the light to turn on when I walk
into the office. But only if needed; the light shouldn't turn on if it's
bright enough already due to light coming in through the window. If I
get up to take a leak at night, the bedroom and bathroom light (and any
hall that might be between them) should turn on so that I don't trip
over something. Like the cat. But not at full brightness; they should
come on just enough so I can see where I'm going. If they happen to be
[RGB](https://en.wikipedia.org/wiki/RGB_color_model) lights, they should
glow dimly red to minimize the effect on my sleepy state and that of
anyone else trying to sleep. And they should do that without me even
having to think about it.

In short, I want my environment to anticipate my needs and wants and
cater to them. So that's what I'm working toward.

I've started writing about the project now that I'm at a point where
there's enough to write about. I'll be looking at the various parts of
the system over a series of blog posts.

Overview
--------

Let's start with an overview of the system. Below is a block diagram
showing the major logical and physical components.

![overview](https://daveastels.files.wordpress.com/2017/06/overview.png){.alignnone
.size-full .wp-image-26 width="472" height="558"}

### Nodes

Nodes are custom
[ATMEGA328](http://www.microchip.com/wwwproducts/en/ATmega328) based
computers connected to a collection of sensors and actuators. That's the
MCU used in the Arduino
[Uno](https://www.arduino.cc/en/Main/ArduinoBoardUno),
[Nano](https://www.arduino.cc/en/Main/ArduinoBoardNano),
[ProMini](https://www.arduino.cc/en/Main/ArduinoBoardProMini), and other
models. In fact, my early prototypes were built around the Uno and
ProMini.

Nodes communicate over a 2.4 GHz wireless mesh network the the base node
using
[nRF24L01+](https://www.nordicsemi.com/eng/Products/2.4GHz-RF/nRF24L01P)
radios. Standard sensors include temperature, relative humidity, ambient
light level, and motion. I have some nodes that include a laser-based
time-of-flight proximity sensor to tell when somebody is in front of the
sensor and how close they are. All nodes have an RGB led for displaying
status. Some have a strip of either 8 or 60
[NeoPixels](https://learn.adafruit.com/adafruit-neopixel-uberguide/overview)
connected. So far, these are the nodes that have a proximity sensor and
are used for walk-up, hands-free undercounter lighting. Other sensors or
actuators can be easily connected via a digital signal (there are 8
available) or [I2C](https://en.wikipedia.org/wiki/I²C) (there are 3
connections available).

I made the decision early on to make the nodes as dumb as possible.
Their main purpose is to take and report sensor readings. They mainly do
this periodically (every minute currently), with a couple exceptions
that will be discussed in the article on nodes.

Nodes also accept and execute commands. Commands include things like
"start/stop looking for somebody close to you", "set the LED to this
colour", and "set a specific extension pin high", "report your sensor
configuration".

### Base Node

The base is responsible for being the middleman between the node mesh
and the control system. It talks to the nodes over the mesh network and
the control system over I2C. It also manages a buffer in each direction
to even out surges. It acts like a funnel for the bursts of data coming
from the nodes; buffering them and passing them on to the host as it
requests messages. Finally, it handles forwarding commands from the
control system to specific nodes.

### Host

This is a small process that simply shuttles data and commands back &
forth between the base node (and thus the nodes in the mesh) via I2C and
the brain via [MQTT](http://mqtt.org).

### Brain

This is where the magic happens. It takes all the data being sent by the
nodes, decides what should happen and has either the nodes, the HUE
system, or something else (e.g. using [AWS
Polly](https://aws.amazon.com/polly/) to generate speech and play it
through a speaker) make it happen.

### HUE

This is an off the shelf Philips HUE lighting system.

Configuration
-------------

System configuration is mostly dynamic. The HUE system is queried for
its lights and groups. The nodes are queried for the configuration of
their standard sensors. There is a single configuration file that
defines a few other things about each node: where it is (this
corresponds to HUE groups), whether ambient light level should be
considered when decided whether to turn on the lights in that group, how
long to wait after motion stops to turn off the light, what's connected
to the extension connector, and so on. This will be covered in detail in
the article on the nodes.

Closing
-------

I'm working on articles focussed on each of the components of the
system. At the same time I'll be building more nodes and deploying them
throughout the rest of my apartment, as well as looking into rewriting
the control software from [GoLisp](https://bitbucket.org/dastels/golisp)
in possibly [mruby](https://mruby.org/), and thinking ahead to the real
goals of this whole project... which I'll write about later.

If you find this interesting, stay tuned for more articles and feel free
to get in touch
