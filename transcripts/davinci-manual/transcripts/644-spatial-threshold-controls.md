---
title: "Spatial Threshold Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 644
---

# Spatial Threshold Controls

The Spatial Threshold parameters allow you to control which image characteristics get more or less

noise reduction.

�Luma: Lets you determine how much or how little noise reduction to apply to the luma component

of the image. The range is 0–100, where 0 applies no noise reduction at all, and 100 is the

maximum amount. Too high a setting may eliminate fine detail from the image.

�Chroma: Lets you determine how much or how little noise reduction to apply to the chroma

component of the image by smoothing out regions of high-frequency noise while attempting to

preserve the sharpness of significant edge details. The range is 0–100, where 0 applies no noise

reduction at all, and 100 is the maximum amount. Too high a setting may eliminate fine color detail

from the image. However, you may find you can raise the Chroma Threshold higher than the Luma

Threshold with less noticeable artifacting.

�Luma Chroma Same Threshold: Ordinarily, the Luma and Chroma Threshold parameters are

ganged together so that adjusting one adjusts both. However, you can ungang these parameters

to adjust different amounts of noise reduction to each component of the image.

For example, if an image softens too much at a certain level of noise reduction, but you find more

color speckling than luma noise, you can lower the Luma Threshold to preserve detail while raising

the Chroma Threshold to eliminate color noise.

�Blend: Lets you dissolve between the image as it’s being affected by the Spatial NR parameters

(at 0.0) and the image with no noise reduction (100.0). This parameter lets you easily split the

difference when using aggressive spatial noise reduction.

Global Blend

�Blend: Lets you dissolve between the image with no noise reduction (1.0) and the image with both

Spatial NR and Temporal NR at their current settings (0.0).

Using Noise Reduction

The following procedure suggests a method of using the Noise Reduction (NR) parameters to achieve

a controlled result.

Applying noise reduction to an image:


Enable Temporal NR by choosing 1 to 5 frames from the Number of Frames pop-up menu. Keep in

mind that more frames dramatically increase the render time of this effect, while it may or may not

significantly improve the result, depending on your material.


Choose options from the Motion Est. Type and Motion Range drop-down menus corresponding

to how much motion is in the image. If there’s a lot of motion, you may need to choose Better and

Large. If there’s not very much motion, lesser settings may suffice.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR


With Luma and Chroma Threshold linked, slowly raise either parameter until you just start to see

a reduction in noise within nonmoving areas. Then make smaller adjustments to determine the

maximum amount you can add without creating artifacts or overly softening detail.


If there’s obviously more chroma than luma noise in the image, you can disable Luma/Chroma

linking at a satisfactory level of luma noise reduction, and then raise the Chroma Threshold to

address color speckling in the picture.


Suppose you’re not satisfied with the tradeoff between the maximum possible threshold of noise

reduction and the prevention of motion artifacts. In that case, you may want to adjust the Motion

Threshold setting, lowering it to omit more of the motion from the noise reduction operation, or

raising it to include more motion. If you’re still not satisfied, you can also try better Motion Est. Type

and Motion Range settings.

Keep in mind that the strength of Temporal NR is to reduce noise in unmoving parts of the image.

When you’ve achieved the best tradeoff between noise reduction in the still areas and avoidance

of motion artifacts in the moving areas of the image, it’s time to turn to Spatial NR to further

eliminate noise throughout the rest of the picture.


Enable Spatial NR by raising either the Luma or Chroma Threshold parameters, which are linked

by default, until you strike a suitable balance between the reduction of noise and an unwanted

increase in image softness.


It’s recommended to choose the Enhanced option from the Spatial NR mode pop-up, as it will yield

the best possible results. However, this can be processor-intensive, so if you need better real-time

performance, you can switch the mode to Faster and compare results.


If there’s obviously more chroma than luma noise in the image, you can disable Luma/Chroma

linking at a satisfactory level of luma noise reduction, and then raise the Chroma Threshold to

apply more aggressive Spatial NR to address color speckling in the picture.


If you’ve had to use a high Spatial NR Luma or Chroma Threshold setting to reduce noise visibly,

and areas of detail look a bit chunky or aliased, you can choose a larger setting from the Radius

pop-up menu to enable a more detailed analysis of the scene.

This will result in higher visual quality, but larger NR Radius settings are more processor-intensive

and may reduce real-time performance if you don’t have adequate GPU resources available to

your system.

10	 If you’ve found suitable noise reduction settings, but the result is too aggressive and makes

the image appear too processed, you can try raising the Spatial NR and/or Temporal NR Blend

parameters to fade between the noise reduction added by each set of controls, and the image as

it was before you added noise reduction.

Try Applying Temporal NR First, then Applying Spatial NR

Because Temporal NR analyzes multiple frames for its noise isolation, it tends to be better at

preserving detail accurately in regions of the image where there’s little motion. If you try applying

Temporal NR first and get a successful result, even if only in part of the image, you may reduce how

much Spatial NR you have to apply, thus improving the overall quality of your final result.

Keep in mind that while Temporal NR does a great job in unmoving parts of an image but is less

effective when dealing with subjects in motion, Spatial NR can reduce noise everywhere in the frame

falling below its threshold, even when there’s motion. Ultimately, a combination of the two is almost

always going to be a winning combination.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Spatial NR Radius, How Large Should You Go?

Larger NR Radius settings can dramatically improve the quality of high-detail regions in shots where

you’re using aggressive Spatial noise reduction, but it’s not necessary to always jump to the large

Radius setting, which provides the highest precision. In many cases, when evaluating an image that

you’re applying noise reduction to, you may not be able to perceive the additional quality. You’ll waste

processing time on an unnecessary level of correction.

It’s a good idea to evaluate the full-frame image on a large enough display to see the noise you’re

working on within the viewing context of the intended audience. Zooming really far into a clip while

applying noise reduction may encourage you to use higher quality settings than are necessary

because an excessively enlarged detail of an image lets you see subtle changes that you wouldn’t

notice at actual size.

Object Removal (Studio Version Only)

A Revival category plugin that’s best used in the Color page, Object Removal uses the DaVinci Neural

Engine to attempt to remove an object in the frame as automatically as possible. This plugin works

best when removing a moving object that passes over a temporally stable background, or dirt on the

lens of a shot where the camera is in motion. Smaller objects get better results than larger objects, but

your results really depend on the footage. Here’s a simple procedure that shows how to do this.

General

Show Mask Overlay: Lets you see the actual mask used, highlighted in red, for the

Object Removal.

Analysis

These controls are used to analyze the motion of the scene.

�Scene Analysis: Press this button to analyze the clip using the selected parameters and replace

the object with the appropriate background. You will need to press this button again if you change

any of the parameters in this section.

�Assume No Motion: If the camera has been locked off for the shot while the object moves through

it, check this box to greatly simplify the background analysis.

�Scene Mode: Provides different methods of analyzing the scene, for improving the analysis of how

the area that needs to be replaced moves, to best determine how to fill the hole left by the object

being removed.

Background: Analyzes the entire image except for the object region. Boundary analyzes the

boundary area surrounding the object region. Object is for analyzing an object that moves with the

background, like a sticker that’s on a window while the camera moves.

Boundary: Analyzes the boundary area surrounding the object region.

Object: For analyzing an object that moves with the background, like a sticker that’s on a window

while the camera moves.

�Analysis Boundary: Sets the object’s boundary size for analysis.

�Show Scene Mask Overlay: Toggles the scene mask overlay on or off, letting you see what’s

behind the mask.


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

Render

These parameters let you adjust how the Object Removal is blended into the background. The Object

Removal plugin is highly footage dependent, and you won’t always get a good result this easily.

Problems with the result are shown via gray, either gray fringing or solid gray filling the replacement

window. Gray shows you where the current settings are failing to find background content with which

to fill in the patch you’re removing.

�Search Range: If you notice while playing through the analyzed result that the object removal

mask has gray fringing on some frames, you can try adjusting the “Search Range” slider, which

is the distance, in frames, from the current frame that the Object Removal plugin is searching for

replacement image detail.

For example, if the Search Range is 20, it searches +/-20 frames from the current location,

or 40 frames total. The allowance of 10 frames means we look at every fourth frame. You will

generally get the best results for the smallest range that gives an acceptable result.

�Blend Mode: If the patch is successfully filled, but the result isn’t blending well with the

background, you can try changing the Blend mode. The default is Linear, which is a simple cloning

operation, but you can also choose Adaptive Blend, which can provide better results except in

certain situations where the edges of the replacement patch have a different color or brightness

than the background.

Clean Plate

If you’re noticing that the object removal mask is filled entirely with gray on some frames, this means

that background fill couldn’t be easily generated for those frames. In this case, you can try clicking the

“Build Clean Plate” button.

�Clean Plate Source: Lets you set the source of the clean plate. Options are Gray Image, which is

effectively no source; Internal, which takes a “best guess” approach to generating a background

with which to fill the frame and integrates this with frames that could be successfully filled in; and

External, which lets you connect your own plate from another node.

�Build Clean Plate: Executes the building of a new clean plate background based on the Clean

Plate Source parameter set.

�Show Clean Plate: Checking this box lets you see behind the mask to the clean plate behind it.

To remove a moving object from a clip:


In this example, a drone is flying through a long shot that’s being simultaneously recorded.

We’ll remove the drone using a window to identify the feature to be removed using the Object

Removal plugin.

The original shot with a drone that needs to be removed


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR

In simple cases, it’s often easiest to apply the Object Removal effect to a Corrector node, so you

can use a window or qualifier within that node to isolate the feature you want to remove. That’s

what we’ll do in this example.


Use the Window palette to draw a window around the object that needs to be removed. You’ll get

the best results using windows or masks that hug the feature being removed fairly closely.


Track or keyframe the window to move with the feature you’re removing. Again, you’ll get better

results the closer your window hugs the object being removed, and it’s good to have some

softness at the edge of this window.

The object that needs to be removed is isolated with a window


Drag and drop the Object Removal plugin onto the node in which you’ve just isolated the feature

to be removed.


Click the Scene Analysis button, and wait for the analysis to finish. If the object you’re removing is

moving but the camera is locked, you can turn on the “Assume No Motion” checkbox to improve

your results in this case.

If your footage is ideal for object removal, the object will disappear once analysis is complete,

replaced by a seamless background derived from detail found on neighboring frames.

The result after object removal analysis is complete


Resolve FX Overview | Chapter 163 Resolve FX Revival

COLOR