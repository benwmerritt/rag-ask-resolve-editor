---
title: "Fusion Titles and Fusion Templates"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 193
---

# Fusion Titles and Fusion Templates

The abundance of other Fusion titles in the Effects Library are custom-built text compositions with

built-in animation that expose custom controls in the Inspector.

In actuality, these text generators are Fusion templates, which are Fusion compositions that have been

turned into macros and come installed with DaVinci Resolve to be used from within the Edit page like

any other generator.

A Fusion title creating an animated lower third, with controls open in the Inspector

It’s possible to make all kinds of Fusion title compositions in the Fusion page, and save them for

use in the Edit page by creating a macro and placing it within the /Library/Application Support/

Blackmagic Design/DaVinci Resolve/Fusion/Templates/Edit/Titles directory, but this is a topic for

another day.

There’s one other benefit to Text+ generators and that is they can be graded like any other clip,

without needing to create a compound clip first.

MultiText Titles

Built on Text+, the MultiText tool in the Titles category gives you greater flexibility to add and format

multiple text layers, all within the single tool. It introduces a Text List and a slight rearrangement of

controls, prioritizing functionality based on editors’ needs.


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

The MultiText tool in the Titles section lets you create multiple text layers

and styles and composite them all within a single interface.

The Text List serves as a master panel, displaying all created text layers. The list and controls remain

available across Inspector tabs, allowing quick access to tweak both text and its properties at any

time. Directly below the Text List, the Add Text buttons offer three commonly used layout types: Point,

Text Box, and Circle, making it effortless to add your preferred input style.

When Text Box is selected, the newly added Wrap to Text Box and Clip to Text Box checkboxes can

be found under the Layout tab. With Wrap to Text Box selected, your text will automatically continue

on the next line when it reaches the edge of the text box. When Clip to Text Box is selected, it ensures

that any text extending beyond the text box’s boundaries is visually cut off, preventing overflow while

keeping the excess content intact.

There is also a new Page tab, which allows you to add a custom-colored background behind the

text layers.

Saving Titles in the

Media Pool for Future Use

If you’ve created a title in a style that you want to later reuse, for example, a particularly formatted

lower third that will be the basis for every lower-third in your program, you can drag any title from the

Timeline to the Media Pool, and it will be saved as a separate clip. Title clips in the Media Pool are

shown with a thumbnail showing a preview of the text they contain. If you’ve keyframed any animated

text or video adjustments, those keyframes are also saved with this clip.


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

A text generator saved as a clip in the Media Pool

Using Generators

Generators, with the exception of Solid Color, lack editable parameters other than the Composite,

Transform, Cropping, and Dynamic Zoom parameters that are standard for every clip. Additionally,

generators have a Display Name field in the Inspector that lets you give a particular clip a custom

name that appears in the Timeline.

The various video generators included in DaVinci Resolve can be previewed by hovering your pointer

over any thumbnail in the Generators tab. To edit a generator into your timeline, simply grab the

thumbnail of the generator you wish to use, and place it in your Timeline in the Edit page, or in either

the upper or lower Timelines in the Cut page.

The following generators are available:

�10 Step: A grayscale ramp segmented into 10 steps from black to white.

�100mV Steps: A grayscale ramp segmented into segments of exactly 100mV each.

�BT.2111 Color Bar HLG Narrow: Use these bars if your HDR timeline is using a Hybrid Log Gamma

curve (HLG). This is most commonly used in broadcast for its simple backward compatibility with

SDR televisions.

�BT.2111 Color Bar PQ Full: While PQ Full is a part of the Rec. 2100 (BT.2100) specification, it is not

commonly in use at this time. Use this setting only if you know you need it.

�BT.2111 Color Bar PQ Narrow: Use these bars if your HDR timeline is using a format with a PQ

gamma curve (i.e., DolbyVision or HDR10). This is most commonly used for video streaming

services and Blu-ray discs.

�EBU Color Bar: A 1.77:1 aspect ratio set of color bars for PAL-using countries.

�Four Color Gradient: A gradient that blends four different colors at each corner of the frame. You

can adjust the Center X and Center Y parameters to move the center at which all four colors blend

together, and you can change the four colors that appear at each corner using corresponding

color parameters.

�Grey Scale: A simple grayscale ramp from black to white.

�SMPTE Color Bar: An updated 1.77:1 aspect ratio set of color bars for NTSC-using countries.

�Solid Color: A simple fullscreen color generator. A Color parameter lets you choose what

color this generator outputs.

�Window: A simple white-on-black shape generator, defaulting to a white rectangle against a

black background.

�YCbCr Ramp: A gradient designed to test the Y’CbCr signal.


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

ITU-R BT.2111-1 Color Bar Generators

DaVinci Resolve now includes a ITU-R BT.2111-1 specification Color Bar Generator for HDR video.

These are the color bars to use when calibrating, analyzing, or mastering a Rec. 2100 (BT.2100)

HDR signal.

These new color bars have saturation levels set at 100% at the top, and 75% in the middle

section. They also contain Rec. 709 (BT.709) color bars in the lower corners for compatibility with

HD SDR signals. Commonly referenced levels are indicated on the image below. The full color bar

specification can be found on the ITU’s web site: https://www.itu.int/rec/R-REC-BT.2111/en.

The BT.2111-1 color bars and some of the more commonly used levels

The BT.2111-1 color bars on the Vectorscope, hitting their targets at 100% levels on the outside,

75% levels in the middle, and with the Rec. 709 bars represented in the interior


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

Fusion Generators

The Fusion Generators section of the Generators panel contains Fusion effects that have been made

into reusable generators. By default, a single generator, Noise Gradient, appears as an example of

how these work. Fusion Generators work like any other generator. Once edited into the Timeline, they

act like any other clip, and when selected, they expose customizable parameters in the Inspector that

let you tailor their effect to meet your needs.

However, Fusion Generators are highly customizable. Simply opening the Fusion page while the

playhead intersects a Fusion Generator on the topmost track of the Timeline exposes all of the Fusion

nodes that create that generator’s effect, enabling you to rebuild the effect to do whatever you need.

Furthermore, if you know how to create effects in Fusion, you can create your own generators by

making Fusion Macros and saving them to the Effects Library, so they appear in the Fusion Generators

section of the Effects Library.

For more information on how to do this, see Chapter 68, “Node Groups, Macros, and Fusion

Templates,”

Using Stills

You can import still images into the Media Pool, and edit them into the Timeline as clips with custom

durations. By default, imported stills are 10 seconds long, but you can extend a still image’s Out point

to a maximum of 17 hours and 40 minutes in length, which ought to cover just about any project you’re

planning on working on, so long as you’re not Andy Warhol. DaVinci Resolve is correspondingly

capable of importing still image clips referenced by XML or AAF project files, so long as they’re in a

supported format.

DaVinci Resolve supports the use of stills in the following formats:

File Format

Alpha Channel Support

.tif

Yes

.png

Yes

.jpg

No

.dpx

No

.exr

Yes

.dng

No

.psd

No

.tga

Yes

.heif

No

.NEF

No

.CR2

No

Once edited into the Timeline, still image clips have the same Composite, Transform, Cropping,

Retime, and Scaling attributes as any other clip.


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT