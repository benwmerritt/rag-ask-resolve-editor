---
title: "Combining Qualifiers and Windows"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 571
---

# Combining Qualifiers and Windows

This is covered in more detail in a subsequent section, but if you create a key using one of the

Qualifier modes, and you then add a Window, the final key that’s output by that node is limited to the

intersection of the Qualifier key and the Window. This makes it easy to use a Window to “garbage

matte” out bits of a key that you don’t want, that can’t be eliminated by further adjustment of the

Qualifier controls.

The woman’s skin tone is too close to other elements in the scene.

A Circular Power Window is used to further isolate the woman being isolated.


Color | Chapter 137 Secondary Qualifiers

COLOR

Manipulating Keys Using Additional Nodes

If you need to make more adjustments to a qualified key than the Matte Finesse controls will allow, you

can use the Node Editor to feed the key output of one node to the RGB input of another, at which point

you can use all of the second node’s color adjustment controls to manipulate the grayscale image that

constitutes that key, to improve it.

Connecting a key output to an RGB input, and then connecting the

RGB output back to the next node’s KEY input again

You can also use the Key Mixer node to combine multiple keys in several different ways, adding

keys together, or subtracting them from one another, in order to create exactly the key you need.

Adding multiple keys together using a Key Mixer

For more information about these techniques, see Chapter 146, “Combining Keys and

Using Mattes.”


Color | Chapter 137 Secondary Qualifiers

COLOR

Chapter 138

Secondary Windows

Secondary correction describes isolating a specific part of the image, or a specific

subject, using a key.

Keys in DaVinci Resolve are grayscale images that define which areas of the picture you want to alter

(in white) and which parts of the picture you want to leave alone (in black).

Keys are generated either using the controls in the Qualifier palette, by using a Power Window, or by

importing an external matte.

For more information on how to use external mattes, see Chapter 146, “Combining Keys

and Using Mattes.” This chapter shows you how to use Power Windows to create shapes

with which you can isolate parts of the image in different ways in order to do these kinds of

targeted corrections.

Contents

Power Windows����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3186

Adding Nodes with Windows�������������������������������������������������������������������������������������������������������������������������������������������������������� 3187

The Window Palette Interface����������������������������������������������������������������������������������������������������������������������������������������������������� 3189

Managing Windows��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3190

Showing and Hiding Onscreen Window Controls�������������������������������������������������������������������������������������������������������������� 3190

Using the High-Visibility Power Window Outline Option������������������������������������������������������������������������������������������������� 3191

Window Transform Controls����������������������������������������������������������������������������������������������������������������������������������������������������������� 3191

Window Softness�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3193

Drawing Curves����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3194

Converting Linear, Circular, and Polygon Windows into Bezier Curves������������������������������������������������������������������ 3195

Resetting the Window Palette������������������������������������������������������������������������������������������������������������������������������������������������������ 3196

Combining Power Windows with the Mask Control��������������������������������������������������������������������������������������������������������� 3196

Copying and Pasting Windows��������������������������������������������������������������������������������������������������������������������������������������������������� 3198

Saving Window Presets������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3198

Using Windows and Qualifiers Together������������������������������������������������������������������������������������������������������������������������������� 3199


Color | Chapter 138 Secondary Windows

COLOR

Power Windows

Power Windows are another way of making secondary correction, being essentially shapes you can

use to isolate regions of the image. Different controls let you use oval, rectangular, polygonal, or

custom curved shapes. Because you can isolate regions of the image by drawing, Power Windows

produce exceptionally clean results, with edges that can be precisely positioned and feathered to

achieve a variety of effects.

Before/after Curve Power Window isolates the sky area for a targeted correction.

Power Windows (also referred to as simply “windows”) are excellent when what you need to adjust

can be encompassed within a clearly defined geometrical area. For example, the oval of a person’s

face, the front of a car, or a wide expanse of sky are all good candidates for windowed adjustments.

A drawback of windows can be that they must be animated to follow whatever subject they’re isolating.

Fortunately, this is where DaVinci Resolve’s powerful tracker comes in, making it easy to track Power

Windows quickly and accurately to follow along with the subject being isolated.


Color | Chapter 138 Secondary Windows

COLOR

Circular Power Window to focus attention to the skin

DaVinci Resolve makes it easy to combine multiple Power Windows in different ways, to intersect

with one another and create even more sophisticated shapes. For example, multiple windows can be

added together, or one window can be used to cut out part of another window, which saves you from

the need to make complicated keyframing operations to animate that window’s shape.

Multiple windows combined to isolate and mask the image.

This section covers the use of Power Windows, how to create and modify them, as well as how to

combine multiple windows, and combine windows and qualifiers to create highly specific isolations.

Adding Nodes with Windows

As with qualifiers, you must first add a node to a grade’s node tree before you begin windowing a

correction. This is because all of the windows within a particular node work together to limit that

node’s grade. As a reminder, any node can be changed from a primary operation that affects the

entire image, to a more targeted secondary operation, simply by turning on a window, using a qualifier,

or enabling an external matte.


Color | Chapter 138 Secondary Windows

COLOR

Serial nodes showing the window on Node 2

If you don’t create a new node before creating a window, you’ll discover you’ve inappropriately

changed a primary correction into a secondary correction. If you create a new serial node,

you’ll then need to use the controls found within the Window palette to turn on a window to

customize for your purposes. However, there are also a set of commands you can use to add

serial nodes with a window already turned on, saving you a few clicks or button presses in

the process.

To add a new node with a window already turned on:

Choose Color > Nodes > Add Serial Node + CPW (Option-C) to create a new serial node with a

circular window.

Choose Color > Nodes > Add Serial Node + LPW (Option-Q) to create a new serial node with a

linear window.

Choose Color > Nodes > Add Serial Node + PPW (Option-G) to create a new serial node with a

polygonal window.

Choose Color > Nodes > Add Serial Node + PCW (Option-B) to create a new serial node with a

Curve window.

When you add a node with a Power Window, the Window palette automatically opens up,

ready for editing.

The Window palette

�The Window palette is divided into three sets of controls: the Window list, the Presets, and the

Transform and Softness controls.


Color | Chapter 138 Secondary Windows

COLOR