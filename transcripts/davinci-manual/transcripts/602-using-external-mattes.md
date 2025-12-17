---
title: "Using External Mattes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 602
---

# Using External Mattes

The External Matte node has evolved over the years. What was once purely a means for importing

matte channels for defining opacity and limiting adjustments has expanded to become a way to import

the RGB channels of a media file to be used for overlaying grain, texture, and stylized distress onto an

image, and even as a way to use the channels of a clip itself as a matte.

Matte clips can be added to your project in one of two ways:

�You can add mattes using the Media page, either by attaching them to a clip so a particular matte

is only available to a particular clip as part of a Clip grade, or you can add timeline mattes that

stand alone in the Media Pool, which are then available to any Track grade.

�You can also add a matte to a clip using the Media Pool in the Color page, by dragging a clip from

the Media Pool to the Node Editor. When you do so, that clip is turned into an external matte in the

current grade, which you can use as a matte for secondary adjustments, or as a compositing layer

(in conjunction with the Layer mixer) for mixing textures or images with your grade. That clip is also

automatically attached to the Media Pool clip that corresponds to the clip you’re grading, as a clip

matte, to help you keep track of which clips are using other clips as mattes.

For more information about adding matte clips in the Media page, refer to “Adding and

Removing External Mattes” see Chapter 18, “Adding and Organizing Media with the

Media Pool.””

Whether attached or unattached, mattes operate within a grade using EXT MATTE (external matte)

nodes. EXT MATTE nodes have the following outputs:

An external matte connected to the first node of a grade

�EXT MATTE Outputs: Four blue square key outputs let you output the channels contained within

the EXT MATTE node, but which channels are available affects what is output. If the EXT MATTE

node’s source clip has RGBA channels, then these are available as Alpha, Red, Green, and Blue

key outputs that you can attach to any other node’s key input. On the other hand, if the EXT

MATTE node’s source clip only has RGB channels, then the key outputs that are made available

are Y (luma), Red, Green, and Blue, and a “Use Lum for Alpha Output” setting in the Node Editor

contextual menu lets you use the Y channel as a matte.

An interesting aspect of these four outputs is that each one is dedicated to individual A, R, G, and

B color channels. Ordinarily, External Matte clips are written with matte data written simultaneously


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

to all three RGB channels. However, you could also render separate pure primary-colored mattes

to each color channel (a so-called “disco” matte), so that the Red channel has one matte, the

Green channel another, and the Blue channels still another, thereby exporting three separate

mattes within a single media file, for convenience. If you add another matte to the Alpha channel,

you can even export four mattes within a single file. You can then use each one of these mattes

individually by connecting the correct output of the EXT MATTE node. (Note: For backward

compatibility, projects from versions of DaVinci Resolve previous to 12.5 continue to output RGBY

from the square outputs, not YRGB.)

�RGB Output: A square green RGB output lets you connect the RGB image data of a matte clip to

any other clip’s RGB input. This is especially useful when you’re combining a matte clip with the

current clip using a Layer Mixer node, to create a textured composite of some kind.

External Mattes to Limit Adjustments

Going back to the External Matte node’s original use, mattes are typically grayscale media files that

represent image opacity, and are meant to be used either as alpha channels for creating opacity within

a corresponding RGB clip, or as a matte for limiting effects.

An example of a matte channel would be the key created by a green screen keyer. If you output just

the key, that would be an external matte. If you receive an external matte along with an effects clip,

you can attach the matte to its corresponding RGB clip in the Media page. Then, you can access that

matte via an External Matte node in the Node Editor, so you can use the key it outputs to limit different

kinds of corrections you want to apply.

In the following example, the keyed matte of a green screen composite clip is used to apply different

corrections to the inside and outside of a keyed composite, in order to make the subject match the

background more convincingly.

A matte attached to clip Makeup_Green.mov,

as seen in the Media Pool

To use a clip matte to limit an adjustment within a Clip grade:


Right-click any node, and choose the attached matte you want to use from the Add Matte

submenu of the contextual menu.

By default, the EXT MATTE node that appears has its first output connected to the Connect one of

the EXT MATTE node’s triangular key outputs to the key input of a node you want it to limit.


Select the node to which the EXT MATTE node is attached, and add an Outside node to make it

possible to add adjustments on either side of the matte.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

Node Editor displaying the influence of the external matte

on multiple nodes when the keys are linked


If necessary, select Node 1, and use the Key palette controls to modify the incoming key, inverting

or blurring it as necessary to create the isolation you need.

NOTE: Don’t select the EXT MATTE node, because it exposes different controls in the

Key palette for transforming, flipping, looping, and freezing the matte.

At this point, you can add adjustments to the inside and the outside of this composited shot to

improve the composite.

(Before/After) An external matte is used to apply separate grades to the

foreground and background of a previously composited clip

Ideally, external mattes are exported so that they match the size and duration of the RGB clip

they’re supposed to accompany. If they don’t match or if you’re using some other grayscale clip as

an external matte to create some sort of effect, then there are parameters in the Key palette that

you can use to retime or transform a matte so it works better in your grade.

To slip the sync of a matte relative to the clip it’s attached to:


Select the Ext Matte node you want to slip.


Open the Key palette, and turn off the Lock Matte checkbox.


Raise or lower the Offset parameter until the matte is perfectly aligned with the clip it’s

supposed to match.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

To transform a matte:


Select the Ext Matte you want to transform.


Open the Key palette, and turn off the Lock Matte checkbox.


Use the Pan, Tilt, Zoom, Rotate, Width, Height, HFlip, or VFlip parameters to adjust the matte so it

has the correct geometry.

It’s worth mentioning that you can attach as many external mattes to a single clip in DaVinci Resolve as

you like. For example, if a CGI shot has been delivered with a set of isolation mattes for each of three

characters in the scene, you can import all three mattes and use them to isolate adjustments that you

want to make in the Node Editor.

Extracting External Mattes from OpenEXR Layers

OpenEXR media is capable of containing multiple layers and multiple alpha channels, which can also

be accessed from EXT MATTE nodes. As a result, DaVinci Resolve uses a slightly different but related

procedure for accessing these mattes.

To extract OpenEXR layers as external matte nodes:


Right-click any node, and choose the .exr clip name from the Add Matte submenu of the

contextual menu.

By default, the EXT MATTE node that appears has its first output connected to the Connect one of

the EXT MATTE node’s triangular key outputs to the key input of a node you want it to limit.


Double-click the EXT MATTE node to select it, then right-click it and choose which layer you want

to use from the Select Matte submenu.

Right-clicking an OpenEXR file’s EXT MATTE node to choose which layer to use

OpenEXR files with multiple RGBA layers (or passes) embedded within them (RGBA + RGBA + RGBA

and so on) or OpenEXR files with multiple alpha channels (RGBA + A + A) expose multiple entries

in this submenu. Whichever one you choose is the layer that will be used as a matte by that EXT

MATTE node.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

Once you’ve extracted an OpenEXR layer, you can use it as you would any other EXT MATTE node

described in this section, to limit adjustments (as seen above), or to add texture or transparency (as

seen in the following sections).

When working with a node with multiple matte layers, such as an .exr file, you preview individual matte

layers. To do so, right-click on the node, select Add Matte from the contextual menu, and hover over

the name of the file. A list of all the layers in the node will appear, and by holding down the Option key

while hovering over each layer, it will appear in the Viewer. This can let you quickly check to see if you

are working with the correct matte layer (arm, wheel, shirt, etc.), regardless of what the matte has been

named in the file.

Using External Mattes to Add Texture

You can also use external mattes as creative tools, to add grain and texture. For example, you might

use a more abstract animated matte, or a grayscale film scan of dirt and dust, to apply correction

for effect.

Light leak and dirt and dust images From Warren Eagles’ Scratch FX

collection (FXPHD), designed to add texture to your grades


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

Once attached to a clip, external mattes can be exposed in the Node Editor, and their key output can

be used just like any other key in a node tree.

To use a clip matte to create texture for a Clip or Timeline grade:


When applying a matte as part of a Clip or Timeline grade, right-click any node and choose the

attached or timeline matte you want to use from the Add Matte submenu of the contextual menu.

Unattached mattes appear in the Add Matte > Timeline Mattes submenu.


Disconnect the EXT MATTE node’s key output connection to the Key input of the node it’s

connected to by default.


Add a Layer Mixer to the end of the node tree.


Disconnect the bottom Corrector node’s RGB input, and then connect it to the EXT MATTE node’s

square RGB output.

A node tree set up to feed an EXT MATTE node’s RGB output to the input of a node connected

to a Layer Mixer, in order to blend it with the grade using composite modes


Right-click the Layer Mixer node, and choose Overlay from the Composite Mode submenu to

blend the Ext Matte node most effectively with the grade.


If necessary, you can use the grading controls of the Corrector node to which you’ve attached the

EXT MATTE node to change the characteristics of the texture clip, desaturating it for instance. You

can also select the EXT MATTE node itself, open the Key palette, and use the Transform, Offset,

Loop, or Freeze controls described later to change how the matte appears.

The resulting texture effect, blended with the

grade using the Overlay composite mode

TIP: If you want the texture you create to be unaffected by blur or sharpening operations

within the grade, be sure to add it to the very end of the node tree.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR