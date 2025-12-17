---
title: "Conforming Projects to Stereo 3D Media"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 63
---

# Conforming Projects to Stereo 3D Media

Since DaVinci Resolve manages stereo via a single set of specially created stereo 3D clips, you can

use the same project import methods to import stereo 3D projects as you would for any other project.

Only a single imported timeline is necessary.

This also means that you can edit stereo projects in NLEs that aren’t otherwise stereo-aware, and

finish them in full stereo 3D in DaVinci Resolve. To do this, you need to make sure that you edit the

left-eye media in your NLE, and then export either an EDL or XML file to conform in DaVinci Resolve.

To conform an EDL to stereo 3D media:


Open the Media page, and create the necessary set of stereo 3D clips that will correspond to the

project you’re going to import, as described previously.

Open the Edit page, and then use the Import AAF/EDL/XML command to import your edit.


When the Load EDL/XML dialog appears, do the following:

�If importing an EDL, verify that the frame rate is correct, and click OK.

�If importing XML, make sure you turn off the “Automatically import source clips into

Media Pool” checkbox, since you want to relink the imported project to the stereo 3D clips you

created in step one.

The left-eye media timecode and reel information that’s embedded within each stereo 3D clip will

be used to conform the stereo 3D clips with the imported EDL, and you should be ready to work.

Grading Mastered Stereoscopic Media From Tape

If you’ve been handed a stereo 3D muxed tape with a mastered program that needs to be graded,

but you haven’t been given a project file or EDL, you can ingest it as individual left- and right-

eye media files with a supported VTR, such as HDCAM SR with 4:2:2 x 2 mode, by turning on the

“Use left and right eye SDI” checkbox in the Capture and Playback panel of the Project Settings.

When muxed stereoscopic signals are ingested, each eye is separated into individual left-eye and

right-eye image files

Once ingested, you can use Scene Detection to split the left-eye media in one bin, and to create an

EDL, you can use to split the right-eye media in the same way in another bin, so that you can create a

sequential set of stereo clips for grading.

Adjusting Clips Using the Stereo 3D Palette

Once you’ve either created or imported a stereoscopic 3D-identified timeline, you’re ready to begin

grading. The left eye will be displayed in the Edit and Color pages by default; however, you can

right-click on the Timeline and select Stereo 3D Mode to view the other eye. Most colorists work by

grading one eye first (typically the left), and rippling their grades to the other eye, making separate

adjustments to each eye’s clips when necessary to match undesirable variation between cameras.

DaVinci Resolve lets you do this automatically.

Setting up stereo 3D media enables the Stereo 3D palette on the Color page. This palette contains all

the controls necessary for working on stereoscopic projects. It provides controls for choosing which

eye to grade, adjusting convergence, swapping and copying grades and media between matching

left- and right-eye clips, auto-processing the color and geometry of left- and right-eye clips to match,

stereo 3D monitoring setup, and controls for floating windows.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Stereoscopic 3D palette

Your project must contain stereo 3D clips in order to open this palette.

For more information on setting up a stereo 3D project, see the “Creating Stereo 3D Clips

From Separate Files” section of this chapter.

Stereo Eye Selection

Most colorists work by grading one eye first (typically the left), and rippling their grades to the other

eye, making separate adjustments to each eye’s clips when necessary to match undesirable variation

between cameras.

The first three buttons in the Stereo 3D palette let you choose which eye to grade while you’re

working, as well as whether or not to ripple each clip’s grade to the matching opposite-eye

clip. Whenever you switch eyes, the 3D badge above each clip’s thumbnail changes color

(blue for right, red for left) and the thumbnails themselves update to show that eye’s media.

The Left eye is master

and ganged with the Right

•	 Left button: Displays the left-eye image and grade.

•	 Ripple Link button: When enabled (orange), all changes you make to the grade of the

currently selected eye are automatically copied to the correspondingly opposite eye.

When disabled (gray), grades made to the currently selected eye are made independently.

•	 Right button: Displays the right-eye image and grade.

You can also choose which eye you’re viewing and grading by right-clicking a clip’s thumbnail

and choosing Stereo 3D > Switch Eye or by choosing View > Switch Eye To > Left Eye or

Right Eye.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Using Ripple Link When Grading Stereo 3D Clips

You would turn Ripple Link off to suspend rippling when you want to make an individual adjustment

to the grade of one eye to obtain a better match between the two. When you’re finished matching the

two clips, you can turn it back on to resume automatic grade rippling.

Stereo 3D grade rippling is always relative, so differences between the grades that are applied to the

left- and right-eye clips are preserved. In fact, when you add or remove nodes to or from one eye,

the same nodes are automatically added to or removed from the corresponding clip it’s paired with,

regardless of whether or not Ripple Linked is enabled.

IMPORTANT: Regardless of whether or not Ripple Link is enabled, local versions created for

one stereo 3D-identified clip are automatically available to the paired timeline.

Stereo 3D Geometry Controls

The next group of parameters lets you adjust the geometry of stereo 3D clips. The Pan, Tilt, and

Zoom controls are provided as a convenience, and simply mirror the same parameters found in the

Transform palette’s Input mode, but made specific to the geometry of the left- and right-eye media.

Convergence, Pitch, and Yaw are the three parameters that are unique to the Stereo 3D palette.

Stereoscopic 3D Geometry controls

�Convergence: Adjusts the disparity between the left and right eyes, to define the point of

convergence (POC), or the region within the image where the left- and right-eye features are in

perfect alignment. If necessary, Convergence can be animated using the Stereo Format parameter

group in the Sizing track of the Keyframe Editor. If you want to adjust convergence in pixels, open

the Stereo 3D palette option menu, and turn on “Show convergence in pixels.”

Features that overlap perfectly in both right- and left-eye clips are at zero parallax, putting that

feature’s depth at the screen plane. Matching features that are divergent in the left- and right-

eye clips have increasingly positive parallax, and appear to be farther away from the audience.

Matching features that are divergent and reversed in the left- and right-eye clips have increasingly

negative parallax, and appear to be closer to the audience than the screen plane.

�Linked Zoom button: When enabled (white), both the left- and right-eye clips are automatically

zoomed whenever Convergence is adjusted so that both eyes always fill the screen. When

disabled (gray), changes to Convergence will cause the opposing left and right edges of each

eye’s clip to have blanking intrude.

�Pitch: Pivots the image around the horizontal center plane of the frame.

�Yaw: Pivots the image around the vertical center plane of the frame.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Sizing Repositioning in Stereo 3D

Generally, you’ll want to reposition stereo 3D clips with Ripple Link turned on, but you may

occasionally find yourself needing to make a manual adjustment to one eye in particular with Ripple

Link disabled. As with color adjustments, Sizing adjustments made with Ripple Link disabled are only

applied to the clip in the current Timeline. When Ripple Link is turned on, all Sizing adjustments are

automatically copied to the correspondingly numbered shot of the other stereo 3D timeline.

WARNING: It is not advisable to use the Rotate parameter when transforming stereo

3D clips. Geometrically, rotation tilts a stereo pair of clips inappropriately, and ruins the

“side by side” convergence that’s necessary to create the stereoscopic illusion.

Protecting Stereo Adjustments When Copying Grades

Each version of a grade has independent stereo adjustments stored along with the Sizing settings.

To prevent accidental overwrite of convergence and alignment data when copying grades from

one clip to another, you can right-click within the Gallery and choose one of the following options to

turn them on:

�Copy Grade: Preserve Convergence

�Copy Grade: Preserve Floating Windows

�Copy Grade: Preserve Auto Align

When enabled, these options let you overwrite a clip’s grade without overwriting specific

Stereo 3D parameters.

TIP: Stereo 3D and Sizing settings are processed before node-based corrections in the

DaVinci Resolve image processing pipeline.

Swap and Copy Controls

Another set of controls at the right of the Stereo 3D palette lets you swap and copy grades, and swap

clips, in situations where you need to reverse what’s applied to a pair of left- and right-eye clips.

Swap and Copy grades between eyes

�Swap Grade: Exchanges the grades that are applied to the left- and right-eye clips.

�Swap Shot: A checkbox that, when enabled, switches the actual media used by two

corresponding left- and right-eye clips. Useful in situations where the eyes of a stereo

3D clip were mislabeled, and you want to switch the clips without rebuilding both EDLs.

�Copy Right to Left: Copies the right-clip grade to the corresponding left-eye clip.

�Copy Left to Right: Copies the left-clip grade to the corresponding right-eye clip.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Batch Grade Management for Stereo 3D Projects

There are also a series of batch-processing commands that are useful for stereoscopic grading that

are available when you right-click one or more selected clips in the Thumbnail timeline:

�Stereo 3D Batch Copy: Copies every grade from the left-eye clips to the right-eye clips.

�Stereo 3D Batch Sync: Copies grades from one eye to the other only when their node graphs

have the same number of nodes. This prevents you from accidentally overwriting a custom grade

with a different node structure that was necessary to match two eyes for a problem shot.

The Copy Grade, Swap Grade, Swap Shots, Ripple Link, and Switch Eye commands are also available

from the Stereo submenu of the Timeline contextual menu.

Automatic Image Processing for Stereo 3D

It’s common during stereoscopic shoots for minor divergences in geometry and color to appear in

the source footage. To make the process of grading stereo 3D media less onerous, DaVinci Resolve

provides a set of auto-adjustment controls at the right of the Stereo 3D palette that gives you a starting

point for matching left- and right-eye clips together.

Auto align and color match buttons

Options for Auto Processing

You can choose which frame should be used to automatically analyze and process stereo clips using

the Alignment and Matching controls from the Stereo 3D palette option menu. You can choose Auto

Process > First or Middle, depending on what works best for your media.

Auto Process—Stereo Alignment

For the stereoscopic effect to work without causing headaches, it’s critical that both eyes are aligned.

This can be tricky to adjust using manual controls, but is something that can be automatically analyzed.

You can perform stereo 3D alignment to a single clip, or you can select a range of clips to align all of

them automatically at once. There are two options. Which is more appropriate depends on the type of

geometry issues you’re needing to address.

�Transform Alignment: Analyzes the image and makes vertical and rotational adjustments to line

up the left- and right-eye images as closely as possible.

�Vertical Skew: Analyzes the images and makes a vertical-only adjustment to line up the left- and

right-eye images.

To align one or more clips automatically:


Select one or more stereo clips in the Thumbnail timeline of the Color page.


Choose which frame of each clip you want to use for the analysis by opening the Stereo 3D

palette, clicking the Option menu, and choosing Auto Process > First or Auto Process > Middle.


Click either of the Stereo Alignment buttons. The button to the left is for Automatic Transform,

while the button to the right is for Automatic Vertical Skew.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

If you selected multiple clips, then the Stereo Alignment window appears, and a progress bar shows

the remaining time this operation will take.

Auto Process—Color Matching

Due to the design of different stereo 3D rigs, sometimes the color and contrast of one eye’s media

doesn’t precisely match that of the corresponding eye. DaVinci Resolve provides two commands for

quickly and automatically matching two eyes together.

�Stereo Color Match (Primary Controls): Uses the Lift/Gamma/Gain controls to match one eye to

the other. The result is a simple adjustment that’s easy to customize, but may not work as well as

Custom Curves in some instances.

�Stereo Color Match (Custom Curves): Uses the Custom Curves to create a multipoint adjustment

to match one eye to the other. The result can be more effective with challenging shots.

�Stereo Color Match (Dense Color Match): Performs a pixel by pixel, frame by frame color match

that is incredibly accurate. This operation is processor intensive, so if you’re going to batch

process many clips, or if you’re matching long clips, you’ll want to make sure you have adequate

time. Because this is so precise match, it’s recommended to use Dense Color Match after you’ve

used one of the stereo alignment commands.

TIP: For the best results, it’s recommended to use automatic color matching in a separate

node, independent of other corrections.

Stereo 3D color match works differently depending on whether or not one of the stereo 3D-paired

clips has already been graded. The following procedure shows how to match a pair of left- and right-

eye clips before you make any manual adjustments of any kind.

To match a pair of left- and right-eye clips automatically:


Select one or more clips in the Thumbnail timeline of the Color page.


Open the Stereo 3D palette, and click one of the three Color Match controls.

The Color Matching window appears, and a progress bar shows the remaining time this operation

will take. You can also use automatic color matching to match an ungraded clip to a paired clip that’s

already been graded. This only works for grades consisting of one or more primary corrections;

secondary corrections cannot be auto-matched.

To match an ungraded clip automatically to a paired stereo clip that’s graded:


To suspend stereo grade linking temporarily:

�Open the Stereo 3D palette, and turn off the Ripple Link button.

�Right-click the Thumbnail timeline, and choose Stereo 3D > Ripple Link > Solo.


Make a primary adjustment to a clip in the left-eye timeline to create a simple base grade.

The left-eye clip now has a grade, and the right-eye clip does not.


Do one of the following to switch eyes:

�In the Stereo 3D palette, click Right.

�Right-click the Thumbnail timeline again, and choose Stereo 3D > Switch Eye.

This procedure only works when you use the Stereo Color Match commands on the ungraded clip

of a left- and right-eye stereo pair, to match it to the graded clip.


To make the match, do the following:

In the Stereo 3D palette, click one of the three color match controls. Both clips should match one

another very closely.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA