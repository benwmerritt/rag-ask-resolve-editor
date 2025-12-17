---
title: "Animating Tiles and Advanced Layouts"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 657
---

# Animating Tiles and Advanced Layouts

One of the more powerful aspects of the Video Collage effect is the ability to quickly and easily create

animated intros and outros for each tile. These effects can be fully automated over a customizable

duration, or their duration can be manually keyframed. All animations can be automatically eased, and

you can also enable motion blur for the Fly, Shrink, and Rotate animations.

When you use these controls in Create Background mode, the transparent holes through which other

clips in the background show through are animated to “open or close” to reveal the contents. When

used in Create Tile mode, the actual tile and its contents are animated to fly, shrink, rotate, and/or fade

to appear or disappear.

Tile Animation controls let you create automatic

Intro and/or Outro animations.

Additionally, you have the ability to keyframe the Mute, Start and End Column and Row parameters,

Tile Styling and Drop Shadow parameters, and other aspects of tiles in Tiles mode, either individually

or all together.

In particular, the Start and End Column and Row parameters let you create tiles that span multiple

grid positions, and also move tiles from one grid position to another. Without keyframing, this lets you

create more kinds of layouts with asymmetric arrangements of large and small tiles. With keyframing,

you gain the ability to easily create sophisticated grid-based animations to move tiles from position to

position, and to have tiles expand and contract to encompass neighboring tiles in the layout, all with a

minimum of keyframing.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Tile Animation controls let you create automatic Intro and/or Outro animations.

Keep in mind that, when using multiple instances of the Video Collage effect on superimposed clips

in the Timeline, once you’ve defined your overall layout and used Paste Attributes to copy a particular

instance of this effect with your layout to the rest of the clips, you need only keyframe each instance of

each tile within the clip it’s applied to. Furthermore, since Intro and Outro animations are applied to the

entire duration of the clip, you can easily offset each Intro and Outro animation by offsetting the clips

in the Timeline.

TIP: If you change the duration of clips in a stack that are creating a Video Collage effect,

you can use the Synchronize Keyframing controls in Globals mode to offset all keyframes

applied to that instance of the Video Collage effect by the same amount. You could do the

same thing by opening the keyframe track or Curve Editor for all Video Collage parameters in

the Timeline and offsetting them that way, but this provides a quick shortcut.

Video Collage Controls

Here’s a detailed explanation of all the parameters found in the Video Collage effect.

�Workflow: Defines what the output of Video Collage is, depending on how you want to use it.

Create Background: Outputs a frame with holes, behind which you can position individual layers

of video to show through.

Create Tile: Outputs a single tile, transformed and styled to be one element of a multi-tile layout

�Preview Layout: Turning on Preview Layout lets you see a graphical preview of the entire layout,

and how each tile fits together. In Create Tile mode, this lets you configure how you want the

layout to look before you copy the clip and use paste attributes to apply this effect to the rest of

the video layers you want to arrange into a split-screen.

�Globals/Tile buttons: Choose between the Globals controls, which expose controls that let

you adjust the overall layout, and the Tiles controls, which let you choose the currently active

tile and style it.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Layout

These controls appear in Globals mode.

�Columns: Choose how many vertical columns worth of tiles there are.

�Rows: Choose how many horizontal rows worth of tiles there are.

�Stagger Horizontally: Lets you create an offset from one row to the next in a balanced way, so the

rows are all staggered from one another.

�Stagger Vertically: Lets you create an offset from one column to the next in a balanced way, so

the columns are all staggered from one another.

�Rounding: Rounds the edges of each tile in the layout. A value of 0.000 sets the edges to be

square. Increasing rounding increasingly curves the corners of each tile, until a value of 1 sets the

tile to be perfectly round.

Margins and Spacing

These controls appear in Globals mode.

�Left/Right Margins: Alters the spacing from the edge of the frame to the left and right edges of

the group of all tiles. Increasing this parameter makes all tiles progressively more narrow, as they

squeeze in towards the center of the frame.

�Top/Bottom Margins: Alters the spacing from the edge of the frame to the top and bottom edges

of the group of all tiles. Increasing this parameter makes all tiles progressively shorter, as they

squeeze in towards the center of the frame.

�Horizontal and Vertical Offset: These two sliders let you offset the group of all tiles from the

center however you like.

�Horizontal and Vertical Spacing: These two sliders increase or decrease the spacing between

each tile, making them narrower or wider as a result.

Synchronize Keyframing

These controls appear in Globals mode. They’re basically a built-in utility that lets you offset all Globals

and Tiles parameter keyframes that are applied to the current effect, to account for times when you’ve

done elaborate keyframing to create animated split-screen effects, and you then need to change the

duration of the clip this effect is applied to. Instead of forcing you to expose the keyframes of each

parameter in the Timeline in order to move them, these controls let you move all keyframes for all

parameters forward or backward by a particular number of frames, all at once.

�Offset Frames: Lets you specify how many frames you want to offset all keyframes applied to this

effect forward. Negative values move keyframes to the left.

�Apply Keyframing Offset: Executes the offset.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Manage Tiles

These controls appear in Tiles mode.

�Active Tile: This menu serves two purposes. First, it defines which tile the current clip is displayed

within. This becomes important later on when you apply this effect to other superimposed clips

you want to use together in a layout. However, this control also determines which tile you further

customize using the Tile-based controls of the Inspector. If you enable the Open FX Overlay of the

Timeline Viewer, each tile has its own overlay that lets you click a tile in the Viewer to make that

the Active Tile.

�Bring Tile Forward/Send Tile Back: These two buttons let you rearrange the order of tiles in the

Active Tile drop-down menu.

�Manual Tile Management: While this checkbox is turned off (the default), changing the Columns

and Rows parameters automatically updates the Active Tile drop-down menu with one tile per

node on the resulting grid arrangement. Turning this checkbox on lets you Add and Delete tiles

manually, which lets you create more advanced layouts with overlapping tiles and asymmetric

spacing between tiles.

Mute Tiles

These controls appear in Tiles mode. A single checkbox parameter, Mute Tile, lets you enable

and disable the visibility of the active tile. This checkbox is keyframable, so you can animate the

appearance and disappearance of different tiles to create different effects.

Custom Size/Shape

These controls appear in Tiles mode. They let you further customize layouts on a tile-by-tile basis and

can also be used to quickly and easily animate a single tile to move and resize itself around the grid of

the overall layout.

�Start/End Column and Row: These four controls serve two purposes, letting you change a tile’s

position by row and column number, or enlarge a tile to encompass multiple tile row or column

positions (“spanning”). To use these parameters, you must first choose which tile you want to

adjust from the Active Tile drop-down menu. With the tile you want to edit active, you can then

drag the appropriate sliders to create either effect, as explained below.

To change Tile Position: When adjusted together so that the Start and End values are identical,

they let you manually adjust the position of each tile in the grid that’s defined by the number

of rows and columns you’ve set. This is particularly useful when you want to quickly keyframe

animated changes to tile position, in order to jump a tile around the grid of the layout.

To make a tile span multiple positions: Setting the Start and End Row and/or Column parameters

to different values changes the currently active tile to span multiple grid positions in the layout,

making that tile bigger in order to create asymmetric arrangements of larger and smaller tiles. You

can also keyframe these values to easily animate the effect of a tile expanding to occupy more

grid positions, or shrinking from occupying several grid positions to occupying a single position.

Choose how many rows/columns and in which directions you want that tile to span. Note that if you

span multiple rows or columns that have been offset, the resulting tile is enlarged to encompass

the entire rectangular region defined by the outer boundaries of both offset tiles.

�Custom Size/Shape: Turning this checkbox on enables the rest of the controls in this group,

enabling you to set individual scale and rounding for the active tile that’s selected.

�Custom Scale: Lets you adjust the size of the active tile independently of the other tiles.

�Custom Rounding: Lets you adjust the rounding of the active tile independently of the other tiles.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR

Resize Content

These controls appear in Tiles mode. They let you resize the image being fit within each tile to show

exactly what you want shown.

�Pan/Tilt/Zoom: These three sliders let you move and resize the video layer shown inside of the

active tile to fit however you need it to.

�Edge Behavior: These settings allow you to control how the edges of the video layer respond

inside the tile.

Transparent: Any positioning that goes past the edge of the video is transparent, showing the Tile

Color set in the Tile Styling options.

Reflect: Any positioning that goes past the edge of the video mirrors back on itself.

Wrap: Any positioning that goes past the edge of the video repeats itself.

Replicate: Any positioning that goes past the edge of the video shows a duplicate of the edge

stretched to the boundary of the control, essentially filling in the remaining space with the pixels

used at the extreme edges of the video clip.

�Move With Tile: Defines how the image is fit into the tile when the tile size changes due to other

parameters of the Video Collage effect.

Position Only: The video content in the tile only is sized using Pan and Tilt; Zoom is ignored.

Position and Scale: The video content in the tile is sized using Pan, Tilt, and Zoom.

Tile Styling

These controls appear in Tiles mode. They let you add a colored border and adjust the opacity of all

tiles or just the currently active tile. These parameters are animatable.

�Apply to All Tiles: When checked, this applies any changes made in the Tile Styling parameters to

all tiles in the Video Collage, regardless of which tile is currently active.

�Tile Border: This slider controls the width of the tile’s border. It has a possible range of values

from -0.250 to 0.250, where negative numbers expand the size of the border inside the tile, and

positive numbers expand it outside the tile.

�Tile Color: Allows you to chose the background and border color of the tile.

�Tile Opacity: This slider changes the transparency of the tile itself; it does not effect the video clip

inside the tile. The possible ranges are 0.000 (fully transparent) to 1.000 (fully opaque).

Drop Shadow

These controls appear in Tiles mode. They let you add and customize a drop shadow, either to all tiles

or just to the currently active tile. These parameters are animatable.

�Apply to All Tiles: When checked, this applies any changes made in the Drop Shadow parameters

to all tiles in the Video Collage, regardless of which tile is currently active.

�Strength: This slider controls drop shadow transparency. The possible ranges are 0.000 (fully

transparent) to 1.000 (fully opaque).

�Color: Allows you to choose the color of the Drop Shadow.

�Drop Angle: Lets you set the angle that the shadow is cast from. The slider represents 360

degrees of movement from -180.0 to 180.0.

�Drop Distance: Allows you to set the distance that the shadow appears from its source tile. The

possible values are from 0.000 to 0.200.

�Expand: This slider controls how far the shadow expands from its origin. The possible values are

from 0.900 to 1.250.

�Blur: Allows you to control the amount of diffusion of the Drop Shadow. The possible ranges are

0.000 (no blur) to 1.000.


Resolve FX Overview | Chapter 168 Resolve FX Transform

COLOR