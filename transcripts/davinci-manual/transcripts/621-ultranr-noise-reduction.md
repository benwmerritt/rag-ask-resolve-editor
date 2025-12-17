---
title: "UltraNR Noise Reduction"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 621
---

# UltraNR Noise Reduction

UltraNR is an AI-based noise reduction option that provides intelligently targeted noise reduction

based on the machine learning of real world video noise patterns, rather than relying on a specific

mathematical formula. This mode should give by far the best results for excessively noisy footage, as

well as slightly better results with normal noise reduction. It’s designed to give an optimum balance

between the wanted reduction of noise and the unwanted softening of the picture.


Color Page Effects | Chapter 153 The Motion Effects and Blur Palettes

COLOR

An under-exposed shot of a black dog, on a black blanket, on a black

couch. The perfect storm for video noise, as seen above.

The same shot but with the UltraNR mode in the Spatial NR

settings. The Show Patch icon has been selected, showing a white

box around where the noise pattern is being sampled.

Using UltraNR Controls

UltraNR is applied simply by selecting from the drop-down menu in the Mode section of SpatialNR.

You then just need to click on the Analyze button and UltraNR automatically analyzes a flat area of

the image that it samples to detect Luma/Chroma noise level and sets the analysis Luma and Chroma

sliders appropriately.


Color Page Effects | Chapter 153 The Motion Effects and Blur Palettes

COLOR

The UltraNR control set in the

Color page Motion Effects pane

If your results need further refinement, you can use Auto to detect the flat area and then enable the

“Show Patch” icon. A small white outline square appears on your clip, showing you where the AI

has placed its analysis point. You can then manually drag the patch (or also change its size a bit by

dragging the handles) around flat areas to detect the Luma/Chroma noise level. When you release

the mouse button, the luma and chroma for the new box location is calculated. If the results are not

ideal, then adjust the sliders to vary the analyzed luma and chroma a bit, adjusting luma first and then

chroma. Once you are satisfied with the results, you can hide the patch.

The new UltraNR mode for spatial denoising is available in the Color page in the Motion Effects >

Spatial NR pane, and in the Resolve FX noise reduction effect.

Using Noise Reduction

The following procedure suggests a method of using the Noise Reduction (NR) parameters to achieve

a controlled result.

Applying noise reduction to an image:


Enable Temporal NR by choosing 1 to 5 frames from the Number of Frames drop‑down menu.

Keep in mind that more frames dramatically increase the render time of this effect, while it may or

may not significantly improve the result, depending on your material.


Choose options from the Motion Est. Type and Motion Range drop-down menus corresponding

to how much motion is in the image. If there’s a lot of motion, you may need to choose Better and

Large. If there’s not very much motion, lesser settings may suffice.


With Luma and Chroma Threshold linked, slowly raise either parameter until you just start to see

a reduction in noise within the nonmoving areas of the image, then make smaller adjustments to

determine the maximum amount of Temporal NR you can add without creating motion artifacts, or

overly softening image detail you want to preserve.


If there’s obviously more chroma than luma noise in the image, you can disable Luma/Chroma

linking at a satisfactory level of luma noise reduction, and then raise the Chroma Threshold to

apply more aggressive Temporal NR to address color speckling in the picture.


Color Page Effects | Chapter 153 The Motion Effects and Blur Palettes

COLOR


If you’re not satisfied with the tradeoff between the maximum possible threshold of noise

reduction and the prevention of motion artifacts, you may want to adjust the Motion Threshold

setting, lowering it to omit more of the motion from the noise reduction operation, or raising it

to include more motion. If you’re still not satisfied, you can also try better Motion Est. Type and

Motion Range settings.

(Left) Before and (Right) after Temporal NR to reduce noise in unmoving areas of the image

Keep in mind that the strength of Temporal NR is to reduce noise in unmoving parts of the image.

When you’ve achieve the best tradeoff between noise reduction in the still areas and avoidance

of motion artifacts in the moving areas of the image, then it’s time to turn to Spatial NR to further

eliminate noise throughout the rest of the picture.


Enable Spatial NR by raising either the Luma or Chroma Threshold parameters, which are linked

by default, until you strike a suitable balance between the reduction of noise, and an unwanted

increase in image softness.


It’s recommended to choose the Enhanced option from the Spatial NR mode drop‑down, as it will

yield the best possible results. However, this can be processor‑intensive, so if you need better

real-time performance, you can switch the mode to Faster and compare results.


If there’s obviously more chroma than luma noise in the image, you can disable Luma/Chroma

linking at a satisfactory level of luma noise reduction, and then raise the Chroma Threshold to

apply more aggressive Spatial NR to address color speckling in the picture.

(Left) Before and (Right) after noise reduction improves the “look”


If you’ve had to use a high Spatial NR Luma or Chroma Threshold setting to reduce noise visibly,

and areas of detail look a bit chunky or aliased, you can choose a larger setting from the Radius

drop-down menu to enable a more detailed analysis of the scene.


Color Page Effects | Chapter 153 The Motion Effects and Blur Palettes

COLOR

This will result in higher visual quality, but larger NR Radius settings are more processor intensive,

and may reduce real time performance if you don’t have adequate GPU resources available to

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

effective when dealing with subjects in motion, Spatial NR is able to reduce noise everywhere in the

frame falling below its threshold, even when there’s motion. Ultimately, a combination of the two is

almost always going to be a winning combination.

Spatial NR Radius, How Large Should You Go?

Larger NR Radius settings can dramatically improve the quality of high-detail regions in shots where

you’re using aggressive Spatial noise reduction, but it’s not necessary to always jump to the large

Radius setting, which provides the highest precision. In many cases, when evaluating an image that

you’re applying noise reduction to, you may not actually be able to perceive the additional quality, and

you’ll waste processing time on an unnecessary level of correction.

It’s a good idea to make sure that you’re evaluating the full-frame image on a large enough display to

see the noise you’re working on within the viewing context of the intended audience. Zooming really

far into a clip while applying noise reduction may encourage you to use higher quality settings than

are necessary, because an excessively enlarged detail of an image lets you see subtle changes that

you wouldn’t notice at actual size.

Limiting Noise Reduction in Useful Ways

As with any other correction in the Color page, noise reduction can be limited using HSL Qualification

or Power Windows. This means you can focus your efforts on reducing noise in the most problematic

areas of an image (for example, in shadows and background regions), while sparing elements that you

don’t want to affect (such as faces or better-lit areas of the image).

Furthermore, you can use Spatial NR in lieu of Blur operations to perform a subtler form of

complexion smoothing, using the HSL qualifier or a window to isolate an actor’s skin tone for targeted

noise reduction.

Controlling the Order of Operations for Noise Reduction

You can apply noise reduction at any point in your image processing tree using a dedicated node. If

you have an image with noise that you think might be enhanced by whatever corrections you need

to make (increasing the contrast of underexposed clips often increases whatever noise is within an

image), there are two approaches to noise reduction:

�Apply noise reduction at the beginning of a node tree: This lets you pre-emptively eliminate

any noise before it becomes a problem as a result of whatever adjustments you’re planning to

make. The result can be smoother, but you may also notice that the edge detail within the image

is a bit softer.


Color Page Effects | Chapter 153 The Motion Effects and Blur Palettes

COLOR

�Apply noise reduction at the end of a node tree: The alternative is to make your adjustments first,

and then apply noise reduction in a separate node afterwards. In this case, you may find that the

noise reduced regions of the image aren’t quite as smooth, however the edge detail within the

image may be visibly sharper as a result.

�Apply noise reduction to only one color channel of an image: Using the Splitter/Combiner nodes,

you can also apply noise reduction to only one color component of an image. If you’re grading a

video clip with a noisy Blue channel, this can be a way to focus noise reduction where it’s needed.

Isolating a single color channel for noise reduction is also possible using the Channels selection

when right-clicking a node. By selecting the specific channel numbers in this node corresponding

to your color space (RGB, YUV, LAB, etc.), you can limit the noise reduction operation to the

appropriate channels only.

Neither result is universally better or worse than the other. Which is preferable depends on the image

you’re working on, and the type of result you’re looking for (you might prefer some shots to be a bit

softer, while you’d like other shots to be a bit sharper). The real point is that the node-based image

processing of DaVinci Resolve lets you choose which technique works best for you.

NOTE: If you apply noise reduction and make color adjustments within the same node, noise

reduction is processed first, followed by color adjustments.