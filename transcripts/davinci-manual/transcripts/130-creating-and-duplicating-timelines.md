---
title: "Creating and Duplicating Timelines"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 130
---

# Creating and Duplicating Timelines

If you’re not importing a project that’s been edited elsewhere, you can create a new timeline to cut

together a new edit from scratch, to use to assemble clips for use in a Fusion composition, to grade

a set of dailies, or to put together an audio program within the Fairlight page. When you create a new

timeline, you can either create a timeline that contains all clips found in the Media Pool to quickly

create a big batch of offline dailies, or an empty timeline that’s ready for you to add specific clips to.

Timelines you create are stored in the currently selected Media Pool bin.

If you’d like an easy way to browse all the timelines in your project at once, regardless of their diverse

locations, you can enable the “Smart Bin for Timelines” option, which is in the Editing panel of the User

Preferences. This creates a Smart Bin in the Bin list of the Media Pool that filters all timelines in your

project, making it easy to see all your timelines without altering your original organization.

Individual Timeline Settings for Format,

Monitoring, Output, and Color

When you create a new timeline, there are a number of ways you can customize it, but by default it

will mirror the current project-wide timeline settings for resolution, frame rate, and other format and

monitoring parameters.

The Create New Timeline dialog with standard customization settings

However, you have the option of creating separate timelines with individual Format, Monitoring, Output

Sizing, and Color Management settings for situations where you need to set up multiple timelines to

create multiple deliverables with different resolutions, pixel aspect ratios, frame rates, monitoring,

or output scaling options, and color management than the overall project, including “Mismatched

Resolution Files” settings. To choose individual settings, uncheck the Use Project Settings box in the

New Timeline dialog, and additional controls will appear.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

Clicking Use Custom Settings exposes additional

panels for individualized timeline settings

Once you’ve created a timeline with individual settings, you can edit its settings by right-clicking

that timeline in the Media Pool, and choose Timelines > Timeline Settings from the contextual menu.

An Edit Timeline dialog appears, with separate panels for Format, Monitor, Output, and Color settings

that you can choose. You can also click Use Project Settings to have that timeline use the project-wide

timeline settings instead.

It is also possible to change the starting timecode for multiple timelines at the same time using the

custom timeline settings.

To change the start timecode for multiple timelines at once:


Select the Timelines whose timecode you want to modify.


Right-click on one of the selected Timelines and choose Timelines > Starting Timecode from the

contextual menu.


Enter the new timecode in the Time Start field.


Click on OK.

Creating Blank and Stringout Timelines

If you’re cutting a new video or audio program, you’ll usually want a blank timeline. However, the

same command can be used to create stringout timelines when putting together dailies by turning the

“Empty Timeline” checkbox off.

To create a new blank timeline:


(Optional) Select or create a folder in the Bin list in which to put the new timeline.


Do one of the following:

�Choose File > New Timeline (Command-N).

�Right-click within the Media Pool, and choose Timelines > Create New Timeline.


When the New Timeline Options window opens, set the following options:

Start Timecode: You can change the Start Timecode if a specific start time is required.

Timeline Name: Enter a name into the Timeline Name field.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

No. of Video Tracks: Enter how many video tracks you want to have. You can also drag within this

field to adjust the number of video tracks with a virtual slider.

Use Fairlight Preset: If this box is checked, it creates a timeline with pre-assigned audio tracks

using a previously created Fairlight Configuration preset. A drop-down menu then appears,

allowing you to select the specific preset for the Timeline. The preset is used in lieu of the

No. Of Audio Tracks setting below. You can create Fairlight Configuration presets using the

Fairlight Presets Library, available from the Fairlight menu.

For more information, see Chapter 171, “Setting Up Tracks, Busses, and Patching.” in the

DaVinci Resolve Manual. If you have no Fairlight Configuration presets saved, this option

will not appear.

No. of Audio Tracks: Enter how many audio tracks you want to have. You can also drag within this

field to adjust the number of audio tracks with a virtual slider.

Audio Track Type: Choose the channel mapping you want the new audio tracks to use.

Empty Timeline: Checked by default, this sets new timelines to be created empty. If you turn off

the Empty Timeline checkbox, the new Timeline that’s created will contain all media found in every

bin within the Media Pool, effectively creating a stringout of everything you’ve imported.

Use Selected Mark In/Out: Only available when “Empty Timeline” is turned off. When you turn this

checkbox on, each clip’s duration in the new Timeline is defined by the In and Out points saved

within each clip. If there are no In/Out points in a clip, the clip’s entire duration is used.

Use Custom Settings: Click this button if you want to expose the Format, Monitor, and Output tabs

that can expose unique settings for each timeline.


Click Create New Timeline.

A new timeline is created. If necessary, you can duplicate an existing timeline in order to alter an edit

or create an alternate grade.

TIP: If you’re going to be creating several new timelines with a specific set of parameters, you

can open the User pane of the Preferences and edit the New Timeline Settings, found in the

Editing panel. This will define new presets that populate the New Timeline Options window

from that point forward.

Creating Timelines by Drag and Drop

When you first create a new project, no timeline inhabits the Timeline Editor, and you have an

opportunity to create a new timeline by drag and drop.

To create a timeline by dragging and dropping a clip:

Drag any clip into the empty Timeline Editor area underneath the Viewers on the Edit page, and a new

timeline will automatically be created.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

Creating Timelines From Bins and Selections

The “Create Timeline Using Bin” and “Create Timeline Using Selected Clips” commands let you quickly

assemble a timeline using the contents of the Media Pool, using whatever In and Out points have been

added to each clip, and using the sort order of the enclosing bin to determine the order in which the

clips will be assembled.

TIP: These commands are especially useful for putting together quick assembly edits if you

have metadata-rich media with scene, shot, and take information that you can use to sort clips

into the proper order, and In and Out points that you’ve already logged.

To create a timeline using the full contents of a bin:


(Optional) Put the Media Pool into List mode, set In and Out points for each clip in your Bin,

and sort the Media Pool by the column that will put all clips in the order you want them to

be assembled.


Right-click the bin in the Bin list, and choose Create Timeline Using Bin.


Type the name of the new timeline in the New Timeline Properties dialog. If you want to use

the In and Out points of each clip, make sure “Use Selected Mark In/Out” is checked, and click

Create New Timeline.

To create a timeline using manually selected clips:


(Optional) Put the Media Pool into List mode, set In and Out points for each clip in your

Bin, and sort the Media Pool by the column that will put all clips in the order you want

them to be assembled.


Select one or more clips you want to assemble into a new timeline.


Right-click one of the selected clips, and choose Create Timeline Using Selected Clips.


Type the name of the new timeline in the New Timeline Properties dialog. If you want to use

the In and Out points of each clip, make sure “Use Selected Mark In/Out” is checked, and click

Create New Timeline. By default, Audio Track Type is set to “Based on selected media,” so the

timeline audio tracks reflect the track mapping of the clips you’ve selected, but you can manually

choose other specific mappings if you need to.

Creating Timelines Using an IMF

or DCP Composition Playlist (CPL)

You can create a timeline in DaVinci Resolve that exactly replicates the Composition Playlist (CPL)

of a DCP or IMF package. This is currently a DaVinci Resolve Studio only feature.

To create a timeline using a Composition Playlist (CPL):


Import an IMF or DCP package into the Media Pool, like any other piece of media.


Right-click on the imported clip and choose “Create New Timeline Using Composition Playlist”

from the contextual menu.


In the New Timeline dialog box, choose a specific CPL from the package in the

“Composition Playlist” drop-down menu.


Make any other normal new Timeline adjustments you may need (such as Resolution,

Aspect Ratio, etc.), then click the “Create” button.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

Duplicating Timelines

You can also duplicate existing timelines in preparation for saving a copy prior to making modifications,

or as a starting point for a different version of your content.

To duplicate a Timeline, do one of the following:

�Select a timeline in the Media Pool, and choose Edit > Duplicate Timeline. The duplicate timeline

appears with “copy” appended to the name.

�Right-click a timeline in the Media Pool, and choose Duplicate Timeline from the contextual menu.

Disabling Timelines

You can disable/enable timelines in the Media Pool for both performance and organizational purposes.

This is particularly useful for editors who like to maintain a history of a program’s editing via an

ongoing series of periodically duplicated timelines. Since having a large number of timelines within

a single project file can affect performance, having the ability to disable timelines lets you maintain

these backup/alternate timelines without any penalty.

Disabled timelines are never loaded into RAM, have no effect on the speed at which a project opens,

saves, exports, or loads, and have no effect on program performance. A disabled timeline also hides

the timeline from the viewer drop-down menus throughout the program. Disabled timelines are

still visible in the Media Pool, but have a crossed out eye icon in the lower left to show the status.

A disabled timeline cannot be opened in any page of DaVinci Resolve.

To disable a timeline:

�Select the Timeline, right-click on it and choose “Disable Timeline” from the drop-down menu.

To enable a timeline:

�Select the Timeline, right-click on it and choose “Enable Timeline” from the drop-down menu.

The crossed-out eye in the lower left of the

thumbnail indicates this Timeline is disabled.

TIP: Enabled and Disabled timelines can

be easily grouped and organized across the

entire project by creating a Smart Bin with the

MediaPool Properties > Timeline fields, and

choosing “is Enabled/Disabled.”

Adding Media Pool Timelines

Directly to the Render Queue

You can add a timeline directly to the Deliver page’s Render Queue by right-clicking on the timeline

and hovering over the Add to Render Queue Using, and making a selection from the list of presets.

You can add your own presets to this list by saving a new custom preset in the Deliver page.

You will then be prompted for the location to render the file. The timeline will be added to the Render

Queue in the Deliver page but will not start rendering until the Render All button is pressed.


Edit | Chapter 34 Creating and Working with Timelines

EDIT

Select a Preset from the “Add to Render Queue Using” menu option to directly send the timeline to the Render Queue