---
title: "Collapse Group Grades"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 594
---

# Collapse Group Grades

If you want to take a clip out of a group, but you want its grade to continue incorporating all

adjustments made in the Pre-Group and Post-Group Node Editor modes, you can use the Collapse

Group Grades command to copy all nodes in the Pre-Group and Post-Group grades to the Clip grade.

When you do this, Pre-Group nodes are added before any pre-existing nodes in the Clip grade, and all

Post-Group nodes are added after, in order to maintain the correct order of operations.

(Top) The Clip node tree, (Bottom) After using the Collapse Group Grades command

to flatten the Pre-Group and Post-Group nodes into the Clip node tree


Color | Chapter 142 Grade Management

COLOR

To flatten all group grades into a single Clip mode node tree:

Right-click a clip’s thumbnail in the Thumbnail timeline, and choose Collapse Group Grades

from the contextual menu.

Using Collapse Group Grades on a clip always removes that clip from whatever group it was

previously a member of. This can also be an easy way of creating a single flat node tree in

preparation for saving a grade to the Gallery for applying to other clips that aren’t themselves

in groups.

Groups and Versions

Local or Remote versions you create relate only to the Clip grade. Group Pre-Clip and Group Post-Clip

grades cannot be versioned.

Exporting Grades and LUTs

If you find it necessary to exchange grades with other workstations, there are two ways you can do so

directly: by exporting grades, or LUTs. This section discusses the export of Grades.

For more information about exporting LUTs, see Chapter 150, “Using LUTs.”

To export a grade:


Save the grade you want to export as a still in the Gallery.


Right-click the saved still in the Gallery, and choose Export.


Select the image format you want to save the still as. Choices include: DPX, Cineon, TIFF, JPEG,

PNG, PPM, BMP, and XPM.


Choose a location for the resulting still image and saved grade files, type a name into the

Save As field, and click Save.

Two files are saved. The image file contains the still image of the frame that was stored. A DRX

(DaVinci Resolve eXchange) file contains all the grading information.

To Import a grade:


Right-click anywhere in the gray area of the Gallery, and choose Import.


Click the Options button to select the specific file type you want to import, or select “All Files”

for multiple formats.


Choose the image file that was exported from your DaVinci Resolve workstation, or someone

else’s. The accompanying DRX file must be in the same location. If you lose the original image file,

you can still import the DRX file by itself. It will preserve the node structure of the still, but you will

not be able to wipe against it.

The still you imported appears in the Gallery, containing the grading information you wanted

to import.


Color | Chapter 142 Grade Management

COLOR

Chapter 143

Node Editing Basics

This chapter covers the basics of using the Node Editor in DaVinci Resolve

to manage all of the adjustments you decide to apply to a clip, as well as the

fundamental procedures for editing and organizing nodes within a tree that are the

basis for creating more sophisticated effects.

Contents

Node Editor Basics��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3309

Thumbnail-Optional Nodes���������������������������������������������������������������������������������������������������������������������������������������������������������� 3309

The Node Editor Interface�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3310

The Components of a Node Tree������������������������������������������������������������������������������������������������������������������������������������������������ 3311

Node Badges and Labels��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3313

Selecting Nodes���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3314

Disabling Nodes���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3315

Turning Grades and/or Fusion Effects Off���������������������������������������������������������������������������������������������������������������������������� 3316

Resetting Nodes��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3316

Previewing and Restoring Node Trees������������������������������������������������������������������������������������������������������������������������������������� 3317

Caching Specific Nodes to Improve Performance������������������������������������������������������������������������������������������������������������� 3317

Editing Node Trees����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3317

Adding Nodes���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3317

Adding Nodes with Windows Turned On�������������������������������������������������������������������������������������������������������������������������������� 3318

Deleting Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3318

Connecting and Disconnecting Nodes������������������������������������������������������������������������������������������������������������������������������������ 3319

Extracting a Node������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3319

Inserting a Node���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3319

Rearranging Node Order��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3320

Copying and Pasting All Settings From One Node to Another����������������������������������������������������������������������������������� 3320

Node Context Menu Actions Can Have Assigned Shortcut Keys����������������������������������������������������������������������������� 3320

Keeping Node Trees Organized������������������������������������������������������������������������������������������������������������������������������������������������� 3321

Track Node Changes Using Color�������������������������������������������������������������������������������������������������������������������������������������������� 3322

Using Node Stack Layers�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3323

Copying Node Stack Layers��������������������������������������������������������������������������������������������������������������������������������������������������������� 3324

Post Group Node Stack Layer����������������������������������������������������������������������������������������������������������������������������������������������������� 3324


Color | Chapter 143 Node Editing Basics

COLOR

Node Editor Basics

By default, every clip has one node in the Node Editor that contains the first corrections you make.

However, you also have the option of creating multiple nodes, where each node contains one or more

corrections that affect the image.

The Node Editor showing a reasonably full-featured grade

The specific arrangement of nodes you create lets you exert precise control over the order of

operations performed by your grade, which provides many advantages. This section covers different

ways of creating, editing, and arranging node trees to harness the full power of DaVinci Resolve.

Thumbnail-Optional Nodes

The Node Editor option menu provides a Show Thumbnails option that lets you disable or enable the

thumbnails attached to each Corrector node.

Using Compound Nodes��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3324

Adding Inputs and Outputs to Compound Nodes������������������������������������������������������������������������������������������������������������� 3326

Nesting Compound Nodes����������������������������������������������������������������������������������������������������������������������������������������������������������� 3326

Grading Compound Nodes����������������������������������������������������������������������������������������������������������������������������������������������������������� 3326

Identifying Nodes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3326

Putting Nodes into HDR Mode���������������������������������������������������������������������������������������������������������������������������������������������������� 3327

Clip vs. Timeline Grading��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3327


Color | Chapter 143 Node Editing Basics

COLOR

Disabling thumbnails in the Node Editor option menu makes nodes shorter

How Many Nodes Do I Need to Use?

In this chapter and the ones that follow, you’ll learn many different techniques for combining

adjustments and nodes in different ways to achieve highly specific effects. Consequently, new

DaVinci Resolve users often wonder, how far do I go? There is no right answer, but suffice it

to say that some of the world’s leading colorists achieve stunning results in as few as three

or four nodes, while others routinely build carefully organized hierarchies of ten to twenty

nodes, or more. The number of nodes you use is often dependent on the quality of media

you’ve been given to work with, as well-lit footage usually requires less work than material

shot run-and-gun with available light, that typically needs many more adjustments to achieve

an acceptable result. Furthermore, the number of nodes you may use can also depend

on what kind of program you’re working on, with commercial spots affording the colorist

enough time in the schedule to build truly massive grades that adjust every little detail, and

narrative features and television shows requiring you to work faster and do more within fewer

adjustments in order to stay on track. The real answer? Each grade requires as many nodes as

are necessary. No more, no less.

The Node Editor Interface

As you work within the Node Editor, you may find the need to zoom into or out of it to get a better look

at the node tree, and to pan around the working area to deal with large collections of nodes.

To expand the size of the Node Editor’s working area:

�Drag the border between the Node Editor and the Viewer to the left or right to make it

wider or narrower.

�Right-click anywhere within the Node Editor (except on a node) and choose Toggle Display

Mode, which hides the Viewer and moves the Node Editor to the right of the Gallery, enlarging it

considerably. Right-click and choose Toggle Display Node again to return to the default layout.

To arrange the node tree to fit your current working area:

�Right-click anywhere in the Node Editor (except on a node) and chose Cleanup Node Graph from

the contextual menu. This will rearrange your node tree to fit in whatever size working area you

have at the time.


Color | Chapter 143 Node Editing Basics

COLOR

To zoom and pan within the Node Editor, do one of the following:

�Use the Node Editor’s zoom slider to shrink or enlarge the nodes in the Node Editor.

�Click the Pan tool (the hand icon) at the upper left-hand corner of the Node Editor, and drag

anywhere within the gray area of the Node Editor to pan around.

�Press the H key to toggle between selection and pan modes in the Node Editor.

�Middle-click and drag anywhere within the Node Editor to pan around.

�Right-click and choose Zoom In or Zoom Out.

�Right-click and choose Zoom to Window to fit the node tree to the current size of the node graph.

�Right-click and choose Original Size to return the node graph to the default size.

The Node Editor’s

Pan (Hand) tool