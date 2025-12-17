---
title: "Main Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 646
---

# Main Controls

Each of the Small, Medium, and Large Texture sliders can be moved into both negative and positive

values. A value of 0 means no change is made to the corresponding details of the image. Negative

values remove the corresponding details from the image, eventually leaving only the underlying

smooth structure of the image at –1.000. Positive values add sharpness to the corresponding details of

the image, to a maximum value of 1.000.

�Small Texture: Affects extremely fine detail such as skin pores and strands of hair.

�Medium Texture: Impacts coarser detail such as freckles, wrinkles, and clusters of hair.

�Large Texture: Affects the largest details in the image such as eyelids, eyebrows, the edges of lips

and noses, and the edges where hair meets the face.

TIP: What’s identifiable as a small, medium, or large structure depends in large part on

how the subject of the shot is framed. These structures differ depending on whether you’re

grading a subject in a long shot (where they appear small) versus a subject in closeup (where

they appear large).

Adjust Small Skin Texture Granularity

This control lets you adjust the distinction between the Small and Medium/Large texture controls in

the previous group of controls.

�Small Texture Size: Defines the threshold that differentiates Small Textures from Medium and

Large Textures, to help you fine-tune the Small Texture that you want to preserve. Raising this

value includes more of the image as small details, while lowering this value excludes more of the

image from small details.


Resolve FX Overview | Chapter 164 Resolve FX Sharpen

COLOR

Chapter 165

Resolve FX Stylize

The plugins found in this category all enable different ways of creating artistic

modifications to the image.

Contents

Abstraction (Studio Version Only)����������������������� 3577

Main Controls���������������������������������������������������������������� 3577

Quantization Controls����������������������������������������������� 3577

Draw Edge Controls��������������������������������������������������� 3577

Blanking Fill������������������������������������������������������������������� 3577

Source������������������������������������������������������������������������������ 3578

Fill Extent������������������������������������������������������������������������ 3579

Fill Appearance����������������������������������������������������������� 3580

Drop Shadow��������������������������������������������������������������� 3580

Defocus Background����������������������������������������������� 3580

Adjust Mask�������������������������������������������������������������������� 3581

Effects������������������������������������������������������������������������������ 3582

Advanced Options����������������������������������������������������� 3582

Drop Shadow��������������������������������������������������������������� 3582

Edge Detect����������������������������������������������������������������� 3583

Main���������������������������������������������������������������������������������� 3583

Detection����������������������������������������������������������������������� 3583

Filters������������������������������������������������������������������������������� 3584

Advanced Options����������������������������������������������������� 3584

Emboss��������������������������������������������������������������������������� 3585

Channels������������������������������������������������������������������������ 3585

Mirrors����������������������������������������������������������������������������� 3586

Main Controls��������������������������������������������������������������� 3586

Individual Controls���������������������������������������������������� 3586

Rosette Controls��������������������������������������������������������� 3586

Kaleidoscope Controls�������������������������������������������� 3586

Pencil Sketch in DaVinci Resolve

(Studio Version Only)������������������������������������������������� 3587

Prism Blur���������������������������������������������������������������������� 3588

Scanlines������������������������������������������������������������������������ 3588

Appearance������������������������������������������������������������������ 3588

Color��������������������������������������������������������������������������������� 3588

Composite��������������������������������������������������������������������� 3589

Sky Replacement������������������������������������������������������� 3589

Selecting the Sky to be Replaced��������������������� 3590

Selecting the Replacement Sky������������������������� 3590

Sky Mask Adjustments���������������������������������������������� 3591

Source Sky Appearance������������������������������������������� 3591

Artificial Sky�������������������������������������������������������������������� 3591

Sky Position������������������������������������������������������������������� 3592

Sky Integration������������������������������������������������������������� 3593

Foreground Appearance����������������������������������������� 3593

Sky Replacement Workflow����������������������������������� 3593

Stylize (Studio Version Only)��������������������������������� 3596

Tilt-Shift Blur (Studio Version Only)�������������������� 3597

Main Controls���������������������������������������������������������������� 3597

Lens Iris���������������������������������������������������������������������������� 3597

Depth of Field��������������������������������������������������������������� 3597

Watercolor (Studio Version Only)����������������������� 3598


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Abstraction (Studio Version Only)

A deceptively powerful filter that lets you create a wide range of cartoon-like renders by simplifying an

image into adjustable pools of similar color with optional outlines.

Main Controls

These controls create the foundation of this effect.

�Pre Blur: Simplifies the image by blurring unwanted details prior to this filter taking effect.

�Abstraction Strength and Iterate Abstraction: These parameters work together to then smooth

the image, creating pools of simplified color within the details of the image.

Abstraction Strength: Must be higher than 0 for the Iteration No. parameter to have an effect.

Higher Abstraction Strength simplifies image detail even more by averaging adjacent regions of

color together.

Iterate Abstraction: Reduces the amount of small detail in the image even further by “widening”

adjacent areas of similar color to blend together as one.

Quantization Controls

These controls simplify the pools of color even more aggressively by quantizing the bit depth used to

stylize the image. The result is an even sharper flattening of each region of color.

�Quantization: A checkbox turns this function on.

�Steps: Raising this parameter lets you subdivide each region of color into a greater number of

separate regions.

�Softness: Lets you blur the border between each level of color.

Draw Edge Controls

Adds an edge to the regions of color created by this effect.

�Draw Edge: Enables edge drawing.

�Edge Strength: Raising this value results in thicker and better-defined edges.

�Edge Detection Threshold: Raising this value restricts edges to only the boldest edge

details in the picture.

Blanking Fill

This plugin is specifically designed to quickly fill black frame blanking with a stylized image derived

from the clip itself, to make blanking less intrusive for viewers in documentaries and news segments.

In the following example, the Blanking Fill plugin is used to add image to the left and right of

“pillarboxed” standard definition 4:3 video that appears within a High Definition or Ultra High Definition

16:9 aspect ratio.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

(Top) Original standard definition image (Bottom) Image with default Blanking Fill applied

A variety of controls let you easily customize this effect to suit your own purposes.

Source

These controls let you transform the clip in different ways, which also affects how that clip is used to fill

the blanking area.

�Zoom: Zooms the clip while keeping it within the native domain of definition. Good for quickly

cropping unwanted pixels around the edges so they’re hidden and aren’t used for blanking fill.

�Crop Left and Right: Crops both the left and right edges of the image and increases the area at

the sides with blanking fill.

�Same Left/Right Sliders: On by default, locks both sliders together so moving one moves the

other by a mirrored amount.

�Crop Top and Bottom: Crops both the top and bottom edges of the image and increases the

vertical area with blanking fill.

�Same Top/Bottom Sliders: On by default, locks both sliders together so moving one moves the

other by a mirrored amount.

�Center: If checked, re-centers the image area if a sizing operation has offset it.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Fill Extent

These controls let you choose how the current duplicate of the image is stretched to fill the

blanking area.

�Zoom Mode: There are three options:

Stretch to Timeline: Automatically warps the image to stretch it to fit the full frame. Keeps features

in the blanking fill area level with where they appear in the original image.

Zoom to Timeline: Automatically zooms into the image to fit the full frame. Results in the clip

looking “inset” from the blanking fill image.

Manual: Reveals Expand and Aspect sliders that let you manually choose how much to zoom and

stretch the image to fit the blanking fill area.

�Warp Top Layer: lets you use onscreen controls to choose a section of the edge of an image to

stretch out to fill blanking in the frame. In this mode, there are two sets of onscreen controls you

can use to customize the result:

A set of outer handles let you choose how far out to warp the edges of the image to fill whatever

blanking there is. These default to the project frame size.

A set of inner handles lets you choose how much of the image you want to stretch out. These

default to the current title safe boundary. If you customize these, choosing too narrow an edge

results in a more extreme warping and stretching effect, while choosing a wider edge to stretch

looks more natural, but affects more of the frame.

�Expand: (Only appears when Zoom Mode is set to Manual) Zooms the image.

�Aspect: (Only appears when Zoom Mode is set to Manual) Stretches the image.

The original 4:3 image edited into a 16:9 timeline with black

pillar boxing to the left and right as a result

The image with Blanking Fill set to Warp Top Layer,

stretching the left and right edges to fill the blanking area


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR