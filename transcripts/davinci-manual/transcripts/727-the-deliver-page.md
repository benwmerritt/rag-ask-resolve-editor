---
title: "The Deliver Page"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 727
---

# The Deliver Page

The Deliver page is divided into five areas of functionality, each of which lets you set up a different

part of a render or output to tape.

Deliver page

The Interface Toolbar

At the very top of the Deliver page is a toolbar with buttons that let you show and hide different parts

of the user interface. These buttons are as follows, from left to right:

The Interface toolbar

Delivery full/half height button: Lets you set the Render Settings panel to take up

the full height of your display, if you need more area for browsing the various render

settings, at the expense of a narrower Timeline.

Render Settings: This panel lists all of the render settings that are available

for configuring rendering jobs in DaVinci Resolve. By default, you’re presented with a

short list, but more options are available by clicking “Advanced Settings.”

Tape: Puts the Deliver page into Tape Output mode.

Clips: Hides or shows the Thumbnail timeline above the Deliver page timeline


Deliver | Chapter 186 Using the Deliver Page

DELIVER

Render Queue: A list of all jobs that you’ve set up to render in the current project.

Previously rendered jobs remain in the queue, for your reference or for you to reuse to

re-render those jobs, unless you manually delete them from the queue.

Render Queue full/half height button: Lets you set the Render Queue to take up the

full height of your display, if you need more area for listing render jobs at the expense of

a narrower Timeline.

The Render Settings

The Render Settings contains the customizable settings that determine how media is rendered out of

DaVinci Resolve. If you’re using the Tape option, these settings are disabled.

The Render Settings are divided into

four general sections:

Render Presets: At the very top,

a scrollable row of icons lets you

choose one of a series of presets to

quickly set up the type of render you

want. The Custom option exposes all

render settings so you can set up a

render manually.

Render Location: A Browse button

opens a dialog that lets you choose a

volume and directory to render to.

Render: Two options let you either

render the entire selected area of the

Timeline as a single clip suitable for

reviewing or mastering, or as a series

of individual clips more suited to

round-trip workflows. The option you

choose here changes which render

settings are available below.

Video, Audio, and File Render

Settings Panels: All other render

settings are divided among three

panels. Checkboxes at the top of

the Video and Audio panels let you

selectively disable video export (if

you want to export the audio only) or

disable audio export (if you want to

export video only).

For more information on all of

these settings, see Chapter 187,

“Rendering Media.”

Render Settings


Deliver | Chapter 186 Using the Deliver Page

DELIVER

Rendering Files vs. Outputting to Tape

Because the Deliver page does double duty, you control whether you’re rendering files or outputting

to tape using the Tape button in the Interface toolbar. Doing so replaces the controls in the Viewer

with tape controls.

Render or Edit to Tape modes

The Deliver Page Timeline

You’ll use the Timeline in the Deliver page to define the range of clips you want to render or output

to tape, and to choose which versions for each clip you want to output. The Deliver page Timeline

consists of a Thumbnail timeline at top (that can be shown or hidden via the Clips button) that makes

it easy to select individual clips or ranges of clips that you need to render, and a more ordinary timeline

below that you can use to set In and Out points for rendering arbitrary regions of your program.

A Timeline toolbar lets you choose the render range of the Timeline, and has controls for customizing

the look of the Timeline, and for zooming in and out.

The Deliver page’s Timeline and Thumbnail timeline

TIP: Press Shift-Z to fit the entire program into the available width of the Timeline.

Filtering the Thumbnail Timeline

The Deliver page Thumbnail timeline also has the Timeline Filter dropdown, available to the right of

the Clips button in the Interface toolbar.

The Deliver page’s Thumbnail timeline matches the Color page


Deliver | Chapter 186 Using the Deliver Page

DELIVER

Using this dropdown to filter the contents of the Timeline lets you restrict the range of media you

want to output in different ways. For example, if you’ve already rendered a timeline, but you’ve

since made some changes, you can use one of the “Modified Clips” options to display only the

clips that have changed within a particular timeframe. Another commonly used option is to choose

“Unrendered Clips” to isolate all clips that have not yet been rendered in workflows where you’re only

rendering a part of the Timeline at a time.

When you filter the Thumbnail timeline, you can only set up jobs to render in Individual Clips mode.

You can tell if Thumbnail filtering is enabled by an orange underline under the Clips button in the

UI toolbar.

An orange line under the Clips

button shows that filtering is enabled

The Viewer

When rendering file-based media, the Viewer shows you exactly how the media being output will

look using the current settings, and the transport controls move the playhead throughout the current

Timeline. Audio playback can be turned on or off by clicking on the speaker icon, or adjust the level by

right-clicking on the speaker icon and dragging the slider.

Deliver page Viewer

When outputting to tape, the Viewer shows you the tape output so you can set up insert or assembly

edit points, and the transport controls move the tape in the deck if device control is enabled. You

can also put the Viewer into Cinema Viewer mode by choosing Workspace > Viewer Mode > Cinema

Viewer (P), so that it fills the entire screen. This command toggles Cinema Viewer mode on and off.


Deliver | Chapter 186 Using the Deliver Page

DELIVER

Disabling Viewer Updates While Rendering

An Updates During Renders submenu in the Render page Viewer option menu lets you choose to

disable, minimize, or enable Viewer updates while a program is being rendered. Disabled or minimized

Viewer updates will speed rendering, especially on slower workstations.

The Render Queue

The Render Queue is a list of all the jobs you’ve queued up for delivery. Each job can have an

individualized range of clips and render settings, which you can use to render multiple sections or clips

of a timeline, the same timeline output to multiple formats, or multiple timelines.

The Render Queue also has the option to show either just the jobs within the current project, or jobs

queued up and saved within all projects in the currently open SQL network project library (for the

current user) or local project library (at the currently selected disk location). This can be exceptionally

useful in situations where you’ve broken a program into multiple reels, with each reel being a different

project. This can be turned on and off via the “Show All Projects” option of the Render Queue

Option menu.

Jobs in the Render Queue can be edited (by clicking the pencil button), they can be assigned to

remote rendering workstations, and they can be deleted. Jobs that have already been rendered can

be kept in the Render Queue and re-rendered at a later time.

The Render Queue displays all jobs


Deliver | Chapter 186 Using the Deliver Page

DELIVER

TIP: There is an option to show the Render Settings of each item in the Render Queue,

by selecting “Show Job Details” in the Render Queue Option menu. This provides specific

details of each job’s dimensions, frame rate, codec etc. This is a great help in managing a

complex render queue at a glance.