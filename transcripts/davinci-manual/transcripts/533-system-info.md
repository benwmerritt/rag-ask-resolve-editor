---
title: "System Info"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 533
---

# System Info

The second tab displays information about operational modes currently in use by DaVinci Resolve.

It’s meant to provide the status of different DaVinci Resolve features that can be enabled, disabled, or

cycled among various options. This information includes:

Clips

The total number of clips in the Timeline.

Proxy

The status of Proxy mode (On or Off).

Clip Cache

The status of the Clip Cache mode (Off, All, Dissolves, User, User & D).

Ref Transform

The status of Reference Still reposition.

Ref Mode

The status of the Reference mode (Gallery, Timeline, Offline).

Wipe Style

The currently selected Wipe Style for split screens (Wipe-H, Wipe-V,

Wipe-M, Wipe-A).

Convergence

The current Convergence setting (Linked Zoom, Opposite)

Stereo Grade

The currently displayed Eye and Gang mode (Left or Right - Gang or Solo).

Stereo Display

The current Stereo Display mode (Mono or Stereo).

Clip Details

You can right-click the currently selected clip in the Thumbnail Timeline and choose View Clip Details

to show a small window with all of that clip’s information available at a glance. You can drag this

window anywhere you like, even to another display.

The Clip Details window


Color | Chapter 126 Using the Color Page

COLOR

This information is not editable, but is provided for easy reference, and includes:

File Name

The name of the media file on disk appears at top.

Start Timecode

The source timecode value of the first frame in the clip.

End Timecode

The source timecode value of the last frame in the clip.

Duration

The duration of the clip, in timecode.

Frames

The duration of the clip, in frames.

Reel Name

The reel name of that clip, if one is being read properly.

Version

The name of the remote or local version used by that clip.

Format

The format used by the source clip, along with the frame size and bit depth.

Codec

The codec used by the source clip.

Folder

Which directory on disk the source media resides in.

Description

The description field of the Metadata Editor.

Comments

The Comments field of the Metadata Editor.

EDL Comments

EDL comments for that event, if any exist.

Customizing the Color Page

The various sections of the Color page can be resized, hidden, and rearranged as needed to

accommodate different working styles. This section covers all of the methods that are available for

Color page customization.

You can easily resize the Viewer, Gallery, and Nodes Editor relative to one another to make the

Viewer larger, expand the width of the Node Editor to have more workspace, or to create more or less

room for stills in the Gallery.

To resize the Viewer, Gallery, and Node Editor:

Move the pointer over the vertical divider between any two areas. When the resize icon appears, drag

the divider to the left or right to make one area larger while making the other smaller.

You can also fully expand the Gallery, the Memories, the Node Editor, and the Keyframe Editor to replace

completely whichever interface area is adjacent.

To expand the Keyframe Editor, Viewer, and Gallery:

Click the Expand control at the upper right of whichever interface area you want to expand. Once

expanded, clicking the Expand control again will collapse that interface area back to its original size,

revealing whatever was hidden.

In Display mode, you can completely hide the Viewer, pushing the Gallery all the way to the right side of

the DaVinci Resolve window, and expanding the Node Editor to take the rest of the space.


Color | Chapter 126 Using the Color Page

COLOR

To toggle Display mode:

Right-click in the empty area of the Node Editor, and choose Toggle Display Mode from the contextual

menu. Do this again to toggle Display Mode off and return the interface to the way it was.

To show and hide the Mini-Timeline:

Click the Timeline button at the right of the palette button bar.

To show and hide the Color page Viewer upper toolbar:

Click the Viewer option menu and choose Show Viewer Options to uncheck it.

To return all pages to their default layout:

Choose Workspace > Reset UI Layout.

Undo and Redo in DaVinci Resolve

No matter where you are in DaVinci Resolve, Undo and Redo commands let you back out of steps

you’ve taken or commands you’ve executed, and reapply them if you change your mind. DaVinci

Resolve is capable of undoing the entire history of things you’ve done since creating or opening a

particular project. When you close a project, its entire undo history is purged. The next time you begin

work on a project, its undo history starts anew.

Because DaVinci Resolve integrates so much functionality in one application, there are three

separate sets of undo “stacks” to help you manage your work.

•	 The Media, Cut, Edit, and Fairlight pages share the same multiple-undo stack, which lets

you backtrack out of changes made in the Media Pool, the Timeline, the Metadata Editor,

and the Viewers.

•	 Each clip in the Fusion page has its own undo stack so that you can undo changes you

make to the composition of each clip, independently.

•	 Each clip in the Color page has its own undo stack so that you can undo changes you make

to grades in each clip, independently.

In all cases, there is no practical limit to the number of steps that are undoable (although there

may be a limit to what you can remember). To take advantage of this, there are three ways you

can undo work to go to a previous state of your project, no matter what page you’re in.

To simply undo or redo changes you’ve made one at a time:

�Choose Edit > Undo (Command-Z) to undo the previous change.

�Choose Edit > Redo (Shift-Command-Z) to redo to the next change.


Color | Chapter 126 Using the Color Page

COLOR

Chapter 127

Viewers, Monitoring,

and Video Scopes

Viewers let you see what you’re working on, provide a UI for transport controls

and image comparison, draw windows and drag on-screen controls, and provide a

variety of warnings and information not found anywhere else.

However, at the same time, professional workflows require real time monitoring via supported video

I/O devices on a calibrated display. Lastly, video scopes provide a more precise analysis of the state

of the video signal you’re viewing, and DaVinci Resolve has built-in scopes you can use for creative

decision making and troubleshooting.

This chapter covers the Color page Viewer, external monitoring and display calibration, and video

scopes in more detail.

Contents

Using the Viewer������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2985

The Viewer Title Bar������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2985

Turning Grades and/or Fusion Effects Off��������������������������������������������������������������������������������������������������������������������������� 2987

Viewing Isolated Channels����������������������������������������������������������������������������������������������������������������������������������������������������������� 2987

The Viewer Toolbar�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2987

Showing Marker Overlays and Annotations������������������������������������������������������������������������������������������������������������������������ 2988

The Onscreen Control (OSC) Menu������������������������������������������������������������������������������������������������������������������������������������������ 2988

Toggling Viewer Overlays On and Off������������������������������������������������������������������������������������������������������������������������������������� 2989

Onscreen Controls and External Displays����������������������������������������������������������������������������������������������������������������������������� 2989

Zooming into the Viewer���������������������������������������������������������������������������������������������������������������������������������������������������������������� 2991

Using the Jog Bar and Transport Controls��������������������������������������������������������������������������������������������������������������������������� 2991

Navigating Using the Arrow Keys���������������������������������������������������������������������������������������������������������������������������������������������� 2992

Controlling Playback Using the Spacebar and JKL Keys����������������������������������������������������������������������������������������������� 2992

Fast Review on the Color Page��������������������������������������������������������������������������������������������������������������������������������������������������� 2992

Navigating Using Timecode��������������������������������������������������������������������������������������������������������������������������������������������������������� 2992

Viewer and Transport Timecode Displays��������������������������������������������������������������������������������������������������������������������������� 2993


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Enhanced, Full, and Cinema Viewing������������������������������������������������������������������������������������������������������������������������������������� 2993

Enhanced Viewing Mode��������������������������������������������������������������������������������������������������������������������������������������������������������������� 2993

Full Viewing Mode����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2994

Cinema Viewing Mode�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2995

Safe Area Overlays in the Viewer��������������������������������������������������������������������������������������������������������������������������������������������� 2996

Use Gray Background��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2996

Monitor Calibration��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2997

Viewing Broadcast Safe Exceptions��������������������������������������������������������������������������������������������������������������������������������������� 2998

Comparing Clips in the Viewer�������������������������������������������������������������������������������������������������������������������������������������������������� 2998

Saving and Wiping Stills in the Gallery and Timeline������������������������������������������������������������������������������������������������������� 2999

Different Viewer Reference Modes for Wipes���������������������������������������������������������������������������������������������������������������������� 3001

Wiping Between Clips in the Timeline������������������������������������������������������������������������������������������������������������������������������������� 3002

Using Split Screen Modes������������������������������������������������������������������������������������������������������������������������������������������������������������� 3003

Marker Overlays and Navigation����������������������������������������������������������������������������������������������������������������������������������������������� 3006

Timeline Marker List Available in Color Page Viewer Option Menu������������������������������������������������������������������������� 3006

Using Video Scopes������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3007

Video Scope Location��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3007

Video Scope Measurement Using Scales����������������������������������������������������������������������������������������������������������������������������� 3008

Video Scope Performance and Detail��������������������������������������������������������������������������������������������������������������������������������������� 3011

Display Qualifier Focus in Video Scope Graphs����������������������������������������������������������������������������������������������������������������� 3013

Explanation of Each Video Scope��������������������������������������������������������������������������������������������������������������������������������������������� 3013

Waveform Monitor������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3013

Parade������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3014

Vectorscope������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3015

Histogram (RGB/YRGB parade histogram)������������������������������������������������������������������������������������������������������������������������������ 3016

CIE Chromaticity Scope������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3016

Panning and Zooming the Video Scopes������������������������������������������������������������������������������������������������������������������������������ 3018

Customizing the Video Scopes��������������������������������������������������������������������������������������������������������������������������������������������������� 3018


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR