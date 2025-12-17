---
title: "Rippling Adjustments Among Multiple Clips"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 592
---

# Rippling Adjustments Among Multiple Clips

If you’ve graded a sequence of clips and find yourself needing to make a quick change to several clips

all at once, you can use the Color > Ripple Node Changes to Selected Clips/Current Group commands

to quickly copy changes made to one clip to several others. However, these commands require that

you follow certain rules in order to get the results you want.

Node rippling uses the number of each node to determine what changes should ripple to which

nodes. In other words, changes made to Node 3 will ripple to Node 3 of every other selected clip, or to

Node 3 of every other clip in the current group (depending on which command you use).

Rippling changes from one clip to several others requires that all clips share the same number of

nodes, at least for the nodes you’re rippling. If you try to ripple a change to one or more clips that

don’t have a node with the same number as the one you’re rippling, then no change will be rippled to

those clips.

To ripple a change in one node to several selected clips:


Select the clip you want to use to make the change so that it’s the current clip, outlined in orange.


Now, Command-click or Shift-click to select the range of clips you want to ripple your change to,

so that they’re all selected red.

The orange outlined clip is the current clip you’re modifying, and the clips

highlighted in red are the ones you’re rippling this change to

You don’t have to select the clips you’re going to ripple your change to prior to making the change,

but it may be easier to keep track of what you’re doing if you set everything up in advance. The

clip you’re changing should be outlined in orange, and the clips you’re rippling the change to

should be highlighted in red.


Select a node to modify. Ideally, every selected clip should have a node sharing the same number

as the one you’re modifying. If some clips don’t, then those clips won’t inherit the change you’re

going to be rippling.


Make whatever changes you need to, adjusting any of the palette controls in the Color page you

need to, except for Camera Raw, Sizing, and Data Burn, which aren’t node‑specific.


When you’re happy with the change you’ve made, choose Color > Ripple Node Changes to

Selected Clips.

The change you’ve made should ripple to every other selected clip with a node of the same

number, and in a few moments the thumbnails of those clips should update to show the change.

If you’ve created a group, it’s even easier to ripple node adjustments to the other clips in

the group.


Color | Chapter 142 Grade Management

COLOR

To ripple a change in one node to the current group:


Select the clip you want to use to make the change so that it’s the current clip, outlined in orange.

It must be part of a group for this to work.


Select a node to modify. Ideally, every selected clip should have a node sharing the same number

as the one you’re modifying. If some clips don’t, then those clips won’t inherit the change you’re

going to be rippling.


Make whatever changes you need to, adjusting any of the palette controls in the Color page you

need to, except for Camera Raw, Sizing, and Data Burn, which aren’t node‑specific.


When you’re happy with the change you’ve made, choose Color > Ripple Node Changes to

Current Group.

The change you’ve made should ripple to every other clip in the current group that has a node of the

same number, and in a few moments the thumbnails of those clips should update to show the change.

Appending a Node to Multiple Clips

If you’ve made an adjustment to a node in one clip that you’d like to apply to several other clips, you

can quickly do that using the Color > Append Node to Selected Clips command. You can do this as a

prelude to using one of the Ripple Node Change commands, as it’s a quick way to make sure several

previously ungraded clips have the same nodes, but you can also do this as a quick way to apply the

same node change to several clips, regardless of whether they have matching node trees.

To append a node to other selected clips:


Select the clip you want to use to make the change so that it’s the current clip, outlined in orange.


Select the node you want to append to other clips.


Now, Command-click or Shift-click to select the range of clips you want to ripple your change to,

so that they’re all selected red.

The clip you’re copying from should be outlined in orange, and the clips you’re rippling the change

to should be highlighted in red.


Choose Color > Append Node to Selected Clips.

The selected node should be appended to the end of the node tree of each selected clip, and in a

few moments the thumbnails of those clips should update to show the change.

Using Shared Nodes

Shared nodes are meant to be a way to extend the benefits of automatically rippled changes among

different clips to colorists that prefer a flatter node structure than Group Grading allows. By turning

individual Corrector nodes into Shared nodes, and copying these to multiple clips, you enable linked

adjustments right from within the clip grade. This means that the clip grade can freely mix both clip-

specific nodes and Shared nodes, all within the same node tree. This makes Shared nodes fast to use

as there’s no need to create groups or switch to a group node tree (covered in the next section) to

reap the benefits of linked adjustments among multiple clips.

A grade with an Unshared (at left) and Shared node (at center), a badge

indicates the Shared node, which is also locked


Color | Chapter 142 Grade Management

COLOR

What Are Shared Nodes Good For?

Shared nodes are similar to group grades, except that they don’t require grouping and can be added

to any normal grade. Changes made to a Shared node are automatically rippled to all other instances

of that node in the grades of other clips. Furthermore, you can add as many Shared nodes to a grade

as you like, and you can arrange them in any order to control the order of the operations they apply.

And, of course, you can intersperse them with ordinary Corrector nodes

Shared nodes are extremely flexible. For example, you can use Shared nodes to:

•	 Add a Color Space Transform Resolve FX or a LUT to the beginning of every clip

from a particular source

•	 Add a base correction to every talking head shot of a particular interviewee

•	 Add a shot matching adjustment to each clip from a particular angle of coverage

within a scene

•	 Add a stylistic adjustment to every clip in a specific scene

•	 Make your base adjustments when grading with remote versions, so those adjustments

remain linked when you copy your remote versions to local versions for fine tuning

In fact, you can mix and match Shared nodes among differently overlapping sets of clips to

accomplish any or all of the above at once. For example, you can add one Shared node to

make an adjustment to every clip from a particular camera, add a second Shared node to each

of those clips that are in a particular scene, and then add a third Shared node to whichever

of those clips happen to be a closeup of the lead actress, before adding one or two regular

Corrector nodes that aren’t shared to make clip-specific tweaks.

Creating Shared Nodes

Creating a Shared node is easy, assuming you’ve created a node that has an adjustment you’d like to

share among multiple clips.

To create a Shared node:

�Right-click any Corrector node and choose Save as Shared node.

Locking Shared Nodes

Once you turn a node into a Shared node, that node is automatically locked, preventing you from

accidentally making adjustments to it that would affect all other grades using that same Shared node.

To toggle the locked status of a Shared node, do one of the following:

�Right-click any Shared node and choose Lock Node from the contextual menu.

�Open the Keyframe Editor, and click the Lock icon in the track header of that node’s

keyframe track.

Copying Shared Nodes

Because Shared nodes are essentially Corrector nodes within clip grades, they’re easy to work with.

Once you’ve created one or more Shared nodes, there are a variety of ways you can copy them to the

grades of other clips in your program to take advantage of the linked adjustments they let you make.


Color | Chapter 142 Grade Management

COLOR

Ways of copying Shared nodes among multiple clips:

�Add a Shared node to another clip’s grade using the Node Editor contextual menu: Once you

save a node as a Shared node, it becomes available from the bottom of the Add Node submenu

of the Node Editor contextual menu, making it easy to add any Shared node to any clip. If you

customize the label of the Shared node, that custom label appears in the contextual menu, making

it easier to find what you’re looking for.

�Add Shared nodes to a basic grade you’ll be copying to other clips: If you create one or more

Shared nodes when you initially build a grade, copying that grade to other clips naturally copies

the Shared nodes as well.

�Save a Shared node as a Gallery still and apply it to other clips: If you save a grade with a

Shared node in it to the Gallery, then every time you copy that Gallery still to another clip, you

copy its Shared node.

�Create a Shared node and append it to a selection of additional clips: If you’ve already graded

several clips in a scene, you can add a Shared node to the end of one of the clips grades and

make sure it’s selected, then select all of the other clips in the scene and choose Append Node

to Selected Clips.

�Use Shared nodes to preserve linked adjustments when copying remote grades

to local grades: If you use Shared nodes to make your base adjustments when you grade using

Remote Versions to automatically copy those grades to other clips that come from the same

source media, those adjustments will remain linked when you copy your remote versions to local

versions for fine tuning.

You can also choose options in the Gallery that dictate what happens when you copy a grade that has

shared nodes within it.

Converting Shared Nodes Back to Corrector Nodes

Sometimes you need to stop a node from being shared. For example, if you want to copy a grade from

another scene to use as the starting point for a new grade, chances are you don’t want any shared

nodes to continue being shared as you customize that grade for the new scene. In this instance, you

can convert the Shared node back to a regular Corrector node, make any adjustments you need to

customize it for the new scene, and then turn that node into a brand new Shared node that’s specific

to the new scene.

To convert a Shared node back to a Corrector node:

�Right-click any Shared node, and choose Convert to Corrector from the contextual menu.

Deleting Shared Nodes

If you’ve created a Shared node that’s being used in multiple clips, and you decide you want to

eliminate the linked relationship among these nodes so they all work independently, you can “delete”

a specific Shared node. This leaves the now unlinked nodes intact within each node tree in which they

appear, but clears their effect. Additionally, that Shared node is removed from the Add Node submenu.

To Delete a Shared node:

�Right-click any Shared node, and choose a node to delete from the Delete Shared Node submenu.


Color | Chapter 142 Grade Management

COLOR

Using Adjustment Clips

You can also apply a single grade to multiple clips in the Timeline using Adjustment clips that have

been superimposed over numerous other clips in the Timeline. They can be used to apply a single

grade to all clips in a scene, or to add further color adjustments or trims to a section of clips via a

second grade that’s applied on top of the individual clip grades that are already applied.

Adjustment clips are a great way to add adjustments to multiple clips that you may be making frequent

changes to. If you make changes to a grade in an Adjustment clip, that change is automatically applied

to all clips underneath it in the Timeline. Additionally, grades applied via adjustment layers can be

turned off by disabling the adjustment layers, either one at a time, or by disabling an entire track with

adjustment layers in it.

An Adjustment clip (shown selected in the Mini Timeline)

used to apply a cooler grade to four other clips in a scene

Adjustment clips can be edited into the Timeline on the Edit page, and are available from the

Effects bin of the toolbox in the Effects Library. When an Adjustment clip is superimposed above one

or more clips in the Timeline, all effects that are applied to the Adjustment clip are also applied to all

clips underneath it.

Adjustment clips can be used to apply the following types of effects:

�ResolveFX and OpenFX plugins

�Inspector parameters, including Composite, Transform, Cropping, and Dynamic Zoom

�Fusion page effects

�Color page grading and sizing


Color | Chapter 142 Grade Management

COLOR

Effects clips are a fast and easily revised way to apply one or more grades and effects to a

range of clips.

TIP: Multiple adjustment layers can be grouped together so that you can apply Group and

Clip grades to adjustment layers, linking multiple adjustment layers together in situations

where you want to apply the exact same trim or stylistic adjustment to multiple scenes in non-

contiguous areas of the Timeline.