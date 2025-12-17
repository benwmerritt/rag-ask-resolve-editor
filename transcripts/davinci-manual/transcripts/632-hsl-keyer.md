---
title: "HSL Keyer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 632
---

# HSL Keyer

Based on the HSL Qualifier in the Color page, the HSL Keyer Resolve FX is a general-purpose keyer

that uses three color components, hue, saturation, and luma, to define a key. The HSL Keyer also gives

you the option of disabling color components that you don’t want to contribute to the final key. You can

pull a saturation-only key, or a hue-only key, for instances where choosing only individual components

gives a better result.

The most straightforward way to use any keyer is to sample the image in the Viewer with no changes

to the settings. When you sample one or more pixels, the hue, saturation, and luma values are

analyzed and set different ranges. There are several eyedropper controls available to sample color

and soften the selection.

Selection Range Controls

The Selection Range buttons in the Inspector let you define a key by sampling and softening pixels in

the Viewer with the mouse pointer.

HSL Keyer Color Range controls

�Sample Eyedropper: This tool selects the colors to use as the range of qualification by

clicking and dragging over the image in the Viewer. Clicking it again clears the previous selection.

Generally, you will get better results using long drags instead of short ones.

�Add/Subtract Color Range: These two controls let you add areas of the image to, or subtract them

from, the currently selected inner range of values that define the core of the key. Like the other

sampling controls, you can drag over a range of color.

�Add/Subtract Softness: These two controls let you redefine the softness that transitions from

the inner range of the key, falling off towards the outer edge of the key. Like the other sampling

controls, you can drag over a range of color.

�Invert: Inverts the sampled color to become opaque, and areas not sampled become transparent.

�Reset: Resets all the sampled colors while retaining the general control settings.

Keyer Options

One of the HSL Keyer’s strengths is that you can enable or disable each of the three HSL components

using the Hue, Sat, and Lum checkboxes. This lets you ignore specific color components while

focusing on others that may be more important. For example, if you’re trying to key the saturated parts

of an image, regardless of the hue or brightness, you can turn off Hue and Lum so that only Sat is used

to sample it.

HSL Keyer options


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR

Matte Finesse

You may find that sampling the screen color is not enough to overcome some problems. Issues

such as chattery edges, holes, or noise can sometimes be fixed using the Matte Finesse controls.

These controls filter the output of the Keyer and are adjustments that are made to the matte itself,

modifying the key using the frame’s content.

�Pre Filter: This slider attempts to clean up the image before colors are sampled. This adjustment

can be useful when you have footage containing MPEG blocking artifacts.

�Clean Black: Clean Black is a specialized operation that eliminates noise seen as white speckling

in the black area of a key. Raising Clean Black lets you “fill holes” in the background portion of a

key and erode translucent edges.

�Clean White: Clean White is another specialized operation that eliminates noise (seen as black

speckling when viewing a high-contrast highlight) in the white portion of a key that includes

areas of the image you’re isolating and expands the key by making light parts of a key lighter the

higher you raise this parameter, pushing light gray areas of the key toward white. The practical

result is that raising Clean White lets you “fill holes” in the foreground portion of a key and grow

translucent edges.

�Black Clip: Raising Black Clip applies a “lift” adjustment such that translucent areas of the matte

(gray areas when viewing a high-contrast highlight) are pushed toward black. The range is

0 to 100, with 0 being the default setting.

�White Clip: Lowering White Clip applies a “gain” adjustment such that translucent areas of the

matte (gray areas when viewing a high-contrast highlight) are pushed toward white. The range

is 0 to 100, with 100 being the default setting.

�Blur Radius: In small amounts, blurring a key does well to take the edge off problem edges.

However, blurring a key can also feather the edges of a key past the border of the subject you’re

keying, with the result being a visible “halo” around your subject, depending on the adjustment

you’re making. The range is 0 to 2000, with 0 being the default. With such a large maximum blur

radius, combined with the capabilities that the In/Out Ratio provides in customizing the direction of

spread, you can turn some pretty precarious mattes into surprisingly smooth and useful results.

�In/Out Ratio: Using In/Out Ratio can help eliminate fringing. Raising In/Out Ratio will fill in small

black holes in the matte, while lowering In/Out Ratio below 0 will eliminate speckling by pushing

small white bits of the matte toward black.

�Morph Operation: You can choose Shrink or Grow to dilate or erode the edges of the matte, or

you can choose Opening or Closing to plug or expand holes to clean up a ragged matte.

�Morph Radius: Adjusts how much to shrink, grow, open, or close the key.

�Denoise: Provides a distinct way to post-process extracted keys to selectively reduce the noise in

a key, getting rid of stray areas of qualification and softly filling holes in a matte.

�Shadow: Adjusts key strength based on the darker parts of the original image.

�Midtone: Adjusts key strength based on the midtones of the original image.

�Highlight: Adjusts key strength based on the brighter parts of the original image.

�Post Filter: Performs a final clean-up of the key, using the original image for reference; useful for

bringing back some fine detail in sharp edges or hair.


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR

Garbage Matte

These controls let you crop out other unwanted things in the frame, such as lighting fixtures, boom

microphones, tracking patches, etc.

�Matte Shape: You can choose either a Rectangle or Ellipse with which to crop around the subject

you’re keying. Choosing None turns off Garbage Matte. When a garbage matte is enabled, the

Open FX Overlay mode of the Viewer shows an on-screen control for adjusting the shape and

position of the garbage matte.

�Edge Softness: Lets you soften the edges. Defaults to 50; the range is 0 (no softening) to 100

(maximum softening).

�Invert: Inverts the garbage matte.

�Center X and Y: Lets you adjust and keyframe the position of a garbage matte.

�Bounding Width and Height: Lets you adjust the width and height of the garbage matte.

�Rotation: Lets you adjust the angle of the garbage matte.

Output

The Output controls let you choose how the image is output, composited, and displayed in the Viewer.

�Output: This menu offers three options for which channels are output from the effect.

Alpha Highlight: Displays the transparent part of an Alpha channel as gray and the solid part of an

alpha channel in full color.

Alpha Highlight B/W: Displays the black and white Alpha channel, which is often helpful when

sampling additional areas to key.

Final Composite: The keyed image is displayed composited over any video track below it.

�Use Alpha: A common control in many Resolve FX and 3rd party Open FX plugins; this checkbox

determines if the Alpha channel is used when compositing over another video track. It can be

used instead of choosing RGB Only (Blank Alpha) from the Output menu.

To use the HSL Keyer in the Edit page:


Apply the HSL Keyer to a clip on video track 2 or higher.


From the Viewer Overlay menu in the lower-left corner of the Timeline Viewer

choose Open FX Overlays.


Click and drag across the screen color you want to remove.


The transparency immediately takes effect, showing the keyed subject against whatever clip

appears on the video track underneath it in the Timeline as a composite. To see the matte you

created for further adjustment, choose Alpha Highlight or Alpha Highlight B/W from the Output

drop-down menu.


To add or subtract from the matte, click the plus or minus Color Range control, and click or drag

across the portion of the keyed image.


To add softness to the outer range of the key you’re creating, click the plus Softness control and

then click or drag across the portion of the image you’d like to include as a soft edge.


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR

Luma Keyer

Based on the Luma Qualifier in the Color page, the Luma Keyer pulls a key from the luma channel. It’s

identical to the HSL Keyer with H and S turned off. Although not often used by itself, the Luma Keyer

can produce useful effects when used in conjunction with Composite modes.

Selection Range Controls

The Selection Range buttons in the Inspector let you define a key by sampling pixels in the Viewer

with the mouse pointer.

Luma Keyer Selection Range controls

�Sample Eyedropper: The first control you use whenever sampling the image. It defines the initial

range of the keyer; you must use this tool before any of the others. In the Edit page, the Timeline

Viewer Overlay must be set to Open FX. Clicking once with this tool selects a single pixel value,

while clicking and dragging selects a range of image values that add together.

�Add/Subtract Luma Range: These two controls let you add areas of the image to, or subtract them

from, the currently selected luma range that defines the core of the key. As with the eyedropper,

you can click on single pixels, or drag over a range of color.

�Add/Subtract Softness: These two controls let you redefine the softness that transitions from the

inner range of the key, falling off towards the outer edge of the key. Like the other keying controls,

you can click on single pixels, or drag over a range of color.

�Invert: Inverts the sampled luma range to become opaque, and areas not sampled

become transparent.

�Reset: Resets the sampled luma range while retaining the Output control settings.

Matte Finesse

You may find that sampling the screen color is not enough to overcome some problems. Issues

such as chattery edges, holes, or noise can sometimes be fixed using the Matte Finesse controls.

These controls filter the output of the Keyer and are adjustments that are made to the matte itself,

modifying the key using the frame’s content.

�Pre Filter: This slider attempts to clean up the image before colors are sampled. This adjustment

can be useful when you have footage containing MPEG blocking artifacts.

�Clean Black: Clean Black is a specialized operation that eliminates noise seen as white speckling

in the black area of a key. Raising Clean Black lets you “fill holes” in the background portion of a

key and erode translucent edges.

�Clean White: Clean White is another specialized operation that eliminates noise (seen as black

speckling when viewing a high-contrast highlight) in the white portion of a key that includes

areas of the image you’re isolating and expands the key by making light parts of a key lighter the

higher you raise this parameter, pushing light gray areas of the key toward white. The practical

result is that raising Clean White lets you “fill holes” in the foreground portion of a key and grow

translucent edges.


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR

�Black Clip: Raising Black Clip applies a “lift” adjustment such that translucent areas of the matte

(gray areas when viewing a high-contrast highlight) are pushed toward black. The range is 0 to

100, with 0 being the default setting.

�White Clip: Lowering White Clip applies a “gain” adjustment such that translucent areas of the

matte (gray areas when viewing a high-contrast highlight) are pushed toward white. The range is 0

to 100, with 100 being the default setting.

�Blur Radius: In small amounts, blurring a key does well to take the edge off problem edges.

However, blurring a key can also feather the edges of a key past the border of the subject you’re

keying, with the result being a visible “halo” around your subject, depending on the adjustment

you’re making. The range is 0 to 2000, with 0 being the default. With such a large maximum blur

radius, combined with the capabilities that the In/Out Ratio provides in customizing the direction of

spread, you can turn some pretty precarious mattes into surprisingly smooth and useful results.

�In/Out Ratio: Using In/Out Ratio can help eliminate fringing. Raising In/Out Ratio will fill in small

black holes in the matte, while lowering In/Out Ratio below 0 will eliminate speckling by pushing

small white bits of the matte toward black.

�Morph Operation: You can choose Shrink or Grow to dilate or erode the edges of the matte, or

you can choose Opening or Closing to plug or expand holes to clean up a ragged matte.

�Morph Radius: Adjusts how much to shrink, grow, open, or close the key.

�Denoise: Provides a distinct way to post-process extracted keys to selectively reduce the noise in

a key, getting rid of stray areas of qualification and softly filling holes in a matte.

�Shadow: Adjusts key strength based on the darker parts of the original image.

�Midtone: Adjusts key strength based on the midtones of the original image.

�Highlight: Adjusts key strength based on the brighter parts of the original image.

�Post Filter: Performs a final clean-up of the key, using the original image for reference; useful for

bringing back some fine detail in sharp edges or hair.

Garbage Matte

These controls let you crop out other unwanted things in the frame, such as lighting fixtures, boom

microphones, tracking patches, etc.

�Matte Shape: You can choose either a Rectangle or Ellipse with which to crop around the subject

you’re keying. Choosing None turns off Garbage Matte. When a garbage matte is enabled, the

Open FX Overlay mode of the Viewer shows an on-screen control for adjusting the shape and

position of the garbage matte.

�Edge Softness: Lets you soften the edges. Defaults to 50; the range is 0 (no softening) to 100

(maximum softening).

�Invert: Inverts the garbage matte.

�Center X and Y: Lets you adjust and keyframe the position of a garbage matte.

�Bounding Width and Height: Lets you adjust the width and height of the garbage matte.

�Rotation: Lets you adjust the angle of the garbage matte.


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR