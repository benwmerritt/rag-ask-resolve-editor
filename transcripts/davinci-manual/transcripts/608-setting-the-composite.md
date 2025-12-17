---
title: "Setting the Composite"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 608
---

# Setting the Composite

Mode in a Corrector Node

If you are compositing in the Color page using the Alpha output, you can set a specific composite

mode for any corrector node. Right-click the node and select Composite Mode from the contextual

menu. You can then change the type of composite for the node to any of DaVinci Resolve’s built-in

composite modes.

Choosing a Composite mode for the Corrector node


Color | Chapter 147 Channel Splitting and Image Compositing

COLOR

Using OFX Alpha Channels (Legacy)

Now that all effects use standard color corrector nodes, the OFX Alpha is always available without

having to manually set a menu option. There is no need for the user to do anything else to access an

OFX Alpha moving forward from DaVinci Resolve 18.5.

However, for legacy project use there is still an OFX Alpha menu with two options.

Enable: On by default. When this is unchecked, even if the effect generates an Alpha, the

Alpha is ignored. Why one would go to the bother of generating an effect with an Alpha

channel, only to discard it completely is a matter of conjecture, but the option is there if you’re

doing something exceedingly strange and complicated. Really just leave this on.

Use For Mixing: On by default. When unchecked, no mixing of the Alpha happens on the

node at all.  Power Windows and Keys stop working, and the node behaves like a legacy FX

node. Any Alpha generated is still output, it just doesn’t limit where the effect acts.

The Use OFX Alpha option has been replaced with the OFX Alpha menu.

You most likely want to keep both Enable and Use for Mixing checked unless

you have a really good reason.


Color | Chapter 147 Channel Splitting and Image Compositing

COLOR

Chapter 148

Keyframing in

the Color Page

The Color page has a dedicated Keyframe Editor, found at the right of the palette

area, that you can use to animate grading changes from one frame to another.

Because grading is a fundamentally different task than editing, the Color page

Keyframe Editor operates somewhat differently from the Curve Editor in the Edit page.

Contents

Introduction to Keyframing����������������������������������������������������������������������������������������������������������������������������������������������������������� 3381

The Keyframe Editor Interface���������������������������������������������������������������������������������������������������������������������������������������������������� 3381

All/Color/Sizing����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3383

Keyframing Methods����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3384

Dynamic Keyframes (Dynamics)�������������������������������������������������������������������������������������������������������������������������������������������������� 3384

Static Keyframes (Marks)���������������������������������������������������������������������������������������������������������������������������������������������������������������� 3385

Mixing and Converting Dynamic and Static Keyframes�������������������������������������������������������������������������������������������������� 3385

Keyframed Nodes Have a Badge���������������������������������������������������������������������������������������������������������������������������������������������� 3386

Using Specific Keyframing Tracks�������������������������������������������������������������������������������������������������������������������������������������������� 3387

Corrector Keyframing Tracks������������������������������������������������������������������������������������������������������������������������������������������������������� 3388

ResolveFX Keyframe Tracks��������������������������������������������������������������������������������������������������������������������������������������������������������� 3388

The Sizing Keyframing Tracks������������������������������������������������������������������������������������������������������������������������������������������������������ 3389

The Ext Matte Node’s Freeform Isolation Track����������������������������������������������������������������������������������������������������������������� 3390

Automatic Keyframing�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3390

Modifying Keyframes���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3390

Navigating Among Keyframes����������������������������������������������������������������������������������������������������������������������������������������������������� 3390

Moving Keyframes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3391

Changing Keyframe Values����������������������������������������������������������������������������������������������������������������������������������������������������������� 3391

Changing Dynamic Attributes������������������������������������������������������������������������������������������������������������������������������������������������������� 3391

Deleting Keyframes�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3392

Copying Keyframes�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3393

Keyframes and Saved Stills���������������������������������������������������������������������������������������������������������������������������������������������������������� 3393

Adding EDL Marks���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3394


Color | Chapter 148 Keyframing in the Color Page

COLOR

Introduction to Keyframing

Whether it’s referred to as keyframing, dynamics, or marks, DaVinci Resolve provides an interface for

automatically interpolating color adjustment parameters in various ways from one setting to another.

For example, if you have a clip with varying exposure settings, you can animate a series of contrast

adjustments using Dynamic keyframes to make the changes in exposure less distracting.

The Keyframe Editor with dynamic keyframes animating the parameters of Node 2

In another example, suppose you’re grading a documentary, and an archival clip that’s edited in the

middle of the Timeline actually consists of six different shots from a program in the eighties. If you’re

in a hurry, you can insert Static keyframes (marks) at the cut points of each of these shots, creating

instant one-frame transitions between different adjustments made to that clip’s grade, which allows

you to create unique adjustments for each shot within the clip.

Round static keyframes added to all parameters, enabling individual

adjustment of shots merged together within a single clip

In both cases, you use the Keyframe Editor to create a series of keyframes with which to change

parameters from one value to another. In this section, you’ll learn how to work with the Keyframe Editor

to set up these kinds of animated changes.

The Keyframe Editor Interface

The Keyframe Editor has all the controls necessary to create and modify keyframes for the currently

selected clip. If necessary, you can even make it wider in a single screen layout by clicking its expand

button (at the top right of the Keyframe Editor). If you have two computer displays, you can use the

Color page’s Dual Screen layout which places the Keyframe Editor on a second screen and uses the

entire width of the monitor, for even more room.


Color | Chapter 148 Keyframing in the Color Page

COLOR

The Node Editor shown in wide mode, pushing all other palettes to the left

The Keyframe Editor consists of the following components:

�Timeline Ruler: Mirrors the record timecode of the currently selected clip; dragging within the

Timeline Ruler moves the playhead, and a timecode display to the left shows the current frame.

�Keyframe track header: Each node in the current grade has a corresponding keyframe track,

Sizing has its own keyframe track, and the track header contains controls you can use to

manage the keyframing.

The Keyframe track header

�Enable/Disable button: A round white button lets you enable or disable that track’s

corresponding node.

�Lock button: Lets you prevent any changes from being made to that track’s corresponding node.

Nodes that have been locked show a lock icon. You can also lock or unlock nodes by right-

clicking a node in the Node Editor and choosing Lock Node from the contextual menu.

Nodes 1 and 2 have been locked in the Keyframe Editor of the Color page.

�Auto-Keyframe button: Turn this button on to automatically create a Dynamic keyframe every time

you adjust any parameter within that node.

�Track disclosure triangle: Exposes individually keyframable groups of parameters underneath the

main keyframe track.


Color | Chapter 148 Keyframing in the Color Page

COLOR

�Keyframe tracks: To the right of the track header, the keyframe tracks are where you create and

edit the keyframes that animate parameter changes. A topmost “master keyframe track” shows

every keyframe applied on every keyframe track in the Keyframe Editor, even keyframes applied

to a keyframing track hidden inside a track with a closed disclosure triangle.

�Keyframes: Each keyframe appears as a small diamond for a Dynamic keyframe or as a circle for a

Static keyframe. Dynamic keyframes are associated with dissolves while Static keyframes (marks)

act instantly. Grades are linked to the preceding keyframe, which may be a default one on the first

frame of the master clip. Keyframes can be selected by clicking on them, or moved by dragging

them to another position in the keyframe track.

�FX track: Resolve FX or OFX plugins that have been added to a grade as a standalone node have

a separate track for creating animated effects. Every parameter of that track is keyframed via a

single consolidated keyframe track. If you apply multiple plugins as multiple nodes, each has a

separate FX track.

�Sizing track: The Pan, Tilt, Zoom, Rotate, and Convergence (in Stereo 3D projects) parameter have

an entirely separate track for creating animated pan and scan adjustments.

�Track selection drop-down: A colored bar shows the currently selected scope of keyframing: all

tracks at once, just the current correction node, or the Sizing settings, as defined by the Keyframe

Timeline mode discussed in the next section.

Ordinarily, the Keyframe Editor takes up the rightmost bottom third of the Color page. However, you

can make it wider to have more room to work if you have a scene requiring complex keyframing.

To expand and collapse the Keyframe Editor:

�Click the Expand/Collapse button at the top right corner of the Keyframe Editor. The Keyframe

Editor widens or narrows accordingly.

To zoom into and out of the keyframe tracks:

�Use the Zoom slider to zoom into or out of the Keyframe Editor.

�Right-click any keyframe track and choose Maximum Zoom to zoom all the way in.

�Right-click any keyframe track and choose Reset Zoom to fit the entire clip into the available width

of the Keyframe Editor.