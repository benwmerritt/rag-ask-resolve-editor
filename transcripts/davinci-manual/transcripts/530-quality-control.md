---
title: "Quality Control"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 530
---

# Quality Control

Lastly, it’s important to keep in mind that, for all the creative possibilities that DaVinci Resolve affords,

it’s still important that the final deliverables that you give to your client has appropriate signal levels

relative to their requirements. In particular, programs destined for broadcast have specific outer

boundaries of luma and chroma that you must not exceed, or you’ll risk having a show rejected for QC

(quality control) violations.

However, even if you’re not delivering a show for broadcast, it’s important to be aware of the

mathematical limitations of a digital video signal to make sure you’re not clipping or crushing image

detail through overzealous adjustments that you may, in fact, want to preserve.

For example, if you take a look at the next two images, you can see the perils of overzealous

adjustments when compared to a clip that, while graded creatively, has been adjusted with respect to

the mathematical boundaries of image data.

Image graded to preserve detail in highlights

Image graded with highlight detail blown out

Here, too, DaVinci Resolve provides tools designed to help you exercise control over the fine-tuning

of the image. A Video Scopes window provides the standard Waveform, Parade, Vectorscope, and

Histograms that are used to analyze your image data. These scopes let you see the boundaries of

what’s possible, and make it easy to spot subtle problems, and compare the characteristics of one

image to another.

Video scopes


Color | Chapter 125 Introduction to Color Grading

COLOR

When the time comes that you want to start clipping data in the highlights and shadows, as part of

a creative look, the Soft Clip controls let you introduce a subtle or large roll-off, compressing the

extremes of the signal so that what clipping you do is softer and more pleasing.

For more information about the video scopes and the Soft Clip controls, see Chapter 124,

“Using the Color Page.” and see Chapter 132, “Curves.”

Never Stop Experimenting

So now that you’ve gotten an extremely brief overview of the grading process as seen through

the toolset of DaVinci Resolve, we invite you to use this manual to explore DaVinci Resolve more

thoroughly. You may discover that, the more you work with the different features that are available, the

more unexpected uses you’ll find for different controls that you thought you knew well.

Have fun.


Color | Chapter 125 Introduction to Color Grading

COLOR

Chapter 126

Using the Color Page

Given the origin of DaVinci Resolve as a professional grading application,

the Color page is at the heart of the DaVinci Resolve experience.

Within the Color page are all of the controls available for manipulating color and contrast, reducing

noise, creating limited secondary color corrections, building image effects of different kinds, adjusting

clip geometry, and making many other corrective and stylistic adjustments.

In this chapter, you’ll learn how to understand the Color page interface, how to customize it, and how

to work within it to play through and navigate your project’s timeline. You’ll also learn how to analyze

and compare clips in preparation for grading using stills, playheads, and DaVinci Resolve’s own

internal video scopes.

Contents

The Color Page Interface�������������������������������������������������������������������������������������������������������������������������������������������������������������� 2966

The Interface Toolbar����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2966

Showing Which Panel Has Focus���������������������������������������������������������������������������������������������������������������������������������������������� 2967

Viewer����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2967

Gallery����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2970

LUT Browser����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2970

Media Pool�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2972

Node Editor������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2973

Timeline�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2973

Palette Area������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2975

Dual-Monitor Layout������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2978

The Info Palette and Clip Information������������������������������������������������������������������������������������������������������������������������������������� 2979

Clip Info��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2979

System Info�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2980

Clip Details�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2980

Customizing the Color Page��������������������������������������������������������������������������������������������������������������������������������������������������������� 2981

Undo and Redo in DaVinci Resolve����������������������������������������������������������������������������������������������������������������������������������������� 2982


Color | Chapter 126 Using the Color Page

COLOR

The Color Page Interface

The Color page is divided into seven main areas that work together to let you build a grade. This

section provides an overview of what these areas are and how they function.

The default layout of the Color page

The Interface Toolbar

At the very top of the Color page is a toolbar with buttons that let you show and hide different parts of

the user interface. These buttons are as follows, from left to right:

The Interface toolbar

Gallery: Opens and closes the Gallery panel.

LUTs: Opens and closes the LUT Browser.

Media Pool: Opens and closes the Media Pool.

Clips: Opens and closes the Thumbnail timeline. To the right is a drop-down

menu that lets you choose a timeline filtering option for the Thumbnail timeline.

Quick Export: Opens the Quick Export window.


Color | Chapter 126 Using the Color Page

COLOR

Timeline: Opens and closes the Mini-Timeline.

Nodes: Opens and closes the Node Editor.

Open FX: Opens and closes the Open FX panel.

Lightbox: Opens and closes the Lightbox.

Showing Which Panel Has Focus

Whenever you click somewhere on the DaVinci Resolve interface using the pointer, or use a keyboard

shortcut to “select” a particular panel (such as in the Edit page), you give that panel of the user

interface “focus.” A panel with focus will capture specific keyboard shortcuts to do something within

that panel, as opposed to doing something elsewhere in the interface. A highlight appears at the top

edge to show you which panel has focus so that you can keep track of which part of the current page

is taking precedence, and you can switch focus as necessary to do what you need to do. You can

turn the Focus Indicator on and off in Preferences > User > UI Settings > Show focus indicators in the

user interface.

The focus indicator shown at the top edge of the Media Pool, shown next to a Viewer that doesn’t have focus

Viewer

The Viewer shows the frame at the current position of the playhead in the Timeline. At the top of the

Viewer is a header that displays the Project and Timeline names, as well as a Viewer Timecode display

that shows the source timecode of each clip by default. The Timeline name is also a drop-down

display that lets you switch to any other timeline in the project. A scrubber bar underneath the image

lets you drag the playhead across the entire duration of the clip, while transport controls underneath

that let you control playback. A toolbar at the top provides controls governing Image Wipes,

Split‑Screen controls, and Highlight display. Additional controls let you loop playback, switch Unmix

mode on and off, turn audio playback on and off, and choose which onscreen controls are currently

displayed. More information about using the Viewer appears later in this chapter.


Color | Chapter 126 Using the Color Page

COLOR

The default Viewer with transport controls

You can also put the Viewer into one of three alternate modes to be able to see a larger image as

you work. All three of these modes are available from the Workspace > Viewer Mode submenu.

�Enhanced Viewer: (Option-F to toggle this on and off) hides everything to the left and right of the

Viewer, giving you a large working area for tasks such as window positioning and rotoscoping,

while keeping the palettes and their controls visible as you work.

The Color page in Enhanced Viewer mode


Color | Chapter 126 Using the Color Page

COLOR

�Full Screen Viewer: (Shift-F to toggle this on and off) is available to provide more working area for

tasks such as window positioning and rotoscoping. Full Screen Viewer also lets you display the

Effects panel at full height, and you can turn the Node Editor on and off to access different effects

controls while you work.

The Color page in Full Screen Viewer mode

�Cinema Viewer: (P to toggle this on and off) expands the Viewer to fill your workstation’s entire

monitor. This is useful if you want to play the current Timeline without any distractions. When

you move the pointer over the image, transport controls and a jog bar appear to let you control

playback. For DITs, a contextual menu is available by right-clicking anywhere on the image with

which you can turn on and customize a video scope overlay (which can be dragged to different

locations on the Viewer).

The Color page in Cinema Viewer mode


Color | Chapter 126 Using the Color Page

COLOR