---
title: "Deleting Groups"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 252
---

# Deleting Groups

Deleting a group is no different from deleting any other node in the Node Editor. Select a group and

press Delete, Backspace, or Forward-Delete, and the group along with all nodes contained within it

are removed from the node tree.

Expanding and Collapsing Groups

A collapsed group is represented by a single “stack” node in the node tree. If you want to modify any

of the nodes inside the group, you can open the group by double-clicking it or by selecting the group

node and pressing Command-E.

An open group window showing

the minimize button.

When you open a group, a floating window shows the nodes within that group. This floating window is

its own Node Editor that can be resized, zoomed, and panned independently of the main Node Editor.

Within the group window, you can select and adjust any node you want to, and even add, insert, and

delete nodes while it is open. When you’re ready to collapse the group again, click the minimize button

at the top left corner of the floating window, or use the keyboard shortcut (Cmd-E).

Panning and Scaling within Open Group Windows

You can pan and scale an open group window using the same mouse buttons you use to pan and

scale the main Node Editor. However, when you’re working in an expanded group and simultaneously

making changes to the main node tree, you may want to prevent the expanded group from being

individually panned or scaled. Turning off the Position button at the right of the group title bar locks

the group nodes to the size of the nodes in the rest of the overall node tree. Turning on this Position

button lets you size group nodes independently of the rest of the node tree.

Ungrouping Nodes

If you decide you no longer need a particular group, or you simply find it easier to have constant

access to all the nodes in the group at once, you can decompose or “ungroup” the group without

deleting the nodes within it to eliminate the group but keep the contents in the Node Editor.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

To ungroup nodes, do the following:


Right-click on the group.


Choose Ungroup from the contextual menu. The nodes inside the group are placed back in the

main node tree.

Saving and Reusing Groups

One of the best features of groups is that every group and its settings can be saved for later use in

other shots or projects. Groups and their settings can be recalled in various ways.

A good example of when you might want to Save and Load a group is in a studio with two or more

compositing artists. A lead artist in your studio can set up the master comp and create a group

specifically for keying greenscreen. That key group can then be passed to another artist who refines

the key, builds the mattes, and cleans up the clips. The setting can then be saved out and loaded

back into the master comp. As versions are improved, these settings can be reloaded, updating the

master comp.

Methods of saving and reusing groups:

�To save a group: Right-click a group and choose Settings > Save As from the contextual menu.

�To reuse a group: Drag it from your computer’s file browser directly into the Node Editor.

This creates a new group node in the node tree with all the same nodes as the group you saved.

�To load the settings from a saved group to another group with the same nodes: Right-click a

group in the Node Editor and choose Settings > Load from the contextual menu.

In Fusion Studio, you can also save and reuse groups from the Bins window:

�To save a group: Drag the group from the Node Editor into the opened Bin window. A dialog

will appear to name the group setting file and the location where it should be saved on disk.

The .setting file will be saved in the specified location and placed in the bins for easy access

in the future.

Macros

Some effects aren’t built with one tool, but with an entire series of operations, sometimes in complex

branches with interconnected parameter controls. Fusion provides many individual effects nodes

for you to work with but gives users the ability to repackage them in different combinations as

self‑contained “bundles” that are either macros or groups. These “bundles” have several advantages:

�They reduce visual clutter in your node tree.

�They ensure proper user interaction by allowing you to restrict which controls from each node of

the macro are available to the user.

�They improve productivity by allowing artists to quickly leverage solutions to common compositing

challenges and creative adjustments that have already been built and saved.

Macros and groups are functionally similar, but they differ slightly in how they’re created and presented

to the user. Groups can be thought of as a quick way of organizing a composition by reducing the

visual complexity of a node tree. Macros, on the other hand, take longer to create because of how

customizable they are, but they’re easier to reuse in other comps.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

Creating Macros

While macros let you save complex functions for future use in very customized ways, they’re actually

pretty easy to create.

To make a macro from nodes in the Node Editor:


Select the nodes you want to include in the macro you’re creating. Because the macro you’re

creating will be for a specific purpose, the nodes you select should be connected together to

produce a particular output from a specific set of inputs.

TIP: If you want to control the order in which each node’s controls will appear in the

macro you’re creating, Command-click each node in the order in which you want it to

appear.


Right-click one of the selected nodes and choose Macro > Create Macro from the

contextual menu.

A Macro Editor window appears, showing each node you selected as a list, in the order in which

each node was selected.

The macro editor with a Blur node and Color Corrector node.


First, enter a name for the macro in the field at the top of the Macro Editor. This name should

be short but descriptive of the macro’s purpose. No spaces are allowed, and you should

avoid special characters.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION


Next, open the disclosure control to the left of each node that has controls you want to expose

to the user and click the checkbox to the right of each node output, node input, and node control

that you want to expose.

The controls you check will be exposed to users in the order in which they appear in this list, so

you can see how controlling the order in which you select nodes in Step 1, before you start editing

your macro, is useful. Additionally, the inputs and outputs that were connected in your node tree

are already checked, so if you like these becoming the inputs and outputs of the macro you’re

creating, that part is done for you.

For each control’s checkbox that you turn on, a series of fields to the left of that control’s row lets

you edit the default value of that control as well as the minimum and maximum values that control

will initially allow.


When you’re finished choosing controls, click Close.


A dialog prompts you to save the macro. Click Yes.


A Save Macro As dialog appears in which you can re-edit the Macro Name (if necessary), and

choose a location for your macro.

To have a macro appear in the Fusion page Effects Library Tools > Macros category, save it in the

following locations:

�On macOS: Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/

DaVinci Resolve/Fusion/Macros/

�On Windows: C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\

Support\Fusion\Macros

�On Linux: home/username/.local/share/DaVinciResolve/Fusion/Macros

To have a macro appear in the Fusion Studio Effects Library Tools > Macros category, save it in the

following locations:

�On macOS: Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/

Fusion/Macros/

�On Windows: C:\Users\username\AppData\Roaming\Blackmagic Design\Fusion\Macros

�On Linux: home/username/.fusion/BlackmagicDesign/Fusion/Macros


When you’re done, click Save.

Using Macros

Macros can be added to a node tree using the Add Tool > Macros or Replace Tool > Macros submenus

of the Node Editor contextual menu.

Re-Editing Macros

To re-edit an existing macro, just right-click anywhere within the Node Editor and choose the macro

you want to edit from the Macro submenu of the same contextual menu. The Macro Editor appears,

and you can make your changes and save the result.

Groups Can Be Accessed Like Macros

Groups can also be loaded from the Insert Tool > Macros submenu if you save a group’s

setting file to the Macros folder in your file system. For example, on macOS, the Macintosh

HD/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Macros/ directory.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

Other Macro Examples

A macro can also be used as a custom LUT. Just copy the macro’s .setting file to the LUTs: folder, and

the macro will be selectable in the viewers as a LUT. These LUT macros can be used for more than just

a color adjustment; you could make a macro that does YUV 4:2:2 resampling, a resize, a sharpening

filter, or just watermarking.

Creating Fusion Templates

The integration of Fusion into DaVinci Resolve has enabled the ability to create Fusion Titles,

Transitions, Effects, and Generators templates for use in the Edit page. You can create these templates

in the Fusion page or within Fusion Studio and then copy them into DaVinci Resolve. Fusion Titles,

Generators, and Transition templates are essentially comps created in Fusion but editable in the

Timeline of the Edit page with custom controls. This section shows you how it’s done.

Getting Started with a Fusion Title Template

The first part of creating a Fusion title template is to create a Fusion composition consisting of Fusion-

generated objects assembled to create nearly any kind of title or generator you can imagine. If you’re

really ambitious, it can include animation. In this example, 3D titles and 2D titles have been combined

into a show opener.

Building a composition to turn into a title template.

Saving a Title Macro

Macros are basically Fusion compositions that have been turned into self-contained nodes. Ordinarily,

these nodes are used as building blocks inside of Fusion so that you can turn frequently-made

compositing tricks that you use all the time into your own nodes. However, you can also use this macro

functionality to build title templates for the Edit page.

Having built your composition, select every single node you want to include in that template except for

the MediaIn and MediaOut nodes in DaVinci Resolve or Loader and Saver nodes in Fusion Studio.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

Selecting the nodes you want to turn into a title template.

TIP: If you want to control the order in which node controls will be displayed later on, you

can Command-click each node you want to include in the macro, one by one, in the order in

which you want controls from those nodes to appear. This is an extra step, but it keeps things

better organized later on.

Having made this selection, right-click one of the selected nodes and choose Macro > Create

Macro from the contextual menu.

Creating a macro from the selected nodes.

The Macro Editor window appears, filled to the brim with a hierarchical list of every parameter in

the composition you’ve just selected.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

The Macro Editor populated with the parameters of all the nodes you selected.

This list may look intimidating, but closing the disclosure control of the top Text1 node shows us

what’s really going on.

A simple list of all the nodes we’ve selected.

Closing the top node’s parameters reveals a simple list of all the nodes we’ve selected. The Macro

Editor is designed to let you choose which parameters you want to expose as custom editable

controls for that macro. Whichever controls you choose will appear in the Inspector whenever you

select that macro, or the node or clip that macro will become.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

So all we have to do now is to turn on the checkboxes of all the parameters we’d like to be able

to customize. For this example, we’ll check the Text3D node’s Styled Text checkbox, the Cloth

node’s Diffuse Color, Green, and Blue checkboxes, and the SpotLight node’s Z Rotation checkbox,

so that only the middle word of the template is editable, but we can also change its color and tilt its

lighting (making a “swing-on” effect possible).

Selecting the checkboxes of parameters we’d like to edit when using this as a template.

Once we’ve turned on all the parameters we’d like to use in the eventual template, we click the

Close button, and a Save Macro As dialog appears.

To have the Title template appear in the Effects Library > Titles category of DaVinci Resolve, save

the macro in the following locations:

On macOS: Macintosh HD/Users/username/Library/Application Support/Blackmagic

Design/DaVinci Resolve/Fusion/Templates/Edit/Titles

On Windows: C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\

Support\Fusion\Templates\Edit\Titles

On Linux: home/username/.local/share/DaVinciResolve/Fusion/Templates/Edit/Titles

Choosing where to save a title template for the Edit page in DaVinci Resolve.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION