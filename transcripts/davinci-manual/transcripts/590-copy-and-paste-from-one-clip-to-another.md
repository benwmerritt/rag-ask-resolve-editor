---
title: "Copy and Paste From One Clip to Another"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 590
---

# Copy and Paste From One Clip to Another

The simplest way to copy color adjustments from one clip and apply them to another clip is to use

the same Edit > Copy and Paste commands shared with nearly every other application ever made.

However, you can use this straightforward functionality in one of two ways, depending on the focus of

the interface.

•	 If you click on the clip in the Thumbnail Timeline, you copy and paste the entire grade from

one clip to another.

•	 If you click inside the Node Editor, you copy and paste only the selected node to another

selected node.

You can override this focus-based selection, and make the default behavior to only copy between

nodes rather than entire grades regardless of the interface focus. Do this by checking the “Always

perform copy and paste on selected nodes” box in the Color section of the User panel in Preferences.

Methods of copying and pasting grades and node adjustments.

�To copy and paste an entire grade: Choose a clip with a grade you want to copy, and press

Command-C. Then select the clip you want to copy the grade to in the Thumbnail Timeline, and

choose Command-V to paste the entire grade.

�To copy and paste a single node: Choose a clip with a node you want to copy, and press

Command-C. Then select the clip you want to copy the node to in the Thumbnail Timeline, and

then click anywhere inside the Node Editor. Then choose Command-V to paste the node that was

selected when you copied to the currently selected node in the node tree.

Copy and Paste Specific Parameters Using Paste Value

The Edit > Paste Value (Shift-Option-V) command lets you paste only the value of a specific parameter

into the node of another clip.

To paste only a specific value:


Select a Corrector node with a parameter you want to copy, and press Command-C to copy it.

You’re really copying the entire grade, but that’s okay.


Choose any other node in any grade, and open the palette that contains the parameter you want

to paste into.


Double-click the number field of the specific parameter you want to paste the copied value into.


Choose Edit > Paste Value (Shift-Option-V) to paste that value.

NOTE: Paste Value only works for parameters within palettes; it does not work for OFX or

Resolve FX in the Inspector.

Applying Saved Grades From the Gallery

Every time you save a still into the Gallery or a memory, it contains both the Clip grade, and the

Timeline grade, if one is applied. Which grade is applied from a still using the Apply Grade or Append

Node Graph commands depends on which mode the Node Editor is in. This is selectable from the

drop-down menu in the upper right-hand corner of the Node Editor.


Color | Chapter 142 Grade Management

COLOR

Node Editor Clip and Track selector

If you’re in Clip mode, you’ll only copy the saved clip grade. If you’re in Timeline mode, you’ll

only copy the saved timeline grade.

NOTE: This mechanism also works for saving and applying grades for clips that are in

Groups. The currently selected group grade in the Node Editor determines which grade is

saved with a still, and the currently selected mode in the Node Editor determines where a

saved grade will be applied.

Preparing to Copy or Apply Grades

For all other methods of copying or applying grades described in this chapter, there are some common

methods of controlling how adjustments from the clip or still you’re copying from are applied to the clip

you’re pasting or applying to.

Choosing Which Aspect of a Grade to Apply with All/Color/Sizing

When applying grades using any of the techniques described in this section, you can use the All/

Color/Sizing setting that are available via the Mark > Keyframe Timeline Mode submenu, the drop-

down menu that’s visible at the upper-right of the Keyframes Editor. When copying a grade in

conjunction with the settings in this menu, the following rules apply:

�All: When All is selected, both the grade and the sizing are copied.

�Color: Only the grade is copied, the target clip retains its original Input Sizing settings.

�Sizing: Only the Input Sizing is copied, the target clip retains its original grade.

Choosing How to Copy Keyframes

When copying or applying grades that have keyframes, you can choose how these keyframes are

copied via a setting in the Gallery contextual menu by right-clicking anywhere in the gray background

area of the Gallery, and choosing one of these options from the Apply Grades Using submenu. There

are three options:

�No Keyframes: No keyframes are copied. The state of the grade at the frame used to save the still

is what is applied to the target clip or clips.

�Keyframes Aligning Source Timecode: Keyframes are copied aligning the source timecode of

the saved grade with the source timecode of the target clip. This is the ideal setting when you’re

copying a grade back to the clip it came from originally, or to a duplicate of that clip elsewhere in

the Timeline, and you want the keyframes to align with the same frames as before. If there is no

source timecode overlap, keyframes will be pasted aligning with the start frame of the edit, the

same as the third option (below).

�Keyframes Aligning Start Frame: Keyframes are copied aligning the start frame of the clip that still

was saved from with the start frame of the target clip. This is the ideal setting when you’re copying

a grade with keyframes from one clip to a completely different clip, with different timecode.


Color | Chapter 142 Grade Management

COLOR

From that point on, keyframes, should they exist, will be copied or applied using the selected

method whenever you copy a grade using any of the previously described methods.

Copying Grades Using the Pointer

An incredibly easy way of copying a grade from one clip to another, or from a still or memory in the

Gallery to a clip, is by using the third button of your mouse, usually mapped as the “middle‑click” of the

mouse scroll wheel.

To copy a grade from a clip or still to one or more clips using the pointer:


Select the clip thumbnail you want to copy the grade to in the Timeline; a single selected

clip appears highlighted orange. If you want to copy a grade to several clips, you can either

Command‑click multiple non-adjacent clips, or Shift-click a continuous range of clips; multiple

selected clips appear highlighted red.


Middle-click the clip thumbnail, Gallery still, or memory you want to copy the grade˛from.

The grade of the clip you middle-clicked is copied to the previously selected clip or clips.

TIP: If you’re using a trackpad, third-party software may allow you to define a “three‑finger-

click” that works the same as mouse button 3. If you’re a pen and tablet or trackball user, you

may be able to define a stylus or other button to perform the same button-3 action.

If you don’t have access to a middle-click on the pointing device you’re using, there’s another way of

doing this using a contextual menu command.

To copy a grade from a clip or still to one or more clips using the Apply Grade command:


Select the clip thumbnail you want to copy the grade to in the Timeline; a single selected clip

appears highlighted orange. If you want to copy a grade to several clips, you can either Command-

click multiple non-adjacent clips, or Shift-click a continuous range of clips; multiple selected clips

appear highlighted red.


Right-click the clip thumbnail, Gallery still, or memory you want to copy the grade from, and

choose Apply Grade from the contextual menu.

The grade of the clip you middle-clicked is copied to the previously selected clip or clips.

Copy Forward Commands

Another simple way of copying grades is to use the equals (=) and minus (–) keys on the keyboard to

copy grades forward from one or two clips behind the currently selected clip. This is a great way to

copy grades in scenes with a shot-reverse-shot structure, where you’re cutting between two angles of

coverage, each of which uses the same grade.

To copy grades forward:

�To copy a grade from one clip back: Choose Color > Apply Grade From One Clip Prior, or

press Equals (=).

�To copy a grade from two clips back: Choose Color > Apply Grade From Two Clips Prior, or

press Minus (–).


Color | Chapter 142 Grade Management

COLOR

Copying Using Memories

Memories are virtually identical to stills, except that they’re labeled with a letter (A–Z) for easy access

via keyboard shortcuts. A memory bank above the Gallery browser provides a visual reference

of which saved grade is assigned to which letter. This makes it easy to keep track of multiple

saved memories in instances where you’re copying them to several different clips throughout a

scene or program.

For example, you might save a memory for each angle of coverage in a complicated scene, making it

easy to copy grades forward. In another example, you might save a memory for the grade applied to

each interview subject’s headshot in a documentary, so you can copy that grade forward as you work

through the documentary.

To save the current clip’s grade to a memory for future use, do one of the following:

�Choose Color > Memories > Save Memory A–H (Option-1–8).

If you save a grade to a memory that already contains something, the previous memory is overwritten.

To apply a memory to one or more clips in a timeline, do one of the following:


Choose one or more clips in the Thumbnail timeline to copy to. This can be the current clip, or it

can be a range of clips that you select by Command-Clicking or Shift-Clicking.


Do one of the following to copy a grade to the selected clips:

�Right-click a memory and choose Apply Grade.

�Choose Color > Memories > Load Memory A–H (Command-1–8).

To clear a memory:

�Right-click a memory, then choose Clear.

Copying Using Preview Memory

You can also preview the effect of a memory or saved grade on the current clip, with the option to

either keep it if it works, or go back to the previous grade if it doesn’t.

To Preview Memory:


Move the playhead to a clip for which you want to preview a memory.


Choose Color > Preview Memory (Option-Shift-P).


Do one of the following:

�Right-click any saved still in the Gallery and choose Apply Grade.

�Choose Memories > Load > Memory A–H (Command-1–8).

The selected grade or memory is now being previewed.


Now, do one of the following to either accept or reject the memory:

�If you like the effect, then you can leave it be and move on to another clip.

�If you don’t like the effect, then choosing Color > Preview Memory (Option-Shift-P) again reverts

the clip to the original grade.


Color | Chapter 142 Grade Management

COLOR

Copying from Stills in the Gallery

As mentioned previously, each still you store in the Gallery contains the grading information as well as

the image of the frame it was saved from. This saved grade can be applied to any clip in the Timeline.

IMPORTANT: Copied grades overwrite any previously existing grades on the clip or clips you

copy to.

To apply a grade from a still to one or more selected clips in a timeline:


Choose one or more clips in the Thumbnail timeline to copy to. This can be the current clip, or it

can be a range of clips that you select by Command-clicking or Shift-clicking.


Do one of the following to copy a grade to the selected clips:

�Drag the still from the Gallery into the Viewer.

�Right-click a still in the Gallery and choose Apply Grade.

�Middle-click a still in the Gallery.

�Double-click a still to wipe it in the Viewer against the current clip in the Timeline, then right‑click

the Viewer and choose one of the options from the Apply Grade submenu.

Append Node Graph

You can also append a saved grade to any clip in a timeline. This adds the entire node graph of the

saved still to the end of the node tree of the current clip. In other words, the current clip’s grade isn’t

overwritten, the applied grade is added to the end of it.

By planning ahead, you can save fragmentary grades that create specific effects or adjustments using

only a few nodes. You can then use these fragmentary grades as a toolkit that you can add to other

grades in order to mix and match different adjustments and effects.

For example, you could create a three-node glow effect, save it, and then apply that effect at the end

of a completely different clip’s grade.

Appending grades places them after the original nodes


Color | Chapter 142 Grade Management

COLOR

To append a saved grade or memory as individual nodes, do one of the following:

�Drag a still or memory from the Gallery onto a connection line in the Node Editor; when the

plus icon appears, drop it and its nodes will be appended within the node tree starting at

that connection.

�Right-click a still or memory in the Gallery, and choose Append Node Graph.

Ordinarily, when you append the node graph from a memory or still to another node graph,

you end up adding a whole shedload of new nodes. This may be exactly what you need, but in

situations where you want to keep things a bit tidier, you also have the option of appending node

graphs as compound nodes.

To append a saved grade or memory as a compound node:

�Command-drag a still or memory from the Gallery onto a connection line in the Node Editor;

when the plus icon appears, drop it and its nodes will be appended to the node tree as a single

compound node.

NOTE: When you append the nodes from a gallery still to a grade, how keyframes are

applied depends on the “Apply Grades Using” setting of the Gallery.

For more information, see Chapter 141, “Using the Gallery.”

Aligning Keyframes to a Specific Frame While Copying Grades

If you need to copy a grade with keyframes so that the start keyframe of the copied grade aligns with

a specific frame of the Timeline, you can do so using the following procedure:

To copy a grade and align its keyframes to a specific frame of the Timeline:


Save a grade with keyframes as a Gallery still by right-clicking the Viewer and choosing Grab Still.


Choose the clip you want to copy the saved grade to in the Thumbnail timeline.


Double-click the Gallery still to wipe it against the current clip in the Viewer.


Move the playhead to the frame of this clip you want the first keyframe of the saved grade to be

aligned with.


Right-click the Viewer and choose Apply Grade > Align Keyframes to Current Frame.