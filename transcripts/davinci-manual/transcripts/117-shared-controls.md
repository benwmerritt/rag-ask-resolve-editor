---
title: "Shared Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 117
---

# Shared Controls

Every category of effect at the bottom of the Viewer has two shared controls. A toggle control at the

far left lets you enable or disable an effect without losing whatever custom adjustments you’ve made.

A reset control at the far right lets you reset every parameter within a particular category of controls to

the default settings.

The Toggle button (at left) and Reset button (at right)

Transform

When you select Transform, onscreen transform controls appear that let you directly manipulate the

image in the Viewer. You can drag anywhere within the clip’s bounding box to adjust pan and tilt, drag

any diagonal corner to proportionally resize, drag any top/bottom/left/right side to squeeze or stretch

width or height, or drag the center handle to rotate.

Onscreen Transform controls in the Viewer

TIP: While dragging a clip using the onscreen controls to reposition it, holding the Shift key

down constrains movement to just the X or Y axes.

The onscreen controls also correspond to the following editable parameters, which are also editable in

the Video Inspector and in the Edit Sizing mode of the Sizing palette in the Color page:

Zoom Width and Height: Allows you to blow the image up or shrink it down. The X and

Y parameters can be linked to lock the aspect ratio of the image, or released to stretch or

squeeze the image in one direction only.

Position X and Y: Moves the image within the frame, allowing pan and scan adjustments to be

made. X moves the image left or right, and Y moves the image up or down.

Rotation Angle: Rotates the image around the anchor point.

Pitch: Rotates the image toward or away from the camera along an axis running through the

center of the image, from left to right. Positive values push the top of the image away and

bring the bottom of the image forward. Negative values bring the top of the image forward

and push the bottom of the image away. Higher values stretch the image more extremely.

Yaw: Rotates the image toward or away from the camera along an axis running through the

center of the image from top to bottom. Positive values bring the left of the image forward and

push the right of the image away. Negative values push the left of the image away and bring

the right of the image forward. Higher values stretch the image more extremely.

Flip Image: Two buttons let you flip the image in different dimensions.

•	 Flip Horizontal control: Reverses the image along the X axis, left to right.

•	 Flip Vertical control: Reverses the clip along the Y axis, turning it upside down.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

Crop

The Cut page has a set of onscreen controls you can use to directly crop the image in the Viewer.

Each side of the image has an individual handle for cropping just that side. These parameters are also

editable in the Video Inspector and the Color page Sizing palette.

Onscreen Crop controls in the Viewer

The Crop effects also correspond to an additional set of cropping parameters, with an additional

control for softness:

Crop Left, Right, Top, and Bottom: Lets you cut off, in pixels, the four sides of the image.

Cropping a clip creates transparency, so whatever is underneath shows through.

Softness: Lets you blur the edges of a crop. Setting this to a negative value softens the

edges inside of the crop box, while setting this to a positive value softens the edges outside

of the crop box.

Dynamic Zoom

The Dynamic Zoom controls, which are off by default, make it fast and easy to do pan and scan effects

to zoom into or out of a clip. A set of two onscreen controls let you create a Dynamic Zoom effect.

A green box shows the starting size and position of the animated transform, while a red box shows

the ending size and position of the animated transform. Drag anywhere within either bounding box to

reposition either the start or the end of the animated effect, and drag any of the corners to adjust the

size at the start or end. A motion path appears to show you motion that’s being created. Adjusting the

Dynamic Zoom controls automatically enables dynamic zoom. These controls are also available in the

Video Inspector.

Dynamic Zoom controls in the Viewer

These controls correspond to two parameters in the toolbar (Dynamic Zoom is also editable in the

Video Inspector).

Zoom/Pan/Angle Presets: Let you enable or disable preset positions for the zoom level, pan

location, and angle of this effect.

Swap: This button reverses the start and end transforms that create the dynamic zoom effect.

Ease Buttons: Lets you choose how the motion created by these controls accelerates. You

can choose from Linear, Ease In, Ease Out, and Ease In and Out.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

TIP: While dragging dynamic zoom outlines to reposition them, holding the Shift key down

constrains movement to just the X- or Y-axis.

Composite

Two controls let you create transparency and use composite modes to create different compositing

effects (also called Blend modes or Transfer modes). These controls also editable in the

Video Inspector.

Composite controls in the Viewer

Composite Modes: Composite modes blend two superimposed clips together on the

Timeline using different kinds of math to achieve differing results, to create transparency

effects, increase image exposure, and combine multiple clips into a single image in many

creative and useful ways. All Composite modes interact with the Opacity slider.

For more information on what each Composite mode does, see Chapter 50, “Compositing and

Transforms in the Timeline.”

Opacity: This slider lets you make a clip more transparent, over a range from 0 (totally

transparent) to 100 (totally opaque). When set to a value less than 100, the selected clip is

mixed with whatever video clip is underneath it on the Timeline, using the Composite mode

that’s currently selected. If no clip appears underneath the Timeline, then the clip is mixed with

black and will work similarly to a fade.

TIP: If a superimposed video or still image clip in the Timeline has an alpha channel, that

alpha channel automatically creates transparency within that clip, compositing it against

whatever is in the track underneath. There’s no need for you to do anything for this to work.

Speed

Speed effects let you speed up, slow down, or otherwise change the playback speed of clips in the

Timeline. When you change the speed of a clip, that clip’s duration also changes to reflect a shorter

clip that plays faster, or a longer clip that plays more slowly. Speed effects change both video and

audio playback, but the audio of sped up or slowed down clips is always pitch corrected. Speed

effects applied in the Cut page also appear and are editable via several different methods in the

Edit page timeline and the Video inspector.

Speed Effects controls in the Viewer


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

Add Speed Point: Lets you add a speed change point at the playhead position for speed

ramping effects.

Speed: Changing this value lets you speed up or slow down playback by a simple numeric

multiplier. You also have the option of choosing a negative value to create reverse speeds.

Duration: When you retime a clip, the Duration field lets you see how the change you’re

making affects the new duration based on the original duration of the clip with no speed

effect applied.

Stabilization

The Image Stabilization controls use warping and/or translation to let you smooth out or even lock

unwanted camera motion within a clip. The analysis is performed in such a way as to preserve the

motion of individual subjects within the frame, as well as the overall direction of desirable camera

motion, while correcting for unsteadiness.

Stabilization controls in the Viewer

To stabilize an image, all you need to do is to choose a Stabilization Method from the drop-down (see

below for more information), and then click the Stabilize button. DaVinci Resolve analyzes the current

clip, and applies a stabilization effect.

The rest of the stabilization controls let you refine the result. Whenever you adjust any of these

parameters, you must click the Stabilize button again for the effect to be updated.

Stabilization Method: A drop-down menu provides three different options that determine how

the selected clip is analyzed and transformed during stabilization. You must choose an option

first, before clicking the Stabilize button, because the option you choose changes how the

image analysis is performed. If you choose another option, you click the Stabilize button again

to reanalyze the clip.

•	 Perspective: Enables perspective, pan, tilt, zoom, and rotation analysis and stabilization.

•	 Similarity: Enables pan, tilt, zoom, and rotation analysis and stabilization, for instances

where perspective analysis results in unwanted motion artifacts.

•	 Translation: Enables pan and tilt analysis and stabilization only, for instances where only

X and Y stabilization gives you acceptable results.

Stabilize: Clicking this button on a previously unstabilized clip analyzes the motion in that

clip and applies an initial smoothing effect. Clicking this button on a clip that’s already been

analyzed lets you recalculate a modified stabilization effect.


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT

TIP: These controls are identical to those found in the Video Inspector and the Color page

Tracker palette, and populate the same image processing data. This means that you can use

the Stabilization found on the Cut page, and then use the stabilization graph and controls

found in the Color page to refine the results, if necessary.

Lens Correction

Lens Correction presents two controls that let you either correct lens distortion in the image, or add

lens distortion of your own for effect. These controls are also editable in the Video Inspector and Color

page Edit Sizing palette.

Lens Correction controls in the Viewer

Analyze: Automatically analyzes the frame in the Timeline at the position of the playhead

for edges that are being distorted by wide angle lens. Clicking the Analyze button moves

the Distortion slider to provide an automatic correction. If you’re analyzing a particularly

challenging clip, a progress bar will appear to let you know how long this will take.

Distortion: Dragging this slider to the right lets you manually apply a warp to the image that

lets you straighten the bent areas of the picture that can be caused by wide angle lenses. If

you clicked the Analyze button and the result was an overcorrection, then dragging this slider

to the left lets you back off of the automatic adjustment until the image looks correct.

Color

The Color section of the Tools consists of only one option: Auto Color. The Auto Color command

provides a quick way to automatically balance the blacks and whites of a clip based on the current

frame at the position of the playhead. Using advanced algorithms, based on the DaVinci Neural

Engine, it provides superior results when automatically adjusting color balance and contrast.

For more details on using Auto Color, see Chapter 127, “Automated Grading Commands and

Imported Grades.”

Color controls in the Viewer


The Cut Page | Chapter 31 Video and Audio Effects in the Cut Page

CUT