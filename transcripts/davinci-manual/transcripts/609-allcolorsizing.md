---
title: "All/Color/Sizing"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 609
---

# All/Color/Sizing

Perhaps the most important control for keyframing, the Keyframe Timeline mode, lets you switch

the scope of what tracks get keyframed when you use the Start Dynamic or Add Static Keyframe

commands, either from the keyboard or via the buttons of your control panel. This command alternates

among three modes:

�All: The default mode. Adds keyframes to every track in the Keyframe Editor, keyframing every

parameter in every node all at once, including the Sizing settings. In this mode, an orange bar

appears highlighting the topmost “master keyframe track.”

�Color: Only adds keyframes to the node currently selected in the Node Editor. In this mode, a

green bar appears highlighting the keyframe track corresponding to the node currently selected.

�Sizing: Only adds keyframes to the Sizing track, which is useful when you’re keyframing “pan

and scan” style transforms. In this mode, a blue bar appears highlighting the Sizing track.

�EXT MATTE: Only appears if there’s an external matte node in the node tree. Lets you keyframe

external matte-specific parameters in the Key palette.


Color | Chapter 148 Keyframing in the Color Page

COLOR

Even though All is the default setting, it may be to your advantage to switch to the Color or Sizing

keyframing modes to avoid creating a lot of unnecessary keyframes. Even though keyframing

everything all at once is a fast way to work, the extra keyframes may slow you down when you later

need to make adjustments to nodes that didn’t need to be keyframed in the first place.

To change the keyframing mode, do one of the following:

�Choose an option from the Keyframe mode drop-down at the top right of the Keyframe Editor.

�Choose an option from the Mark > Keyframe Timeline mode submenu.

TIP: This control has one other function. Choosing a mode also affects what is copied when

you use the various grade management tools in DaVinci Resolve. For example, if you choose

Color, then you can copy a clip’s color grade without copying its sizing. If you choose Sizing,

then you can copy the sizing without copying the color grade.

For more information, refrer to “Copying Grades” see Chapter 142, “Grade Management.”

Keyframing Methods

There are two different types of keyframes used by DaVinci Resolve to create automated changes.

Each type of keyframe interpolates parameters differently.

Dynamic Keyframes (Dynamics)

Dynamic keyframes are the most conventional type of keyframe you’ll use, and are the type of

keyframe used for creating animated changes from one state to another. For example, if you need

a grade to become brighter over time to compensate for a change in lighting conditions, you’ll use

Dynamic keyframes.

Nearly every parameter and control in the Color page can be keyframed, but it’s important to

understand that the Interface controls do not animate to match whatever dynamically keyframed

changes are taking place. Instead, visible Interface controls that correspond to keyframed changes will

jump from their initial position at one keyframe to their final position when the playhead reaches the

next keyframe.

This can be most confusing with Curves, which can be interpolated using Dynamic keyframes just like

any other control or parameter. Just keep in mind that the actual settings are animating, even though

the controls are not.

To animate a node using Dynamic keyframes:


Move the playhead in the Keyframe Editor’s Timeline ruler to the frame where you want to

begin a change.


Do one of the following to place a Dynamic keyframe at that frame:

�Choose Mark > Add Keyframe (Command-[).

�Turn on the Auto Keyframe button for the track you want to animate in the Keyframe Editor.

Dynamic keyframes are diamond-shaped.


If necessary, adjust your clip at this first position of your animated change. If you’re using

Auto Keyframe, then you have to make an adjustment for a keyframe to be created.


Color | Chapter 148 Keyframing in the Color Page

COLOR


Now, move the playhead to the frame that is at the second position of the animated change

you’re making, and create another Dynamic keyframe if you’re creating keyframes manually, or

make another adjustment if Auto Keyframe is on.


After you’ve created this second keyframe, make whatever adjustments are necessary to the clip

to create the final look you need.

At this point, playing from the first keyframe to the second keyframe should show a smoothly

animated change from the first adjustment to the second. When you’re finished, make sure you

turn Auto Keyframe off if it was enabled.

Static Keyframes (Marks)

Static keyframes, or marks, are keyframes that are used to create abrupt, one frame changes from

one state to another. They’re typically used to mark edit points separating one shot from another

when multiple shots appear within a single clip. However, Static keyframes are also useful in any

situation where you need a sudden change from one setting to another, such as when creating a

lightning effect.

Static keyframes are round.

To automate a node using Static keyframes:


Find the frame at which you want the abrupt change to take place, and place a keyframe at that

frame by doing one of the following:

�Choose Mark > Make Static Keyframe (Command-]).

�Static keyframes (marks) are round.


Move the playhead to any frame before the keyframe to make changes to the entire segment of

the clip leading up to the keyframe, or move the playhead to any frame after the keyframe to make

changes to the entire segment of the clip appearing after the keyframe. The playhead does not

need to be on top of the keyframe, but if it is, you’ll be adjusting the second portion of the clip.

NOTE: If you’re using Static keyframes to automate grading changes between multiple shots

appearing within a single clip, keep in mind that you can’t add nodes from one keyframe to

the next as you would if you had split the clip in the Edit page.

Mixing and Converting Dynamic and Static Keyframes

Typically, if you’re creating multiple animated changes within a clip, you’ll want to use all Dynamic

keyframes. Similarly, if you’re creating a series of abrupt changes, you’ll use all Static keyframes.

However, you can mix Dynamic and Static keyframes together, so long as you keep in mind the

following rules:


Color | Chapter 148 Keyframing in the Color Page

COLOR

�If you add a Dynamic keyframe to the right of a Static keyframe: There will be no interpolation

from the Static keyframe to the Dynamic keyframe. However, if you add a Static keyframe to the

right of a Dynamic keyframe, there will be interpolation.

No dynamic interpolation following the static keyframe

If you accidentally create the wrong kind of keyframe, it’s easy to convert it into the type of

keyframe you need.

To change one kind of keyframe into another:


Click the keyframe you want to convert to select it.


Right-click the selected keyframe, and choose either Change to Dynamic Keyframe or Change to

Static Keyframe.

Try Creating Keyframed Changes in a Separate Node

One tip to keep in mind is that you don’t have to create keyframed changes within the same

nodes you’re using to create other adjustments. If you want to create some automated

changes without altering the nodes you’ve already adjusted, you can simply create a new

node in which to make your keyframed changes. That way, if you don’t like the result, or you

somehow find yourself hopelessly tangled up in a needlessly complicated set of keyframes,

it’s easy to reset either just the keyframes or the entire node without affecting the rest of

your grade.

Keyframed Nodes Have a Badge

Nodes with keyframed parameters display a keyframe badge in the Node Editor, to make them easy

to find. Note that keyframe badges won’t appear when you simply add a keyframe but only once

there’s an actual keyframed adjustment being made.

Keyframed nodes display a

badge in the Node Editor.


Color | Chapter 148 Keyframing in the Color Page

COLOR

Using Specific Keyframing Tracks

If you’re simply using the Color mode of the All/Color/Sizing command to do keyframing, then you’ll

be adding keyframes to every parameter of the currently selected node whenever you apply a single

keyframe. However, often that’s overkill in situations where you only need to keyframe a single setting

or group of settings.

For example, you may find that you need to keyframe a color adjustment in order to change the color

temperature and brightness when the camera pans across a window, but you don’t want to keyframe

the Windows palette controls because you want to adjust them independently. This can be done by

opening a Corrector track to expose the keyframing tracks within.

Individual keyframing tracks within a Color Corrector node

Keyframing tracks let you keyframe different sets of similarly functioning parameters separately from

one another. For example, there’s one keyframing track for all the color adjustment parameters, and

another keyframing track governing the parameters found within the Qualifier palette.

To reveal a node’s keyframing tracks:

�Click the disclosure triangle next to the number of the node you’re keyframing.

To keyframe an individual keyframing track manually:


Make whatever adjustments you need to the currently selected node, and click its disclosure

triangle to reveal its keyframing tracks.


Move the playhead in the Keyframe Editor to where you want to add the first keyframe, then right-

click within the keyframing track you want to animate, and choose Add Static Keyframe or Add

Dynamic Keyframe (this example shows a Dynamic keyframe).

A keyframe appears at the position of the playhead in that keyframing track.


Move the playhead in the Keyframe Editor to where you want to add the next keyframe, then right-

click within the keyframing track and again choose either Add Static Keyframe or Add Dynamic

Keyframe (this example shows a Dynamic keyframe).


Color | Chapter 148 Keyframing in the Color Page

COLOR

Keyframing just the Circular Power Window using its individual keyframe track

Now, you can make whatever changes you need to the controls governed by the keyframing track

you keyframed, in order to create the necessary animated effect.

TIP: You can also animate individual keyframing tracks using automatic keyframing,

explained in more detail later in this chapter.