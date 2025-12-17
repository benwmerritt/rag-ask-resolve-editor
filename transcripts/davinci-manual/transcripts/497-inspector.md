---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 497
---

# Inspector

The Tracker node Trackers tab

Trackers Tab

The Trackers tab contains controls for creating, positioning, and initiating tracking operations.

After tracking, offset controls are used to improve the alignment of the image following the track.

Track Buttons

There are four buttons to initiate tracking, and one button in the middle used to stop a track in

progress. These buttons can track the current pattern forward or backward in time. Holding the pointer

over each button displays a tooltip with the name of each button.

The buttons operate as follows:

�Track Reverse: Clicking this button causes all active trackers to begin tracking, starting at the end

of the render range and moving backward through time until the beginning of the render range.

�Track Reverse From Current Time: Clicking this button causes all active trackers to begin

tracking, starting at the current frame and moving backward through time until the beginning of

the render range.

�Stop Tracking: Clicking this button or pressing ESC stops the tracking process immediately.

This button is active only when tracking is in process.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

�Track Forward From Current Time: Clicking this button causes all active trackers to begin

tracking, starting at the current frame and moving forward through time until the end of

the render range.

�Track Forward: Clicking this button causes all active trackers to begin tracking, starting at the first

frame in the render range and moving forward through time until the end of the render range.

Tracking Behavior Controls

The following controls all affect how trackers adapt to changing patterns, how the resulting track path

is defined, and how many keyframes are generated.

Frames Per Path Point

This slider determines how often the Tracker sets a keyframe on the path. The default is 1, which sets a

keyframe on the tracked path at every frame.

Increasing the value causes the tracked path to be less accurate. This may be desirable if the track is

returning fluctuating results, but under normal circumstances, leave this control at its default value.

TIP: If the project is field rendered, a value of 1 sets a keyframe on every field. Since the

Tracker is extremely accurate, this will result in a slight up-and-down jittering due to the

position of the fields. For better results when tracking interlaced footage in Field mode, set

the Frames Per Path Point slider to a value of 2, which results in one keyframe per frame of

your footage.

Adaptive Mode

Fusion is capable of reacquiring the tracked pattern, as needed, to help with complex tracks. This

menu determines the Adaptive tracking method.

�None: When set to None, the tracker searches for the original pattern in each frame.

�Every Frame: When set to Every Frame, the tracker reacquires the pattern every frame. This helps

the Tracker compensate for gradual changes in profile and lighting over time.

�Best Match: When set to Best Match, the tracker compares the original selected pattern to the

pattern acquired at each frame. If the variation between the two patterns exceeds the threshold

amount defined by the Match Tolerance control, the tracker does not reacquire the pattern on that

frame. This helps to avoid Tracker drift caused by transient artifacts that cross the pattern’s path

(such as a shadow).

Path Center

This menu determines how the Tracker behaves when repositioning a pattern. This menu is particularly

useful when a pattern leaves the frame or changes so significantly that it can no longer be tracked.

�Pattern Center: When Pattern Center is selected in the menu, the tracked path continues from the

center of the new path. This is appropriate when replacing an existing path entirely.

�Track Center (append): When Track Center (append) is selected in the menu, the path tracked by

a new pattern will be appended to the existing path. The path created is automatically offset by

the required amount. This setting is used to set a new tracking pattern when the original pattern

moves out of the frame or gets obscured by other objects. This technique work bests if the new

pattern is located close to the position of the original pattern to avoid any problems with parallax

or lens distortion.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Tracker List

A Tracker node can track multiple patterns. Each tracker pattern created in the current Tracker node is

managed in the Tracker List.

Tracker List

The Tracker List shows the names of all trackers created.

�Each tracker pattern appears in the list by name, next to a small checkbox. Clicking the name of

the tracker pattern will select that tracker pattern.

�The controls below the list will change to affect that tracker pattern only. Click a selected tracker

pattern once to rename the tracker pattern to something more descriptive.

�Clicking the checkbox changes the state of the tracker.

Tracker States

�Enabled (black checkbox): An enabled pattern will re-track each time the track is initiated.

Its path data is available for use by other nodes, and the data is available for Stabilization and

Corner Positioning.

�Suspended (white circle): A Suspended pattern does not re-track when the track is initiated.

The data is locked to prevent additional changes. The data from the path is still available for

other nodes, and the data is available for advanced Tracking modes like Stabilization and

Corner Positioning.

�Disabled (clear): A Disabled pattern does not create a path when tracking is initialized, and its

data is not available to other nodes or for advanced Tracking operations like Stabilization and

Corner Positioning.

Three tracking patterns from top to bottom:

enabled, suspended, and disabled

Add/Delete Tracker

Use these buttons to add or delete IntelliTrack or Point trackers from your Tracker List.

Show

This menu selects what controls are displayed in the Tracker node controls. They do not affect the

operation of the tracker; they only affect the lower half of the Inspector interface.

�Selected Tracker Details: When Selected Tracker Details is chosen, the controls displayed

pertain only to the currently selected tracker. You will have access to the Pattern window and the

Offset sliders.

�All Trackers: When All Trackers is selected, the pattern window for each of the added tracking

patterns is displayed simultaneously below the Tracker List.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Left Pattern Display

The pattern display has two side-by-side image windows and a series of status bars. The window on

the left shows the pattern initially selected, while the one on the right shows a real-time display of the

current pattern as tracking progresses.

As the onscreen controls move while tracking, the display in the leftmost window updates to show

the pattern. As the pattern moves, the vertical bars immediately to the right of the image indicate the

clarity and contrast of the image channels.

The best channel or channels get selected for tracking based on clarity. These channels have a

gray background in the vertical bar representing that channel. You can use the automatic tracking or

override the selection and choose the channel by selecting the button beneath the channel to track.

Tracker pattern display

Under normal circumstances, the channel selected shows in the pattern display. If the selected

channel is blue, then a grayscale representation of the blue channel for the pattern appears.

The image is represented in color only when you activate the Full Color button.

Override this behavior by selecting the Show Full Color button beneath the pattern display instead of

the Show Selected Channel button.

TIP: Because Fusion looks for the channel with the highest contrast automatically, you might

end up tracking a noisy but high-contrast channel. Before tracking, it’s always a good idea to

zoom in to your footage and check the RGB channels individually.

Right Pattern Display

The pattern display on the right indicates the actual pattern acquired for tracking. This display is

black until tracking the selected pattern for the first time. The pattern display becomes active during

tracking, displaying the pattern that Fusion acquires from frame to frame.

As the tracking occurs, the pattern from each frame accumulates into a Flipbook, which can be played

back in the pattern window after tracking by using the transport controls at the bottom of the window.

While the track is progressing, the vertical bar immediately to the right of the pattern shows how

confident Fusion is that the current pattern matches the initially selected pattern. A green bar indicates

a high degree of confidence that the current pattern matches the original, a yellow bar indicates less

certainty, and a red bar indicates extreme uncertainty.

After tracking, the pattern display shows a small Flipbook of the track for that pattern to help identify

problem frames for the track.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Tracker Sizes

In addition to onscreen controls, each tracker has a set of sizing parameters that let you adjust the

pattern and search box.

�Pattern Width and Height: Use these controls to adjust the width and height of the selected

tracker pattern manually. The size of the tracker pattern can also be adjusted in the viewer, which

is the normal method, but small adjustments are often easier to accomplish with the precision of

manual controls.

�Search Width and Height: The search area defines how far Fusion will look in the image from

frame to frame to reacquire the pattern during tracking. As with the Pattern Width and Height, the

search area can be adjusted in the viewer, but you may want to make small adjustments manually

using these controls.

Tracked Center

This positional control indicates the position of the tracker’s center. To remove a previously

tracked path from a tracker pattern, right-click this parameter and select Remove Path from the

contextual menu.

X and Y Offset

The Offset controls help to create a track for objects that may not provide very well defined or reliable

patterns. The Offset controls permit the tracking of something close to the intended object instead.

Use these Offsets to adjust the desired position of the path, while the tracker pattern rectangle is

positioned over the actual tracking location.

The Offset can also be adjusted directly in the viewer by activating the Offsets button in the

viewer toolbar.

The tracker offset icon in the

upper left of the viewer is used

to offset the tracking pattern

from the intended object.

Operation Tab

While the Trackers tab controls let you customize how the Tracker node analyzes motion to create

motion paths, the Operation tab puts the analyzed motion data to use, performing image transforms of

various kinds.

The Tracker node is capable of performing a wide variety of functions, from match moving an object

into a moving scene, smoothing out a shaky camera movement, or replacing the content of a sign. Use

the options and buttons in the Operation tab to select the function performed by the Tracker node.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

The Tracker Operation tab

Operation Menu

The Operation menu contains four functions performed by the Tracker. The remaining controls in this

tab fine-tune the result of this selection.

�None: The Tracker performs no additional operation on the image beyond merely locating and

tracking the chosen pattern. This is the default mode, used to create a path that will then drive

another parameter on another node.

�Match Move: When only the orange background input is connected, this mode stabilizes the

image. When a foreground image is connected to the green foreground input, the foreground

image matches the position, rotation, and scaling based on the tracking patterns. Stabilizing and

match move require a minimum of one tracking pattern to determine position, and two or more to

determine scaling and rotation.

�Corner Positioning: The Corner Positioner mode tracks the four corners of a rectangular object

and replaces the contents with a new image. This function requires a minimum of four tracking

patterns. If there are not enough tracking patterns, new tracking patterns are added until the total

equals four.

�Perspective Positioning: This mode is the inverse of the Corner Positioning mode. Rather than

replacing the contents of the rectangle, the four trackers are mapped to the four corners of the

image. This is generally used to remove perspective from an image. Like the Corner Positioning

mode, this mode requires four tracking patterns, which automatically get added if there are

fewer patterns.

Additional Layering Controls

When you choose any operation other than None, a series of additional controls appear.

Merge

The Merge control determines what is done (if anything) with the image provided to the green

Foreground input of the Tracker. This menu appears when the operation is set to anything other

than None.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

�BG Only: The foreground input is ignored; only the background is affected. This is used primarily

when stabilizing the background image.

�FG Only: The foreground input is transformed to match the movement in the background, and this

transformed image is passed through the Tracker’s output. This Merge technique is used when

match moving one layer’s motion to another layer’s motion.

�FG Over BG: The foreground image is merged over the background image, using the Merge

method described by the Apply Mode control that appears.

�BG Over FG: The background is merged over the foreground. This technique is often used when

tracking a layer with an Alpha channel so that a more static background can be applied behind it.

Apply Mode and Operator Menus

This menu provides a variety of options that determine how the two layers should be combined.

The options in this menu are identical to those found in the Merge node.

�Apply Modes: The Apply Mode setting determines the math used when blending or combining

the foreground and background pixels.

Normal: The Default merge mode uses the foreground’s alpha channel as a mask to determine

which pixels are transparent and which are not. When this is active, another menu shows possible

operations, including Over, In, Held Out, Atop, and XOr.

Screen: Screen merges the images based on a multiplication of their color values. The alpha

channel is ignored, and layer order becomes irrelevant. The resulting color is always lighter.

Screening with black leaves the color unchanged, whereas screening with white will always

produce white. This effect creates a similar look to projecting several film frames onto the same

surface. When this is active, another menu shows possible operations, including Over, In, Held

Out, Atop, and XOr.

Dissolve: Dissolve mixes two image sequences together. It uses a calculated average of the two

images to perform the mixture.

Multiply: Multiplies the values of a color channel. This will give the appearance of darkening

the image as the values are scaled from 0 to 1. White has a value of 1, so the result would be the

same. Gray has a value of 0.5, so the result would be a darker image or, in other words, an image

half as bright.

Overlay: Overlay multiplies or screens the color values of the foreground image, depending

on the color values of the background image. Patterns or colors overlay the existing pixels

while preserving the highlights and shadows of the color values of the background image.

The background image is not replaced but is mixed with the foreground image to reflect the

original lightness or darkness of the background image.

Soft Light: Soft Light darkens or lightens the foreground image, depending on the color values of

the background image. The effect is similar to shining a diffused spotlight on the image.

Hard Light: Hard Light multiplies or screens the color values of the foreground image, depending

on the color values of the background image. The effect is similar to shining a harsh spotlight on

the image.

Color Dodge: Color Dodge uses the foreground’s color values to brighten the background

image. This is similar to the photographic practice of dodging by reducing the exposure of an

area of a print.

Color Burn: Color Burn uses the foreground’s color values to darken the background image. This

is similar to the photographic practice of burning by increasing the exposure of an area of a print.

Darken: Darken looks at the color information in each channel and selects the background or

foreground image’s color value, whichever is darker, as the result color. Pixels lighter than the

merged colors are replaced, and pixels darker than the merged color do not change.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Lighten: Lighten looks at the color information in each channel and selects the background or

foreground image’s color values, whichever is lighter, as the result color value. Pixels darker than

the merged color are replaced, and pixels lighter than the merged color do not change.

Difference: Difference looks at the color information in each channel and subtracts the foreground

color values from the background color values or the background from the foreground, depending

on which has the greater brightness value. Merging with white inverts the color. Merging with

black produces no change.

Exclusion: Exclusion creates an effect similar to but lower in contrast than the Difference mode.

Merging with white inverts the base color values. Merging with black produces no change.

Hue: Hue creates a result color with the luminance and saturation of the background color values

and the hue of the foreground color values.

Saturation: Saturation creates a result color with the luminance and hue of the base color and the

saturation of the blend color.

Color: Color creates a result color with the luminance of the background color value and the hue

and saturation of the foreground. This preserves the gray levels in the image and is useful for

coloring monochrome images.

Luminosity: Luminosity creates a color with the hue and saturation of the background color

and the luminance of the foreground color. This mode creates an inverse effect from that of

the Color mode.

�Operator Modes: This menu is used to select the Operation Mode of the merge. It determines

how the foreground and background are combined to produce a result. This drop-down menu is

visible only when the Merge node’s Apply Mode is set to either Normal or Screen.

NOTE: For an excellent description of the math underlying the Operation modes,

read “Compositing Digital Images,” Porter, T., and T. Duff, SIGGRAPH 84 proceedings,

pages 253-259. Essentially, the math is as described below.

TIP: Some modes not listed in the Operator drop-down menu (Under, In, Held In, Below)

are easily obtained by swapping the foreground and background inputs and choosing a

corresponding mode.

The formula used to combine pixels in the merge is always fg * x + bg * y. The different operations

determine exactly what x and y are, as shown in the description for each mode.

The Operator modes are as follows:

�Over: The Over mode adds the foreground layer to the background layer by replacing the

pixels in the background with the pixels from the Z wherever the foreground’s alpha channel is

greater than 1.

x = 1, y = 1-[foreground Alpha]

�In: The In mode multiplies the alpha channel of the background input against the pixels in

the foreground. The color channels of the foreground input are ignored. Only pixels from the

foreground are seen in the final output. This essentially clips the foreground using the mask from

the background.

x = [background Alpha], y = 0


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

�Held Out: Held Out is essentially the opposite of the In operation. The pixels in the foreground

image are multiplied against the inverted alpha channel of the background image. You can

accomplish exactly the same result using the In operation and a Matte Control node to invert the

matte channel of the background image.

x = 1-[background Alpha], y = 0

�ATop: ATop places the foreground over the background only where the background has a matte.

x = [background Alpha], y = 1-[foreground Alpha]

�XOr: XOr combines the foreground with the background wherever either the foreground or the

background have a matte, but never where both have a matte.

x = 1-[background Alpha], y = 1-[foreground Alpha]

�Subtractive/Additive: This slider controls whether Fusion performs an Additive merge, a

Subtractive merge, or a blend of both. This slider defaults to Additive merging for most operations,

assuming the input images are premultiplied (which is usually the case). If you don’t understand

the difference between Additive and Subtractive merging, here’s a quick explanation:

�An Additive merge is necessary when the foreground image is premultiplied, meaning that the

pixels in the color channels have been multiplied by the pixels in the alpha channel. The result is

that transparent pixels are always black since any number multiplied by 0 always equals 0. This

obscures the background (by multiplying with the inverse of the foreground alpha), and then

simply adds the pixels from the foreground.

�A Subtractive merge is necessary if the foreground image is not premultiplied. The compositing

method is similar to an Additive merge, but the foreground image is first multiplied by its alpha to

eliminate any background pixels outside the alpha area.

In most software applications, you will find the Additive/Subtractive option displayed as a simple

checkbox. Fusion lets you blend between the Additive and Subtractive versions of the merge

operation, which is occasionally useful for dealing with problem composites with edges that are

calling attention to themselves as too bright or too dark.

For example, using a Subtractive setting on a premultiplied image may result in darker

edges. Using an Additive setting with a non-premultiplied image may result in lightening

the edges. By blending between Additive and Subtractive, you can tweak the edge

brightness to be just right for your situation.

Filter Method (Match Move)

Determines which filter to use to handle image transforms made using the Tracker node. This menu

appears only when the Operation Mode is set to Match Move.

�Box: This is a simple interpolation resize of the image.

�Linear: This uses a simplistic filter, which produces relatively clean and fast results.

�Quadratic: This filter produces a nominal result. It offers a good compromise between

speed and quality.

�Cubic: This produces better results with continuous-tone images but is slower than Bi‑Cubic.

If the images have fine detail in them, the results may be blurrier than desired.

�Catmull-Rom: This produces good results with continuous-tone images that are resized down.

It produces sharp results with finely detailed images.

�Gaussian: This is very similar in speed and quality to Bi-Cubic.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

�Mitchell: This is similar to Catmull-Rom but produces better results with finely detailed images.

It is slower than Catmull-Rom.

�Lanczos: This is very similar to Mitchell and Catmull-Rom but is a little cleaner and also slower.

�Sinc: This is an advanced filter that produces very sharp, detailed results; however, it may produce

visible “ringing” in some situations.

�Bessel: This is similar to the Sinc filter but may be slightly faster.

Edges

This menu selects how the revealed edges are handled when the image is moved to match position

and scaling.

�Black Edges: Out-of-frame edges revealed by Stabilization are left black.

�Wrap: Portions of the image moved off frame to one side are used to fill edges that are revealed

on the opposite side.

�Duplicate: The last valid pixel on an edge is repeated to the edge of the frame.

�Mirror: Image pixels are mirrored to fill to the edge of the frame.

Position, Rotation, and Scaling Checkboxes (Match Move)

The Position, Rotation, and Scaling checkboxes appear only when the mode is set to Match Move.

They determine what components of motion that Stabilization will attempt to correct in the image.

For example, if only the Position checkbox is selected, no attempt will be made to correct for Rotation

and Scaling in the image.

Flatten Transformation (Match Move)

This checkbox appears only when the mode is set to Match Move. Like most transformations in Fusion,

Stabilization is concatenated with other sequential transformations by default. Selecting this checkbox

will flatten the transform, breaking any concatenation taking place and applying the transform

immediately.

Mapping Type

The Mapping Type control appears only in the Corner Positioning mode. There are two options

in the menu:

�Bi_Linear: The first method is Bi-Linear, where the foreground image is mapped into the

background without any attempt to correct for perspective distortion. This is identical to how

previous versions of Fusion operated.

�Perspective: The foreground image is mapped into the background taking perspective distortion

into account. This is the preferred setting since it maps better to the real world than the older

Bi‑Linear setting.

Corner Selector (Corner or Perspective Positioning)

When the operation of the Tracker is set to either Corner or Perspective Positioning modes, four drop-

down menus appear. These options choose which trackers map to each of the four corners of the

rectangle. This is useful when a Tracker has more than four patterns selected, and you must choose

which patterns the positioners use.

Rotate Clockwise and Counter-Clockwise Buttons (Corner or Perspective Positioning)

These controls appear only when the operation of the Tracker is set to either Corner or Perspective

Positioning modes. They are used to rotate the foreground image by 90 degrees before it is applied to

the background.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Stabilize Settings

The Tracker node automatically outputs several steady and unsteady position outputs to which

other controls in the Node Editor can be connected. The Stable Position output provides X and Y

coordinates to match or reverse motion in a sequence. These controls are available even when the

operation is not set to Match Move, since the Stable Position output is always available for connection

to other nodes.

Match Move Settings

These settings determine how tracking data is correlated with the reference pattern

for making transforms.

Pivot Type

The Pivot type menu determines how the anchor point for rotation is selected.

�Tracker Average: Averages the location based on the tracking points.

�Selected Tracker: Provides a menu where one of the current trackers can be selected

as the pivot point.

�Manual: Displays X and Y position number fields where you can manually position the pivot points.

Reference

The Reference mode determines the “snapshot frame” based on the frame where the pattern is first

selected. All Stabilization is intended to return the image back to that reference.

�Select Time: Lets you select the current frame.

�Start: The Snapshot Frame is determined to be the first frame in the tracked path. All Stabilization

is intended to return the image back to that reference.

�Start and End: The Start and End Reference mode is somewhat different from all other Reference

modes. Where the others are intended to take a snapshot frame to which all stabilization returns,

immobilizing the image, the Start and End mode is intended to smooth existing motion, without

removing it. This mode averages the motion between the Start and End of the path, drawing a

straight line between those points.

When this mode is active, it reveals the Reference Intermediate Points control. Increasing the value

of this control increases the number of points in the path used by the Reference, smoothing the

motion from a straight line between Start and End without making it wholly linear.

�End: The Snapshot Frame is determined to be the last frame in the tracked path. All Stabilization is

intended to return the image back to that reference.

TIP: By default, the Tracker displays a single displacement path of the tracked data in

the Spline Editor. To view X and Y paths of the tracked points in the Spline Editor, go to

Preferences > Globals > Splines.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION

Display Options Tab

The Display Options tab lets you customize the look of onscreen controls in the viewer.

The Tracker Display Options tab

Show Pattern Names

This option defines whether the Tracker’s pattern names will be displayed in the viewer. Switch it off to

see the pattern rectangle instead.

Enlarged Pattern on Dragging

This option defines whether there is a magnified thumbnail view when positioning

the pattern rectangle.

Enlargement Scale

The zoom factor that is used when positioning the pattern rectangle when the above

option is activated. TIP: The outputs of a tracker (seen in the Connect to… menu) can also be used by

scripts. They are:

�SteadyPosition: Steady Position

�UnsteadyPosition: Unsteady Position

�SteadyAxis: Steady Axis

�SteadySize: Steady Size

�UnsteadySize: Unsteady Size

�SteadyAngle: Steady Angle

�UnsteadyAngle: Unsteady Angle

�Position1: Tracker 1 Offset position

�PerspectivePosition1: Tracker 1 Perspective Offset position

�PositionX1: Tracker 1 Offset X position (3D Space)

�PositionY1: Tracker 1 Offset Y position (3D Space)

�PerspectivePositionX1: Tracker 1 Perspective Offset X position (3D Space)

�PerspectivePositionY1: Tracker 1 Perspective Offset Y position (3D Space)

�SteadyPosition1: Tracker 1 Steady Position

�UnsteadyPosition1: Tracker 1 Unsteady Position (likewise for the 2nd, 3rd, and so on)

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Tracking nodes. These common controls

are described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 119 Tracking Nodes

FUSION