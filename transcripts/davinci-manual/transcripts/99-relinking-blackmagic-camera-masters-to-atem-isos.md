---
title: "Relinking Blackmagic Camera Masters to ATEM ISOs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 99
---

# Relinking Blackmagic Camera Masters to ATEM ISOs

The ATEM records each camera’s ISO as an H.264 HD video stream, which may not be of high enough

resolution or quality for some purposes. It’s possible to instantly switch your ATEM camera ISOs to the

original camera recordings made in a Blackmagic Camera instead. This workflow enables the highest

visual quality of Blackmagic RAW and the ability to output in higher resolutions (such as 4K or UHD)

than are supported by the ATEM internally. Essentially, the ATEM can reference an additional set of

higher quality ISOs recorded in the cameras, rather than those from the ATEM itself. This feature is

only available using Blackmagic Cameras.

This workflow requires one more step in the process, namely making sure that you have sufficient

recording space attached to each camera to record the show in its entirety. Refer to your ATEM’s

specific documentation for how to set up ISO recording and camera control, but one important setting

is to make sure that you’ve checked the “ISO Record All Inputs” and the “Record in All Cameras”

settings in the ATEM software control before you start shooting.

To relink to Blackmagic Camera masters from ATEM ISO recordings:


(Before you shoot) Check the “Record in All Cameras” setting in the ATEM software control.


(Before you shoot) Check the “ISO Record All Inputs” setting in the ATEM software control.


At this point, record your show using the ATEM device and note the project’s folder location.


Copy all the resulting camera masters from each camera’s memory card to the ATEM project’s

“Video ISO Files” folder, and then import the project into DaVinci Resolve.


DaVinci Resolve automatically creates a separate Blackmagic RAW folder in your project and

moves all the camera masters to that folder.


Use the menu Timeline > Switch to Camera Originals to instantly switch between referencing the

ATEM H.264 ISOs and the Blackmagic Camera masters.

The Show Camera Originals button

Once your project is imported successfully into DaVinci Resolve, it can be edited using the variety

of specialized Multicam editing tools found in the Cut page, including the Sync Bin, Live Overwrite,

and the DaVinci Resolve Speed Editor.

For more information on using these tools, see Chapter 28, “Fast Editing in the Cut Page.”


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

Media Pool Views

Once you’ve imported some clips into the Media Pool, three controls at the upper right-hand side let

you control how they look, depending on what you need to accomplish.

The View Mode buttons

Metadata View

In the Metadata view mode, each clip is represented by its own card with a thumbnail and basic

clip metadata information visible. This view is designed to have more metadata information than a

thumbnail but more targeted information than the List view. This feature, combined with its sort modes,

is a powerful way to organize and reorganize your clips in the Media Pool.

The metadata fields of the Metadata view (from the top down):

�Thumbnail: A scrubbable thumbnail image of your clip.

�Row 1: A main description field that is variable and determined by the sort order selection.

�Row 2: Start Timecode, Date Created, Camera #.

�Row 3: Scene, Shot, Take.

�Row 4: Clip Name, Comment.

The Metadata View icon view (highlighted icon in the top bar),

showing the thumbnail being scrubbed next to the clip’s metadata

The strength of the Metadata view is the automatic clustering of your clips in the Source Tape,

based on the sort order you choose in the Media Pool Sort By menu at the very upper-right

corner of the Media Pool. It is also possible to use these sort options in the Thumbnail, List, and

Filmstrip views as well.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

The sort modes available in the Metadata view are:

The Media Sort options

�Timecode: This mode clusters the clips by creation date,

changes the main description field to creation date and

start timecode, and orders the list by timecode.

�Camera: This mode clusters the clips by Camera #,

changes the main description field to camera # and start

timecode, and orders the list by timecode.

�Date Time: This mode clusters the clips by day, changes

the main description field to creation date and file name,

and orders the list by timecode.

�Clip Name: This mode clusters the clips by the first

letter of the clip name in alphabetical order, changes

the main description field to clip name, and orders the

list by timecode.

�Bin: This mode clusters the clips by bin, changes the

main description field to clip name, and orders the

list by timecode.

�Scene, Shot: This mode clusters the clips by scene,

changes the main description field to scene-shot-take,

and orders the list by scene-shot-take.

�Clip Color: This mode clusters the clips by clip color

name, changes the main description field to creation

date and start timecode, and orders the list by timecode.

�Date Modified: This mode clusters the clips by day,

changes the main description field to creation date and

file name, and orders the list by the last time the clip was

modified by the OS filesystem.

�Date Imported: This mode clusters the clips by day,

changes the main description field to creation date and

file name, and orders the list by the date the clip was

added to the Media Pool.

�Online Status: This mode clusters the clips by proxy or

original status.

�Ascending: Orders the Media Pool from lowest

numerical value to highest, and alphabetically

from A to Z.

�Descending: Orders the Media Pool from highest

numerical value to lowest, and alphabetically

from Z to A.


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

Each different sort mode changes the main description field on the card and re-arranges the Source

Tape to reflect the selected organization method.

(Top) The Metadata view with clips sorted by Scene-Shot-Take

(Bottom) The Metadata view with the same clips sorted by Camera


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT

Thumbnail View

Each clip is represented by a scrubbable thumbnail. Hover the playhead over each thumbnail and

move it left and right to see the clip’s image play, and use the I and O keys to mark sections of a clip

that you want to use. Hover scrub can be enabled and disabled using the Media Pool option menu on

the Edit page.

The Icon View mode

Filmstrip View

Each clip is represented by a filmstrip of consecutive frames the length of the Media Pool. Hover the

playhead over the clip and move it left and right to see the clip’s image play, and use the I and O keys

to mark sections of a clip that you want to use.

The Filmstrip View mode


The Cut Page | Chapter 27 Importing and Organizing Media in the Cut Page

CUT