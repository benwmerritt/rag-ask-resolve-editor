---
title: "Color Wheels and Bars"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 549
---

# Color Wheels and Bars

The Color Wheel palette’s Primaries Wheels mode lets you rebalance color and adjust contrast via

the traditional DaVinci controls, which govern three overlapping tonal ranges referred to as Lift,

Gamma, and Gain. The Lift/Gamma/Gain color balance and Master Wheel controls are tied to the

YRGB Lift/Gamma/Gain sliders found in the Primaries palette; adjustments made to one set of controls

are mirrored in the other.

Though they may look different, the Wheels and Bars controls both actually

adjust the same components, but in different ways.

These tonal ranges are defined by image lightness, on a scale where 0 is absolute black and

1023 is absolute white. The following illustration shows an approximation of how the Lift, Gamma,

and Gain tonal zones broadly overlap, and how each zone’s influence falls off towards the

opposing extremes of image tonality.

Lift

Gamma

Gain

Graphic displays the relationship of the Lift, Gamma, and Gain controls

over the image brightness range that they control


Color | Chapter 131 Primaries Palette

COLOR

The Lift color balance control region of influence starts at black, and then falls off through the middle

grays to diminish to no influence at white. Meanwhile, the Gamma color balance control has its

greatest influence over the image in the middle grays, and its influence diminishes towards black and

white. Lastly, the Gain control is the inverse of Lift, having its greatest effect on the image at white, with

its influence falling off to diminish at black.

Because these tonal ranges overlap so broadly, you can make very soft, subtle, naturalistic

adjustments using these controls. Furthermore, you can capitalize on their overlap by moving an

adjacent color balance control toward a color that’s complementary to an adjustment you’ve just made

to restrict further how much of the image is affected.

The following image shows the interaction of extreme corrections made to a grayscale image using

all three Color Balance controls. Lift has been pushed toward green, Gamma has been pushed toward

blue, and Gain has been pushed toward red.

Extreme adjustments showing the overlap of the Lift, Gamma, and Gain color balance controls

Notice how, even though these corrections are extreme, the colors blend smoothly. This is the reason

for the broad overlap among all three controls, and why Lift, Gamma, and Gain are so effective in

making corrections to the ambient color temperature of a scene to account for inconsistencies in

lighting or camera settings.

3-Way Master Wheel Adjustments

The Master Wheels located below the Color Balance controls let you precisely modify image contrast

by YRGB adjustments, which individually alter the black point, the white point, and distribution of

midtones that fall in between.

Lift: Lets you adjust the perceived shadow density of the image by altering the black point

of the image. Dragging the Lift master wheel to the left makes the darkest values in the

image darker, increasing the distance between the black and white points of the image,

and stretching all the midtone values in-between. Dragging the Lift master wheel to the

right makes the darkest values in the image lighter, reducing contrast and squeezing all the

midtone values between the black and white points.


Color | Chapter 131 Primaries Palette

COLOR

Gamma: Lets you adjust the overall perceived lightness of the image by altering the

distribution of midtones that fall between the Lift and Gain master wheel settings. Dragging

the Gamma master wheel to the left darkens the overall image, while dragging it to the right

brightens it. Most Gamma contrast adjustments have a minimal effect on the black and white

point of the image, but large adjustments may push either boundary of image lightness farther

out. This interaction is described in more detail below.

Gain: Lets you adjust the lightness of the highlights by altering the white point of the image.

Dragging the Gain master wheel to the left makes the lightest values of the image darker,

squeezing the midtones between the white and black points of the image. Dragging Gain to

the right makes the lightest values even lighter, eventually clipping at maximum white.

Waveform display shows the clips contrast range

These contrast adjustments are not limited by one another. For example, raising or lowering the

Gamma master wheel by a large amount may push the highlights of the image higher or the shadows

of the image lower, regardless of the current Lift or Gain contrast setting.

As a result, these controls are somewhat interactive, and you may find yourself going back and forth

between controls as you make your final contrast adjustments. This is one of the reasons a control

panel is valuable, as it allows you to adjust all three settings simultaneously.

Offset Color and Master Controls

The fourth set of Color Balance and Master Wheel controls is actually shared with the Log controls and

with the Offset sliders in the Primaries palette. These are the Offset controls, which let you make linear

adjustments to rebalance the entire tonal range of the RGB channels. There is no Y-only control for

Offset, only a Master RGB adjustment.

The Offset color balance control: Works as a simultaneous adjustment to all three Offset

sliders located in the Primaries palette; adjustments made to the Offset color balance control

also alter the Offset sliders. Used subtly, this makes it easy to neutralize color imbalances

in the darkest part of the image, while simultaneously rebalancing every other part of the

image. Used more dramatically, this control makes it easy to add a color wash throughout the

entire image.

The Offset master wheel: Acts as a global adjustment to image lightness, an operation

sometimes referred to as setup, raising or lowering all RGB channels together.


Color | Chapter 131 Primaries Palette

COLOR

When using a DaVinci Micro or Mini control panel, the Offset color balance and master controls are

adjusted via either the third trackball and ring while in Offset mode, or the fourth trackball and ring of

the DaVinci Advanced Panel in Offset mode.

Color Bars Mode

The Bars mode contains the original set of DaVinci Resolve color adjustment sliders. These sliders

serve two uses. First, they’re highly visible indicators of the individual YRGB channel adjustments

that are made using the trackballs, rings, and knobs of a grading control panel. Second, they provide

control of individual YRGB Lift/Gamma/Gain parameters using a mouse, tablet, or trackpad.

Primary grading controls

The main controls of the Bars mode are the individual Luma (or Y), Red, Green, and Blue sliders, four

each for Lift, Gamma, and Gain. These sliders provide precise Lift/Gamma/Gain style control over each

of the YRGB channels of the image. When used in conjunction with a Parade Scope video analysis of

the image, these controls can enable you to fix irregular color imbalances in specific channels quickly.

Additionally, the Luma (Y) Lift/Gamma/Gain sliders allow easy Y-only adjustments to contrast, where an

increase in contrast results in perceptually diminished color saturation. These correspond to the three

knobs arranged vertically to the left of the Trackball panel of the DaVinci Advanced control panel, or

the three left-most knobs of the DaVinci Micro or Mini control panels.

Making Y-only adjustments to contrast is a great way to increase contrast when you’re going for muted

saturation or a gritty look. This kind of adjustment is also useful in situations where you’re trying to

increase shadow density without increasing image colorfulness.

Log Wheels Mode

The Shadow/Midtone/Highlight color balance and Master Wheel controls operate independently of the

Lift/Gamma/Gain color balance and Master Wheel controls found in the Primaries mode. While the Log

mode uses the same types of controls as the Primaries mode, the way each control affects the image

is very different.

To switch between the Primaries and Log modes of the Wheels:

Choose an option from the mode drop-down, click the right mode button, or press Option-Z.


Color | Chapter 131 Primaries Palette

COLOR

Log color balance controls, with behavior that is very different from the Wheels mode color balance controls

There are two ways of using the Log mode controls. The first takes advantage of the way these

controls work to make fast, filmic adjustments to log-encoded media prior to it being normalized

or “de-logged” by operations that are performed using nodes appearing after it in the image

processing pipeline of your node tree. Normalizing or de-logging the image can be done via Color

Space Transform operations, LUTs, and manual adjustments if you’re grading using DaVinci YRGB

color science. If you’re using color management, they can be done via the Output Color Space

setting of Resolve Color Management (RCM), or via the ACES Output Device Transform (ODT).

The other way of using the Log controls is to take advantage of the more restrictive, but adjustable

tonal range of the Shadow/Midtone/Highlight controls to stylize normalized clips by tinting or

adjusting the contrast of tonally-specific regions of the image.

Whether or Not to Use Legacy Log Grading Ranges and Curve

DaVinci Resolve 12.5 introduced a modification to the Log grading controls that provides

smoother, more pleasing results using the same controls. To maintain backward compatibility

with older projects, a “Use legacy Log grading ranges and curve” checkbox in the General

Options panel of the Project Settings lets you switch your project between the older Log

control behavior and the newer one. Older projects that are opened in DaVinci Resolve have

this checkbox turned on by default, while new projects have this turned off by default.

Using the Log Mode Controls to Grade Log-Encoded Media

The Log controls are so named because they’re designed to work specifically with media with Log-C or similar

gamma and color encoding, derived from the Cineon Log gamma curve, developed by Kodak to digitally

store flat-contrast, wide-gamut image data that preserves image detail with a wide latitude for adjustment.

An example of a log-encoded clip (left), and the same clip after being normalized (right)


Color | Chapter 131 Primaries Palette

COLOR

You can debayer most raw formats to a log-encoded image in order to derive the maximum amount of

image data and adjustable latitude from that source.

For more information, see Chapter 7, “Camera Raw Settings.” However, the resulting image

needs to be normalized to occupy the final range of color and contrast that you intend for the

final result.

You can do this one of two ways:

�You can make a very careful curves adjustment in a second node to stretch the log-encoded

image out to fit the contrast profile you want. By making this adjustment in Node 2, you make room

for a customizing adjustment made using the Log controls in Node 1, prior to the normalization

adjustment. This is key.

�You can also apply a 1D Output or 3D LUT to the first node of a clip to normalize the image. This is

a faster, if less flexible operation, but a smooth tonal range may be easier to obtain. Since a LUT

applied within a node is always the last adjustment within that node’s order of operations, you can

also use Node 1’s Log controls to customize the look of the footage.

In either case, it’s important that the normalizing adjustment happens after your Log control

adjustments, for the Log control adjustments to work as they should. With your node tree set up in this

way, you’ll be monitoring an ordinary-looking image, but taking advantage of the Log mode controls’

unique tonal ranges to manipulate the log-encoded image data with great specificity.

TIP: Within corrector nodes, LUTs are applied after Log control adjustments, so if you want to

keep the number of nodes in your node tree to a minimum, you can apply a normalizing (or

de-logging) LUT to the same node with which you’re making Log adjustments, knowing that

the LUT will be properly applied after log adjustments.

For more information, see Chapter 144, “Image Processing Order of Operations.”

When using the Log mode controls, here’s a workflow to consider as you learn how they work:

�First, use the Offset master wheel to set the black point, and use the Contrast and Pivot

parameters to stretch or compress contrast as necessary to achieve the tonal range you require.

�Second, use the Offset color balance control to adjust the overall color balance of the

image to your liking.

�Third, use the Shadow/Midtone/Highlight color balance and Master Wheel controls to make

specific, targeted adjustments to the color and contrast of the image in tonal ranges that match

where that data is in the log-encoded image.

Working in this way, you’ll find that adjustments made with the Offset color balance and Master

Wheel controls and Contrast controls control the log-encoded image very nicely to create an overall

adjustment, while the Shadow, Midtone, and Highlight controls allow you to fix specific issues, such as

shadow balance and density, after your main adjustment has been set.

The following illustration shows an approximation of how the default ranges of the Shadow, Midtone,

and Highlight controls divide the tonal range of a log-encoded image.


Color | Chapter 131 Primaries Palette

COLOR

This graphic shows the tonal range of each of the Log controls when used with a log-encoded image

As you can see, when used with a log-encoded image the color interactions between each

adjustment overlap very softly, while still allowing more specific adjustments than those made by the

Lift/Gamma/Gain controls.

Furthermore, the boundaries of the Shadows, Midtones, and Highlights Log controls can be

customized using the Low and High Range parameters. This gives you added flexibility to apply more

specific contrast and color adjustments.

Once you’ve made an adjustment using Log mode controls along with a normalizing LUT or curve

adjustment, you can always apply additional nodes and use the Wheels mode of the Primaries palette

to make further alterations to the now normalized image, working as you normally would with any of

the other tools in DaVinci Resolve.

TIP: Internal to each node’s image processing order of operations, the Lift/Gamma/Gain

adjustments of the Wheels mode are applied prior to the Shadow/Midtone/Highlight/Offset

adjustments of the Log mode, so if you want to apply Log mode controls before Wheels mode

controls, then you need to use Wheels controls in a subsequently added node.

For more information, see Chapter 144, “Image Processing Order of Operations.”