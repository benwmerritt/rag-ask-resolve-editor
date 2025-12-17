---
title: "Title Generator Panels"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 192
---

# Title Generator Panels

The parameters of text generators are divided into two panels in the Video Inspector: the Title panel

and the Settings panel.

�The Title panel contains all of the text editing, styling, and sizing controls used to edit the contents

and look of a title in your project, including the Rich Text, Drop Shadow, Stroke, and Background

parameters.

�The Settings panel contains the same Composite, Transform, and Cropping parameters that

all other clips in DaVinci Resolve have. These parameters are intended for compositing and

animating a title.

Shared Title Generator Parameters

With the exception of the Text+ generator, all other title generators in DaVinci Resolve are capable

of rich text styling. This means you can select any portion of a generator’s text and style it differently.

For example, you could have three lines of text within a single generator and style each line

individually to create a particular design.

A single generator with three lines of differently styled text

Each title generator shares the same parameters in the Video Title panel of the Inspector for editing

and styling text:

Rich Text: A control group consisting of a text entry field and parameters that can be used to style

different parts of the text independently.

�Text: A text entry field for editing the title being generated. If no characters are selected, the

styling controls affect the entire block of text. If you select a specific set of characters, the

styling controls only affect the selection. Text in this field can also be edited directly in the

Timeline Viewer.

�Font family: A pop-up for choosing one of the font families installed on your workstation.

�Font face: A pop-up for choosing which face of the font family currently selected to use.

�Color: Opens the standard color picker for choosing a font color.

�Size: Slider for choosing the text size.

�Tracking: Slider that sets the spacing between characters.

�Line spacing: Slider for setting the spacing between the selected line of text and the

next one below.

�Font style: Buttons to apply underline, overhead line, strikethrough, superscript,

and subscript styling.


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

�Font case: A pop-up for forcing the text selection to be Mixed Case (the default),  All Caps, All

Lowercase, Small Caps, or Title Caps.

�Alignment: Buttons to select the method of alignment: left, centered, right, or justified.

�Anchor: Buttons for selecting how text is anchored to the current position, both horizontally (top,

centered, bottom) and vertically (right, centered, left).

�Position: X and Y parameters determining the bottom left-hand corner (the default Anchor

settings) of the rich text block being generated. Corresponds to the act of dragging a selected text

box in the Timeline Viewer.

�Zoom: X and Y parameters determining the scale of the text. A link button lets you keep the X

and Y parameters locked together. Corresponds to the act of resizing a selected text box in the

Timeline Viewer from either the corners (to resize proportionally), or the top/bottom/sides (to

stretch or squeeze the text).

�Rotation Angle: A slider for rotating the orientation of the text. Corresponds to the act of rotating a

selected text box in the Timeline Viewer using the rotation handle.

Drop Shadow: A group of controls that lets you apply a customizable drop shadow to every character

of text being generated.

�Color: Opens the standard color picker for choosing a drop shadow color.

�Offset: X and Y parameters determining how offset the drop shadow is from the original text.

�Blur: A slider for blurring the drop shadow.

�Opacity: A slider determining how transparent the drop shadow is.

Stroke: Lets you add an outline to every character of text being generated.

�Color: Opens the standard color picker for choosing the stroke color.

�Size: A slider lets you choose the thickness of the stroke, in pixels.

Background: This group of controls provides an extremely flexible rectangle or rounded rectangle

shape that you can use to add a background, bar, outline, or other intersecting shape to use when

designing a title.

�Color: Opens the standard color picker for choosing the interior color of the background shape.

�Outline color: Opens the standard color picker for choosing outline color of the

background shape.

�Outline width: A slider lets you choose the thickness of the background shape outline, in pixels.

�Width: A slider lets you choose how wide to make the background shape.

�Height: A slider lets you choose how tall to make the background shape.

�Corner radius: A slider lets you choose the roundness of the rectangle edges.

�Center: X and Y parameters you can use to offset the background shape from the text

being generated.

�Opacity: A slider lets you set the transparency of the background shape.

Title Generator Settings Parameters

Additionally, each generator has Composite, Transform, and Cropping parameters in the Settings

panel of the Video Inspector that let you composite, resize, and animate titles against other clips in the

Timeline for motion graphics effects. These parameters are the same as those available for every clip,

as described later in this chapter.


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

The Text+ Title Generator

A new kind of title generator, named Text+, is available in the Titles category of the Effects Library’s

toolbox. This is the exceptionally fully-featured 2D text generator from Fusion, available for editing and

customizing right in the Edit page. It’s capable of most of what the Text generator can do, including rich

text editing and use of on-screen controls in the Timeline Viewer. It also has many more styling and

animation controls than the Text generator.

TIP: At the time of this writing, the Text generator is still very useful for quickly creating text

pages with multiple styles, whereas the Text+ generator excels at creating text for animated

motion graphics.

The new Text+ title generator, along with new Fusion titles below

You can use the Text+ generator the same way you use any generator in the Edit page. Simply edit it

into a video track of the Timeline, select it, and open the Inspector to edit and keyframe its numerous

properties to create whatever kind of title you need.

In addition to having many more styling options, the origin of the Text+ generator in a compositing

tool means that it offers many more panels worth of keyframable parameters, along with advanced

animation controls built-in. These include keyframable Write On/Write Off controls, layout and

animation using shapes (options include point, frame, circle, and path), character, word, and line

transforms and animation, advanced shading, and full interlacing support.


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

Four panels of the Text+ title generator,

including Text, Layout, Transform, and Shading


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

Better yet, with the playhead parked on your new Text+ “Fusion Title,” you can open the Fusion

page and access its parameters there too, if you want to start building upon this single generator

to create a multi-layered motion graphics extravaganza.

Opening the Text+ node in the Fusion page reveals it as an actual Fusion page operation

NOTE: If you receive a project with a Text+ title and are missing a specific font used in the title

on your local machine, an overlay will appear on the Viewer informing you of this.

Text+ Viewer Controls

You can perform various editing actions directly on Text+ in the viewer overlay, such as editing text,

displaying a cursor, and selecting text. This capability extends to the viewer within Edit page when the

Fusion overlay is enabled.

The Text+ Viewer controls are activated by selecting Fusion Overlay

(circled) from the Timeline Viewer Overlay menu.

�To enable Text+ Viewer controls: Select Fusion Overlay from the Timeline Viewer Overlay

drop-down menu.

From here you can use your mouse on the text in the Viewer to select and edit text, as well as

move it around in the frame.


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

For more information about the extensive capabilities of the Text+ generator, see Chapter 104,

“Generator Nodes.”