---
title: "Working with Node Groups"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 240
---

# Working with Node Groups

Render nodes can be configured into Groups, which are then used when submitting compositions.

For example, imagine you have five Render nodes. All the Render nodes are members of the group

named All. Two of the Render nodes include more memory and faster processors, so you create a new

group called Hi-Performance.

New Render nodes are automatically added to All, but you can assign them to other groups as well.

To assign a Render node to a Group:


Open the Render Manager and select the Render nodes to assign to a group.


Choose Render Node > Assign Group or right-click over the Render nodes and choose Assign

Group from the drop-down menu.


In the Choose Group dialog, enter a name for the group.


To assign Render nodes to multiple groups, separate the name of each group using a comma

(e.g., All, Local, or Hi-Performance). The order of the groups determines the priority. See “Using

Multiple Groups” below.

When a render is submitted to the network, it is automatically sent to the All group. However, you can

choose to submit it to other groups in the list.

To submit a comp to a group from the Render Manager:


Open the Render Manager.


Submit the comp.


Click the Pause Render button.


Right-click over the comp in the queue list and select Assign Group.


In the Assign Group dialog, select an existing group to render the comp and click OK.


Click the Resume Render button.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

To submit a comp to a group from the Render Settings dialog:


Click the Render button in the transport controls area.


In the Render Settings dialog, enable the Use Network checkbox.


Select an existing group from the Available groups list.


Click the Start Render button.

Continuing with the group example above, five Render nodes are contained in the All group, and

two of those Render nodes are also in the Hi-Performance group. If you submit a render to the Hi-

Performance group, only two of the computers on the network are used for rendering. If a composition

is then submitted to the All group, the remaining three machines will start rendering the new

composition. Once the two Render nodes in the Hi_Performance group complete the first job, they

join the render in progress on the All group.

Groups are optional and do not have to be used. However, groups can make managing large networks

of Render nodes easier and more efficient.

Using Multiple Node Groups

A single Render node can be a member of multiple groups. A single composition can also be

submitted to multiple groups. Submitting a composition to multiple groups results in it rendering on all

Render nodes in the selected groups.

When a Render node is a member of multiple groups, the order of the groups is important because the

order defines the priority for that Render node.

For example, if groups are assigned to a Render node as All, Hi-Performance, then renders submitted

to the All group take priority. Any renders in progress that were submitted to the Hi-Performance

group will be overridden. If the order is changed to Hi-Performance, All, then the priority is reversed.

Viewing the Render Log

The Render Log is displayed in the lower half of the Render Manager window, although it can also be

displayed in the console window. The text in the log displays the Render Manager activities, including

which frame is assigned to which Render node, which Render nodes have loaded the compositions in

the queue, and statistics for each render after completion.

To view the Render Log in the console:

�Open the Render Manager and choose Misc > Show Render Log.

�There are two modes for the Render Log: a Verbose mode and a Brief mode. Verbose mode logs

all events from the Render Manager, while Brief mode logs only which frames are assigned to

each Render node and when they are completed.

To disable Verbose mode:

�Choose Misc > Verbose Logging from the Render Manager’s menu bar.

Using Third-Party Render Managers with Fusion Studio

You can make use of third-party render manager software to control network rendering. This allows

for efficient sharing of your computer resources between the many applications that may make use of

them. Examples of such managers are Smedge from Uberware LLC, Rush from Seriss, and Deadline

from GetRender. Generally, these render managers use a command line renderer. By default, Fusion’s

Render nodes operate as a service to the Fusion internal Render Manager. However, you can also run

the Render nodes via the command line for third-party render managers.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Keep in mind that using a third-party render manager will prevent the use of some of Fusion’s network

rendering features, such as the ability to create network rendered Flipbook Previews and disk caches.

Command Line Rendering

For studios using third-party render farm managers like Deadline, Smedge, or Rush, the Fusion Render

node can be called via command line passing arguments and file paths. In this Windows example, a

Render node is called to load a composition called exampleV001, and render 10 frames:

//pathtoRN/FusionRenderNode.exe //pathtoProject/exampleV001.comp -render -start

101 -end 110 -quit

This would start up, render frames from 101 to 110, and then quit.

The following table lists additional command line features.

Command

Description

"Fusion Server -i"

Installs the license server as a service or daemon, launching it

on startup before user login.

"Fusion Server -S" (capital S)

Causes the Fusion Server to run persistently in the background,

until force-quit.

<filename.comp>

Full path and comp name, like

/storage/project/episode/shot/filename.comp.

-render

Tells the Render Node to render.

-frames <frameset>

Passes a series of frame ranges to be rendered—e.g.,

101..110,120,121,130..150.

-start <frame>

Sets the start frame of the render.

-end <frame>

Sets the last frame of the render.

-step <step>

Normally set to 1, step skip frames for rendering. For instance, 2

would render every second frame

-quit

Causes the Render Node to quit after the render is complete.

-join <host>

Prompts the node to connect to a manager at <hostname,IP>,

and (re)join any ongoing renders.

-listen

The node remains running and waits for incoming requests from

a manager.

-log <filename>

Causes the Render Node to output information about the render

to a log file. This appends to the end of an existing log file.

-cleanlog

Clears existing text from a log file.

-verbose

Outputs more detailed information into the log file.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Command

Description

-quiet

Suppresses pop-ups and interface buttons from displaying and

needing interaction.

-version

Returns the Render Node version number.

-pri high|above|normal|below|idle

Sets the node’s process priority to high, above, normal,

below, or idle.

-args <arg1> [, <arg2> ...]

Allows storing custom values that can be fetched by calling the

script function GetArgs(), which will return a table of { <arg1>,

<arg2>, ... }

TIP: An X11 virtual frame buffer is required to make a headless Linux command

line interface work.

Preparing Compositions

for Network Rendering

The way you construct a composition in Fusion Studio can help or hinder network rendering.

The media you read in, where plugins are installed, and the mix of operating systems on your

networked computers all play a part in how smoothly your network rendering goes. Your setup must

include several essential parts before network rendering will work:

�License dongle, Render Master, and Render nodes must be on the same local network (subnet).

�Fusion Server must be running as a background service on the same

computer where the dongle is installed.

�All source media from the comp should be placed on a network volume.

�The network volume must be mounted on each Render node.

�Loaders must point to the media on the mounted volumes.

�Savers must write to a drive that is mounted on each Render node.

�The Fusion comp must be saved to a volume that is mounted on each Render node.

�All Render Nodes and Render Masters need read and write access to any volumes specified as a

source media location or render destination.

�Make sure all fonts used in the comp for Text+ and 3D text nodes are installed on all the

Render nodes

�Make sure all Render nodes have third-party OFX plugins installed if any are used in the comp.

Below are more details about some of these items.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Using Relative Paths

The file paths used to load a composition and its media, and to save the composition’s rendered

results, are critical to the operation of network rendering. Each computer used for network rendering

must be able to access the media location for each Loader in the comp. Savers must be set up to save

to folders that all Render nodes can see and to which all Render nodes have write permission. Even

the composition must be saved in a folder accessible to all Render nodes, and it should be added to

the queue list using a path that’s visible to all Render nodes.

For example, if you open a composition located at c:\compositions\test1.comp in Fusion Studio and

add the composition to the network rendering queue, the Render Manager sends a message to each

Render node to load the composition and render it. The problem is that each computer is likely to have

its own c:\drive that does not contain the comp you created. In most cases, the Render nodes will be

unable to load the composition, causing it to fail.

Path Maps located in Fusion Preferences are virtual paths used to replace segments of file paths. They

can change the absolute paths used by Loader and Saver nodes to relative paths. There are a number

of Path Maps already in Fusion, but you can also create your own. The most common path to use is the

Comp:\ path.

Comp:\ is a shortcut for the folder where the actual composition is saved. So, using Comp:\ in a Loader

makes the path to the media file relative, based on the saved location of the comp file. As long as

all your source media is stored in the same folder or subfolder as your comp file, Fusion locates the

media regardless of the actual hard drive name.

Here’s an example of a file structure that enables you to use relative file references.

The composition is stored in the following file path:

Volumes\Project\Shot0810\Fusion\Shot0810.comp

And your source media is stored here:

Volumes\Project\Shot0810\Fusion\Greenscreen\0810Green_0000.exr

This overall directory structure can be seen in the following screenshot:

File paths can use relative paths based on the location of the saved comp file.

In this situation, using the Comp:\ path means your media location starts from your comp file’s

location. The relative path set in the Loader node would then be:

Comp:\Greenscreen\0810Green_0000.exr

Replacing the Loader’s path to start with

Comp:\ creates a relative path from the comp file’s location.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

If your source media’s actual file path uses a subfolder in the same folder as the comp

file’s folder:

Volumes\Project\Shot0810\Footage\Greenscreen\0810Green_0000.exr

The relative path set in the Loader node would then be:

Comp:\..\Footage\Greenscreen\0810Green_0000.exr

The two dots .. instruct the path to go up one folder.

TIP: Some Path Maps are not set up on a Fusion Render Node automatically. For instance,

you must manually add an entry for macros if you are using macros in your comp.