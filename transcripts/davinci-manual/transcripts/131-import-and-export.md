---
title: "Import and Export"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 131
---

# Import and Export

DaVinci Resolve Timelines (.drt)

You can export and import individual timelines from one DaVinci Resolve project into another

previously existing DaVinci Resolve project, allowing you to pass timelines quickly between projects

and workstations, without creating additional imported project files. Just the timeline and its

associated clip information are exported; none of the actual media files are included.

To export a timeline from the Media Pool:


Select a timeline from the Media Pool.


Choose File > Export > Export AAF, XML, DRT (Shift-Command-O).


Choose “DaVinci Resolve Timeline Files (*.drt)” from the format options popup in the file

system dialog.


Choose where to save the DaVinci Resolve Timeline file (.drt) in the file system dialog, and

click Save.

To export multiple timelines from the Media Pool:


Select multiple timelines from the Media Pool.


Right-click on a timeline and choose Timelines > Export > DaVinci Resolve Timeline Files.


Select the folder where you wish to save them from your file browser.

Unlike exporting individual timelines, when exporting multiple timelines, you will not be able to rename

the .drt files on export. They will retain the timeline name they have in the Media Pool.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

To import a timeline into the Media Pool:


Choose a bin in the Media Pool in which you want the imported timeline to be saved.


Do one of the following:

�Choose File > Import Timeline > Import AAF, XML, DRT (Shift-Command-I), then Select a DaVinci

Resolve Timeline file (.drt) from the file system dialog, and click Open.

�Double click the .drt file in your file system.

The timeline will appear in the Media Pool, along with all of the clips associated with it, including

any media sync information. Any timelines imported this way will have the word “import” appended

to their name, to avoid duplicate names. The imported timeline will be automatically conformed to

corresponding media that’s already in the Media Pool. However, if the timeline has been moved to

another computer, you may have to reimport or relink missing or offline media in to bring the imported

timeline fully online.

NOTE: Only a single timeline can be imported and exported at a time using this method.

To import or export multiple timelines, use the Import/Export Bin function instead.

Backing Up and Restoring Timelines

Turning on the Timeline Backups checkbox in the Project Save and Load panel of the User

Preferences enables DaVinci Resolve to save multiple backups of a timeline at periodic intervals,

using a method that’s analogous to a GFS (grandfather-father-son) backup scheme. This can be done

regardless of whether or not Live Save is turned on.

If you want to revert to a previous backup of a timeline, simply right-click on the Timeline in the Media

Pool, select Restore Timeline Backup from the contextual menu, and choose the backup from the list

of options. Backups are organized by date and time, making it easy to find the specific timeline you

want to restore.

Restoring a timeline backup in the Media Pool


Edit | Chapter 34 Creating and Working with Timelines

EDIT

Restoring a timeline backup does not overwrite your current timeline. Instead the selected backup will

be brought into the Media Pool as a new timeline with the name “Backup” appended to it.

Timeline backups are only saved when changes have been made to a project. If DaVinci Resolve sits

idle for any period of time, such as when your smart watch tells you to go outside and walk around the

block, no additional project backups are saved, preventing DaVinci Resolve from overwriting useful

backups with unnecessary ones.

Three fields let you specify how often to save a new backup, while the fourth lets you choose where

the backups will be saved. These settings apply to both Project and Timeline backups.

�Perform backups every X minutes: The first field specifies how often to save a new backup within

the last hour you’ve worked. By default, a new backup is saved every 10 minutes, resulting in six

backups within the last hour. Once an hour of working has passed, an hourly backup is saved and

the per-minute backups begin to be discarded on a first in, first out basis. By default, this means

that you’ll only ever have six backups at a time that represent the last hour’s worth of work.

�Hourly backups for the past X hours: The second field specifies how many hourly project

backups you want to save. By default, two hourly backups will be saved for the current day. Past

that number, hourly backups will begin to be discarded on a first in, first out basis.

�Daily backups for the past X days: The third field specifies for how many days you want to save

backups. The very last backup saved on any given day is preserved as the daily backup for that

day, and by default daily backups are only saved for two days. Past that number, daily backups

will begin to be discarded on a first in, first out basis. If you’re working on a project over a longer

stretch of time, you can always raise this number.

�Project backup location: Click the Browse button to choose a location for these backups to be

saved. By default they’re saved to a “ProjectBackup” directory on your scratch disk, although

you could change this to a volume that better fits into your data backup methodology. This folder

contains both Project and Timeline backups.

Timeline View Options

As you’re working on an edit, it can often be useful to modify the appearance of the Timeline,

changing the height of video or audio clips, choosing whether audio waveforms are drawn or not, and

so on. Using the Timeline View Options drop-down at the far left of the Timeline, you can make these

kinds of changes as you work.

The Timeline View

Options drop-down


Edit | Chapter 34 Creating and Working with Timelines

EDIT

You have the following options:

�Timeline View Options: Three buttons let you choose to show or hide specific Timeline interface

elements, including the following:

Display Stacked Timelines: This option lets you show stacked timelines for simultaneous display

of timelines one on top of another.

Display Subtitle Tracks: Lets you display or hide the subtitle tracks region of the Timeline. Hiding

subtitle tracks does not disable subtitle display; to do that you must disable the currently displayed

subtitle track.

Display Audio Waveforms: Lets you turn audio waveform viewing off and on. When Audio

Waveform is turned off, audio tracks are minimized.

�Thumbnail View Options: Three buttons let you choose the overall appearance of the video track.

From left to right:

Filmstrip: Displays each clip as a series of frames along its length. The number of frames

displayed depends on the current zoom level of the clip in the Timeline.

Thumbnail: Displays each clip as a solid color with a thumbnail image of the clip’s In point at the

beginning of the clip and a thumbnail image of the Out point at the end. The thumbnails displayed

depend on the current zoom level and track height of the clip in the Timeline. If the clip does not

have enough room for both, only the In point thumbnail will appear.

None: Displays each clip as a solid color along its length.

�Viewer Background: Four options: Checkerboard, Black, Gray, or Alert Red let you determine

what color the transparent background will be in the Viewer.

�Fixed Playhead: This option lets you toggle between a fixed playhead, keeping the playhead

static in the middle of the timeline, while the tracks on the timeline move underneath it, or Free

Playhead, where the playhead travels along the timeline as it is played back.

When using the Fixed Playhead option, you can choose where to set the location of the

Fixed Playhead in the timeline, rather than just have it in the center. To do so, hover the pointer

over the top of the playhead in the Timeline Ruler and drag it to the new location you want to use.

Moving the Fixed Playhead can be useful in increasing the amount of timeline working area for

clips before or after the current position.

�Audio View Options: Three buttons govern the look of audio waveforms in the Timeline,

when visible.

Display Non-Rectified Waveform: Lets you toggle between the waveform being drawn from the

bottom of the audio track up, or centered and mirrored about itself.

Display Full Waveform: Hides the divider bar that keeps the waveform separate from the file name

area of each audio clip, so the waveform occupies the full space of each audio bar in the Timeline.

Display Waveform Border: Draws a dark border around the edges of each waveform to make

them easier to see.

�Video track height slider: Lets you resize the size of all video tracks at once, independently of the

audio tracks.

�Audio track height slider: Lets you resize the size of all audio tracks at once, independently of the

video tracks.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

In addition, any track in the Timeline can be individually resized by dragging its top divider in the Track

Header area. Track heights in the Edit page are independent of the Thumbnail and Waveform view

settings in the Timeline View options. Previously, specific Timeline viewing options such as Filmstrip or

Thumbnail view had minimum track height settings. Now you can freely change track height no matter

what options you’ve chosen, and resizing one or more tracks below the minimum height for filmstrips

or thumbnails automatically collapses those tracks into Simple view to avoid clutter.

Resizing an individual Timeline track by

dragging its top border in the Track Header

Modifying Timeline Tracks

When you’re getting ready to edit clips into the Timeline, you need to make sure you’ve got enough

tracks to do the job. The following procedures cover the different methods available for adding,

removing, and rearranging tracks as you work. These commands are all available via the contextual

menu that appears when you right-click anywhere in the Timeline header area (the header of the

Timeline is the area to the left where each track’s various buttons and controls are located).

Keyboard Shortcuts can be assigned for track header context menu actions to add, delete, move,

change color, and link tracks. Tracks can be selected in the Track index, or the Edit and Fairlight

timelines. For example, you can assign a keyboard shortcut to add a new Audio Track in the Edit page

by navigating to Commands > Edit Timeline > Track Controls > Add Track > Audio in the Keyboard

Customization window.

Methods for adding, deleting, and rearranging tracks:

�To add a track to the Timeline: Right-click on a Track Timeline header and choose Add Track.

A new video track will be created immediately above the track you right-clicked on. A new audio

track will be created immediately below the track you right-clicked on. If you add an audio track,

you can choose what type of channel mapping you want.

For more information about audio track channel mappings,

see Chapter 45, “Working with Audio in the Edit Page.”

�To add multiple tracks to the Timeline at a specific position: Right-click anywhere in the Timeline

header and choose Add Tracks. When the Add Tracks dialog appears, choose the number of

video and audio tracks you want to add, choose the position you want to insert the tracks above

or below, and choose the Audio Track Type you want to add if you’re adding audio tracks. When

you’re done, click “Add Tracks.”

�To delete a track from the Timeline: Right-click within a track’s Timeline header and choose

Delete Track. If there are clips on a track you remove, they are deleted from the Timeline.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

�To delete all unused tracks in the Timeline: Right-click anywhere in the track header area and

choose Delete Empty Tracks. All tracks without clips will be deleted at once.

�To move tracks and the clips on them up and down: Right-click within a track’s Timeline header

and choose Move Track Up or Move Track Down from the contextual menu. That track, along with

all clips on it, will be moved up or down relative to the other tracks in the Timeline. You can also

rearrange track order from the Tracks Index. Simply click on the track in the # field and drag the

track to its new position.

The Add Tracks Dialog lets you add multiple tracks

at once and set their locations in the timeline.