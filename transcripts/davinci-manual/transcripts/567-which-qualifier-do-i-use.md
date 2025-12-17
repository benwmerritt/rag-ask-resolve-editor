---
title: "Which Qualifier Do I Use?"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 567
---

# Which Qualifier Do I Use?

The Qualifier palette’s four modes offer you the flexibility to use the best keyer for the job when it

comes to isolating a range of color or brightness values. In some cases, keys that are difficult to pull

using some modes are easier to pull using others. Here’s a brief summary:

HSL: In many instances, the HSL keyer is not as immediately accurate as the 3D keyer,

and will include a broader portion of the image for any given sample. On the other

hand, if the 3D keyer is not giving you satisfactory results for a particular shot, the HSL

keyer can sometimes do a better job. Because of its interface, the HSL keyer makes it

easier to “fine-tune” the range and softness of each individual color component that’s

sampled, in order to improve the result. The HSL keyer also gives you the option of

disabling color components that you don’t want to contribute to the final key, so that you

can pull a saturation-only key, or a hue-only key, for instances where that may solve the

issue at hand.


Color | Chapter 137 Secondary Qualifiers

COLOR

RGB: The RGB keyer shares many of the limitations and advantages of the HSL keyer,

but since you’re sampling and adjusting red, green, and blue color components, the

specificity with which you can fine-tune the resulting key works much differently.

LUM: The LUM keyer works specifically to isolate parts of the image based on image

tonality, lightness, or darkness. This is the perfect tool when you’re trying to isolate

highlights or shadows in the image, which let you solve a multitude of different creative

and technical issues. The LUM keyer is identical to using the HSL keyer with the Hue and

Saturation qualifier controls turned off.

3D: The 3D keyer is a good one to start with if you’re trying to isolate a range of color

such as a blue shirt, a cyan sky, a performer’s skin tone, or the orange leaves of a tree

in autumn. Its interface of drawing lines over the part of the image you want to isolate,

coupled with its high quality and extreme specificity, make it a fast and accurate tool

to use in a variety of circumstances. However, the 3D keyer always samples every

color component of the image; it’s not useful when you want to isolate specific color

components, such as luma only, or hue and saturation without luma. The 3D keyer’s

greatest strength, the speed with which you can sample areas of the picture to include

(or exclude) from the final key, is also occasionally a weakness with images where your

initial samples aren’t giving you satisfactory results, because there aren’t many ways to

fine tune the key as it’s being generated (although you can manipulate the result). On

the other hand, for most images you would want to qualify, two or three samples is all

you need, in conjunction with using the Matte Finesse controls to adjust the resulting

key. If you need to do some compositing in the Color page, the 3D keyer also does an

excellent job doing blue and green screen keying to create transparency, and has a built-

in Despill control as well.

The following two sections provide an overview of how to use the 3D and HSL keyer modes in

DaVinci Resolve.

Set the Default Qualifier Mode

You can set your favorite qualifier to open as the default when you apply a qualifier on a new clip on

the timeline. This can save a significant amount of clicks over the course of a project. As expected, if a

qualifier other than the default has been applied to the clip, that qualifier will open instead.

To change the Default Qualifier, click on the Qualifiers (3-dot) Option menu, select Default Qualifier,

and choose an option from the list.

Changing the Default Qualifier to 3D, which will now open the 3D

qualifier instead of the HSL qualifier on new clips


Color | Chapter 137 Secondary Qualifiers

COLOR

Basic Qualification Using the 3D Qualifier

The 3D Qualifier mode offers a fast, simple way of pulling a key to isolate a range of color in the image,

by drawing lines over the parts of the image you want to key. Each line you draw over the image adds

to or subtracts from the cloud of values you’re carving out of a three-dimensional representation of all

available colors; you don’t see this representation, but this “under the hood” functionality is what gives

the 3D keyer its name.

The 3D keyer is a general-purpose keyer, letting you isolate any color you like. However, the 3D keyer

is not good at pulling luma-only keys. If you’re looking to isolate a range of luma values in the image,

you should use the LUM mode.

To use the 3D mode to isolate a subject in the Viewer:


Open the Qualifier palette, choose the 3D icon in the upper right and click the eyedropper.


Click and drag across the part of the image you want to isolate to draw a line. Lines that add to the

key are colored blue.

Drawing a line to create a key using the 3D qualifier


To see the key you’re creating as you work, click the Highlight button in the Viewer Options

toolbar at the top of the Viewer. As you draw the line, the viewer will update to show your current

key in real time.

Viewing the key using the Highlight button


Color | Chapter 137 Secondary Qualifiers

COLOR


If necessary, draw additional lines to add more of the image to the key you’re creating. Ordinarily,

it’s a good idea to not to draw more then two or three lines to sample the part of the image you’re

trying to isolate. A few long strokes are better than several short ones. Ideally, you want the key

you’re pulling to have a somewhat soft edge, which makes it easier to use the Matte Finesse

controls to fine-tune your result later on. If you draw too many lines to sample the image, the result

can be a key with hard, jagged edges that can sometimes be more difficult to adjust later on.

A hard-edged key created with three samples


Alternately, if there are parts of the image that are included in the key that you want to omit, hold

the Option key down and draw a line over these areas. You can see that Option-drawn lines

are red, and these subtract areas from the key you’re creating. Again, try not to overdo drawing

subtractive red lines, as you can end up with an overly hard-edged key that’s difficult to adjust

using other controls in the next few steps. Additionally, you can still use power windows in

conjunction with the 3D qualifier to exclude specific parts of the image.

Blue lines add to the key and a red line subtracts the

grass from the key, as seen with the highlight turned off


If you find yourself wondering whether a particular sample in the list at left is doing any good, you

can click the color patch at the left of any entry in the list to toggle that sample off and on. If you

decide you don’t need a particular sample, click the trash can button at the right to delete it.


Color | Chapter 137 Secondary Qualifiers

COLOR

Controls for toggling samples off and on,

and deleting them from the list


When you’re satisfied that the key is good enough to start fine-tuning, stop drawing lines. It’s

all right if there’s a bit of noise, speckling, or if there are small holes in the key you’re creating,

because you can take care of these using the Matte Finesse controls.

A sampled key that’s ready for further refinement

Nearly every key you pull will benefit from some further “post-key” refinement. What this means is

that, once you’ve created the best key you can procedurally through sampling the image, you can

now adjust the resulting key itself, which is just a gray-scale image, to improve the isolated result.

This is what the Matte Finesse controls are for.


Color | Chapter 137 Secondary Qualifiers

COLOR

Matte Finesse controls


The three most common methods of key refinement using the Matte Finesse controls are to

increase Clean Black to fill in “holes” in the parts of the image you’re omitting (the background),

increase Clean White to close holes in the part of the image you’re isolating (the foreground), and

then use Blur Radius and In/Out Ratio controls to blur the edge of the key and push it in and out.

Using these controls, you can vastly improve nearly any key without the need to endlessly readjust

the Qualifier controls.

More information about using the Matte Finesse controls appears later in this chapter.


When you’re finished, click the Highlight control to turn the highlight off, and make whatever

adjustment you need. In this example, the orange of the helicopter will be adjusted using the Hue

control to make it blue instead.

Adjusting the orange color of the helicopter to be blue instead


Color | Chapter 137 Secondary Qualifiers

COLOR