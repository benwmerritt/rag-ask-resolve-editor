---
title: "What Are Mattes For?"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 73
---

# What Are Mattes For?

Matte files are useful for two things. Traditionally, mattes are grayscale media files that identify

regions of varying opacity, with white representing solid areas, and black representing transparency.

For example, exported clips from a compositing application sometimes are accompanied by one or

more matte files that correspond to keys or rotoscoped mattes from the composite. By importing these

matte files using the “Add as Matte” command, you can attach them to the clips they belong to in the

Media Pool, so that they’re only available to the clips they’re synced to.

However, mattes can also be used as creative tools to apply grain and texture for effect. What a matte

does depends on how you connect it in the Node Editor of the Color page. These are media files that

you may want to use as mattes for potentially any clip, so they can also be added to the Media Pool as

a so-called timeline matte, that can be applied to any clip you want.

TIP: If necessary, you can also apply LUTs to both clip mattes and timeline mattes in

the Media Pool, simply by right-clicking a matte, and choosing a LUT from the 1D LUT or

3D LUT submenus. This can be helpful for adjusting incorrectly formatted mattes.

Adding Mattes

To use mattes, you need to add them in very specific ways.

To assign a matte to a clip in the Media Pool:


Select a clip in the Media Pool to which you want to attach an external matte.


Select the matching external matte file in the Media Storage panel, right-click it, and choose

Add to Media Pool as a Matte.

The matte is attached to the clip as a clip matte. A badge indicates that clip has a matte when the

Media Pool is in Icon view, and the matte itself can be seen, if you put the Media Pool into List

view, appearing as a nested item underneath the clip it’s attached to.

Removing mattes from clips in the Media Pool:


Put the Media Pool into List view.


Right-click the external matte file you need to remove, and choose Remove Selected Clips.

Removing an external matte clip also removes that matte’s key from any clip grades that use

it, such that any clips using it as a key input change from a secondary operation to a primary

operation, where the color adjustment affects the entire image.

To add a timeline matte to the Media Pool:


Make sure no clip is selected in the Media Pool.


Select an external matte file in the Media Storage panel, right-click it, and choose Add to Media

Pool as a Matte.

The external matte appears in the Media Pool as a timeline matte.

You can also assign mattes to clips directly in the Color page, which can sometimes be faster.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

To assign a matte to a clip in the Color page:

�Drag any clip from the Media Pool to the Node Editor.

That clip appears an an External matte for the current clip’s grade in the Node Editor, and it’s also

automatically assigned to the current clip in the Media Pool.

For more information on using external matte clips as keys when grading, see Chapter 146,

“Combining Keys and Using Mattes.”

Using Embedded Mattes in OpenEXR Files

If you’re importing OpenEXR files with embedded matte passes, there’s nothing special you

need to do, as the mattes are within the clip you’ve just imported into the Media Pool.

For more information on how to use mattes within OpenEXR files, see Chapter 146,

“Combining Keys and Using Mattes.”

Adding Offline Reference Movies

When moving a project from another application to DaVinci Resolve, it’s useful to export the entire

program as a single media file for use as an Offline Reference Movie. Then, you can import this file

in a special way to use for dual Viewer comparison in the Edit page, or as a split-screen comparison

for fade wipe in the Color page. As of DaVinci Resolve 16 it’s no longer necessary to import reference

movies in this way to make an offline comparison, but it can still be convenient when managing

multiple timelines and versions that require great specificity.

To add a clip as an offline reference clip:

Right-click it in the Media Storage panel, and choose “Add As Offline Clip.”

That clip appears with a small checkerboard badge in its icon in the Media Pool, or as the icon

to the left of the Media Pool.

Checkerboard icon indicating

an Offline comparison video

For more information on using an offline video to compare with an imported Timeline in the

Edit page, see Chapter 55, “Preparing Timelines for Import and Comparison.”

For more information on split-screen reference of Offline video in the Color page, see Chapter

124, “Using the Color Page.”


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Extracting Audio in Media Storage

If there’s a video clip in the Media Storage panel that has audio you need, but you don’t want the video

component, you can use the Extract Audio command to create a self-contained audio clip that you can

then import into the Media Pool by itself.

To extract the audio from a media file:


Right-click a clip in the Media Storage panel, and choose Extract Audio.


Click the Browse button in the Extract Audio dialog to find another disk location for the

extracted clip.


Click Extract. The audio channels are extracted and written as a .WAV file to the selected

destination.


After you’ve extracted the stand-alone .WAV file, you’ll need to import it into the Media Pool if you

want to use it in your project.

Manually Organizing the Media Pool

Whether you’re doing onset work, creating digital dailies, organizing media to edit, or ingesting media

to conform to an imported project, it’s vitally important to stay organized. The Media Pool provides

many different tools for doing so. This section examines how you can create bins to manually organize

collections of clips.

To Select Clips in the Media Pool

There are a variety of ways you can make clip selections in the Media Pool in preparation for relinking,

unlinking, moving, duplicating, deleting, or doing any other operation to them.

•	 Click any clip to select it.

•	 Drag a bounding box around several clips to select them all.

•	 Hold the Command or Shift keys down and drag a bounding box around another

discontiguous group of clips to either add them to the current selection or remove them

from the current selection.

•	 Click one clip, then Shift-click another to select both clips and make a continuous selection

of all clips in-between. Shift-clicking another clip can expand or contract the selection.

•	 Command-click individual clips to select a discontiguous number of clips. Command-

click a clip that’s already selected to individually de-select it, while leaving the rest of the

selection alone.

•	 With one clip selected, hold the Shift or Command keys down and use the Arrow keys to

expand the selection to other clips.

Organizing Media into Bins

You can easily organize clips into different bins in the Media Pool. For some workflows, this is required,

while with other workflows it’s purely optional.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Methods of working with bins in the Media Pool:

�To add a bin to the Media Pool: Right-click in the Bin list and choose Add Bin. To add a bin inside

another bin, right-click any bin and choose Add Bin.

�To move selected clips into a new bin: Select all the clips you want to put into a new bin, then

right-click one of the selected clips, and choose Create Bin With Selected Clips.

�To rename a bin: Select the bin you want to rename, and then click its name a second time to

make it editable. With the bin name highlighted, type a new name and press Return. Alternately,

you can right-click a bin, choose Rename Bin, and then type a new name and press Return.

�To add incoming clips to a specific bin in the Media Pool: Click a bin to select it, then use any of

the previously described methods to add media from the Media Storage panel directly to that bin.

�To move media from one bin to another: Drag one or more selected clips from their current

location in the Media Pool into that bin. Multiple clips in the Media Pool can be selected by

Shift‑clicking or Command-clicking them, or by dragging a bounding box over a group of clips.

You can also drag one bin into another one.

�To delete a bin: Select the bin you want to delete, and press the Backspace or Delete key.

Or, right-click a bin and choose Delete Bin. Deleting a bin with nested bins inside of it results in

that entire set of bins being deleted.

�To sort bins: Right-click on any bin, and choose an option from the Sort By submenu. You can

choose from Name, Date Created, Date Modified, and User Sort.

�To reorganize bins manually: Right-click anywhere within the Bin list, and choose Sort By

> User Sort. Then, drag bins up or down in the Bin list to put them into the order you want.

An orange dividing line shows where dragged bins will be placed when you drop them and helps

you see when a bin you’re dragging will become nested within another bin or not. The User Sort

order is saved even when you change to another sort order, and selecting User Sort again results

in your custom sort order being recalled.

Import and Export DaVinci Resolve

Project Bins (.drb)

You can import/export specific bins from one DaVinci Resolve project to another, allowing you to pass

bins quickly between projects and workstations that have access to the same media. All Metadata,

In/Out points, Timelines, etc. are transferred along with the clips in the bin, but none of the actual

media files are included.

To export bins from the Media Pool:


Select one or more bins in the Media Pool.


Right-click the selection and choose “Export Bin,” or choose File > Export > Export Bin.


Choose where to save the DaVinci Resolve Bin file (.drb) in the file system dialog, and click Save.

To import bins into the Media Pool:


Right-click in the Media Pool and choose “Import Bin,” or choose File > Import > Import Bin.


Do one of the following:

�Choose a DaVinci Resolve Bin file (.drb) from the file system dialog.

�Double click the .drb file in your file system.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

The bin or bins will appear in the Media Pool. Any bins imported this way will have the word “import”

appended to their name, to avoid duplicate names. If you import a bin that contains clips that were

already in the Media Pool, the potentially duplicate clips are excluded from the import and instead

relinked to the media referenced by your project. This keeps your Media Pool tidy. However, if the bin

or bins have been moved to another computer, you may have to relink offline media.

Import and Export Power Bins

You can import and export Power Bins (bins that persist from project to project) as .drb files,

just like normal bins. Power Bins are hidden by default and can be turned on by clicking on the

Media Pool Option (3-dot) menu and selecting Show Power Bins.

Import and Export

DaVinci Resolve Timelines (.drt)

You can export and import individual timelines from one DaVinci Resolve project into another

previously existing DaVinci Resolve project, allowing you to pass timelines quickly between projects

and workstations, without creating additional imported project files. Just the timeline and its

associated clip information is exported, none of the actual media files are included.

To export a timeline from the Media Pool:


Select a timeline from the Media Pool.


Choose File > Export > Export AAF, XML, DRT (Shift-Command-O).


Choose “DaVinci Resolve Timeline Files (*.drt)” from the format options popup

in the file system dialog.


Choose where to save the DaVinci Resolve Timeline file (.drt) in the file system dialog,

and click Save.

To export multiple timelines from the Media Pool:


Select multiple timelines from the Media Pool.


Right-click on a timeline and choose Timelines > Export > DaVinci Resolve Timeline Files.


Select the folder where you wish to save them from your file browser.

Unlike exporting individual timelines, when exporting multiple timelines you will not be able to rename

the .drt files on export. They will retain the timeline name they have in the Media Pool.

To import a timeline into the Media Pool:


Choose a bin in the Media Pool in which you want the imported timeline to be saved.


Do one of the following:

�Choose File > Import Timeline > Import AAF, XML, DRT (Shift-Command-I), then Select a DaVinci

Resolve Timeline file (.drt) from the file system dialog, and click Open.

�Double click the .drt file in your file system.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

The timeline will appear in the Media Pool, along with all of the clips associated with it, including

any media sync information. Any timelines imported this way will have the word “import” appended

to their name, to avoid duplicate names. The imported timeline will be automatically conformed to

corresponding media that’s already in the Media Pool. However, if the timeline has been moved to

another computer, you may have to reimport or relink missing or offline media in to bring the imported

timeline fully online.

NOTE: Only a single timeline can be imported and exported at a time using this method.

To import or export multiple timelines, use the Import/Export Bin function described above.