---
title: "Using Loader and Saver Nodes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 235
---

# Using Loader and Saver Nodes

in the Fusion Page

The Loader and Saver nodes in Fusion Page are specifically used for workflows that center around

multi-channel EXR files. OpenEXR media can contain high-quality floating-point image data, multiple

matte channels, as well as auxiliary channels rendered from 3D software. The Loader node lets you

add OpenEXR files to a composition directly from the file system, retaining all the channels that are

embedded within that file. Saver nodes enable you to render either all or part of a composition as EXR

files directly to disk, bypassing the DaVinci Resolve Deliver page.

To import a multi-channel EXR image sequence into the Fusion page:


Open the Fusion page.


Open the Effects Library, and select the Tools > I/O category, and click the Loader node.


In the OS navigation window that opens, select the EXR image sequence you want to import, and

click Open.


A Loader node linked to the EXR file will appear in the Fusion page, although a clip will not appear

in the Media Pool.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Loader Node Parameters

The image tab of Loader nodes shares parameters with MediaIn nodes, as described previously in

this chapter. However, when using a Loader node for EXR files, the Format tab selectively enables and

disables the use of specific auxiliary channels contained in the file.

The Format tab in a Loader node Inspector

displays Aux channels in EXR files.

Outputting Images Using Saver Nodes

Saver nodes render OpenEXR image sequences to disk directly from the Fusion page. Saver nodes

can be added to any branch of a node tree, allowing you to export one or more subsets of nodes

in a composition. You can add as many Saver nodes as you like to whichever branches of your

composition’s node tree you need to output, to export multiple parts of a composition. For example,

if a particular composition is made up of one branch of nodes working together to create a complex

background, and another branch of nodes creating a foreground character with transparency,

you could export the background and foreground branches as separate OpenEXR files using two

Saver nodes.

To do this, simply create a Saver node after any set of nodes you want to output, and then open the

Inspector and click Browse to choose a name and location for the rendered result.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

When naming the file, you must add the .exr file extension. Fusion sets the output format accordingly.

A four-digit frame number is automatically added before the filename extension. However, you can

specify the frame padding by adding several zeroes to indicate the number of digits. For example,

000 signifies 001.

Once the Saver node is set up, output one or more Saver nodes, and choose Fusion > Render

All Savers.

The Inspector parameters for a Saver node.

Manual Disk Caching Using Loader and Saver Nodes

The Loader and Saver nodes in the Fusion page are also useful for optimizing extremely complex

and processor-intensive compositions. For example, you can render out specific branches of a

node tree that no longer require frequent adjustment to OpenEXR via a Saver node, then reimport

the result to take the place of the original branch of nodes in order to improve the performance of

your composition. Used this way, Loader and Saver nodes provide a bulletproof manual workflow

for caching using media files that will never be automatically purged unless you specifically delete

them. As long as you retain the original branch of nodes, you can always readjust and re-render these

manually cached parts of a composition, if necessary.

Preparing Compositions in Fusion Studio

The next few sections in this chapter cover preparing a project and adding clips into a composition

when using Fusion Studio. The term composition, or comp, is used to refer to the Fusion project

file. By default, opening the Fusion Studio application creates a new empty composition when it’s

launched. A composition can contain single frames, image sequences, or movie files at various

resolutions and bit depths. Knowing which files you can load in, how to set up a composition to handle

them, and finally, reading those files in are the first steps in beginning to composite.

Opening, Closing, and Saving Compositions

As soon as you open Fusion Studio, a new empty composition is created. If necessary, you can also

create or open multiple compositions at once. Each additional composition is opened as a tab to the

main Fusion Studio window.

Three compositions opened as tabs in Fusion Studio.

To create a second new composition:

�Choose File > New.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

To open an existing composition, do one of the following:

�Choose File > Open.

�Choose File > Open Recent, and choose from the list of recently opened comps.

�Drag a composition file from an OS file browser into the tabbed composition area at the top of the

Fusion Studio window.

�Double-click on a composition file in the OS file browser.

The following methods can be used to close the current composition:

�Choose File > Close from the menu at the top of the Fusion window.

�Click the Close X icon on the right of the composition’s tab.

If the composition has unsaved changes, a dialog box appears allowing you to save before closing.

TIP: Compositions that have unsaved changes will display an asterisk (*) next to the

composition’s name in the Fusion Studio title bar and in the composition’s tab.

To save the current composition, you can do the following:

�Choose File > Save and enter a name if the comp has yet to be named.

�Choose File > Save As to save under a new name.

�Choose File > Save Version to save the current composition with an added three-digit version

number at the end of the name. Each time you save a version, the number automatically

increments and the comp file is saved in the same location as the first version.

Auto Save

Auto save automatically saves the composition to a temporary file at preset intervals. Auto saves help

to protect you from loss of work due to power loss, software issues, or accidental closure.

To enable auto save for new compositions, choose Fusion Studio > Preferences, and then locate

Global > General > Auto Save in the Preferences dialog.

An auto-save file does not overwrite the current composition in the file system. A file with the same

name is created in the same folder as the composition but with the extension .autosave instead of

.comp. Unsaved compositions will place the autosave file in the default folder specified by the Comp:

path in the Paths panel of the Global Preferences.

If an auto-save file is present when Fusion Studio loads a composition, a dialog will appear asking to

load the auto-saved or original version of the composition.

The Composition File Format

Composition files are saved as readable plain text files. Using plain text files to describe a

composition makes it easier to integrate Fusion into structured, visual effects pipeline and asset

management solutions.

Composition files can be opened and edited using any standard text editing program. However,

it is never a good idea to open the file using a word processor, such as Microsoft Word or Apple

Pages, as these will generally save additional formatting information which will make the composition

unreadable to Fusion.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Importing and Exporting a Composition from DaVinci Resolve

Although the compositions created in DaVinci Resolve’s Fusion page are saved in the DaVinci Resolve

project library as .drp project files, you can import and export Fusion composition files when in the

Fusion page. This makes it very easy to share Fusion compositions between the different applications.

To export a Fusion composition from DaVinci Resolve:


From within DaVinci Resolve, switch to the Fusion page with the composition you want to export.


Choose File > Export Fusion Composition.


A Save dialog appears in which you can enter a name and location from the exported

Fusion composition.

A .comp extension is added to the end of the filename. Only the node tree created in the Fusion page

is exported. Clips not added to the Node Editor will not appear in the Fusion Studio bins. ResolveFX

added to the comp will also not translate from the Fusion page to Fusion Studio.

MediaIn nodes from DaVinci Resolve are automatically converted to Loader nodes, and if the file path

remains identical, the media is automatically relinked.

MediaOut nodes are converted to Saver nodes.

The return trip can also be performed, saving a composition file from Fusion Studio and importing it

into the Fusion page within DaVinci Resolve.

To import a composition from Fusion Studio into the Fusion page within DaVinci Resolve:


From within Fusion Studio, open the composition you want to move into the Fusion page.


From within DaVinci Resolve, switch to the Fusion page with an empty composition.

The composition you import will completely replace the existing composition in the Fusion page

Node Editor.


Choose File > Import Fusion Composition.


In the Open dialog, navigate to the Fusion comp and click Open.


The new comp is loaded into the Node Editor, replacing the previously existing composition.

TIP: To keep an existing comp in the Fusion page and merge a new comp from Fusion

Studio, open Fusion Studio, select all the nodes in the Node Editor, and press Command-C to

copy the selected nodes. Then, open DaVinci Resolve and switch the Fusion page with the

composition you want, click in an empty location in the Node Editor, and press Command-V

to paste the Fusion Studio nodes. Proceed to connect the pasted node tree into the existing

one using a Merge or Merge 3D node.

Setting Up a Composition

Source media can come in a variety of formats, including HD, UHD, and 4K or larger. Often you will

have different formats within a single comp. Each format has different properties, from resolution to

color depth and gamma curve. Fusion can mix and match material of different formats together in a

single composite, but it is important to note how Fusion Studio configures and combines materials of

different formats when loading and merging them together.

When you open Fusion Studio, an empty composition is created. The first thing you do when

starting on a new composition is to set the preferences to match the intended final output format.

The preferences are organized into separate groups: one for global preferences, and one for the

preferences of the currently opened composition.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION

Frame Format preferences for images generated in Fusion.

Although the final output resolution is determined in the Node Editor, the Frame Format

preferences are used to determine the default resolution used for new Creator tools (i.e., text,

background, fractals, etc.), aspect ratio, as well as the frame rate used for playback.

If the same frame format is used day after day, the global Frame Format preferences should match

the most commonly used footage. For example, on a project where the majority of the source

content will be 1080p high definition, it makes sense to set up the global preferences to match the

frame format of the HD source content you typically use.

To set up the default Frame Format for new compositions, do the following:


Choose Fusion Studio > Preferences.


Click the Global and Default Settings disclosure triangle in the sidebar to open the Globals group.


Select the Frame Format category to display its options.

When you set options in the Global Frame Format category, they determine the default frame format

for any new composition you create. They do not affect existing compositions or the composition

currently open. If you want to make changes to existing compositions, you must open the comp. You

can then select the Frame Format controls listed under the comp’s name in the sidebar.

For more information on preferences, see Chapter 75, “Preferences,” in the DaVinci Resolve

Reference Manual or Chapter 15 in the Fusion Reference Manual.


Fusion Fundamentals | Chapter 65 Getting Clips into Fusion

FUSION