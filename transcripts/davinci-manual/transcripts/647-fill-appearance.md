---
title: "Fill Appearance"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 647
---

# Fill Appearance

These controls let you change the look of the image being used to fill the blanking area.

�Blend Edges: Lets you feather the edges where the original image meets the blanking fill area.

�Blur Background: Lets you choose how much or how little to blur the image that fills the

blanking fill area.

�Fade Amount: Lets you fade or tint the blanking fill area. At 0, there’s no fade applied. At 1.000,

the blanking area is filled with a solid color defined by the Fade Color control.

�Fade Color: A color picker/eyedropper combination that lets you choose a color with which to

fade, tint, or fill the blanking fill area.

Drop Shadow

These controls let you add a drop shadow to “lift” the foreground image against the blanking fill image.

�Shadow Strength: Lets you choose how solid the drop shadow appears.

�Drop Angle: Lets you choose the angle the drop shadow appears at. At 0 the

drop shadow is centered.

�Drop Distance: Offsets the drop shadow farther in the direction of the Drop Angle

�Blur: Softens the drop shadow.

�Color: Tints the drop shadow.

Defocus Background

The Defocus Background effect lets you blur only the background of an image and provides a detailed

set of tools to mimic shooting with a shallow depth of field.

The original image with a busy, distracting background


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Using the Defocus Background effect to blur the background, making

it less distracting and mimicking a shallower depth of field

The Defocus Background effect does not qualify or isolate the foreground subject. In order to use

the Defocus Background, you must first isolate the foreground subject using an effect or mask using

another tool like Magic Mask or a Power Window. You can then apply Defocus Background either to

the same node or connect the key output from a previous node.

Connecting the key output of the Magic Mask to the Defocus

Background effect; Defocus Background requires a key generated

from another tool like Magic Mask or a Power Window to work.

Adjust Mask

These controls let you adjust the mask that separates the sharply focused areas from the areas you

want to blur.

�Mask Preview: Checking this box will bring up a black and white preview of your mask. The white

areas of the mask will stay sharp, while black areas of the mask are what will be blurred using

the mask controls below. This is convenient to have up while you’re perfecting the mask, then

disabled to see the output of the Effects and Advanced options.

�Mask Invert: Checking this box will invert the mask, making the white areas black and vice-versa.

�Mask Blur: This control adjusts the size of the Blur around the mask, letting you smoothly blend

the foreground and background together.

�Mask Contrast: This controls how strong the divide is between the focused and blurred

regions of the matte.

�Adjust Pivot: This allows you to set where the divide is between the focused and blurred regions

of the matte.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

The Mask Preview option shows where the

defocus operations will take place (black areas).

Effects

These controls set the main characteristics of the blurred area.

�Blur: This slider controls the size and how much blur to apply to the blurred area.

�Saturation: This slider controls the saturation of the blurred area. 1.000 (default) is

full saturation. A value of 0.000 makes the blurred areas monochrome.

�Colorize: This slider controls the amount of color to tint the blurred areas. 0.000 is the default

(no colorization).

�Color: This is the color picker for the Colorize operation above.

Advanced Options

These controls let you adjust some of the physical characteristics of the blurred area.

�Blur Type: This lets you choose the blurring algorithm used to make the blur. Either Lens blur or

Gaussian blur are options.

�Anamorphism (Lens Blur): This slider lets you set the aspect ratio of the blur to match different

lens types.

�Highlights (Lens Blur): Lets you adjust how the highlights of the image affect the blur, dilating or

eroding the image.

Drop Shadow

Lets you add a simple drop shadow to any clip, using that clip’s native or generated alpha channel to

create the shape of the shadow.

�Shadow Strength: Lets you choose how solid the drop shadow appears.

�Drop Angle: Lets you choose the angle the drop shadow appears at. At 0 the drop

shadow is centered.

�Drop Distance: Offsets the drop shadow farther in the direction of the Drop Angle

�Blur: Softens the drop shadow.

�Color: Tints the drop shadow.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Edge Detect

An edge detection effect that isolates high-contrast boundaries with options for customizing which

edges create outlines. With the edges isolated, this allows you to sharpen soft clips or to create a glow

around a subject.

(Top) Original image, (Bottom) Image with default edge detect applied

Main

�Mode: Lets you choose between RGB and Grayscale edges. RGB is the default. RGB finds

edges based on color and brightness, while Grayscale detects edges based solely on

brightness changes.

�Edge color: (only enabled if Mode is set to Grayscale) Lets you colorize the edge outlines

that are generated.

Detection

These controls determine the strength and parameters of the detected edges.

�Edge Width: Lets you set the thickness of the resulting edges.

�Brightness: Lets you set how bright you want the edges to be.

�Gamma: Applies a gamma curve to the edge detection. A gamma below one adds brightness to

mid-strength edges, making more edges “detected,” while a gamma above one darkens mid-

strength edges, reducing the edges to all but the strongest detected.

�Blur: Softens the final result, allowing the edges to blend in more naturally.

�Edge Mask Overlay: This checkbox overlays the edges on top of the current frame to observe the

filter’s results. Unchecking this box shows only the detected edges.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Filters

These controls determine how the edges are blended with the original frame.

�Preprocess: Lets you choose which method of de-noising filtering to use. The default is None.

Filter: Reduces texture and filters out detail at the chosen Scale parameter below.

Flatten: Flattens smooth areas of the image, leaving edges only where they divide between other

flat regions in the image. The Strength parameter below controls the amount of this smoothing.

�Half-Edges Only: Edges are detected between regions of different brightness. This option

lets you determine which side of the edge to keep. The default is None (both sides of the

edge are kept).

Keep Light Side: Edge selects only the brighter half of the edge. Useful, for example, in creating a

light-wrap effect on a person’s face as only the lighter (face side) of the edge is selected, limiting

the increased brightness of the light wrap to the face only and not the background. The Half-

Edge Gain slider allows you to further boost the brightness of the edge, separately from the main

Brightness control.

Keep Dark Side: Edge selects only the darker half of the edge. Useful, for example, in creating

a glow effect on a person’s face as only the darker (background side) of the edge is selected,

allowing a halo to form around the face, but not on it. The Half-Edge Gain slider allows you to

further boost the brightness of the edge, separately from the main Brightness control.

Advanced Options

These controls allow you to select some advanced parameters for the effect.

�Normalize Per Frame: Performs a brightness adjustment on each incoming frame to a consistent

level, causing edges to remain visible as the scene changes brightness or flickers. Use this

setting if your scene has content that has constant changes in brightness levels, otherwise

uncheck this box.

�Clamp Brightness: Keeps the output edges from becoming too bright if the contrast of the content

is too high.

For example, if you wanted to make a slight glow

around the woman in the frame below using edge detect:

•	 Select RGB Edges, Check the Edge Mask Overlay box, and adjust the Blur to about .5 to

blend them into the frame subtly.

•	 Next select Flatten from the Preprocess control to smooth out the fine details in the image,

ensuring that only the highlights from the woman’s hat, arm, and phone are detected, as

well as the bright fluorescent light on the wall. These are what we want to “glow.” Adjust the

Strength slider to taste.

•	 Then select “Keep Dark Side” in the Half-Edges Only box. This ensures that the glow

radiates out from the edges and not onto the woman and the light. Adjust the Half-Edge

Gain slider to taste.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

The shot before the Edge effect

The Edge Detect effect only on the same image with the parameters described above

The Edge Detect result; notice the glow coming from the light

and around the woman’s hat, arm, and phone.