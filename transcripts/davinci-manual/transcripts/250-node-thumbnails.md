---
title: "Node Thumbnails"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 250
---

# Node Thumbnails

Once a source or an effect has been added to the Node Editor, it’s represented by a node. By default,

nodes are rectangular and thin, making it easier to fit reasonably complicated grades within a relatively

small area. However, if you like, you can also display node thumbnails.

A node in the Node Editor shown without and with a thumbnail.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Nodes can be displayed as a small rectangle or as a larger square. The rectangular form displays the

node’s name in the center, while the square form shows either the tool’s icon or a thumbnail of the

image it is outputting.

TIP: Even if you’re not displaying node thumbnails, you can quickly obtain detailed

information about a node and the data it’s processing by hovering your pointer over it in the

Node Editor and viewing the tooltip bar below.

Choosing Which Nodes Show Thumbnails

If you want to use node thumbnails to help visually identify media and operations in your node trees,

there are a variety options for which nodes should display thumbnails in the contextual menu that

appears when you right-click anywhere in the background of the Node Editor.

Force All Tile Pictures

This option shows thumbnails for every single node in the Node Editor. This can make simple node

trees easier to read, but it’ll make all node trees take up considerably more room.

NOTE: If Show Thumbnails is enabled, nodes may not update until the playhead is moved in

the Time Ruler.

Force Active Tile Pictures

You may also choose to only show thumbnails for nodes that are currently selected, which can make it

easier to see which node you’re working on. When nodes become deselected, the thumbnails will be

hidden again.

Force Source Tile Pictures

This enables thumbnails for all MediaIn and Loader nodes in the Node Editor, as well as all generators,

and is a great way to be able to quickly see where all the clips are in a composition.

Force Mask Tile Pictures

This enables thumbnails for all Mask nodes in a composition, which can make them easier to

distinguish when you’re building complex shapes made from multiple Mask nodes.

Manually Showing Tile Pictures and Node Options

You also have the option of manually choosing which nodes you’d like to show thumbnails.

For example, there may be certain key points of the node tree where you’d like to see a small visual

representation of what’s happening in the composition.

To toggle thumbnails for one or more specific nodes:


Select one or more nodes in the Node Editor.


Right-click one of the selected nodes, and choose one of the following from the contextual menu:

�Show > Show Tile Pictures

�Show > Show Modes/Options


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

When you’ve manually enabled thumbnails for different nodes, they’ll remain visible whether or not

those nodes are selected.

Switching Thumbnails between Images and Icons

Whenever you enable node thumbnails, you have the choice of having these thumbnails either display

an image of the state of the image at that node, or you can instead choose to display the icon for that

particular node. The setting for this affects all nodes at once.

To display icons instead of thumbnails:

Right-click anywhere in the background of the Node Editor and deselect Show Thumbnails in the

contextual menu.

Sometimes Nodes Only Show Icons

As you add more and more nodes to a composition, you’ll notice that some nodes never

display an image in their thumbnail. In these cases, the default icon for that node is displayed

instead of an image.

Most nodes in the Particle and 3D categories fall into this group. The exceptions are the

pRender node and the Render 3D node. These two nodes are capable of displaying a

rendered thumbnail if you have the menu options set for Thumbnails to be displayed.

In other cases, whether nodes display images in their thumbnail is more situational. Some

Transform nodes are able to concatenate their results with one another, passing the actual

processing downstream to another node later in the node tree. In this case, upstream

Transform nodes don’t actually process the image, so they don’t produce a thumbnail.

In other situations where the Loader is not reading in a clip or the clip is trimmed in the

Keyframes Editor to be out of range, it can cause the node not to process the image, so it will

not produce a rendered Thumbnail image. Also, nodes that have been set to Pass Through

mode are disabled and do not display a rendered Thumbnail image.

Finding Nodes

Modern visual effects require detailed work that often results in compositions with hundreds of nodes.

For such large node trees, finding things visually would have you panning around the Node Editor for a

long, long time. Happily, you can quickly locate nodes in the Node Editor using the Find dialog.

The Find dialog lets you quickly locate nodes wherever they are in the Node Editor.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Performing Simple Searches

To do simple searches using node names is easy.

To search for a node in the Node Editor:


Press Command-F, or right-click in an empty area of the Node Editor and choose Find from the

contextual menu.


When the Find dialog appears, do the following:

�Enter a search term in the Find field.

�Choose search options, such as whether to match the whole phrase in the Find field, whether to

match the case, whether to use a sequence number, or whether to use a regular expression in

the Find field.

�Choose what to search. Options include tool name, tool type name, or tool type ID.


To perform the find, do one of the following:

�Click Find Next to try to select a downstream node matching the criteria.

�Click Find Previous to try to select an upstream node matching the criteria.

�Click Find All to try to select all nodes in the Node Editor that match the criteria.

The Find window closes. If either the Find Next, Find Previous, or Find All operations are

successful, the found node or nodes are selected. If not, a dialog appears letting you know that

the string could not be found.

TIP: Finding all the nodes of a particular type can be very useful if you want, for example, to

disable all Resize nodes. Find All will select all the nodes based on the search term, and you

can temporarily disable them by pressing the shortcut for Bypass, Command-P.

Using Regular Expressions

If you need to do more complicated searches, you can turn on the Regular Expression checkbox,

which lets you enter some simple expressions with which to create more complex find operations.

Some useful examples of regular expressions that are valuable include the use of Character Sets.

Character Sets

Any characters typed between two brackets [ ] will be searched for. Here are some examples of

character set searches that work in Fusion.

[a-z]

Finds: Every node using a lower caps letter

[a-d]

Finds: Every lower caps letter from a to d,

and will find nodes with a, b, c, or d

[Tt]

Finds: Every node with an upper case T

or a lower case t

[aeiou]

Finds: Every vowel

[0-9]

Finds: Every numeral

[5-7]

Finds: Every numeral from five to seven, and

will find nodes numbered with 5, 6, or 7


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION

Custom Node Settings

When a node is added to the Node Editor, its parameters are set to the default values for that type

of node. If you find yourself constantly readjusting the parameters of a node to a preferred starting

point as soon as it’s added to the node tree, you can override the default node settings with your own

custom settings.

To save new default settings for a particular type of node:


Create a new node.


Open the Inspector and customize that node’s settings to the new defaults you want it to have.


Right-click that node in the Node Editor, or right-click that node’s control header in the Inspector,

and choose Settings > Save Default from the contextual menu.

TIP: You can also save six different settings for a node in the Node Editor using the Version

buttons at the top of the Inspector. For more information, see Chapter 70, “Editing Parameters

in the Inspector,” in the DaVinci Resolve Reference Manual or Chapter 8 in the Fusion

Reference Manual.

Managing Saved Settings

Custom node default settings are saved to a folder on your hard drive that’s based on the Path Map

> Defaults preference in the Fusion Settings. This path is customizable for facilities where multiple

compositing artists use a common set of facility defaults, stored somewhere commonly accessible.

The default paths are:

For macOS systems, this path defaults to: /UserName/Library/Application Support/

Blackmagic Design/DaVinci Resolve/Fusion/Defaults.

For Windows systems, this path defaults to C: \Users\<username>\AppData\Roaming\

Blackmagic Design\DaVinci Resolve\Fusion\Defaults.

For Linux systems, this path defaults to: ~/.fusion/BlackmagicDesign/DaVinci Resolve/

Fusion/Defaults.

If you browse this directory, the settings for each node are saved using a name taking the form

INTERNALNAME_PUBLICNAME.settings, where INTERNALNAME is the internal name of the Fusion

tool, and PUBLICNAME is the name of the Node that’s derived from the internal Fusion tool. For

example, the default setting for a Blur node would be called Blur_Blur.setting. This naming convention

is partly to ensure that third-party plugin nodes don’t overwrite the defaults for built-in Fusion nodes

that happen to have the same name.


Fusion Fundamentals | Chapter 67 Working in the Node Editor

FUSION