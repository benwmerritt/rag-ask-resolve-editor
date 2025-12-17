---
title: "What Is Fusion?"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 222
---

# What Is Fusion?

Blackmagic Design Fusion is powerful 2D and 3D visual effects compositing software with over

thirty years of evolution serving the motion picture and broadcast industry, creating effects seen in

countless films and television series. It is available as a stand-alone application as well as a page

within DaVinci Resolve.

In its purest form, Fusion is a collection of image-processing engines called nodes. These nodes

represent effects like blurs and color correctors, as well as images, 3D models, and spline masks.

Similar to effects you may be familiar with, each node includes a set of parameters that can be

adjusted and animated over time. Stringing different nodes together in a graphical user interface

called a node tree allows you to create sophisticated visual effects. The nodes, node trees, and all

settings you create are saved in a document called a Composition, or “comp” for short.

The Fusion Page within DaVinci Resolve

Merged right into DaVinci Resolve, the Fusion page makes it possible to jump immediately from editing

right into compositing, with no need to export media, relink files, or launch another application to get

your work done. Now everything you need lives right inside DaVinci Resolve.

The Fusion page in DaVinci Resolve, showing viewers, the Node Editor, and the Inspector

How Do I Use the Fusion Page?

The relationship between the Edit page and the Fusion page is similar to the relationship between the

Edit page and the Color page. Each clip can have a grade applied to it in the Color page, and similarly

every clip can have a composition applied to it in the Fusion page.

If you use the Fusion page to create any kind of effect or composite, a badge appears on that clip in

the Timeline to show that clip has a composition applied to it.


Fusion Fundamentals | Chapter 63 Introduction to Compositing in Fusion

FUSION

Clips with Fusion page compositions have a

Fusion badge to the right of the name.

To create an effect in the Fusion page of DaVinci Resolve, you need only park the playhead over a clip

in the Edit or Cut page and then click the Fusion page button. Your clip is immediately available as a

MediaIn node in the Fusion page, ready for you to add a variety of stylistic effects. You can paint out

an unwanted blemish or feature, build a quick composite to add graphics or text, or accomplish any

other visual effect you can imagine, built from the Fusion page’s toolkit of effects.

Alternatively, in DaVinci Resolve, you have the option of editing together all the clips you want to use,

superimposing and lining up every piece of media you’ll need with the correct timing, before selecting

them and creating a Fusion clip. A Fusion clip functions as a single item in the Edit or Cut page

timeline, but once in the Fusion page, each piece of media you’ve assembled is revealed in a fully built

Fusion composition, ready for you to start adding nodes to customize for whatever effect you need

to create.

Whichever way you want to work, all this happens on the very same timeline as editing, grading, and

audio post, for a seamless back and forth as you edit, refine, and finish your projects.

How Do Fusion Effects Differ from Edit Page Effects?

When using DaVinci Resolve, you can create numerous effects in the Edit page. Transitions, fades,

superimpositions, over-the-shoulder picture-in-picture effects, time remapping, and lower third

titles are some of the effects that can be quickly and more efficiently created in the Edit or Cut page

timeline. However, the Fusion page’s node-based interface lets you go deep into the details of a

composition to create sophisticated 2D and 3D effects with precise control and endless customization.

Effects that include more than two or three layers can be much more manageable in Fusion. Green or

blue screen composites, sky replacements, and object removal are all effects better suited for Fusion’s

more advanced toolset.

How Do Fusion Effects Differ from Color Page Effects?

The Color page in DaVinci Resolve can also handle some visual effects work. Effects that blur the line

between color grading and finishing can be very fast and intuitive in the Color Page, especially for

people already familiar with the Color page toolset. Beauty work and small image repairs can make

efficient use of the Color page’s straightforward Tracking tool, Face Refinement, and Patch Replacer

effects. However, when it comes to more challenging blue/green screen compositing, the tools built

around Fusion’s powerful Delta keyer are more capable of handling these shots. Integrating 3D

objects into live-action scenes, split-screen effects, motion graphics, and precise keyframing are all

better suited to the Fusion page.


Fusion Fundamentals | Chapter 63 Introduction to Compositing in Fusion

FUSION

The Fusion Studio Stand-Alone Application

Creating visual effects with the stand-alone Fusion Studio software begins with opening Fusion,

creating a new composition, importing some clips via Loader nodes, and building out your composite

with effects. Just like the Fusion Page in DaVinci Resolve, you add effects using different nodes from

the Effects Library, and you combine multiple layers of imagery using Merge nodes. Once you’ve

created the desired result, add a Saver node to the end of the tree of nodes you’ve created to render

your final result.

Rendering Out Your Final Result

Unlike the Fusion Page in DaVinci Resolve, which renders directly back into the Edit or Cut page

timeline, the final step in Fusion Studio is to render the finished effect to disk as a movie file or image

sequence. The last node in every node tree is a Saver node. Saver nodes configure the output file

format and render the file to disk. You can use as many Saver nodes in a composite as you need. For

instance, you might use multiple Saver nodes to render out intermediate areas of a composite or to

output a composite in multiple formats.

What Kinds of Effects Does Fusion Offer?

In addition to the kinds of robust compositing, paint, rotoscoping, and keying effects you’d expect from

a fully-featured 2D compositing environment, Fusion offers much more.

3D Compositing

Fusion has powerful 3D nodes that include extruded 3D text, simple geometry, and the ability to

import 3D models. Once you’ve assembled a 3D scene, you can add cameras, lighting, and material

shaders, and then render the result with depth-of-field effects and auxiliary channels to integrate with

more conventional layers of 2D compositing, for a sophisticated blending of 3D and 2D operations in

the very same node tree.

A 3D scene with textured 3D text, created entirely within Fusion

Particles

Fusion also has an extensive set of nodes for creating particle systems that have been used in

major motion pictures, with particle generators capable of spawning other generators, 3D particle

generation, complex simulation behaviors that interact with 3D objects, and endless options for

experimentation and customization. You can create particle system simulations for VFX or more

abstract particle effects for motion graphics.


Fusion Fundamentals | Chapter 63 Introduction to Compositing in Fusion

FUSION

A 3D particle system, also created entirely within Fusion

Text

The Text tools in Fusion are exceptional, giving you layout and animation options in both 2D and 3D.

Furthermore, within DaVinci Resolve, these Text tools have been incorporated into the Edit and Cut

pages as Fusion Titles. These title templates are compositions saved from Fusion as macros with

published controls that are visible in the Edit or Cut page Inspector for easy customization, even if

you’re working with people who don’t know Fusion.

A multi-layered text composite integrating video clips and Fusion-generated elements

And Lots More

The list goes on. With Stereo and VR adjustment nodes, Planar Tracking, Deep Pixel nodes for

re‑compositing rendered 3D scenes using Auxiliary Channel data, powerful Masking and Rotoscoping

nodes, and Warping effects, Fusion is an impressively featured environment for building worlds, fixing

problems, and flying multi-layered motion graphics animations through your programs.


Fusion Fundamentals | Chapter 63 Introduction to Compositing in Fusion

FUSION

How Hard Will This Be to Learn?

That depends on what you want to do, but honestly it’s not so bad with this PDF at your side, helping

guide the way. It’s worth repeating that this Fusion documentation was developed specifically to help

users who’ve never before worked with Fusion learn the core concepts needed to perform the basics,

in preparation for learning the rest of the application on your own.

Fusion is a deep, production-driven product that’s had decades of development, so its feature set is

deep and comprehensive. You won’t learn it in an hour, but much of what you’ll find won’t be so very

different from other compositing applications you may have used. And if you’ve familiarized yourself

with the node-based grading workflow of the DaVinci Resolve Color page, you’ve already got a leg up

on understanding the central operational concept of compositing in Fusion.


Fusion Fundamentals | Chapter 63 Introduction to Compositing in Fusion

FUSION