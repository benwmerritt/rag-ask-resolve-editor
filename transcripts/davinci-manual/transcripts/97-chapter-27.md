---
title: "Chapter 27"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 97
---

# Chapter 27

Importing and

Organizing Media

in the Cut Page

Before you can start editing, you need to import the clips you want to use for your

program into the Media Pool, which is the central repository of clips in your project.

This can include video, audio, and graphics files in any format that’s supported by DaVinci Resolve.

Once imported, the Media Pool on the Cut page has many organizational tools you can use to make

your project’s media faster for you to access and sort through as you find the clips you need to create

your program.

Contents

Importing Media������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 517

Removing Media������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 518

Organizing Media into Bins�������������������������������������������������������������������������������������������������������������������������������������������������������������� 518

Master Bin�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 518

Creating and Using Bins��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 518

Opening Bins������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 519

Create Bin With Selected Clips������������������������������������������������������������������������������������������������������������������������������������������������������� 519

Renaming Bins����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 519

Import and Export Specific DaVinci Resolve Project Bins ����������������������������������������������������������������������������������������������� 520

Import and Export Individual DaVinci Resolve Timelines ������������������������������������������������������������������������������������������������ 520

Sync Media Pool Bins with File System Folders������������������������������������������������������������������������������������������������������������������� 521

Import Blackmagic Cloud Shared Folders to Media Pool����������������������������������������������������������������������������������������������� 523

ATEM Switcher Integration�������������������������������������������������������������������������������������������������������������������������������������������������������������� 524

Importing ATEM Mini Pro ISO Projects��������������������������������������������������������������������������������������������������������������������������������������� 525

Relinking Blackmagic Camera Masters to ATEM ISOs������������������������������������������������������������������������������������������������������� 526

Media Pool Views��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 527

Metadata View��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 527


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

Importing Media

Two Import buttons at the top of the Media Pool let you use import dialogs to select media you want to

bring into the Media Pool for use in your project.

The Import Media and Import Folder buttons

To import individual clips:


Do one of the following:

a)	 Click the Import Media button.

b)	 Press Command-I.

c)	 Right-click the Media Pool and choose Import Media.


Use the Import dialog to select one or more clips to import, and click Open.


If you’re prompted to change the frame rate of a currently empty project to match that of the

incoming media, click Change.

Each piece of media you import, whether it’s video, audio, or graphics, appears as an individual clip in

the Media Pool. You can also import an entire folder full of media as a bin in the Media Pool.

Thumbnail View ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 530

Filmstrip View����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 530

List View����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 531

Metadata Display Palette������������������������������������������������������������������������������������������������������������������������������������������������������������������ 531

Sorting and Searching����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 532

Searching�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 532

Navigable Clip Paths��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 532

Sort Media By����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 532

Finding Timeline Clips in the Media Pool���������������������������������������������������������������������������������������������������������������������������������� 533

Clip Color�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 533

Relinking Media������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 534

Relink Media�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 534

Relink Selected Clips�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 535

Voiceover Tool��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 536

Using Voiceover on the Cut Page������������������������������������������������������������������������������������������������������������������������������������������������� 536

ATEM Switcher Integration�������������������������������������������������������������������������������������������������������������������������������������������������������������� 539

Importing ATEM Mini Pro ISO Projects��������������������������������������������������������������������������������������������������������������������������������������� 539

Relinking Blackmagic Camera Masters to ATEM ISOs������������������������������������������������������������������������������������������������������� 540


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

To import a folder full of media into a bin:


Click the Import Media Folder button.


Use the Import dialog to select a folder containing media you want to import, and click Open.


If you’re prompted to change the frame rate of a currently empty project to match that of the

incoming media, click Change.

Each folder you import appears as a bin in the Media Pool. Double-clicking a bin opens its contents

into the Media Pool, enabling you to view each individual clip.

TIP: For additional media import features, you can use the Media page, with its Media

Storage browser and more feature-rich version of the Media Pool.

Removing Media

If there are clips you no longer want in your project, you can simply select them and press the Delete

or Backspace keys. A Dialog asks if you want to remove the selected clip or clips; clicking Remove will

remove them from the Media Pool, while leaving them intact on your media storage device.

If you want to remove every clip in the currently open bin (even the Master bin), you can also right-click

anywhere within the Media Pool and choose Remove All Clips in Bin from the contextual menu.

Organizing Media into Bins

For short projects, having all your clips together in a single bin (the Master bin is the top level of

the Media Pool) can be fast. However, for longer projects, organizing your media into subsets

of clips within individual bins can make browsing each bin’s contents using the Source Tape of

the Viewer more manageable.

TIP: You can move clips you know you don’t want, such as instances where the camera rolled

on unusable scenery or moments, or completely unusable takes, into another bin so those

clips don’t present themselves in the Source Tape for bins containing clips you want to use.

Master Bin

At the top level of your project hierarchy is the Master bin. The Master bin contains all of the media

content (clips, timelines, graphics, other bins, etc.) for your project. In the Cut page, the Master bin

also shows all of your project’s timelines for easy access, regardless of where they’ve been created in

your project.

Creating and Using Bins

You can create bins with which to organize your media by choosing File > New Bin (Shift-Command-N),

or by right-clicking in the Media Pool and choosing New Bin from the contextual menu. You can create

bins inside of other bins, and in so doing hierarchically organize the clips you need in a variety of ways.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

Bins seen in the Media Pool

Once you’ve created a bin, you can move one or more selected clips into it via drag and drop, just as

you would on the desktop of your operating system’s file manager.

Opening Bins

Any visible bin in the Media Pool can be opened by double-clicking it, or by clicking the Bin drop-

down at the upper left-hand corner of the Media Pool and choosing a bin to open from the menu

(they’re shown as a hierarchical list). When opened, a bin’s contents fill the Media Pool, and a path

indicator at the top of the Media Pool lets you see how many levels deep you are in cases where you

have bins inside of bins. You can click any level of this path to jump back up the hierarchy, or you can

choose another bin from the Bin drop-down.

The hierarchical Bin drop-down menu

Create Bin With Selected Clips

You can also create a bin and put clips into it in one step. Select one or more clips in the Media Pool,

right-click one of the selected clips, and choose Create Bin With Selected Clips from the contextual

menu. A new bin appears called “Bin X” (where X is the next number that’s available) displaying the

selected clips it now contains.

Renaming Bins

To rename a bin, click its name once, then slowly click a second time (clicking too fast is a “double-

click” which opens the bin), and the name becomes highlighted, ready for editing. You can also right-

click a bin and choose Rename Bin from the contextual menu, which also highlights the bin’s name,

ready for editing. When you’re done typing a new name, press Return (or Enter).


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

Import and Export Specific DaVinci Resolve Project Bins

You can import/export specific bins from one DaVinci Resolve project to another, allowing you to pass

bins quickly between projects and workstations that have access to the same media. All Metadata, In/

Out points, Timelines, etc. are transferred along with the clips in the bin, but none of the actual media

files are included.

To export bins from the Media Pool:


Select one or more bins in the Media Pool.


Right-click the selection and choose “Export Bin,” or choose File > Export > Export Bin.


Choose where to save the DaVinci Resolve Bin file (.drb) in the file system dialog, and click Save.

To import bins into the Media Pool:


Right-click in the Media Pool and choose “Import Bin,” or choose File > Import > Import Bin.


Do one of the following:

�Choose a DaVinci Resolve Bin file (.drb) from the file system dialog.

�Double click the .drb file in your file system.

The bin or bins will appear in the Media Pool. Any bins imported this way will have the word “import”

appended to their name, to avoid duplicate names. If you import a bin that contains clips that were

already in the Media Pool, the potentially duplicate clips are excluded from the import and instead

relinked to the media referenced by your project. This keeps your Media Pool tidy. However, if the bin

or bins have been moved to another computer, you may have to relink offline media.

Import and Export Individual DaVinci Resolve Timelines

You can export and import individual timelines from one DaVinci Resolve project into another

previously existing DaVinci Resolve project, allowing you to pass timelines quickly between projects

and workstations, without creating additional imported project files. Just the timeline and its

associated clip information is exported, none of the actual media files are included.

To export a timeline from the Media Pool:


Select a timeline from the Media Pool.


Choose File > Export > Export AAF, XML, DRT (Shift-Command-O).


Choose “DaVinci Resolve Timeline Files (*.drt)” from the format options drop-down in the file

system dialog.


Choose where to save the DaVinci Resolve Timeline file (.drt) in the file system dialog,

and click Save.

To import a timeline into the Media Pool:


Choose a bin in the Media Pool in which you want the imported timeline to be saved.


Do one of the following:

�Choose File > Import Timeline > Import AAF, XML, DRT (Shift-Command-I), then Select a DaVinci

Resolve Timeline file (.drt) from the file system dialog, and click Open.

�Double click the .drt file in your file system.

The timeline will appear in the Media Pool, along with all of the clips associated with it. Any timelines

imported this way will have the word “import” appended to their name, to avoid duplicate names.

The imported timeline will be automatically conformed to corresponding media that’s already in the

Media Pool. However, if the timeline has been moved to another computer, you may have to reimport

or relink missing or offline media in to bring the imported timeline fully online.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

NOTE: Only a single timeline can be imported and exported at a time using this method.

To import or export multiple timelines, use the Import/Export Bin function described above.