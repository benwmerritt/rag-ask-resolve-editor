---
title: "Texture Pop (Studio Version Only)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 653
---

# Texture Pop (Studio Version Only)

Texture Pop is a more sophisticated and flexible version of the Midtone Detail control found in

the Primaries and HDR palette. Using the controls of this effect, you can either remove texture or

exaggerate it. There are two modes of operation that determine how specific a result you can achieve.

•	 In Simple mode, you can apply more extreme versions of the Midtone Detail effect found

in the Primaries and HDR palette. A single Details slider lets you soften or sharpen midtone

detail in the image with a greater range of operation, while a Strength slider lets you

exaggerate the effect further or attenuate the effect to back it off.

•	 In Advanced mode, you can fine-tune the softness or sharpness of high, medium, and

low-frequency image detail with great specificity via seven individual “details” sliders,

labeled Rough, Coarse, Medium, Small, Fine, and Tiny. This lets you adjust the textural

characteristics of multiple frequencies of image detail in different ways, for example

softening Fine detail while intensifying Medium detail. The Strength slider lets you

exaggerate or attenuate the overall effect caused by all sliders.

In either mode, the Details/Range sliders default to 0.000, which causes no change to the

image. This is the level to choose to preserve the original quality of detail in the image. They

range from -1.000 (maximum softening) to +1.000 (maximum sharpening). Additionally, a set of

Tonal Range controls (described later) lets you choose how much of this effect is applied to

the Shadows, Midtones, and Highlights of the image, giving you even more specific control

over which parts of the image are softened and/or sharpened.

Understanding Advanced Mode

Advanced mode is the most exciting way to use this effect. The best way to learn what Advanced

mode does is to set all of the Details sliders to -1.000, and then raise each one individually to see what

kind of image detail get reintroduced, and ultimately enhanced, if you raise each slider above 0.000. In

the following image, each of the Details sliders has been set to -1, which is the maximum smoothing for

each setting. The result is an image with minimal detail.

In the following example, a person and the mechanical details of a helicopter shot are smoothed by

setting each detail slider to -1.000. You can see that the resulting images both retain the broad strokes

of color and contrast that define each region of color, but outside of high-contrast edges, all textural

detail has been smoothed to a clean gradient.


Resolve FX Overview | Chapter 167 Resolve FX Texture

COLOR

(Previous page) An image of a person with all detail smoothed,

(Above) An image of mechanical detail with all detail smoothed

Then, by raising each of the Details sliders back to 0 or even +1 one at a time, you can see exactly

what kind of detail that slider is affecting. As you can see in the example of the person, the Tiny and

Fine sliders are affecting only the smallest details, hairs, lines, and pores of the skin. In the helicopter

detail, you can see the kind of small textures, tiny lines, and rivet details that come back.

(Top) The same image of the person with the Tiny and Fine sliders

raised to add subtle detail back to the image, (Bottom) The helicopter

detail with Tiny and Fine detail added back to the image


Resolve FX Overview | Chapter 167 Resolve FX Texture

COLOR

Here are two sets of generalizations that hold true if you’re thinking about the detail of a

human face.

•	 Tiny, Fine, and Small controls affect the smallest details in an image, including the pores

(tiny), blemishes (fine), and wrinkles (small) of average closeup shots. Other features affected

would include high-frequency edge detail of strands of hair, leaves on a tree, or text on a

page of paper or screen.

•	 Rough, Coarse, and Medium tend to affect progressively smaller shadow contouring of

faces, bodies, and objects.

Of course, the granularity of a particular type of image detail depends on how much of a

closeup or long shot the clip is. When the camera is closer to the subject being adjusted, you’ll

be able to adjust much finer details. When the camera is distant, then even large details on

the subject are affected by the Tiny, Fine, and Small controls. This means when you create an

adjustment for a subject in a closeup, you’ll need to make changes to the adjustment if you try

and apply it to a long shot.

Mode Controls

�Operating Mode: Lets you choose between the Simple and Advanced modes of this plugin.

�Color Mode: Lets you choose between working in RGB and Luma/Chroma mode. In RGB, a single

set of parameters affect all three color channels at once. In Luma/Chroma mode, two sets of

controls let you fine-tune the luma and the chroma separately.

�Output Mode: Lets you choose between outputting the Final Result, Differences mode, which lets

you see the effect differenced against the original image, and Difference Magnitude, which shows

a high-contrast differencing comparison.

Details Controls

�Strength: Lets you exaggerate the effect of the other Details sliders further, or attenuate the effect

to back it off.

�Details: (Simple mode only) Lets you soften or sharpen midtone detail in the image with a greater

range of operation.

�Rough/Coarse/Medium: (Advanced mode only) These three sliders affect progressively larger

contours of the image, appearing to affect the shadows and structure of the image.

�Small/Fine/Tiny: (Advanced mode only) These three sliders affect progressively smaller details

and texture of the image, adjusting medium to tiny details, lines, and specks.

Tonal Range Controls

�Shadows: Lets you reduce the effect you’ve created in the shadows of the image, as defined by

the Low Range parameter.

�Midtones: Lets you reduce the effect you’ve created in the midtones of the image, as defined by

the Low and High Range parameters.

�Highlights: Lets you reduce the effect you’ve created in the highlights of the image, as defined by

the High Range parameter.

�Low Range: Lets you define the image value that defines the transition from Shadows to Midtones.

�High Range: Lets you define the image value that defines the transition from Midtones

to Highlights.


Resolve FX Overview | Chapter 167 Resolve FX Texture

COLOR

Chapter 168

Resolve FX

Transform

The plugins in this category allow different types of animated and non-animated

transforms than are possible in the Sizing palette or Clip Transform controls

of the Inspector.

Contents

Match Move (Studio Version Only)����������������������� 3615

A Match Move Workflow������������������������������������������� 3615

Main Controls��������������������������������������������������������������� 3620

Tracking Controls������������������������������������������������������� 3620

Positioning����������������������������������������������������������������������� 3621

Compositing����������������������������������������������������������������� 3622

Stabilizing����������������������������������������������������������������������� 3622

Surface Tracker (Studio Version Only)�������������� 3623

Bounds����������������������������������������������������������������������������� 3624

Mesh���������������������������������������������������������������������������������� 3624

Track��������������������������������������������������������������������������������� 3625

Result�������������������������������������������������������������������������������� 3627

Using the Surface Tracker������������������������������������� 3629

Transform������������������������������������������������������������������������ 3637

General���������������������������������������������������������������������������� 3637

Position Controls�������������������������������������������������������� 3639

Image Adjustment����������������������������������������������������� 3639

Animation����������������������������������������������������������������������� 3639

Advanced Options����������������������������������������������������� 3639

Global Blend����������������������������������������������������������������� 3640

Video Collage�������������������������������������������������������������� 3640

Create Background��������������������������������������������������� 3640

Create Tile����������������������������������������������������������������������� 3641

Animating Tiles and Advanced Layouts��������� 3646

Video Collage Controls�������������������������������������������� 3647

Layout������������������������������������������������������������������������������ 3648

Margins and Spacing������������������������������������������������ 3648

Synchronize Keyframing����������������������������������������� 3648

Manage Tiles���������������������������������������������������������������� 3649

Mute Tiles���������������������������������������������������������������������� 3649

Custom Size/Shape��������������������������������������������������� 3649

Resize Content������������������������������������������������������������ 3650

Tile Styling��������������������������������������������������������������������� 3650

Drop Shadow��������������������������������������������������������������� 3650

Tile Animation���������������������������������������������������������������� 3651

Easing & Blur���������������������������������������������������������������� 3652

Global Blend����������������������������������������������������������������� 3652


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Match Move (Studio Version Only)

TIP: Match move workflows are now much more effectively accomplished in the Fusion page

using the tools and methods found there.

The Match Move filter is a patch-based tracker that follows a pattern region defined by a tracker

control. You can place as many trackers as you like by applying this filter to a node and clicking on a

feature you want to track in the Viewer. Ideal features for tracking are high contrast details that have

sharp angles that are clearly defined.

Each tracker control consists of (a) a center point that indicates where the tracked motion path will be

centered, (b) an inner box that identifies the patch of image you’re tracking (that can be resized), (c) an

outer box that defines the search region for the track (that can also be resized), and (d) a patch window

that shows you a zoomed in closeup of the patch you’re tracking. Patch windows can be resized, and

the other tracking controls hidden or shown, using controls in the Display Options section of the Match

Move controls.

A tracker control in the Match Move filter

If you’ve accidentally placed a tracker control somewhere you don’t want one, you can either drag

anywhere within the inner box to move it to another location, or you can Option-click it to delete

that tracker.

Once placed, you can choose how much image detail is considered for analysis by resizing that

tracker control. To resize a tracker, move the pointer over the edge of the inner box, and drag to shrink

or enlarge it.

This plugin will automatically derive as much motion data as the number of trackers you’ve

placed allows:

�One tracker tracks horizontal and vertical position (pan and tilt).

�Two or more trackers also track rotation.

�Four or more trackers also track perspective.

�If you place six or more trackers, then the Match Move filter is capable of automatically choosing

the best tracker data from the overall collection to give you the most accurate track that’s possible.

A Match Move Workflow

The following example shows the simplest complete workflow for importing a foreground clip to

composite with a match move to follow a background clip that’s already in the timeline. This workflow

is suitable for such operations as placing a graphic as a sign on a side of a building, or into the display

of a phone.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

To match move:


Open the Media Pool in the Edit page, right-click a clip you want to match move to a clip in the

Timeline, and choose “Add as Matte For Color Page Clip” to add it to the Color page Node Editor

of the currently selected clip as a Timeline Matte. This is currently the only way you can match

move and composite a foreground clip against a background clip in the Color page.


Open the Color page, make sure the background clip you want to match move to is selected, then

open the OpenFX library and drag the Match Move plugin directly onto the connection from the

last node in the tree to the Output, to add it as a stand-alone FX node.

Adding the Match Move filter as a stand-alone FX node


Right-click any corrector node in the node tree (Node 01 in this example) and choose the clip you

added in step 1 in the Add Matte > Timeline Mattes submenu of the contextual menu to expose

that clip as an Ext. Matte node. Delete the connection between the new Ext. Matte node and the

node it’s connected to, and then reconnect its RGB output to the second input of the FX node.

Connecting the foreground image to the second input of the FX node


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR


Select the FX node, make sure the OpenFX onscreen controls are enabled, choose whether

you want to start at the first or last frames of the clip to begin the tracking process, and then click

within the Viewer to place tracker controls on the surface of the image you’re going to attach the

foreground image to. If you want to do a perspective track, place at least four tracker patches in

areas you know won’t be occluded by other things in the frame. Choose features that are high

contrast and angular for the best results, and try to make sure the features you track won’t go

offscreen or be occluded by other features within the frame. As you place tracking controls, their

patch window will be tinted the color of the channel that DaVinci Resolve automatically determines

will provide the best tracking result.

Adding tracker controls to the feature you need to Match Move to


(Optional) If necessary, you can delete trackers you don’t want by Option-clicking them.


Now that your tracker controls are all set up, you’re ready to begin the tracking analysis. If the

playhead is at the beginning of the clip, click Track Forward, otherwise click Track Backward.

DaVinci Resolve will automatically analyze all tracker controls within the clip until the last frame of

the clip is reached.

Using the Tracking controls


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR


(Optional) If anything occludes a patch that’s being tracked, or if the tracked feature starts going

off the edge of the frame, that tracker control may veer off course and will eventually turn off. If this

happens, there’s a way to continue the track that’s surprisingly easy:

a)	 Click the Track Forward or Track Backward button again to stop the analysis.

b)	 Move the playhead back to the last good frame of tracking data, then click the inner box

of each tracker control that went wrong to make sure they’re turned on (you know it’s on if

the patch window is displayed), and then click “Clear tracking forward” or “Clear tracking

backward” as necessary to delete the incorrect tracking data. When you’re done, click the

inner box of each tracker that went wrong to turn it back off again, so it doesn’t continue trying

to track incorrectly (you know it’s off if the patch window is hidden).

c)	 Now, place additional trackers on different features of the same surface to replace the trackers

that you had to turn off.

Placing more tracking controls to cover for tracking controls that turn themselves

off when going offscreen or being occluded by other moving features in the image

d)	 Click “Track forward” again to continue the track, and DaVinci Resolve will automatically use

those additional features to continue the analysis.

e)	 When the analysis is complete, turn the trackers you disabled back on again. All trackers that

are turned on contribute data to the match move, for whichever ranges of frames they contain

valid tracking data.


When DaVinci Resolve finishes its analysis, move the playhead back to the first frame of the track,

and choose Positioning from the “Show controls for” pop-up menu. This takes you to the next

stage in the Match Moving process.

Choosing the Positioning controls


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR


A grid appears, covering the Viewer. This is the positioning canvas, and it lets you corner-pin the

area in which the foreground image you connected in step 3 will be composited and tracked.

You can corner-pin and resize it by dragging it by the corners, and you can move it by dragging

the center.

Resizing the canvas to fit the foreground image into the background

10	 Once you’ve positioned the grid, scrub back and forth to verify that it tracks correctly and looks

right once it’s in motion.

11	 Choose Compositing from the “Show controls for” pop-up menu to expose the

compositing controls.

12	 Set the Output pop-up menu to “Composite” to output the final match-moved composite. If

necessary, you can use the Composite Type and Plate Cropping controls to choose how the

foreground image is blended with the background and whether you need to crop unwanted parts

of the image from the edges.

The final match moved composite

At this point, you’ve finished the match move.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR