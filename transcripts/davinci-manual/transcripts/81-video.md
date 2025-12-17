---
title: "Video"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 81
---

# Video

The Video Panel of the Inspector exposes a vast array of controls designed to manipulate the size,

speed, and opacity of your clips.

Transform

The Transform section of the Video Inspector panel

The Transform group includes the following parameters for resizing and repositioning your clips:

�Zoom X and Y: Allows you to blow the image up or shrink it down. The X and Y parameters can

be linked to lock the aspect ratio of the image, or released to stretch or squeeze the image in one

direction only.

�Position X and Y: Moves the image within the frame, allowing pan and scan adjustments to be

made. X moves the image left or right, and Y moves the image up or down.

�Rotation Angle: Rotates the image around the anchor point.

�Anchor Point X and Y: Defines the coordinate on that clip about which all transforms are centered.

�Pitch: Rotates the image toward or away from the camera along an axis running through the

center of the image, from left to right. Positive values push the top of the image away and bring

the bottom of the image forward. Negative values bring the top of the image forward and push the

bottom of the image away. Higher values stretch the image more extremely.

�Yaw: Rotates the image toward or away from the camera along an axis running through the center

of the image from top to bottom. Positive values bring the left of the image forward and push the

right of the image away. Negative values push the left of the image away and push the right of the

image forward. Higher values stretch the image more extremely.

�Flip Image: Two buttons let you flip the image in different dimensions.

Flip Horizontal control: Reverses the image along the X-axis, left to right.

Flip Vertical control: Reverses the clip along the Y-axis, turning it upside down.

Cropping

The Cropping section of the Video Inspector panel


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA

The Video Inspector controls the image’s cropping parameters:

�Crop Left, Right, Top, and Bottom: Lets you cut off, in pixels, the four sides of the image. Cropping

a clip creates transparency so that whatever is underneath shows through.

�Softness: Lets you blur the edges of a crop. Setting this to a negative value softens the edges

inside of the crop box, while setting this to a positive value softens the edges outside of

the crop box.

�Retain Image Position: Clicking this checkbox will lock the crop parameters in place when you

resize the image using the Transform tool above. Unchecking this box will scale and position the

crop as well as the image.

Dynamic Zoom

The Dynamic Zoom section of the Video Inspector panel

The Dynamic Zoom controls, which are off by default, make it fast and easy to do pan and scan

effects to zoom into or out of a clip. Turning the Dynamic Zoom group on activates two controls in

the Inspector that work hand-in-hand with the Dynamic Zoom onscreen adjustment controls.

For more information on using the Dynamic Zoom controls, see Chapter 50, “Compositing

and Transforms in the Timeline.”

�Dynamic Zoom Ease: Lets you choose how the motion created by these controls accelerates.

You can choose from Linear, Ease In, Ease Out, and Ease In and Out.

�Swap: This button reverses the start and end transforms that create the dynamic zoom effect.

Composite

The Composite section of the Video Inspector panel

Composite modes can be used to combine clips that are superimposed over other clips in

the Timeline.

�Composite Mode: This selects the type of composite mode to combine the superimposed clips.

The default “Normal” means no compositing mode is applied.

For more information on Composite Modes, see Chapter 50, “Compositing and

Transforms in the Timeline.”

�Opacity: This slider makes a clip more or less transparent in addition to compositing

already being done.


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA

Lens Correction

The Lens Correction section of the Video Inspector panel

The Lens Correction group (only available in Resolve Studio) has two controls that let you correct

for lens distortion in the image, or add lens distortion of your own.

�Analyze: Automatically analyzes the frame in the Timeline at the position of the playhead for

edges that are being distorted by wide angle lens. Clicking the Analyze button moves the

Distortion slider to provide an automatic correction. If you’re analyzing a particularly challenging

clip, a progress bar will appear to let you know how long this will take.

�Distortion: Dragging this slider to the right lets you manually apply a warp to the image that lets

you straighten the bent areas of the picture that can be caused by wide angle lenses.

If you clicked the Analyze button and the result was an overcorrection, then dragging this slider to

the left lets you back off of the automatic adjustment until the image looks correct.

Retime and Scaling

The Retime and Scaling section of the Video Inspector panel

The Retime and Scaling group has four parameters that affect retiming quality and clip scale:

�Retime Process: Lets you choose a default method of processing clips in mixed frame rate timelines

and those with speed effects (fast forward or slow motion) applied to them, on a clip-by-clip basis.

The default setting is “Project Settings,” so all speed-effected clips are treated the same way.

There are three options: Nearest, Frame Blend, and Optical Flow, which are explained in

more detail in the Speed Effect Processing section of Chapter 51, “Speed Effects.”

�Motion estimation mode: When using Optical Flow to process speed change effects or clips with

a different frame rate than that of the Timeline, the Motion Estimation pop-up lets you choose

the best-looking rendering option for a particular clip. Each method has different artifacts, and

the highest quality option isn’t always the best choice for a particular clip. The default setting is

“Project Settings,” so all speed-effected clips are treated the same way. There are several options.

The “Standard Faster” and “Standard Better” settings are the same options that have been

available in previous versions of DaVinci Resolve. They’re more processor efficient and yield good

quality that are suitable for most situations. However, “Enhanced Faster” and “Enhanced Better”

should yield superior results in nearly every case where the standard options exhibit artifacts, at

the expense of being more computationally intensive, and thus slower on most systems.

�The “Standard Faster” and “Standard Better” settings are the same options that have been

available in previous versions of DaVinci Resolve. They’re more processor efficient and yield

good quality that are suitable for most situations. However, “Enhanced Faster” and “Enhanced


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA

Better” should yield superior results in nearly every case where the standard options exhibit

artifacts, at the expense of being more computationally intensive, and thus slower on

most systems.

�“Speed Warp Faster and “Speed Warp Better” are available for even higher-quality slow motion

effects using the DaVinci Neural Engine. Your results with this setting will vary according to

the content of the clip, but in ideal circumstances this will yield higher visual quality with fewer

artifacts than even the Enhanced Better setting.

�Scaling: Lets you choose how clips that don’t match the current project resolution are handled on

a clip-by-clip basis. The default setting is “Project Settings,” so that all mismatched clips use the

same method of being automatically resized.

However, you can also choose an individual method of automatic scaling for any clip.

The options are Crop, Fit, Fill, and Stretch; for more information see the 2D Transforms

section see Chapter 152, “Sizing and Image Stabilization.”

�Resize Filter: For clips that are being resized in any way, this setting lets you choose the filter

method used to interpolate image pixels when resizing clips. Different settings work better for

different kinds of resizing. There are four options:

Sharper: Usually provides the best quality in projects using clips that must be scaled up to fill a

larger frame size, or scaled down to HD resolutions.

Smoother: May provide higher quality for projects using clips that must be scaled down to fit an

SD resolution frame size.

Bicubic: While the Sharper and Smoother options are slightly higher quality, Bicubic is still an

exceptionally good resizing filter and is less processor intensive than either of those options.

Bilinear: A lower quality setting that is less processor intensive. Useful for previewing your work on a

low-performance computer before rendering, when you can switch to one of the higher quality options.

Other Resize Methods: A selection of specific resize algorithms is available if you need to match

them to other VFX workflows.

Super Scale

The Super Scale parameters

For instances when you need higher-quality upscaling than the standard Resize Filters allow, you

can now enable one of the “Super Scale” options in the Inspector. Unlike using one of the numerous

scaling options in the Edit, Fusion, or Color pages, Super Scale actually increases the source

resolution of the clip being processed, which means that clip will have more pixels than it did before

and will be more processor-intensive to work with than before, unless you optimize the clip (which

bakes in the Super Scale effect into the optimized media) or cache the clip in some way.

For more detailed information on Super Scale, see Chapter 11, “Image Sizing and Resolution

Independence.”


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA

Using Super Scale in the Inspector is functionally equivalent to setting the same controls for the

media clip in the Clip Attributes. This means that changing this setting affects all of the additional edits

referencing the selected media as well.

The Super Scale group has the following parameters that affect the quality and clip scale:

�Super Scale: Lets you choose the amount of scaling required. The options are 2-3-4x

and 2-3-4x Enhanced.

�Sharpness: Lets you choose the amount of detail in the scaling. This is limited to Low, Medium, or

High, unless the Super Scale mode is set to Enhanced, which allows you to apply variable

sharpness. You will want to balance this setting against Noise Reduction.

�Noise Reduction: Lets you choose the amount of noise reduction in the scaling. This is limited to

Low, Medium, or High, unless the Super Scale mode is set to Enhanced, which allows you to apply

variable noise reduction. You will want to balance this setting against Sharpness.

Audio

The Audio Inspector parameters

The Audio tab contains four commonly used audio

controls for video editing purposes, including

Clip Volume, Clip Pan, Clip Pitch, and Clip Equalizer.

Clip Volume: Each clip has a single volume control

that corresponds to the volume overlay over each

audio clip.

Clip Pan: (Only exposed for clips) A simple Pan

slider that controls stereo panning.

Clip Pitch: Lets you alter the pitch of a clip without

changing the speed. Two sliders let you adjust clip

pitch in semi tones (large adjustments, a twelfth of

an octave) and cents (fine adjustments, 100th of a

semi tone).

Equalizer

This six-band parametric equalizer has both

graphical and numeric controls for boosting or

attenuating different ranges of frequencies within

that clip, before it even gets to the EQ built into the

Mixer. Each band has controls for the filter type

(Bell, Lo-Shelf, Hi-Shelf, Notch), Frequency, Gain,

and Q-factor (sharpness of the band), with the

available controls for each band of EQ changing

depending on the filter type.

TIP: Clip EQ settings can be copied and pasted from one Clip EQ to another, and between

Clip EQ and Track EQ instances.


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA

Clip  EQ in the Audio Inspector

Master EQ Controls

The Equalizer window has the following overall controls located in the upper

right and left corners.

•	 Enable button: Turns the overall EQ effect off and on, without resetting the controls.

•	 Reset button: Resets all controls of the EQ window to their defaults.

Clip EQ Graph

This graph displays the current EQ curve with handles that correspond to each enabled

EQ band listed below. You can drag any numbered handle to boost or attenuate the range

of frequencies governed by that band, using whatever type of equalization that band has

been set to..

The Clip EQ graph with user-draggable handles

Dragging the numbered handles on this graph in turn modifies the parameters of the

corresponding band, and changing each band’s parameters will also alter the EQ graph,

which serves the additional purpose of providing a graphical representation of the

equalization being applied to that track.


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA

Bands 1 and 6

The outer two sets of band controls let you make high-pass and low-pass adjustments, if necessary.

�Band enable button: Turns each band of EQ on and off.

�Band filter type: Bands 1 and 6 can be switched among five specific filtering options for

processing the lowest or highest frequencies in the signal.

�For Band 1, these include (from top to bottom): Lo-Shelf, Bell, Notch, Hi-Shelf, and Hi-Pass.

�For Band 6, the options are (from top to bottom): Lo-Pass, Lo-Shelf, Bell, Notch, and Hi-Shelf.

�Freq: Adjusts the center frequency of the EQ adjustment.

�Gain: Adjusts the amount by which the affected frequencies are impacted. Negative values

attenuate those frequencies, while positive values boost those frequencies.

�Q Factor: This parameter adjusts the width of affected frequencies and appears whenever the

Bell option is selected. Lower values include a wider range of frequencies; higher values include a

narrower range of frequencies.

Bands 2 through 5

These band controls let you make a wide variety of equalization adjustments.

�Band enable button: Turns each band of EQ on and off.

�Band filter type: Offers four filtering options (from top to bottom): Lo-Shelf, Bell, Notch,

and Hi-Shelf.

�Frequency: Adjusts the center frequency of the EQ adjustment.

�Gain: Adjusts the amount by which the affected frequencies are altered. Negative values

attenuate those frequencies, while positive values boost those frequencies.

�Q Factor: This parameter appears when the Bell setting is selected. It adjusts the width of affected

frequencies. Lower values include a wider range of frequencies; higher values narrow the range of

frequencies.

NOTE: There are many more refined plugins and effects for audio clips in the Audio FX

library. If you apply any of these, the controls will appear in the Inspector’s Effects tab Audio

section, instead of here.


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA