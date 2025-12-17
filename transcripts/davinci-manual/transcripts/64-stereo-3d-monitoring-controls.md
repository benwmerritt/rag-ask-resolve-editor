---
title: "Stereo 3D Monitoring Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 64
---

# Stereo 3D Monitoring Controls

To output both eyes to a stereo 3D display, you need to click the Vision: Mono or Stereo button, and

then choose a display mode from the Out pop-up menu.

Monitoring controls for Stereo 3D

�Vision: Click a button to choose between Stereo, where both eyes can be displayed in the Viewer

and output to video in a variety of different formats, and Mono, where only one eye is monitored in

the Viewer and your video output interface.

�Out: A pop-up menu that provides different stereo viewing options for previewing stereo 3D

signals in different ways. By default, this option is also linked to the Viewer display Internal Video

Scope options. For detailed descriptions of each stereo 3D viewing mode, see the following

section, “Stereo 3D Output Options.”

�Link button: When enabled, the Viewer and internal video scopes both use the Out pop-up

menu’s option for stereo 3D viewing. When disabled, you can choose different stereo 3D viewing

options for the Viewer and internal video scopes.

�Viewer: Lets you choose a stereo 3D viewing option for the Viewer.

�WFM: Lets you choose a stereo 3D viewing option for the internal video scopes.

�Cbd Size: If any stereo 3D viewing options are set to Checkerboard, this parameter becomes

enabled, and lets you define the size of the checkerboard boxes, in pixels.

Dual 4:2:2 Y’CbCr stereoscopic video streams are output via HD-SDI on selected Blackmagic I/O

devices when you turn on the ”Use left and right eye SDI output” checkbox on the Master Settings

panel of the Project Settings. You can select either Side-by-Side or Line-by-Line output to be fed

to your stereo-capable display, depending on your display’s compatibility.

Stereo 3D Output Options

Additionally, the Viewer and video scopes can be set to display both “eyes” in one of a variety of

different modes.

�Side by Side: Displays both images side by side. Each eye is squeezed anamorphically to fit both

eyes into the same resolution as the GUI viewer.

�Top and Bottom: Displays both images one over the other. Each eye is squeezed vertically to fit

both eyes into the same resolution as the GUI viewer.

�Line by Line (Even/Odd): An interlaced mode where each eye is displayed on alternating lines.

The thickness of the lines as seen in the Viewer depends on how zoomed in you are.

�Checkerboard: Displays both eyes via an alternating checkerboard pattern. This is an excellent

mode for identifying regions of the image where there’s variation in color or geometry between

the two eyes.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

�Anaglyph (B/W): Each eye is desaturated and superimposed via Red/Cyan anaglyph to show the

disparity between both eyes in different regions of the image. Left-eye divergence is red, and

right-eye divergence is cyan. Regions of alignment between both eyes appear grayscale.

Anaglyph modes are useful for evaluating the geometric differences between both eyes, as well

as for identifying the point of convergence (where both eyes align most perfectly) that places a

region of the image at the screen plane.

Red/cyan color coding also identifies the direction of parallax. For any given feature, disparity

such that red is to the right and cyan is to the left indicates positive parallax (backward projection

away from the audience). Red to the left and cyan to the right indicates negative parallax (forward

projection towards the audience).

�Anaglyph (Color): Similar to Anaglyph (B/W), except that regions of close alignment are shown

in full color. Incidentally, both anaglyph modes can be previewed on ordinary displays using

old-fashioned red/cyan anaglyph glasses, enabling stereo 3D monitoring on non-stereo

3D-capable displays.

�Difference: Superimposes grayscale versions of both eyes using the difference composite

mode. Corresponding left/right-eye pixels that are perfectly aligned appear black, while pixels

with disparity appear white. This mode is extremely useful for evaluating geometric differences

between both eyes, as well as for identifying the point of convergence, without the distraction of

color that the anaglyph modes present.

NOTE: Only displays the eye corresponding to the currently selected timeline in the Viewer.

However, this option also works in conjunction with the “Use Dual Outputs on SDI” checkbox

in the Master Settings of the Project Settings which, when turned on, outputs each eye to an

individual HD-SDI output of your Blackmagic I/O card.

The Viewer set to display an anaglyph stereo image in color

Floating Windows

Floating Windows are meant to correct for “Window violations,” where elements of the image with

negative parallax, that project forward from the screen plane towards the audience, are cut off by the

edge of the frame. In these instances, differences between the images being shown to the left and

right eyes can result in a visual paradox that’s difficult for viewers to reconcile. Specifically, when a

forward-projecting element is cut off by the left or right edge of the frame, one eye sees things that

the other eye does not.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

If the subject is moving quickly, this may not be an issue, but if the cut off (or occluded) element lingers

onscreen, it causes problems for viewers that defeat the stereo 3D illusion. The viewer’s binocular

vision (or stereopsis) is providing one depth cue, while occlusion is providing a completely different

depth cue.

To fix this, you can use Floating Windows to crop the cut off object from the eye on the side of the

object that’s cut off, thus eliminating the portion of the stereo image that is unseen to the other

eye that causes the problem.

Floating Window controls

The objective of using Floating Windows is to manipulate the illusion of the viewer’s “window into

the scene.” In addition to fixing Window violations, it has been proposed that Floating Windows

can be used as a creative tool by manipulating the geometry of this Window to alter subtly the

viewer’s perception of the screen orientation.

�By cropping the right-hand side of the right-eye frame, you also create the illusion that the right

edge of the “window into the image” is tilted farther forward toward the viewer.

�By cropping the left-hand side of the left-eye frame, you create the illusion that the left edge of the

Window is tilted toward the viewer.

�If you crop both the left-hand side of the left-eye frame and the right-hand side of the right-eye

frame, you create the illusion that the entire plane of the “virtual screen” is coming toward you.

�If you apply opposite-angled Windows to the left- and right-eye clips at one or both of the edges

of the frame, it appears to “tilt” the screen toward or away from the viewer.

Animating Floating Windows

Floating Windows can be animated using the Float Window keyframing track, found within the Sizing

track of the Keyframe Editor, to push the edge of the frame in as needed, and then pull it back out

when the partially occluded subject has moved fully into the frame.

For more information about animating keyframing tracks, see Chapter 148, “Keyframing in the

Color Page.”

Floating Windows have the following controls and parameters.

L/R/T/B buttons: Lets you choose an edge to which to apply a Floating Window. Click the

button corresponding to the edge you want to adjust. Each edge has its own position, rotate,

and softness settings.

Position: Adds masking to the currently selected edge.

Rotate: Rotates the currently selected edge, letting you create an angled Window.

Softness: Feathers the edge of the currently selected edge, letting you create a soft Window that can

be less noticeable to viewers.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

To add a Floating Window to fix a Window violation:


Choose to which eye you want to add the Floating Window.

�To apply a Floating Window to eliminate a Window violation on the right-hand side of the screen,

click the right eye view.

�To apply a Floating Window to eliminate a Window violation on the left-hand side of the screen,

click the left eye view.


Choose which edge you want to adjust by clicking the L or R buttons.

�To eliminate a Window violation on the right-hand side, click R.

�To eliminate a Window violation on the left-hand side, click L.


Adjust the Position parameter as necessary to crop the portion along the edge of the selected eye

that’s not visible in the other.


Optionally, if you feel that the Window adjustment you’ve just made is too obvious, increase the

Softness parameter to make that edge less noticeable.

Outputting Stereo 3D Media

in the Deliver Page

To render full frame media, you’ll need to render each stereo 3D eye separately using the controls of

the Deliver page, outputting whatever media format is required by the client.

Rendering Frame-Compatible Media

Frame-compatible media has both the left- and right-eye images squeezed anamorphically into a

single media file. To create frame-compatible media, choose the “Both eyes as” option from the

Render Stereoscopic 3D controls at the bottom of the File output options of the Deliver page, and then

choose a method of output from the Mesh Options pop-up menu.

Stereoscopic 3D mesh render options on the Deliver page

You can choose Side-by-Side, Line-by-Line, or Top-Bottom. You can also choose Anaglyph if you want

to output a traditional anaglyph red/cyan stereo 3D image for viewing on any display.

Rendering Individual Left- and Right-Eye Clips

If your workflow requires you to deliver separate sets of left- and right-eye media, this is easily

accomplished by either setting up a render job with “Render Stereoscopic 3D” set to either “Right eye”

or “Left eye,” or selecting “Both eyes as” and choosing the “Separate files” option.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Apple Spatial Video (MacOS only)

Recent models of Apple iPhone have a Spatial Video mode that creates 3D videos designed to be

viewed in a VR headset. These spatial videos are automatically recognized by DaVinci Resolve and

allow you to use all of DaVinci Resolve’s features, including the full 3D toolset described above.

Grading an Apple Spatial Video in the Color page using Anaglyph (B/W)

mode (not pictured: goofy 3D glasses on the colorist)

Using Apple Spatial Video in DaVinci Resolve

Spatial Video footage recorded on an iPhone is easily transferred into DaVinci Resolve but is only

available on the MacOS version.

To import iPhone Spatial Video footage into DaVinci Resolve:


On your iPhone, the camera mode must be turned to Spatial Video (not photo) before you record

the video.


Once the video is finished, find the video in the Photos app and press the Share icon.


Now export the spatial video via AirDrop or other method to your computer.


Open DaVinci Resolve and import the spatial video clips into the Media Pool as normal.


Properly imported spatial video clips will have a 3D icon automatically applied to their thumbnails.

Once imported, you can edit, color, audio mix, and create visual effects using all of DaVinci Resolve’s

toolset, just as if it were normal 3D footage.

Spatial Video clips imported correctly should

have a 3D icon applied on their thumbnails.


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA

Tips for using Apple Spatial Video in DaVinci Resolve:

•	 Currently Apple Spatial Video is required to be 1080p at 30fps. Ensure your

project settings match this.

•	 In the 3D tools in the Color page, make sure that the Left/Right eyes and

Convergence are linked.

When exporting a Spatial Video for playback in various VR headsets,

the Deliver page Video Settings should be:

•	 Format: QuickTime

•	 Codec: H.265

•	 Render Stereoscopic 3D: Both eyes as: MV-HEVC

Spatial Video export settings


Setup and Workflows | Chapter 15 Stereoscopic Workflows

MEDIA