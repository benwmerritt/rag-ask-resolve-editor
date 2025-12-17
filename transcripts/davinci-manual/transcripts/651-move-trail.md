---
title: "Move Trail"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 651
---

# Move Trail

This group of controls determines the offset, direction, size, and rotation of the copies. Adjustment

amounts are applied as offsets from one copy to the next. For instance, if rotation is set to 5 degrees,

the first trail copy is rotated 5 degrees, the second trail copy is rotated 10 degrees, the third copy is

rotated 15 degrees, and so on.

�Pan: Adjusts the offset of the trail copies from the original image.

�Pan Angle: Changes the angle at which the trails are offset from the original image. The values are

shown in degrees.

�Zoom: Adjust a scale adjustment, successively, to each copy.

�Rotate: Applies an angle of rotation, successively, to each copy.

�Reuse Current Frame: When this checkbox is disabled (the default), each copy uses the frame

after the copy before it. For instance, the first copy is the current frame -1, and the second copy is

the current frame -2. When this checkbox is enabled, all copies use the same frame as the current

frame in the clip.

�Border Type: This menu determines how edges of the frame are handled when the copies are

scaled smaller than the timeline resolution.

Black: The area outside the image is set to black.

Soften: This control blends the edges of the rectangular frame borders to give the images a more

organic appearance.

Replicate: Duplicates the outermost pixels along the edge of the image. The pixels are stretched

out from each side to reach the timeline resolution boundary.

Reflect: The image is flipped and flopped to create a mirrored image that extends to the timeline

resolution frame boundary.

Wrap-Around: Duplicates the image to create a video wall effect, used to fill in the space to the

timeline resolution frame boundary.

Smear (Studio Version Only)

The Smear effect simulates motion blur in a clip by blending a user-definable number of frames.

�Frames Either Side: Determines the number of frames that are blended on either side of the

current frame. For instance, entering a value of 2 uses two frames before and two frames after the

current frame to create the effect.

�Luma Threshold: This control sets how bright a pixel must be to contribute to the smear effect.

A lower value causes only darker pixels to be smeared. A higher value includes brighter

pixels in the effect.

�Chroma Threshold: This control sets how saturated a pixel must be to contribute to the smear

effect. A lower value causes only low saturated pixels to be smeared. A higher value includes

more saturated pixels in the effect.


Resolve FX Overview | Chapter 166 Resolve FX Temporal

COLOR

Stop Motion

This plugin is used to replicate the stuttering motion effect found in stop motion animations.

Traditional stop motion animation exposes each frame of the shot individually, while the subject is

manually moved in tiny increments between frames. An extremely labor intensive process, often

individual frames were repeated in a shot to speed up the production which resulted in a staccato

motion cadence.

Advanced Options

Set Reference Frame: Selects the current frame in the Viewer as the reference frame.

Reference Frame: The frame number of the reference frame used for the skip pattern.

The frame number is calculated from the start of the entire original media clip (frame 0).

Sampling Variation: This slider increasingly produces more uneven motion in the clip.

Frame Repeat: Selects how many frames (from 1-10) to duplicate in the shot. A larger number

makes a more staggered cadence.


Resolve FX Overview | Chapter 166 Resolve FX Temporal

COLOR

Chapter 167

Resolve FX Texture

These plugins are designed to add texture to images, to replicate both naturalistic

and other effects.

Contents

Analog Damage (Studio Version Only)������������������������������������������������������������������������������������������������������������������������������������ 3604

Detail Recovery (Studio Version Only)������������������������������������������������������������������������������������������������������������������������������������� 3606

Detail Recovery����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3607

Details Extraction������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3607

Fast Noise���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3608

Appearance������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3609

Adjustment�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3609

Position��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3609

Auto-Animation������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3610

Output������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3610

JPEG Damage�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3610

Texture Pop (Studio Version Only)����������������������������������������������������������������������������������������������������������������������������������������������� 3611

Mode Controls�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3613

Details Controls����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3613

Tonal Range Controls����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3613


Resolve FX Overview | Chapter 167 Resolve FX Texture

COLOR

Analog Damage (Studio Version Only)

A Texture category plugin that simulates different kinds of signal degradation resulting from analog

transmission and recording, Analog Damage can be used to create “old TV” or “junky videotape”

effects of various kinds. A Preset pop-up menu lets you choose from a variety of different looks, while

a Custom option lets you create your own.

(Top) The original image, (Bottom) The image with Analog Damage applied

Preset: Lets you add a number of video damage types to your footage that DaVinci Resolve was

designed to repair in the first place.

It has the following categories of parameters:

Telecine Source: Options for lens vignetting and automated shutter weave to the left and right.

�Vignetting: Darkens the image around the edges to replicate a poor lamp in a telecine.

�Vignette Aspect: Adjusts the width of the vignette effect.

�Shutter Weave: Replicates the slight movement of the image as the film reel unwinds

on a telecine.


Resolve FX Overview | Chapter 167 Resolve FX Texture

COLOR

Broadcast Signal: Options for customizable noise, detail loss, signal ghosting, and

chroma misalignment.

�Noise Scale: Determines how fine the noise is.

�Signal Noise: Determines how much static is in the Luma signal.

�Chroma Noise: Determines how much static is in the Chroma signal.

�Detail Loss: Determines how much of the detail is lost in “transmission.”

�Chroma Detail Loss: Determines how much of the chroma detail is lost in “transmission.”

�Ghosting: Replicates the ghost image due to a reflected signal.

�Ghost Offset: Lets you reposition the ghost image.

�Chroma Misalignment: Determines how offset the color signal is from the brightness.

Color Dials: Television-signal specific color adjustment controls.

�Brightness: Replicates a consumer television brightness control knob.

�Contrast: Replicates a consumer television contrast control knob.

�Color: Replicates a consumer television color (saturation) control knob.

�Tint: Replicates a consumer television tint control knob.

Scan: Controls to simulate problems with television scanning.

�Image Aspect: Adjusts the shape of the frame, padding or cropping as necessary.

�H-Shift: Lets you roll the image horizontally.

�V-Shift: Lets you roll the image vertically.

�V-Hold/Latch: V-Hold interacts with the V-Hold Latch parameter to make it easy to use simple key

framing to trigger animated vertical rolls that “bounce” over time in a realistic way for broadcast.

�Overscan: Allows you to adjust how much of the image is cropped for display on the screen.

�V-Scale: Lets you adjust the vertical scaling of the image.

�Vertical Blanking: Lets you determine the Vertical Blanking Interval size.

Scan lines: Simulate customizable television scan lines that are capable of simulating moire and color

artifacts.

�Line Sharpness: Lets you adjust the visible sharpness of the scan lines.

�Line Frequency: Lets you adjust how many scan lines are in the image.

�Colored Lines: Check this box to add color outlines to the scan lines.

TV Construction: Controls to simulate issues with CRT phosphor brightness, tint, and defocus, and the

ability to add a customizable curved border and warped screen curvature.

�Phosphor Brightness: Lets you adjust the brightness of the front screen, even when

the tv should be “off.”

�Phosphor Tint: Lets you adjust the color of the front screen, even when the tv should be “off.”

�Defocus: Lets you adjust how much detail is lost to the screen.

�Screen Curvature: Lets you adjust how curved the picture tube is.

�Edge Mask: Check this box to add a black mask around the edge of the screen.

�Edges Transparent: Check this box to make the screen edges transparent for compositing.

�Mask Curvature: Lets you adjust the shape of the black mask.

�Mask Aspect: Lets you adjust the black mask’s aspect ratio.


Resolve FX Overview | Chapter 167 Resolve FX Texture

COLOR

VHS: Lets you add a customizable “Restless Foot” to simulate recorded tape artifacts.

�Restless Foot Height: Lets you set how much restless foot intrudes from the bottom of the screen.

�Restless Foot Offset: Lets you choose which direction and how much to distort the restless foot.

�Restless Foot Jitter: Lets you adjust the shaking of the restless foot between frames.

TIP: Using the Analog Damage plugin on the Fusion page makes it possible connect

Modifiers to add automatic animation (such as Perturb) to different parameters in order to

quickly and easily create automated video damage effects.