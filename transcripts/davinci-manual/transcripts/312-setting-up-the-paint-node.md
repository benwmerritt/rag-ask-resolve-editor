---
title: "Setting Up the Paint Node"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 312
---

# Setting Up the Paint Node

The Paint node has two inputs. Typical of most Fusion nodes, the orange input background is the

primary input for connecting the “canvas” or image to paint on, while the second blue input is an

Effect Mask. Unlike the Mask Paint node, the Paint node requires a background input to begin painting.

Setting the Paint Node’s Resolution

No matter how you use the Paint node in your node tree, the Paint node assumes the resolution of the

background input image as your working resolution for that operation. Although the Paint tool is in fact

resolution independent and you can change this assigned resolution at any time, it’s essential to make

sure you properly set the resolution of the media you’re working with, because it will affect operations

such as motion tracking that you’ll want to use as part of your paint workflow.

Because of this, the Paint node requires a background input to set the resolution of the “canvas” you’ll

be painting upon. To do this, you can set up a Paint node in the node tree in one of two ways: painting

directly on an image or using Paint as the foreground.

Painting Directly on an Image

You can connect the image you want to paint on directly to the background input of the Paint node.

This is the easiest and cleanest node tree construction, but it doesn’t provide much in terms of

compositing flexibility.

The Paint node is inserted directly after the node it is painting on

Using Paint as the Foreground in a Merge Composite

An alternative setup is to use a Background node to set the resolution for the Paint node, compositing

the result over the actual background using a Merge node. Working this way lets you use the Merge

node’s Apply Mode setting (also referred to as composite modes) to control how your paint strokes are

composited against the image, but it does require a bit more setup.

The Paint node is composited over the image

you want to paint on using the merge


Fusion Fundamentals | Chapter 81 Paint

FUSION

Setting this up requires some configuration of the nodes. The Background node must be fully

transparent and, unless you are doing something simple like using the Stroke tool set to Color to paint

over an image, you must drag the image you want to clone or smudge into the Source Tool field in the

Paint node’s inspector. These steps are described in more detail later in this chapter.

Paint Node Workflow

You begin painting by first selecting the paint stroke type from the Paint toolbar above the viewer.

There are ten stroke types to choose from as well as two additional tools for selecting and grouping

paint strokes.

The stroke types and tools are described in detail, see Chapter 113, “Paint Node,” in the

DaVinci Resolve Reference Manual or Chapter 53 in the Fusion Reference Manual.

The primary tool for painting and cloning is the Stroke tool. The Stroke tool is a fully

animatable and editable vector-based paint stroke and initially uses a duration of the entire

global range.

The Stroke tool is most often used for cloning,

beauty work, and creative paint

Select the Correct Paint Stroke Type

Instead of having multiple dedicated Paint nodes for different operations, the procedural nature of

Fusion’s Paint tool means there is just one tool with a variety of different stroke types. Each stroke type

serves a different purpose. The Paint toolbar above the viewer allows you to choose between different

stroke types and drawing tools. These are grouped into a few categories.

Single-Frame Stroke Types

The Multistroke and Clone Multistroke are explicitly designed for single-frame retouching paint jobs

like removing raindrops in a shot that’s supposed to be a sunny day or removing scratch marks and

dust when restoring vintage content. When handling these types of jobs, these two Multistroke

options are faster than the other stroke types, but they’re not editable later on. This means you must

set up the size and function of the brush as well as the duration for the paint stroke before you paint.

The duration of each of these stoke types is one frame by default, but this can be changed using the

Stroke Duration slider in the Inspector. Multistroke and Clone MultiStroke are basically the same tools,

except Clone Multistroke automatically configures the tool for cloning. In contrast, the Multistroke

requires you to set up the tool for cloning manually.

The Multistroke and Clone Multistroke are

non-editable single frame stroke types


Fusion Fundamentals | Chapter 81 Paint

FUSION

Editable Stroke Types

The Stroke and Polyline are similar in that they can be modified and animated at any time. Also,

they both begin with a duration lasting the entire comp, but that also can be changed using the

Keyframes Editor.

The Stroke and Polyline strokes are

editable and last for the entire comp

The Stroke Tool

One of the most flexible editable stroke types you’ll use for many tasks is the Stroke, because it is fully

animatable and editable. You can animate all elements of the Stroke, and you can use the Write-on/

Write-off parameters to control how the stroke appears onscreen. You can also connect to a tracker

from the Center point of the Stroke if you want to make the stroke follow specific onscreen motion.

By default, the Stroke type does not expose control points for the shape of the path. You can move

and track the center and rotation of the Stroke, but the individual control points that create the spline

are hidden. To reveal the control points, you can open the Stroke Controls at the bottom of the

Inspector and click the Make Editable button.

The Stroke’s control points can be revealed

using the Make Editable button

Although the Stroke type is the most flexible, that flexibility can come at a performance penalty if

you’re painting hundreds of strokes on a frame. For larger numbers of strokes that do not need to be

animated, it’s better to use Multistroke or Clone Multistroke, as these are more processor efficient.

The Polyline Stroke Tool

The Polyline Stroke acts more like a drawing tool than a paintbrush. It includes the same functionality

as the Stroke tool, except that it is created not by dragging or “painting” like a paintbrush, but by

clicking to create a spline path, as you do with masks and motion paths. Without even creating a stroke

in the viewer, the Polyline Stroke can connect to existing polylines like a mask or a motion path.

If a motion path is published, right-clicking on the Shape Animation label at the bottom of the Polyline

Stroke’s Stroke Controls allows you to use the Connect To menu to assume the shape of a motion path

or mask. You can also use this method if you import SVG graphics and want to “paint-on” the outlines.


Fusion Fundamentals | Chapter 81 Paint

FUSION

The Polyline Stroke Shape Animation label

Shape Drawing Tools

Five shape-based drawing tools allow you to draw shapes and either fill them with a color or clone

an area from a source image. All these tools act similarly to the Stroke and Polyline stroke type in that

they are editable at any time and have a default duration spanning the entire global range of the comp.

However, you can edit the duration at any time in the Keyframes Editor.

The Shape Strokes are used to create shapes or clone areas based on shapes

All of the Copy [Shape Name] stroke types require that you connect the source node you are cloning

from into the Paint node, and set the Fill Type menu to Image.

The Copy Shapes require a Source to be directly

connected to the Paint tool and set to Image


Fusion Fundamentals | Chapter 81 Paint

FUSION

Setting the Brush Size

After selecting the Stroke type, the Brush size can be set in the Inspector or more intuitively in the

viewer. With the Paint node selected in the Node Editor and the pointer positioned over the viewer,

you can see an outline of the current brush size. To change the brush size, hold down the Command

key and drag. The circle changes size, so you can set it relative to other objects you may be

painting over.

Brush size can be changed interactively in the viewer

Choosing an Apply Mode

The Apply Mode buttons determine the functionality of the paintbrush. There are eight Apply modes

that set the brush to do things like paint a color, clone from a source, smudge an area, or remove

thin wires.

Apply Mode buttons determine the paint brush functionality

Picking a Paint Color

There are several ways to pick the paint color and opacity for a colored brush stroke. You use the Fill

button in the row of Apply modes when you want to paint with a solid color.

The Color swatch shows the current color

Clicking it opens the OS Color Picker window


Fusion Fundamentals | Chapter 81 Paint

FUSION

To select a color for the paint brush, do one of the following:

�Click the color swatch to open a standard OS Color Picker window.

�Drag the Eyedropper into the viewer.

�Drag inside the color chooser to select a saturation and luminance. Drag on the sidebars to

change the hue and transparency.

When you paint, each stroke is unpremultiplied, so adjusting the Alpha slider in the Inspector does not

affect what you apply to the RGB channels. However, changing opacity affects all four channels.

Cloning from the Frame

Choosing the Clone Apply Mode allows you to paint from one area of an image over another area.

This is the most common use of the Paint tool. It allows you to remove objects or artifacts from a clip

by covering them up with another area of the frame. Depending on the Stroke type chosen, you may

clone on either a single frame or for the entire duration of the clip.

The Clone Apply Mode allows you to sample from one

area and use it as a source to paint over another area

You can use the Clone Apply Mode to clone from the same image connected to the Paint node’s

background input or a different source from the node tree.

To clone from a different area of the same frame:


Select a Stroke type from the Paint toolbar above the viewer.


Using the size slider in the Brush controls section of the Inspector, set the size of the brush.


From the Apply Mode buttons, select the Clone mode.


Option-click over the area in the viewer you want to use as the source. A dot appears showing you

the center of what you’re sampling from.


Fusion Fundamentals | Chapter 81 Paint

FUSION

The Clone source starting area identified by the X

and the paint brush size represented by the circle


Paint over the area you want to cover up using the source pixels.

The Clone completed after selecting the source area

and painting over the flag pole

When trying to erase objects or artifacts from a clip using the Clone Apply Mode, it can sometimes

be easier if you sample from a different frame on the same clip. This works well when the object you

are trying to clone out moves during the clip, revealing the area behind the object. Sampling from a

different frame can use the revealed background by offsetting the source frame.

To clone from a different frame of the same clip:


Select a Stroke type from the Paint toolbar above the viewer.


Set the size of the brush.


From the Apply Mode buttons, select the Clone mode.


Drag the clip (MediaIn or Loader) from the Node Editor into the Source Tool field in the Inspector.

The Paint Inspector with the MediaIn1 dragged from

the Node Editor into the Source Tool field


Fusion Fundamentals | Chapter 81 Paint

FUSION


Click the Overlay checkbox to see the current frame and the offset frame superimposed.


Drag the Time Offset slider to select the source frame you want to use.


Option-click over the area in the viewer you want to use as the source or to offset the source

frame’s position.

Overlay shows two frames overlapped with Time Offset, allowing you to clone from one frame onto another


Paint over the area you want to cover up using the source pixels.

The plane is half painted out using on the Overlay with Time Offset


Disable the Overlay checkbox.

The Clone Apply Mode can use a different

frame from the same clip


Fusion Fundamentals | Chapter 81 Paint

FUSION

TIP: When using a Clone Apply Mode, you can hold down the O key instead of clicking the

Overlay checkbox in Inspector to see the Overlay. Releasing the O key will return to normal

viewing without the Overlay.