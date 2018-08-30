Title: My smarthome vision
Date: 2017-07-24 21:15
Author: dastels
Category: smarthome
Slug: 230
Status: draft

The hype
--------

There are several *"Smarthome"* systems on the market, on kickstarter,
or being talked about. The thing is, they aren't all that smart.

The current marketing trend seems to be to brand any device with
anything more than an on/off switch as "smart". And marketing is largely
all it is.

What they are are home automation systems. Any smarts that are involved
are on the part of the user. These systems simply provide a more
convenient way to control the things in your home. Sometimes this is
from a central control panel or a phone. Some systems use bluetooth to
sense who is in a room and control things based on that (e.g. turning on
lights). Or more precisely, whose phone is in the room. But, seriously,
who carries their phone with them all the time when they are at home?

The vision
----------

My vision is grander. A smarthome system has to understand the occupants
of the home. It has to know how people move around, what their activity
patterns are. It has to know when you’re up late or (shudder) early
versus getting up in the middle of the night. It has to learn about you
and use that knowledge to tailor its behaviour to you. A smarthome
system should be like a very good butler or valet. It should learn you
well enough to anticipate your needs.

A great goal, but what is the path to getting there?

Infrared motion sensing
-----------------------

The home needs to track motion within it. This is for a couple reasons:

1.  To know when there is movement in low or no light situations. A
    camera might not work well enough in these situations.
2.  To feed the learning of activity behaviour.

To this end, all areas of the home should be covered by infrared motion
sensors.

Cameras
-------

Cameras are the eyes of the home.

### Motion and Occupant Detection

In conjunction with motion sensors, camera data can be used to tell when
people are in the a space.

### Recognition

Camera data can also be used to recognise the people within home using
facial recognition. Also, whereas a simple motion sensor may not
differentiate between a person and a pet, a camera provides enough
information to tell the difference.

### Levels of camera

Not all sensor nodes need full multi megapixel camera, or even VGA
resolution. There a common 8x8 IR detector that would do a lot of what
I've mentioned, specifically verifying that there is a warm body in the
room, and that it's not a pet.

Voice interface
---------------

Primary interaction with the system is vocal. Voice input system needs
to do several things:

### Capture and understand spoken utterances

This is obvious. The system has to hear and understand what you are
saying to some level. The more involved the semantic analysis is, the
more interactive the system can be, and the more intelligently it can
behave.

### Recognising occupants as well as strangers

Different people have different behaviour, patterns, and needs. The
system should provide a individualised experience/interaction for each
person. In addition to knowing who is interacting with it, it needs to
know when someone unknown is talking to it. This just makes sense from a
security point of view. This is one of the serious limitation of systems
like Alexa.

### Recognising emotion in speech

Sometimes how things are said convey as much or more information as what
is said. This is crucial information for enabling the smarthome to
behave accordingly.

### Conversational Interface

The voice interface has to be conversational. The problem with a system
such as Alexa is that it is not very conversational. One gives it
commands:

*”Alexa, turn the kitchen lights on.”*  
`OK`

In some cases you are asked for minimal additional information

*”Alexa, set a timer.”*  
`for how long?`  
*”one hour”*  
`Timer for one hour, starting now.`

Interaction with current systems is typically initiated by the user. A
notable exception is when a timer terminates and the system alerts the
user, who then stops the alarm. This is just barely a system initiated
interaction.

The voice interface for a proper smarthome system must be fluently
conversational. Amazon is making headway in this area with it's LEX
chatbot system. It already has Polly for test to speech that does a good
job.

Behavioural learning and modelling
----------------------------------

The main goal of learning and modelling the behaviour of the home’s
occupants (and even regular visitors) is to predict it on an ongoing
basis. This can then be used to anticipate desires and requirements. For
example, brewing coffee when it sees you getting up in the morning. Or
knowing when you’re up for some reason in the middle of the night and
setting lighting appropriately.

Another use is to use lighting when you are away to reflect your usual
patterns of behaviour to make it appear that you are home. There are
system that let you do something similar to that, but they simulate what
you think your patterns are, not what they actually are. And you
generally have to remember to turn them on. A truly smart home knows
when you aren't around, and knows when it should pretend you are.

The rest of your life.
----------------------

A smarthome system would have access to your calendars, so it would have
even more indication as to when you're home and when you're likely not.

Security
--------

If your smarthome system knows all this about you, you will want it
fully secure and locked down. Here is one area where I take a stance
again the Internet of Things fad. This stuff should not be on the
internet. That means it should not be stored in the cloud, or sent to a
cloud service for processing. Your data should stay in your home, safe
under digital lock & key.
