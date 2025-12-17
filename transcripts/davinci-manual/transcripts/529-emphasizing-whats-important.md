---
title: "Emphasizing What’s Important"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 529
---

# Emphasizing What’s Important

Another important aspect of the color correction process is the ability to make adjustments

to emphasize or de-emphasize specific elements within the frame. It’s similar in concept to

equalization in audio mixing, in that you’re choosing which color values to boost or suppress using a

variety of techniques.

This can be done to direct the viewer’s gaze, for example by surrounding a specific part of the image

with a window, which lets you restrict specific adjustments made to the inside and outside of the

window’s shape.

Drawing a window to isolate a region of the picture to highlight

Specific alterations can also be made to prevent audience distraction. For example, a low-saturation

monochromatic tint may be a pleasing look overall, but in the soft wash of color, the viewer might lose

track of the watch that’s preoccupying the protagonist. Using tools such as the Hue curves and HSL

Qualifier, you can quickly and easily tune the color of the woman’s hands and of the watch to guide the

viewer’s eye, and bring some needed depth to the scene.

Source image

Curves and HSL qualification used to

distinguish hands and highlight watch

For more information on Power Windows, see Chapter 136, “Secondary Windows.” For more

information on Hue curves, see Chapter 132, “Curves.”


Color | Chapter 125 Introduction to Color Grading

COLOR

Audience Expectations

There is another family of tools, the HSL, RGB, and Luma Qualifiers, that provide even more specific

control, and they’re useful for adjusting ranges of color to either play into or against the audience

expectations for color in a scene. Substantial research into what has been termed “memory color”

shows that people have finely tuned expectations for the hues of particular subjects, such as

flesh tone, foliage greens, and sky blues. Deviation from these expectations can create a sense of

something being not quite right, which can be either detrimental or beneficial, depending on your

goals for a particular scene.

HSL Qualification is effectively a chroma keyer that lets you sample the image to create a key that’s

used to define where to apply a specific correction. For example, if you’re happy with the rest of the

image, but the skin tone of the actor has an unhealthy green tinge to it as a result, you can isolate the

color of that actor’s skin and adjust it to a healthier hue.

Source Image

HSL qualification on the skin

Skin now has warmer grade

Another common example is the adjustment of skies. If you’re aiming for a gorgeous summer day, a

washed out sky in the source media can be a bit of a bummer. However, using qualification it’s easy to

isolate that wedge of blue, then push and pull it into just the right amount of summertime joy.

Originally graded scene

HSL qualification of the sky


Color | Chapter 125 Introduction to Color Grading

COLOR

Corrected and sky enhanced

For more information on using qualifiers, see Chapter 135, “Secondary Qualifiers.”

Balancing Scenes

It’s rare when the uncorrected shots of a scene match one another perfectly. Even the most carefully

exposed angles of coverage can have small variances that need to be evened out. On the other end

of the spectrum, run-and-gun programs using available light often result in edited scenes with huge

changes in lighting and color as each shot cuts away to the next.

Small or large, unintended variations from one shot to the next can call undue attention to the editing, and

jar the audience’s attention in ways that throw them out of the program. Evening out these differences

and balancing the clips in each scene to match is another of the fundamental tasks of the colorist.

You know you’re finished when the color in the scene flows unnoticeably from one clip to the next.

DaVinci Resolve has a variety of tools that you can use to help you compare images with one another,

the most important of which is the Gallery, in which you can save still images of clips that you can then

compare to other clips using an adjustable split screen.

Timeline thumbnail view of unbalanced clips

Thumbnail view of balanced clips

By using the Gallery to play stills, either split or whole (flipping back and forth between the clip you’re

adjusting and the still), it becomes easier to use the extensive DaVinci Resolve toolset to match the

color and exposure of every clip in a scene.


Color | Chapter 125 Introduction to Color Grading

COLOR

Split screen of two shots

Left image corrected to match right

An additional set of features let you manage grades by copying them from clip to clip, or by linking

similar clips, either automatically, or manually using groups.

Link icon indicates clips are grouped for grading

For more information on using the Still Store, see Chapter 124, “Using the Color Page.” For

more information on grade management, see Chapter 142, “Grade Management.”

Adding Style

Of course, it’s not all about subtlety and correction. It’s often appropriate, when grading music videos

and commercials, for instance, to add some radical style to a piece. Here, too, DaVinci Resolve

provides an abundance of features for manipulating unexpected aspects of the image; for example, by

abusing the Custom Curves to create the illusion of chemical cross‑processing.

Custom Curves controls


Color | Chapter 125 Introduction to Color Grading

COLOR

Original image

Image enhanced with Curves

DaVinci Resolve’s node-based image processing makes it possible to use more exotic node structures

to create effects using composite modes, such as a colored glow generated by adding two differently

graded versions of the same image together using a Layer node.

Node tree adding two different treatments together

Original image

Enhanced and balanced final

You can also create complex node trees to build specific mattes, to use for isolating specific elements

of the image. For example, if you wanted to isolate an actor in color against a background turned

monochromatic, you can create multiple keys (pulled via HSL Qualification) and combine them using a

Key Mixer node to build that effect.


Color | Chapter 125 Introduction to Color Grading

COLOR

Node tree to isolate the man’s face and clothes

Original image

The final effect, desaturating

everything except for the man

Finally, DaVinci Resolve doesn’t just have tools governing color and contrast. A Blur palette provides

controls over blurring, sharpening, or adding mist to all or part of the image. When combined with the

other tools that are available for isolation and color adjustment, these are powerful additions to your

creative arsenal.

Defocus effect created in real time

For more information on all of these features, see Chapter 124 through Chapter 142 of

this manual.


Color | Chapter 125 Introduction to Color Grading

COLOR