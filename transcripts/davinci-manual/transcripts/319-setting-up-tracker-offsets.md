---
title: "Setting Up Tracker Offsets"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 319
---

# Setting Up Tracker Offsets

Often, it’s impossible to track the thing you want to apply an effect to. For example, the only pattern

available for an accurate track is a button on an actor’s sleeve. However, the effect requires the

person’s hand to be glowing. To cause the glow’s effect mask to be centered on the actor’s hand, it’s

necessary to use the Tracker Offset control.

The Tracker Offset controls in the Inspector

The X and Y Offset controls allow for constant or animated positional offsets to be created relative to

the actual Tracker’s pattern center. The position of the offset in the viewer will be shown by a dashed

line running from the pattern center to the offset position. You can also adjust the offset in the viewer

using the Tracker Offset button. Clicking the button enables you to reposition the path while keeping

the Tracker pattern in place.

The Tracker Offset tool in the Node toolbar of the viewer; a track of

the orange dot is being offset to the center of the ray gun

Once an offset for a pattern is set, you can connect other positional controls to the Tracker’s Offset

menu using the Connect To > Tracker: Offset Position option in the control’s contextual menu. The

path created during the track remains fixed to the center of the pattern.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Stabilizing with the Tracker Node

When a Tracker node is set to Match Move in the Operations tab, it is capable of a variety of functions.

Applying the motion from the background clip to the foreground clip is the obvious functionality.

However, the Match Move operation is also used for stabilizing footage to to either completely remove

motion from the scene or smooth existing motion.

Here are some common scenarios for stabilization that are handled when the Tracker is set to

Match Move.

�A sequence that should be steady has vibrations or undesirable movement.

�A sequence that requires a smooth camera move suffers from jarring.

The Tracker Operation tab Match Move

set to BG Only for stabilization

Stabilization Using the Tracker Match Move Mode

Stabilizing motion completely removes the appearance of motion from the image. The motion from

frame to frame is calculated, and the contents of the frame are transformed to return the image to a

reference position. This position can be either the start or end of the sequence or a manually selected

frame from the sequence.

Stabilization can correct for position with as little as one pattern. Two or more patterns are required to

correct for rotation or scaling within the image.

When the Operation menu is set to Match Move, choosing BG only from the Merge operation menu

stabilizes the background (yellow input) clip. Only the controls that are applicable for stabilization

operations will appear in the Operation tab.

Several of the stabilization controls are always available, collected under the Match Move Settings

disclosure button. These controls are available at all times because the Steady and Unsteady positions

of a tracker are always published. This makes them available for connection by other controls, even

when the Tracker’s operation is not set to match moving.

The Match Move settings

Merge

The Merge menu determines to which input connection the Tracking data is applied. When stabilizing

an image to remove all motion, or smooth the motion, the Merge button must be set to BG Only.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Edges

The Edges menu determines whether the edges of an image that leave the visible frame are cropped,

duplicated, or wrapped when the stabilization is applied. Wrapping edges is often desirable for some

methods of match moving, although rarely when stabilizing the image for any other purpose.

For more information on the controls, see Chapter 119, “Tracking Nodes,” in the

DaVinci Resolve Reference Manual or Chapter 59 in the Fusion Reference Manual.

Position/Rotation/Scaling

Use the Position, Rotation, and Scaling checkboxes to select what aspects of the motion are corrected.

Match Move Settings

Options for the Match Move settings include Pivot and Reference.

Pivot Type

The Pivot Type for the stabilization is used to calculate the axis of rotation and scaling

calculations. This is usually the average of the combined pattern centers but may be changed

to the position of a single tracker or a manually selected position.

Reference

The Reference controls establish whether the image is stabilized to the first frame in the

sequence, the last frame, or to a manually selected frame. Any deviation from this reference by

the tracked patterns is transformed back to this ideal frame.

As a general rule, when tracking to remove all motion from a clip, set the Merge mode to

BG Only, the Pivot Type to Tracker Average or Selected Tracker, and the Reference control to

Start, End, or Select Time.

Smoothing Motion

When confronted with an image sequence with erratic or jerky camera motion, instead of trying to

remove all movement from the shot, you often need to preserve the original camera movement while

losing the erratic motion.

The Start & End reference option is designed for this technique. Instead of stabilizing to a reference

frame, the tracked path is simplified. The position of each pattern is evaluated from the start of the

path and the end of the path along with intervening points. The result is smooth motion that replaces

the existing unsteady move.

The Reference Intermediate Points slider is displayed when

Start & End is selected to enable the smoothing of motion


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

To preserve some of the curvature of the original camera motion, you can increase the value of the

Reference Intermediate Points slider that appears when the Start & End reference mode is selected.

When tracking to create smooth camera motion, ensure that the Start & End reference mode is

enabled and set the Merge mode to BG Only. It is recommended to leave the Pivot Type control set to

Tracker Average.

Using the Tracker Node for Match Moving

A simple match moving example is shown at the beginning of this chapter, but this section presents

additional details that you may not have been aware of. Examples of match moving include:

�A static CG element must be believably added to a moving sequence.

�Two sequences with different motions must be composited together.

Some clips may need to be stabilized so that an element from another source can be added to the

shot. After the element or effect has been composited, the stabilization should be removed to make

the shot look natural again.

Simple Match Moving

Match moving essentially applies the movement from the tracked clip to another clip. There are two

ways to perform match moving. One method involves connecting other nodes, such as Transform or

Merge, to a Tracker’s outputs. The other method is to stabilize an image by trying to remove all motion,

but instead of setting the Merge menu to BG Only, set it to FG Over BG, FG Only, or in rare occasions,

BG Over FG.

Set the Merge menu to BG Only, FG Over BG, or BG Over FG

When using this Merge menu, you connect a foreground image to the Tracker node’s input connection

in the Node Editor.

Connect a foreground image to the Tracker’s foreground input

Enabling the FG Only mode will apply the motion from the background to the foreground, and the

Tracker will only output the modified FG image. This result can later be merged over the original,

allowing further modifications of the foreground to be applied using other nodes before merging the

result over the background clip.


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Corner Positioning Operations

The Corner Positioning operation maps the four corners of a foreground image to four patterns within

the Tracker. This operation, or technique, is most commonly used for sign replacements.

The Corner Positioning operation of the Tracker requires the presence of a minimum of four patterns. If

this operation mode is selected and there are not four patterns set up in the Tracker already, additional

patterns will automatically be added to bring the total up to four.

When this mode is enabled, a set of drop-down boxes will appear to select which tracker relates to

each corner of the rectangle. It has no effect when the Merge control option is set to BG Only.

Perspective Positioning Operations

The Perspective Positioning operation is used to remove perspective from a foreground image or

apply the perspective from one sequence to another. This can be useful when you need to paint out

an area that is distorted by perspective. Removing the perspective flattens the images for painting,

and then another tracker adds the perspective back.

The Perspective Positioning operation of the Tracker requires the presence of a minimum of four

patterns. If this operation mode is selected and there are not four patterns set up in the Tracker

already, additional patterns will automatically be added to bring the total up to four.

When this mode is enabled, a set of drop-down boxes will appear to select which tracker relates to

each corner of the rectangle. It has no effect when the Merge control option is set to BG Only.

Connecting to Trackers’ Operations

One of the most common applications for a tracked pattern is using the tracked position or path

to drive the position of another node’s parameters. For example, tracking an eye in order to color

correct the eye to blue using an effect mask. You start off by tracking the eye, and then create a

color corrector with the desired settings. You create a mask in the shape of the eye and connect the

Tracker’s position to the Center of the mask.

In addition to the path (called Offset Position), each pattern in a tracker publishes four other values for

use as connections that are available to other nodes in the Node Editor.

You connect a node’s position parameters to a tracker by selecting the connection type from the

controls contextual menu (for example, Transform 1: Center > Connect To > Tracker 1 > Offset Position).

There are five connection types automatically published by the tracker to connect to a position

parameter in another node.

Steady Position

Steady Position can be used to stabilize footage in both X and/or Y to remove camera shake and

other unwanted movement. The connection inverts the output of the tracked pattern’s motion. When

you connect a Center parameter to the Steady Position of the Tracker, it will be placed at 0.5/0.5

(the center of the screen) by default at frame 1. You can change this using the Reference mode in the

Tracker’s Operation tab.

Steady Angle

The Steady Angle mode can be used to stabilize footage in both X and/or Y to remove camera shake

and other unwanted movement. When you connect a control, for example the Angle of a Transform,

to the Steady Angle of the Tracker, it will be placed at 0 degrees by default at frame 1. This can be


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

changed by means of the Reference mode in the Tracker’s Operation tab. From there on, the resulting

motion of the Steady Angle mode will rotate into the opposite direction of the original motion.

So if the angle at frame 10 is 15 degrees, the result of the Steady Angle will be -15 degrees.

To use Steady Angle, you need at least two tracked patterns in your tracker. With just one point, you

can only apply (Un)Steady Position.