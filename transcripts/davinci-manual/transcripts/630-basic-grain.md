---
title: "Basic Grain"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 630
---

# Basic Grain

These controls are a subset of the Film Grain effect for quick grain settings. If you prefer, you can add

an instance of the full Film Grain effect after the Halation effect on the same node for greater detail.

�Append Gain internally: Turns on the simplified grain control.

�Strength: Adds grain to the halation layer.

�Size: Controls the size of the grains in the halation layer.

�Softness: Softens the grain texture.

�Saturation: Applies saturation on the grain.

Global Adjustments

�View Glow Alone: This checkbox shows the Halation effect alone before it’s added to the frame.

This is a useful setting to turn on when modifying any of the above tools.

The View Glow Alone checkbox shows you only the Halation effect in

isolation and not blended with the underlying image.

�Reduce Highlights: Reduces the effect where it will brighten the scene without contributing

to the halo. This essentially confines the halo to the edges of a region without blowing out the

region itself.

�Aspect Ratio: Stretch or squeeze the glow and grain horizontally for anamorphic projects.

�Detail Loss: Removes sharp detail that the film stock should not have captured by defocusing the

image under the effect.

Vignette

A plugin with two modes for creating vignette effects of different kinds.

�Basic mode gives you Size, Anamorphism, and Softness controls for quickly creating a traditional

lens vignetting effect to darken the edges of the frame. A Color control lets you tint the vignette.

�Advanced mode adds Border Shape, Rotation, Center, Transparency, and Composite Type

controls for customizing this vignetting effect even more specifically.


Resolve FX Overview | Chapter 157 Resolve FX Film Emulation

COLOR

Chapter 158

Resolve FX

Generate

These plugins generate imagery that can be used within grades

and composites in different ways.

Contents

Color Generator��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3495

Color Palette (Studio Version Only)������������������������������������������������������������������������������������������������������������������������������������������� 3495

Grid����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3495


Resolve FX Overview | Chapter 158 Resolve FX Generate

COLOR

Color Generator

Generates a single color using a color picker or eyedropper control. Useful in conjunction with a layer

node’s ability to mix a color with an image using different composite modes.

�Color picker: You can click the color picker and use the resulting color controls to choose a color

to be generated.

�Eyedropper: You can also click the eyedropper to sample a color from the image in the Viewer;

the eyedropper always samples the image from the input of the current node, regardless of how

the current image looks.

Color Palette (Studio Version Only)

More of an analysis tool than a creative effect, this plugin displays the dominant colors of each frame.

�Display Mode: A pop-up that provides four different options.

Color Palette: This displays the most dominant colors in the image as rectangular swatches along

the bottom (8 colors is the default), and the eight most dominant colors in each of the three main

zones of image tonality (shadow, midtone, highlight) are displayed as smaller rectangular patches

just above. This lets you see, at a glance, the color palette of any given shot, and this can be

output for intrepid art directors who find it useful.

Shadow Region, Midtone Region, or Highlight Region: Displays a visual preview of which parts

of the image fall into which regions (as currently defined by the Shadow and Highlight Threshold

sliders). These previews are displayed with the current tonal region appearing saturated and all

other parts of the image appearing black.

�Number of Colors: Defines the number of isolated colors. This can be set to display anywhere

from 8 to 24 patches.

�Shadow and Highlight Threshold: The definition of where shadows, midtones, and highlights end

and begin is controlled by the Shadow and Highlight Threshold sliders.

Grid

As the name implies, this plugin generates a grid overlay on your image. Not a creative effect, but a

useful measuring tool for your images.

�General: These controls let you adjust the overall density and orientation of the grid.

Row Cells and Column Cells: These sliders let you choose how many cells to divide the grid into,

both vertically and horizontally.

Major Line Spacing: Sets how many grid squares will make up a thicker major line on the grid.

A value of zero turns this function off.

�Line Properties: These controls let you control the properties of the grid lines themselves.

Line Color: This color picker control and accompanying eyedropper let you choose a color with

which to draw the grid.

Individual Hor. Line Width and Ver. Line Width: These sliders let you adjust the thickness

of all horizontal or all vertical lines.

Major Line Width: Lets you choose how thick to make the major lines.

Pan, Tilt, Zoom, Rotate, Width, Height, ShearX, ShearY, Pitch, and Yaw: These controls let you

transform the grid to serve whatever purpose is necessary.


Resolve FX Overview | Chapter 158 Resolve FX Generate

COLOR

Chapter 159

Resolve FX Key

DaVinci Resolve includes several Resolve FX dedicated to compositing and keying

tasks that are applied directly on the Timeline.

Contents

3D Keyer�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3497

Selection Range Controls��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3497

Behavior Options������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3498

Usage Options������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3498

Key Adjustments�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3499

Matte Finesse�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3500

Garbage Matte������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3501

Output������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3501

Alpha Matte Shrink and Grow (Studio Version Only)������������������������������������������������������������������������������������������������������� 3502

HSL Keyer���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3503

Selection Range Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3503

Keyer Options�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3503

Matte Finesse�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3504

Garbage Matte������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3505

Output������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3505

Luma Keyer������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3506

Selection Range Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3506

Matte Finesse�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3506

Garbage Matte������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3507

Output������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3508


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR

3D Keyer

Based on the 3D Qualifier in the Color page, the 3D Keyer Resolve FX offers a fast, simple way of

pulling a key to isolate a range of color in the image by dragging your mouse pointer over the parts

of the image you want to key. Each time you drag over the image to add or subtract from the cloud of

values, you’re carving out of a three-dimensional representation of all available colors; this is viewable

in the tools Key Map box and is what gives the 3D Keyer its name.

TIP: If you’re looking to isolate a range of luma values in the image, the HSL or Luma keyer

will give you more control.

The 3D Keyer is a good one to start with if you’re trying to key a blue screen or green screen

background. Its interface of dragging the mouse pointer over the screen color you want to remove,

with live feedback, gives precise control. The 3D Keyer’s greatest strength is the speed with which you

can sample areas of the picture to extract from the final key. However, this can also be a weakness if

your initial samples aren’t giving you satisfactory results because, unlike the Delta Keyer in the Fusion

page, there aren’t many ways to fine-tune the key as it’s being generated. On the other hand, for

well-lit subjects you want to key, two or three samples is all you need. Small numbers of long strokes

will generally give better results in consistently selecting a range of similar colors, like a broad brush.

Conversely, five to ten short strokes act like a fine brush and will only select a very narrow range of

color that you’ve specified.

Selection Range Controls

The Selection Range buttons in the Inspector let you define a key by sampling pixels in the Viewer

with the mouse pointer.

The 3D Keyer Selection Range controls

�Picker: Chooses the initial color to qualify. Longer strokes will tend to give you a better key. In the

Edit page, the Timeline Viewer Overlay must be set to Open FX.

�Picker -: Lets you choose an additional color to exclude from the current qualification; also

available by holding down the Option key.

�Picker +: Choses an additional color region to add to the current qualification.

�Invert: Inverts the current key; qualified areas are then unqualified and vice versa.

�Stroke: Displays the list of picked (+) and unpicked (-) colors, along with their respective

RGB values.

�Delete Stroke: Deletes the current stroke selected in the Stroke drop-down menu.

�Reset: Deletes all strokes and resets the 3D Keyer to its default state.


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR