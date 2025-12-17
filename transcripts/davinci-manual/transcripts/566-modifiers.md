---
title: "Modifiers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 566
---

# Modifiers

Each of the Modifier buttons let you manipulate selections and selected control points on the warping

grid in different ways immediately upon clicking each button.

The Modifier buttons

�Increase Falloff/Smooth Selection: If you’ve selected one or more control points, clicking this

button expands the selection to include all adjacent control points surrounding the selection.

�Decrease Falloff/Smooth Selection: If you’ve selected a group of control points, clicking this

button shrinks the selection by deselecting the outermost ring of selected control points, leaving

the inner control points selected.

�Invert Selection: Clicking this button selects all unselected control points, and de-selects all

selected control points. This is useful when you want to make separate color adjustments to both

specifically selected halves of the warping grid.

�Convert Selection to Pin: Clicking this button pins all currently selected control points.

�Select/Pin Column: If you have one or more control points selected, clicking this button expands

the selection to include all points on every column that have at least one selected point.

�Select/Pin Row: If you have one or more control points selected, clicking this button expands the

selection to include all points on every row that have at least one selected point.

�Select/Pin All, Deselect/Pin All: Clicking this button toggles the selected state of the entire

warping grid on or off.

�Reset Selection/Pins: If you have one or more control points selected, clicking this button resets

their position to the original default position in the warping grid, without de-selecting them.

Range

The Range control is a fast method of selecting multiple control points corresponding to a specific

range of colors.

The Range control

�Range: A gradient shows the range of hues currently being presented in the warping grid.

Dragging the left and right handles of the Range control selection box, or dragging within the

range control to set both boundaries, lets you automatically select all control points corresponding

to the hues that appear within the selection box. Once you’ve set a range, you can move the

range to the left and right by dragging the center of the selection. This is a fast way of selecting all

control points within a range of colors for uniform manipulation.


Color | Chapter 136 Color Warper

COLOR

Auto Lock Controls

The Auto Lock controls enables DaVinci Resolve to automatically lock a border of control points

surrounding any control point you select and adjust, which makes highly specific color adjustments

easier to accomplish. These are particularly useful in the Chroma-Luma warping grid.

The Auto Lock controls

�Auto Lock: Enables and disables this behavior.

�X Points Border: Lets you set how many points away from the control point you’re adjusting the

border of locked control points that restricts your adjustments is. How large an area this ends

up being depends on how many points you choose, and on the resolution of the warping grid.

At higher grid resolutions, the same points distance isolates a smaller region of color.

�Lock Column: Lets you choose to restrict your adjustment to affect all control points within a

particular column of the rectangular Chroma-Luma graph. The width of this column is defined by

the border width controls. This is useful when you want to primarily adjust the lightness of a range

of colors, while making a small adjustment to hues.

�Lock Row: Lets you choose to restrict your adjustment to affect all control points within a particular

row of the rectangular Chroma-Luma graph. The height of this row is defined by the border width

controls above. This is useful when you want to primarily adjust the hue of a range of colors, while

making a small adjustment to lightness.

�Lock Region: Lets you choose to restrict your adjustment to affect all control points within a

rectangular region surrounding the selected point. The is useful when you want to adjust a

targeted region of color that corresponds to a well-defined feature of the image, such as a

specifically colored hat, shirt, foliage, or skin tone. Smaller regions will make more specific

adjustments than larger regions.

Smoothing Controls

If you’ve found that you’ve gone a bit too far with an adjustment and need to back off a little bit, the

Smooth controls let you do so gradually, or start over if necessary.

The Smoothing controls

�Smooth Chroma: Each click of this button moves selected control points left or right, back towards

their original position, bringing the hue of the adjusted colors closer and closer to the original hues

of the image. Luma is unaffected.

�Reset Chroma: Resets the position of all selected control points to the original hues of those

control points. Luma adjustments are unaffected.

�Smooth Luma: Each click of this button moves selected control points up or down, back towards

their original position, bringing the luma of the adjusted colors closer and closer to the original

luma of the image. Chroma is unaffected.

�Reset Luma: Resets the position of all selected control points to the original luma of those control

points. Chroma adjustments are unaffected.


Color | Chapter 136 Color Warper

COLOR

Chapter 137

Secondary Qualifiers

Secondary correction describes isolating a specific part of the image,

or a specific subject, using a key.

Keys in DaVinci Resolve are grayscale images that define which areas of the picture you want to alter

(in white) and which parts of the picture you want to leave alone (in black).

Keys can be generated either using the controls in the Qualifier palette, by using a Power Window,

or by importing an external matte,

For more information on how to use external mattes, see Chapter 146, “Combining Keys and

Using Mattes.” This chapter focuses on how you can use qualifiers to key a range of color

values (similarly to doing a green screen key) in order to create a matte with which to do this

kind of isolated adjustment.

Contents

Secondary Qualifiers������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3158

Adding a Secondary Operation to the Node Editor���������������������������������������������������������������������������������������������������������� 3158

The Qualifier Interfaces������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3159

Which Qualifier Do I Use?��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3160

Set the Default Qualifier Mode���������������������������������������������������������������������������������������������������������������������������������������������������� 3161

Basic Qualification Using the 3D Qualifier��������������������������������������������������������������������������������������������������������������������������� 3162

Basic Qualification Using the HSL Qualifier������������������������������������������������������������������������������������������������������������������������ 3166

HSL Qualifier Presets����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3169

Using Highlight to See What You’re Isolating��������������������������������������������������������������������������������������������������������������������� 3170

Using Highlight to Solo Nodes������������������������������������������������������������������������������������������������������������������������������������������������������� 3171

Showing Picker RGB Values��������������������������������������������������������������������������������������������������������������������������������������������������������� 3172

Qualifier Parameters������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3172

HSL Qualification Controls������������������������������������������������������������������������������������������������������������������������������������������������������������� 3172

RGB Qualification Controls������������������������������������������������������������������������������������������������������������������������������������������������������������� 3174

Luma Qualification Controls����������������������������������������������������������������������������������������������������������������������������������������������������������� 3174

3D Qualifier Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3175

Matte Finesse Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3178

The Many Ways to Invert a Key��������������������������������������������������������������������������������������������������������������������������������������������������� 3182

Combining Qualifiers and Windows����������������������������������������������������������������������������������������������������������������������������������������� 3183

Manipulating Keys Using Additional Nodes������������������������������������������������������������������������������������������������������������������������� 3184


Color | Chapter 137 Secondary Qualifiers

COLOR

Secondary Qualifiers

This section covers the use of the Qualifier palette, which lets you pull a 3D, HSL, RGB, or Luma key,

with which to isolate the correction you need. The Qualifier controls are fast and flexible when you

need to isolate an irregularly shaped subject with a distinct range of color or lightness. Since you’re

generating a key by sampling the image, there’s no need for tracking or keyframing, so in the right

situation qualifiers can be your fastest solution. In the following example, the client likes the slightly

cool treatment overall, but wishes that the skin tones were a little more vibrant. This is exactly the sort

of situation where qualifiers can help out. Adding a second node, and using the 3D or HSL Qualifier to

isolate the face makes it relatively simple to add color exactly where you want it.

Adding a second node and using HSL

Qualification to isolate the skin tones

The image with a simple primary correction

The final adjusted image

Just about every control in the Color page can be limited using of the Qualifier modes available in

DaVinci Resolve. This makes the Qualifier palette a jack-of-all-trades tool with 101 uses. A few practical

examples include keying a red element that’s too intense for broadcast, in order to darken it or

desaturate it; keying a range of green foliage, so you can shift its hue to a more attractive color; keying

an actor’s skin tone in a commercial, to apply some selective softening to it; or keying a range of sky,

in which to add blue.

The Qualifier palette is color-space-aware when you’re using Resolve Color Management (RCM) or

ACES. This enables Qualifiers to create high-quality keys as you would expect, no matter what the

color space of the original media is, or what Timeline Color Space you’re using, for both SDR and HDR

mastering. This makes Qualifier isolations easier, and a more consistent experience no matter what

your workflow happens to be.

Adding a Secondary Operation to the Node Editor

Any node can be switched between functioning as a primary correction, where the adjustments you

make affect the entire image, and a secondary correction, where you’re adjusting a specific element in

the scene. The only difference is that nodes being used for secondary corrections are limited using a

qualifier, Power Windows, or an external matte.


Color | Chapter 137 Secondary Qualifiers

COLOR

If you’re planning to add a secondary operation to the current grade, you’ll need to first add another

node in the Node Editor. When pulling a key to qualify part of the image, it’s important to understand

that you’ll be sampling the YRGB values being fed to that node from any previous nodes in the

tree. That means that the state of the image being fed to a node you’re qualifying affects the key

you’re pulling.

For example, if the image coming out of Node 1 is well saturated and has a neutral color

balance with a wide range of colors, but the image coming out of Node 2 applies a low

saturation, monochromatically orange color wash, you may find it more difficult to pull a

detailed key from Node 2 than you would from Node 1.

Choosing your battles–the image coming out of

Node 1 will be easier to key than the highly stylized

image coming out of Node 2

This is important because you have the flexibility of determining from what image you

want to try pulling a qualified key. By connecting the node that’s outputting the best YRGB

image for the key you’re trying to create to the node you’re qualifying, you can control what

you’re keying.

For more information about choosing which node to use for setting up a qualifier,

see Chapter 146, “Combining Keys and Using Mattes.”

The Qualifier Interfaces

The DaVinci Resolve Qualifier palette interface is straightforward. To the left, graphical controls above

numeric parameters let you manually adjust what ranges of each color component contributes to the

key you’re creating. To the right, Selection Range tools below let you define a key by sampling pixels

of the image using the pointer, while below a set of Matte Finesse parameters let you alter the shape

of the key that’s been pulled.

Qualifier palette with HSL controls selected


Color | Chapter 137 Secondary Qualifiers

COLOR

The default qualification mode is the HSL Qualifier, which uses three color components, hue,

saturation, and luma, to define a key. However, you can also use the RGB or LUM (Luma) qualification

modes to pull keys using other combinations of color components. The LUM qualifier mode, in

particular, lets you make targeted adjustments to specific ranges of image lightness. This is a

technique employed by many colorists to alter color temperature within a specific range of image

highlights or shadows.

Alternately, you can use the 3D qualifier to quickly and easily pull well-refined keys by drawing lines to

sample colors from the image that correspond to volumes of color within a three‑dimensional gamut.

While the underlying technology is sophisticated, all you have to do is to draw blue lines to sample

colors you want to isolate, or red lines to sample colors you want to subtract from the isolation you’re

creating, all of which automatically generate a high-quality key. Each line you draw adds a sample to

the selection list; you can turn each sample off and on to evaluate its contribution to the resulting key,

or delete samples that don’t make a positive contribution.

The 3D qualifier

No matter which qualifier mode you use, the Matte Finesse controls make it easy to refine the resulting

key to be even cleaner and more usable. In some instances, you can even take a marginal key that

would otherwise be unusable, and squeeze it into something useful using the Clean Black, Clean

White, and Blur Radius controls.