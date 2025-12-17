---
title: "Wipe"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 190
---

# Wipe

Wipe transitions are intended to preserve the continuity of motion between two clips. They do this by

matching the overall movement and direction of the subjects across the outgoing and incoming clips.

�Band Wipe: Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the Border

slider to determine the amount of feathering at the edge of the transition. The Reverse checkbox

reverses the direction of the transition. Preset lets you choose one of the following presets:

�Horizontal

�Vertical

�Horizontal Bilinear

�Vertical Bilinear

�Center Wipe: Color sets the color of the border, if there is one. Border sets the width of the

border, in pixels, with 0 creating no border. Angle specifies the angle of the wipe as it emerges

from the middle of the screen. Feather is a checkbox that, when turned on, uses the Border

slider to determine the amount of feathering at the edge of the transition. The Reverse checkbox

reverses the direction of the transition.

�Clock Wipe: Color sets the color of the border, if there is one. Border sets the width of the

border, in pixels, with 0 creating no border. Angle specifies the starting angle of the wipe as it

spins around the center of the screen. The Clockwise checkbox sets the direction of the clock

wipe. Feather is a checkbox that, when turned on, uses the Border slider to determine the

amount of feathering at the edge of the transition. The Reverse checkbox reverses the direction

of the transition.

�Edge Wipe: Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Angle specifies the angle of the wipe as it moves across

the screen. Feather is a checkbox that, when turned on, uses the Border slider to determine the

amount of feathering at the edge of the transition.

�Radial Wipe: Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the Border

slider to determine the amount of feathering at the edge of the transition. The Reverse checkbox

reverses the direction of the transition.

�Spiral Wipe: Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the Border

slider to determine the amount of feathering at the edge of the transition. The Reverse checkbox

reverses the direction of the transition.


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

�Venetian Blind Wipe: Color sets the color of the border, if there is one. Border sets the width

of the border, in pixels, with 0 creating no border. Repeat specifies how many “blinds” appear

within the wipe effect. Angle specifies the angle of this multi-wipe effect. Feather is a checkbox

that, when turned on, uses the Border slider to determine the amount of feathering at the edge

of the transition.

�X Wipe: Color sets the color of the border, if there is one. Border sets the width of the border, in

pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the Border

slider to determine the amount of feathering at the edge of the transition. The Reverse checkbox

reverses the direction of the transition.

User Transitions

Any transition presets you’ve created are stored in the User category. These are the only transitions

that can be deleted.

Fusion Transitions

The Fusion Transitions section of the Transitions panel contains Fusion effects that have been made

into reusable transitions. Fusion Transitions work like any other transition. Once edited into the

Timeline, they can be edited like any other transition, and when selected, they expose customizable

parameters in the Inspector that let you tailor their effect to meet your needs.

However, Fusion Transitions are highly customizable. Simply right-click a Fusion Transition and choose

Open in Fusion Page to expose all of the Fusion nodes that create that transition’s effect, enabling

you to rebuild it to do whatever you need. When you go back to the Edit page, that transition is

automatically saved.

Furthermore, if you know how to create effects in Fusion, you can create your own Transitions by

making Fusion Macros and saving them to the Effects Library, so they appear in the Fusion Transitions

section of the Effects Library.

For more information on how to do this, see Chapter 68, “Node Groups, Macros, and Fusion

Templates,”

�Brightness Flash: Ramps up brightness as it transitions between the two clips. Brightness controls

the luminance level of the flash. Saturation controls the saturation of the flash.

�Camera Shake: Performs a shaking of the frames with color channel separation as a transition.

Shake Speed controls how fast the shaking is. Shake Strength controls how large the shakes are.

Contrast, Brightness and Saturation control their respective parameters on the transition.

�Circles: Transitions between two frames using concentric circles. Circle Color chooses the

transition color. Red, Green, Blue, and Alpha control the relative strengths of each channel. Circle

Thickness lets you adjust the width of the circles.

�Crash Zoom: Performs two rapid zoom-ins on the clips as a transition.

�Cross Dissolve: Dissolves between two clips. This is the base Fusion transition to use if you want

to create your own custom transition in Fusion.

�Drop Warp: Creates a virtual water drop to transition between the two clips. Warp Scale adjusts

the amount of image warping to the drop.

�Fall and Bounce: The trailing clip falls into the frame and bounces as a transition. Fall Angle

controls the direction of the fall-in.


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

�Film Strip: Performs a zoom of a moving virtual film strip as a transition between the two clips.

Color selects the color of the film base. Red, Green, Blue, and Alpha control the relative strengths

of each channel.

�Flip 3D: Performs a simple rotation between the sides of a plane as a transition.

�Foreground Wipe: Performs a zoomed-in column wiping across the frame as a transition. Invert

Wipe changes the direction of the wipe. Shadow Softness controls the “depth” of the column.

Border Width controls the width of the column.

�Glitch: Performs a digital breakup of the image as a transition. Best used in very short durations of

a few frames.

�Noise Dissolve: Uses Fusion’s FastNoise tool as a transition. You can store up to 6 versions of

this transition. Mix controls the dissolve’s progress through the frame. Type controls the direction

the noise emanates from. Softness controls the feathering of the border between the two clips.

Animation controls the speed of the noise changes. Border allows you to set a colored border on

the boundary of the noise between the two clips.

�Paint On: This performs virtual paint brush strokes as a transition. Shadow Blend controls the

“depth” of the strokes. This transition is best used in longer durations.

�Pan (Down, Left, Right, Up): This performs mirrored images in motion as a transition. The direction

of the motion is respective of which transition you choose.

�Rotate: This performs a combination of counterclockwise 180 degree rotation and

dissolve as a transition.

�Rotate 90: This performs a combination of counterclockwise 90 degree rotation and

dissolve as a transition.

�Round and Down: This performs a counterclockwise rotation around a central pivot point as it

dissolves between two clips.

�Slice Push: Performs a transition consisting of several columns sliding out and pushing across

the two clips. Slices control the number of columns. Angle lets you set the angle of the columns.

Shadow sets the strength of the column’s drop shadow. Shadow Softness controls the spread of

the drop shadow. Shadow Offset controls the angle of the shadow.

�Slide (Down, Left, Right, Up): Performs a mirrored slide in the direction indicated. The Curve

control lets you set the following animation curve options:

�Linear

�Easing

�Custom

�Tunnel of Light: Performs a glowing transition where the first clip is sucked into a point, then the

second clip expands from that same point. Contrast lets you determine the contrast of the light

rays. Glow Gain controls the glow’s brightness. Glow Size controls the amount of glow. Glow Red,

Green, and Blue allow you to change the color of the glow.

�Warp: Performs a warping transition like a water circling a drain between the two clips.

�Zoom In: Performs a transition that zooms in and blends the two clips together. Zoom Scale

controls the strength of the zoom (a negative value zooms out instead of in). Zoom Center allows

you to set the point around which the zoom occurs. The Curve control lets you set the following

animation curve options:

�Linear

�Easing

�Custom

�Zoom In and Out: Performs a transition that zooms in on the first clip blended with a zoom out on

the second clip. Zoom Scale controls the strength of the zoom. Zoom Center allows you to set the

point around which the zoom occurs.


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

Resolve FX Transitions

Resolve FX Transitions are stylized graphical transitions that are more computationally intensive than

the standard wipes and dissolves.

Burn Away Transition

This transition replicates the visual of a film print burning up in the projector. Use this transition to

achieve a classically retro effect, or to strike terror into the hearts of projectionists everywhere.

Burn Away transition showing two pirates concerned about the state of their release print

The Burn Away effect has the following parameters:

Progression

This set of controls affects the type of movement the burn takes as it passes through the frame.

�Motion: Allows you to pick a type of burning effect. Each option reveals different parameters.

Directional: The burn moves linearly from one edge of the frame to another. This setting replicates

the film being torn away by the take-up reel as it burns. In this mode, the OFX overlay in the

Viewer lets you choose the direction.

Hotspots: The burn erupts from one or more central points. This setting replicates the film

jamming in front of a projector bulb and melting away. In this mode, the OFX overlay in the Viewer

lets you move the burn points directly in the Viewer.

Path: Creates a curved path that the burn follows. This setting allows you to specify the burn

direction precisely, to account for elements in the frame that you want to burn first. In this mode,

the OFX overlay in the Viewer lets you add points to a spline with which to create any curved

motion path you want the effect to use.

�Angle: (Directional Only) The angle that the burn moves along. You can also change this in the

Viewer directly in Open FX Overlay mode.

�Number of Hotspots: (Hotspots Only) The number of points that the burn erupts from.

The possible values are from 1 to 8.

�Randomize Hotspots: (Hotspots Only) Will pick a random distribution of the hotspots in the frame.

�Number of Points: (Path Only) The number of points on the onscreen curve control. The range is

from 2 to 5. These points can be manipulated directly in the Viewer in Open FX Overlay mode.


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

Adjust Timing

This set of parameters allows you to control the start and end progression of the burn.

�Adjust Start: Adjusts how far along in the transition the effect starts. Values are

from -1.000 to 1.000.

�Adjust End: Adjusts how far along in the transition the effect ends. Values are

from 0.000 to 2.000.

Edge

These controls let you adjust the qualities of the edge of the film as it burns.

�Raggedness: How rough the edge of the burn is. Values are from 0.000 (perfectly flat)

to 1.000 (extremely rough).

�Scale: The scale of the raggedness. Values are from 1.00 to 10.00.

Appearance

These controls adjust the look and color of the burn as it moves through the transition.

�Melt: Controls the amount of distortion in the image as it burns away. Values are

from 0.000 to 1.000.

�Char: Controls the amount of darkened charring along the edge. Values are from 0.000 to 1.000.

�Char Color: Lets you select the color of the Char effect.

�Burn: Lets you set the thickness of the burn effect. Values are from 0.000 (no burn)

to 1.000 (maximum thickness).

�Burn Hue: Lets you select the hue of the Burn effect.

�Burn Sat: Lets you select the intensity of the color of the Burn effect.

�Burn Brightness: Lets you set the brightness of the Burn effect. At lower values, the burning edge

assumes a motley, irregular effect. Values are from 0.000 to 1.000.

�Glow Brightness: Lets you control the intensity of a glow effect emanating from the Burn effect.

Values are from 0.000 to 2.000.

�Glow Spread: Lets you control the width of the glow effect. Values are from 0.000 to 2.000.

�Ash: Controls how much ash trails behind the burn as it moves through the frame.

Values are from 0.000 to 1.000.

�Ash Color: The color of the Ash parameter.

DCTL Transition

DCTL (DaVinci Color Transform Language)-based transitions are now supported in DaVinci Resolve.

See the DaVinci Resolve Developer Documentation in the help menu for more details.


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT