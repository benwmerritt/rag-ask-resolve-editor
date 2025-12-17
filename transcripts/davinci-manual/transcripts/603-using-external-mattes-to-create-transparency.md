---
title: "Using External Mattes to Create Transparency"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 603
---

# Using External Mattes to Create Transparency

You can also use an EXT MATTE node to create transparency in a clip, for compositing with clips

underneath it on the Timeline.

To use a clip matte to create transparency in a clip:


Right-click any node, and choose the attached matte you want to use from the Add Matte

submenu of the contextual menu.

Adding an EXT MATTE node to a Clip grade applies the effect to only that clip, whereas adding an

EXT MATTE node to a Track grade applies the effect to the entire Timeline.


Right-click any empty area of the Node Editor, and choose Add Alpha Output to reveal the Node

Tree output on the right that lets you assign a key to be used to define clip transparency.


Connect one of the EXT MATTE node’s triangular key outputs to the Alpha output at the right of

the Node Editor.

The node setup for using an external matte to composite two layer

The areas of the matte defined by the key are now rendered transparent.

The final composite created

using the external matte node


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

Key Palette Controls for the External Matte Node

When you select an EXT MATTE node, the Key palette displays different parameters only for mattes.

Be aware that you must turn off the Lock Matte checkbox before you can make adjustments to

transform the matte.

The Key Palette showing a texture layer added as an EXT MATTE node

�Transform: Standard Pan, Tilt, Zoom, Rotate, Width, and Height parameters let you transform a

matte to fit the image better.

�Flip Image: Two buttons let you flip the matte clip horizontally or vertically.

�Offset: Adjust this parameter to offset the start point of a matte clip.

�Freeze: Turning on this checkbox freezes the matte clip on a single frame. Adjust the Offset

parameter to choose which frame to freeze on.

�Loop: Turning on this checkbox enables matte clips to loop endlessly, which lets shorter matte

clips cover longer durations.

�Lock Matte: When turned on, locks the sizing of a matte to whatever changes are made to the

Input Sizing of that clip, so the matte transforms to follow the clip.

You can also use external mattes as creative tools. For example, you might use a more abstract

animated matte, or a grayscale film scan of dirt and dust, to apply correction for effect.

Using Mattes From the Fusion Page

If you’re grading a composite that’s been created in the Fusion page, you can feed mattes created in

different parts of a Fusion composition to the Color page to use in the grade as well. For example, if

you’re grading a composite of a foreground actor who’s green screen keyed against a background

layer, you might want to use the matte generated for the key to protect the foreground subject from an

operation in your grade that you only want to affect the background. Happily, this is easy to set up.

In the following Fusion composition, two DeltaKeyer nodes (one to create an overall matte, and

one to create a solid matte protecting the core) and one BSpline node (to create a garbage matte)

work together to create a finely-tuned matte. This matte is used by the Merge1 node to preserve the

subject’s hair and composite them in front of a gently blurred (using the LensBlur node) planet, with the

final result connected to the MediaOut1 node, which feeds this image to the Edit page and Color page

for continued adjustment.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

A green screen composition in the Fusion page, outputting the RGB in

MediaOut1, and the foreground matte in MediaOut2

Because the Merge1 node outputs the entire composition as a single image, a second MediaOut node

(highlighted) is added to output the matte, just in case the colorist might want to use it later.

TIP: In this composition, the foreground and background images are different sizes, so

outputting the alpha channel of the DeltaKeyer1 node would result in a matte sized to match

the foreground image, but that doesn’t fit the composition, which is cropping the top and

bottom of the foreground image based on the frame size of the widescreen background

image. To get around this, the foreground and background images are composited a second

time using the Merge2 node, which has the Operator parameter set to “In” to output just the

foreground image and matte, as resized by the Merge operation. The resulting MediaOut2

node thus outputs a foreground matte that’s properly sized to fit the composition.

On the Color page, the grade in node 1 is applied to the overall final result, which is a single image.

After grading, it’s decided that the woman appears a bit warm relative to the cool blue of the

planet behind.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

The composition as it appears in the Color page Node Viewer

Right-clicking the background of the Node Editor and choosing Add Source adds a second source at

the left of the Node Editor.

Adding a source to bring in the MediaOut2 node’s

matte output from the Fusion page composition

This second source corresponds to the second MediaOut node you added to the Fusion page

composition, which outputs the Matte as a key in the Color page, usable just like any other key. If you

hover your pointer over each source, a tooltip appears letting you know which output corresponds to

which node.

Hovering the pointer over a

source identifies it in a tooltip

Generally, sources are arranged from top to bottom from the first MediaOut node appearing in a

Fusion composition to the last. At this point, you can connect the second Source to the Key input of a

second corrector node, using that key to selectively grade just the woman in the foreground (grade

exaggerated for effect), without affecting the background. The Viewer is shown with Splitscreen set

to Highlight Modes, so you can see the result as well as the key from the Fusion page that’s being

used by Node 2.


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

Connecting the second source to a second Corrector node’s KEY input to use

the matte to limit a correction made to the foreground character

Using the Key Mixer

The Key Mixer node lets you mix keys output from multiple Corrector nodes, combining them in

different ways to create a single key output. This makes it possible to build much more intricate keys

than you can with a single qualifier or set of four windows. In particular, the Key Mixer node is the only

way to combine multiple keys made using qualifiers and windows, adding, subtracting, or intersecting

them to create a highly specific result.

Adding Two Keys Together

In the following example, you’ll learn how to set up a Key Mixer to combine the keys output by two

Corrector nodes in a node tree. Then you’ll learn how to change the way the input keys are combined

using the Key palette.

To combine two or more keys using the Key Mixer:


Right-click anywhere on the gray area of the Node Editor, and choose Add Node > Key Mixer.


Create two Corrector nodes, then attach their RGB inputs to the RGB output from an appropriate

node in the main part of the tree, and attach their key outputs to the key inputs of the Key Mixer.


Next, attach the key output of the Key Mixer node to the key input of the node you want to use to

make the correction. Remember, the objective is to use the key that’s output by the Key Mixer to

limit the adjustment being made using another node, in this case Node 3.

Setting up the node tree you’ll need to combine two keys together


Color | Chapter 146 Combining Keys and Using Mattes

COLOR

Keep in mind, especially since this is a significant reordering of nodes in the Node Editor, that

every node needs to be connected properly for the overall grade to work.


Now that the node structure is fully connected, use windows, qualifiers, or both to create keys in

each of the nodes that you connected to the Key Mixer. In this example, Node 2 is isolating the

main skin tone, and Node 5 is isolating the blue of his jeans and hood.

By default, all keys connected to the Key Mixer are added together, as you can see in the

Key Mixer’s thumbnail.

Combining multiple keys with the Key Mixer

If you wanted, you can use the controls in the Key palette to change this, in order to isolate the

intersection of two keys, or to subtract one key from another. This is covered in the next section.


Continuing with the previous setup where both keys are added together by default, selecting

Node 3 and dropping the saturation to be very faint stylizes the entire background, while leaving

the various hues of the man we’ve isolated alone.

Final grade, the talent in color with a B&W background