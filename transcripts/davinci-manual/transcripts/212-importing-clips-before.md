---
title: "Importing Clips Before"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 212
---

# Importing Clips Before

Importing an EDL, AAF, or XML

When you import media prior to importing an EDL, DaVinci Resolve follows a specific set of rules to

determine which Media Pool clips correspond to clips in the resulting timeline. These rules also apply

to situations where you’ve imported media prior to importing an AAF or XML file, in situations where

you want to prioritize specific media over the file paths embedded in those imported timeline formats.

The following sections go into detail on what these rules are, and how to use them to your advantage.

Essential Clip Metadata for Easy Conforming and Relinking

When conforming projects in DaVinci Resolve, the accuracy and integrity of clip metadata is critical

for a successful result. Keep the following three criteria in mind when you’re preparing media to use in

DaVinci Resolve.

�Accurate timecode: Essential for every clip. First off, each clip should have a valid timecode

track, and it should go without saying that the timecode should match the same timecode used

by all other instances of that media file in a particular project. If there are problems with a clip’s

timecode, DaVinci Resolve has tools you can use to edit or offset timecode to account for known

inconsistencies. By default, the “Use Timecode” project setting is set to “Embedded in the

Source Clip,” so that timecode is read from the embedded timecode track within a QuickTime or

MXF file, or from the header data of a DPX frame file. However, you can also choose the “From the

source clip frame count” option which enables timecode to be read from the Source clip’s frame

count for image sequences.

�File names: When “Assist using Reel Names” in the General Options panel of the Project Settings

is off (the default setting), this forces DaVinci Resolve to conform clips using file names when

importing XML and AAF projects. File names can only be only used when conforming XML or AAF

files, or when importing a DaVinci project; file names are never used when conforming EDLs.

�Reel Name: Only used for conforming if “Assist using Reel Names” is on in the General

Options panel of the Project Settings. Assigning reel names to your media is not essential, but

recommended, and can make media management easier for certain operations, especially in EDL

workflows. However, if you experience problems conforming clips with “Assist using Reel Names”

turned on, you should try turning it off as one possible troubleshooting step.

How DaVinci Resolve matches media files to clips in an imported project depends on how

you’re importing the project.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

Defining Clip Metadata When Adding Media to the Media Pool

For workflows where you’re manually adding media files to the Media Pool when you’re editing from

scratch in DaVinci Resolve, preparing to process dailies, or as a separate step before importing EDL,

XML, or AAF project files and reconforming them to a higher quality set of media than what was

originally used to edit with, the rules for how clip metadata is defined in preparation for conforming

are a bit different.

Timecode: Calculated using the “Timeline Frame Rate” setting in the Master Project Settings

panel of the Project Settings.

Reel Names: Determined depending on whether the “Assist using Reel Names from the”

checkbox is on or off in the General Options panel of the Project Settings, and on which

option you’ve selected. Reel names can be extracted dynamically, so any time you change

this setting the reel names in the Media Pool update to reflect the change, or they can be

defined manually, in which case you can set different clips to use different methods of reel

name extraction.

Clip Names: Read and stored, used for AAF and XML imports, but not used for

imported EDLs.

How Reel Names Are Identified

The “Assist using Reel Names” checkbox in the General Options panel of the Project Settings is an

extremely important setting for controlling how the conform process works. By default, it’s turned off,

and reel names are left blank. This is fine for conform workflows where all you need is the file path

or file name and source timecode to successfully identify which media files correspond to what clips.

However, if you need more information than that to reconform the clips in your project, you can turn

on the “Assist using Reel Names” checkbox to enable DaVinci Resolve to use one of four different

methods to automatically define reel names for every clip in the Media Pool.

Automatically Defining Reel Names

When you use the “Assist using Reel Names” options in the General Options panel of the Project

Settings, reel names are extracted dynamically. This means that any time you change the method of

reel name extraction in the Project Settings, the reel names of all clips in the Media Pool automatically

update to reflect the change. This can be seen in the Reel Name column that’s visible if you put the

Media Pool into List view. For example, were you to change the “Assist using reel names” options from

“Source clip file pathname” to “Mediapool folder name,” the contents of the Reel Name column would

visibly change. This is useful when you’re importing a project for which all clips use the same method

of determining their reel name.

Manually Choosing Reel Name Definitions for Individual Clips

You also have the option of manually choosing the criteria for how one or more selected clips in the

Media Pool have their reel names defined, using the Clip Attributes dialog. This is useful when there

are certain clips in a project that need to use a different method of reel name extraction, or manually

entered reel names.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

To manually define reel names for one or more clips:


Select one or more clips in the Media Pool.


Right-click one of the selected clips, and choose Clip Attributes from the contextual menu.


Open the Reel Name panel of the Clip Attributes dialog, choose a new option, and click OK.

Once you’ve used Clip Attributes to change the reel names of clips, those clips no longer automatically

update when you change the “Assist using Reel Names” options in the General Options panel of the

Project Settings.

For more information on using Clip Attributes, see Chapter 19, “Using Clip Metadata.”

Methods of Defining Reel Names

There are five options that are available for automatically determining how reel names are extracted

from the source media when “Assist using Reel Names” is turned on, and one option in the Clip

Attributes Reel Name panel for manually defining reel names. The use of reel names is critical in EDL

and AAF workflows, but isn’t necessarily as important in XML‑centric workflows.

�Source clip file pathname: Obtains the reel name by extracting it from each media file’s path. This

makes it possible to extract a reel name from all or part of the file name, or from all or part of the

name of any folder in the path that encloses that file. This extraction is defined using the Pattern field.

�Pattern: A code that defines how a reel name should be extracted from the source clip pathname.

More information about creating patterns appears later in this chapter.

�Media Pool folder name: The reel name is obtained from the name of the bin in the Media Pool

that encloses that clip. For example, in a stereoscopic workflow you might want to export offline

stereo media with the “Left” and “Right” bin names in which they’re organized as reel names.

Another example would be organizing VFX being incrementally processed in individually named

bins, such as “VFX_Tuesday_10-12.”

�Embedding in Source clip file: Useful for file formats where the reel name is embedded within the

media file itself. Blackmagic RAW and other digital cinema cameras, QuickTime files created by

Final Cut Pro, and DPX frame files are formats that can contain reel name header data.

�Source clip filename: If there is no defined reel number, often it’s easy to just use the

Source clip filename.

�User Defined: This option is only available when you manually alter the Reel Name for one or

more selected clips in the Media Pool using the Clip Attributes dialog. Choosing User Defined lets

you type any string of text you like to use as the reel name.

An additional checkbox is available, “Extract reel names from EDL comments,” which is

primarily useful for legacy workflows in which you conform an EDL exported from Final Cut Pro

7 to camera original R3D media.

Extract reel names from EDL comments: Some media file formats, such as R3D, have reel

names, obtained from the file names, that are longer than the eight characters that are

allowable in a standard EDL. This option allows DaVinci Resolve to extract reel names from

appropriately formatted EDL comments, such as those output from Final Cut Pro 7.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

Using the Pattern Field

If you’re using the Pattern option to extract the reel name from a clip’s source file pathname, you have

the option to create your own search pattern, enabling you to have DaVinci Resolve extract the reel

name in highly specific ways to accommodate more exotic workflows.

Extraction patterns are interpreted from right to left, deciphering each clip’s file path element by

element starting with the file name, and then considering each enclosing directory’s name to the left.

Each extraction pattern consists of a series of text characters and “wild card” operators in unique

combinations corresponding to the length and names used in the file path.

Here are a series of search characters that may be used.

Extraction Pattern Operators

?

Looks for matches of any single character. Add as many question marks as there are

characters you want to match. ?? matches two characters such as 02; ???? matches four

characters such as 0002.

*

A wildcard that creates matches for any sequence of zero or more characters.

%R

Specifies the reel name’s actual location. Reel names may contain any character,

but should not contain a directory separator (forward slash).

%_R

Extracts the reel name and strips out the R3D file name underscores found in EDLs from

Final Cut Pro 7 or earlier.

%D

Matches any directory name or file name. When this is the last operator in a pattern,

do not add a forward slash.

/

Used to separate any two operators

If you’re trying to create a new extraction pattern for a unique workflow, there’s a test dialog you can

use to try different patterns out before applying them to your project.

To test the extraction path:


Turn on “Assist using reel names from the” and click the Test button next to the current Pattern

in the General Options panel of the Project Settings. The “Specify Reel Extraction Pattern”

dialog opens.


Type the extraction patten you want to test into the Pattern field.


Using whatever method you prefer, find the file path of the media file that you want to test the

extraction pattern on, and copy or type it into the Sample Path field.


Click Test.


If the reel name that appears below is correct, then click Apply to copy the extraction pattern into

the Pattern field of the General Options panel of the Project Settings. If the reel name that appears

is not correct, modify the extraction pattern and try again.

Examples of Reel Name Extraction Patterns

To better understand how this process works, below are several examples showing the various

methods of reel name extractions. The / is used as the separator between control parameters.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT

Example 1

This example shows the reel name stored within the parent folder name of the clip.

•	 Pattern: */%R/%D

•	 File path: vol0/MyMovie/Scans/004B/Frame[1000-2000].dpx

•	 Reel name: 004B

Parsing takes place from right to left so to analyze this pattern start at the right end. In this

case the %D matches to the file name “FrameNNNN.dpx” where NNNN is the frame number

in each file of the clip. Moving left of the file name, the /%R/ section of the string is next. This

specifies that the reel name will be the entire name of the parent directory immediately above

the file. Then the * at the beginning of the string says match any pathname in front of the

directory name that has the reel name. This string would find the parent directory regardless

of how many levels deep it is nested on the directory path.

Example 2

Here we see the reel name stored in the parent folder name of the clip and prefixed with the

reel name.

•	 Pattern: */????%R/%D or alternatively */Reel%R/%D

•	 File path: /vol0/MyMovie/Scans/Reel1234/Frame[1000-2000].dpx

•	 Reel name: 1234

In this example both of these extraction patterns produce the same result. They are also

similar to the first example. The reel name is still in the parent directory name but in this case

it will have the fixed characters “Reel” prefixed in front of the reel name. The first pattern with

???? would actually match with any 4 characters in front of the reel name. The second pattern

is more specific and would only match the word “Reel” in the directory name.

Example 3

This example shows the reel name stored within the parent folder name two directory

levels up.

•	 Pattern: */%R/%D/%D

•	 File path: /vol0/MyMovie/Scans/004B/134500-135000/Frame[1000-2000].dpx

•	 Reel name: 004B

This example is again similar to Example 1. The difference is that in Example 3, the reel name is

the directory name two levels above the clip. In Example 1, the reel name was in the directory

name only one level up.

Example 4

Finally, we see the reel name that is embedded within the clip name of the material.

•	 Pattern: */Reel%R_*

•	 File path: /vol0/MyMovie/Scans/Reel004B_[1000-2000].dpx

•	 Reel name: 004B

This example shows a method for extracting the reel name from the file name of the clip.

Again, starting at the right the two pattern characters “_*” match any series of characters up to

the first underscore character. In this case it will pick up the file extension (.dpx) and the frame

number portion of the file name. Next, the “/Reel%R” characters indicate the reel name is

the characters between the “/Reel” and _ character. The * at the beginning of the pattern will

match a file path any number of directories deep in front of the file name.


Import and Conform Projects | Chapter 56 Conforming and Relinking Clips

EDIT