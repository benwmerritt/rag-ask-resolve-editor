---
title: "Timeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 289
---

# Timeline

The Timeline preferences is where you create and edit Keyframes Editor/Spline Editor filters and set

default options for the Keyframes Editor.

The Timeline preferences

Filter/Filter to Use

The Filter menu populates the hierarchy area below the menu with that setting. It lets you edit the filters.

The Filter to Use menu selects the default filter setting located in the Keyframes Editor Options menu.

Settings for Filters

This area is used to create a new filter and define its settings. You start by first clicking the New button

and entering the name of the new Filter. You then select any of the tools that you want the filter to

contain. Only tools that are checked will appear in the Keyframes Editor or Spline Editor when the filter

is selected. You can also create a copy of the filter using the Copy button or remove a filter from the

list by clicking the Delete button.

Timeline Options

The Timeline Options configure which options in the Keyframe Editor are enabled by default. A series

of checkboxes correspond to buttons located in the Timeline, allowing you to determine the states of

those buttons at the time a new comp is created.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

For more information on the Keyframes Editor functions, see Chapter 71, “Animating in Fusion’s

Keyframes Editor,” in the DaVinci Resolve Reference Manual or Chapter 9 in the Fusion

Reference Manual.

�Autosnap Points: When moving points in the Keyframes Editor, the points will snap to the fields or

to the frames, or they can be moved freely.

�Guides: When moving points in the Keyframes Editor, the point will snap to the guides that are

placed in the Timeline graph.

�Autosnap Guides: When moving or creating guides, the guides will snap to the fields or to the

frames, or they can be moved freely.

�Autoscale: Keeps the Timeline scales intact while changing the editable spline content in the

graph. When set to scroll, the Timeline scrolls horizontally and vertically to show all or most of the

spline points when changing the editable spline content in the graph. When set to Fit, the Timeline

zooms to fit all points within the graph, if necessary.

�Tools Display Mode: This menu controls the default sort order of the tools displayed in the

Keyframes Editor. The default can be changed using the Sort order menu in the upper right of the

Keyframes Editor.

Tweaks

The Tweaks preferences handle a collection of settings for fine-tuning Network rendering in Fusion

Studio and graphics hardware behavior.

The Tweaks preferences


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Network

The Network section is used to control and monitor the health of communication packets over TCP/IP

when rendering over a network in Fusion Studio.

�Maximum Missed Heartbeats: This setting determines the maximum number of times the network

is checked before terminating the communication with a Render node.

�Heartbeat Interval: This sets the time between network checks.

�Load Composition Timeout: This timeout option determines how long the Render Manger will wait

for a composition to load before moving on to another task.

�Last Slave Restart Timeout: This timeout option determines how long the Render Manager will

wait for a render salve to respond before using another render slave.

File I/O

The File I/O options are used to control the performance when reading frames or large media files

from both direct and networked attached storage.

�I/O Canceling: This option enables a feature of the operating system that allows queued

operations to be canceled when the function that requested them is stopped. This can improve

the responsiveness, particularly when loading large images over a network.

Enabling this option will specifically affect performance while loading and accessing formats that

perform a large amount of seeking, such as the TIFF format.

This option has not been tested with every hardware and OS configuration, so it is recommended

to enable it only after you have thoroughly tested your hardware and OS configuration using drive

loads from both local disks and network shares.

�Enable Direct Reads: Enabling this checkbox uses a more efficient method when loading a large

chunk of contiguous data into memory by reducing I/O operations. Not every operating system

employs this ability, so it may produce unknown behavior.

�Read Ahead Buffers: This slider determines the number of 64K buffers that are use to read ahead

in a file I/O operation. The more buffers, the more efficient loading frames from disk will be, but the

less responsive it will be to changes that require disk access interactively.

Area Sampling

The Area Sampling options allow you to fine-tune the RAM usage on Render nodes by trading off

speed for lower RAM requirements.

�Automatic Memory Usage: This checkbox determines how area sampling uses available memory.

Area sampling is used for Merges and Transforms. When the checkbox is enabled (default), Fusion

will detect available RAM when processing the tool and determine the appropriate trade-off

between speed and memory.

If less RAM is available, Fusion will use a higher proxy level internally and take longer to render.

The quality of the image is not compromised in any way, just the amount of time it takes to render.

In node trees that deal with images larger than 4K, it may be desirable to override the automatic

scaling and fix the proxy scale manually. This can preserve RAM for future operations.

�Pre-Calc Proxy Level: Deselecting the Automatic Memory will enable the Pre-Calc Proxy Scale

slider. Higher values will use less RAM but take much longer to render.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Open GL

This section controls how Fusion makes use of your graphics card when compositing in 3D with the

Renderer 3D node. Most settings may be left as they are, but since OpenGL hardware varies widely in

capabilities and different driver revisions can sometimes introduce bugs, these tweaks can be useful if

you are experiencing unwanted behavior.

�Disable View LUT Shaders: OpenGL shaders can often dramatically accelerate View LUTs, but

this can occasionally involve small trade-offs in accuracy. This setting will force Fusion to process

LUTs at full accuracy using the CPU instead. Try activating this if View LUTs do not seem to be

giving the desired result.

�Use Float16 Textures: If your graphics hardware supports 16-bit floating-point textures, activating

this option will force int16 and float32 images to be uploaded to the viewer as float16 instead,

which may improve playback performance.

�Texture Depth: Defines in what depth images are uploaded to the viewer.

Auto: The Auto option (recommended) lets Fusion choose the best balance of performance and

capability.

int8: Similar to the Use Float16 Textures switch, this option can be used to force images to be

uploaded to the Display View as int8, which can be faster but gives less range for View LUT

correction.

Native: The Native option uploads images at their native depth, so no conversion is done.

�Image Overlay: The Image Overlay is a viewer control used with Merge and Transform tools

to display a translucent overlay of the transformed image. This can be helpful in visualizing the

transformation when it is outside the image bounds but may reduce performance when selecting

the tool if cache memory is low. There are three settings to choose from: None, Outside, and All.

None: This setting never displays the translucent overlay or controls, which can reduce the need

for background renders, in some cases resulting in a speed up of the display.

Outside: This will display only those areas of the control that are outside the bounds of the image,

which can reduce visual confusion.

All: Displays all overlays of all selected tools.

�Smooth Resize: This setting can disable the viewer’s Smooth Resize behavior when displaying

floating-point images. Some older graphics cards are not capable of filtering floating-point

textures or may be very slow. If Smooth Resize does not work well with float images, try setting

this to flt16 or int.

�Auto Detect Graphics Memory (MB): Having Fusion open alongside other OpenGL programs

like 3D animation software can lead to a shortage of graphics memory. In those cases, you can

manually reduce the amount of memory Fusion is allowed to use on the card. Setting this too low

or too high may cause performance or data loss.

�Use 10-10-10-2 Framebuffer: If your graphics hardware and monitor support 30-bit color (Nvidia

Quadro/AMD Radeon Pro, and some Nvidia GeForce/AMD Radeon), this setting will render

viewers with 10 bits per primary accuracy, instead of 8 bits. Banding is greatly reduced when

displaying 3D renders or images deeper than 8-bit.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

User Interface

The User Interface preferences set the appearance of the user interface window and how the

Inspector is displayed.

The User Interface preferences

Appearance

When enabled, the Use Gray Background Interface checkbox will change the color of the background

in Fusion’s panels to a lighter, more neutral shade of gray.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Controls

This group of checkboxes manages how the controls in the Inspector are displayed.

�Auto Control Open: When disabled, only the header of the selected node is displayed in the

Inspector. You must double-click the header to display the parameters. When enabled, the

parameters are automatically displayed when the node is selected.

�Auto Control Hide: When enabled, only the parameters for the currently active tool (red outline)

will be made visible. Otherwise, all tool headers will be visible and displayed based on the Auto

Control Open setting.

�Auto Control Close Tools: When enabled, only the active (red outlined) tool in the Node Editor will

have controls displayed. Any previous active node’s tools will be closed in the Inspector. When

disabled, any number of tools may be opened to display parameters at the same time. This setting

has no effect if the Auto Control Hide checkbox is enabled.

�Auto Control Close Modifiers: When enabled, only one modifier’s parameters will be displayed for

the active node. Any additional modifiers for the active node will show only their header.

�Auto Control Advance: If the Auto Control Advanced checkbox is enabled, the Tab key and

Return/Enter key will cause the keyboard focus to advance to the next edit box within the

Inspector. When disabled, Return/Enter will cause the value entered to be accepted, but the

keyboard focus will remain in the same edit box of the control. The Tab key can still be used to

advance the keyboard focus.

�Show Controls for Selected: When this option is disabled, only the active tool’s parameters are

shown in the Inspector. By default, it is enabled, showing controls for the active tool as well as all

selected tools.

�Combined Color Wheel: When the Color Corrector tool is displayed in the Inspector, enabling

this checkbox will show one color wheel with buttons to switch between the master, shadow,

midtones, and highlight channels. Otherwise, four color wheels are displayed in the Inspector.

�Gamma Aware Color Controls: This setting adjusts color correction nodes when working

with Rec. 709 images in a non-color managed project. Rec. 709 images appear correct on

the computer monitor because monitors have a gamma adjustment built in. When working in

the Rec. 709 color space without color management, enabling Gamma Aware color removes

the gamma, applies the color correction as if it where linear, and then reapplies the gamma.

For Rec. 709 images, enable the Gamma Aware setting and enter a Gamma value of 2.4. In a color

managed linear project, this should be set to Off or a value of 1.0. When dealing with mixed color

spaces, Fusion reads the metadata from the image and sets the Aware gamma value based on the

metadata available.

�Grab Distance: This slider ranges from 1 to 10 and defaults to 5. It designates the active area

around the mouse pointer and can be modified if you have difficulties in selecting points for

modification in paths and spline curves. Smaller values will require a more accurate selection with

the mouse pointer.

Touch Scrolling and Mouse Wheel

This group of settings allows you to configure which, if any, keyboard modifiers are needed to pan or

zoom a panel when using a trackpad or middle mouse wheel.


Fusion Fundamentals | Chapter 75 Preferences

FUSION