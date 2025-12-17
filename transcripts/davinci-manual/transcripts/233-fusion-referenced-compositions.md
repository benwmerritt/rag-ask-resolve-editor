---
title: "Fusion Referenced Compositions"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 233
---

# Fusion Referenced Compositions

There is a newer powerful way of applying Fusion composites to your clips called a “Referenced

Composition.” This method allows you to reuse your work across multiple clips or even timelines.

You create a referenced composition on the Edit page by selecting a single clip, or a stack of clips,

and then select “Create Referenced Composition” from the contextual menu. This generates a Fusion

Referenced Composition in the Media Pool. You can enter the Fusion page to start compositing or

double-click the Referenced Composition in the Media Pool to open it.

Referenced comps can be linked to other clips in any timeline by selecting the referenced comp,

then right-clicking the target clip and selecting “Link to Referenced Composition.” Any changes

you make are applied across all connected clips because they are all “referred” or “linked” to

the same composition.

Referenced Compositions are an effective and secure way to keep your work backed up and

organized, as they live in the Media Pool and will persist even if the original referenced clip is deleted

from the timeline.

Creating and Managing Referenced Compositions

To create a Referenced Composition:


Select one or more timeline clips that are “stacked” on tracks in an Edit window timeline (clips

have to overlap in time at least partially).


Right-click and select “Create Referenced Fusion Composition.”


The new reference composition, associated with the top selected clip, now appears in the

Media Pool.

You can open the referenced composition in the Fusion page by double-clicking on it in the

Media Pool. Media nodes match the relative locations of the source track clip arrangement in the

Edit timeline.

The contents of the video track are treated as a source, allowing creative manipulation of clips before

they’re passed on to Fusion for compositing.

You can right-click on a referenced composition in the Media Pool and choose the Usage option to

view and navigate to its target linked clips.

You can duplicate your referenced composition for iteration purposes.

In the example below we create a simple reference composition out of three clips, replacing a logo

on a truck.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Creating a reference composition by selecting multiple overlapping clips, and

then Create Referenced Composition from the contextual menu.

The Reference Composition

thumbnail in the Media Pool

Double-clicking on the Reference Node brings us into Fusion, where we add some Corner Positioner

nodes to line up the green stripe and logos to fit.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Now that we have the referenced composition set, we can easily change the logo, just by performing

a replace edit with the new logo to V3 in the timeline. The new logo is automatically applied in the

Fusion comp with the same settings.

The sBSpline controls

Adding Additional Referenced Clips

Once you’ve established a referenced composition, you can add clip(s) that can use the referenced

composition to affect the other clips.

To add clip references to a referenced composition:


Select the referenced composition that you want to refer to another clip.


Select a target clip in the timeline, right click and choose “Link to Referenced Composition.”


Add other clips, one a time if you wish, including clips from other timelines.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Referenced Composition Behaviors and Rules

There are some additional behaviors and rules to be aware of when using referenced compositions.

�Referenced compositions maintain the original source resolution of your clips.

�When selecting multiple clips, ensure that the clips have some overlap with the top selected clip.

Without this overlap, the context menu action to create a referenced composition across layers is

not available.

�When creating a project composition from multiple overlapping clips, a single composition

associated with the top selected clip is created.

�The referenced composition features additional Media In nodes (one per track). Media In 1

refers to the top selected clip. Subsequent Media In nodes reference timeline tracks (layers)

below the top clip.

�Removing a timeline clip will not remove the associated composition.

�When you edit the contents in a referenced composition’s track, the corresponding Media In

refreshes to automatically to show the new clips, edits, effects, and transitions.

From the timeline clip’s context menu, you can:

•	 Reset Reference Composition: To reset the composition. This affects all referenced clips.

•	 Unlink Reference Composition: To remove the composition reference from the

selected clip. This retains the composition in the Media Pool, but the clip effect is cleared.

Useful if you want to link to another referenced composition.

•	 Find Reference Composition in Media Pool: To find the reference composition the clip is a

part of in the Media Pool.

NOTE: Clips of differing frame rates or clips with speed changes are not supported in

referenced compositions.

Adding Fusion Composition Generators

The Generator category of the Edit page Effects Library has a Fusion Composition generator. It’s

useful for creating an empty placeholder in the Timeline that you later want to work on in the Fusion

page to create a more fully-featured Fusion composition.

To create a blank Fusion clip in the Edit page:


Open the Effects Library, and select the Effects category.


Edit a Fusion Composition clip into the Timeline in whichever way is most convenient.

a)	 You can drag a Fusion Composition clip into the Timeline, which will result in a clip that’s the

length of the “Standard generator duration” preference, which is 5 seconds by default.

b)	 You can set In and Out points in the Timeline, and drag the Fusion Composition clip onto any

of the editing overlays of the Timeline viewer to perform that sort of edit to insert, overwrite,

“place on top,” or ripple overwrite it into a specific place in the Timeline, for a specific duration.


A new clip named “Fusion Composition” appears in the Timeline. It initially displays only black in

the Timeline viewer, since it’s a blank composition with no contents.


With the playhead parked over that clip, open the Fusion page. Since this composition is blank,

there’s only a single MediaOut node in the Node Editor. At this point, you can add whatever media,

generators, and other effects you require.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Creating a Fusion Composition Clip in a Bin

You can create an empty Fusion Composition clip in any bin in the Media Pool without creating a

Timeline. This method can be useful for creating motion graphics or titles when there is no Timeline or

when you plan on using the clip in multiple Timelines.

To create a blank Fusion Composition clip in a bin:


Select the bin in the Media Pool where you want to save the Fusion Composition.


Right click in an empty area of the bin and choose New Fusion Composition.


In the New Fusion Composition clip dialog, enter a Name for the clip, a duration, and a frame rate,

and then click Create.


The clip will appear in the bin. To open it in Fusion, do one of the following:

�Double-click the Fusion Composition

�Right-click over the Fusion Composition clip and choose Open in Fusion Page

Resetting a Fusion Clip

To reset a Fusion clip back to its initial default state, right-click on the Fusion clip in the Edit page

Timeline, and select Reset Fusion Composition. You can select multiple Fusion clips and reset

them at once.

Using Fusion Transitions

Specific Fusion transitions are available in the Edit page Effects Library. You can use these transitions

to bring two clips and the transition between them into the Fusion Page. These transitions can then be

modified and saved back to the Edit page Timelines or saved as a new, reusable Fusion Transition that

appears in the Edit Page Effects lIbrary.

To apply and open a Fusion Transition:


Open the Effects Library, and select the Video Transitions category.


Scroll to the bottom of the transition list and drag one of the Fusion Transitions onto a cut in

the Timeline.


Right-click over the Fusion Transition in the Timeline and choose Open in Fusion Page.


The Fusion page opens with two MediaIn nodes representing the two sides of the transitions.

The MediaIn nodes connect to a cross dissolve or a group of nodes used to create the transition.

At this point, you can modify the transition using masks or other nodes and return to the Edit page

to see the results.

A Noise Dissolve Transition opened in the Fusion page.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

To learn about creating custom Fusion Transitions that appear in the Effects Library, see

Chapter 68, “Node Groups, Macros, and Fusion Templates,” in the DaVinci Resolve Reference

Manual or Chapter 6 in the Fusion Reference Manual.