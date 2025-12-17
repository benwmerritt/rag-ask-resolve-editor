---
title: "Importing and Exporting Stills"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 587
---

# Importing and Exporting Stills

It’s possible to import still images in different graphics formats into the Gallery, which can be

particularly useful when a client provides reference images to which they’d like you to refer. It’s also

possible to export stills from the Gallery, which is good for sending a series of reference stills for

approval to a remote client. In both cases, you can choose whether to import or export images with an

accompanying LUT.

For both import and export, DaVinci Resolve supports the following file formats: DPX, CIN, TIFF, JPEG,

PNG, PPM, BMP, and XPM.

To import one or more still images:


Right-click anywhere on the gray background of the Gallery.


Choose one of the following commands:

�Import: Imports image files, along with a matching DRX file, if one is present in

the selected directory.

�Import With Output LUT: Imports an image and DRX file, along with a matching LUT file,

if one is present in the selected directory.


When the Import Stills dialog appears, choose the type of files you want to import from the

“Files of type” drop-down menu, then navigate to the files you want to import, select them,

and click Import.

To export one or more still images:


If you want to export Gallery stills with labels that have been added to them, right-click anywhere

in the background of the Gallery and choose “Use labels on still export” in the contextual menu so

it becomes checked.


Select one or more stills in the Gallery.


Color | Chapter 141 Using the Gallery

COLOR


Right-click one of the selected stills, and choose one of the following commands:

�Export: Two files are saved for each still you selected. An image file in the format of your choice,

and a DRX (DaVinci Resolve eXchange) file that contains the grading metadata that was saved

with that Gallery still.

�Export With Display LUT: If you have a Video Monitor Lookup Table specified for the current

project in the Color Management panel of the Project Settings, this command will output the

image as it is processed by the specified LUT. A DRX file is also output containing the grading

metadata that was saved with that Gallery still.


When the Export Stills dialog appears, choose a file format to export to from the “Files of type”

drop-down menu, then choose a location, type a name into the Save As field, and click Save.

Each of the selected stills is exported with all accompanying files. Each file uses as its prefix the

name you typed into the Export Stills dialog, followed by an underscore, the still ID number of the

selected still, and the three-letter file extension.

To export the grade only (.DRX file) and no image:

Normally when you export a still from the Gallery, it exports both an image file and a .drx file that

contains the grade for that image. If you wish to export only the (.drx) grades from the Color Gallery,

and not the associated images, you can now do this by right-clicking on a a Gallery still or stills and

selecting Export from the drop-down menu. In the resulting file browser select .drx from the file format

selector, and press export.

Using and Organizing Memories

Stills and memories contain identical information, and can be split screened, copied, appended,

exported, and can display their node graph just like any other still. However, stills that are assigned as

a memory make them easier to access via keyboard shortcuts.

Memories are hidden by default, but you can reveal them by clicking the Memories button to the right

of the Gallery list button at the top-left of the Gallery.

Place grades you will use often in Memories for faster recall

The Memories thumbnail display makes it easy to keep track of which stills have been assigned

to which memories in situations where you’re using multiple memories to copy grades throughout

a program.


Color | Chapter 141 Using the Gallery

COLOR

To copy stills and memories back and forth, do one of the following:

�Drag a still onto a memory bank.

�Drag a memory into the Gallery.

TIP: In this way, memories can be used to copy stills from one album to another.

To save the current clip’s grade to a memory for future use, do one of the following:

�Choose Color > Memories > Save Memory A–H (Option-1 through 8).

�Using the DaVinci Resolve Advanced control panel, press CRNT on the Search Dial panel, then

press the letter of the memory bank you want to save to. Use the SHIFT UP and SHIFT DOWN

buttons to save to another memory sharing the same button.

�If you save a grade to a memory that already contains something, the previous memory

is overwritten.

To apply a memory to the current clip in a timeline:

�Right-click a memory and choose Apply Grade.

To clear a memory:

�Right-click a memory, then choose Clear.


Color | Chapter 141 Using the Gallery

COLOR

Chapter 142

Grade Management

The Color page offers numerous ways of saving grades, copying grades, creating

and altering groups of clips to share grades, rippling grades and adjustments, and

managing multiple versions of grades.

All of these procedures enable you to work faster by leveraging work you’ve already done to apply to

other clips that can benefit from the same adjustments, or by applying changes across multiple clips

all at once.

Contents

Using Versions to Manage Grades������������������������������������������������������������������������������������������������������������������������������������������� 3274

Choosing to Copy Grades Manually or Automatically Using Versions�������������������������������������������������������������������� 3274

Using Local Versions by Default�������������������������������������������������������������������������������������������������������������������������������������������������� 3276

Using Remote Versions to Enable Automatic Linking������������������������������������������������������������������������������������������������������ 3276

Creating a Master Timeline����������������������������������������������������������������������������������������������������������������������������������������������������������� 3278

Working with Versions���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3281

The Importance of “Version 1”����������������������������������������������������������������������������������������������������������������������������������������������������� 3283

Deleting Unused Versions������������������������������������������������������������������������������������������������������������������������������������������������������������� 3284

Rendering Versions�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3284

Copying Grades �������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3285

Protecting Adjustments with the Copy Grade Options��������������������������������������������������������������������������������������������������� 3285

Copy and Paste From One Clip to Another��������������������������������������������������������������������������������������������������������������������������� 3286

Copy and Paste Specific Parameters Using Paste Value����������������������������������������������������������������������������������������������� 3286

Applying Saved Grades From the Gallery����������������������������������������������������������������������������������������������������������������������������� 3286

Preparing to Copy or Apply Grades������������������������������������������������������������������������������������������������������������������������������������������ 3287

Copying Grades Using the Pointer������������������������������������������������������������������������������������������������������������������������������������������� 3288

Copy Forward Commands������������������������������������������������������������������������������������������������������������������������������������������������������������ 3288

Copying Using Memories�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3289

Copying Using Preview Memory������������������������������������������������������������������������������������������������������������������������������������������������ 3289

Copying from Stills in the Gallery����������������������������������������������������������������������������������������������������������������������������������������������� 3290

Append Node Graph������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3290

Aligning Keyframes to a Specific Frame While Copying Grades�������������������������������������������������������������������������������� 3291


Color | Chapter 142 Grade Management

COLOR

Copying Individual Nodes and Settings��������������������������������������������������������������������������������������������������������������������������������� 3291

Copying and Pasting All Settings From One Node to Another������������������������������������������������������������������������������������ 3291

Paste Attributes on the Color Page������������������������������������������������������������������������������������������������������������������������������������������ 3292

Copying from the Node Graph of Other Clips or Gallery Stills������������������������������������������������������������������������������������ 3292

Rippling Adjustments Among Multiple Clips���������������������������������������������������������������������������������������������������������������������� 3296

Appending a Node to Multiple Clips��������������������������������������������������������������������������������������������������������������������������������������� 3297

Using Shared Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3297

What Are Shared Nodes Good For?����������������������������������������������������������������������������������������������������������������������������������������� 3298

Creating Shared Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3298

Locking Shared Nodes�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3298

Copying Shared Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3298

Converting Shared Nodes Back to Corrector Nodes������������������������������������������������������������������������������������������������������ 3299

Deleting Shared Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3299

Using Adjustment Clips������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3300

Using Groups���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3301

Creating and Managing Groups������������������������������������������������������������������������������������������������������������������������������������������������� 3302

Using Group Modes to Control Which Grades Ripple and Which Don’t���������������������������������������������������������������� 3303

Collapse Group Grades������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3306

Exporting Grades and LUTs��������������������������������������������������������������������������������������������������������������������������������������������������������� 3307

Using Versions to Manage Grades

Working quickly requires a mastery of the numerous grade management features built into DaVinci

Resolve. These features are designed to help you copy and ripple grades to individual clips, among

manually defined groups of clips via the Node Editor’s Clip mode, or among automatically linked clips

that share the same source clip in the Media Pool (when using Remote versions). Multiple versions of

grades are supported for every clip, as are various options for previewing, overwriting, and appending

these versions.

Choosing to Copy Grades Manually

or Automatically Using Versions

Each grade you apply to a clip is a version. Each clip can have multiple versions, although only one

version can be applied at a time. By default, the first grade applied to every clip in a timeline is a

local version named “Version 1.” A clip’s version name and/or number appears underneath the clip

thumbnail, to the right. You can also see the version name, along with a list of all the other versions

that are currently available to that clip, by right-clicking a clip in the Timeline and looking for the

version names that appear underneath the Local Versions submenu.


Color | Chapter 142 Grade Management

COLOR

Selecting versions of grades from the Timeline thumbnails

NOTE: Double-clicking the version name underneath a clip’s thumbnail in the Timeline cycles

the version names, the clip names, and the codec used by each clip.

There are two different types of versions in DaVinci Resolve, each of which provides a

different method of grade management and linking among the clips and timelines of a project.

Local versions: The default mode of grade management. Clips using local versions are

unlinked, so each clip has its own grade which is not shared with any other clips in any other

timelines. Changing the grade of a clip using a local version has no effect on any other clip in

that project.

Remote versions: An alternate mode of grade management that you can enable. All clips

using remote versions that share the same source clip in the Media Pool are automatically

linked, in all timelines, and share the same set of grades.

If you use local versions to grade all your clips, you don’t have to worry about one clip’s grade being

accidentally copied to other clips that happen to come from the same file in the Media Pool, which can

make it easier to work. On the other hand, you need to manually copy every grade that you want to

duplicate, even among clips that clearly come from the same take or angle. You can always create a

group to share a grade among clips using local versions, but that’s an extra step.

Switching to use remote versions, instead, puts you into a mode where clips using remote versions

that share the same media file are automatically linked together. This gives you a convenient

shortcut for grading your program, since a grade that’s applied to one linked clip is automatically

copied to every other clip it’s linked to, which can be convenient when grading a series of headshots

appearing throughout a program that come from the same interview take. Another use of remote

versions is when you’re importing a new edit of an already graded timeline. Using remote versions,

you can set your project up so that new incoming timelines are automatically relinked to the previous

timeline’s grades.

The only disadvantage to using remote versions is that when you find you need to make individual

adjustments to clips that are linked, it’s an extra step to either create another version, or switch that

clip to use a local version, in order to keep its adjustment separate. This will be discussed in more

detail later in this chapter.

Mixing Versions

Each clip is capable of having multiple local and remote versions at the same time; you get to choose

which to apply. Which type of versioning is best depends on the type of project you’re working on,

the way in which the media was shot, and how you like to work. The following sections explain the

differences in workflow.


Color | Chapter 142 Grade Management

COLOR