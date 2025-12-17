---
title: "Status Bar"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 8
---

# Status Bar

The status bar at the bottom of the Fusion page, immediately above the Resolve Page bar, shows

you a variety of up-to-date information about things you’re selecting and what’s happening in the

Fusion page.

For example, hovering the pointer over any node displays information about that node in the

status bar (as well as in a floating tooltip), while the currently achieved frame rate appears

whenever you initiate playback, and the percentage of the RAM cache that’s used appears at

all times. Other information, updates, and warnings appears in this area as you work.

The status bar under the Node Editor showing you

information about a node under the pointer and a floating tooltip

The Console

The console, available by choosing Workspace > Console, is a window in which you can see the error,

log, script, and input messages that may explain something the Fusion page is trying to do in greater

detail. The console is also where you can read FusionScript outputs or input FusionScripts directly.

Occasionally, the status bar (described above) will display a badge to let you know there’s a message

in the console you might be interested in. The badge will indicate if the message is an error, log,

or script message.

The Console window


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

The Color Page

The Color page is where you color correct, or grade, your program. It has all of the controls available

for manipulating color and contrast, reducing noise, creating limited secondary color corrections,

building image effects of different kinds, adjusting clip geometry, and making many other corrective

and stylistic adjustments. The Color page is divided into seven main areas that work together to let

you build a grade.

For more detailed information about the Color page, see Chapter 124, “Using the Color Page.”

The Color page

Viewer

The Viewer shows the frame at the current position of the playhead in the Timeline. The contents

of the Viewer are almost always output to video via whichever I/O interface you have connected.

At the top of the Viewer is a header that displays the Project and Timeline names, as well as a Viewer

Timecode display that shows the source timecode of each clip by default. The Timeline name is also

a drop-down display that lets you switch to any other timeline in the project. A jog bar (sometimes

referred to as a scrubber bar) underneath the image lets you drag the playhead across the entire

duration of the clip, while transport controls underneath that let you control playback. A toolbar at the

top provides controls governing Image Wipes, Split-Screen controls, and Highlight display. Additional

controls let you turn audio playback on and off, or adjust them by right-clicking on the speaker icon

and dragging the slider. You can also choose which onscreen controls are currently displayed.


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Viewer with transport controls

You can also put the Viewer into Cinema Viewer mode by choosing Workspace > Viewer Mode >

Cinema Viewer (Command-F), so that it fills the entire screen. This command toggles Cinema Viewer

mode on and off. Two other modes, Enhanced Viewer (Option-F) and Full Screen Viewer (Shift-F), are

available to provide more working area for tasks such as window positioning and rotoscoping.

Gallery

The Gallery is used for storing still frames to use as reference when comparing clips to one another.

Each still frame also stores that clip’s grade so you can copy it later; stills and grades are stored

together. A button lets you open up the Album browser, used for organizing your stills. At the top of the

Gallery, Memories let you store grade information that you can apply using a control panel or keyboard

shortcuts. You can also open a larger Gallery window within the Color page that provides more room

for organizing your saved stills and grades.

For more information on the Gallery page, see Chapter 141, “Using the Gallery.”

The Gallery has Memories, stills saved in albums, and your PowerGrades


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

Node Editor

The Node Editor is where you assemble one or more individual corrections (nodes) together to create

multi-correction grades (seen as node trees). This is a powerful way of assembling grades, since

different combinations of nodes let you create different corrections and very specific adjustments by

reordering operations, combining keys, or changing the layer order of different adjustments.

For more information about the Node Editor, see Chapter 143, “Node Editing Basics.”

Node Editor to construct your grade processing signal flow

Timeline

The Timeline in the Color page reflects the contents of the Timeline in the Edit page, but has a

different appearance that’s tailored to the requirements of the colorist. However, the content is

identical, and changes made to the Timeline in the Edit page are immediately seen in the Color page

as you switch back and forth. The Color page Timeline provides several ways of navigating the clips in

your project, as well as keeping track of what has been done to which clips.

The Color page Timeline


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

The Timeline is divided into three parts, each of which shows different information and provides

differing controls. A Timeline Ruler at the top lets you scrub the playhead across multiple clips,

and can be zoomed out enough to show every clip in your entire program. Underneath, the Mini-

Timeline (which can be opened or closed via a button at the right of the palette bar) shows a small

representation of the Timeline in the Edit page wherein each clip is as long as its actual duration.

At the bottom of the Timeline is the Thumbnail timeline, in which each clip is represented by a single

frame. The currently selected clip is outlined in orange, and information appears above and below

each thumbnail such as each clip’s source timecode, clip number and track number, version name,

whether it’s been graded, whether it’s been tracked, if it’s been flagged, and so on.

Left Palettes

A series of palettes at the bottom left of the Color page provide access to different sets of grading

tools, used principally for manipulating color, contrast, and raw media format settings. Each individual

palette is opened by clicking the corresponding icon at the top of the Palette panel.

Left palette selection buttons in the top bar

The available palettes are the Camera Raw palette (for making metadata adjustments to raw media

formats), the Color Match palette (for creating automatic grades by sampling on-camera color charts),

the Color Wheels (graphical color balance controls and master wheels or sliders for adjusting YRGB

Lift/Gamma/Gain), HDR Grade for enhanced High Dynamic Range grading, the RGB Mixer (for mixing

color channels into one another), and the Motion Effects palette (with controls for noise reduction and

artificial motion blur).

Center Palettes

At 1920x1080 resolution or higher, a second set of palettes is organized at the bottom center of the

Color page. These palettes span a wide range of functionality, and the adjustments you make with

them can be combined with those made using the Color palettes.

Center palette selection buttons


DaVinci Resolve Interface | Chapter 1 Introduction to DaVinci Resolve

INTRO

NOTE: At lower resolutions, the Left and Center palettes are merged to fit the

DaVinci Resolve interface into a smaller area.

The eight available Center palettes include the Curves palette, the Color Warper palette, the Qualifiers

palette, the Windows palette, the Tracker palette, the Magic Mask palette, the Blur palette, the Key

palette, the Sizing palette, and the Stereoscopic 3D palette.