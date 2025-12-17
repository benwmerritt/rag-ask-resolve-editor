---
title: "Adding Subclips From the Media Storage Panel"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 71
---

# Adding Subclips From the Media Storage Panel

If you’re browsing long source clips in the Media Storage panel, but you only want to import a small

segment of a much longer clip into the Media Pool, you can create subclips directly from the Media

Storage panel.

To add a subclip from a clip in the Media Storage panel to the Media Pool:


Single-click any clip in the Media Storage panel to open it into the Viewer in order to create a

subclip without needing to first import that clip into the Media Pool.


Set In and Out points in the Source Viewer to define the section you want to turn into a subclip.


Do one of the following:

�Right-click the jog bar and choose Make Subclip from the contextual menu

�Drag the clip from the Viewer to the Media Pool to add it as a subclip


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Adding Individual Frames From Image Sequences

If you’re working with image sequences, or with sequentially numbered image files from any source,

DaVinci Resolve automatically presents them as clips in the Media Storage panel. This is good if that’s

what they are, but there are instances where sets of photos, of which each frame is in actuality a

separate media file, are also sequentially numbered. For this reason, you can import individual frames,

rather than entire image sequences.

To choose between adding individual frames from a number sequence of images,

or adding them as image sequence clips in the Media Storage panel:


Click the Media Storage panel option menu, and choose Frame Display Mode.


Close one of the drop-down options:

Auto: DaVinci Resolve will automatically select Individual Frames or Image Sequence based on file

type. For example, DPX and EXR files will be imported as image sequence clips, while JPG files

will be imported as individual frames.

Individual: Each image sequence is now separated into its individual frames, allowing you to

select only the frames you need.

Sequence: Will group sequentially numbered files together as an image sequence clip, regardless

of file type.


Use any of the previous described methods to add the frames you want to the Media Pool as

individual clips or image sequences.

Adding Media Based on EDLs

Another strategy for adding media to the Media Pool is to use an EDL to add only the clips it refers

to from a directory. This lets you add only the clips that are necessary for conforming a particular

imported project before conforming an EDL, and eliminates the need to add too much media to

the Media Pool, which might slow you down in the case of projects referencing terabytes of media.

Furthermore, you can choose multiple EDLs to base the import on, and many directories to examine.

The EDLs will reference clips via their timecode and sometimes reel name and path. It is these settings

and the conform frame rate that you made previously in the Configuration screen that are now used to

place images correctly into the Media Pool.

To add only media used in an EDL to the Media Pool:


If necessary, open the General Options panel of the Project Settings, turn on the “Assist using

reel names from the” checkbox, and choose a method with which to extract reel name

information from the media files you’re about to import.

For more information, see Chapter 19, “Using Clip Metadata.”


Right-click a directory in the Media Storage panel, and choose one of the following commands:

�Add Folder Based on EDLs into Media Pool

�Add Folder and SubFolders Based on EDLs into Media Pool


Using the file dialog that appears, select one or more EDLs to use.

DaVinci Resolve searches the directory hierarchy, either one level deep or all levels deep, for every

media file matching the source timecode and the reel ID of an event in one of the selected EDLs.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Splitting Clips Based on EDLs

You can also use EDLs to split a media file into multiple clips in the Media Pool, either as an alternate

means of “preconforming” a flattened master media file, or to import multiple sections of a longer

media file that happen to be referenced by an EDL.

To split and add clips based on an EDL:


Right-click a directory in the Media Storage panel, and choose “Split and add into Media Pool.”


Using the file dialog that appears, select an EDL to use, and click Open.


Choose a frame rate to use to conform the clips to in the “File Conform Frame Rate” dialog,

and click OK.


Choose a handle size, in frames, and whether or not you want to split unreferred clips from

the “Enter handle size for splitting” dialog, and click Split & Add. The media file is split into the

component clips specified in the EDL, and added to the Media Pool.

TIP: Turning on the Split Unreferred Clips checkbox automatically splits out sections of the

file that were not referred to by the EDL you selected, and adds them to the Media Pool

separately, giving you access to every piece of media that’s available.

Import Clips With Metadata Via Final Cut Pro 7 XML

In order to support workflows with media asset management (MAM) systems, DaVinci Resolve

supports two additional Media Pool import workflows that use Final Cut Pro 7 XML to import clips

with metadata.

To import clips with metadata using Final Cut Pro 7 XML files, do one of the following:

Right-click anywhere in the background of the Media Pool, choose Import Media from XML,

and then choose the XML file you want to use to guide import from the import dialog.

Drag and drop any Final Cut Pro 7 XML file into the Media Pool from the macOS Finder.

Every single clip referenced by that XML file that can be found via its file path will be imported into

the Media Pool, along with any metadata entered for those clips. If the file path is invalid, you’ll

be asked to navigate to the directory with the corresponding media. Additionally, the following

metadata is imported:

�Clips

�Browser metadata

�Subclips

�Clip Markers, with colors and duration

�Bin Hierarchy

�Comments


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Adding Media With Offset Timecode

Sometimes source media was created with incorrectly offset timecode, due to mistakes made earlier

in the postproduction process. If this offset is consistent, you can use the “Add Folder with Source

Offset” command to add media to the Media Pool as clips with a timecode offset.

To add a folder of clips to the Media Pool with offset timecode:


Right-click a directory in the Media Storage panel, and choose one of the following commands:

�Add Folder with Source Offset

�Add Folder and SubFolders with Source Offset


Choose a number of frames with which to offset the timecode from the “Change Frame Offset”

dialog, and click Apply.

The media is imported as clips with offset timecode in the Media Pool. However, the original source

timecode of the clips on disk has not been altered. All media rendered out of the Deliver page will

reflect the offset timecode.

Import Blackmagic Cloud

Shared Folders to Media Pool

You can now import and sync Blackmagic Cloud Folders into the Media Pool. This allows you to

connect to one or more cloud media folders and selectively download media from them to your

local machine. Blackmagic Cloud Folders are online common storage folders that are not tied to a

specific project. This lets you create a pool of commonly used media assets, such as title sequences,

credits, bumpers, etc., and share them online without having to import them separately into each

individual project.

The Import Cloud Folder icon at the top of the Media Pool

To link a Blackmagic Cloud Folder to your project:


Sign into your Blackmagic Cloud account in DaVinci Resolve.


Click on the Import Blackmagic Cloud Folder icon at the top of the Media Pool in any page.


In the Blackmagic Cloud Folder dialog, click select to choose a Blackmagic Cloud Folder. The

choices here will show any Blackmagic Cloud Folder that you have created or someone else has

shared with you. Click the Add button.


In the Download Folder Location, select a file location on your local system that you want the

media from the Blackmagic Cloud Folder to be stored in.


Choose whether you want to sync proxies only, or proxies and used originals.


Press Download to add the Cloud Folder to your Media Pool.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

The Blackmagic Cloud Folder link dialog

When you open the Blackmagic Cloud Folder in the Media Pool, it will be empty and populate

one clip at a time as their clip names (not their media) are downloaded from the cloud. Also, the

Blackmagic Cloud Folder is not actually linked to your project yet; it is only linked when the first

media clip is “used.”

A “used” clip is new terminology in DaVinci Resolve and simply means a clip that has been altered

in any way inside the project. A clip can be used be by putting it on a timeline, certainly, but also

includes other actions like applying a flag, altering its metadata, transcribing it, etc. Once a clip is

used, its media will start to download to your local machine. Clips that are used are denoted by a

red dot next to them in the Media Pool. Any unused clips will remain as virtual clips in the Cloud

Folder until used. Once downloaded, clips in Cloud Folders can be used just like any other clip in

the Media Pool.

The Cloud Folder linked in List view. Clips with red dots are “used,” and the original media

has been downloaded. Unused clips have just their proxies available to view. The Cloud

Sync column shows that the media is registered and synced with the Blackmagic Cloud.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA