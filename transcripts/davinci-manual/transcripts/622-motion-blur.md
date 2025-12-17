---
title: "Motion Blur"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 622
---

# Motion Blur

Motion Blur settings use optical-flow based motion estimation to add artificial motion blur to clips that

have none. This can be useful in cases where a program was shot using a fast shutter speed, and you

later decide that the resulting video has too much strobing. By analyzing the motion within a clip, the

Motion Blur settings can selectively apply blurring to the image based on the speed and direction of

each moving element within the scene.

Motion Blur controls

Three parameters let you set how much motion blur to add, and at what quality:

�Motion Est. Type: A setting of Better provides more accurate pixel mapping at the expense of

being more processor intensive. Faster provides a more approximate result, but is less processor

intensive.

�Motion Range: Determines what speed of motion to consider when defining regions

being blurred.

�Motion Blur: Raise this parameter to add more motion blur to the image, lower it to add less.

The range is 0–100, where 0 applies no motion blur, and 100 applies maximum motion blur.


Color Page Effects | Chapter 153 The Motion Effects and Blur Palettes

COLOR

The Blur Palette

The Blur palette has three different modes of operation—blur, sharpen, and mist. While the

functionality of the Blur and Sharpen modes somewhat overlap, each mode provides dedicated

controls that the other ones lack.

As with virtually everything else in the Color page, the operations performed in the Blur palette can be

limited as a secondary operation using HSL Qualifiers, Windows, or Imported mattes, which makes it

easy to apply these effects to specific portions of the image.

Many of the controls in the Blur palette consist of three ganged sliders, one for red, one for green, and

one for blue.

By default, these ganged sliders move together as one, resulting in each color channel of the image

being equally affected. A small white button to the left of each control’s name lets you ungang these

sliders, in order to apply degrees of adjustment to individual color channels.

Blur

The default mode, Blur lets you apply an exceptionally high-quality Gaussian blur, or another equally

high-quality sharpening operation to your image. This mode of operation has the simplest controls.

Blur Radius controls are ganged by default, but can be unganged

Two sets of linked parameters let you adjust the extent and directionality of blur or sharpening. Which

is applied depends on the direction in which you adjust the Radius control.

�Radius: This is the primary control for adding blur or sharpening. The default value of 0.50 results

in no effect being applied to the image. Raising the radius slider increases blur, while lowering the

radius increases sharpness, with a minimum value of 0.00 providing maximum sharpness.

TIP: If you raise the Radius slider all the way to 1.00 and the image isn’t blurred enough,

add another node and use it to add another blur operation. You can also use the scroll

wheel on your mouse while hovering over one of the bars to increase the radius.

�H/V Ratio: Lets you add directionality to the current operation. At the default value of 0.50, the

image is affected in both the horizontal and vertical directions equally. Raising H/V Ratio makes

the effect increasingly directional along the horizontal axis, while lowering makes the effect

increasingly directional along the vertical axis.


Color Page Effects | Chapter 153 The Motion Effects and Blur Palettes

COLOR

Sharpen

While the Blur controls also let you apply sharpening simply by lowering, rather than raising,

the Radius sliders, the actual Sharpen mode provides additional controls specifically for tailoring

sharpening operations.

Sharpening with Coring Softness and Level

�Radius: This is the primary control for adding blur or sharpening. The default value of 0.50 results

in no effect being applied to the image. Raising the radius slider increases blur, to a maximum

value of 1.00. Lowering the radius increases sharpness, with a minimum value of 0.00 providing

maximum sharpness.

�H/V Ratio: Lets you add directionality to the current operation. At the default value of 0.50, the

image is affected in both the horizontal and vertical directions equally. Raising H/V Ratio makes

the effect increasingly directional along the horizontal axis, while lowering makes the effect

increasingly directional along the vertical axis.

�Scaling: Multiplies the amount of scaling being applied by the Radius control for sharpening

operations. The scaling parameter has no effect if Radius is set to 0.50 or above for blur effects.

The Coring Softness and Level parameters work together to let you limit sharpening to only the most

detailed areas of the picture that would most benefit from it, based on a threshold of image detail that

you define using the Level and Softness parameters.

�Level: The first slider you should use. Raising this value sets the threshold at which image detail

is omitted from the sharpening operation. The default setting of 0 sets the threshold low enough

to sharpen the entire image. Raising Level gradually omits low-detail areas of the image, which

results in sharpening being restricted to well-defined outlines.

�Coring Softness: After you’ve set the Level slider to an appropriate amount, raising Coring

Softness blends the border between parts of the image that are sharpened and parts of the image

that are left alone.


Color Page Effects | Chapter 153 The Motion Effects and Blur Palettes

COLOR

Mist

The Mist mode lets you combine blur and sharpen operations in such a way as to create effects similar

to those achieved via “Vaseline on the lens” or Pro-Mist optical filters.

Mist including Mist Mix control

Unlike the Blur or Sharpen modes, where the Radius sliders provide immediate access to the desired

effect, the Mist mode requires you to lower the Radius and Mix sliders together to get a desirable

result. By varying the amounts of Radius and Mix, you can create many variations on the mist effect.

�Radius: When creating a Mist effect, you first need to lower Radius to sharpen the image. This

operation then combines with a lowering of the Mix parameter to provide the combination of detail

and blurring that results in a mist effect.

�H/V Ratio: Lets you add directionality to the current operation. At the default value of 0.50, the

image is affected in both the horizontal and vertical directions equally. Raising H/V Ratio makes

the effect increasingly directional along the horizontal axis, while lowering makes the effect

increasingly directional along the vertical axis.

�Scaling: Multiplies the amount of scaling being applied by the Radius control, and lets you

intensify a mist effect beyond the Radius slider’s ordinary range. The scaling parameter has no

effect if Radius is set to 0.50 or above for blur effects.

�Mix: After you sharpen the image using the Radius slider, decreasing the Mix parameter adds a

superimposed blur that mixes with the high-detail areas of the picture to create the mist effect.


Color Page Effects | Chapter 153 The Motion Effects and Blur Palettes

COLOR

COLOR

Resolve FX

Overview

CONTENTS

154	 Resolve FX������������������������������������������������������������������������������������������������������������������������������������������������ 3458

155	 Resolve FX Blur���������������������������������������������������������������������������������������������������������������������������������������� 3461

156	 Resolve FX Color������������������������������������������������������������������������������������������������������������������������������������ 3467

157	 Resolve FX Film Emulation����������������������������������������������������������������������������������������������������������������� 3480

158	 Resolve FX Generate���������������������������������������������������������������������������������������������������������������������������� 3494

159	 Resolve FX Key���������������������������������������������������������������������������������������������������������������������������������������� 3496

160	 Resolve FX Light������������������������������������������������������������������������������������������������������������������������������������� 3509

161	 Resolve FX OpenColorIO��������������������������������������������������������������������������������������������������������������������� 3521

162	 Resolve FX Refine���������������������������������������������������������������������������������������������������������������������������������� 3524

163	 Resolve FX Revival�������������������������������������������������������������������������������������������������������������������������������� 3550

164	 Resolve FX Sharpen������������������������������������������������������������������������������������������������������������������������������ 3572

165	 Resolve FX Stylize���������������������������������������������������������������������������������������������������������������������������������� 3576

166	 Resolve FX Temporal���������������������������������������������������������������������������������������������������������������������������� 3599

167	 Resolve FX Texture�������������������������������������������������������������������������������������������������������������������������������� 3603

168	 Resolve FX Transform���������������������������������������������������������������������������������������������������������������������������� 3614

169	 Resolve FX Warp ����������������������������������������������������������������������������������������������������������������������������������� 3653