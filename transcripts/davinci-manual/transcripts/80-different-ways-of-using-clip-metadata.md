---
title: "Different Ways of Using Clip Metadata"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 80
---

# Different Ways of Using Clip Metadata

To encourage you to take advantage of the clip metadata tools that exist in DaVinci Resolve, here’s a

short list of the many different ways you can use clip metadata to help you work faster.

�Searching for clips in the Media Pool

�Searching for clips in the Timeline

�Sorting the Media Pool by metadata columns in list view

�Creating Smart Bins in the Edit page

�Creating Timeline Filters in the Color page

�Using Metadata to create clip Clip Names

�Displaying Metadata in frame using the Color page Burn In palette

Renaming Clips Using Clip Names

The most fundamental piece of clip metadata is each clip’s name, which is used to identify clips

nearly everywhere they appear inside DaVinci Resolve. By default, clips show the file name of the

corresponding media file on disk. Since the dawn of tapeless recording, however, editors have been

stuck with camera original media having names that are not exactly “human readable.”

Fortunately, you have the option of entering a more user-friendly clip name to use instead, while

preserving the original file name that’s critical for maintaining the link between a clip and its media,

as well as for tracking an offline clip’s corresponding link to the online media from which it originated.

There are a few ways you can edit the clip name of a clip.

NOTE: You can also edit the clip names of timelines, compound clips, and multicam clips, so

that you can have two sets of naming conventions for these items, one for when you’re doing

creative editing, and one for when you’re doing finishing tasks.


Ingest and Organize Media | Chapter 19 Using Clip Metadata

MEDIA

To edit a clip’s clip name, do one of the following:

�In the Media Pool’s Icon view, click a clip’s name once, pause a moment, then click a second time

to select the name, type a new name, then press return to accept the name.

�In the Media Pool’s List view, the Clip Name mirrors the source clip’s file name (hidden by default),

but you can click the Clip Name column for any clip to add a new name from scratch.

�With the Clip Name column exposed in the Media Pool’s List view, Option-click the Clip Name

column for any clip to edit the file name, rather than entering a brand new name.

�To edit the clip name of multiple clips, select all of the clips for which you want to change the clip

name, then right-click one of the selected clips and choose Clip Attributes. Open the Name panel

of the Clip Attributes window, edit the Clip Name field, and click OK.

After you’ve changed a clip’s clip name, that clip appears in the following places using the clip name

instead of the original file name:

�The Media Pool’s Thumbnail view

�The name bar of each clip in the Timeline

�The Source Viewer title bar

�The Clip Name field of the Clip Attributes dialog’s Name panel

Switching Between File Names and Clip Names

Since different tasks require different information, you have the ability to switch between using clip file

names and clip names. For example, finishing editors will probably have more reason to refer to the file

name of each clip, making it easier to troubleshoot problems with reconforming and relinking. Creative

editors, on the other hand, will want to use easier-to-read clip names to make it easier to find what

they need.

To switch between file names and clip names:

Choose View > Show File Names to toggle between both naming conventions.

Using Metadata to Define Clip Names

If you’re an enthusiastic user of clip metadata (and you should be), you can use “metadata variables”

that you can add into a field that let you reference other metadata for that clip. For example, you could

add the combination of variables and text seen in the following screenshot to define a clip name

automatically. Variables, once they’ve been entered, are represented as graphical tags shown with a

background, while regular text characters that you enter appear before and after these tags.

Variables and text characters entered to create a clip name based on a clip’s metadata

As a result, that clip would display “12_A_3” as its name if scene “12,” shot “A,” and take “3” were

its metadata. When you do this, you can freely mix metadata variables with other characters (the

underscore, as in the example above) to help format the metadata to make it even more readable.

Every single item of metadata that’s available in the Metadata Editor can be used as a variable, and

several other clip and timeline properties such as the version name of a clip’s grade, a clip’s EDL event

number, and that clip’s timeline index number can be also referenced via variables.


Ingest and Organize Media | Chapter 19 Using Clip Metadata

MEDIA

Since the use of metadata variables is a great way to automatically generate names for multiple clips,

you may find it more useful to add metadata variable-driven clip names by selecting all of the clips you

want to edit, and opening the Clip Attributes window. By editing the Clip Name field found in the Name

panel, you can add a single clip name to all selected clips at once.

To add a variable to a text field that supports the use of variables:


Type the percentage sign (%) and a scrolling list appears showing all variables that are available.


To find a specific variable quickly, start typing the characters of that variable’s name and this list

automatically filters itself to show only variables that contain the characters you’ve just typed.


Choose which variable you want to use using the Up and Down Arrow keys, and press Return to

choose that variable to add.

The variable list that appears when you type the % character

As soon as you add one or more metadata variables to a clip’s Clip Name column and press

Return, the string is replaced by its corresponding text. To re-edit the metadata string, simply

click within that column, and the metadata variables will reappear. Be aware that, for clips where a

referenced metadata field is blank, no characters appear for that corresponding metadata variable

in the Clip Name column.

To remove a metadata variable:

Click within a field using variables to begin editing it, click a variable to select it, and

press Delete.

For more information on the use of variables, as well as a list of all variables that are available

in DaVinci Resolve, see Chapter 16, “Using Variables and Keywords.”


Ingest and Organize Media | Chapter 19 Using Clip Metadata

MEDIA

Chapter 20

Using the Inspector

in the Media Page

The Inspector holds all the controls to modify, resize, retime, and generally adjust

anything related to a clip, transition, or effect on the Media page Timeline.

Contents

Using the Inspector����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 424

Adjusting Media Pool Clips in the Inspector�������������������������������������������������������������������������������������������������������������������������� 424

Video����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 425

Audio����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 429

Image���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 432

File ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 432


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA

Using the Inspector

The Inspector has been redesigned to make it easier to find specific controls and to adjust common

settings for your clips. Instead of a long vertical list, different aspects of the Inspector have now been

organized into panels, with each controlling specific grouped sets of parameters for your clip.

The Inspector is activated by clicking on the Inspector Panel in the upper-right section of

the User Interface toolbar. The Inspector is broken up into individual Video, Audio, Effects,

Transition, Image, and File panels. Inspector panels that are not applicable to your clip or

selection are grayed out.

The Inspector Panel icon in

the upper right of the UI toolbar

The Inspector panels showing Video, Audio, and

File parameters available for adjustment; others are grayed out.

Methods of using controls in the Inspector:

•	 To activate or deactivate a control: Click the toggle to the left of the control’s name.

The orange dot on the right means the control is activated. A gray dot on the left means the

control is deactivated.

•	 To reveal a control’s parameters: Double-click the control’s name.

•	 To reset controls to their defaults: Click the reset button to the right of the control’s name.

Adjusting Media Pool Clips in the Inspector

You can directly modify Media Pool clips in the Inspector, before you edit those clips into a timeline.

This allows you to change the parameters of source media so that clips that are subsequently edited

into a timeline carry those new settings with it. For example, you can prepare your material prior to

editing by changing the clip’s file and RAW settings, adjusting the audio levels and EQ, or assigning

it a specific lens correction, etc. Once modified, any part of that clip would have the correct Inspector

parameters already in place when you edited them into your timeline.

To adjust Media Pool clips in the Inspector:


Select one or more clips in the Media Pool Panel of either the Media, Cut, Edit, or Fairlight pages.


Open the Inspector panel, and adjust any parameters in the Video, Audio, Image and File tabs.

These parameter changes are stored with the Media Pool clip, and will be carried over when any

part of that clip is edited into the Timeline. Of course, each clip’s Inspector parameters can be further

modified once it’s in the Timeline, and those Timeline parameters are independent from the Media

Pool Inspector settings. This means that any further adjustments you make to the clip in the Timeline

do not affect that same clip’s adjustments already in the Media Pool.


Ingest and Organize Media | Chapter 20 Using the Inspector in the Media Page

MEDIA