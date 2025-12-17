---
title: "Creating Transition Presets"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 189
---

# Creating Transition Presets

If you find yourself using a particular transition that’s customized in a particular way over and over

in your work, you can create a Preset of that transition for easy recall. Once saved, Presets can be

favorited or set to be the Standard Transition to make them more easily available.

To save a transition preset for future use:


Add a transition to the Timeline, then double-click it to open it in the Inspector to adjust its settings

to be the way you need it to be.


(Optional) if necessary, open the transition’s Curve Editor and set the type of curve you want the

transition to have. A customized transition curve will be saved inside of that transition’s preset.


Right-click on the transition you want to save, and choose Create Transition Preset.


Type a name for the transition preset in the dialog that appears, and click OK. That transition is

saved to the User section at the bottom of the Toolbox Video Transitions area, where you can

apply it just like any other transition.

To remove a transition preset:

Right-click any preset and choose Delete Transition Preset.

Changing Transitions to

Fusion Compositions

If you need to create a more complex transition than you can get from the Inspector, it is now possible

to change any transition to a Fusion Composition on the Edit page Timeline.

To convert a Resolve transition to a Fusion composition:


Add a transition between two clips on your Timeline.


Right-click on the transition and select “Convert to Fusion Cross Dissolve.”


Right-click on the transition again and select “Open in Fusion Page.”

A new Fusion composition opens with the base Cross Dissolve nodes and tools already set. You now

can use all of the powerful tools in the Fusion page to customize your transition.

The node tree you start with after converting a transition to a Fusion cross dissolve


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

Video Transitions

The following are transitions that are available within DaVinci Resolve by default, along with the

parameters that are available for each of them from the Inspector:

Dissolve

A dissolve in the visual language of film generally denotes a passage of time or place. It indicates to

your audience that one scene has ended and another is beginning.

Additive Dissolve: Start Ratio lets you adjust how far along the transition is when it first begins. End

Ratio lets you adjust how far the transition gets at the very end.

Blur Dissolve: Horizontal/Vertical Strength sets how much blur is performed in the X and Y dimensions

during the course of this transition. Start Ratio lets you adjust how far along the transition is when it

first begins. End Ratio lets you adjust how far the transition gets at the very end.

Cross Dissolve: Style lets you choose what type of cross dissolve you want; choices include: Video,

Film, Additive, Subtractive, Highlights, Shadows. Start Ratio lets you adjust how far along the transition

is when it first begins. End Ratio lets you adjust how far the transition gets at the very end.

Dip to Color Dissolve: Start Ratio lets you adjust how far along the transition is when it first begins.

End Ratio lets you adjust how far the transition gets at the very end. Color lets you choose what color

the dissolve dips to at the midpoint.

Non-Additive Dissolve: Start Ratio lets you adjust how far along the transition is when it first begins.

End Ratio lets you adjust how far the transition gets at the very end.

Smooth Cut: A special-purpose transition designed to make short jump cuts in the middle of a clip

less noticeable. This is done by using AI powered Speed Warp processing to match the same features

on either side of a cut in order to automatically morph a subject from one position to another over the

duration of the transition.

�A Mode drop-down menu provides two options: Faster and Better. The Better option is default,

with excellent quality and the capability of preserving the motion of subjects for the duration of the

transition. The Faster option morphs between stills of the outgoing and incoming frames. In most

practical circumstances, the Better mode will give you a superior result, but certain cuts or effects

may be better addressed with the Faster option.

The Smooth Cut effect works best on clips such as sit-down interviews and close-up head shots

with a minimum of background and subject motion, and where the subject’s position on either

side of the cut is not significantly different. A good example of when Smooth Cut is effective is

when you’re cutting pauses, partial repeats, filler sounds such as “um” or “you know,” or other

speech disfluencies out of an interview clip to tighten the dialog, and you want to eliminate the

little “jump” that occurs at the cut without having to cut away to B-roll. Applying a short two or four

frame Smooth Cut transition to the edit can make this kind of edit invisible, as long as the speaker

doesn’t change position significantly during the cut. The more motion there is in the background

of the shot, and the more the speaker changes position, the harder it will be to get a useful result

using Smooth Cut. Although the default duration for any transition is one second, you’ll find that

Smooth Cut transitions work much better when they’re short; 2- to 6-frame Smooth Cut transitions

often work best to disguise jump cuts.

NOTE: As of DaVinci Resolve 20, Smooth Cut uses a new AI powered Speed Warp to

perform the transition. If you would prefer to revert to the older optical flow version, simply

uncheck the Speed Warp box in the Transition inspector.


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

Iris

Irises are directional transitions that are commonly used to both call attention to a specific part of the

frame and indicate to the audience that one scene has ended and another begun. Irises were widely

used in the silent film era instead of the more technically complicated dissolve.

�Arrow Iris: Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Aspect Ratio allows you to change the proportions of the

shape. Offset to center lets you alter the center point at which this transition is positioned. Rotation

changes the angle of the iris. Feather is a checkbox that, when turned on, uses the Border slider to

determine the amount of feathering at the edge of the transition. The Reverse checkbox reverses

the direction of the transition.

Preset lets you choose one of the following presets:

�Arrow Up

�Arrow Down

�Arrow Left

�Arrow Right

�Cross Iris: Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Offset to Center identifies the center point at which the cross

wipe begins, as X and Y coordinates on the screen. Feather is a checkbox that, when turned on,

uses the Border slider to determine the amount of feathering at the edge of the transition. The

Reverse checkbox reverses the direction of the transition.

�Diamond Iris: Color sets the color of the border, if there is one. Border sets the width of the

border, in pixels, with 0 creating no border. Offset to Center identifies the center point at which the

diamond-shaped wipe begins, as X and Y coordinates on the screen. Feather is a checkbox that,

when turned on, uses the Border slider to determine the amount of feathering at the edge of the

transition. The Reverse checkbox reverses the direction of the transition.

�Eye Iris: Color sets the color of the border, if there is one. Border sets the width of the border, in

pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the Border

slider to determine the amount of feathering at the edge of the transition. The Reverse checkbox

reverses the direction of the transition.

�Hexagon Iris: Color sets the color of the border, if there is one. Border sets the width of the

border, in pixels, with 0 creating no border. Aspect Ratio allows you to change the proportions

of the shape. Offset to center lets you alter the center point at which this transition is positioned.

Rotation changes the angle of the iris. Feather is a checkbox that, when turned on, uses

the Border slider to determine the amount of feathering at the edge of the transition. The

Reverse checkbox reverses the direction of the transition. Preset lets you choose one of the

following presets:

�Hexagon

�Hexagon Vertical

�Oval Iris: Color sets the color of the border, if there is one. Border sets the width of the border, in

pixels, with 0 creating no border. Offset to Center identifies the center point at which this circular

wipe begins, as X and Y coordinates on the screen. Oval Ratio changes the aspect ratio of the

oval, making it either wider or taller. Feather is a checkbox that, when turned on, uses the Border

slider to determine the amount of feathering at the edge of the transition. The Reverse checkbox

reverses the direction of the transition.

�Pentagon Iris: Color sets the color of the border, if there is one. Border sets the width of the

border, in pixels, with 0 creating no border. Aspect Ratio allows you to change the proportions

of the shape. Offset to center lets you alter the center point at which this transition is positioned.

Rotation changes the angle of the iris. Feather is a checkbox that, when turned on, uses the

Border slider to determine the amount of feathering at the edge of the transition. The Reverse


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

checkbox reverses the direction of the transition. Preset mode lets you choose one of the

following presets:

�Pentagon Up

�Pentagon Down

�Square Iris: Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Aspect Ratio allows you to change the proportions of the

shape. Offset to center lets you alter the center point at which this transition is positioned. Rotation

changes the angle of the iris. Feather is a checkbox that, when turned on, uses the Border slider to

determine the amount of feathering at the edge of the transition. The Reverse checkbox reverses

the direction of the transition. Preset mode lets you choose one of the following presets:

�Square Flat

�Square Point

�Triangle Iris: Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Aspect Ratio allows you to change the proportions of the

shape. Offset to center lets you alter the center point at which this transition is positioned. Rotation

changes the angle of the iris. Feather is a checkbox that, when turned on, uses the Border slider to

determine the amount of feathering at the edge of the transition. The Reverse checkbox reverses

the direction of the transition. Preset mode lets you choose one of the following presets:

�Triangle Up

�Triangle Bottom

�Triangle Left

�Triangle Right

Motion

Motion transitions use the movement of the frames to impart simulated physical momentum to the

transition between the outgoing and incoming clips.

�Barn Door: Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the Border

slider to determine the amount of feathering at the edge of the transition. Motion Blur smooths out

the motion of the transition between frames. The Reverse checkbox reverses the direction of the

transition. Preset mode lets you choose one of the following presets:

�Barn Door Vertical

�Barn Door Horizontal

�Push: Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the

Border slider to determine the amount of feathering at the edge of the transition. Motion Blur

smooths out the motion of the transition between frames. Preset mode lets you choose one of the

following presets:

�Push Left

�Push Right

�Push Up

�Push Down

�Slide: Direction determines whether or not the incoming clip slides in or the outgoing clip slides

out. Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the

Border slider to determine the amount of feathering at the edge of the transition. Motion Blur


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

smooths out the motion of the transition between frames. Preset mode lets you choose one of the

following presets:

�Slide, Left-Right

�Slide, Right-Left

�Slide, Bottom-Up

�Slide, Top-Down

�Slide, Top-Left

�Slide, Bottom-Right

�Split: Color sets the color of the border, if there is one. Border sets the width of the border, in

pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the Border

slider to determine the amount of feathering at the edge of the transition. The Reverse checkbox

reverses the direction of the transition. Motion Blur smooths out the motion of the transition

between frames.

Shape

Shape transitions use geometrical outlines to define the transition from the outgoing to the incoming

clip. Ideally the shape used will be motivated by the content of the scenes involved.

�Box: Color sets the color of the border, if there is one. Border sets the width of the border, in

pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the Border

slider to determine the amount of feathering at the edge of the transition. The Reverse checkbox

reverses the direction of the transition. Box mode lets you choose one of the following options:

�Upper Left

�Upper Right

�Lower Left

�Lower Right

�Left Center

�Top Center

�Right Center

�Bottom Center

�Heart: Color sets the color of the border, if there is one. Border sets the width of the border,

in pixels, with 0 creating no border. Aspect Ratio allows you to change the proportions of the

shape. Offset to Center identifies the center point at which this circular wipe begins, as X and Y

coordinates on the screen. Rotation changes the angle of the shape. Feather is a checkbox that,

when turned on, uses the Border slider to determine the amount of feathering at the edge of the

transition. The Reverse checkbox reverses the direction of the transition.

�Star: Color sets the color of the border, if there is one. Border sets the width of the border, in

pixels, with 0 creating no border. Aspect Ratio allows you to change the proportions of the

shape. Offset to Center identifies the center point at which this circular wipe begins, as X and Y

coordinates on the screen. Rotation changes the angle of the shape. Feather is a checkbox that,

when turned on, uses the Border slider to determine the amount of feathering at the edge of the

transition. The Reverse checkbox reverses the direction of the transition. Preset lets you choose

one of the following options:

�4-Point Star

�5-Point Star

�6-Point Star


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

�Triangle Left: Color sets the color of the border, if there is one. Border sets the width of the

border, in pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the

Border slider to determine the amount of feathering at the edge of the transition. The Reverse

checkbox reverses the direction of the transition.

�Triangle Right: Color sets the color of the border, if there is one. Border sets the width of the

border, in pixels, with 0 creating no border. Feather is a checkbox that, when turned on, uses the

Border slider to determine the amount of feathering at the edge of the transition. The Reverse

checkbox reverses the direction of the transition.