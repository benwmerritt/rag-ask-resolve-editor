---
title: "Using Transform Controls in the Merge Node"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 305
---

# Using Transform Controls in the Merge Node

The Merge node includes a set of transform parameters in the Inspector that specifically affect the

foreground input’s image. This makes it quick and easy to adjust a foreground image to match the

background without requiring another node.

The Merge node transform controls that

affect the foreground input’s image

NOTE: When connecting two images of different sizes to a Merge node, the resolution of the

background image defines the output resolution of that node. Keep that in mind when you run

into resolution issues.

You can use the Size slider to resize the foreground.

The final composite


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Building a Simple Green-Screen Composite

Taking another step forward in compositing, the next example shows how you can equate a

multilayered Timeline like the one in DaVinci Resolve’s Edit page to nodes in Fusion’s node tree. We’ll

use DaVinci Resolve, but understanding how layers map to nodes can be helpful for anyone new to

dealing with a node-based interface. In this example, we’ll create a simple composite using a green-

screen key and two other layers to create a news story.

Mapping Timeline Layers to Nodes in Fusion

This composite involves three layers in a Timeline. The Timeline consists of a background graphic on

video track 1, a green-screen clip on video track 2, and a foreground graphic on video track 3.

Background on video track 1 (top left), green-screen clip on

video track 2 (bottom), and graphic file on video track 3 (top right)

Implied in a timeline-based system is that higher numbered video tracks appear as the more forward,

or frontmost, element in the viewer. Video track 1 is the background to all other video tracks. Video

track 3 is in the foreground to both video track 1 and video track 2.

TIP: If using DaVinci Resolve, you can bring all three layers from the Edit page into Fusion by

creating a Fusion clip.

For more information on creating Fusion Clips, see Chapter 65, “Getting Clips into Fusion.” in

the DaVinci Resolve Reference Manual or Chapter 3 in the Fusion Reference Manual.


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

A stack of clips to use in a composite (previous page), and turning that stack

into a Fusion clip in DaVinci Resolve’s Edit page (above)

In Fusion, each video clip is represented by a MediaIn in the Fusion page or a Loader in Fusion Studio.

In our example below, the MediaIn2 is video track 2, and MediaIn 1 is video track 1. These two

elements are composited using a Merge node (foreground over background, respectively). The

composite of those two elements becomes the output of the first Merge node, which becomes the

background to a second Merge. There is no loss of quality or precomposing when you chain Merges

together. MediaIn3 represents video track 3 and is the final foreground in the node tree since it is the

topmost layer.

The initial node tree of the three clips we turned into a Fusion clip


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

With this node tree assembled to mimic the video layers, we can focus the rest of this example on

adding the nodes we’ll need to each branch of this tree to create the green-screen composite.

Pulling a Green-Screen Key Using the Delta Keyer

To make this composite, you need to create transparency behind the newscaster. When working in a

node tree, you must become accustomed to rearranging existing nodes to make room for new ones.

You’ll often move nodes off to the side or up above to make room for the additional nodes.

Creating space after the MediaIn nodes and selecting the second one in preparation for adding a node

The DeltaKeyer node is the main tool used for green-screen keying. It attaches to the output of

the node that represents the green screen—in our example, that is the MediaIn2 node. With the

MediaIn2 selected, pressing Shift-Space opens the Select Tool dialog where you can search for

and insert any node. Below we have added the DeltaKeyer after the MediaIn2 node but prior to

being merged with the background.

Adding a DeltaKeyer node inline after the MediaIn2 node

The DeltaKeyer node is a sophisticated keyer that is capable of impressive results by combining

different kinds of mattes and a clean-plate layer, but it can also be used very simply if the

background that needs to be keyed is well lit. And once the DeltaKeyer creates a key, it embeds

the resulting alpha channel in its output, so in this simple case, it’s the only node we need to add.

It’s also worth noting that, although we’re using the DeltaKeyer to key a green screen, it’s not

limited to keying green or blue only; the DeltaKeyer can create impressive keys on any color in

your image.

With the DeltaKeyer selected, we’ll use the Inspector controls to pull our key by quickly sampling

the shade of green from the background of the image. To sample the green-screen color, drag the

Eyedropper from the Inspector over the screen color in the viewer.


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Dragging the Eyedropper to the viewer

samples the screen color

As you drag in the viewer, an analysis of the color picked up by the location of the Eyedropper

appears within a floating tooltip, giving some guidance as to which color you’re really picking.

Meanwhile, if viewing the Merge in a second viewer, we get an immediate preview of the

transparency and the image we’ve connected to the background.

The original image (left), and after sampling the green screen using the Eyedropper from the Inspector (right)

When we’re happy with the preview, releasing the pointer button samples the color, and the

Inspector controls update to display the value we’ve chosen.

The DeltaKeyer Inspector updates with the sampled color


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Loading the DeltaKeyer into the viewer and clicking the Color button to view the alpha channel being produced

No matter how good the composite may look, once you’ve selected the screen color to pull a key,

you need to load the DeltaKeyer node into the viewer itself. This allows you to evaluate the quality or

density of the alpha channel created by the key. Above the viewer, click the Color button in the viewer

toolbar, or click in the viewer and press C to switch the viewer between the RGB color channels of the

image and the alpha channel.

Black in a matte represents the transparent areas, while white represents the opaque areas. Gray

areas represent semi-transparency. Unless you are dealing with glass, smoke, or fog, most mattes

should be pure white and pure black with no gray gray areas. If a close examination of the alpha

channel reveals some fringing in the white foreground of the mask, the DeltaKeyer has integrated

controls for post-processing of the key and refining the matte. Following is a quick checklist of the

primary adjustments to make.

After making the screen selection with the Eyedropper, try the following adjustments to

improve the key.

�Adjust the Gain slider to boost the screen color, making it more transparent. This can adversely

affect the foreground transparency, so adjust with care.

�Adjust the Balance slider to tint the foreground between the two non-screen colors. For a

green screen, this pushes the foreground more toward red or blue, shifting the transparency

in the foreground.

Clicking the third of the seven tabs of controls in the DeltaKeyer Inspector opens up a variety of

controls for manipulating the matte.

Initial adjustments in the matte tab may include the following parameters:

�Adjust the lower and upper thresholds to increase the density in black and white areas.

�Very subtly adjust the Clean Foreground and Clean Background sliders to fill small holes in the

black and white matte. The more you increase these parameters, the more harsh the edges of

your matte become.


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Adjusting the Clean Foreground slider in the

Matte panel of the DeltaKeyer controls

In this case, raising the Clean Foreground slider a bit eliminates the inner fringing we don’t want,

without noticeably compromising the edges of the key.

The original key (left), and the key after using the Clean Foreground slider (right)

With this accomplished, we’re happy with the key, so we load the Merge1 node back into the viewer, and

press C to set the Color control of the viewer back to RGB. We can see the graphic in the background,

but right now it’s too small to cover the whole frame, so we need to make another adjustment.

The final key is good, but now we need to work on the background


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION