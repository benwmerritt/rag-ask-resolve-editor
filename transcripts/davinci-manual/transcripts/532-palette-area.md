---
title: "Palette Area"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 532
---

# Palette Area

Most everyday tools and functions for grading are distributed among a series of palettes found in the

palette area of the Color page. These palettes can be accessed via a series of palette buttons running

along the Palette bar at the top of this area.

All palettes seen in the Palette bar

These buttons also give you feedback about which palettes have adjustments for the current selected

node in the Node Editor. Palettes with adjustments show a small orange dot in the corresponding

palette button.

An orange dot in a palette button lets you know there are adjustments in that palette

Left Palettes

A series of palettes at the bottom left of the Color page provide access to different sets of grading

tools, used principally for manipulating color, contrast, and raw media format settings. Each individual

palette is opened by clicking the corresponding icon at the top of the Palette panel.


Color | Chapter 126 Using the Color Page

COLOR

Left palette selection buttons

Camera Raw palette: For making metadata adjustments to raw media formats

Color Match palette: Automatic grading based using test charts

Primaries: Graphical color balance controls and master wheels, along with a Slider

mode for adjusting YRGB Lift/Gamma/Gain

HDR palette: Advanced primary grading controls designed for wide-gamut media and

SDR or HDR mastering

RGB Mixer: For mixing color channels into one another

Motion Effects palette: With controls for noise reduction and artificial motion blur

The five available palettes can be used individually or together depending on what you’re trying to accomplish.

For more information on most of these palettes, see Chapter 129, “Primaries Palette.”

For more information on the Motion Effects palette, see Chapter 153, “The Motion Effects and

Blur Palettes.”

Center Palettes

At 1920x1080 resolution or higher, a second set of palettes is organized at the bottom center of the

Color page. These palettes span a

range of functionality, and the adjustments you make with them can be combined with those made

using the Color palettes.

Center palette selection buttons

NOTE: At lower resolutions, the Left and Center palettes are merged to fit the

DaVinci Resolve interface into a smaller area.


Color | Chapter 126 Using the Color Page

COLOR

The center palettes include the Curves palette, Color Slice palette, the Color Warper palette, the

Qualifier palette, the Window palette, the Tracker palette, the Magic Mask palette, the Blur palette, the

Key palette, the Sizing palette, and the Stereoscopic 3D palette.

Curves palette

ColorSlice palette

Color Warper palette

Qualifier palette

Window palette

Tracker palette

Magic Matte palette

Blur palette

Key palette

Sizing palette

Stereoscopic 3D palette

Keyframe Editor, Video Scopes, and Information

The bottom right of the Color page can be switched between one of three things:

The three controls for displaying the Keyframe Editor,

video scopes, or Information palette

Keyframe Editor: Provides an interface for animating Color, Sizing, and Stereo Format

adjustments over time. Each node in the Node Editor corresponds to a track in the

Keyframe Editor, which lets you animate each node’s adjustments independently.

Furthermore, each node’s track can be opened up to reveal parameter groups, so

that you can animate subsets of an individual node’s functions independently of other

functions within the same node.

For more information about keyframing, see Chapter 148, “Keyframing in the

Color Page.”

Video scopes: Provides a docked area where you can expose one video scope at

a time for reference while you work. You can also “undock” the video scopes into

a stand-alone window, in which you can show four different scopes at a time. More

information about using the video scopes appears later in this chapter.

Information: Provides a way of seeing clip and system information while you work.


Color | Chapter 126 Using the Color Page

COLOR

Dual-Monitor Layout

The Color page has a dual monitor layout that provides maximum space for the Viewer, Node Editor,

and Control palettes on the primary monitor, and a simultaneously displayed Gallery, Lightbox,

Keyframe Editor, Metadata Editor, and Video Scope panel on the secondary monitor. The second

screen of a dual-screen layout can be resized, but not reorganized.

If you have an single ultra-wide monitor, you can also use the dual-monitor layout, and DaVinci Resolve

will scale the interface as if you had two normal monitors side by side.

To enter dual-screen mode:

Choose Workspace > Dual Screen > On.

The Color page in dual screen mode


Color | Chapter 126 Using the Color Page

COLOR

To switch which UI elements appear on which monitors:

Choose Workspace > Primary Display > (Monitor Name), which reverses the contents of both

monitors in dual screen mode.

The Info Palette and Clip Information

The Info palette is hidden by default. Clicking the Info palette button at the far right of the toolbar

reveals it. The Info palette has two tabs that display different information. There are no user-editable

controls in the Info palette.

Info palette displaying Clip Info and System Status

Clip Info

The first tab displays information about whichever clip is currently selected in the Timeline.

This information is not editable, but is provided for reference, and includes:

File Name

The name of the media file on disk. If the current clip is a Multicam clip, this shows

the name of the currently selected angle.

Reel Name

The reel name of that clip, if one is being read properly.

Start T/C

The source timecode value of the first frame in the clip.

End T/C

The source timecode value of the last frame in the clip.


Color | Chapter 126 Using the Color Page

COLOR

Duration

The duration of the clip, in timecode.

Frames

The duration of the clip, in frames.

Version

The name of the remote or local version used by that clip.

Frame Rate

The frame rate used by that clip.

Source Res

The native resolution of the source clip.

Codec

The codec or format used by the source clip.