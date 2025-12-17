---
title: "How to Key with Primatte"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 446
---

# How to Key with Primatte

You begin keying with Primatte by connecting the blue- or green-screen shot to the orange

foreground input on the Primatte node and the background shot for the composite into the green

background input. Once the connections are made, there are four main steps to using the Primatte:


Select Background Color.


Clean the Background Noise.


Clean the Foreground Noise.


Remove Spill.

Selecting Background Color

�In the Inspector, click the Select Background Color button.

�Position the mouse pointer over the blue/green-screen area in the viewer, somewhere near the

foreground subject.

�Drag over the background color.

Primatte averages the pixels to get a single color. Sometimes Primatte works best when only a

single pixel is sampled instead of a range of pixels.

Should you have difficulties with your keying, try the Select Background Color operation again

with a single dark screen pixel or single light screen pixel.

Instead, If you want to make a rectangular selection, use the Box button in the top left-hand corner

of the viewer. The Median button is the same as Line selection, except that each point sampled

is the result of a 3 x 3 region based on where you click and then apply a median filter. This can

potentially reduce any noisy pixels.

Primatte viewer buttons


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

If the foreground image has a shadow in it that you want to keep in the composite, do not

select any of the dark screen pixels in the shadow. This keeps the shadow with the rest of the

foreground image.

Clean Background Noise

If there are any white or light gray regions in the dark screen area, this is referred to as “noise.”

Technically, it is varying shades of the screen color that did not get picked up on the first sample and

should be removed. You remove background noise using the Clean Background Noise button.


From the View Mode menu in the Inspector, select Black.


Above the viewer, click the Alpha Channel/RGB button.

The image displayed changes to a black and white “matte” view of the image.


Click the Clean Background Noise button.


Drag the mouse pointer through these white or light gray regions that should be pure black.

Primatte processes the selection and eliminates the noise.


Repeat this procedure as often as necessary to clear the noise from the background areas.

Selecting Gain/Gamma from the viewer’s Options menu to increase the brightness or gamma

allows you to see noise that would otherwise be invisible.

Primatte viewer Options menu

You do not need to remove every single white pixel to get good results. Most pixels displayed

as a dark color close to black in a key image are considered transparent and virtually allow

the background to be the final output in that area. Consequently, there is no need to eliminate

all noise in the screen portions of the image. In particular, if an attempt is made to remove

noise around the foreground subject meticulously, a smooth composite image is often difficult

to generate.

TIP: When clearing noise from around loose, flying hair or any background/foreground

transitional area, be careful not to select any of the areas near the edge of the hair. Leave

a little noise around the hair as this can be cleaned up later using the Fine Tuning tools.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Clean Foreground Noise

If there are dark regions in the middle of the mostly white foreground subject, the key is not 100% in

those areas. Using Clean Foreground Noise can make the matte as white as possible.


Keep the View Mode menu set to Black and the viewer set to the Alpha Channel.


Click the Clean Foreground Noise button.


Drag the mouse pointer through these dark pixels in the foreground that should be pure white.

Primatte processes the selection and eliminates the noise.


Repeat this procedure as often as necessary to clear the noise from the foreground areas.


If enabled, disable Gain/Gamma from the viewer’s Options menu to return to a regular viewer.

Removing Spill

The first three sections created a clean matte. At this point, the foreground can be composited onto

any background image. However, if there is color spill on the foreground subject, a final operation is

necessary to remove that screen spill for a more natural-looking composite.


From the View Mode menu, select Composite.


Above the viewer, click the Alpha/RGB toggle button to see the RGB image.

There are two ways in Primatte to remove the spill color:

Spill Sponge

The quickest method is to select the Spill Sponge button and then sample the spill areas

away. Additional spill removal can be done using the tools under the Fine Tuning tab or by

using the Spill(-) button.

Fine Tuning Tab

To use the Fine Tuning tab for spill, first scrub over the spill color in the viewer. For most

images, adjusting the Spill slider is all that is required to remove any remaining spill.

NOTE: When using the slider in the Fine Tuning tab to remove spill, spill color replacement is

replaced based on the setting of the Spill Replacement options.

You can use the other two sliders in the same way for different key adjustments. The Detail

slider controls the matte softness for the color that is closest to the background color. For

example, you can recover lost rarefied smoke in the foreground by selecting the Fine Tuning

mode, clicking on the area of the image where the smoke starts to disappear and moving the

Detail slider to the left. The Transparency slider controls the matte softness for the color that

is closest to the foreground color. For example, if you have thick and opaque smoke in the

foreground, you can make it semitransparent by moving the Transparency slider to the right

after selecting the pixels in the Fine Tuning mode.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Relight [RLt]

The Relight node

Relight Node Introduction

Relight allows you to add light sources to your scene, realistically illuminating the objects within it.

Unlike a simple shape node whose polygon is fixed on screen, Relight analyzes the shapes of people

and objects to create a Surface Map and uses that map to reflect light appropriately. When dialed-in

properly, this effect can provide the illusion of light following the curves of an object, reflecting off

highlights and disappearing into shadows.

Relight is useful in situations when you wished you had another light in the scene, want to accentuate

an existing light to match another shot, or want to increase the realism of day-for-night grading.

NOTE: The Relight effect creates the illusion of depth with its analysis of the surfaces in

a scene, but it does not calculate 3D relationships between objects in the scene. Shapes

cannot be made to cast shadows, and depth information cannot be produced.

For more information on Relight, see Chapter 162, “Resolve FX Refine.”

Inputs

The Relight tool has three inputs.

Input: The orange input is used for the primary footage you wish to relight.

Effect Mask: The optional blue effect mask input accepts a mask shape created by polylines,

basic primitive shapes, paint strokes, or bitmaps from other tools. Connecting a mask to this input

limits the filter to only those pixels within the mask. An effects mask is applied to the tool after the

tool is processed.

Normals: The green input is used to connect an externally created normal maps, instead of the one

generated internally by the Relight tool.

Basic Node Setup

In order to use the Relight tool, you need an additional node structure to build around it. In addition to

the standard MediaIn node, you will need a Merge node, and another effect like the ColorCorrector or

Brightness/Contrast tools.

�MediaIn: The output from the MediaIn node goes to the orange inputs of the Relight,

ColorCorrector (or other effect node), and the Merge node.

�ColorCorrector (effect): Receives the input from the MediaIn node, and its output connects to the

green foreground input of the Merge node.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

�Relight: Receives the input from the MediaIn node, and its output connects to the blue effect mask

input on the Merge node. Set this node to appear in the viewer of your choice.

�Merge: Receives the background input from the MediaIn node, receives the green foreground

input from the ColorCorrector, and the blue effect mask input from Relight. Its output goes to the

rest of the node tree or media out. Set this node to appear in the viewer of your choice.

The node tree showing the surrounding node structure for the Relight tool. Note

that the ColorCorrector can be replaced by any other preferred effect.

With the above node structure in place, you should see something similar to the setup

below. On Viewer 1 is the final relight effect that gets passed onto the rest of the node tree.

On Viewer 2 you have the relight interface that allows you to drag the lighting position around

the frame. Depending on your Relighting Map Preview option, this will either be a black and

white embossed image, or the RGB image with a semi-transparent background.

The Merge node in Viewer 1 (left), and the Relight node in Viewer 2 (right);

both sets of on-screen controls are active.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION