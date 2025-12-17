---
title: "YSFX Sliders"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 559
---

# YSFX Sliders

Each of the Custom curves (Y’, R, G, and B) has a vertical YSFX slider at the upper left-hand corner

of the Curve Editor that lets you invert any or all color channels by any amount you want, to create

different types of stylized effects.

Image with the Luma channel modified using the vertical YSFX slider

As with all other adjustments in the Color page, YSFX may be combined with Power Windows or

HSL qualification to limit channel inversions to specific portions of the image for creative purposes.

Soft Clip

The Soft Clip controls consist of four sliders underneath the Curve controls of the Custom curves,

and give you an interface for adjusting highlight and shadow soft clipping either overall, with Ganging

enabled, or on a per-channel basis. The Soft Clip controls are intended to provide clip-by-clip

adjustment, as opposed to the Generate Soft Clip LUT settings, which let you set one soft-clipping

setting for the entire program.

For more information on the Soft Clip LUT setting, see Chapter 4, “System and User

Preferences.”

High and Low Soft Clip controls

within the Curves palette

Soft clipping lets you apply a “knee” to any clipping that occurs at the upper or lower extremes of the

image, and can be used to quickly ease off any unpleasantly harsh loss of detail that occurs as a result

of blowing out the highlights or crushing the shadows too aggressively.

In the following example, the screenshot at top has had the highlights deliberately blown out by

excessively boosting the highlight contrast. As you can see, the edges of the clipped area lack

detail. The screenshot at bottom shows the same image with soft clipping increased for all three

color channels. The result retrieves detail, compressing the highlights to bring the tops of each color

channel back within the allowable range.


Color | Chapter 134 Curves

COLOR

Using High Soft Clip to pull highlight details into the viewable range

Ganging and Unganging Soft Clip Controls

Soft clipping can be simultaneously applied to all three color channels by enabling the Ganging control

(on by default), or you can disable Soft Clip ganging to individually adjust each channel. For example,

using soft clipping on individual channels can be useful for legalizing RGB out-of-gamut errors for

channels that over- or undershoot your QC standards.

To disable Soft Clip ganging and edit soft clipping for individual color channels:

Click the channel control button corresponding to the color channel you want to edit, and then

drag the sliders to create the desired adjustment.

To re-enable Soft Clip ganging:

Click the Ganging control to the left of the Soft Clip channel controls.

TIP: Applying too much soft clipping to individual color channels may add an unwanted

color tint to the corresponding highlights or shadows of an image. To avoid this, use the soft

clipping parameters with ganging enabled to clip all three color channels equally.

Soft Clip Controls

Whether all channels are ganged or not, soft clipping is controlled via two sliders and two additional

parameters for each color channel.

High

The High Clipping Point slider lets you adjust the maximum signal level above which the signal is

clipped. Any pixels above the clipping level are made equal to the clipping level.


Color | Chapter 134 Curves

COLOR

The High Clipping Point defaults to a digital level of 1023 relative to the DaVinci Resolve internal

video scopes. Dragging this slider to the left causes the highlights of the image to clip at a lower

level, resulting in lower, dimmer maximum levels.

Selecting and adjusting

the high clip

RGB Parade displays

the clipped image

At the default position, no clipping occurs and image data that you push above 1023 on the

internal scopes is preserved and passed through the image processing pipeline to subsequent

nodes. For example, in the following two screenshots, the highlights in the screenshot at top

are blown out raising the gain dramatically in Node 1. In the screenshot at bottom, a subsequent

adjustment in Node 2 lowers the gain and retrieves all the previously clipped values.

The image is clipped using the Gain control in Node 2


Color | Chapter 134 Curves

COLOR

The image data that was clipped in Node 1 is retrieved in Node 3 by lowering the Gain

control. This illustrates the preservation of deliberately clipped data.

However, if at any point in a node tree you drag the High Clip slider to the left, even by a single

digit, all image data above the new clipping threshold is discarded from that node forward. In

the following example, the High Clip slider in Node 1 is lowered. The result is that all clipped

image data is discarded. As a result, when Node 2 lowers the gain, there is no image detail left to

retrieve, and all three channels exhibit flattening.

Lowering the High Clip slider in Node 1 forces all image data above the new High Clip threshold

to be irretrievably discarded. Clipped data cannot be brought back by subsequent nodes.

High Soft

The High Soft slider sets the threshold, below the clipping point, at which highlights begin to compress

before hard clipping. At unity, no soft clipping occurs. As you raise this value, more and more of

the clipped highlight values are compressed, rather than clipped, resulting in softer, more pleasant

“glowing” highlights.

IMPORTANT: Image data that was clipped “in camera” is not necessarily retrievable using

the Soft Clip controls, although there may be some preserved overhead in the super-white

highlights of Y’CbCr-encoded video data.

Low

The Low Soft Clipping Point slider lets you adjust the minimum signal level at which the signal clips.

This defaults to a digital level of 0 relative to the DaVinci Resolve internal video scopes. Dragging this

slider to the right causes the shadows of the image to clip at a higher level, resulting in lighter minimum

levels, and a lower-contrast image with lighter (possibly milky) shadows.


Color | Chapter 134 Curves

COLOR

Low Soft

The Low Soft slider sets the threshold, above the minimum clipping point, at which shadows begin to

compress before hard clipping. At unity, no soft clipping occurs. As you drag this slider to the right,

more and more of the clipped shadow values are compressed, rather than clipped, resulting in a

softer, more pleasant rolloff in the shadows.

The HSL Curves

Three sets of Hue curves, and additional Lum vs. Sat, Sat vs. Sat, and Sat vs Lum curves, let you

make different types of curve-based alterations to the image. Whereas the Custom curves let you

make adjustments to the color channels of an image based on tonality (for example, boosting the Red

channel in the highlights while lowering it in the shadows), the Hue curves let you make adjustments to

the hue, saturation, or luma of elements in an image based on their hue.

Curves controls including six-vector selection and bezier handle button

For example, you could use the Hue vs. Sat curve to selectively lower the saturation of everything

that’s blue, while raising the saturation of everything that’s red.

You can use these curves to make adjustments similar to those made using HSL qualification, but

with one critical difference. Curve adjustments are mathematically smoother than the matte-limited

adjustments of HSL qualifiers, so it can sometimes be easier to make specific alterations that blend

smoothly with the rest of the image, without the potential for artifacts at the edges of qualified keys

that can sometimes defeat a seamless result.

On the other hand, it is often easier to define more distinct boundaries between separate elements

using HSL qualification. Only time and experience will help you determine which tools are best for

which situations.


Color | Chapter 134 Curves

COLOR

Right–Original image, Left–the image as altered by the Hue vs. Sat curve shown above

Unlike the Custom curves, which default to a diagonal position where lower left represents the black

point and upper right represents the white point, Hue and Sat curves are flat. In the case of the Hue

vs. Hue/Sat/Lum curves, the horizontal range of the curve from left to right represents the overall

range of possible hues, from red through green through blue and then cycling back to red.

Because the range of hues cycle smoothly from the left to the right edge, changes that affect the

curve near the left boundary of these curves loop smoothly around to the right boundary, and vice

versa, such that the left and right sides of the curve always move together (as you can see in the

above screenshot).

IMPORTANT: When using Hue curves, the range of hue that you isolate with control points

is always relative to the RGB input connected to that node. That means if you change the

hue of a shirt from blue to red using Hue vs. Hue and you then want to raise the same shirt’s

saturation with the Hue vs. Sat curve within the same node, you need to add control points to

the same range of blue for both curves.