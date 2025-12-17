---
title: "Managing Strokes in the Stroke List"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 579
---

# Managing Strokes in the Stroke List

When you draw a stroke, it appears in the Stroke list. By default, all strokes last for the duration of the

clip to which they’re applied, so if you draw a stroke to identify a figure that’s not moving, there’s no

requirement to motion track the stroke. Strokes in Person mode appear in one long list, while strokes

in Features mode appear hierarchically, with the strokes for each feature separated by the title of each

feature. Once a stroke appears in this list, it has the following controls.

Enable/disable feature: In Features mode, once you draw at least one stroke to identify that

feature, the title of that feature appears, underneath which is organized all the strokes for that

feature. A toggle next to the feature name lets you turn that feature’s contribution to the overall

mask on and off.

Enable/disable stroke: Each individual stroke in this list has a blue dot that lets you turn that

stroke’s contribution to the overall mask on or off.

Stroke Timeline Area with Stroke Tracks: The stroke track for each stroke lets you keep

track of and manipulate the animation of strokes to follow camera and subject motion. Blue

or red frames in this track let you see at a glance how much of each stroke has been motion

tracked; blue frames for positive strokes, red frames for negative strokes. You can also use

these tracks to identify frames where you’d like to mute that stroke’s contribution to the final

mask and to keep track of which frames have been muted. You can draw a bounding box

within the stroke track around however many frames of however many strokes for which you

want to delete motion tracking.

Stroke Duration

When you first draw a stroke, that stroke has a duration of one frame, located at the timecode position

of the playhead when you drew it. If you move the playhead to the left or right, you’ll see the stroke

disappear. If you want one or more strokes to continue analyzing the subject for the duration of that

shot, you need to use the Motion Tracking controls to track the stroke to follow along with the motion

of whatever it’s drawn on top of. As a stroke is tracked, its duration increases to cover the entire range

of tracked frames. If at any point a stroke outlasts its usefulness, such as when a person walks off

frame, you can stop tracking that stroke when it’s no longer necessary and it will stop contributing to

the analysis.

This is useful, because often you’ll want to place strokes to deal with analysis issues that only last for

a few frames, to fix a hole in the mask that only appears briefly. Just be aware, you can’t simply draw

a stroke and move on to the next shot; you must track at least one stroke to last for the duration of a

subject’s time on screen for that subject to be continuously masked.

Tracking Strokes to Follow Subject Motion

You can think of each stroke you’ve drawn as a persistent eyedropper that samples the image that

overlaps it. The mask that results from all strokes’ collective analysis of the image is generated live

over each frame of the clip. This means that if the camera or the subject moves, you need to motion

track or otherwise adjust the position of each stroke to follow along with the motion, so the subject

continues to be correctly identified. You also need to make sure that each stroke is able to analyze

what it’s supposed to, and turn off strokes that can’t for whatever reason.


Color | Chapter 139 Magic Mask

COLOR

TIP: Magic Mask is a processor-intensive operation, so to accommodate users of less

powerful workstations, there is a Use Fast Tracking option available in the Magic Mask

palette’s Option menu, which speeds up the process of tracking at the expense of potentially

less accurate tracking for fast or erratically moving subjects.

Methods of Moving Strokes to Follow Subject Motion

For these reasons and more, there are multiple methods of manipulating strokes to refine the

final analysis.

�Motion Tracking: A set of tracking controls at the top of the Magic Mask palette let you motion

track one or more strokes to follow the camera and subject motion in a clip. Every frame that’s

motion tracked effectively has a motion-tracked reference frame placed on it that moves the

stroke to a new position.

�Reference Frame: Any time you drag a stroke from its original position in the Timeline, you create

a static reference frame at that frame that instantly moves the stroke from its previous position to

the new position at that frame. Because these are similar to static keyframes, there’s no motion

interpolation from one “keyframe” to the next in order to create animation. Instead, a reference

frame in the Magic Mask palette is a simple frame-by-frame operation. Every time you move a

stroke at a new frame, you change the stroke’s position at that frame from that point forward,

without changing stroke position on any other frame that’s been previously tracked.

�If this seems simplistic, keep in mind that the goal is not to create beautiful stroke animation with

this tool. You only need to move each stroke to follow along with whichever subject or background

feature it’s supposed to be sampling in each frame. The only important thing is that, in every frame,

the stroke overlaps a suitable part of the feature you’re isolating to create the appropriate mask.

If the stroke itself jumps around abruptly, that doesn’t matter so long as the mask that’s generated

is good. This means that even if you’re stuck doing a limited amount of frame-by-frame animation

to make a stroke follow along with a troublesome feature (such as a veil flapping in the wind),

it’ll go pretty fast, because in each frame you’re just dragging the stroke to overlap the feature

wherever it happens to have moved. This repositioning doesn’t have to be smooth, just accurate.

�Combining Tracking and Reference Frames: Since each frame that’s motion tracked is effectively

keyframed, manually dragging a stroke on a frame that’s already been tracked overrides the

tracking data at that frame with a reference frame that records the new position of the stroke at

that frame. If there’s no more tracking data, either before or after that reference frame, then the

stroke disappears until you do more tracking. If there’s tracking data immediately after a reference

frame, then the stroke jumps to the position dictated by that tracking data.

�Deleting Stroke Tracking at Specific Frames: To accommodate cases where a subject you’re

isolating moves behind something and becomes hidden for a range of frames, you have the ability

to delete stroke tracking for one or more frames. This lets you eliminate the stroke for however

many frames the subject you’re tracking is obscured and cannot be sampled. This makes it easy

to deal with features that come and go over the duration of a clip, since you can delete stroke

tracking over however many ranges of frames the feature disappears. If you’ve muted frames by

mistake, you can either undo or re-track the stroke over those frames.

To delete tracking frames, draw a bounding box on the stroke tracks over the range you want to

delete, and then choose Clear Selected Track Data from the Magic Mask option menu.


Color | Chapter 139 Magic Mask

COLOR

Option Menu Commands for Removing Strokes and Tracking

The Option menu of the Magic Mask palette presents a number of commands for clearing either

strokes or stroke tracking data.

�Clear All Strokes: Deletes every stroke in the Stoke list, along with tracking.

�Clear All Strokes of Current Frame: Deletes the tracking data at the current position of the

playhead on all strokes in the list.

�Clear All Strokes from In to Out: If you use the I and O keys to set In and Out points in the Stroke

Timeline, this command deletes all tracking data on all strokes within that range.

�Clear Selected Stroke from In to Out: If you select a stroke in the Stroke list, and then use the I

and O keys to set In and Out points in the Stroke Timeline, this command deletes the tracking data

of selected strokes within that range.

�Clear Selected Track Data: If you drag a bounding box around tracking data for one or more

strokes, this command deletes all tracking data within the box.

An Example Stroke Tracking Workflow

By combining motion tracking, manual reference frames, and stroke muting, you’ll be able to make

short work of isolating most moving subjects. The following procedure illustrates how you might

use these techniques together to make the strokes you’ve drawn follow along with the features

you’re isolating.

To track one or more strokes to follow a subject:


If necessary, move the playhead to the frame where you want to begin isolating the subject you

want to mask. For example, if you’re isolating a person walking into the room through a door, you

probably want to begin your work on a frame where the person is already in the room, and work

your way backward and forward from that frame. If your subject is already fully visible at the first

frame of the shot, you can start there.


Draw at least one stroke identifying the subject or feature you want to isolate. You cannot track a

stroke to follow the features unless there’s at least one stroke.


Choose whether you want to track all strokes or only selected strokes. By default, all existing

strokes with at least one frame in the Stroke Timeline at the position of the playhead will be

tracked. However, you can choose to track only selected strokes in the Stroke list by choosing

Track Selected Stroke Only in the Magic Mask palette’s Option menu.


Click the Track Forwards to End or Track Backwards to Beginning buttons if you want to motion

track the strokes over the remaining duration of the clip.

By default, each stroke is tracked to follow whatever image detail immediately surrounds it;

you don’t have to define a tracking region, this is done automatically. As tracking proceeds, the

tracking bar for each stroke will fill up showing you which frames have been tracked, and which

have yet to be tracked. Meanwhile, each stroke being tracked will transform to follow along with

simple position and rotation changes in the subject. However, things that obscure the subject, as

well as more extreme movements, may cause problems.

Strokes that are tracking a feature that moves off screen are automatically excluded from tracking

at the frame where the feature is completely off screen, even if that feature returns onscreen in a

later frame.


Color | Chapter 139 Magic Mask

COLOR


(Optional) If a problem occurs during the track, such as the subject being occluded behind

something else in the frame (for example, a person’s face moves behind a tree as they walk),

click the Pause Track button. You can deal with problems in the track in the following ways:

a)	 If a stroke has completely moved off of the subject: For example, you’re tracking a stroke

to follow a person and they turn around 180 degrees, so the stroke moves off onto the

background. To fix this, pause the track, move the playhead to the first frame where the

stroke hasn’t followed the subject properly, then use the pointer to drag the stroke onto

another part of the subject that’s clearly visible. On each frame where you drag the stroke

to a new position, a new reference frame will be automatically added. Continue this process

until the subject’s motion is consistent enough to be trackable again, and you can then

resume tracking.

b)	 If a stroke has moved onto something that’s partially obscuring the subject: Pause the track,

drag a bounding box over the frames where the track is having a problem, and choose Delete

Selected Tracking from the Magic Mask Option menu to clear the bad tracking data. Then,

move the playhead to the first frame of the deleted tracking data, and use the pointer to drag

the stroke onto any part of the subject that’s visible to either side of the occlusion. Move the

playhead to each successive frame, and drag the stroke onto whichever part of the subject

is visible from behind the occlusion, until the subject moves past the occlusion. At that point,

you can use the Track Forwards to End or Track Backwards to Beginning buttons to continue

tracking as usual.

c)	 If the subject becomes completely hidden: Clips where the subject appears and disappears

over the duration of a clip can be resolved by deleting the stroke or strokes on that subject

over all frames where the subject is obscured, so that strokes only sample the image when the

subject is visible and thus able to be isolated. You can delete one or more strokes by dragging

a bounding box over a range of frames, and then choosing Clear Selected Track Data from the

Magic Mask Option menu.

d)	 If a stroke is having trouble following the subject: If the subject you’re tracking is moving too

fast, too irregularly, or is changing shape too greatly for the tracker to give a good result (for

example, someone lifts their arm towards the camera), you can track through the problem area

of the clip one frame by frame using the Track Forward 1 Frame or Track Backward 1 Frame

buttons, and then use the pointer to manually drag the stroke to follow along with the subject

as you go. Once the problem motion stops and the motion of the subject becomes more

regular, you can use the Track Forwards to End or Track Backwards to Beginning buttons to

continue tracking as usual.

e)	 If the subject is moving off the frame: If you’ve drawn a stroke in the middle of someone’s

face, and their face is moving off screen, you can manually reposition the stroke on the last

few frames before the subject completely exits so that stroke continues to identify what parts

of the face are still visible even though the part of the face it was originally following becomes

hidden. Once the face completely exits the frame, you can mute the stroke for the rest

of the shot.


(Optional) If you only tracked the stroke’s movement over part of a shot, you can click the Jump to

Start or Jump to End buttons to move the playhead to the first or last tracked frame, in preparation

for tracking from that frame onward.


Color | Chapter 139 Magic Mask

COLOR

Chapter 140

Motion Tracking

Windows

While Power Windows can be manually keyframed to follow a moving subject

you want to isolate, this chapter shows how you can use the powerful cloud

and point-based motion tracking controls in DaVinci Resolve to make Power

Windows follow along with the motion of subjects and the camera in the fastest,

easiest way possible.

Then, numerous techniques are presented for dealing with complicated tracking scenarios and

common problems that arise for subjects that are difficult to track.

Contents

Motion Tracking Windows������������������������������������������������������������������������������������������������������������������������������������������������������������� 3179

Simple Tracking Using the Tracker Menu������������������������������������������������������������������������������������������������������������������������������� 3180

Tracking Windows Across Transitions��������������������������������������������������������������������������������������������������������������������������������������� 3181

Tracking Windows When You’ll Be Exporting Media With Handles��������������������������������������������������������������������������� 3181

Simple Ways of Working With Existing Tracking Data������������������������������������������������������������������������������������������������������� 3181

Tips for Better Tracking�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3182

Tracking One Frame at a Time����������������������������������������������������������������������������������������������������������������������������������������������������� 3182

Copying and Pasting Tracking������������������������������������������������������������������������������������������������������������������������������������������������������ 3182

Tracker Palette Controls in More Detail��������������������������������������������������������������������������������������������������������������������������������� 3183

Controls in the Window Tracker Palette���������������������������������������������������������������������������������������������������������������������������������� 3183

IntelliTrack AI Point Tracker (Studio Version Only)�������������������������������������������������������������������������������������������������������������� 3187

Cloud Tracker Workflows��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3188

Using Interactive Mode to Manually Choose Tracking Features�������������������������������������������������������������������������������� 3188

Dealing With Occlusions When Tracking�������������������������������������������������������������������������������������������������������������������������������� 3192

Point Tracker Workflows����������������������������������������������������������������������������������������������������������������������������������������������������������������� 3194

Tracking a Window Using the Point Tracker�������������������������������������������������������������������������������������������������������������������������� 3194

Removing Trackers������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3197

Using Frame Mode to Offset Track��������������������������������������������������������������������������������������������������������������������������������������������� 3197


Color | Chapter 140 Motion Tracking Windows

COLOR