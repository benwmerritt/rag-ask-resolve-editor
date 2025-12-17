---
title: "Creating Media Drop Zones in Templates"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 255
---

# Creating Media Drop Zones in Templates

For additional ease of use in the Edit page, Fusion effects, plugins, and transitions can have media

drop zones, allowing the user to simply drag clips from the Media Pool directly to the template. For

example, you can instantly replace the background of a Fusion effect with a star-field, just by dragging

that clip from the Media Pool to the media drop zone in the Inspector.

To create a media drop zone in a Fusion template:


Create a Macro of your current Fusion template.


For any MediaIn node that you want to make a media drop zone, make sure the ClipName

parameter is checked.


Place your template in the appropriate Fusion Edit template folder (Transition, Effect, etc.), and

relaunch DaVinci Resolve.

When you use this template in the Edit page, now you can drag clips from the Edit page Media

Pool and drop them in the Transition Inspector’s Clip Name field. They will then instantly update

the template with the chosen media.

The Clip Name parameters are checked

for MediaIn2 and MediaIn1 nodes in

the Macro Editor, allowing media drop

zones for both incoming and outgoing

sides of this Fusion transition.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

A clip from the Media Pool being dropped

on a Clip Name field in the resulting

Transition Inspector in the Edit page

Creating a Custom Template Icon

It is possible to create a custom icon that is embedded with your template thumbnail in the

Effects Library, instead of the default first three letters of the template name.

To create a simple Custom Template Icon:


Create a .png file of the icon you want to use for the template. The recommended size is

104 x 58 pixels, but any image will be resized to fit.


Name the file exactly the same name as your template, just with a .png extension rather than a

.setting extension.


Place the .png image in the same directory as your template.

When you restart DaVinci Resolve, the icon you created will be embedded in the template thumbnail

across all the Effects Libraries in the program.

A Custom Icon added to a fisheye template,

before (above) and after (below)

Using Fusion Template Bundles

For ease in distributing templates to other Fusion users, multiple templates can now be bundled

together into a single .drfx file. This file can then be imported back into another Fusion workstation

easily to ensure that all custom templates are the same between computers.

Creating a Fusion Template Bundle requires using a specific directory structure and using your

operating systems file browser and .zip compression utility. The directory structure is listed below, and

you can always find a specific folder from within Fusion by right-clicking on any bin in the Effect Library

and selecting Show Folder.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

Folder structure for Templates used in the Edit page:

•	 Edit

•	 Effects

•	 Generators

•	 Titles

•	 Transitions

Folder structure for Templates used in the Fusion page:

•	 Fusion

To create a Fusion Template Bundle:


In your OS, create a folder structure above that includes the specific folder for the type of

templates you want to be in the bundle. For example, if you have a transition and two effects

templates, you would create an Edit folder, and two subfolders inside it named Transitions

and Effects.


Copy your template (.setting) files into the appropriate directories. You can also include icon files

and any associated assets as well.


Use your OS zip compression utility to create a .zip file of the directory structure.


Rename the .zip file in your OS with the “.drfx” extension instead of .zip. The file icon should

change to reflect the new extension.

To import a Fusion Template Bundle:


Double-click on a .drfx file in your OS. DaVinci Resolve will launch and a dialogue box will appear

asking if you want to install the template bundle.


Drag to the .drfx file from your OS directly into the Fusion page in DaVinci Resolve. A dialogue box

will appear asking if you want to install the template bundle.

To delete a Fusion Template Bundle:


Navigate to the appropriate template directory in your file browser.


Delete the .drfx file.

IMPORTANT: The Fusion Template Bundle contains all the templates in one file. It does not

uncompress them into separate template files again. Therefore if you delete the .drfx file, all

associated templates inside that bundle will be removed as well.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

Chapter 69

Using Viewers

This chapter covers working with viewers in Fusion, including using onscreen

controls and toolbars, creating groups and subviews, managing viewer Lookup

Tables (LUTs), working with the 3D viewer, and setting up viewer preferences and

options.

Contents

Viewer Overview��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1391

Single vs. Dual Viewers�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1391

Floating Viewers in Fusion Studio���������������������������������������������������������������������������������������������������������������������������������������������� 1392

Video Output����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1392

Clean Feed��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1392

Loading Nodes into Viewers�������������������������������������������������������������������������������������������������������������������������������������������������������� 1392

Clearing Viewers��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1393

Position and Layout��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1393

The Viewer Divider���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1393

Zooming and Panning into Viewers����������������������������������������������������������������������������������������������������������������������������������������� 1394

Flipbook Previews������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1394

Creating Flipbook Previews����������������������������������������������������������������������������������������������������������������������������������������������������������� 1394

Playing Flipbook Previews������������������������������������������������������������������������������������������������������������������������������������������������������������� 1395

Removing Flipbook Previews�������������������������������������������������������������������������������������������������������������������������������������������������������� 1396

Flipbook Preview Render Settings��������������������������������������������������������������������������������������������������������������������������������������������� 1396

Onscreen Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1397

Showing and Hiding Onscreen Controls��������������������������������������������������������������������������������������������������������������������������������� 1398

Making Fine Adjustments to Onscreen Controls���������������������������������������������������������������������������������������������������������������� 1398

Toolbars��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1398

Viewer Toolbar������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1398

Node Toolbars�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1399

A/B Buffers�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1399

Flipping between Buffers���������������������������������������������������������������������������������������������������������������������������������������������������������������� 1399

Split Wipes between Buffers��������������������������������������������������������������������������������������������������������������������������������������������������������� 1400

Moving the Wipe Divider������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1401


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Subviews�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1401

Showing and Hiding Subviews����������������������������������������������������������������������������������������������������������������������������������������������������� 1402

Changing the Subview Type��������������������������������������������������������������������������������������������������������������������������������������������������������� 1402

Swapping the Subview with the Main View��������������������������������������������������������������������������������������������������������������������������� 1402

Viewer and Subview Types������������������������������������������������������������������������������������������������������������������������������������������������������������ 1403

Viewing Selective Channels��������������������������������������������������������������������������������������������������������������������������������������������������������� 1407

Viewing Color Channels������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1407

Viewing Auxiliary Channels����������������������������������������������������������������������������������������������������������������������������������������������������������� 1408

Viewing Multilayer Files (Studio Version Only)�������������������������������������������������������������������������������������������������������������������� 1408

The 3D Viewer�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1410

Panning, Scaling, and Rotating a 3D Viewer�������������������������������������������������������������������������������������������������������������������������� 1410

Viewing Objects via Wireframe���������������������������������������������������������������������������������������������������������������������������������������������������� 1410

Changing the POV of a 3D Viewer������������������������������������������������������������������������������������������������������������������������������������������������ 1411

Copying a Viewer’s POV to a Camera����������������������������������������������������������������������������������������������������������������������������������������� 1411

Lighting and Shadows in 3D Viewers����������������������������������������������������������������������������������������������������������������������������������������� 1412

Transparency in 3D Viewers����������������������������������������������������������������������������������������������������������������������������������������������������������� 1413

Grid�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1414

Vertex Normals�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1414

Quad View���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1415

Quad View Layouts����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1416

Using Quad Views for 2D Scenes����������������������������������������������������������������������������������������������������������������������������������������������� 1416

Guides������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1416

Frame Format Settings����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1417

Domain of Definition and Region of Interest������������������������������������������������������������������������������������������������������������������������ 1418

Domain of Definition (DoD)�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1418

Region of Interest (RoI)���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1419

Enabling RoI Controls������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 1419

Managing Viewer Lookup Tables (LUTs)��������������������������������������������������������������������������������������������������������������������������������� 1420

How Lookup Tables Work in Fusion�������������������������������������������������������������������������������������������������������������������������������������������� 1421

Types of Viewer LUTs������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1421

Using Viewer LUTs����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1423

Editing Viewer LUTs���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1424

LUT Processing Order���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1426

Applying Multiple LUTs�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1426

Saving Custom LUTs��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1427

LUT Files�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1428

Viewer Preferences and Settings���������������������������������������������������������������������������������������������������������������������������������������������� 1429

The Viewer Options Menu������������������������������������������������������������������������������������������������������������������������������������������������������������� 1429

Locking the Viewer (Command-L)���������������������������������������������������������������������������������������������������������������������������������������������� 1430

Additional Viewer Options������������������������������������������������������������������������������������������������������������������������������������������������������������ 1430

Status Bar Information����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1431


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION