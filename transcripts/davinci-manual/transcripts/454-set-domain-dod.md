---
title: "Set Domain [DOD]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 454
---

# Set Domain [DOD]

The Set Domain node

Set Domain Node Introduction

Set Domain is used to adjust or set the active area of an image or the area of the image considered to

have valid data.

It does not change the image‘s physical dimensions. Downstream nodes will not process anything

outside the Domain of Definition (DoD), thus speeding up rendering of computation-intensive nodes.

This node provides an absolute mode, for setting the domain of definition manually, and a relative

mode for adjusting the existing domain of definition.

Inputs

The two inputs on the Set Domain node are used to connect 2D images.

Input: The orange background input must be connected. It accepts a 2D image with the DoD you want

to replace or adjust.

Foreground: The green image input is optional but also accepts a 2D image as its input. When the

foreground input is connected, the Set Domain node will replace the Background input’s domain of

definition with the foreground’s DoD.

Basic Node Setup

The example below assumes an image is connected to a Set Domain node to manually

configure the DoD.

A Set Domain node manually sets the area to limit image processing.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Inspector

The Set Domain Controls tab in Set mode

The Set Domain Controls tab in Adjust mode

Controls Tab

Mode

The Mode menu has two choices depending on whether you want to adjust or offset the existing

domain or set precise values for it.

The same operations can be performed in Set or in Adjust mode. In Adjust mode, the sliders default

to 0, marking their respective full extent of the image. Positive values shrink the DoD while negative

values expand the DoD to include more data.

Set mode defaults to the full extent of the visible image. Sliders default to a scale of 0-1 from left to

right and bottom to top.

Left

Defines the left border of the DoD. Higher values on this slider move the left border toward the right,

excluding more data from the left margin.

1 represents the right border of the image; 0 represents the left border. The slider defaults to 0

(left border).

Bottom

Defines the bottom border of the DoD. Higher values on this slider move the bottom border toward the

top, excluding more data from the bottom margin.

1 represents the top border of the image; 0 represents the bottom border. The slider defaults to 0

(bottom border).

Right

Defines the right border of the DoD. Higher values on this slider move the right border toward the left,

excluding more data from the right margin.

1 represents the right border of the image; 0 represents the left border. In Set mode, the slider defaults

to 1 (right border).

Top

Defines the top border of the DoD. Higher values on this slider move the top border toward the

bottom, excluding more data from the top margin.

1 represents the top border of the image; 0 represents the bottom border. In Set mode, the slider

defaults to 1 (top border).


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other miscellaneous nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.

Switch [Swi]

The Switch node

Switch Node Introduction

Switch is a tool that enables artists to alternate between multiple input sources, allowing the selection

of one output from the chosen inputs. This capability is especially useful for toggling between different

visual elements within a composition. The number of input connections can vary, with the node

supporting a dynamic number of inputs that can be renamed as needed. Controls in the Config tab

allow users to add or remove inputs and change their names.

Switch works with most types of tools, including Shapes and 3D. Additionally, users can find the Switch

modifier in the Modify With and Insert submenus of a control’s context menu, allowing it to be applied

to any supported control.

Inputs

You can add up to nine inputs to a Switch Node using the slider in the Config tools. If you need more

than nine sources, you can type that number manually into the Number of Inputs field.

Basic Node Setup

Connect as many input sources as you wish to the Switch Node, and connect its output to the rest of

the node tree.

The Switch tool receiving three media inputs, allowing you to choose one to go through the transform node


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Inspector

The Switch Controls let you choose a

source to pass through the switch.

Controls

The Switch Controls consist of a Source switcher that lets you choose which source to pass through

the switch.

The Switch Configuration

Config

The Switch Configuration lets you choose the number of inputs and rename them.

�Number of Inputs: Adjust the slider to add the number of inputs you wish to use, up to nine. If you

want more than nine inputs, you can click in the number field and type the number manually.

�Name X: You can change the name of the input from numerical to something more descriptive.

Time Speed [TSpd]

The Time Speed node

Time Speed Node Introduction

The Time Speed node allows image sequences to be sped up, slowed down, reversed, or delayed.

Image Interpolation offers smooth, high-quality results. Time Speed should be used for static

speed changes or to introduce delays in the footage. To apply animated changes in time, such as

accelerating or decelerating time, use a Time Stretcher instead.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

When operating in Flow mode, Optical Flow data is required. This node does not generate optical flow

directly. You have to create it upstream using an Optical Flow node or by loading the forward/reverse

vector channels from the image.

TimeSpeed does not interpolate the aux channels but instead destroys them. In particular, the Vector/

BackVector channels are consumed and destroyed after computation.

Add an Optical Flow after the Time Speed node if you want to generate flow vectors for the

retimed footage.

Inputs

The single input on the Time Speed node is used to connect a 2D image that will be retimed.

Input: The orange input is used for the primary 2D image that will be retimed.

Basic Node Setup

The Time Speed node setup is as simple as connecting a 2D image into the orange background input

of the node.

A MediaIn node having its speed changed in the Time Speed node.

Inspector

The Time Speed Controls tab

Speed

This control is used to adjust the Speed, in percentage values, of the outgoing image sequence.

Negative values reverse the image sequence. 200% Speed is represented by a value of 2.0, 100% by

1.0, 50% by 0.5, and 10% by 0.1.

The Speed control cannot be animated.

Delay

Use this control to Delay the outgoing image sequence by the specified number of frames. Negative

numbers offset time back, and positive numbers advance time.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Interpolate Mode

This menu determines the how the time speed is processed in order to improve its visual playback

quality, especially in the case of clips that are slowed down. There are three choices in the menu.

�Nearest: The most processor efficient and least sophisticated method of processing; frames are

either dropped for fast motion or duplicated for slow motion.

�Blend: Also processor efficient, but can produce smoother results; adjacent duplicated frames are

dissolved together to smooth out slow or fast motion effects.

�Flow: The most processor intensive but highest quality method of speed effect processing.

Using vector channels pre-generated from an Optical Flow node, new frames are generated to

create slow or fast motion effects. The result can be exceptionally smooth when motion in a clip

is linear. However, two moving elements crossing in different directions or unpredictable camera

movement can cause unwanted artifacts.

Sample Spread

This slider is displayed only when Interpolation is set to Blend. The slider controls the strength of the

interpolated frames on the current frame. A value of 0.5 blends 50% of the frame before and 50% of

the frame ahead and 0% of the current frame.

Depth Ordering

This menu is displayed only when Interpolation is set to Flow. The Depth Ordering is used to

determine which parts of the image should be rendered on top. This is best explained by example.

In a locked-off camera shot where a car is moving through the frame, the background does not move,

so it produces small, or slow, vectors. The car produces larger, or faster, vectors.

The Depth Ordering, in this case, is Fastest on Top, since the car draws over the background.

In a shot where the camera pans to follow the car, the background has faster vectors, and the car has

slower vectors, so the Depth ordering method would be Slowest on Top.

Clamp Edges

This checkbox is displayed only when Interpolation is set to Flow. Under certain circumstances, this

option can remove the transparent gaps that may appear on the edges of interpolated frames. Clamp

Edges can cause a stretching artifact near the edges of the frame that is especially visible with objects

moving through it or when the camera is moving.

Because of these artifacts, it is a good idea to use clamp edges only to correct small gaps around the

edges of an interpolated frame.

Edge Softness

This slider is only displayed when Interpolation is set to Flow and Clamp Edges is enabled. It helps to

reduce the stretchy artifacts that might be introduced by Clamp Edges.

If you have more than one of the Source Frame and Warp Direction checkboxes turned on, this

can lead to doubling up of the stretching effect near the edges. In this case, you’ll want to keep the

softness rather small at around 0.01. If you have only one checkbox enabled, you can use a larger

softness at around 0.03.


Fusion Page Effects | Chapter 111 Miscellaneous Nodes

FUSION

Source Frame and Warp Direction

These checkboxes are displayed only when Interpolation is set to Flow. These controls determine

which frames and which vectors are used to create the in-between frames. Each method ticked on will

be blended into the result.

�Prev Forward: Takes the previous frame and uses the Forward vector to interpolate

the new frame.

�Next Forward: Takes the next frame in the sequence and uses the Forward vector to interpolate

the new frame.

�Prev Backward: Takes the previous frame and uses the Back Forward vector to interpolate

the new frame.

�Next Backward: Takes the next frame in the sequence and uses the Back vector to interpolate the

new frame.

Freeze Frame

Pressing this button automatically adjusts the Speed and Delay controls to freeze playback on the

currently selected frame.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other miscellaneous nodes. These common

controls are described in detail at the end of this chapter in “The Common Controls” section.