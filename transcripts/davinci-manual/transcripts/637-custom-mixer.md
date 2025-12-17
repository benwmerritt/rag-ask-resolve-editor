---
title: "Custom Mixer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 637
---

# Custom Mixer

The Custom Mixer is an advanced version of the Layer node. It takes two inputs and combines them

based on the Alpha channel of the second input. The Custom Mixer has controls to mix sources,

blend effects, and interpolate between grades with per-channel control and mixing options. You can

use this tool in a variety of ways to control the relative intensity between the sources, or simply as an

alternative to the Layer Node but with slider controls.

The Custom Mixer should be added directly to the node graph and not dragged on top of a Corrector

node. To add the Custom Mixer to your Node Graph, drag the Custom Mixer icon from the Resolve

FX Refine section of the Effects library, directly into the Node Graph. You can also drag it on top of an

existing link in the Node Graph to place it inline.

The Custom Mixer node is connected in the following way. The first and second RGB (Green) inputs

are input 1 and input 2 respectively. The alpha of the second input controls the blend of input 2 onto

input 1. The Alpha of the 1st input does not affect the result; it is passed through the node to the

output key.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

The Custom Mixer Node connections: Input 1 (Green triangle above), and

Input 2 (Green triangle below). The alpha from Input 2 controls the blend

of Input 2 onto Input 1 and is what you modify in the Custom Mixer controls.

The Custom Mixer has two main modes chosen by the Mix mode; both have the same behavior, just

different controls to change how the input affects the output.

Blend

Blends the second input onto the first input. The normal range is from 0 (fully input 1) to 1 (fully input 2),

however you can set the blend factor up to 10 times more or less by typing the numbers directly into

the fields. This allows you to enhance the difference between inputs beyond the appearance of either

one alone. All the sliders can be keyframed independently.

�Blend Input 2 onto 1: Controls the strength of each source, based on the color channels of

the selected color space (RGB, YUV, XYZ, etc.). These can be adjusted separately if the Gang

checkbox is unchecked.

�Gang: Check this box to gang the channels of the custom mixer together, or uncheck to

adjust separately.

Combine

Combines the inputs together, allowing you to change the relative strength of each input’s contribution

to the mix. The normal range is from 0 (fully input 1) to 1 (fully input 2), however you can set the blend

factor up to 10 times more or less by typing the numbers directly into the fields. This allows you to

enhance the difference between inputs beyond the appearance of either one alone. All the sliders can

be keyframed independently.

�Input 1 Contribution: Controls the strength of input 1’s source, based on the color channels of

the selected color space (RGB, YUV, XYZ, etc.). These can be adjusted separately if the Gang

checkbox is unchecked.

�Input 2 Contribution: Controls the strength of input 2’s source, based on the color channels of

the selected color space (RGB, YUV, XYZ, etc.). These can be adjusted separately if the Gang

checkbox is unchecked.

�Offset: Controls the offset of the combination, based on the color channels of the selected

color space (RGB, YUV, XYZ, etc.). These can be adjusted separately if the Gang checkbox

is unchecked.

�Gang: Check this box to gang the channels of the custom mixer together, or uncheck to

adjust separately.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

Advanced Options

Sets the composite type, as well as the color space and gamma of the resulting mix.

�Composite Type: Sets the composite type used for the mixer from the drop-down menu.

�Color Space: Sets the Color Space used for the blend. The default is the current

Timeline color space.

�Gamma: Sets the Gamma used for the blend. The default is the current Timeline color space.

The initial setup of the Custom Mixer, Node 1 is the original image,

Node 2 is identical but with a Noise Reduction effect applied to it.

The final setup of the Custom Mixer, by extending the blend factor by 7,

the mixer actually adds noise to the image instead.

For the example above, by applying the Noise Reduction FX to Node 2, and directly

connecting the same image from Node 1 to the Custom Mixer, the only difference between

the inputs is the noise pattern from the effect itself. By manually turning the blend up past 1,

you are blending in more of the noise than you started with. So by using Noise Reduction in

conjunction with the Custom Mixer, you can actually add additional noise to an image that

perfectly matches the original grain pattern without having to find a similar external grain or

noise source.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

Depth Map (Studio Version Only)

NOTE: The Depth Map Resolve FX has been considerably improved under the hood and

updated from DaVinci Resolve 20 and above. While the interface and usage remains the

same as the original, you should get significantly more precise results from the tool. The new

Depth Map v2 has replaced the original and is applied automatically when using the Depth

Map effect.

Depth Map creates an Alpha channel based on the perceived distance of objects in your clip. By being

able to isolate a specific depth region, the opportunities to manipulate the resulting image are greatly

expanded. For example, combined with a Fast-Noise plugin you could simulate a fog effect, but

confined only to the distant background of your shot. You could enhance a foreground object like a

person, increasing contrast, saturation, and sharpness, similar to using a qualifier. You can use a Depth

Map to fix video issues, for example fixing a color temperature problem by isolating a far window that

was shot in daylight causing background actors to be tinted blue, while leaving the foreground subject

that was shot with studio lighting unaffected. Depth Map can also be combined with DaVinci Resolve’s

other windows and keying tools to form more complex rotoscoping and keys with less effort.

The resulting Depth Map Alpha channel is visualized as a black and white image, with white being the

area that is affected by the resulting changes and black areas remaining unchanged.

(Top) The original image  (Bottom) The Depth Map v2 analysis of the scene;

white for areas “closer” to the camera and black for areas farther away


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

Main Controls

These controls set the main parameters of the Depth Map.

�Quality: Depth Map is a very computationally intensive effect. The quality setting allows a Faster

mode to speed up the responsiveness to adjustments, while the default Better mode gives the

best results and should be turned on when the adjustments are finished.

�Depth Map Preview: By default this box is checked, and shows you the current Depth Map for

making adjustments. When this check box is disabled, the resulting alpha can then be used for

grading on other nodes. If you applied the effect to a corrector node, make sure to right click on

the Depth Map’s node and select “Use OFX Alpha” to have the node correctly pass the effect’s

Alpha channel.

�Invert: Checking this box reverses the Depth Map, switching its transparent and opaque regions.

Resulting Map Adjustment

These controls let you determine how the Depth Map’s contrast is adjusted.

�Adjust Map Levels: When deselected (default), you can use DaVinci Resolve’s grading tools

(lift, gamma, gain, etc.) to adjust the full range of the Depth Map. When enabled, this option clips

the Depth Map’s levels to 0 and 1. This functions as a preview of what will happen to the Depth Map

when used as an Alpha channel where the values are always clipped to 0 and 1 by DaVinci Resolve.

�Far Limit: This control adjusts the black levels of the Depth Map.

�Near Limit: This control adjusts the white levels of the Depth Map.

�Gamma: This control adjusts the intermediate depth values to be brighter or dimmer compared to

the fixed black and white levels.

Isolate Specific Depth

These controls allow you to sweep backwards and forwards in the scene by depth, allowing you to

isolate a specific depth range to adjust.

�Isolation: This checkbox turns the depth isolation tools on or off.

�Target Depth: This controls the specific depth you want to isolate. 1 is fully in the foreground,

while 0 is fully in the background.

�Tolerance: Sets the range to either side of the Target Depth to include in the Depth Map.

�Softness: This sets a subtle ramp-in and ramp-out of the selected range, giving it a more

organic selection.

Map Finesse

These controls modify the resulting Depth Map’s Alpha channel for use in grading.

�Post Processing: This control turns the Map Finesse tools on or off.

�Post Filter: Smooths the depth map along image contours.

�Contract/Expand: This control dilates or erodes the overall shape at the edges, useful for fine

tuning the boundary between the affected and unaffected regions of the map.

�Blur: This control softens the boundary of the map, allowing it to blend more smoothly into the

resulting image.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR