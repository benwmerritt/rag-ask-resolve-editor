---
title: "Image Sampling for Hue and Sat Curves"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 560
---

# Image Sampling for Hue and Sat Curves

There’s an additional way to use Hue curves in DaVinci Resolve. Whenever one of the Hue vs. Hue,

Hue vs. Sat, Hue vs. Lum, Lum vs. Sat, or Sat vs. Sat curve tabs are open, clicking or clicking and

dragging over any range of pixels within the Viewer area samples the hues and/or image tonality of

that region of the picture, and automatically places three control points on the currently open curve

that correspond to the range of color and contrast you sampled.


Color | Chapter 134 Curves

COLOR

Additional Controls in the Hue and Sat Curves

While the Hue vs. Hue, Hue vs. Sat, Hue vs. Lum, Lum vs. Sat, and Sat vs. Sat curves can be adjusted

similarly to the Custom curves, they have additional controls running underneath the curve graph.

Enable Bezier button: Turning this button on forces a curve to use Bezier control handles,

rather than the default DaVinci Resolve Curve Control points, to manipulate each control point

on the curve. With Bezier handles enabled, click any control point to reveal its two Bezier

handles. Drag either handle to alter the shape of the curve at that control point.

Six-Vector Color Patches: The Hue curves each have six buttons for automatically adding

control points to manipulate the red/yellow/green/cyan/blue/magenta ranges of hue. Clicking

any of these buttons adds three control points; two to define the outer range of hue to be

adjusted, and a middle control point that you use to make the adjustment.

Input and Output (Hue Rotate/Saturation/Lum) fields: These two number fields correspond

to the horizontal and vertical adjustment values for the currently selected control point.

Click any control point on a curve to view or alter these values. The label of the second field

depends on the curve that’s selected.

The following sections describe each available curve in more detail. Each type of curve is accessed by

selecting the appropriate icon in the upper right of the Curve Palette.

Custom

Hue vs. Hue

Hue vs. Sat

Hue vs. Lum

Lum vs. Sat

Sat vs. Sat

Sat vs. Lum

Hue vs. Hue

The Hue vs. Hue curve lets you change any hue to any other hue. In the following example, the image

on the left is the unadjusted original. The image on the right has had the orange jacket shifted to an

olive green via a set of three control points.

Changing the hue of the woman’s jacket using the Hue vs. Hue

curve; Left–original image, Right–altered image

One excellent use of the Hue vs. Hue curve is to quickly and subtly alter elements that require only

minor adjustments. For example, a sky that appears a bit too cyan can be made into a richer shade of

blue with a small adjustment.


Color | Chapter 134 Curves

COLOR

Hue vs. Hue is also useful for making more radical changes to elements that might be too noisy to key

successfully using the HSL qualifier controls. For example, red autumnal foliage blowing in the wind

might result in a chattery matte, but you can use the Hue vs. Hue curve to change reds to greens,

without having to worry about aliased matte edges giving your correction away.

Hue vs. Sat

The Hue vs. Sat curve lets you selectively alter the saturation of any hue within the image. This is a

terrific tool for creative effect, allowing you to quickly and easily boost the saturation of elements you

want to catch the viewer’s eye, while reducing the saturation of elements you’d prefer the audience

not dwell upon.

This can be extremely useful for legalizing over-saturated overshoots or undershoots during

a QC pass. For example, desaturating reds that are off the charts while leaving everything else alone.

Lowering the saturation of the woman’s jacket using the

Hue vs. Sat curve; Left–original image, Right–altered image

The Hue vs. Sat curve can also be a powerful tool for increasing the color contrast of images that

seem lackluster and flat. By boosting the saturation of colorful elements that are distinct from the

dominant palette of a scene, you can add variety to an otherwise monochromatic image.

Hue vs. Lum

The Hue vs. Lum curve lets you increase or decrease the lightness of elements of specific colors.

Darkening the woman’s jacket using the Hue vs.

Lum curve; Left–original image, Right–altered image

This is a tricky curve to use with highly compressed footage, as it can quickly reveal artifacts in the

image if you aren’t careful. However, if you’re working with very high-quality footage, this can be a

great tool to darken specific hues to add richness and depth, or to lighten colorful elements to which

you want to draw attention.


Color | Chapter 134 Curves

COLOR

Lum vs. Sat

The Lum vs. Sat curve is similar to the Custom curves in that alterations to the saturation of an image

are based on user-definable ranges of image tonality, rather than hue. In the following example,

the Lum vs. Sat curve is being used to decrease selectively the saturation of everything falling

into the highlights and shadows of the image, while increasing the saturation of everything within

the midtones.

In the following example, a vividly saturated treatment results in shadows that seem artificially colorful.

Using the Lum vs. Sat curve, it’s easy to gradually desaturate everything below a certain range, with a

nice smooth falloff.

This is an outstanding curve to use for creative effect, for example, slightly boosting saturation within

the midtones while reducing saturation in the shadows to increase the depth of the darkest portions

of the image. It’s also a great curve to use to solve QC violations. For example, if you have illegal

saturation in the highlights of an image, you can use the Lum vs. Sat curve cleanly and smoothly to

lower the specific values that are causing problems.

Selective desaturation in the shadows and highlights using the Lum vs. Sat curve;

Right–original image, Left–altered image

Sat vs. Sat

The Saturation vs. Saturation curve lets you selectively manipulate image saturation within specific

regions defined by the image’s original image saturation. Control points added to the left of this

curve affect areas of progressively lower saturation, effectively letting you increase or decrease the

saturation of lower-saturated features. Control points added to the right affect areas of progressively

higher saturation, letting you increase or decrease the most saturated features of an image.


Color | Chapter 134 Curves

COLOR

Like all curves, this operation is extremely useful for stylizing the image. You can create custom

vibrance operations, where you selectively increase the saturation of low-saturated regions of the

image in different ways to give the picture more “pop.” It’s also an excellent tool for taking care of over-

saturated areas of the picture when adhering to conservative QC requirements. You can specifically

desaturate only the most over-saturated parts of the picture, without affecting similar hues at lower

levels of saturation.

In the following example, you can see that the portion of the image with the highest saturation has

been desaturated, while the rest of the image has been left alone.

Desaturating only the highest saturated elements in the picture

by lower control points at the right of the Sat vs. Sat curve

Sat vs. Lum Curve

The inverse of the Lum vs. Sat curve, Sat vs. Lum lets you quickly adjust the luminance of pixels that

falls within a particular range of saturation. This is useful for cases where regions of the image you

want to make lighter or darker happen to coincide with an identifiably consistent range of saturation.

To help guide your adjustment, the histogram drawn for this curve lets you see how many pixels there

are at each level of saturation found within the image, with the leftmost part of the curve representing

minimum saturation, and the rightmost part of the curve representing maximum saturation. Seeing

where the levels of saturation lie in the current image help you to quickly make targeted luminance

adjustments when you sample the region of the image you want to adjust to add points to this curve.


Color | Chapter 134 Curves

COLOR

The Sat vs. Lum curve

In the following example, the right side of this curve is lowered so that the most saturated parts

of the image become darkened. You might want to make an adjustment like this to emulate one

of the properties of film, where highly saturated colors block more light from passing through the

emulsion than less saturated colors. Or, you may do this in an effort to desaturate bright colors in

highlights that might otherwise clip past maximum white. Or, you might do this to quickly darken highly

saturated skies.

(Top Left) The original image, (Top Right) The highly saturated blue sky and sea reflections are

darkened to a more intense blue by lowering the right part of the Sat vs. Lum curve (Bottom).


Color | Chapter 134 Curves

COLOR