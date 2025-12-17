---
title: "Using Composite Modes in the Merge Node"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 304
---

# Using Composite Modes in the Merge Node

To create a more convincing composite in layer-based systems, you often use Blend modes. Blend

modes are located in the Merge node since that is where one layer gets composted over another.

Let’s take an example where you want to use the Screen mode to make a foreground image look more

like a reflection.

The Merge node has a variety of controls built into it for creating just about every compositing

effect you need. Items you may be familiar with as Blend modes are located in the Apply Mode

pop-up menu. You can use these mathematical compositing modes to combine the foreground

and background layers together. A Blend slider allows you to fade the foreground input

with the background.

Adjusting the Apply Mode and Blend slider

of the Merge node in the Inspector

NOTE: The Subtractive/Additive slider disappears when you choose any other Apply

Mode option besides Normal, because the math would be invalid. This isn’t unusual; there

are a variety of controls in the Inspector that hide themselves when not needed or when a

particular input isn’t connected.

The Screen node is perfect for simulating reflections, and lowering Blend a bit lets you balance the

foreground and background images. It’s subtle, but helps sell the shot.

TIP: You may have noticed that the Merge node also has a set of Flip, Center, Size,

and Angle controls that you can use to transform the foreground image without needing

to add a dedicated Transform node. It’s a nice shortcut for simplifying node trees large

and small.


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Creating and Using Text

In this next example, we’ll look at how to create a simple text object using the Text+ node.

Then, we’ll see how to use the text generator’s alpha channel in another image to create a more

complex composite.

Creating Text Using the Text+ Node

The Text+ node is the primary tool for creating 2D text in the Fusion page. If you are using DaVinci

Resolve, this is also the same Text+ generator available in the Edit page. It is easily accessible right in

the toolbar.

The Text+ node is an incredibly deep tool for creating text effects, with six tabs of controls for adjusting

everything from text styling, to different methods of layout, to a variety of shading controls including

fills, outlines, shadows, and borders. As sophisticated a tool as this is, we’ll only be scratching the

surface in this example.

We’ll start with a MediaIn node that will serve as our background selected in the Node Editor. Clicking

the Text+ button automatically creates a new Text+ node connected as the foreground input of a

Merge node. The same behavior occurs if you are using Fusion Studio, with a Loader node.

Selecting a node you want to append another node to (top) Clicking

the Text+ button on the toolbar automatically creates a Merge

composite with the text as the foreground input connection (bottom)

Selecting a Text node opens the default Text panel parameters in the Inspector, and it also adds a

toolbar at the top of the viewer with tools specific to that node. Clicking on the first tool at the left lets

you type directly into the viewer, or you can type into the Styled Text field in the Inspector.

The viewer toolbar for the Text node with tools

for text entry, kerning, and outline controls


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

If you’re viewing the Merge, the text appears in the viewer superimposed against the background clip.

Onscreen controls appear that let you rotate (the circle) and reposition (the red center handle and two

arrows) the text, and we can see a faint cursor that lets us edit and kern the text using other tools in

the viewer toolbar.

Text that’s been typed into the viewer, with onscreen text transform controls

Styling and Adjusting Text

To style the text, you use the controls in the Inspector, modifying text style controls such as Font, Size,

and Tracking to change the spacing between the letters.

The restyled text

TIP: Holding down the Command key while dragging any control in the Inspector “gears

down” the adjustment so that you can make smaller and more gradual adjustments.


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Selecting the Manual Kerning tool in the viewer toolbar (second tool from the left) reveals small red

dots underneath each letter of text.

Clicking a red dot under a particular letter puts a kerning highlight over that letter.

The Manual Kerning tool

in the viewer toolbar

To make manual kerning adjustments:


Option-drag the red dot under any letter of text to adjust that character’s kerning while

constraining letter movement to the left and right. You can also drag letters up and down for other

effects. Depending on your system, the kerning of the letter you’re adjusting might not update until

you drop the red dot in place.


If you don’t like what you’ve done, you can open the Advanced Controls in the Inspector and clear

either the kerning of selected letters or all manual kerning before starting over again.

Option-dragging the little red dot revealed by the Manual

Kerning tool to manually adjust kerning


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Using Text as a Mask

You can fill the text with a color or gradient, or you can use the text as a matte to cut the letters out of

another image. First, we’ll drag another clip of a chalkboard covered with math from the Media Pool to

the Node Editor as a disconnected MediaIn2 node.

Disconnecting and Reconnecting Nodes

If we start from the previous example that had a MediaIn as the background and the Text+ as the

foreground to a Merge, we’ll need to do a little rearranging. Clicking the last half of the connection

from the Text1 node to the Merge foreground input disconnects it.

Clicking the second half of a connection to disconnect it (previous

page), and the result with the text node disconnected (above)

Connecting a MediaIn2 or Loader2 node onto the Merge1 node’s foreground input causes the entire

viewer to be filled with the MediaIn2 (assuming we’re still viewing the Merge node). At this point, we

need to insert the Text1 node’s image as an alpha channel into the MediaIn2 node’s connection, and

we can do that using a MatteControl node.

The updated composite, with two video images

connected and the text node disconnected


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

Using Matte Control Nodes

Select the MediaIn2 node, and click the Matte Control button in the toolbar to add it between the

MediaIn2 and Merge1 nodes. (To tidy up, I’ve moved the nodes around a bit in the screenshot.)

The MatteControl node has numerous uses. Among them is taking one or more alpha channels,

mattes, or images that are connected to the Garbage Matte, Solid Matte, and/or foreground inputs,

combining them, and using the result as an alpha channel for the image that’s connected to the

background input. It’s critical to make sure that the image you want to add an alpha channel to is

connected to the background input of the MatteControl node, or the MatteControl node won’t work.

The second image properly connected to

the MatteControl node’s background input

With this done, connecting the Text+ node’s output, which has the alpha channel, to the MatteControl

node’s Garbage Matte input, is a shortcut we can use to make a mask, matte, or alpha punch out a

region of transparency in an image.

Keep in mind that it’s easy to accidentally connect to the wrong input. Because inputs rearrange

themselves depending on what’s connected and where the node is positioned (and, frankly, the colors

can be hard to keep track of when you’re first learning), it’s key to make sure that you always check

the tooltips associated with the input you’re dragging a connection over to make sure that you’re really

connecting to the correct one. If you don’t, the effect won’t work, and if your effect isn’t working, the

first thing you should always check is whether you’ve connected the proper inputs.

Option-dragging a node connection to drop onto

another node exposes a node input menu


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION

One alternate method of connecting nodes together is to hold down the Option key while dragging a

connection from one node’s output and dropping it onto the body of another node. This opens a pop-

up menu from which you can choose the specific input you want to connect to, by name. Note that

the menu only appears after you’ve dropped the connection on the node and released your pointing

device’s button.

Once the Text1 node is properly connected to the MatteControl node’s Garbage Matte input, a text-

shaped area of transparency is displayed for the graphic if you load the MatteControl node into

the viewer.

Connecting the Text node to the MatteControl node’s Garbage Matte

input (previous page), and the resulting hole punched in the image (above)

Customizing Matte Control Nodes

You can use the Inspector to change some parameters to get the result you want. In the Inspector

controls for the MatteControl node, revealing the Garbage Matte controls exposes parameters for

modifying how the Garbage Matte input is applied to the image. For example, you can choose to have

the text mask filled with the image instead of cutting a hole in the image.


Fusion Fundamentals | Chapter 79 Compositing Layers in Fusion

FUSION