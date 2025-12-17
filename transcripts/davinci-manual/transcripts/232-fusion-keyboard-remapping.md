---
title: "Fusion Keyboard Remapping"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 232
---

# Fusion Keyboard Remapping

When using the Fusion page, functions and tools can be mapped to hot keys on your keyboard by

choosing DaVinci Resolve > Keyboard Customization. In the Commands column of the Keyboard

Customization window, select Panels > Fusion Page.

For more information on using the Keyboard Customization window, see Chapter 4, “System

and User Preferences.”

Fusion Studio Keyboard Remapping

When using Fusion Studio, functions and tools can be mapped to hot keys on your keyboard by

choosing Views > Customize Hotkeys.

The Fusion Hotkey Manager dialog is divided into two sections. The left is where you select the

functional area where you want to assign a keyboard shortcut. The right side displays the keyboard

shortcut if one exists. You can use the New button at the bottom of the dialog to add a new

keyboard shortcut.

The Fusion Studio Hotkey Manager window

For instance, if you want to add a shortcut for a specific node:


Open the Keyboard Hotkey Manager.


Select Views > Effect from the Target area of the Hotkey Manager.


Below the Key/Action area, click the New button to create a new keyboard shortcut for the Node.


In the Edit Hotkey window, click the Tools disclosure arrow, and then select Blur to display all the

Blur-related nodes.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION


Select Glow in the Action panel.


At the top of the Edit Hotkey window, type G as the shortcut for the Glow node, and then click OK.


Glow and the G hotkey will now appear in the Key/Action area on the right.


Click OK to close the Hotkey Manager.


Click in the Node Editor and press G to add a Glow node.

Undo and Redo

Undo and Redo commands let you back out of steps you’ve taken or commands you’ve executed and

reapply them if you change your mind. Fusion is capable of undoing the entire history of things you’ve

done since creating or opening a particular project. When you close a project, its entire undo history is

purged. The next time you begin work on a project, its undo history starts anew.

There is no practical limit to the number of steps that are undoable (although there may be a limit to

what you can remember).

To simply undo or redo changes you’ve made one at a time:

Choose Edit > Undo (Command-Z) to undo the previous change.

Choose Edit > Redo (Shift-Command-Z) to redo to the next change.


Fusion Fundamentals | Chapter 64 Exploring the Fusion Interface

FUSION

Chapter 65

Getting Clips

into Fusion

This chapter details the various ways you can move clips

into Fusion as you build your compositions.

Contents

Preparing Compositions in the Fusion Page����������������������������������������������������������������������������������������������������������������������� 1265

Working on Single Clips in the Fusion Page�������������������������������������������������������������������������������������������������������������������������� 1265

Turning One or More Clips into Fusion Clips������������������������������������������������������������������������������������������������������������������������� 1266

Fusion Referenced Compositions���������������������������������������������������������������������������������������������������������������������������������������������� 1268

Adding Fusion Composition Generators����������������������������������������������������������������������������������������������������������������������������������� 1271

Creating a Fusion Composition Clip in a Bin������������������������������������������������������������������������������������������������������������������������� 1272

Resetting a Fusion Clip�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1272

Using Fusion Transitions����������������������������������������������������������������������������������������������������������������������������������������������������������������� 1272

Adding Clips from the Media Pool����������������������������������������������������������������������������������������������������������������������������������������������� 1273

Finding Clips in the Media Pool from the Node Editor������������������������������������������������������������������������������������������������������ 1274

Adding Clips from the File System���������������������������������������������������������������������������������������������������������������������������������������������� 1274

Using MediaIn Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1274

MediaIn Node Inputs�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1274

Inspector Properties of MediaIn Nodes������������������������������������������������������������������������������������������������������������������������������������ 1275

Using Loader and Saver Nodes in the Fusion Page���������������������������������������������������������������������������������������������������������� 1278

Preparing Compositions in Fusion Studio����������������������������������������������������������������������������������������������������������������������������� 1280

Setting Up a Composition�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1282

Reading Clips into Fusion Studio������������������������������������������������������������������������������������������������������������������������������������������������ 1284

Aligning Clips in a Fusion Studio Composition�������������������������������������������������������������������������������������������������������������������� 1285

Loader Node Inputs��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1286

Using Proxies for Better Performance������������������������������������������������������������������������������������������������������������������������������������ 1286

Presetting Proxy Quality������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1287

File Format Options�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1288

Loading Audio WAV Files in Fusion Studio���������������������������������������������������������������������������������������������������������������������������� 1290


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Preparing Compositions in the Fusion Page

Ordinarily, clips come into the Fusion page from the Edit or Cut page Timeline as either a single clip,

or as multiple layers contained within a Fusion clip. You can also add clips to a composition directly

from DaVinci Resolve’s Media Pool. How clips find their way into a Fusion composition can determine

how they function within that composition and what resolution that composition outputs to the rest of

DaVinci Resolve.

Working on Single Clips in the Fusion Page

Positioning the playhead over a clip in the Edit page or Cut page Timeline and clicking the Fusion

page button causes that clip to appear in the Fusion page as a single MediaIn node connected to a

MediaOut node. Only the topmost visible clip is taken into Fusion. Clips that aren’t visible because

they’re on lower tracks with clips above them are ignored, unless you disable the clips or tracks that

appear above. These very simple default compositions are referred to unofficially in this manual as

“single-clip compositions.”

The MediaIn node represents the image that’s fed to the Fusion page for further work, and the

MediaOut node represents the final output that’s fed onward to the Color page for grading.

The default node tree that appears when you first open the

Fusion page while the playhead is parked on a clip.

This initial node structure makes it easy to quickly use the Fusion page to create relatively simple

effects using the procedural flexibility of node-based compositing.

For example, if you have a clip that’s an establishing shot, with no camera motion, that needs some

fast paint to cover up a bit of garbage in the background, you can open the Fusion page, add a Paint

node, and use the Clone mode of the Stroke tool to paint it out quickly.

A simple paint effect applied to a shot with no camera motion.

TIP: The resolution of a single clip brought into Fusion via the Edit or Cut page Timeline is the

resolution of the source clip, not the Timeline resolution.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Once you’ve finished, simply go back to the Edit or Cut page and continue editing, because the

entire Fusion composition is encapsulated within that clip, similarly to how grades in the Color page

are also encapsulated within a clip. However you slip, slide, ripple, roll, or resize that clip, the Fusion

effects you’ve created and the Color page grades you’ve made follow that clip’s journey through your

edited Timeline.

TIP: While you’ll likely want to do all the compositing for a greenscreen style effect in

the Fusion page, it’s also possible to add a keyer, such as the excellent DeltaKeyer node,

between the MediaIn and MediaOut nodes, all by itself. When you pull a key this way, the

alpha channel is added to the MediaOut node, so your clip on the Edit page has transparency,

letting you add a background clip on a lower track of your Edit page Timeline.

How Nodes Are Named

While the documentation refers to nodes by their regular name, such as “MediaIn,” the actual names

of nodes in the Fusion Node Editor have a number appended to them, to indicate which node is which

when you have multiple instances of a particular type of node.

Turning One or More Clips into Fusion Clips

For situations where you know you’re creating a more ambitious composited effect that requires

multiple layers edited together with very specific timings, you can create a “Fusion clip” right from the

Timeline. For example, if you have a foreground greenscreen clip, a background clip, and an additional

graphic clip, you can stack them all on the Timeline as superimposed clips. You can then use the Edit

page slip and slide features to align their timings so they work together as necessary. You can also

edit multiple consecutive clips together that you want to use in a composition as a series of clips. Once

that’s done, you can select every clip in the stack to create a Fusion clip, so you can easily use all

these superimposed layers within a Fusion composite.

To create a Fusion clip:


Edit all the clips you want to use in the Edit page Timeline.


Select all clips you want to be in the same composite at once.


Right-click one of the selected clips and choose New Fusion Clip from the contextual menu.


A new clip, named “Fusion Clip X” (where X is an automatically incrementing number) appears

in the currently selected bin of the Media Pool and in the Timeline to replace the previously

selected clips.


With the playhead parked over that clip, open the Fusion page to see the new arrangement of

those clips in the Fusion page Node Editor.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

A stack of clips to use in a composite (Top), and turning that stack into a Fusion clip in the Edit page (Bottom).

The nice thing about creating a Fusion clip is that every superimposed clip in a stack is

automatically connected into a cascading series of Merge nodes that create the desired

arrangement of clips. Note that whatever clips were in the bottom of the stack in the Edit page

appear at the top of the Node Editor in the Fusion page, but the arrangement of background and

foreground input connections is appropriate to recreate the same compositional order.

The initial node tree of the three clips we turned into a Fusion clip.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

TIP: Fusion clips change the working resolution of the individual clips to match the Timeline

resolution. For instance, if two 4K clips are stacked one on top of the other in an HD Timeline,

creating a Fusion clip resizes the clips to HD. The full resolution of the individual 4K clips is

not available in Fusion. To maintain the full resolution of course clips, bring only one clip into

the Fusion composition from the Edit or Cut page Timeline, and then bring other clips into the

Fusion composition using the Media Pool.