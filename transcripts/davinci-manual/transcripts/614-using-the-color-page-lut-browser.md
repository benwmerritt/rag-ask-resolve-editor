---
title: "Using the Color Page LUT Browser"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 614
---

# Using the Color Page LUT Browser

The LUT Browser on the Color page provides a centralized area for browsing and previewing all of the

LUTs installed on your workstation. All LUTs appear in the sidebar, by category.

By default, all LUTs appear with a test thumbnail that give a preview of that LUT’s effect, but you can

also get a live preview of how the current clip looks with that LUT by hover scrubbing with the pointer

over a particular LUT’s thumbnail (this is described in more detail below).

The LUT Browser


Color | Chapter 150 Using LUTs

COLOR

To open the LUT Browser:

�Click the LUT Browser button in the UI Toolbar at the top of the Color page.

Methods of working with the LUT Browser:

�To see the LUTs in any category: Click on a LUT category to select it in the sidebar, and its

LUTs will appear in the browser area.

�To make a LUT a favorite: Hover the mouse over a LUT and click the star badge that appears at

the upper right-hand corner, or right-click any LUT and choose Add to Favorites. That LUT will then

appear when you select the Favorites category in the Node Editor contextual menu for nodes.

�To search or filter for specific LUTs: Open a bin that has the LUT you’re looking for, then click

the magnifying glass icon to open the search field, and type text that will identify the LUTs

you’re looking for.

�To see LUTs in Column or Thumbnail view: Click the Column or Thumbnail buttons at the top right

of the LUT Browser to choose how to view LUTs in the browser area.

�To sort LUTs in Thumbnail view: Click the Thumbnail Sort pop-up menu and choose which criteria

you want to sort LUTs by. The options are filename, type, relative path, file path, usage, date

modified. There are also options for ascending and descending sort modes.

�To sort LUTs in Column view: Click the column header to sort by that column. Click a header

repeatedly to toggle between ascending and descending modes.

�To update the thumbnail of a LUT with an image from a clip: Choose a clip and frame that you

want to use as the new thumbnail for a particular LUT, then right-click that LUT and choose Update

Thumbnail With Timeline Frame.

�To reset the thumbnail of a LUT to use the standard thumbnail: Right-click a LUT and choose

Reset Thumbnail to go back to using the standard test image.

�To refresh a LUT category with new LUTs that may have been installed: Select a LUT category,

then right-click anywhere within the browser area and choose Refresh to refresh the contents of

that category from disk.

Enabling and Disabling the LUT Viewer live preview:


Open the LUT Viewer’s option menu and choose Live Preview.

The Live Preview option for the LUT browser lets you

hover over a LUT to preview it on the current clip in the Viewer


Click a node in the Node Editor you want to preview applying a LUT to. The live preview will

display how the current clip will appear with the LUT you select applied to the currently selected

node of the current grade, which will affect the result.


Move the pointer over the LUT you want to preview.

The Viewer image updates to show how that clip would look with that LUT applied to the currently

selected node.


Color | Chapter 150 Using LUTs

COLOR

To apply a LUT from the LUT Browser to a specific node, do one of the following:

�Right-click a LUT and choose Apply LUT to current node.

�Drag a LUT from the LUT Browser and drop it onto the node you want to apply a LUT to. If

you drag a LUT onto a node that already has a LUT, the previous LUT will be overwritten by

the new one.

Applying a LUT Within a Node

DaVinci Resolve lets you apply LUTs within a grade by connecting a LUT to a particular node in the

Node Editor. This gives you the greatest amount of control over where the LUT is applied in your

image processing pipeline, and it also gives you the opportunity to apply image adjustments prior to

the LUT, and after the LUT, as you require.

To apply a LUT within a node, do one of the following:

�Right-click any node, and choose a LUT from the 1D Input LUT, 1D Output LUT, 3D LUT, DCTL, or

CLF (common LUT format) submenus of the LUT submenu. The LUT submenus list whichever LUTs

have been installed on your workstation.

For more information on installing LUTs, see Chapter 4, “System and User Preferences.”

�Right-click any node, and choose a LUT from the LUT > Favorites submenu.

�Use the LUT Browser to find a LUT you want to use, and then drag and drop that LUT onto the

node you want to apply it to

TIP: If you hold down the Option key while scrolling through the submenu of LUTs in a

Corrector node’s contextual menu, you’ll get a live update in the Viewer of how each LUT

affects the image.

To reveal a selected node’s LUT:

For any node in the Node Editor with a LUT applied to it, you can right-click that node and choose

Reveal Selected LUT to automatically open the LUT viewer and select that LUT.

LUTs Are the Last Operation Within a Node

Each node in the Node Editor is capable of performing multiple operations, and these operations

occur in a specific order. LUTs that you add to a node impose their transformation as the last operation

within that node, after all other Color page adjustments applied by that node.

Practically, this means that you can use a node’s Color and Contrast controls to trim the image data

that will be fed into a LUT applied to that same node. For example, if a LUT’s contrast adjustment clips

the highlights of the image too much, you can use that node’s Contrast controls to lower the highlights

of the image prior to the LUT, restoring detail to the image.


Color | Chapter 150 Using LUTs

COLOR

Favorite LUTs Submenu in Node Editor

When you “star” a LUT as a favorite in the LUT Browser, those favorite LUTs appear in a submenu of

the contextual menu that appears when you right-click on a node in the Node Editor. This makes it

easy to create a short list of your go-to LUTs for various situations, for rapid application right in the

Node Editor.

A Favorite LUTs submenu in the Node Editor contextual menu gives you a short list

Missing LUTs

Clips with missing LUTs show an overlay at the bottom right of the screen indicating the name of the

LUT if a single LUT is missing, or an indicator that multiple LUTs are missing. This allows for quick

previews of missing LUTs without interruption. Multiple missing LUTs can be seen and managed from

the Missing LUTs tab in the LUT Browser, which only appears if you have one or more LUTs missing.

Exporting LUTs

If you find it necessary to exchange image adjustments with other grading applications, compositing

applications, or NLEs, often the easiest inter-application solution is to export a LUT. This can be done

whether your grade consists of one node or several nodes, so long as they contain only Primaries

palette adjustments, Custom Curves palette adjustments, and compatible ResolveFX plugins that

include Color Space Transform, ACES Transform, and Gamut Mapping. All nodes with compatible

functions will be mathematically combined and translated into a LUT.

Keep in mind that any nodes that use Qualifiers, Windows, incompatible filtering operations (such as

sharpening or blurring), or incompatible Resolve FX or Open FX will be completely ignored, as will all

other correction operations made within these nodes.

To export a LUT:


Right-click a clip thumbnail in the Timeline of the Color page, and choose an option from the

Generate LUT submenu:

�Generate 3D LUT (17 Point Cube): A DaVinci-developed LUT format

�Generate 3D LUT (33 Point Cube): A DaVinci-developed LUT format

�Generate 3D LUT (65 Point Cube): A DaVinci-developed LUT format

�Generate 3D LUT (Panasonic VLUT): A LUT format associated with Panasonic VariCam cameras


Color | Chapter 150 Using LUTs

COLOR


Choose a location for the resulting LUT file in the file dialog. The default file path depends on your

operating system; saving it here will make it available to DaVinci Resolve for future use.

On OS X: Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/

On Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT

On Linux: /home/resolve/LUT

If you like, you can create a new folder in which to save your custom LUTs.


Enter a name into the Save As field, and click Save. A LUT file is saved.

Once created, you can use an exported LUT from within DaVinci Resolve, applying it to a clip or

node directly, or applying it to the entire project using the settings found in the Color Management

panel of the Project Settings. You can also copy the LUT to a memory stick to give to someone for

monitoring or previewing in an onset workflow, or to someone using another grading application

that can read this LUT format.


Color | Chapter 150 Using LUTs

COLOR

COLOR