---
title: "Cropping"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 196
---

# Cropping

The Video Inspector has an additional set of cropping parameters:

Crop Left, Right, Top, and Bottom: Lets you cut off, in pixels, the four sides of the image. Cropping a

clip creates transparency, so that whatever is underneath shows through.

Softness: Lets you blur the edges of a crop. Setting this to a negative value softens the edges inside of

the crop box, while setting this to a positive value softens the edges outside of the crop box.

Dynamic Zoom

The Dynamic Zoom controls, which are off by default, make it fast and easy to do pan and scan effects

to zoom into or out of a clip. Also, if you import a project from Final Cut Pro X with clips that use the

Ken Burns effect, then those clip’s effects will populate the Dynamic Zoom parameters in DaVinci

Resolve. Turning the Dynamic Zoom group on activates two controls in the Inspector that work hand-

in-hand with the Dynamic Zoom onscreen adjustment controls you can expose in the Timeline Viewer

(described below):

Dynamic Zoom Ease: Lets you choose how the motion created by these controls accelerates.

You can choose from Linear, Ease In, Ease Out, and Ease In and Out.

Swap: This button reverses the start and end transforms that create the dynamic zoom effect.

Stabilization

Image Stabilization is available for clips right in the Timeline. These controls let you smooth out or even

steady unwanted camera motion within a clip. The analysis is performed in such a way as to preserve

the motion of individual subjects within the frame, as well as the overall direction of desirable camera

motion, while correcting for unsteadiness.

These are the same stabilizer controls found in the Color page’s Tracker palette (minus the tracker

graph), and the resulting stabilization analysis is mirrored on the Color page, where you can see the

data visualized on the graph, if necessary.

A pop-up menu provides three different options that determine how the selected clip is analyzed and

transformed during stabilization. You must choose an option first, before clicking the Stabilize button

above, because the option you choose changes how the image analysis is performed. If you choose

another option, you must click the Stabilize button again to reanalyze the clip.

Perspective: Enables perspective, pan, tilt, zoom, and rotation analysis and stabilization.

Similarity: Enables pan, tilt, zoom, and rotation analysis and stabilization, for instances where

perspective analysis results in unwanted motion artifacts.

Translation: Enables pan and tilt analysis and stabilization only, for instances where only X and Y

stabilization gives you acceptable results.

Stabilization controls found in the Edit

page Inspector for each clip


Editing Effects and Transitions | Chapter 50 Compositing and Transforms in the Timeline

EDIT

The other controls let you customize how aggressively the selected clip is stabilized.

Stabilization Toggle: The toggle control for the Stabilization controls lets you turn stabilization off and

on to be able to compare the stabilized and unstabilized image.

Camera Lock: Turning on this checkbox disables Cropping Ratio and Smooth, and enables the

stabilizer to focus on eliminating all camera motion from the shot in an effort to create a locked shot.

Zoom: When this checkbox is turned on, the image is resized by a large enough percentage

to eliminate the blanking (black edges) that is the result of warping and transforming the image

to eliminate unwanted camera motion. The lower a value Cropping Ratio is set to, the more

DaVinci Resolve will need to zoom into an image to eliminate these blanked edges. If you turn this

off, the image is not zoomed at all, and whatever blanking intrudes into the image is output along with

the image, on the assumption that you’ll have dedicated compositing artists deal with eliminating this

blanking by filling in the missing image data in a more sophisticated manner. You may also leave this

checkbox turned off if you’re planning on animating the Input Sizing Zoom parameter to dynamically

zoom into and out of a shot being stabilized to eliminate blanking only where it occurs, using only as

much zooming as is necessary for each region of the shot.

Cropping Ratio: This value limits how hard the stabilizer tries to stabilize, by dictating how much

blanking or zooming you’re willing to accept in exchange for eliminating unwanted motion. A value

of 1.0 results in no stabilization being applied. Progressively lower values enable more aggressive

stabilization. Changing this value requires you to click the Stabilize button again to reanalyze the clip.

Smooth: Lets you apply mathematical smoothing to the analyzed data used to stabilize the clip,

allowing camera motion in the shot while eliminating unwanted jittering. Lower values perform less

smoothing, allowing more of the character of the original camera motion to show through, while higher

values smooth the shot more aggressively. Changing this value requires you to click the Stabilize

button again to reanalyze the clip.

Strength: This value is a multiplier that lets you choose how tightly you want to use the stabilization

track to eliminate motion from a shot using the current analysis. With a value of 1, stabilization is

maximized. Since some clips might look more natural with looser stabilization, choosing a number

lower than 1 lets a percentage of the original camera motion show through. Zero (0) disables

stabilization altogether. As an additional tip, you can invert the stabilization by choosing –1 when

pasting a stabilization analysis from another clip to perform a match move based on the overall motion

of the scene, and you can use a negative value either lower than 0 or higher than –1 to under or

overcompensate when inverting the stabilization, simulating the effects of parallax where foreground

and background planes move together but at different speeds.

Lens Correction

The Lens Correction group (only available in Resolve Studio) has two controls that let you correct for

lens distortion in the image, or add lens distortion of your own.

Analyze: Automatically analyzes the frame in the Timeline at the position of the playhead for edges

that are being distorted by wide angle lens. Clicking the Analyze button moves the Distortion slider to

provide an automatic correction. If you’re analyzing a particularly challenging clip, a progress bar will

appear to let you know how long this will take.

Distortion: Dragging this slider to the right lets you manually apply a warp to the image that lets you

straighten the bent areas of the picture that can be caused by wide angle lenses. If you clicked the

Analyze button and the result was an overcorrection, then dragging this slider to the left lets you back

off of the automatic adjustment until the image looks correct.


Editing Effects and Transitions | Chapter 50 Compositing and Transforms in the Timeline

EDIT

Retime and Scaling

The Retime and Scaling group has four parameters that affect retiming quality and clip scale:

Retime Process: Lets you choose a default method of processing clips in mixed frame rate timelines

and those with speed effects (fast forward or slow motion) applied to them, on a clip-by-clip basis.

The default setting is “Project Settings,” so all speed-effected clips are treated the same way. There

are three options: Nearest, Frame Blend, and Optical Flow, which are explained in more detail in the

Speed Effect Processing section see Chapter 51, “Speed Effects.”

Motion estimation mode: When using Optical Flow to process speed change effects or clips with

a different frame rate than that of the Timeline, the Motion Estimation pop-up lets you choose the

best-looking rendering option for a particular clip. Each method has different artifacts, and the highest

quality option isn’t always the best choice for a particular clip. The default setting is “Project Settings,”

so all speed-effected clips are treated the same way. There are several options. The “Standard Faster”

and “Standard Better” settings are the same options that have been available in previous versions of

DaVinci Resolve. They’re more processor-efficient and yield good quality that are suitable for most

situations. However, “Enhanced Faster” and “Enhanced Better” should yield superior results in nearly

every case where the standard options exhibit artifacts, at the expense of being more computationally

intensive, and thus slower on most systems. The Speed Warp setting is available for even higher-

quality slow motion effects using the DaVinci Neural Engine. Your results with this setting will vary

according to the content of the clip, but in ideal circumstances this will yield higher visual quality with

fewer artifacts than even the Enhanced Better setting.

Scaling: Lets you choose how clips that don’t match the current project resolution are handled on

a clip-by-clip basis. The default setting is “Project Settings,” so that all mismatched clips use the

same method of being automatically resized. However, you can also choose an individual method of

automatic scaling for any clip. The options are Crop, Fit, Fill, and Stretch; for more information see the

2D Transforms section of Chapter 149, “Sizing and Image Stabilization.”

Resize Filter: For clips that are being resized in any way, this setting lets you choose the filter method

used to interpolate image pixels when resizing clips. Different settings work better for different kinds of

resizing. There are four options:

�Sharper: Usually provides the best quality in projects using clips that must be scaled up to fill a

larger frame size, or scaled down to HD resolutions.

�Smoother: May provide higher quality for projects using clips that must be scaled down to fit an

SD resolution frame size.

�Bicubic: While the Sharper and Smoother options are slightly higher quality, Bicubic is still an

exceptionally good resizing filter and is less processor intensive than either of those options.

�Bilinear: A lower quality setting that is less processor intensive. Useful for previewing your work

on a low-performance computer before rendering, when you can switch to one of the higher

quality options.

�Other Resize Methods: A selection of specific resize algorithms is available if you need to match

them to other VFX workflows.


Editing Effects and Transitions | Chapter 50 Compositing and Transforms in the Timeline

EDIT

Onscreen Controls for Transform,

Crop, and Dynamic Zoom

You also have the option of transforming, cropping, or adding dynamic zoom effects to clips using

the Transform/Crop/Dynamic Zoom button at the bottom left of the Timeline Viewer. These on-screen

controls can also be selected by choosing an option from the View > Viewer Overlay submenu; these

commands are not mapped to keyboard shortcuts by default, but you can make a manual mapping if

there’s a mode you find yourself using regularly. The currently selected overlay can be toggled on and

off by pressing Shift-` (Tilde), or by choosing View > Viewer Overlay > Toggle On/Off.

Transform controls in the Timeline Viewer

Object Snapping in the Viewer

While dragging objects or dynamic zoom outlines to reposition them, snapping occurs at the X and Y

center of the frame, as well as around the outer third of the frame. Holding the Shift key down while

dragging a text object constrains movement to just the X or Y axis.

Using Onscreen Controls

For many, the onscreen controls provide a more intuitive experience for manipulating your clips.

To transform a clip using graphical controls in the Timeline Viewer:


Click the Transform/Crop button at the bottom left of the Timeline Viewer to turn it on; white is

enabled, gray is disabled. When enabled, if no clips are selected in the Timeline, then the clip in

the highest auto-select-enabled track that intersects the playhead will display onscreen transform

controls. If a clip is selected, that specific clip can be transformed.


Do one of the following:

a)	 Choose the Transform mode from the pop-up menu, if necessary, to change modes.

The appropriate onscreen controls appear to let you manipulate the clip with the mouse.

When in Transform mode, you can drag anywhere within the clip’s bounding box to adjust pan

and tilt, drag any diagonal corner to proportionally resize, drag any side to squeeze or stretch

just width or height, or drag the center handle to rotate.


Editing Effects and Transitions | Chapter 50 Compositing and Transforms in the Timeline

EDIT

Onscreen controls for transforming in the Timeline Viewer

b)	 Choose the Cropping mode from the pop-up menu. In this mode, each side has a

handle for cropping.

Onscreen controls for cropping in the Timeline Viewer


Editing Effects and Transitions | Chapter 50 Compositing and Transforms in the Timeline

EDIT

c)	 Choose the Dynamic Zoom mode from the pop-up menu. In this mode, the green box shows

the starting size and position of the animated transform, while the red box shows the ending

size and position of the animated transform. Drag anywhere within either bounding box to

adjust pan and tilt for either the start or the end of the animated effect, and drag any of the

corners to adjust the size. A motion path appears to show the motion that’s being created.

Adjusting the Dynamic Zoom controls automatically enables dynamic zoom in the Inspector.

Onscreen controls for transforming and cropping in the Timeline Viewer


If necessary, choose a smaller viewing percentage from the Timeline Viewer scale pop-up to

better see the onscreen controls if you’re rescaling the image, or use the scroll control of your

mouse, trackpad, or tablet to zoom out of the image.


When you’re finished, turn the Transform/Crop/Dynamic Zoom button off.


Editing Effects and Transitions | Chapter 50 Compositing and Transforms in the Timeline

EDIT