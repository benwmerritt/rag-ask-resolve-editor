---
title: "Keyframing in the Edit Timeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 204
---

# Keyframing in the Edit Timeline

and Curve Editor

You can use keyframes directly in the the Timeline, or if you need to do more complicated keyframe

editing than the relatively simple controls of the Inspector and Timeline allow, you can use the

Keyframe tracks and Curve Editor found in the Edit Timeline. When one or more clip parameters are

keyframed, two small buttons appear at the far right of a clip’s name bar in the Timeline, a Curve

button and a Keyframe button. These buttons let you access specialized keyframe editors that serve

different purposes.

Keyframe Directly in the Timeline During Playback

Keyframes can be added directly on clips in the Timeline while playing back. You can add and delete

keyframes to a clip using keyboard shortcuts, and DaVinci Resolve will try to intelligently predict the

context of the clip to set the appropriate key frame.

This method allows you to quickly and precisely add retime and audio gain Keyframes during playback

and then come back and manipulate the points you specified.

To Add a Keyframe to a Clip in the Timeline:

�Playback the clip on the Timeline and when the playhead is over the frame of the clip where you

want to add the keyframe.

�Choose Mark > Add Keyframe (Command-[).

To Delete a Keyframe in a Clip in the Timeline:

�Select the keyframe or keyframes you want to delete from the clip.

�Choose Mark > Delete Keyframe (Option-]).

While adding a keyframe on the timeline clip is a simple keyboard press, how does DaVinci

Resolve know what specific parameter from all the options available in the inspector you wanted to

keyframe? Essentially the keyframes are now context aware, meaning which keyframable attribute

(Zoom, Position, Volume, etc.) is selected by DaVinci Resolve depends largely on the last item you

manipulated, or falling back to the most commonly used.

The keyframe selection hierarchy in DaVinci Resolve runs through the keyframable options from top to

bottom; if no keyframe makes sense in the context of the top entry, it automatically chooses the next

one down the list, and so on.

The DaVinci Resolve Keyframe Selection Order:

�The Retime Controls (if already active)

�The active effect curve in the Keyframe Editor (if already open)

�The last Inspector control that was manipulated

�Audio Gain


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

For example, if you previously adjusted the Zoom parameter on a clip, then added a new keyframe to

the clip by pressing Option-[ , it would bypass the Retime Controls, the Effect Curves if those controls

were closed in the inspector, and add a new Zoom keyframe, as that was the last tool manipulated.

This also means that when you add a keyframe to a basic clip on a timeline with no modifications, it

adds an Audio Gain Keyframe.

If you want to do more complex keyframing, or DaVinci Resolve is not picking up on the context

correctly, you can use the Keyframe Editor.

The Keyframe Editor

The Keyframe Editor in the Timeline is the most powerful way of exposing all of a clip’s keyframes and

adjusting their timing and interpolation. It’s only available when you’ve already keyframed one of a

clip’s Inspector properties.

To open or close the Keyframe Editor:

•	 Click a clip’s Keyframe button at the far right of a clip’s name bar.

•	 Select a clip and choose Clip > Show Keyframe Editor (Command-Shift-C).

The Keyframe track button

in the Timeline appearing

on a keyframed clip

The Keyframe Editor exposes one keyframe track for each group of parameters that’s keyframed.

For example, the Composite parameters, Transform parameters, and Cropping parameters are all

encapsulated by group tracks. For example, if you’d added keyframes to the Zoom and Position

parameters, these keyframes all appear within a single keyframe track labeled Transform, while

Opacity adjustments appear on a second keyframe track for Composite.

Group keyframe tracks open in the Timeline

However, each group keyframe track has a disclosure button that lets you show or hide each

individual parameter that’s keyframed within that group. For example, clicking the Transform keyframe

track’s disclosure button shows the Zoom and Position tracks, so you can adjust those individual

keyframes.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

Individual parameter keyframe tracks open in the Timeline

These keyframe tracks let you edit keyframes in context of the actual clip durations in the Timeline.

Click the small Keyframe button at the bottom right of the clip’s name bar to close the keyframe tracks

when you’re finished.

Methods of adding and selecting keyframes in the Keyframe Editor of the Edit page:

�To add new keyframes to the Keyframe Editor: Press Command-[ or Option-click anywhere on a

track of the Keyframe Editor to add a new keyframe, which defaults to whatever the current value

is for that parameter at that frame. New keyframes create linear animated changes by default.

�To duplicate one or more keyframes: Make a selection of keyframes, then hold the Option

key down and drag the selected keyframes to duplicate them and move the duplicates

to a new position.

�To select a single keyframe: Click a single keyframe to select it.

�To select multiple discontiguous keyframes: Command-click all keyframes you want to select,

whether they’re next to one another or not.

�To select multiple contiguous keyframes: Click the first keyframe you want to select, and

then shift-click the last keyframe you want to select, and all keyframes between will also be

selected, or drag a bounding box within the keyframe track around multiple keyframes to select

them all at once.

Methods of changing keyframe interpolation/easing/

smoothing in the Keyframe Editor of the Edit page:

�To change one or more Linear keyframe to Ease In or Ease Out: Eased keyframes create

animated changes that begin slowly and accelerate to full speed, or slow down gradually to

decelerate to a stop. This only works when you have two or more keyframes creating an animated

effect. Select one or more keyframes, then right-click one of the selected keyframes and choose

Ease In, Ease Out, or Ease In and Out, depending on which keyframe you’re editing and the effect

you want to create.

�To change one or more eased keyframes to Linear: Select one or more keyframes, then right-

click one of the selected keyframes and choose Linear.

Methods of moving and adjusting keyframes in the Keyframe Editor of the Edit page:

�To move one or more keyframes: Select one or more keyframes and drag left or right. While you

drag keyframes, a tooltip appears showing you the offset in frames of your adjustment from the

beginning of that clip’s source media. If you’re only dragging one keyframe, the tooltip also shows

you the name of the parameter you’re modifying.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

�To nudge selected keyframes one frame at a time: Select one or more keyframes and press

Command-Left Arrow or Command-Right Arrow to nudge them back and forth, for precision

editing. The Curve Editor must also be open.

Methods of Cutting, Copying, Pasting, and Deleting keyframes:

�To cut or copy, and paste one or more keyframes: Make a selection of keyframes, and use the

Cut (Command-X) or Copy (Command-C) key shortcuts. Then, move the playhead to where you

want the first of the copied keyframes to start, and press Paste (Command-V). The Curve Editor

must also be open.

�To delete one or more control points from a curve: Select the keyframe(s) you want to delete and

press Backspace, or press Option-]. The Curve Editor must also be open.

Keyframe and Curve Editor

The Keyframe and Curve Editors in DaVinci Resolve are designed to give you fine control for complex

animations that are too detailed to use in the Inspector.

The Keyframe and Curve Editor is accessible from both the Cut and Edit pages as its own panel.

Simply click on the Keyframes tab in the upper left to open it. By default, the Keyframe Editor is

displayed, showing you all of the keyframable parameters in the Video Inspector and any existing

keyframes that may have been added there. Clicking on the Curve icon in the upper left will take you

to the Curve Editor.

The Keyframe Editor

The Keyframe Editor in the Timeline is the most powerful way of exposing all of a clip’s keyframes and

adjusting their timing and interpolation.

The Keyframe Editor showing all the Video attributes found in the Inspector


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

The Keyframe Editor exposes one keyframe track for each parameter that’s possible to be

keyframed on the selected clip. Initially this looks like a big list of complicated items to keep

track of (no pun intended), but it does provide a good overview of everything that’s animatable

for your clip. However, the Keyframe Editor has several tools to help remove unnecessary

clutter and only focus on the exact parameters you’re interested in animating. These keyframe

tracks let you edit keyframes in context of the actual clip durations in the Timeline.

Keyframe Tracks: Transform is the track group (shown by the

disclosure triangle), Zoom and Position XY are tracks within that

group. Selected keyframes are shown white with an outline.

The tracks are also grouped by parameter category. For example, all the Transform, Cropping,

and Speed parameters are encapsulated by group tracks. If you’d added keyframes to

the Zoom and Position parameters, these keyframes also appear within a single keyframe

track labeled Transform, while Crop Left and Crop Right adjustments appear on another

group keyframe track labeled Cropping. Moving a keyframe on a group track will adjust the

keyframes at the same position for all of its enclosed parameters at the same time.

Each group keyframe track has a disclosure arrow that lets you show or hide each individual

parameter within that group. For example, clicking the Transform keyframe track’s disclosure

arrow shows the Zoom and Position tracks, so you can adjust those individual keyframes.

Organizing the Keyframe Editor

While keyframing itself is a fairly simple process, the sheer number of keyframable attributes can be

overwhelming, so unless you’re planning on animating something incredibly complicated, it’s probably

a better idea to focus the Keyframe Editor’s interface on just what you need.

To show or hide tracks by parameter group

� Click on the small disclosure triangle next to the group track’s name. For example, if you were

only intending to keyframe parameters in the Transform group (Zoom, Position, etc.), you could

close the disclosure triangles in the Cropping and Speed groups to hide the excess tracks.

� Click on the 3-dot option menu in the right of the parameters column, and choose Expand All

Parameters to open every group track to see their enclosing parameters.

� Click on the 3-dot option menu in the right of the parameters column, and choose Collapse All

Parameters to close all group tracks.

To show only tracks that already have keyframes

� Click on the 3-dot option menu in the right of the parameters column, and choose Display

Parameters with Keyframes. This will show only tracks that have already at least one keyframe

assigned to them, and their enclosing group tracks.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

To show only Video related tracks

� Click on the 3-dot option menu in the right of the parameters column, and choose Display All

Video Parameters. This will hide any keyframe tracks that control audio-related functions from the

Audio Inspector.

To show only specific tracks

� Click on the 3-dot option menu in the right of the parameters column, and choose Display

Selected Parameters. You can then choose checkboxes for Video and Audio. Clicking on these

will open up another set of checkboxes that allow you to specify exactly which tracks you

want to show.

To undock and resize the Keyframe Editor

� Click on the undock icon in the Keyframe Editor to open it as an independent window. You can

then resize the window to expand the Keyframe Editor to any size that you need.

Using the Keyframe Editor

Once the Keyframe Editor is open and the parameters you wish to animate are exposed, you have

many ways to add, delete, and manipulate keyframes along these tracks.

The Keyframe Track controls (L-R): Toggle Curve Visibility, Toggle Keyframe Lock,

Track Color, Track Name, Keyframe, Reset Keyframes, Keyframe position.

Keyframe Track Controls:

Toggle Curve Visibility: Click on this icon to turn this track’s curve visibility on or

off in the Curve Editor.

Toggle Keyframe Lock: Click on this icon to turn the keyframe lock on or off to

prevent accidental changes.

Track Color: A small colored dot shows the color of the track’s curve in the

Curve Editor.

Track Name: The name of the track parameter.

Keyframe: Clicking the diamond will add a new keyframe at the current position. If

there is an active keyframe at the position this diamond will be orange, otherwise

white. The left and right arrows will skip to the previous and next keyframes

respectively.

Reset Keyframes: Removes all keyframes in the track.

Keyframe Position: Shows all set keyframes for the track and their position

in the clip.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

Methods of adding and selecting keyframes in the Keyframe Editor:

�To add new keyframes to the Keyframe Editor: Adjust the playhead to where you want the

keyframe, then click on the gray diamond next to the parameter’s name. The diamond will turn

orange to let you know a keyframe has been added, and it will also appear on the parameter

track at the playhead position. Subsequent keyframes can be added on this track by pressing

Command [ to add another keyframe.

�To select a single keyframe: Click a single keyframe to select it.

�To select multiple discontiguous keyframes: Command-click all keyframes you want to select,

whether they’re next to one another or not.

�To select multiple contiguous keyframes: Drag a bounding box within the keyframe track around

multiple keyframes to select them all at once.

�To move one or more keyframes: Select one or more keyframes and drag left or right.

Methods of Cutting, Copying, Pasting, and Deleting keyframes:

�To cut or copy, and paste one or more keyframes: Make a selection of keyframes, and use the

Cut (Command-X) or Copy (Command-C) key shortcuts. Then, move the playhead to where you

want the first of the copied keyframes to start, and press Paste (Command-V).

�To delete one or more keyframes: Select the keyframe(s) you want to delete and press Delete.

IMPORTANT: Keyframes on the Timeline can exist past a clip’s current extents. For example,

if you set several keyframes on a clip, then trim its duration on the Timeline past one of

the keyframes, that keyframe is still there and fully functional, just not visible. You can

still navigate to these invisible keyframes by using the Previous “[“ and Next “]” keyframe

commands or using the keyframe controls in the Inspector.

The Keyframe Editor controls (L-R): Curves Editor, Keyframe Editor, Detail Zoom,

Full Extend Zoom, Zoom Slider, Expand, Option Menu.

Curves Editor: Click this icon to open the

Curves Editor.

Full Extend Zoom: Zooms the Keyframe Editor

out to show the range of the whole clip.

Parameters: Click this icon to open the

Keyframe Editor.

Zoom Slider: Lets you choose a custom zoom

level for the Keyframe Editor

Detail Zoom: Zooms the Keyframe Editor in

around the playhead position.

Expand: Opens the Keyframe and Curves Editor

in its own resizable window.


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

Option Menu:

�Display Time Ruler in Seconds: Shows the

time ruler in HH:MM:SS:FF timecode format

based on the timeline.

�Display Time Ruler in Frames: Shows the

time ruler as number of frames since the

timeline start.

�Snap Keyframes to Grid: When enabled

in the Curve Editor, this snaps keyframe

control points to the playhead position.

�Show Curve Tooltips: When enabled in

the Curve Editor, placing the pointer over a

curve will show its track name and value at

the given point.

Parameters: Shows a list of keyframable

parameters.

Option Menu:

�Display Parameters with Keyframes:

Only shows tracks with existing keyframes

and hides all others.

�Display All Video Parameters: Shows all

keyframable tracks found in the Video

Inspector, and hides all others.

�Display Selected Parameters

(Video & Audio): Opens a checkbox to

turn on or off individual track visibility.

In addition, if you’ve added a keyframable

Open FX or Resolve FX to the clip, you can

select those parameters here.

Expand All Parameters: Opens every group

track to see their enclosing parameters.

Collapse All Parameters: Closes every group

track to hide their enclosing parameters.

Opening the Keyframe Tray in the Timeline

In addition to the dedicated Keyframe Editor panel, you can also expose a keyframe tray on the

timeline by selecting the Show Keyframe Tray icon on the main timeline toolbar in both the Cut and

Edit pages. This keyframe tray shows all the keyframes of the currently selected clip on the timeline

and operates in the same way as the Keyframe Editor.

You can open up the Keyframe Editor directly in the timeline by

clicking on the Show Keyframe Tray icon (circled red).


Editing Effects and Transitions | Chapter 53 Keyframing Effects

EDIT

Opening the Keyframe and Curve Editor in Its Own Window

If you are doing extensive keyframing in the Edit page (not available in Cut), you can open up the

Keyframe and Curve editor in its own resizable window to give you more space to work with. To do so,

click on the Expand icon in the upper right of the Keyframe Editor.

The Keyframe and Curve Editor can be expanded to its own resizable window.