---
title: "Playing Stills and Setting Up Image Wipes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 585
---

# Playing Stills and Setting Up Image Wipes

There are many ways to play a still in the Color page, making it visible as an image wipe in the Viewer

and on the external display connected to your video interface.

To play a still, displaying it as an image wipe or full screen, do one of the following:

�Double-click a still in the Gallery.

�Select a still in the Gallery, and click the Image Wipe button on the top Viewer toolbar.

�Click a still in the Gallery, then right-click in the Viewer and choose Show Reference Wipe.

�From the Color > Stills menu, choose Next Still (Option-Command-N) or Previous Still (Option-

Command-B) to select a still in the Gallery, and then choose Wipe On/Off (Command-W) to play it.

�Press PREV STILL or NEXT STILL on the DaVinci Resolve Advanced Search Dial panel, or the

DaVinci Resolve Advanced control panel to select a still, then press PLAY STILL. Press PLAY STILL

again to dismiss the still.

Whenever you play a still, the Viewer mode’s drop-down menu changes to Split mode.

Once displayed, the wipe between the current clip and the still being referenced can be

moved and reoriented in different ways. If you want a full-screen view so you can flip back

and forth between the still and the current clip, simply adjust the split until the still fills the

entire Viewer.

To adjust a wipe in the Viewer, do one of the following:

�Drag the pointer within the Color page’s Viewer to move the wipe.

�Push the T-bar lever up and down on the T-bar panel of the DaVinci Resolve

Advanced control panel.

To customize the type of image wipe that’s displayed

in the Viewer, do one of the following:

�Click any of the controls at the top right of the Viewer toolbar to choose Horizontal, Vertical,

Mix, Alpha, Box, and Difference types of wipe.

�Choose Gallery, Timeline, or Offline from the Reference Wipe Mode submenu in the

Viewer’s option menu.

�Choose Horizontal, Vertical, Mix, Alpha, Difference, and Box from either the Wipe Style submenu

in the Viewer’s option menu, or the style icons at the top of the Viewer.

�Choose Invert Wipe (Option-W) from the Viewer’s option menu.


Color | Chapter 141 Using the Gallery

COLOR

Timeline Wipes

A timeline wipe is when you use the Wipe Timeline Clip command in the Thumbnail timeline (it’s found

in the contextual menu when you right-click a clip other than the current clip) to wipe the current clip

against another clip in the Timeline, without needing to save a still first. When you turn a timeline wipe

on, the clip in the timeline that’s being wiped is outlined in blue.

Gang Timeline Wipe With Current Clip

A “Gang timeline wipe with current clip” option, available from the Viewer option menu, lets you

maintain the offset between the current clip and a timeline clip you’re wiping against when you move

the current clip selection to other clips. With this option enabled, the offset between the timeline

wiped clip and the current clip is maintained when you move the clip selection. When this option is

disabled, the timeline wiped clip stays where it is regardless of what clip you select.

Change a Timeline Wipe Using

the Timelines Album of the Gallery

While you’re using the Wipe Timeline Clip to show a wipe of the current clip against any other

clip in the Timeline, you can open the Timelines album of the Gallery and click different clips to

change which Timeline clip you’re wiping against (outlined in blue) without changing the current clip

(outlined in orange). Make sure you have selected the same timeline in both the Timeline album,

and the Color page.

Labeling and Searching

for Stills and Sources

By default, all stills are identified by a three-number code. The first number is the video track the clip is

on, the second number is the clip’s position number in the current Timeline, and the third number is the

version number of the grade.

If you’ve saved many stills, it can help to label the important ones with whatever text you

find helpful. Once labeled, you can search for stills by label using the Search field, at

the upper right-hand corner of the Gallery.

All stills are numbered Track.Shot.Version


Color | Chapter 141 Using the Gallery

COLOR

Automatic Labeling

If you like, you can choose an option from the Color group in the General Options panel of the Project

Settings to “Automatically label Gallery stills” in different ways. There are many options:

�Clip Name: Saves the Clip Name, which defaults to the File Name unless you’ve customized it.

�Clip Version Name: Automatically saves the name of the current version.

�Source timecode (HH.MM.SS.FF): Saves the source timecode of the current frame.

�Timeline timecode (HH.MM.SS.FF): Saves the timecode for the playhead’s

position in the Timeline.

�Timeline Name: Saves the name of the currently open Timeline.

�Display LUT Name: Saves the name of the currently used Display LUT, if one is applied.

�Custom label using tags: Choosing this option reveals a field you can use to either type custom

text into, or in which you can use metadata variables to save automatically updated information

relating to the currently selected clip and timeline. For more information about using metadata

variables, see Chapter 16, “Using Variables and Keywords.”

For all options, there’s also a checkbox you can toggle:

�Append still number on export: Turning this checkbox on lets you choose how to include the

default still number when exporting stills with the “Use labels on export” option enabled, either as

a prefix or suffix.

Manual Labeling

Sometimes the easiest thing to do is to just give a particular still a custom name that’s representative

of what that still represents, such as “SeemedLikeAGoodIdea.” When naming stills manually, it’s best to

avoid using the forward slash character in case you find yourself exporting these stills with file names.

In fact, it’s a good idea to avoid using the forward slash character for just about any text that you add in

DaVinci Resolve.

To manually label a still:


Right-click a still in the Gallery and choose Change Label or double-click directly under the Still ID.


Type a name into the Change Still Label dialog, and click OK.

The new label appears underneath the still number.

You can also label stills

for easier identification


Color | Chapter 141 Using the Gallery

COLOR

Searching For Stills

Once labeled, you can search for stills you need in the Gallery.

To search for a still by label:

Click the Magnifying Glass button to open the Search field, click to place the cursor within,

and then type the name or description you are searching for.

As soon as you start typing, DaVinci Resolve automatically begins to filter the results of the

currently selected album in the Gallery to match what’s been typed.

Match Reference Wipe Frame

You can right-click any Gallery still and choose Match Reference Wipe Frame to automatically

move the playhead to the exact frame that corresponds to that still, and select that clip in the

Color page Timeline.

Gallery Options

In the upper right corner of the Gallery palette there are several options that let you adjust the view

and organization of your stills.

�Still Size Slider: Dragging this slider to the left makes the still thumbnails smaller, dragging it to the

right makes them larger.

�Sort Stills: Choosing an option from this submenu changes the sort order of all clips in the Gallery.

The options are:

Still ID: Sorts all stills by their assigned ID number (track, clip number, grade version).

Label: Sorts all stills by their text label.

Record Timecode: Sorts all stills by their position in the program.

Source Timecode: Sorts all stills by the timecode of the source clip they came from.

Grab Date: Sorts all stills by the date they were originally grabbed.

Create Time: Sorts stills based on when you saved each still.

�Thumbnail View: Pressing this icon puts the gallery in Thumbnail view; each still is represented

by an image.

�List View: Pressing this icon puts the gallery in List view; each still is represented by

columns of text attributes.

�Search: Opens up a search dialog box, to find stills based on their text label.

�Gallery View: Opens up the full Gallery Management window.

The Gallery options (L-R): Still Size Slider, Sort Stills,

Thumbnail, List, Search, Expand, Options


Color | Chapter 141 Using the Gallery

COLOR

When you right-click the gray area of the Gallery, behind the Still icons, you can open a contextual

menu that provides a variety of additional options for controlling how many stills are saved, how

they’re displayed, and how they’re arranged in the Gallery. There are the following options:

�Switch Wipe Mode: Switches the Reference mode between showing a “Gallery” still, a “Timeline”

clip, or an “Offline” reference movie.

�Trace Timeline: When enabled, selecting a clip in the Timeline also automatically selects the first

still that was saved from that clip to the Gallery.

�One Still Per Scene: When enabled, restricts the Gallery to save only a single still for each clip in

the Timeline. If multiple stills have already been saved before turning this option on, those stills

will remain in the Gallery until you save another still from the same clip, at which time all other stills

from that clip will disappear.

�Apply Display LUT: If you have a Display LUT selected in the Lookup Tables panel of the Color

Management panel of the Project Settings, it’s applied to the video output via a connected video

interface, and also to the Viewer. Ordinarily, you don’t also want the Display LUT applied to stills

you’re saving since it’s meant to be temporary. Accordingly, stills are saved with a LUT-free image.

However, in instances where you may also want to save a reference to the currently used Display

LUT, turning on “Apply Display LUT” saves the Display LUT along with the still, and applies that LUT

when that still is used for split-screen reference. Keep in mind that the internally saved Display LUT

is only used when playing that still in the Viewer; the DPX image that’s saved remains unaffected.

�Apply Grades Using: This submenu contains three options for how to apply the keyframes that are

automatically saved within each saved grade.

No Keyframes: No keyframes are copied. The state of the grade at the frame used to save the still

is what is applied to the target clip or clips.

Keyframes Aligning Source Timecode: Keyframes are copied aligning the source timecode of

the saved grade with the source timecode of the target clip. This is the ideal setting when you’re

copying a grade back to the clip it came from originally, or to a duplicate of that clip elsewhere in

the Timeline, and you want the keyframes to align with the same frames as before. If there is no

source timecode overlap, keyframes will be pasted aligning with the start frame of the edit, the

same as the third option (below).

Keyframes Aligning Start Frames: Keyframes are copied aligning the start frame of the clip

that still was saved from with the start frame of the target clip. This is the ideal setting when

you’re copying a grade with keyframes from one clip to a completely different clip, with

different timecode.

�Use labels on still export: Lets you use labels that you’ve added to stills in the file name of

exported stills.

�Show All Stills: This command shows all available stills in the current album if any have been

hidden, for example by searching or by using the Show Current Timeline Only command.

�Show Current Timeline Only: Choosing this option restricts the Gallery to only showing the stills

that were saved from the currently selected Timeline. All other stills from other Timelines are

hidden until you switch to that Timeline.

NOTE: There are a variety of other commands available in this contextual menu that are

covered elsewhere in this chapter.


Color | Chapter 141 Using the Gallery

COLOR