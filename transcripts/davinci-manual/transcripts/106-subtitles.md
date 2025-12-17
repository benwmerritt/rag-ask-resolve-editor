---
title: "Subtitles"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 106
---

# Subtitles

Subtitles in the Cut Timeline

The Cut page now has the same subtitle support as the Edit page, including the automatic Create

Subtitles from Audio feature.

For more information on how to use subtitles,

see Chapter 52, “Subtitles and Closed Captioning.”

To Add a Subtitle Track in the Cut Timeline:

�Click on the Timeline Actions icon.

�Select Add Subtitle Track from the drop-down menu.

Subtitle Tracks can be minimized in the Cut page to give more room for Audio and Video tracks by

clicking on the Timeline Options icon, and selecting Minimize Subtitle Track.

Create Subtitles from Audio (Studio Version Only)

You can automatically create subtitles from your timeline’s audio tracks by using the DaVinci Resolve

Neural engine to analyze the speech, and automatically turn it into text subtitles.

For more information on automatic subtitling,

see Chapter 52, “Subtitles and Closed Captioning.”

To Automatically Detect and Create Captions from Timeline Audio:

�Open the timeline with the video and audio clips you want to caption.

�Select the Timeline Actions icon and choose Create Subtitles from Audio from the drop-down menu.

Source Tape Editing

While all the features of the Cut page can be used individually, certain features are designed to be

used in conjunction with each other to make your editing experience more streamlined. For example,

combining the File Inspector, Source Tape, Metadata View, and the Navigable Folder Structure can

create a well structured and organized project out of a single folder of unorganized clips.

Metadata Entry Using the File Inspector

The first step in organizing any project is metadata entry. In our initial project we have a large amount

of clips all residing in a single Master Bin. We need to add appropriate metadata to these clips, and to

do this we will be using the File Inspector.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

An unorganized Media Pool in the Cut page

After the File Inspector is open, check the box Auto Select Next Unsorted Clip, and this will

automatically select the same metadata field in the next clip in the Media Pool, after you hit the return

key. Enter in the Scene, Shot, and Take metadata for each clip, based on the information on the slate in

each clip.

Once each clip has its scene, shot, and take metadata, select all the clips in the Media Pool, then enter

the text string “%{Scene}_%{Shot}_%{Take}” in the Name field of the File Inspector. These variables will

replace the clip names for all clips with their scene shot and take numbers separated by underscores,

for example: “02A_CU_03”.

Entering Scene, Shot, and Take metadata in the File Inspector, and renaming all clips via variables

Now make two new bins in the Media Pool, Scene01 and Scene02, and drag all the clips that start with

the name 01 into the Scene01 folder, and all the clips that start with the name 02 into the Scene02

folder. Our metadata entry for this project is now done.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

The Media Pool with all scene 1 clips

in the Scene01 folder, and scene

2 clips in the Scene02 folder

Using the Source Tape

Now turn on the Source Tape, by clicking on its icon in the Viewer. Select Metadata View from the

Media Pool view options, and then Sort By Scene, Shot in the Sort menu. You will now see the clips

clustered by scene in the Media Pool, and all clips from both scenes are laid out in scene order in the

Source Tape viewer. Selecting a specific clip in the Media Pool will snap the playhead to the first frame

of that clip in the Source Tape. From here you can easily see the progression of the shots (take two

follows take one, etc.), and continue your editing from here without having to hunt and click in the

Media Pool.

The Source Tape reflecting all clips in the Media Pool,

and the Metadata View showing the clips clustered by Scene

Limiting the Source Tape Scope by Folder Structure

As your project grows, it can become unwieldy to constantly have an entire film’s worth of media in the

Source Tape. It is possible to limit the scope of the Source Tape at the bin level. As you navigate in the

Source Tape, the current clip is highlighted, and its hierarchy will now appear in top of the Media Pool

title bar. By clicking directly on bins in this bin path, you can quickly broaden or narrow the scope of

the Source Tape. If you click on Scene02, the Source Tape will then zoom in to only show you clips in

that folder. Clicking back on Master will zoom out the Source Tape to show the clips in all folders again.

The navigable folder structure; clicking

on these levels will narrow or broaden

the scope of the Source Tape.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

The Source Tape limited to showing only clips from Scene02

The Source Tape limited to showing only clips from Scene01

The Source Tape broadened to showing all clips in the Master folder

This is also useful when navigating bin structures that reflect the original camera file system. For

example, you may have a camera that records to each memory card as a separate folder, and then

each individual clip is saved as a separate folder inside that folder. When you bring this file system into

the Media Pool using the Create Bins option, these nested levels are mirrored in the Media Pool bin

structure. Now when you click on a card bin in the Source tape, it will directly show you all the clips on

that card, rather than show many individual sub-bins. This view is also viewable in Thumbnail, List, and

Filmstrip views.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Sync Bin Multicam Editing

DaVinci Resolve has a number of tools to make editing multi-camera productions more intuitive and

efficient. If simultaneously recorded clips from different cameras share common timecode, DaVinci

Resolve can automatically sync all of these different camera angles together as you edit. The tools

described in this section act as a sort of digital assistant editor that is constantly searching through

all your media, and presenting all of the relevant shots to you at the exactly the right time. This

functionality, combined with the DaVinci Resolve Speed Editor, makes the Cut page an extremely

powerful multi-camera editor.

Preparing Footage for Sync Bin Editing

In order to properly work with the Sync Bin, every clip in that bin must have the following characteristics.

All Clips Must Have a Common Timecode

Professional video cameras and audio recorders generally have the ability to “jam-sync” their

timecodes together so that each separate video and audio source records the exact same timecode

at the exact same time. Jam-syncing timecode is the quickest, easiest, and most reliable method to

ensure your footage syncs perfectly.

If your footage does not have a common timecode, you will need to go through some extra steps to

ensure that all your material matches up at the correct time. For more information, see the Sync Clips

Window section below.

All Clips Must Have a Unique Camera Name

Most professional video cameras will have some sort of mechanism for naming the camera in its

internal menu system. This camera name is then recorded as metadata in each captured clip, which

can be read automatically by DaVinci Resolve. Cameras should be named either alphabetically

(A, B, C, etc.), or numerically (1, 2, 3, etc.), and in a sequential order totaling the number of cameras that

you are recording with.

If your camera does not automatically record this information (or it’s set incorrectly), you can manually

set the camera’s name by modifying the Camera # field in the Metadata Editor in the Media Pool.

Sync Clips Window

If your footage does not share common timecode, or if the existing timecode needs to be modified for

any reason, the Media Pool in the Cut page offers a Sync Clips window that allows you to modify the sync

of all clips in a bin. It is accessed by clicking on the Sync Clips Window icon on top of the Media Pool.

The Media

Pool Sync Clips

window icon

The Sync Clips window opens and shows a live multi-camera sync Viewer on the left, and a standard

clip Viewer on the right. There is also a timeline below that shows the temporal relationship of all the

clips in the bin.


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

The Media Pool Sync Clips window

Sync By Tools

DaVinci Resolve offers several tools to automatically align your shots into perfect sync.

�Timecode: This button will try to align all the clips in the Sync Clips window by timecode; this is the

default option.

�Audio: This button will try to align all the clips in the Sync Clips window by analyzing the audio

tracks of each clip. In order for this to work, each clip must have at least a portion of the same

audio track recorded clearly enough to analyze. An error message will notify you of which tracks

could not be synced by this method.

�In Point: This button will try to align all the clips in the Sync Clips window by their user set In point.

This is useful if you have a common mark that was shot across all cameras, for example a slate that

claps closed, or a camera flash.

�Out Point: This button will try to align all the clips in the Sync Clips window by their user set

Out point. This is useful if there was a common tail slate.

�Sync: This button will execute the Sync By method selected above.

Once all of the clips in the window are synced appropriately, hit the Save Sync button in the lower

right-hand side of the window.

The Media Pool Sync By icons (L-R: Timecode, Audio, In point, Out point)


The Cut Page | Chapter 28 Fast Editing in the Cut Page

CUT

Manually Syncing Clips in the Sync Clips Window

If none of the Sync By tools is appropriate for the clips in your bin, you can manually sync the clips

together by dragging each clip to the appropriate position on the Sync Clips Window timeline. For finer

control, select the clip you want to sync and press the Comma (,) or Period (.) keys to nudge the clip

backward or forward by one frame. Shift-Comma (,) or Shift-Period (.) nudges the clip by 5 frames

(default), or by the amount of frames set in the “Default fast nudge length” setting in the General

Settings section of the Editing panel in the User settings of the Resolve Preferences. Each clip has its

own track, and you can enable sync lock in the right-hand Viewer to prevent accidental slipping.

Once all of the clips in the window are synced appropriately, click the Save Sync button in the lower

right-hand corner of the window.

Using Your Newly Synced Clips

After saving the sync on your clips, a new Multicam clip will appear in the Media Pool. If you select the

Thumbnail View, a Sync icon appears on all the clips you modified. If you want to modify your sync, right-

click on a thumbnail and select Open Sync Group to reopen your clips in the Sync Clips window. Once

you place your first clip on the Timeline as a reference, you are now ready to use the Sync Bin to edit.

Sync icons (upper left arrows) identifying synced media clips