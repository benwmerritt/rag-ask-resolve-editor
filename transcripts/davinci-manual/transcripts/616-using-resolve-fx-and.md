---
title: "Using Resolve FX and"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 616
---

# Using Resolve FX and

Open FX in the Color Page

This section provides an overview of procedures that describe how you can work with Open FX

plugins within the Color page.

Methods of working with Open FX:

•	 To add an Open FX plugin to a node: Drag a plugin from the Open FX Library onto a

node. If you drag a plugin onto a node that already has a plugin, the previous plugin will be

overwritten.

•	 To remove an Open FX plugin from a node: There are two ways to delete an Open FX

plugin from a node.

Right-click a node showing the FX badge, and choose Remove OFX Plugin from the

contextual menu.

Click on the trashcan icon to the right of the name of the effect in the Effects Inspector.

•	 To edit the parameters of an Open FX plugin: Select any node with an FX badge, and open

the Open FX Panel to show the Settings list. You can switch to the Library by clicking the

Library button.

•	 To sample a color parameter within an Open FX plugin: Some OFX plugins have a color

swatch parameter, which exposes an eyedropper button in the Settings. Clicking the

eyedropper turns the pointer into an eyedropper you can use to sample the contents of

the Viewer.

•	 To use Open FX onscreen controls in the Viewer: Select any node with an FX badge, and

the onscreen controls, if there are any, should appear in the Viewer. If not, make sure the

Viewer mode drop-down is set to FX.

Applying Resolve FX and Open FX Plugins

Once you’ve found an Open FX plugin you want to use in the Library, there are two ways of applying

it within the Node Editor of the Color page. Which method you use depends on how you want to use

that plugin.

Adding a Plugin to an Existing Corrector Node

If you want to combine an Open FX plugin with a grade within a single node, simply drag and drop it

onto a new corrector node to apply that plugin’s effect to that node. Nodes with an Open FX plugin

applied have an FX badge in the bottom left-hand corner.


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR

A node with an

Open FX plugin mapplied

You can only apply one Open FX plugin to a node at a time, but by using multiple nodes you

can add as many Open FX plugins to your grade as you need.

When added to a corrector node, Open FX are applied after Motion Blur and Noise Reduction,

but before anything else. This means you can use Motion Blur and Noise Reduction to pre-

process the image before it’s handed off to the Open FX plugin. This also means that all other

adjustments you make within that node are applied to the Open FX plugin’s output.

However, the principal advantage of adding plugins to corrector nodes is that you can use

secondary operations such as a window, a qualifier, or a key to limit that plugin’s effect, much

as you would limit any other kind of adjustment you’d make with a corrector node.

Adding a Plugin as a New Corrector Node

If you want to add an Open FX plugin to your grade as a stand-alone effect, you can simply drag any

plugin from the Open FX Library into the Node Editor or onto a connection line of your grade, and a

new Corrector Node with the Open FX plugin applied will be created.

This new node will now include all the additional inputs and Alpha connectors needed to use the

effect. So now that color correction nodes can be used for everything, there is no need to make

separate FX nodes anymore. This should help simplify node trees and involve much less manual

management of connections between nodes.

Adding a Plugin as a Stand-Alone FX Node (Legacy)

As part of an overhaul of the Resolve FX system to make it more intuitive and easier to use, dragging

an effect from the Effects Library into the Node Editor will now create that effect using a standard

corrector node and not an FX Node.

As of DaVinci Resolve 18.5, FX nodes have been depreciated. There is no need to make an FX node

anymore as all of the previous functionality found in FX nodes have been rolled into the standard

corrector node instead.

However for legacy projects, or if you still prefer to work in the old way, you can still force an FX node

by option-dragging the effect from the Effects Library into the Node Editor instead of dragging it.


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR

Resolve FX and Open FX Settings

When you select a node with a Resolve FX or Open FX plugin applied to it, the Open FX panel

switches to the Settings, which show you every single parameter associated with that plugin,

ready for customization.

Adjust any of the standard controls to manipulate that plugin’s effect on the image.

The parameters of the Glow Resolve FX

Editing Effects Using the Full Screen Viewer

Because the Open FX panel can often be too short to present the full controls of more complicated

filters, it remains visible when you switch to the Full Screen Viewer mode in the Color page. Jump into

this mode by choosing Workspace > Viewer Mode > Full Screen Viewer (Shift-F).

This control layout makes it considerably easier to do detailed work while viewing a larger image and

having all of your effects visible in a taller panel off to the side.

TIP: You can also open and close the Node Editor while in Full Screen Viewer mode, if you

need to switch nodes while doing effects work.


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR

The Full Screen Viewer mode of the Color page lets you keep the Settings panel open as you work

Resolve FX and Open FX

Onscreen Controls

In the Edit page, Fusion page, and Color page, Resolve FX and Open FX display on-screen controls

that you can use to visually edit an effect. In the Edit and Color pages, selecting an Open FX plugin

node or a plugin in the Inspector that has onscreen controls automatically changes the Viewer’s

mode to Open FX Overlay mode, with the available controls ready to use. Different plugins expose

different custom controls, letting you control the effect or manipulate the image, depending on that

plugin’s function.

Adjusting the onscreen controls exposed by the GenArts Sapphire Glint Rainbow plugin


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR

If for whatever reason you switch the Viewer to another onscreen control mode (for example,

showing the Window or Image Wipe controls), you can always switch back to the Open FX controls

by choosing the Open FX Overlay mode from the onscreen control drop-down menu underneath

the Viewer.

TIP: You may find that as you work you want to temporarily hide or show the onscreen

controls in the Viewer so you can get an uncluttered look at the image you’re adjusting. You

can quickly toggle any set of onscreen controls off and on without selecting Off in the menu

by pressing Shift-` (tilde).

Keyframing Resolve FX

and OFX in the Inspector

Resolve FX and Open FX can be keyframed in the Edit, Fusion, and Color pages. However,

they can only be keyframed in the Edit and Color pages using the keyframing controls found

in the Inspector (at the time of this writing). Happily, most simple keyframing tasks can be

performed using three buttons that appear to the right of any parameter that’s capable of

being keyframed. It takes two keyframes at minimum to create an animated effect.

The three keyframe

controls that appear in

the Inspector, from left

to right: Previous keyframe,

Create/Delete keyframe,

Next keyframe

Methods of keyframing parameters in the Inspector:

�To add a keyframe: Select a clip, open the Inspector, then move the Timeline playhead to

the frame where you want to place a keyframe, and click the Keyframe button next to the

parameter of the Inspector you want to animate. Once you’ve added at least one keyframe to a

parameter, all other adjustments you make to parameters in the Inspector, or using the onscreen

Transform/Crop controls in the Timeline Viewer, add new keyframes automatically if the playhead

is at another frame.

�To move the playhead to the next or previous keyframe: Click the small left- or right-hand arrow

to either side of a parameter’s keyframe control, or press Right-Bracket ( [ ) or Left-Bracket ( ] ), to

jump the playhead to the next or previous keyframe.

�To edit an existing keyframe of a parameter: Move the playhead to be on top of the keyframe

you want to edit, and then change that parameter, either in the Inspector, or using the onscreen

controls of the Timeline Viewer.


Color Page Effects | Chapter 151 Using Open FX and Resolve FX

COLOR

Methods of changing keyframe interpolation in the Inspector:

�To change a keyframe to Static: (Color page only) Static keyframes create abrupt one-frame

changes at the keyframe to which they’re applied, which is good for creating sudden effects.

Move the playhead to a frame with a keyframe using the next/previous keyframe controls, then

right-click the orange keyframe button and choose “Change to Static Keyframe.” The keyframe

control changes to a round button to show that keyframe is now Static.

�To change a keyframe to Dynamic: Move the playhead to a frame with a keyframe using the

next/previous keyframe controls, then right-click the orange keyframe button and choose

“Change to Dynamic Keyframe.” The keyframe control changes to a diamond button to show that

keyframe is now Dynamic.

Methods of deleting keyframes and disabling keyframed effects:

�To delete a single keyframe: Open the Inspector, move the Timeline playhead to a frame with a

keyframe, and click the orange Keyframe button in the Inspector to delete it.

�To delete all keyframes for one parameter: Click the reset button to the right of a parameter’s

keyframe control in the Inspector.

�To delete all keyframes in a group of parameters in the Inspector: Click the reset button to the

right of a parameter group’s title bar in the Inspector.

�To disable or enable a single parameter’s keyframed effect: In the Timeline, click the toggle

control at the left of a parameter’s keyframe track. A white dot means it’s enabled, while no dot

means it’s grayed-out and disabled.

�To disable or enable a group of parameters in the Inspector: Click the toggle control at the

left of a parameter group’s title bar in the Inspector. Orange means that group is enabled.

Gray is disabled.