---
title: "Perturb"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 526
---

# Perturb

The Perturb modifier generates smoothly varying random values for a given parameter based on

Perlin noise. It can be used to add jitter, shake, or wobble to any animatable parameter, even if the

parameter is already animated. Its results are similar to those of the Shake modifier, although it uses a

different set of controls that may be more intuitive. Unlike other random modifiers, you can apply the

Perturb modifier to polylines, shapes, grid meshes, and even color gradients.

For example, to add camera shake to an existing path, right-click the crosshair and choose Insert >

Perturb, and then adjust the Strength down to suit. Alternatively, right-clicking the path’s “Right-click

here for shape animation” label at the bottom of the Inspector lets you apply perturb to the path’s

polyline. This works best if the polyline has many points—for example, if it has been tracked or hand-

drawn with the Draw Append pencil tool. A third usage option is to use the Insert contextual menu to

insert the modifier onto the Displacement control. This causes the motion along the path to jitter back

and forth without actually leaving the path.

NOTE: Perturb can only add jitter; it cannot smooth out existing animation curves.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Inspector

The Perturb modifier Controls tab

Controls Tab

The Controls tab for Perturb is mainly used for controlling the Strength, Wobble, and Speed

parameters of the random jitter.

Value

The content of this control depends on what type of control the modifier was applied to. If the Perturb

modifier was added to a basic Slider control, the Value is a slider. If it was added to a Gradient control,

then a Gradient control is displayed here. Use the control to set the default, or center value, for the

Perturb modifier to work on.

The Perturb modifier Gradient controls


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Jaggedness

(Polylines and meshes only) This allows you to increase the amount of variation along the length of

the polyline or mesh, rather than over time. Increasing Jaggedness gives a squigglier polyline or more

tangled mesh, independent of its movement.

Phase

(Polylines and meshes only) Animating this can be used to move the ripple of a polyline or mesh along

itself, from end to end. The effect can be most clearly seen when Speed is set to 0.0.

Random Seed Randomize

The Random Seed is used to “seed” the amount of jitter applied by the modifier. Two Perturb modifiers

with identical settings, but different random seeds, produce two completely different results. Click the

Randomize button to assign a random seed value.

Strength

Use this control to adjust the strength of the Perturb modifier’s output, or its maximum variation from

the primary value specified above.

Wobble

Use the Wobble control to determine how smooth the resulting values are. Less wobble implies a

smoother transition between values, while more wobble produces less predictable results.

Speed

Increasing the Speed slider value speeds up the rate at which the value changes. This can increase

the apparent wobbliness in a more predictable fashion than the Wobble control and make the jitter

more frantic or languorous in nature.

Probe

The Probe modifier is one of the most versatile modifiers in Fusion. It allows you to control any numeric

parameter by the color or luminosity of a specific pixel or rectangular region of an image. Think of

driving the Brightness node by probing the pixel values of flickering lights in a shot, or measuring

graded LUTs to compare values.

It can be applied by right-clicking a parameter and selecting Modify With > Probe.

Inspector

The Probe modifier Controls tab

Controls Tab

The Controls tab for the Probe modifier allows you to select the node to probe, define the channel

used to drive the parameter, and control the size of the probed area.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Image to Probe

Drag a node from the Node Editor to populate this field and identify the image to probe.

Channel

Select the channel you want to probe. The usual options are:

�Red

�Green

�Blue

�Alpha

Luma

Once a Probe modifier is present somewhere in your comp, you can connect other node’s values to its

outputs as well. The Probe allows you to connect to its values individually:

�Result

�Red

�Green

�Blue

�Alpha

Position X Y

The position in the image from where the probe samples the values.

Probe Rectangle

By default, the Probe samples only the value of a single pixel at its position. By using the Probe

Rectangle mode, you can sample from a larger area of pixels based on the Evaluation method.

Width Height Controls

These determine the size of the area to be probed.

Evaluation

Sets how the pixels inside the rectangle are computed to generate the output value.

Options include:

�Average: All pixel values inside the rectangle are averaged.

�Minimum: The smallest value of all pixels inside the rectangle is used.

�Maximum: The highest value of all pixels inside the rectangle is used.

The Probe modifier Value tab


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Value Tab

The Value tab controls the range or scale of the modifier adjustment, thereby adjusting the sensitivity

of the Probe.

Scale Input

By default, the Probe generates the Black Value when the probed area results in a value of 0 (i.e.,

black), and it generates its White Value when the probed area results in a value of 1 (i.e., white). By

using this range control, you can modify the sensitivity of the Probe.

Black Value

The value that is generated by the Probe if the probed area delivers the result set in Scale Input Black.

White Value

The value that is generated by the Probe if the probed area delivers the result set in Scale Input White.

Out of Image Value

The value that is generated by the Probe if the probed area is outside the frame boundaries of the

probed image. If probing a rectangle, this value does not generate before the entire rectangle is

outside the frame boundaries of the image to be probed.

Publish

Only parameters that are animated will be available from the Connect To menu. To connect to non-

animated parameters, you must Publish them first. Animated controls are automatically published,

whereas static controls must be published manually.

To publish a static control, right-click the control and select Publish from the contextual menu.

The Publish modifier Controls tab

Controls Tab

The Controls tab shows the published control available for linking to other controls.

Published Value

The display of the published control is obviously dependent on which control is published from

which node.


Fusion Page Effects | Chapter 124 Modifiers

FUSION