---
title: "Organizing Smart Bins"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 75
---

# Organizing Smart Bins

Manually created Smart Bins can be organized into Folders and Sub-Folders for better sidebar

management, just like regular bins.

Smart Bins organized into folders

To add a Smart Bin folder:

Right-click in the Smart Bins area and choose Add Folder from the contextual menu to create folders

that you can drag Smart Bins into. Each folder has a disclosure triangle, so you can show or hide

its contents.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Another benefit of Folders is that when you select a Folder, you can see the full contents of all Smart

Bins inside of it in the Media Pool browsing area. Selecting any one Smart Bin then restricts the Media

Pool to showing only the media reference by that Smart Bin.

Folders can be renamed, removed, opened as a new window, or sorted along with all other Smart Bins

by right-clicking them and using commands in the contextual menu.

Duplicating Clips in the Media Pool

You can duplicate clips in order to create an instance of that media that’s treated as a completely new

source clip, entirely separate from the original instance of that clip that was imported into DaVinci

Resolve. The duplicate is capable of storing individualized metadata and markers that are completely

distinct from the original clip that was imported into your project.

To duplicate one or more clips:


Select one or more clips to duplicate.


Do one of the following:

�Choose Edit > Duplicate Clip

�Hold the Option key down while dragging one or more selected clips to another bin

�Right-click a clip in the Media Pool, and choose Duplicate Clip from the Contextual Menu

Adding Clips From the Timeline to the Media Pool

You can also drag one or more clips from the Timeline back into the Media Pool to create a duplicate.

As with duplicating clips in the Media Pool, each duplicate is created as a new source clip that’s

entirely separate from the original instance of that clip that was imported into DaVinci Resolve and is

capable of storing individualized metadata and markers that are completely distinct from the original

clip that was imported into your project.

For example, the original clip in the Timeline remains conformed to the original clip that was first

imported into the Media Pool; deleting the original clip from the Media Pool will make that clip “non-

conformed” in the Timeline, while the duplicate you just created remains linked and available. If

you’re in this situation, you can always turn Conform Lock Enabled off for that clip in the Timeline and

reconform the Timeline Clip to the duplicate you just created, but that’s an extra step because the

duplicate clip is considered by DaVinci Resolve to be a whole new piece of media that just happens to

share the same clip details.

This may seem strange, but there are a variety of finishing workflows that use this capability, so it’s

good to know about.

Duplicating Timelines

Timelines can be duplicated for a variety of reasons: to create a backup of a timeline at a specific date,

to create a variation of an edit, or to create separately graded versions.

To duplicate a Timeline:

�Select a Timeline in the Media Pool, and choose Edit > Duplicate Timeline.

�Press Command-4 to give focus to the Timeline, and choose Edit > Duplicate Timeline.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Choosing How to Display Bins

Once you’ve created a bin structure for your project, you can customize how your bins are displayed,

depending on how you like to work.

Showing Bins in Separate Windows

If you right-click a bin in the Bin list, you can choose “Open As New Window” to open that bin into its

own window. That window is basically its own Media Pool, complete with its own Bin list, Power Bins

and Smart Bins lists, and display controls.

Multiple Media Pool bins opened as new windows

When multiple Media Pool windows are open, the Workspace > Media Pool Windows submenu lets

you bring a floating Media Pool window into focus when you have one or more open and hidden.

This is most useful when you have two displays connected to your workstation, as you can drag these

separate bins to the second display while DaVinci Resolve is in single screen mode. If you hide the

Bin list, not only do you get more room for clips, but you also prevent accidentally switching bins if you

really want to only view a particular bin’s contents in that window.

Using the Media Pool in Thumbnail View

If you work in Thumbnail view using the controls at the top right of the Media Pool, you have the option

to resize the thumbnails to make them easier to see, and you can move the mouse pointer over each

clip to hover scrub through its contents. Clicking any clip to select it displays it in the Media page

Viewer. Whichever clip is currently selected is also output to video for monitoring.

In Thumbnail view, you can use the Sort Order drop-down, at the top right of the Media Pool, between

the Icon Size slider and the Icon/List view buttons, to choose how clips are sorted. There are fourteen

options: File Name, Reel Name, Clip Name, Start TC, Duration, Type, FPS, Audio Ch, Flags, Date

Modified, Date Created, Shot, Scene, and Take.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Custom Sort of Clip Thumbnails in the Media Pool

You can now manually reposition Media Pool clips in Thumbnail view, allowing you to group clips

together in any way that visually makes sense to you.

You can turn on Custom Sort by selecting Custom in the Sort menu in the Media Pool.

Select Thumbnail View in the Media Pool, and from the sort menu select Custom. Then you can

drag your thumbnails around in any order or grouping that you wish. If Snap to Grid is selected in the

Sort menu, the icons will line up in neat rows and columns. Turn off Snap To Grid to enable freeform

positioning. If two thumbnails are overlapping, the last one moved will show on top.

With Snap to Grid deselected you can rearrange thumbnails in any way (even overlapping),

and it is retained throughout the Medial Pool on all pages.

The position of your icon thumbnails are persistent in the Media Pools across all pages in DaVinci

Resolve. The positioning is also retained if you temporarily choose another sort order, and then return

to the Custom sort.

Working With Columns in List View

If you work in List view using the controls at the top right of the Media Pool, you gain additional

organizational control by exposing columns that show the metadata that each clip contains, prior to

media being added to your timeline. You can use these columns to help organize your media.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Methods of customizing metadata columns in List view:

�To show or hide columns: Right-click at the top of any column in the Media Pool to reveal the

column list, and while the column list is open, click the checkboxes of any columns you want to

show or hide. Unchecked columns cannot be seen. When you’re finished, click anywhere else in

the Media Pool to dismiss the column list.

�To rearrange column order: Drag any column header to the left or right to rearrange

the column order.

�To resize any column: Drag the border between any two columns to the right or left to narrow or

widen that column.

�To sort by any column: Click the column header you want to sort with. Each additional time you

click, the same header toggles that column between ascending and descending sort order.

Once you’ve customized a column layout that works for your particular purpose, you can save it for

future recall.

Methods of saving and using custom column layouts:

�To create a column layout: Show, hide, resize, and rearrange the columns you need for a

particular task, then right-click any column header in the Media Pool, and choose Create Column

Layout. Enter a name in the Create Column Layout dialog, and click OK.

�To recall a column layout: Right-click any column header in the Media Pool, choose the name of

the column layout you want to use from the contextual menu, and choose Load from that item’s

submenu. All custom column layouts appear at the top of the list.

�To edit a column layout: Load the column layout you want to edit, make whatever changes you

need to, then right-click any column header in the Media Pool, choose the name of the column

layout you just edited from the contextual menu, and choose Update from that item’s submenu.

�To delete a column layout: Right-click any column header in the Media Pool, choose the name

of the column layout you want to delete from the contextual menu, and choose Delete from

that item’s submenu.

While the available columns of metadata correspond to those fields shown in the Metadata Editor,

the available columns in the Media Pool of the Media and Edit pages are a subset of the total amount

of metadata that’s available, although they represent the most commonly used metadata you’ll find

yourself referring to when editing and finishing.

The available columns in List view include:

Angle: An editable field to contain the angle of the media in a multi-camera shoot.

Audio Bit Depth: The bit depth of any audio channels in the media file.

Audio Ch: The total number of audio tracks in the media file.

Audio Codec: The specific codec used by the audio portion of the media file.

Audio Offset: Lists the audio offset, in frames, for clips that have been synchronized to separately

recorded audio. This parameter is editable in the Media Pool.

Bit Depth: The bit depth of the media file.

Camera #: The number assigned to a specific camera.

Clip Color: The current color assigned to that clip.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Clip Name: Editing the Clip Name lets you change the name with which clips appear throughout

DaVinci Resolve when View > Use Clip Name for Clip Titles is enabled. By default, the clip name mirrors

the source clip’s file name. When editing the clip name in the List view of the Media Pool, you can use

“metadata variables” that you can add as graphical tags that let you reference clip metadata.

For example, you could add the corresponding metadata variable tags %scene_%shot_%take and that

clip would display “12_A_3” as its name if “scene 12,” “shot A,” “take 3” were its metadata. The clip name

can also be edited in the Clip Attributes window.

For more information on the use of variables, as well as a list of all variables that are available in DaVinci

Resolve, see Chapter 16, “Using Variables and Keywords.”

Comments: A user-editable field for entering information about that clip.

Data Level: The data level setting for the media file.

Date Created: The date the media file was created.

Date Modified: The last date the media file was modified.

Description: A user-editable field for entering information about that clip.

Duration: The total duration of the clip, in timecode.

End: The last frame number of the media file.

End TC: The timecode value of the last frame in the media file.

FPS: The frame rate of the media file.

File Name: The name of the file on disk that clip is linked to.

File Path: The file path where that media file is located on disk.

Flags: Which flags, if any, have been added to a media file.

Format: The image format used by that clip, such as QuickTime, MXF, WAVE, and so on.

Frame/Field: Whether that media file is progressive or interlaced.

Frames: The total duration, in frames.

Good Take: An editable field to contain the circled state of media, relative to the

script supervisor’s notes.

H-FLIP: Whether that media file is horizontally flipped in DaVinci Resolve.

HDRX: Only displayed for R3D media, indicates whether or not it’s HDRX media.

IDT: If ACES color science is selected in the Color Management panel of the Project Settings, the IDT

used by that clip is listed here.

In: The timecode value of the In point, if any, that’s stored for that clip.

Input Color Space: If Resolve Color Management is selected in the “Color Science” menu of the

Color Management panel of the Project Settings, then this column will show the Input Color Space that

has been assigned to each clip. By default, all clips inherit the Input Color Space setting that’s been

selected in the Color Management panel of the Project Settings.

Input LUT: Which input Lookup table has been assigned, if any.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Input Sizing Preset: The currently selected Input Format Preset, if there is one.

Keyword: A user-editable field for entering searchable keywords pertaining to that clip. Only shows clip

keywords, not marker keywords.

Offline Reference: Lists the offline reference video that has been assigned to a given timeline.

Optimized Media: Populated with the resolution of whatever optimized media you’ve created

(Original, Half, Quarter, and so on). Clips that have not been optimized appear with “None.”

Out: The timecode value of the Out point, if any, that’s stored for that clip.

PAR: The pixel aspect ratio, if assigned.

Reel Name: The reel name of that clip. Dynamically generated by the “Assist using reel names from the”

setting in the General Options panel of the Project Settings.

Resolution: The frame size of the media file.

Roll/Card: An editable field to contain the roll number of media that was scanned from film.

S3D Sync: Shows a frame count when you slip an eye to fix non-synced timecode using

the “Slip Opposite Eye One Frame Left/Right” commands. This parameter is editable in the Media Pool.

Sample Rate: The sample rate of the media file’s audio, if there is any.

Scene: An editable field to contain the scene number of the media, relative to the script.

Shot: An editable field to contain the shot number of the media, relative to the scene.

Slate TC: The Slate timecode track used to sync audio with video.

Start: The first frame number of the media file.

Start KeyKode: The starting KeyKode value of a scanned negative.

Start TC: The timecode value of the first frame in the media file.

Take: An editable field to contain the take number of the media, relative to the shot.

Type: The type of item, such as Video+Audio, Video, Audio, Timeline, Multicam, Still, and so on.

Usage: After a timeline has been created by importing an AAF, EDL, or XML project, the Usage column

automatically reflects how many times each clip is used in the project. This makes it easy to identify clips

that aren’t in use, and which can be removed from the Media Pool.

V-FLIP: Whether that media file is vertically flipped in DaVinci Resolve.

Video Codec: The specific codec used by the video portion of the media file.