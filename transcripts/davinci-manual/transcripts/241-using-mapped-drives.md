---
title: "Using Mapped Drives"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 241
---

# Using Mapped Drives

Having the comp and media set to relative paths solves only part of the problem. Each computer

involved in rendering needs to have access to the drive where the comp and source media are

located. Mapping a drive provides permanent access to a folder on another computer or network

storage device.

Windows assigns a new drive letter to the folder, and it can be accessed just like any other drive

connected to your computer. Mapped drives assign a letter of the alphabet to a shared network

resource. Your shared drives must be the same drive letters on all Render nodes. For example, if your

media is on drive Z, then the network drive must appear as the letter Z on each of the Render nodes.

On macOS, you can map a network drive using Connect to Server from the Go menu. Entering the

smb:// path to the drive will mount it on the computer. Using Accounts > LogIn Items, you can have the

network drive auto-mount after a reboot as well.

Installing All Fonts on Render Nodes

All fonts used by Text tools in the composition must be available to all nodes participating in the

render. The render will otherwise fail on the Render nodes that do not have the font installed.

Installing Third-Party Plugins on Render Nodes

All third-party plugins and tools used by a composition must be installed in the plugins directory of

each Render node. A Render node attempting to render a composition that uses a plugin that’s not

installed will fail to render. Licensed plugins are required on each Render node.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Other Uses of Network Rendering

Although you will probably set up network rendering for the purpose of accelerating the output

of your final renders, Fusion is capable of using the network for other purposes as well. You can

use the Render nodes on your network to accelerate the creation of Flipbook Previews and disk

caching as well.

Flipbook Previews

Fusion Studio is able to use Render nodes to accelerate the production of Flipbook Previews, allowing

for lightning fast previews. Frames for previews that are not network rendered are rendered directly

into memory. Select the Use Network checkbox and the Render nodes to render the preview frames

to the folder set in the Preferences Global > Path > Preview Renders. This folder should be accessible

for all Render nodes that will participate in the network render. The default value is Temp\, which is a

virtual path pointing to the system’s default temp folder. This will need to be changed before network

rendered previews can function. Once the preview render is completed, the frames that are produced

by each Render node are spooled into memory on the local workstation. As each frame is copied into

memory, it is deleted from disk.

Disk Cache

Right-clicking a node in the Node Editor and choosing Cache to Disk opens a dialog used to create

the disk cache. If you enabled the Use Network checkbox and click the Pre-Render button to submit

the disk cache, the network Render nodes are used to accelerate the creation of the disk cache.

Render nodes can be used for disk caching as well as final renders.

When Renders Fail

It is a fact of life that render queues occasionally fail. The composition has an error, the power goes

out, or a computer is accidentally disconnected from the network are some causes for failure. If no one

is available to monitor the render, the risk that an entire queue may sit inactive for several hours may

become a serious problem.

Fusion Studio includes a variety of measures to protect the queue and ensure that the render

continues even under some of the worst conditions.

Automatic Rejoining of the Queue

If a Render node becomes unavailable to the Render Master for any reason, frames assigned to that

Render node are reassigned among the remaining Render nodes in the list.

When the Render node becomes available for rendering again, it will signal the Render Master that it is

ready to render again, and new frames will be assigned to that Render node.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

This is why it is important to set the Render Master in the network preferences of the Render

nodes. If the master is not set, the Render node will not know what master to contact when it

becomes available.

In the Fusion Render Node Preferences, select the Tweaks panel. Using the Last Render Node Restart

Timeout field, you can enter the number of seconds Fusion waits after the last Render node goes

offline before aborting that queue and waiting for direct intervention.

Relaunching Render Nodes with Fusion Server

Fusion Server is a small utility installed with Fusion Studio and the Render node. The application is

Fusion Server is a small utility installed with Fusion Studio and the Render node. The application is

silently launched by each Fusion Render node when started.

Fusion Server monitors the Render node to ensure that the Render node is still running during

a render. It consumes almost no CPU cycles and very little RAM. If the monitored Render node

disappears from the system’s process list without issuing a proper shutdown signal, as can happen

after a crash, the Fusion Server relaunches the Render node, allowing it to rejoin the render.

Fusion Server will only detect situations where the Render node has exited abnormally. If the Render

node is still in the process list but has become unresponsive for some reason, the Fusion Server

cannot detect the problem. Hung processes like this are detected and handled by frame timeouts, as

described below.

Frame Timeouts

Frame timeouts are a fail-safe method of canceling a Render node’s render if a frame takes longer

than the specified time (with a default of 60 minutes, or one hour). The frame timeout ensures that

an overnight render will continue if a composition hangs or begins swapping excessively and fails to

complete its assigned frame.

The timeout is set per composition in the queue. To change the timeout value for a composition from

the default of 60 minutes, right-click on the composition in the Render Manager’s queue list and select

Set Frame Timeout from the contextual menu.

Right-click over a comp in the Render Manager to set a timeout value.

To change the frame timeout value, choose Set Frame Time Out from the Render Manager’s Misc

menu and enter the number of seconds you want for the Time Out.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Heartbeats

The Render Master regularly sends out heartbeat signals to each node, awaiting the node’s reply.

A heartbeat is basically a message from the manager to the Render node asking if the node is still

responsive and healthy. If the Render node fails to respond to several consecutive heartbeats, Fusion

will assume the Render node is no longer available. The frames assigned to that Render node will be

reassigned to other Render nodes in the list.

The number of heartbeats in a row that must be missed before a Render node is removed from the list

by the manager, as well as the interval of time between heartbeats, can be configured in the Network

Preferences panel of the master. The default settings for these options are fine for 90% of cases.

If the compositions that are rendered tend to use more memory than is physically installed, this will

cause swapping of memory to disk. It may be preferable to increase these two settings somewhat to

compensate for the sluggish response time until more RAM can be added to the Render node.

Managing Memory Use

Often, the network environment is made up of computers with a variety of CPU and memory

configurations. The memory settings used on the workstation that created a composition may not be

appropriate for all the Render nodes in the network. The Render node software offers the ability to

override the memory settings stored in the composition and use custom settings more suited to the

system configuration of a specific Render node.

To access preferences for a node, right-click on the icon in the Windows Notification area or from the

macOS menu bar and choose Preferences. In the Preferences dialog, select the Memory panel.

Override Composition Settings

Enable this option to use the Render node’s local settings to render any incoming compositions.

Disable it to use the default settings that are saved into the composition.

Render Several Frames at Once

Fusion has the ability to render multiple frames at once for increased render throughput. This slider

controls how many frames are rendered simultaneously. The value displayed multiplies the memory

usage (a setting of 3 requires three times as much memory as a setting of 1).

Normal values are 2 or 3, although machines with a lot of memory may benefit from higher values,

whereas machines with less memory may require the value to be 1.

Simultaneous Branching

Enable this option to render every layer in parallel. This can offer substantial gains in throughput

but may also use considerably more memory, especially if many layers are used in the composition.

Machines with limited memory may need to have Simultaneous Branching disabled when rendering

compositions with many layers.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION

Limitations of Render Nodes

There are a few important limitations to remember while setting up compositions and

rendering over a network.

Time Stretching

Compositions using the Time Stretcher and Time Speed tools may encounter difficulties when

rendered over the network. Speeding up or slowing down compositions and clips requires fetching

multiple frames before and after the current frame that is being rendered, resulting in increased I/O to

the file server. This may worsen bottlenecks over the network and lead to inefficient rendering. If the

composition uses the Time Stretcher or Time Speed tools, make certain that the network is up to the

load or pre-render that part of the composition before network rendering.

Linear Tools

Certain tools cannot be network rendered properly. Particle systems from third-party vendors, such as

Genarts’s Smoke and Rain, and the Fusion Trails node cannot render properly over the network. These

tools generally store the previously rendered result and use it as part of the next frame’s render, so

every frame is dependent on the one rendered before it. This data is local to the tool, so these tools

do not render correctly over a network.

Saving to Multi-Frame Formats

Multiple machines cannot render a single QuickTime file. Always render to separate sequential file

formats like EXR, DPX, JPEG, and so on. Once the render is complete, a single workstation can load

the image sequence in order and save to the desired compiled format.

NOTE: The above does not apply to network rendered previews, which are previews created

over the network that employ spooling to allow multi-frame formats to render successfully.

Only final renders are affected by this limitation.

Troubleshooting

There are some common pitfalls when rendering across a network. Virtually all problems with network

rendering have to do with path names or plugins. Return to the “Preparing Compositions for Network

Rendering” section in this chapter to review some of the essential setup requirements. Verify that all

Render nodes can load the compositions and the media, and that all Render nodes have installed the

plugins used in the composition.

If some difficulties persist, contact Blackmagic Design’s technical support using the support section on

the Blackmagic Design website. Save a copy of the render.log file to send to technical support.

Checking the Render Log

The log file shown in the Render Manager dialog displays messages that can assist with diagnosing

why a render or node has failed. The render log shows a step-by-step account of what happened (or

didn’t happen) during a render. If a Render node cannot be found, fails to load a composition or render

a frame, or simply stops responding, it will be recorded here.


Fusion Fundamentals | Chapter 66 Rendering Using Saver Nodes

FUSION