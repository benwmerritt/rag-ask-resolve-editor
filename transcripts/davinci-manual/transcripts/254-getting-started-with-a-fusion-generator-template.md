---
title: "Getting Started with a Fusion Generator Template"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 254
---

# Getting Started with a Fusion Generator Template

There is one simple Noise Gradient Fusion Generator located in the Effects Library that you can use as

a starting point for creating your own generators.

The Fusion Generator templates located in DaVinci Resolve’s Effects Library.

To open the Fusion Noise Gradient Generator in the Fusion page, do the following:


On the Edit page, drag the Fusion Noise Gradient Generator from the Effects Library to

the Timeline.


Right-click over the Noise Gradient Generator and choose Open in Fusion Page from the

pop-up menu.

The Fusion page opens, displaying the node tree that is used to create the Fusion Generator.

Creating a Fusion Generator Template

As easy as it is to begin with the Noise Gradient Generator template, you can just as easily start by

adding a Fusion Composition Effect to a Timeline in the Edit page.

To begin creating a Fusion Generator Template with an empty

Fusion composition, do the following:


On the Edit page, drag the Fusion Composition Effect from the Effects Library to the Timeline.


Right-click over the Composition Effect and choose Open in Fusion Page from the pop-up menu.

An empty Fusion page with a single MediaOut node opens, ready for you to create a

Fusion Generator.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

The Fusion Generator is a solid image generated from any number of tools combined to create a

static or animated background. You can choose to combine gradient colors, masks, paint strokes, or

particles in 2D or 3D to create the background generator you want.

The Fusion Generator node tree creating concentric circles.

Saving a New Fusion Generator

After creating the generator you want in Fusion, you need to save it to the Effects Library to reuse

it in other projects from the Edit page. To do this, you must create a Macro and save it to the

Generator folder.

Ordinarily, macros are used as building blocks inside of Fusion so that you can turn frequently-made

compositing tricks that you use all the time into your own nodes. However, you also use this macro

functionality to build Generator templates for the DaVinci Resolve Edit page.

Start by selecting every node in the Node Editor that you want to include in the Generator template

including the MediaOut node.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

Having made this selection, right-click one of the selected nodes and choose Macro > Create Macro

from the contextual menu.

The Macro Editor displaying the parameters of all the nodes you selected.

The Macro Editor window appears, displaying a hierarchical list of every parameter in the composition

you’ve just selected. The order of nodes is based on the order they were selected in the Node Editor

prior to creating the macro.

The Macro Editor is designed to let you choose which parameters you want to display as custom

controls in the Edit page Inspector when the Generator is applied. You can choose a simplified set of

parameters for customization by enabling the checkboxes next to any parameter name.

Once you enable all the parameters you want to use in the eventual template, click the Close button,

and a Save Macro As dialog appears. Here, you can enter the name of the Transition, as it should

appear in the Edit page Effects Library.

To have the Generator template appear in the Effects Library > Fusion Generators category of DaVinci

Resolve, save the macro in the following locations:

On macOS: Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/

DaVinci Resolve/Fusion/Templates/Edit/Generators

On Windows: C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\

Support\Fusion\Templates\Edit\Generators

On Linux: home/username/.local/share/DaVinciResolve/Fusion/Templates/Edit/Generators


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

Using Your New Generator Template

After you’ve saved your macro, you’ll need to quit and reopen DaVinci Resolve. When you open the

Effects Library on the Edit page, the new Generator template is listed in the Generators category, in

the Fusion Generators list.

Custom Fusion Generator saved in the Edit page Effects Library.

Applying this Generator to the Timeline and opening the Inspector shows the parameters you enabled

for editing, if any.

Creating a Fusion Effect Template

You start building a Fusion Effect template by bringing a clip from the Edit page Timeline into Fusion.

This clip is only used for creating the template and will not be saved with the effect.

Once inside Fusion, you use Fusion’s nodes to create the effect you want. You can use a single

node or a hundred, depending on the effect you want to create. For instance, using Fusion’s Color

Correction nodes, you can create a simple color corrector you can use on the Edit page.

To create a simple Color Corrector effect, do the following:


Insert the Color Corrector node between the MediaIn and MediaOut nodes.


Select the Color Corrector node in the Node Editor, and then press Cmd-A to select the

remaining nodes.


Right-click over any of the selected node and choose Macro > Create Macros from the contextual

menu. Enabling the checkboxes in this window determines the parameters that appear in the

Edit page Inspector.


The Macro Editor window opens. Here, you can enable the checkboxes for any parameters you

want to be shown in the Edit page Inspector.


Enter the name of your effect at the top of the Macro Editor window.


To save the Macro, click Close at the bottom of the window, then click Yes in the dialog that

appears asking you to save the changes.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

The Macros must be saved into the correct folder for DaVinci Resolve to recognize the

Macro as an effect.

In the save dialog, save the Macro in the following locations:

On macOS: Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/

DaVinci Resolve/Fusion/Templates/Edit/Effects

On Windows: C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\

Support\Fusion\Templates\Edit\Effects

On Linux: home/username/.local/share/DaVinciResolve/Fusion/Templates/Edit/Effects

You can save and organize your Fusion Effects into separate subfolders underneath the paths above.

These subfolders will show up in the Effects section in the Edit page.

To see the effect in the Edit page Effects Library, you’ll need to quit DaVinci Resolve and

relaunch the application.

Creating a Fusion Effect Template for Two or More Layers

If the effect you want to create requires multiple images like a video wall, you start by creating a Fusion

clip on the Edit page Timeline that includes the number of layers you want the effect to have. The

clips are only used to create the number of image inputs for the template and will not be saved with

the effect.

Once inside Fusion, use Fusion’s nodes to create the effect you want.

Save the Macro following the same steps you use for single clip effects. Enable any of the parameters

you want to control in the Edit page. To be able to switch the order of video layers within the effect,

make sure you have the Layer checkbox enabled for all the MediaIn nodes.

Once you’ve saved the Macro and relaunched DaVinci Resolve, to use the effect on multiple timeline

layers, you must create a Fusion clip.  The Fusion clip should contain the same number of layers the

effect requires. The order of the Timeline layers, going from the bottom track to the top, matches the

MediaIn numbers. For instance, video track 1 will match the position and appearance of MediaIn1,

video track 2 matches MediaIn2 and so on. If you want to change how tracks map to MediaIn

nodes, you can change the Layer number in the Inspector, assuming you enabled the MediaIn Layer

checkbox when creating the Macro.

Changing Durations of a Template

After you make a template in Fusion, you may want to change its duration in the Edit or Cut page

Timeline. Changing the duration when animation is involved can be complicated, so there are two

Modifiers in Fusion that can help determine how keyframes react when the duration is updated in the

Edit or Cut page Timeline.

Anim Curves Modifier

The Animation Curves Modifier (Anim Curves) is used to dynamically adjust the timing, values, and

acceleration of an animation, even if you decide to change the duration of a Comp. Using this Modifier,

it becomes infinitely easier to stretch or squish animations, create smooth motion, add bouncing

properties, or mirror animations curves without the complexity of manually adjusting splines.

When creating Fusion templates for the Edit or Cut page in DaVinci Resolve, the Anim Curves Modifier

allows the keyframed animation you’ve created in Fusion to stretch and squish appropriately as the

transition, title, or effect’s duration changes on the Edit and Cut page Timelines.


Fusion Fundamentals | Chapter 68 Node Groups, Macros, and Fusion Templates

FUSION

Keyframe Stretcher Modifier

The Keyframe Stretcher modifier is primarily used when creating title templates in Fusion for use

in DaVinci Resolve’s Edit or Cut page. The Keyframe Stretcher modifier is added to any animated

parameter so that the Hold keyframes between the initial animation on screen and the final animation

off-screen stretch when the template is trimmed in the Timeline. This allows the animation to retain its

timing while the static portion of the title stretches to meet the new duration requirements.