---
title: "Using Reconform From Media Storage"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 214
---

# Using Reconform From Media Storage

DaVinci Resolve 14 introduces another reconform method, that lets you conform clips in a timeline

to clips in a specific File System directory (including all subdirectories) using the “Reconform From

Media Storage Folders” command. This allows you to reconform multiple clips in a timeline, all at

once, to matching source media files on disk without having to import those clips to the Media Pool

first; all clips that can be conformed according to the specified conform criteria will be automatically

imported as necessary.

An important aspect of the Reconform From Media Storage command is that DaVinci Resolve

will reconform all timeline clips that can be matched to source media files on disk in the

selected Media Storage directories, but all Timeline clips that cannot be matched are

left alone. This makes Reconform From Media Storage an ideal command to use in the

following situations:

•	 When you need to reconform clips that are found throughout an existing timeline to a

smaller subset of media in a specific directory on disk, such as updated VFX or Motion

Graphics from a third-party application.

•	 When you need to quickly reconform missing timeline clips throughout an imported timeline,

and especially when you need to use custom conform criteria to successfully reconform

those clips. (Unlinked clips can only be reconformed with this command if you select them

and turn off Conform Lock Enabled first.)

Similar to the Reconform From Bins command, you can specify exactly what combination of conform

criteria you want to use to match clips in the timeline with clips in the Media Pool. This means that

you’re not restricted to only using Timecode, Reel Name, and File Name, you could also use any

combination of Total Duration, Resolution, Bit Depth, Frame Rate, File Format, Codec, and/or Media

UMID/UID to control how clips are conformed, depending on your needs and the problem you

have to solve.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

The Reconform From Media Storage dialog

This method of timeline conform is ideal when the only way you can conform a timeline to the media

you require is using a very specific combination of metadata that’s different from the rules that

DaVinci Resolve defaults to.

For example, you have a jumbled mix of 8- and 10-bit versions of the same clips on your hard drive,

but you only want to conform a given timeline to the 10-bit media in preparation for finishing. Using

“Reconform from media storage folders” lets you be this specific with what media to use.

To use “Reconform from media storage folders” to reconform a timeline:


Double-click the Timeline you want to reconform to open it.


Either select the specific clips you want to reconform, or press Command-A to select every clip in

the Timeline if you want to reconform clips throughout the entire timeline without having to make

individual selections.


Right-click one of the selected clips, and choose “Conform Lock Enabled” to disable

Conform Lock Enabled for the clips you want to reconform. This frees DaVinci Resolve to consider

all possible conform matches for those clips in cases where there may be multiple clips with

overlapping timecode in the Media Pool.


Right-click the timeline you want to reconform, and choose Timelines > Reconform from media

storage folders. The Import From dialog appears, with a File System browser to the left, and an

Options panel to the right.


From the Timeline Options section, choose whether you want to conform to All Clips or just

to Selected Clips. Then, choose whether you want to “Set clips to Conform Lock Enabled”

after conform.

Choosing which clips in the Timeline to attempt to reconform


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT


From the Conform Folders section, choose a directory that contains media you want to reconform to.

Selecting a directory that has media you want to conform to


Next, choose the conform options you want to be considered when matching timeline clips to

source media files in the selected directory. By default, Timecode is enabled. Choose additional

criteria to be even more selective about which clips will be reconformed, or choose different

criteria if you need to use other metadata to get better results.

Selecting criteria to guide the reconform

TIP: Choosing Custom from the top of the pop-up menu for File Extensions, File Format,

and Codec displays editable fields into which you can enter multiple options, separated

by commas, in order to list multiple possibilities for a successful match. The order in which

you enter these is important, as DaVinci Resolve will attempt to conform clips starting

with the first format/codec at the left, moving to try the next format/codec to the right if no

match is found, until every entry in your list has been tried.


Click OK. Where possible, the Timeline is automatically updated to conform to the media in the

directory you selected, and all source media files that were conformed have been imported into

the Media Pool.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT


After you’ve used “Reconform From Media Storage Folders,” any timeline clips that have been

reconformed and that now have timecode and reel names/file names that match two or more

source clips in the Media Pool will display a clip conflict badge in the Timeline. To eliminate this

badge, you can select either just the clips that were conformed, or all clips in the Timeline, right-

click them, and choose Conform Lock Enabled to eliminate these warnings.

Understanding, Fixing, and

Using Reel Conflicts

As long as the “Auto conform clips with media added into Media Pool” setting is enabled in the

General Options panel of the Project Settings, the same dynamic relationship between clips in the

Media Pool and those in a timeline are maintained whether clips are linked or unlinked, it makes no

difference. However, this does mean that if you have two different versions of the same clip in the

Media Pool, or even two completely different clips that share the same file name (or reel name) and

the same overlapping timecode, then DaVinci Resolve is capable of automatically conforming to

either clip.

A good example of this is if you have both the camera raw version of a clip, and a ProRes or MXF

transcoded version imported into the Media Pool at the same time. Both clips have the same content,

the same file name, and the same range of frames. This poses the potential for what DaVinci Resolve

refers to as a “clip conflict.”

You won’t necessarily notice this at first because, by default, all clips that are imported with a timeline,

or that you’ve edited into a brand new timeline, have a Conform Lock Enabled setting enabled by

default. All clips in a timeline with Conform Lock Enabled turned on only consider the current clip in the

Media Pool to which they’re conformed as the valid clip; all other clips with file names and overlapping

timecode that would otherwise make them an otherwise valid match are ignored.

However, if you right-click such a clip in the Timeline and turn Conform Lock Enabled off, that clip will

display a “clip conflict” error, with an “attention” badge to the left of its name in the Timeline.

Conflict icon indicating at least two clips have

matching conform parameters

Clip conflicts are typically considered to be an error, but not always. They can be a problem if the

media you’ve imported along with an imported project from another application has media that was

added with timecode but no reel identifier (for example, when shots from multiple unidentified reels

that all start at 0 hour). The thing is, you may not immediately notice such clip conflicts, until you turn

Conform Lock Enabled off.

TIP: Overlapping timecode often occurs in the normal course of work, but should be

managed by altering each clip’s embedded reel name, or by organizing media in different bins.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

Using Clip Conflicts as a Conform Tool

On the other hand, clip conflicts can often be desirable solutions to workflows where you need

to switch among different versions of a particular clip. To take the example of an edited timeline

consisting of transcoded QuickTime versions of camera raw original media, if you only had the

transcoded clips in the Media Pool, then all is well.

However, suppose in the course of working that you decide you need the resolution or additional

color latitude of the camera raw version of a particular clip. If you import the camera raw version of that

one clip, you should notice nothing different. However, if you then right-click that clip in the Timeline

and choose Conform Lock Enabled to uncheck the setting and turn it off, you should then see the

attention badge to the left of the clip name in the Timeline. This lets you know that this clip in the

Timeline is correctly seeing the relationship between it and the now two simultaneously named clips

with timecode overlap in the Media Pool.

The current relationship between this timeline clip and the one to which it is conformed doesn’t

change; this badge is only letting you know that now there is a second clip in the Media Pool to which

you could potentially conform this clip in the Timeline. Now, you need only choose which one by

double-clicking the clip conflict badge, and following the procedure below.

Resolving Clip Conflicts

Once you have a clip conflict, whether intentional or not, it’s really easy to resolve it. In fact, this feature

is the very basis for the name of the software.

To resolve a reel conflict by relinking a clip’s media:


Double-click the “attention” badge of any clip in the Timeline, displayed to the left of that

clip’s name.

The Conflict Resolution window appears, showing a list of all files in the Media Pool, of any format,

that have identical file names (or reel names) and timecode that overlaps with the clip you right-

clicked. Each item in this list shows a thumbnail of the clip, the file path of the media on disk, the

file name, starting timecode, reel name (if any), and creation date, to help you determine which of

the clips in that list is the one you want to use.

Conflict Resolution window showing what other clips have overlapping timecode and reel information


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT


Click the entry in the list that you want to conform to, and click Apply. The clip in the Timeline

changes to reflect the media you selected, and the “attention” icon is replaced with a “resolved”

badge indicating that the conflict has been resolved. Keep in mind that you can always double-

click the “resolved” badge to change which Media Pool clip you want to conform to. It remains a

dynamic relationship.

A clip badge showing that the conflict was resolved