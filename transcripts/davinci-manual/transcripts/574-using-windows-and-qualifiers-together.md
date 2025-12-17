---
title: "Using Windows and Qualifiers Together"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 574
---

# Using Windows and Qualifiers Together

Another use of windows is to act as a “garbage matte” when used together with a qualifier. By default,

when you use a window and qualifier together, a key is only output where both the window and

qualifier intersect. This makes it easy to exclude unwanted parts of a key that are too difficult to

eliminate by further refinement of the qualifier controls.

For example, the following qualification is intended to isolate the woman’s face, but some of

the similarly colored wood and sky in the background is also included.

Instead of driving yourself crazy trying to eliminate the unwanted parts of the key by modifying

the current qualification, which is doing a great job of isolating the skin tones, you could

instead use a window to isolate her face, excluding everything outside the window, and

simplifying your job considerably.

A qualified image with highlight on


Color | Chapter 138 Secondary Windows

COLOR

If she moves, then you can simply track the window to follow. For simple tracking

see Chapter 140, “Motion Tracking Windows.”

Now with additional Power Window isolation

Furthermore, you can use the window’s Invert control to do the reverse, excluding all qualified

portions of the key inside the window, and including all qualified portions of the key outside

the window.

If you need to build more complex qualifier/window combinations than this, you can add

more windows, or you can use multiple qualifiers and windows with the Key Mixer node, see

Chapter 146, “Combining Keys and Using Mattes.”


Color | Chapter 138 Secondary Windows

COLOR

Chapter 139

Magic Mask

The Magic Mask palette uses the DaVinci Neural Engine, guided by the user via a

click-based interface, to automatically create detailed masks with which to isolate

objects or humans, either whole or in part, to which you want to make secondary

adjustments in DaVinci Resolve.

This chapter describes how to guide these powerful features using the stroke and tracking controls

found within this palette.

Contents

Magic Mask v2 (Studio Version Only)��������������������������������������������������������������������������������������������������������������������������������������� 3202

Tracking�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3204

Fixing Masks with the Paint Tool������������������������������������������������������������������������������������������������������������������������������������������������ 3204

The Magic Mask Interface������������������������������������������������������������������������������������������������������������������������������������������������������������� 3206

Mask Adjustment Controls and Matte Finesse������������������������������������������������������������������������������������������������������������������� 3207

Magic Mask v1 (Legacy Version)������������������������������������������������������������������������������������������������������������������������������������������������� 3209

What Magic Mask Is Good For, and What It’s Not������������������������������������������������������������������������������������������������������������� 3212

The Magic Mask Interface������������������������������������������������������������������������������������������������������������������������������������������������������������� 3213

Magic Mask Toolbar��������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3213

Stroke List����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3214

Mask Adjustment Controls and Matte Finesse�������������������������������������������������������������������������������������������������������������������� 3215

Choosing What to Isolate��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3216

Object Mode����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3216

Person Mode����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3216

Features Mode������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3216

Identifying More Than One Person��������������������������������������������������������������������������������������������������������������������������������������������� 3217

Using Matte Finesse Controls����������������������������������������������������������������������������������������������������������������������������������������������������� 3218

Using Magic Mask as a Garbage Matte����������������������������������������������������������������������������������������������������������������������������������� 3218

Dealing With Hair�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3219

About Hats��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3221

Dealing With Accessories��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3221

Adding Strokes to Guide Mask Creation�������������������������������������������������������������������������������������������������������������������������������� 3221

Managing Strokes in the Stroke List���������������������������������������������������������������������������������������������������������������������������������������� 3225


Color | Chapter 139 Magic Mask

COLOR

Magic Mask v2 (Studio Version Only)

The underlying AI technology in Magic Mask has been entirely redesigned to both simplify the

interface and provide dramatically better results over the previous version and has been designated

Magic Mask v2. In addition to better pattern and shape recognition, you will notice the benefits in

difficult tracking situations, like objects passing in front of the mask and other depth related issues.

Magic Mask v2 user controls remain mostly the same from

the original Magic Mask with the following new changes:

•	 There are no longer separate Person or Object modes. Magic Mask v2 can handle both

on its own.

•	 Drawing Strokes is no longer necessary and has been replaced by simply performing Clicks

on the object to make a selection.

•	 A simple paint tool has been added to manually paint in or out additional regions from the

mask on a frame by frame basis.

The Magic Mask palette uses the DaVinci AI Neural Engine to automagically create a mask to isolate

one or more people or objects in the frame, guided by user-applied clicks to identify the subject for

isolation. Masks can be generated for either an entire object, person, or for specific features of that

person (their face, hair, arms, shoes, etc.). The following images show these two kinds of masks with

Highlight enabled in the Viewer. A red onionskin overlay lets you see what Magic Mask is isolating.

(Left) Using Magic Mask to isolate just skin tones, (Right) Using Magic Mask to isolate just the apron. Note how the color

of the apron and shirt are very close together, but Magic Mask understands the shape of the apron to generate the mask.

While the masks generated by Magic Mask can often be good enough to use directly for making high-

quality isolated adjustments, it won’t always give perfect results. In these cases, the Matte Finesse

controls let you make the resulting mask softer and looser, as necessary, to clear the edge of a difficult

subject you’re isolating with the help of another mask generation technique, such as a qualifier key

or window. For quick touch up work on a frame, you can also use the paint tool to manually include or

exclude regions of the mask.

Stroke Duration���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3225

Tracking Strokes to Follow Subject Motion������������������������������������������������������������������������������������������������������������������������� 3225

Methods of Moving Strokes to Follow Subject Motion��������������������������������������������������������������������������������������������������� 3226

Option Menu Commands for Removing Strokes and Tracking����������������������������������������������������������������������������������� 3227

An Example Stroke Tracking Workflow����������������������������������������������������������������������������������������������������������������������������������� 3227


Color | Chapter 139 Magic Mask

COLOR

If you’re isolating specific features of a person, you can also mix and match what you’re isolating to

create exactly the type of mask you require. In the above example, you might isolate the face, along

with exposed skin on the torso and arms, to create a mask for creating an overall skin tone adjustment

that doesn’t include the subject’s hair or clothes.

This whole process is guided by clicks you make to identify the subject. In a typical workflow, you’ll

make positive clicks (colored blue) over the person or feature you want to isolate. Then, if necessary,

you can also make subtractive clicks (colored red) over parts of the image that are not the person or

feature you’re isolating, to correct any problems you see in the generated mask.

Blue clicks identify a person or feature to isolate, while red clicks identify things that shouldn’t be

included in the mask. In this example we added a positive click (blue) to isolate the wood cutting board,

and three subtractive clicks (red) on items that were also roughly wood colored (the wood serving dish

and pepper grinder on the left, and her arm) to ensure they would never become part of the mask.

Ideally, both positive and subtractive clicks should be centered on the part of the person or object

you’re trying to add to the mask. If you don’t like the result you’re getting in the mask with a particular

click you’ve made, you can drag it to another position without clicking again; clicks are live and can be

selected using the pointer to move or delete them.

A single blue click on her back correctly masks her entire body, including arms and hair. Note Magic Mask

v2 correctly differentiates her from her reflection in the mirror, even when they are overlapping.


Color | Chapter 139 Magic Mask

COLOR

As you work, each click shows up in the Click list, which lets you select, enable/disable, delete, and

otherwise manage the different clicks you create to guide automatic mask generation.

The Click list keeps track of all clicks you’ve made.