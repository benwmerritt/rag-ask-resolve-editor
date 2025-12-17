---
title: "Chapter 78"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 297
---

# Chapter 78

Understanding

Image Channels

This chapter seeks to demystify how Fusion handles image channels and, in the process,

show you how different nodes need to be connected to get the results you expect.

It also explains the mysteries of premultiplication, and presents a full explanation of how Fusion

is capable of using and even generating auxiliary data.

Contents

Channels in Fusion����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1612

Types of Channels Supported by Fusion��������������������������������������������������������������������������������������������������������������������������������� 1612

Fusion Node Connections Carry Multiple Channels���������������������������������������������������������������������������������������������������������� 1613

Node Inputs and Outputs���������������������������������������������������������������������������������������������������������������������������������������������������������������� 1613

Node Colors Tell You Which Nodes Go Together���������������������������������������������������������������������������������������������������������������� 1617

Using Channels in a Composition���������������������������������������������������������������������������������������������������������������������������������������������� 1619

Channel Limiting���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1620

Adding Alpha Channels�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1621

How Channels Propagate During Compositing������������������������������������������������������������������������������������������������������������������� 1622

Rearranging or Combining Channels���������������������������������������������������������������������������������������������������������������������������������������� 1622

Understanding Premultiplication����������������������������������������������������������������������������������������������������������������������������������������������� 1623

The Rules of Premultiplication������������������������������������������������������������������������������������������������������������������������������������������������������ 1625

Alpha Channel Status in MediaIn and Loader Nodes������������������������������������������������������������������������������������������������������� 1627

Controlling Premultiplication in Color Correction Nodes����������������������������������������������������������������������������������������������� 1627

Controlling Premultiplication With Alpha Divide and Alpha Multiply������������������������������������������������������������������������ 1627

Multi Channel Compositing���������������������������������������������������������������������������������������������������������������������������������������������������������� 1628

Compositing with Beauty Passes����������������������������������������������������������������������������������������������������������������������������������������������� 1628

Working with Auxiliary Channels������������������������������������������������������������������������������������������������������������������������������������������������ 1634

Auxiliary Channels Explained������������������������������������������������������������������������������������������������������������������������������������������������������� 1636

Propagating Auxiliary Channels�������������������������������������������������������������������������������������������������������������������������������������������������� 1644

Nodes That Use Auxiliary Channels������������������������������������������������������������������������������������������������������������������������������������������ 1644

Image Formats That Support Aux Channels������������������������������������������������������������������������������������������������������������������������� 1646

Creating Auxiliary Channels in Fusion�������������������������������������������������������������������������������������������������������������������������������������� 1646


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

Channels in Fusion

Fusion introduces some innovative ways of working with the many different channels of image

data that modern compositing workflows encompass. This chapter’s introduction to color and data

channels and how they’re affected by different nodes and operations is a valuable way to begin the

process of learning to do paint, compositing, and effects in Fusion.

If you’re new to compositing, or you’re new to the Fusion workflow, you ignore this chapter at your

peril, as it provides a solid foundation to understanding how to predictably control image data as you

work in this powerful environment.

Types of Channels Supported by Fusion

Digital images can be divided into separate streams of image data called Channels, each of which

carries a specific kind of image data. Nodes that perform different image processing operations

typically expect specific channels to provide predictable results. You are probably familiar with

the three standard color channels of red, green, and blue, but there are many others. This section

describes the different kinds of channels that Fusion supports.

RGB Color channels

The red, green, and blue channels of any still image or movie clip combine additively to represent

everything we can see via visible light. Each of these three channels is a grayscale image when seen

by itself. When combined additively, these channels represent a full-color image.

Alpha Channels

An alpha channel is an embedded fourth channel that defines different levels of transparency in an

RGB image. Alpha channels are typically embedded in RGB images that are generated from computer

graphics applications. In Fusion, white denotes solid areas, while black denotes transparent areas.

Grayscale values range from more opaque (lighter) to more transparent (darker).

If you’re working with an imported alpha channel from another application for which these conventions

are reversed, never fear. Every node capable of using an alpha channel is also capable of inverting it.

Single-Channel Masks

While similar to alpha channels, mask channels are single channel images, external to any RGB image

and typically created by Fusion within one of the available Mask nodes. Mask nodes are unique in

that they propagate single-channel image data that defines which areas of an image should be solid

and which should be transparent. However, masks can also define which parts of an image should be

affected by a particular operation, and which should not. Mask channels are designed to be connected

to specific mask inputs of nodes including Effect Mask, Garbage Mask, and Solid Mask inputs.

Auxiliary Channels

Auxiliary channels (covered in more detail later in this chapter), describe a family of special-purpose

image data that typically expose 3D data in a way that can be used in 2D composites. For example,

Z-Depth channels describe the depth of each pixel in an image along a Z axis, while an XYZ Normals

channel describes the orientation (facing up, facing down, or facing to the left or right) of each pixel

in an image. Auxiliary channel data is generated by rendering 3D images, so it usually accompanies

or is embedded with RGB images generated by 3D modeling and animation applications.

These channels can also be generated from within Fusion via the Renderer 3D node, which outputs

a 3D scene that you’ve assembled and lit as 2D RGBA channels, with optionally accompanying

auxiliary channels.


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

The reason to use auxiliary data is that 3D rendering is computationally expensive and time-consuming,

so outputting descriptive information about a 3D image that’s been rendered empowers compositing

artists to make sophisticated alterations in 2D. You can add motion blur, perform relighting, and

composite with depth information faster than re-rendering the 3D source material over and over.

TIP: You can view any of a node’s channels in isolation using the Color drop-down menu

in the viewer. Clicking the Color drop-down menu reveals a list of all channels within the

currently selected node, including red, green, blue, or auxiliary channels.

Fusion Node Connections Carry Multiple Channels

The connections that pass image data from one node to the next in Fusion’s Node Editor are capable

of carrying multiple channels of image data. That means that a single connection may route RGB,

or RGBA, or RGBAZ-Depth, or even just Z-Depth, depending on the Input you connect to and the

node’s function.

In the following example, the two MediaIn nodes output RGB data. However, the Delta Keyer creates

an alpha channel and combined it with MediaIn2’s RGB image. The RGB-A of the Delta Keyer becomes

the foreground image that the Merge node can use to create a two-layer composite.

The alpha channel generated by the Delta key is used for

compositing by the foreground input of the Merge node.

NOTE: Node trees shown in this chapter may display MediaIn nodes found in

DaVinci Resolve’s Fusion page; however, Fusion Studio Loader nodes are interchangeable

unless otherwise noted.

Running multiple channels through single connection lines makes Fusion node trees simple to read,

but it also means you need to keep track of which nodes process which channels to make sure that

you’re directing the intended image data to the correct operations.

Node Inputs and Outputs

By default, MediaIn nodes in the Fusion page and Loader nodes in Fusion Studio output RGBA

channels. When you connect one node’s output to another node’s input, the active channels are

passed from the upstream node to the downstream node, which then processes the image according

to that node’s function. Only one node output can be connected to a node input at a time. In this

simple example, a MediaIn node’s output is connected to the input of a Highlight node to create a

sparkly highlight effect.


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

MediaIn node connected to a Highlight node connected to MediaOut node in the Fusion page.

When connecting nodes, a node’s output carries the same channels no matter how many times the

output is “branched.” You cannot send one channel out on one branch and a different channel out on

another branch.

The MediaIn node’s output is branched but carries the same RGB channels to both inputs.

Using Multiple Inputs

Most nodes have two inputs, one for RGBA and another for an effect mask that can be optionally

used to limit the effect of that node to a particular part of the image. However, some nodes have

three or even more inputs, and it’s important to make sure you connect the correct image data to the

appropriate input to obtain the desired result. If you connect one node’s output to another node’s input

and nothing happens, chances are you’ve connected to the wrong input.

For example, the MatteControl node has a background input and a foreground input, both of which

accept RGBA channels. However, it also has SolidMatte, GarbageMatte, and EffectsMask inputs that

accept alpha or mask channels to modify the transparency of the Node’s output. If you want to perform

the extremely common operation of using a MatteControl node to create an alpha channel using a

Polygon node for rotoscoping an image, you need to make sure that you connect the Polygon node

to the GarbageMatte input to obtain the correct result. The GarbageMatte input is automatically set to

alter the alpha channel of the foreground image. If you connect to any other input, your Polygon mask

may not produce expected results.

Polygon node connected to the GarbageMatte input of a MatteControl node for rotoscoping


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

In another example, the DeltaKeyer node has a primary input (labeled “Input”) that accepts RGBA

channels, but it also has three Matte inputs. These SolidMatte, GarbageMatte, and EffectsMask inputs

on the Delta Keyer accept alpha or mask channels to modify the matte being extracted from the image

in different ways.

The DeltaKeyer combines the multiple mask nodes in different ways.

If you position your pointer over any node’s input or output, a tooltip appears in the Tooltip bar at the

bottom of the Fusion window, letting you know what that input or output is for, to help guide you to

using the right input for the job. If you pause for a moment longer, another tooltip appears in the Node

Editor itself.

(Left) The node input’s tooltip in the Tooltip bar,

(Right) The node tooltip in the Node Editor

Connecting to the Correct Input

When you’re connecting nodes, pulling a connection line from the output of one node and dropping it

right on top of the body of another node makes a connection to the default input for that node, which

is typically the “Input” or “Background” input.

Side by side, dropping a connection on a node’s body to connect to that node’s primary input


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

However, if you drop a connection line right on top of a specific input, then you’ll connect to that

input, so it’s important to be mindful of where you drop connection lines as you wire up different node

trees together.

Side by side, dropping a connection on a specific node input, note how the

inputs rearrange themselves afterwards to keep the node tree tidy-looking

TIP: If you hold the Option key down while you drag a connection line from one node onto

another, and you keep the Option key held down while you release the pointer’s button to

drop the connection, a menu appears that lets you choose which specific input you want to

connect to, by name.

Inputs Require Specific Channels

Usually, you’re prevented from connecting a node’s output to another node or node input that’s not

compatible with it. For example, if you try to connect a Text3D node’s output directly to the input of a

regular Merge node, it won’t work; 3D nodes do not produce RGB images, they produce 3D geometry

data, so you must first connect to a Renderer3D node that creates the RGB output appropriate for 2D

compositing operations.

In other cases, connecting the wrong image data to the wrong node input won’t give you any error,

it simply fails to produce the result you were expecting, necessitating you to troubleshoot the

composition. If this happens to you, check the Fusion Effects section of this manual to see if the node

you’re trying to connect to has any limitations as to how it must be attached.

TIP: This chapter tries to cover many of the easy-to-miss exceptions to node connection that

are important for you to know, so don’t skim too fast.

Always Connect the Background Input First

Many nodes combine images in different ways, using “background” and “foreground” inputs. This

includes the Merge node, the Matte Control node, and the Channel Booleans node, to cite common

examples. The color of inputs on a node can help you make the right corrections. For instance,

background inputs are always orange, and foreground inputs are always green.


Fusion Fundamentals | Chapter 78 Understanding Image Channels

FUSION

When you first connect any node’s output to a multi-input node, you usually want to connect the

background input first. This is handled for you automatically when you first drop a connection line onto

the body of a new multi-input node. The orange-colored background input is almost always connected

first (the exception is Mask nodes, which always connect to the first available Mask input). This is good

because you want to get into the habit of always connecting the background input first.

If you connect to only one input of a multi-input node and you don’t connect to the background input,

you may find that you don’t get the results you wanted. This is because each multi-input node expects

that the background is connected before anything else so that the internal connections and math used

by that node can be predictable.

TIP: The only node to which you can safely connect the foreground input prior to the

background input is the Dissolve node, which is a special node that can be used to either

dissolve between two inputs, or automatically switch between two inputs of unequal duration.