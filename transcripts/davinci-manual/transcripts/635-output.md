---
title: "Output"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 635
---

# Output

The Output controls let you preview the image with different stages of the Lens Reflections

effect applied.

�Select Output: Lets you choose to view the Isolated Source (to help when adjusting the Isolation

controls), Reflections Alone (showing you the flaring effect that will be applied to the image

by itself), or the Final Composite (the complete effect).

�Alpha Masks Light Sources: Check this box to use the input Alpha channel to exclude sources in

those areas from casting light rays.

�Alpha Limits Effect: Check this box to use the input Alpha channel for compositing purposes.

Unchecking means the input Alpha is ignored.

�Quality: This pop-up lets you choose how to render the effect. Options are Full, Half (Faster), and Quarter

(Fast). The tradeoff is between sharpness and speed. The actual reflection process is the same across

all quality levels. Smoother and lower resolution content will not benefit from the Full Quality setting.

Isolation Controls

The Isolation controls let you choose which highlights in the scene will generate lens reflections.

The effect of these controls can be directly monitored by setting Select Output to Isolated Source.

It’s highly recommended to customize the Isolation controls for the image at hand when using this

plugin, as even more so than other plugins, the particular highlights used will have a huge impact on

the resulting effect.

�Color Mode: A pop-up menu that lets you either choose to keep the colors of the different

highlight regions that generate lens reflections, or treat them all as grayscale brightness only

(color controls later can change the effect). Grayscale is faster to process, but Color can result in

some brilliant effects.

�Brightness: Sets the threshold at which highlights are isolated.

�Gamma: Lets you shape the isolated highlights.

�Smooth: Lets you blur details in the highlights that you don’t want to be pronounced.

�Color Filter: Lets you choose a particular color of highlight to isolate (an eyedropper lets you

select a value from the Viewer).

�Morph Operation: A pop-up lets you adjust the resulting Isolation matte (options include Shrink,

Grow, Opening, Closing), and a slider lets you define how much.

Morph Amount: Adjusts the edges of the light source based on the Morph Operation chosen.


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR

Global Controls

The Global controls let you quickly and easily adjust the overall quality of the Lens Reflections effect

using a centralized group of parameters.

�Global Brightness: Lets you raise and lower the level of all reflections. Lowering brightness is

a good way to make a large lens reflection effect more subtle, although images with small lens

reflection effects may benefit from being a little brighter.

�Global Blur: Lets you defocus all reflections. This is another good way of making lens reflection

effects of all kinds more subtle.

�Anamorphism: Lets you deform the reflection elements to simulate an anamorphic lens’

stretching effect.

�Global Colorize: Lets you adjust the color intensity of the reflections, either intensifying the color

of all reflections or desaturating it.

Presets

A Presets pop-up provides a number of different settings to get you started. Selecting a preset

populates the Reflecting Elements parameters below, at which point you can customize the effect to

work best with the image at hand. It’s highly recommended to customize these effects to suit the type

of highlights in your image, in order to get the best results.

Reflecting Elements

There are four groups of Reflecting elements, each with identical controls. This lets you create

interactions combining up to four sets of reflections. The controls found within each group are

as follows.

�Brightness: Lets you adjust the intensity of that reflection.

�Position in Optical Path: Lets you shift the reflection according to an element’s position in the

lens. Practically, this means that positive values will enlarge an inverted reflection based on the

highlights, while reducing values toward 0 will shrink the reflection, and pushing this into negative

values will invert the reflection and pull it into the opposite direction as it begins to enlarge again.

A value of –1 positions the reflection right over the highlight that creates it.

�Defocus type: Lets you choose what kind of blur to use, choices include Box blur, Triangular blur,

Lens blur (the most processor intensive), and Gaussian blur (the default).

�Defocus: Lets you choose how much to blur that element.

�Stretch: Lets you give the flare an anamorphic widescreen look.

�Stretch Falloff: Lets you taper the edges for a less uniform stretching effect.

�Lens Coating: A pop-up lets you choose common colors such as purple, green, and yellow that

correspond to different anti-reflective lens coatings, as well as a selection of other vibrant colors.

Defaults to none. When you choose any other option, a color control and eyedropper let you

manually choose a color or pick one from the image. A Colorize slider lets you vary how much to

tint the reflection by the selected color, although setting Colorize to 0 lets the flare take its color

from the source highlights of the image, which can sometimes give you the most interesting look.


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR

Light Rays

A “rays of light” effect that simulates volumetric lighting emerging from light sources defined by a

threshold you define. The effect mimics what are sometimes called “god rays” in the sky, or other

highly directional glow effects.

Main Controls

The Main controls include:

�Select Output: Lets you preview the image with different stages of the Lightray effect applied,

viewing the Final Image, Lightrays Alone, and Source Regions.

�Source of Rays: Lets you choose the emitter of the rays, using Bright Regions or Edges.

�Source Threshold: A slider that lets you choose the limit at which bright areas of the

image emit rays.

�Alpha Masks Light Sources: Check this box to use the input Alpha channel to exclude sources in

those areas from casting light rays.

�Alpha Limits Effect: Check this box to use the input Alpha channel for compositing purposes.

Unchecking means the input Alpha is ignored.

Position

Position parameters let you define the direction rays take.

�Ray Directions: A pop-up menu that lets you choose either “From A Location,” which exposes

controls to let you choose an X or Y position to define a point of origin that defines the angle of

the light beams, or “At an Angle,” which exposes controls to let you choose an overall orientation

for the rays.

Appearance

Appearance parameters let you customize the ray effect.

�Ray Dropoff: A pop-up with four options.

Default (soft): Produces soft, indistinct rays of light that appear to fade away as they stream out.

Keep Shape of Source: The edge of the light rays are defined by the shape that emitted them.

CCD Bloom Harsh: Severely raises the brightness of the part of the image that’s emitting rays as

Length is raised, resulting in harsh glow or bloom in the image.

CCD Bloom Soft: Gently raises the brightness of the part of the image that’s emitting rays as

Length is raised, resulting in a very gentle lightning of the image.

�Length: Lets you make the rays longer or shorter.

�Soften: Lets you blur the rays being emitted.

�Brightness: Lets you adjust how bright the rays are.

�Gamma: Adjusts the brightness of the ray effect using a gamma curve.

�Saturation: Adjusts the intensity of the ray’s color.

�Color: A color picker and eyedropper let you define a color with which to tint the rays.

�Composite Type: Lets you choose a composite mode to use to blend the glow effect with the

image. Defaults to Add, which is good for hotter, more intense rays. Screen lets you create more

gentle rays, while other composite modes let you create other varied effects.

�Bright Region Recovery: Adjust this slider to reclaim some image detail in areas that are blown out

by the rays.


Resolve FX Overview | Chapter 160 Resolve FX Light

COLOR

Chapter 161

Resolve FX

OpenColorIO

OpenColorIO (OCIO) is an open color management system created by the

Academy Software Foundation. It is used by many professional vfx and editing

programs (including DaVinci Resolve and Fusion) to ensure color accuracy

throughout the production pipeline.

These are technical FX to integrate OpenColorIO data into the DaVinci Resolve workflow.

Contents

OCIO CDL Transform ��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3522

OCIO Color Space����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3522

OCIO Display��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3523

OCIO File Transform������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3523


Resolve FX Overview | Chapter 161 Resolve FX OpenColorIO

COLOR

OCIO CDL Transform

The OCIO CDL Transform FX lets you create, save and apply standard Color Decision List (CDL)

grades to or from the node. A CDL exchanges basic primary color information from one application

to another.

�CDL File: Clicking Load will allow you to load a Color Decision List (.cc or .ccc) file to the controls.

CC is a single CDL and CCC is an archive of multiple CDL looks. If loading a CCC file, another

CCID field appears and lets you chose the name or number of the index. Type the name or

number and press Reload to load the new version.

�Reload: Lets you reload a CDL after choosing another name or number from the

index of a CCC file.

�Export: Exports the current settings in Controls as a new .cc file.

�CDL Controls: These controls let you modify the basic color information of the node that can

be exported as a CDL file for other applications to read. These controls, Slope, Offset, Power

and Saturation, are how the American Society of Cinematographers encode color information.

The color controls are self explanatory, but without getting deep into the math, these controls

allow you to adjust color in either a film or video based manner as below:

�Slope is essentially Gain

�Offset is essentially Exposure

�Power is Essentially Gamma

�Contrast is a combination of Slope and Offset

�Lift is a combination of Slope and Offset

�Forward: Applies the CDL changes to the node.

�Reverse: Attempts to remove the CDL changes from the node. For example, if you receive some

footage with a baked in color grade, reversing the CDL used will remove those changes back to

the original ungraded source material. However, not all color correction can be undone.

�Export: Exports the current settings in Controls as a new .cc file.

OCIO Color Space

This effect allows you to to do color space transforms using an OCIO config file (.ocio).

�OCIO Config File: Click Browse to load a .ocio config file for the color space transform.

�Source Space: Based on the config file, the available source color spaces are listed here. The

content of this list is based solely on the loaded profile and hence can vary immensely.

�Output Space: Based on the config file, the available output color spaces are listed here. The

content of this list is based solely on the loaded profile and hence can vary immensely.

�Look: Installed OCIO Color Transform Looks appear in this menu. If no looks are installed, this

menu has only None listed as an option.

�Forward: Applies the Color Space changes to the node.

�Reverse: Attempts to remove the Color Space changes from the node.


Resolve FX Overview | Chapter 161 Resolve FX OpenColorIO

COLOR