---
title: "HDR Grading With the Primaries Palette"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 548
---

# HDR Grading With the Primaries Palette

Starting in DaVinci Resolve 17, some of the palettes of the Color page with which color adjustments

are made have been made “color space aware.” This means that the functionality of the palette will

be mostly the same no matter what Timeline Color Space you’re using, or whether you’re grading

to create SDR or HDR output. However, not every color palette has been made color space aware,

and so when using various grading controls in the Color page to grade wide-latitude images for HDR

output, if you find the controls aren’t working smoothly, you may find it useful to enable the HDR Mode

of the node you’re working on by right-clicking that node in the Node Editor and choosing HDR Mode

from the contextual menu (this is only available in Resolve Studio).

This setting forcibly adapts that node’s controls to work within an expanded HDR range. Practically

speaking, this makes it easier to work with wide-latitude signals using controls that operate by letting

you make adjustments at different tonal ranges such as Lift/Gamma/Gain or the Log controls.

Which Do I Start With, the Primaries or HDR Palette?

The HDR palette, introduced in DaVinci Resolve 17, has also been developed to work as a powerful

method of creating primary adjustments to serve as the foundation of your grade. While the Global

and Zones controls of the HDR palette operate from a different philosophy of signal adjustment,

they’re designed to let you tackle the same issues, so it’s a completely valid choice to start out using

the HDR palette instead of the Primaries palette. So, which to use?

Ultimately, this is going to come down to your comfort with the HDR palette, and your experience with

the Primaries palette. If your muscle memory of working with the Primaries palette continues to make

it the fastest way for you to dial in your adjustments, there’s no reason to stop using it now. In fact, the

Offset/Printer Points controls in the HDR palette continue to be adjustments that are distinctly different

from the functionality found within the HDR palette.

However, you should also give the HDR palette a try, because it has powerful primary grading

capabilities that aren’t possible with the Primaries palette modes. Even if the functionality is new to

you, if you give it a week you’ll find innumerable advantages to the HDR palette’s way of doing things,

even though it requires some new ways of looking at the process.

The bottom line, however, is that you’ll probably continue using both palettes. If you do, keep in

mind that in each Corrector node’s order of image processing operations, the HDR palette controls

are processed before the Primaries palette controls, largely because the HDR palette’s more

“photographic” approach to grading has been intentionally designed to meet the needs of primary

color adjustment in our new world of wide-gamut HDR mastering and output, so it’s been fit into the

image processing pipeline as the new foundation of all adjustments.

Shared Controls in the Primaries Palette

This section explains, in a generic way, how to use the common control interface conventions used by

the Wheels, Bars, and Log modes to make adjustments. It also describes the use of parameters that

are shared among all three modes.

Switching Between Primaries Tools

The icons in the upper right of the Primaries palette allow you to switch between the Primaries tools at

the click of a button.


Color | Chapter 131 Primaries Palette

COLOR

Primaries: Color Wheels

Primaries: Color Bars

Primaries: Log Wheels

Color Balance Controls

Whether you’re using the Wheels or Log controls, Color Balance controls provide a way to adjust

all three color channels of a particular range of the image simultaneously with a single move of the

pointer, according to the mode that’s currently selected. There are also a variety of keyboard modifiers

that let you make specific adjustments via the GUI. These controls also correspond to the trackballs

found on any of the DaVinci or third-party control panels, should you have one connected.

Methods of making adjustments using the Color Balance controls:

�Click and drag anywhere within the color ring: Moves the Color Balance indicator relative to its

previous position, and rebalances the three color channels in whatever range of image tonality is

governed by that control. You don’t need to drag the Color Balance indicator itself. This simulates

the kind of relative control you get when using a trackball to manipulate these parameters. As the

Color Balance indicator moves, the RGB parameters underneath change independently to reflect

the independent adjustments being made to each channel.

�Shift-click and drag within the color ring: Jumps the Color Balance indicator to the absolute

position of the pointer, letting you make faster, more extreme adjustments to the color balance

governed by that control.

�Double-click within the color ring: Resets the color adjustment without resetting the

corresponding contrast adjustment for that control.

�Command-click and drag within the color ring: Adjusts YRGB contrast identically as if you were

dragging that control’s master ring.

�Click the reset control at the upper-right of a color ring: Resets both the Color Balance control

and its corresponding master ring.

Master Wheels

The Master Wheels, located below the Color Balance controls, let you adjust the YRGB channels for

a particular range of image tonality together. This has the practical effect of letting you adjust image

lightness and contrast.

Lift, Gamma, and Gain or Shadow, Midtone, and Highlight, plus Offset master wheels to adjust contrast


Color | Chapter 131 Primaries Palette

COLOR

The Master Wheels correspond to the rings surrounding the trackballs on all of the DaVinci control

panels, which let you modify image contrast via YRGB adjustment (as opposed to modifying image

contrast via Y-only adjustment, discussed later in this chapter).

To adjust a Master Wheel:

Dragging a Master Wheel to the left makes the corresponding tonal region of the image

darker, and dragging it to the right makes that tonal region of the image lighter. The effect

will vary according to the mode you’re in. As you make an adjustment, the YRGB parameters

located underneath all change together to reflect the simultaneous adjustment you’re making

to all channels.

Numeric Parameters

Each Color Balance Control and Master Wheel pair of controls also have a set of four YRGB number

fields underneath that display the YRGB adjustment being made by both controls. These four values

encompass every color and master adjustment you can make with these controls, and they also

directly correspond to the Bars interface that mirrors the Wheels controls.

These fields can be edited like any other parameter on the Color page. Even though these values

display two decimal places of precision because of space restrictions in the interface, they really

contain three decimal places of precision since these are floating point operations; you just can’t see

the third decimal place.

To edit YRGB values directly:

�You can double-click on a field to edit its value numerically.

�You can insert the text cursor next to a value in this field, and use the Up and Down Arrow keys to

adjust the value one digit at a time.

�You can cut, copy, and paste values among fields.

�You can click on the field and drag left or right to adjust its value with a virtual slider.

The number fields for each Color Balance

Control and Master Wheel are editable.

Shared Adjustment Controls

The three modes of the Primaries palette also share two strips of controls for making more specific

adjustments to different aspects of the image, such as Contrast, Saturation, Hue, Highlight retrieval,

Color boost, and so on.

Like most parameters in DaVinci Resolve, clicking and dragging a parameter’s name or value to the left

or right lowers and raises that parameter with a virtual slider, while double-clicking that parameter’s

number lets you edit it numerically, and double-clicking that parameter’s name resets the parameter to

its default position.


Color | Chapter 131 Primaries Palette

COLOR

The top adjustment controls

�Temp: A specifically constrained Gain color balance adjustment that lets you adjust the image

along a warm/orange to cool/blue axis corresponding to the naturalistic spectrum of color

temperatures used for lighting. Raising this parameter performs a Gain color balance adjustment

toward orange, while lowering this parameter to a negative value performs a Gain color balance

adjustment toward a blue/cyan split. 0 is unity. The range is –4000 to +4000.

�Tint: A specifically constrained Gain color balance adjustment that lets you adjust the image along

a magenta to green axis corresponding to the unnatural spectrum of color temperatures found

in artificial lighting sources such as fluorescent and sodium vapor lighting fixtures. Raising this

parameter performs a Gain color balance adjustment toward magenta (sometimes referred to as

“minus green” to correct for fluorescent lighting), while lowering this parameter to a negative value

performs a Gain color balance adjustment toward green (“plus green” to correct for other kinds of

lighting). 0 is unity. The range is –100 to +100.

�Contrast: The Contrast parameters let you quickly narrow or widen image contrast about a user-

definable pivot point. Regardless of which mode you’re in, these parameters are identical. This

one parameter lets you increase or reduce the distance between the darkest and lightest values

of an image, raising or lowering image contrast. The effect is similar to using the Lift and Gain

master controls to make simultaneous opposing adjustments. Bright and dark parts of the image

are pushed apart or brought together about a center point defined by the Pivot parameter. The

“Use S-curve for contrast” setting in the General Options panel of the Project Settings (on by

default) sets the contrast control to apply an “S-curve” to the image, such that the shadows and

highlights of a signal will not be clipped when you increase the value. If you would prefer for these

contrast adjustments to be made linearly, and for the signal to be allowed to clip when you reach

the upper and lower boundaries of the video signal, you can turn this checkbox off.

�Pivot: Changes the center of tonality about which dark and bright parts of the image are stretched

or narrowed during a contrast adjustment. Darker images may require a lower Pivot value to avoid

crushing the shadows too much when stretching image contrast, while lighter images may benefit

from a higher Pivot value to increase shadow density adequately.

�Midtone Detail (MD): When this parameter is raised, the contrast of regions of the image with

high edge detail is raised to increase the perception of image sharpness, sometimes referred to

as definition. When this parameter is lowered to a negative value, regions of the image with low

amounts of detail are softened while areas of high-detail are left alone. 0 is unity. The range is

–100 through +100.

The bottom adjustment controls

�Color Boost: A non-uniform saturation operation that affects regions of low saturation more

than regions of high saturation. This is sometimes referred to as a vibrance operation. 0 is unity,

showing the original color values. Raising color boost from 0-100 increases color intensity, but low-

saturation parts of the image are raised more aggressively. Lowering color boost from 0 to -100

decreases color intensity, but low-saturation parts of the image are lowered more aggressively.

0 is unity, showing unaltered saturation. The range is –100  through +100.

�Shadows: Lets you selectively lighten or darken shadow detail. Raising this value retrieves shadow

detail recorded below 0 percent, while leaving the midtones alone. 0 is unity. The range is –100

through +100.


Color | Chapter 131 Primaries Palette

COLOR

�Highlights: Makes it easy to selectively retrieve blown-out highlight detail in high-dynamic-range

media by lowering this parameter, and achieves a smooth blend between the retrieved highlights

and the unadjusted midtones for a naturalistic result. 0 is unity. The range is –100 through +100.

�Saturation: A uniform saturation operation that raises (above 50) or lowers (below 50) the

color intensity of every color value within the image. 50 is unity, showing unaltered saturation.

The range is 0 (completely desaturated) through +100 (saturation is doubled).

�Hue: Rotates all hues of the image around the full perimeter of the color wheel. The default setting

of 50 shows the original distribution of hues. Raising or lowering this value rotates all hues forward

or backward along the hue distribution as seen on a color wheel.

�Lum Mix: Lets you control the balance between YRGB contrast adjustments you’ve made using

the Master Wheels or ganged Custom curves, and Y-only adjustments to contrast made using the

Y channel Lift/Gamma/Gain controls of the Primaries palette or the unganged Luma curve. At the

default of 100, YRGB and Y-only adjustments to contrast contribute equally. Reducing this value

diminishes the effect of Y-only contrast adjustments until, at 0, Y-only contrast adjustments are

turned off.

Additionally, you’ll notice that at the default Lum Mix setting of 100, individual adjustments to

R, G, or B using the RGB sliders or unganged Custom curves result in automatic adjustments being

made to the other two color channels in order to maintain constant Luma levels. At a Lum Mix

setting of 0, individual color channel adjustments have no effect on the other color channels.

Auto Correction

The Auto Color command provides a quick way to automatically balance the blacks and whites of a

clip based on the current frame at the position of the playhead. As of DaVinci Resolve 16, the A button

in the Primaries palette and the Shot Match command that is available from the Thumbnail Timeline

contextual menu both now use advanced algorithms, based on the DaVinci Neural Engine, to provide

superior results when automatically adjusting color balance and contrast. These controls have been

developed to provide optimal results when working in the Rec. 709 color space, and at a gamma

of 2.4, so they work well in conjunction with using Resolve Color Management (RCM) to normalize

media first.

For more information on using these, see Chapter 127, “Automated Grading Commands and

Imported Grades.”

Reset Controls

The Reset control, found at the upper right-hand corner of the Primaries palette, lets you reset every

single setting in the entire palette. However, there are a variety of parameter-specific reset controls

available to make more targeted resets.

�Each pair of Color Balance and Master Wheel controls have a reset control that resets both.

�Each numeric parameter can be individually reset by double-clicking the name of the parameter.

�The numeric parameters underneath each Color Balance and Master Wheel control pair can be

reset by double-clicking the color label that appears underneath them.


Color | Chapter 131 Primaries Palette

COLOR