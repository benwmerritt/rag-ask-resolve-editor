---
title: "Adding Inputs and Outputs to Compound Nodes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 598
---

# Adding Inputs and Outputs to Compound Nodes

When you open the contents of a compound node using the Show Compound Node command, you

can make whatever adjustments you like to the node tree within, but you also have the option of right-

clicking within the Node Editor and choosing Add Source to add an input to the compound node, or

Add Output to add an output. Adding more inputs and outputs lets you set up the node to connect to

the rest of your node tree in more complicated ways. Disconnected inputs and outputs have no effect

on your grade.

Furthermore, you can also use the Add Alpha Source and Add Alpha Output contextual menu

commands to add KEY inputs and outputs to a compound node, making it easy to route key or alpha

channel data to other connections in the enclosing node tree.

Nesting Compound Nodes

Compound nodes can also be nested within other compound nodes, if necessary.

Grading Compound Nodes

After you’ve created a compound node, you can select it to make one or more adjustments using the

compound node itself, which effectively adds those adjustments after all other adjustments that take

place via the nodes that are inside of the compound node. This gives you the opportunity to “trim” the

effect that compound node is having on your grade, or to limit it using a qualifier or window.

To adjust the individual nodes nested within a compound node, you need to first open the compound

node. Then, you can select and adjust any node as you ordinarily would.

Identifying Nodes

As you make various adjustments to nodes, small badges appear underneath that indicate what each

node is actually doing. Since nodes are capable of holding multiple adjustments, any given node may

have multiple badges; how many badges a node can show depends on the zoom level of the Node

Editor. Larger nodes will show more badges, whereas smaller nodes will show fewer badges, hiding

whichever badges don’t fit.

Another nice organizational feature of the Node Editor is an automatic tooltip that appears whenever

you hover the pointer over a particular node, that shows you a concise list of all the operations applied

to that particular node.

(Left) Badges underneath each node indicate which adjustments it contains.

(Right) Using a node’s contextual menu to put that node into HDR mode


Color | Chapter 143 Node Editing Basics

COLOR

Putting Nodes into HDR Mode

When using various grading controls in the Color page to grade wide-latitude images for HDR output,

you may find it useful to enable the HDR mode of the node you’re working on by right-clicking that

node in the Node Editor and choosing HDR Mode from the contextual menu.

This setting adapts that node’s controls to work within an expanded HDR range. Practically speaking,

this makes it easier to work with wide-latitude signals using controls that operate by letting you make

adjustments at different tonal ranges such as Lift/Gamma/Gain, Custom Curves, Soft Clip, and so on.

Clip vs. Timeline Grading

Ordinarily, the Node Editor has two modes. The default Clip mode lets you create individual

grades for each clip or group in the Timeline. However, the Timeline grade mode lets you apply a

single grade simultaneously to every clip in the Timeline, as seen in the Thumbnail timeline in the

following screenshot.

A paragon of sophisticated grading, the author applies a red edge vignette to

every clip in the project simultaneously using the Timeline grade

There are a variety of reasons you might want to do this. For example, if you’re working on a

commercial spot, you might elect to use Clip grades to do general correcting and scene-to-scene

balancing, and then use the Timeline grade to apply a single stylistic grade to the entire spot

simultaneously. That way, any changes the client wants made to the style of the grade can be instantly

applied to the whole spot.

Another example would be using the Timeline grade to apply corrections meant to address QC issues

running throughout a program, desaturating highlights or selectively darkening a specific shade of red

wherever it appears.

To switch between Clip and Timeline grading modes:

�Choose the mode from the drop-down menu at the top right of the Node Editor.

Selecting Track mode in the Node Editor

�Click the dot in the Node Editor toolbar that corresponds to the Clip or Timeline mode

Two dots show whether you’re in Clip or

Timeline mode; these can be clicked to switch


Color | Chapter 143 Node Editing Basics

COLOR

NOTE: When you reset the Timeline grade using the Color > Reset All Grades and Nodes

command, the Output Sizing parameters are reset as well.

Two dots at the top of the Node Editor let you switch between Clip and Timeline modes via a single

click. If you’re working on a clip that’s part of a group, four dots will be displayed to allow fast access to

the Pre-Clip and Post-Clip Group modes as well.

For more information about group grading, see Chapter 142, “Grade Management.”

Timeline Grades and Saved Stills

When you save a Gallery still, the Clip and Timeline grades are both saved. However, when you apply

a grade from that still, you only apply either the Clip grade, or the Timeline grade, depending on which

mode the Node Editor is in.

For more information on saving and applying grades, see Chapter 143, “Node Editing Basics.”


Color | Chapter 143 Node Editing Basics

COLOR

Chapter 144

Image Processing

Order of Operations

The addition of the HDR palette and Color Warper in DaVinci Resolve 17

necessitated an updated diagram of the order of all image processing operations in

DaVinci Resolve, from input through output.

A truly detailed breakdown now requires two charts as detailed in this chapter; the first chart details

the overall order of operations taking place on every page, while the second zooms into the specific

order of operations occurring within each node of the Pre-Clip, Clip, Post-Clip, and Timeline grades

that you create on the Color page. Understanding the order of operations presented here will make

it easier for you to control the power of the full DaVinci Resolve toolset.

Contents

Overall Image Processing������������������������������������������������������������������������������������������������������������������������������������������������������������� 3330

Image Processing Within Grades����������������������������������������������������������������������������������������������������������������������������������������������� 3331


Color | Chapter 144 Image Processing Order of Operations

COLOR

Overall Image Processing

In the following chart, each image processing operation in DaVinci Resolve is shown in the order in

which it’s processed. Operations are color-coded to indicate the page on which those controls appear,

because in many cases page order does not determine image processing order. Why? Either to make

sure each operation is processed as cleanly as possible, or to give the user the maximum control over

the image. For both of these reasons, image processing order is carefully considered, and in some

cases the best result requires operations on different pages to alternate with one another.

Most of the time, this order of operations is irrelevant to the user who’s only interested in the end

result. However, if you’re trying to achieve something very specific, or if you’re wondering why you

see a particular result when you use the features of the Cut, Edit, Fusion, and Color pages together

all at once, this chart should help make things clear. Finishing artists in particular should find this

chart illuminating.

The overall order of image processing operations in DaVinci Resolve, from input through output


Color | Chapter 144 Image Processing Order of Operations

COLOR