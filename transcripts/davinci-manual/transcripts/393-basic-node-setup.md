---
title: "Basic Node Setup"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 393
---

# Basic Node Setup

Merge nodes are typically connected in the following way, with two input images connected to the

background and foreground inputs, and the output connected to the next node in the composition. In

this example, the effect mask input is not used, as this is not typical.

A typical Merge node structure in DaVinci Resolve

Resolution Handling

While you can connect images of any resolution to the background and foreground inputs of the

Merge node, the image that’s connected to the background input determines the resolution of

the output.

TIP: If you want to change the resolution of the image connected to the background, you can

use the Crop node to change the “canvas” resolution of the image without changing the size

of the original image, or you can use the Resize node to change both the resolution and the

size of the image.

Inspector

Merge node controls


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Merge Tab

The Merge tab contains most of the controls necessary for customizing most merge operations.

Foreground Sizing Controls

These controls let you adjust the sizing of the image connected to the foreground input, making it

unnecessary to use a separate Transform node to fit the foreground layer to match the background

layer in simple compositions.

�Center X and Y: This control determines the position of the foreground image in the composite.

The default is 0.5, 0.5, which centers the foreground image in the exact center of the background

image. The value shown is always the actual position in normalized coordinates, multiplied by the

reference size. See below for a description of the reference size controls.

�Size: Use this control to increase or decrease the size of the foreground image before it is

composited over the background. The range of values for this slider is 0.0 to 5.0, but any value

greater than 0 can be entered manually. A size of 1.0 gives a pixel-for-pixel composition, where a

single pixel in the foreground is the same size as a single pixel in the background.

�Angle: Use this control to rotate the foreground image before it is combined with the background.

Compositing Mode and Adjustment Controls

The next six parameters control how the background and foreground input images are combined to

create a single output image.

�Apply Modes: The Apply Mode setting determines the math used when blending or combining

the foreground and background pixels.

Normal: The default Normal merge mode uses the foreground’s Alpha channel as a mask to

determine which pixels are transparent and which are not. When this is active, another menu

shows possible operations, including Over, In, Held Out, Atop, and XOr.

Screen: Screen merges the images based on a multiplication of their color values. The Alpha

channel is ignored, and layer order becomes irrelevant. The resulting color is always lighter.

Screening with black leaves the color unchanged, whereas screening with white will always

produce white. This effect creates a similar look to projecting several film frames onto the same

surface. When this is active, another menu shows possible operations, including Over, In, Held

Out, Atop, and XOr.

Dissolve: Dissolve mixes two image sequences together. It uses a calculated average of the two

images to perform the mixture.

Darken: Darken looks at the color information in each channel and selects the background or

foreground image’s color value, whichever is darker, as the result color. Pixels lighter than the

merged colors are replaced, and pixels darker than the merged color do not change.

Multiply: Multiplies the values of a color channel. This will give the appearance of darkening the

image as the values are scaled from 0 to 1. White has a value of 1, so the result would be the same.

Gray has a value of 0.5, so the result would be a darker image, or an image half as bright.

Color Burn: Color Burn uses the foreground’s color values to darken the background image. This

is similar to the photographic dark room technique of burning by increasing the exposure of an

area of a print.

Linear Burn: Linear Burn decreases the brightness of the base color based on the value of the

blend color. The result is darker than Multiply but less saturated than Color Burn. Linear Burn

also produces the most contrast in darker colors than any of the other blending modes in the

Darker group.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Darker Color: The Darker Color blending mode is very similar to Darken. This blending mode

does not blend pixels. It only compares the base and blend colors, and it keeps the darkest of the

two. The difference is that Darker Color looks at the composite of all the RGB channels, whereas

Darken looks at each RGB channel individually to come up with a final blend.

Lighten: Lighten looks at the color information in each channel and selects the background or

foreground image’s color values, whichever is lighter, as the result color value. Pixels darker than

the merged color are replaced, and pixels lighter than the merged color do not change.

Color Dodge: Color Dodge uses the foreground’s color values to brighten the background image.

This is similar to the photographic dark room technique of dodging by reducing the exposure of an

area of a print.

Linear Dodge: Linear Dodge (Add) produces similar but stronger results than Screen or Color

Dodge. This blending mode looks at the color information in each channel and brightens the base

color to reflect the blend color by increasing the brightness. Blending with black produces no

change. Linear Dodge (Add) blends differently when Fill Opacity is adjusted, compared to when

Opacity is adjusted.

Lighter Color: Lighter Color is very similar to Lighten. This blending mode does not blend pixels. It

only compares the base and blend colors, and it keeps the brightest of the two. The difference is

that Lighter Color looks at the composite of all the RGB channels, whereas Lighten looks at each

RGB channel to come up with a final blend.

Overlay: Overlay multiplies or screens the color values of the foreground image, depending

on the color values of the background image. Patterns or colors overlay the existing pixels

while preserving the highlights and shadows of the color values of the background image. The

background image is not replaced but is mixed with the foreground image to reflect the original

lightness or darkness of the background image.

Soft Light: Soft Light darkens or lightens the foreground image, depending on the color values of

the background image. The effect is similar to shining a diffused spotlight on the image.

Hard Light: Hard Light multiplies or screens the color values of the foreground image, depending

on the color values of the background image. The effect is similar to shining a harsh spotlight on

the image.

Vivid Light: Vivid Light is an extreme version of Overlay and Soft Light. Anything darker than

50% gray is darkened, and anything lighter than 50% gray is lightened. Vivid Light is one of those

blending modes where you may want to adjust the opacity, since 100% opacity is generally too

strong. Vivid Light is the fifth blending mode of eight that give you different results when you

reduce the fill compared to opacity.

Linear Light: Linear Light uses a combination of the Linear Dodge blending on lighter pixels and a

Linear Burn on darker pixels. Typically, the resulting colors are extreme, and you may want to use

the Opacity or Fill sliders to adjust it. Linear Lights blends differently when Fill Opacity is adjusted,

compared to when Opacity is adjusted.

Pin Light: Pin Light is an extreme blending mode that performs a Darken and Lighten blending

mode simultaneously. It can result in patches or blotches, and it completely removes all mid-tones.

Difference: Difference looks at the color information in each channel and subtracts the foreground

color values from the background color values or the background from the foreground, depending

on which has the greater brightness value. Merging with white inverts the color. Merging with

black produces no change.

Exclusion: Exclusion creates an effect similar to, but lower in contrast than, the Difference mode.

Merging with white inverts the base color values. Merging with black produces no change.

Hue: Hue creates a result color with the luminance and saturation of the background color values

and the hue of the foreground color values.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Saturation: Saturation creates a result color with the luminance and hue of the base color and the

saturation of the blend color.

Color: Color creates a result color with the luminance of the background color value and the hue

and saturation of the foreground. This preserves the gray levels in the image and is useful for

coloring monochrome images.

Luminosity: Luminosity creates a result color with the hue and saturation of the background color

values and the luminance of the foreground color values. This mode creates an inverse effect from

that of the Color mode.

Hypotenuse: This blend mode is good for HDR images that have out of range colors above 1, It

uses a square root of each color squared and added to blend the color.

Out = sqrt (Fc*Fc +Bc*Bc)

Geometric: This blend mode is good for HDR images that have out of range colors above 1, For

values above zero the result is 2 times the foreground times the background color divided by the

foreground plus background color.

Out = 2*Fc*Bc / (Fc+Bc)

�Operator Modes: This menu is used to select the Operation mode of the merge. Changing

the Operation mode changes how the foreground and background are combined to produce

a result. This pop-up menu is visible only when the Merge node’s Apply mode is set to either

Normal or Screen.

For an excellent description of the math underlying the Operation modes, read Compositing

Digital Images, Porter, Thomas, and T. Duff, ACM SIGGRAPH Computer Graphics proceedings,

1984, pages 253-259. Essentially, the math is as described below. Note that some modes not

listed in the Operator drop-down menu (Under, In, Held In, Below) are easily obtained by swapping

the foreground and background inputs (with Command-T or Ctrl-T) and choosing a corresponding

mode. The formula used to combine pixels in the merge is always (fg * x) + (bg * y). The different

operations determine exactly what x and y are, as shown in the description for each mode.

The Operator modes are as follows:

Over: The Over mode adds the foreground layer to the background layer by replacing the pixels

in the background with the pixels from the Z wherever the foreground’s Alpha channel is greater

than 1.

x = 1, y = 1-[foreground Alpha]

In: The In mode multiplies the Alpha channel of the background input against the pixels in

the foreground. The color channels of the foreground input are ignored. Only pixels from the

foreground are seen in the final output. This essentially clips the foreground using the mask from

the background.

x = [background Alpha], y = 0

Held Out: Held Out is essentially the opposite of the In operation. The pixels in the foreground

image are multiplied against the inverted Alpha channel of the background image. Accomplish

exactly the same result using the In operation and a Matte Control node to invert the matte

channel of the background image.

x = 1-[background Alpha], y = 0

Atop: Atop places the foreground over the background only where the background has a matte.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

x = [background Alpha], y = 1-[foreground Alpha]

XOr: XOr combines the foreground with the background wherever either the foreground or the

background has a matte, but never where both have a matte.

x = 1-[background Alpha], y = 1-[foreground Alpha]

Conjoint: The Conjoint mode will make a decision based combination of Alpha channels of the

foreground and background images; this is helpful in soft edge and motion blurred Alpha where

Alpha is not solid.

X= 1, Y= X+Y(1-af)/ab, if af>ab

Disjoint: The Disjoint mode will make a decision based combination of Alpha channels of the

foreground and background images; this is helpful in combining layers as to not get out of range

Alpha, and premultiplied edges get the correct Alpha combination.

X= X+Y(1-af)/ab, Y= X+Y if af+ab<1

Mask: The Mask mode will output the background image multiplied by the foreground Alpha.

X = X * af, Y =0

Stencil: The Stencil mode will output the background image multiplied by the inverse

foreground Alpha.

X = X * (1-af), Y =0

Under: The Under mode is the same operation as the Over mode but will swap foreground and

background images in the operations.

X = Y, Y =X *(1-af)

�Subtractive/Additive slider: This slider controls whether Fusion performs an Additive merge, a

Subtractive merge, or a blend of both. This slider defaults to Additive merging for most operations,

assuming the input images are premultiplied (which is usually the case). If you don’t understand

the difference between Additive and Subtractive merging, here’s a quick explanation.

�An Additive merge is necessary when the foreground image is premultiplied, meaning that the

pixels in the color channels have been multiplied by the pixels in the Alpha channel. The result is

that transparent pixels are always black, since any number multiplied by 0 always equals 0. This

obscures the background (by multiplying with the inverse of the foreground Alpha), and then

simply adds the pixels from the foreground.

�A Subtractive merge is necessary if the foreground image is not pre-multiplied. The compositing

method is similar to an additive merge, but the foreground image is first multiplied by its own

Alpha to eliminate any background pixels outside the Alpha area.

While the Additive/Subtractive option could easily have been a checkbox to select one mode or

another, the Merge node lets you blend between the Additive and Subtractive versions of the

merge operation—an operation that is occasionally useful for dealing with problem composites

with edges that are calling attention to themselves as too bright or too dark.

For example, using Subtractive merging on a premultiplied image may lead to darker edges, whereas

using Additive merging with a non-premultiplied image will cause any non-black area outside the

foreground’s Alpha to be added to the result, thereby lightening the edges. By blending between

Additive and Subtractive, you can tweak the edge brightness to be just right for your situation.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

�Alpha Gain slider: Alpha Gain linearly scales the values of the foreground’s Alpha channel. In

Subtractive merges, this controls the density of the composite, similarly to Blend. In Additive

merges, this effectively reduces the amount that the background is obscured, thus brightening the

overall result. In an Additive merge with Alpha Gain set to 0.0, the foreground pixels are simply

added to the background.

�Burn In slider: The Burn In control adjusts the amount of Alpha used to darken the background,

without affecting the amount of foreground added in. At 0.0, the merge behaves like a straight

Alpha blend, whereas at 1.0, the foreground is effectively added onto the background (after Alpha

multiplication if in Subtractive mode). This gives the effect of the foreground image brightening

the background image, as with Alpha Gain. For Additive merges, increasing the Burn In gives an

identical result to decreasing Alpha Gain.

�Blend slider: This is a cloned instance of the Blend slider in the Common Controls tab. Changes

made to this control are simultaneously made to the one in the common controls. The Blend slider

mixes the result of the node with its input, blending back the effect at any value less than 1.0. In

this case, it will blend the background with the merged result.

Additional Controls

The remaining controls let you fine-tune the results of the above settings.

�Filter Method: For input images that are being resized, this setting lets you choose the filter

method used to interpolate image pixels when resizing clips. The default setting is Linear. Different

settings work better for different kinds of resizing. Most of these filters are useful only when

making an image larger. When shrinking images, it is common to use the Linear filter; however,

the Catmull-Rom filter will apply some sharpening to the results and may be useful for preserving

detail when scaling down an image.

Nearest Neighbor: This skips or duplicates pixels as needed. This produces the fastest but

crudest results.

Box: This is a simple interpolation resize of the image.

Linear: This uses a simplistic filter, which produces relatively clean and fast results.

Quadratic: This filter produces a nominal result. It offers a good compromise between

speed and quality.

Cubic: This produces better results with continuous-tone images. If the images have fine detail in

them, the results may be blurrier than desired.

Catmull-Rom: This produces good results with continuous-tone images that are resized down.

Produces sharp results with finely detailed images.

Gaussian: This is very similar in speed and quality to Bi-Cubic.

Mitchell: This is similar to Catmull-Rom but produces better results with finely detailed images. It is

slower than Catmull-Rom.

Lanczos: This is very similar to Mitchell and Catmull-Rom but is a little cleaner and also slower.

Sinc: This is an advanced filter that produces very sharp, detailed results; however, it may produce

visible “ringing” in some situations.

Bessel: This is similar to the Sinc filter but may be slightly faster.

Window Method: Some filters, such as Sinc and Bessel, require an infinite number of pixels to

calculate exactly. To speed up this operation, a windowing function is used to approximate the

filter and limit the number of pixels required. This control appears when a filter that requires

windowing is selected.

Hanning: This is a simple tapered window.

Hamming: Hamming is a slightly tweaked version of Hanning.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Blackman: A window with a more sharply tapered falloff.

Kaiser: A more complex window, with results between Hamming and Blackman.

Resize Filters from left to right: Nearest Neighbor, Box, Linear, Quadratic, Cubic,

Catmull-Rom, Gaussian, Mitchell, Lanczos, Sinc, and Bessel

�Edges Buttons: Four buttons let you choose how to handle the space around images that are

smaller than the current DoD of the canvas as defined by the resolution of the background image.

Canvas: The area outside the frame is set to the current color/opacity of the canvas. If you want to

change this value, you can attach a Set Canvas Color node between the image connected to the

foreground input and the foreground input itself, using Set Canvas Color to choose a color and/or

transparency setting with which to fill the canvas.

Wrap: Creates a “video wall” effect by duplicating the foreground image as a grid.

Duplicate: Duplicates the outermost pixels along the edge of the foreground image, duplicating

them to stretch up, down, left, and right from each side to reach the end of the DoD.

Mirror: Similar to duplicate, except every other iteration of the foreground image is flipped and

flopped to create a repeating pattern.

�Invert Transform: Select the Invert Transform control to invert any position, rotation, or scaling

transformation. This option is useful when connecting the merge to the position of a tracker for

match moving.

�Flatten Transform: The Flatten Transform option prevents this node from concatenating its

transformation with subsequent nodes. The node may still concatenate transforms from its input,

but it will not concatenate its transformation with the node at its output.

�Reference Size: The controls under Reference Size do not directly affect the image. Instead, they

allow you to control how Fusion represents the position of the Merge node’s center.

Normally, coordinates are represented as values between 0 and 1, where 1 is a distance equal to

the full width or height of the image. This allows resolution independence, because the size of the

image can be changed without having to change the value of the center.

One disadvantage to this approach is that it complicates making pixel-accurate adjustments to an

image. To demonstrate, imagine an image that is 100 x 100 pixels in size. To move the center of

the foreground element to the right by 5 pixels, we would change the X value of the merge center

from 0.5, 0.5 to 0.55, 0.5. We know the change must be 0.05 because 5/100 = 0.05.

If you specify the dimensions of the background image in the Reference Size controls, this

changes the way the center control values are displayed so that it shows the actual pixel positions

in its X and Y fields.

Extending the example, set the width and height to 100 each and the center will now be shown as

50, 50, and we would move it 5 pixels toward the right by entering 55, 50.

Internally, the Merge node still stores this value as a number between 0 to 1 and, if the center

control’s value was to be queried via scripting or the center control was to be published for use

by other nodes, the original normalized value would be retrieved. The change is only visible in the

value shown for merge center in the node control.

Use Frame Format Settings: Select this to force the merge to use the composition’s current frame

format settings to set the reference width and reference height values.

Width and Height: Set these sliders to the width and height of the image to change the way that

Fusion displays the values of the Merge node’s center control.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION

Channels Tab

Merge node Channels tab

The Channels tab has controls that let the Merge node use Z-channels embedded within each image

to define what’s in front and what’s behind during a Merge operation. The following controls let you

customize the result.

�Perform Depth Merge: Off by default. When turned on, the Z-channel of both images will be used

to determine the composite order. Alpha channels are still used to define transparency, but the

values of the Z-Depth channels will determine the ordering of image elements, front to back. If a

Z-channel is not available for either image, the setting of this checkbox will be ignored, and no

depth compositing will take place. If Z-Depth channels are available, turning this checkbox off

disables their use within this operation.

�Foreground Z-Offset: This slider sets an offset applied to the foreground image’s Z value. Click

the Pick button to pick a value from a displayed image’s Z-channel, or enter a value using the slider

or input boxes. Raising the value causes the foreground image’s Z-channel to be offset further

away along the Z-axis, whereas lowering the value causes the foreground to move closer.

�Subtractive/Additive: When Z-compositing, it is possible for image pixels from the background to

be composited in the foreground of the output because the Z-buffer for that pixel is closer than the

Z of the foreground pixel. This slider controls whether these pixels are merged in an Additive or a

Subtractive mode, in exactly the same way as the comparable slider in the Merge tab.

When merged over a background of a different color, the original background will still be visible

in the semitransparent areas. An Additive merge will maintain the transparencies of the image but

will add their values to the background.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in both the Dissolve and Merge nodes. These

common controls are described in the following “The Common Controls” section.


Fusion Page Effects | Chapter 95 Composite Nodes

FUSION