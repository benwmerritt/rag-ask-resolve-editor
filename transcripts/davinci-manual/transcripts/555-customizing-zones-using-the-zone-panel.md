---
title: "Customizing Zones Using the Zone Panel"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 555
---

# Customizing Zones Using the Zone Panel

Similarly to the controls of the Log palette, how these zones overlap can be adjusted in order to

make each zone’s controls work best for the tonal distribution of the images in any given scene.

Zone overlap is governed by individual pairs of Range and Falloff controls, so you can make precise

adjustments no matter what the distribution of tonality is in the image you’re grading. All zones are

organized and customized using the Zone panel, which is divided into the Zones sidebar to the left,

and the Zone graph to the right.

The Zone panel of the HDR palette

The Zone Sidebar

The Zone sidebar show a list of all the zones in the current preset. This list is sorted by range values,

with minimum range zones (affecting shadows) appearing at top and maximum range zones (affecting

highlights) appearing below. Clicking any zone in the list selects that zone, which also selects that

zone’s boundary handle in the Zone graph at the right.

Zone sidebar controls:

�Enable Zone toggle: Toggles let you turn each zone on and off. Disabled zones will not

be rendered.

�Max/Min button: Defines whether the adjustment of a particular zone affects the image from the

current range value and below (Max) or the current range value and higher (Min). This setting is

typically used when creating your own custom preset, to define which zones stretch down toward

the shadows and which zones stretch up toward the highlights.

�Show/Hide Zone button: This button lets you hide sets of zone controls you don’t want to adjust

any further, leaving more room in the UI and on your control surface for the zones you do want to

adjust. For example, if you decide you don’t need to use the default Black and Specular zones,

you can hide them so that only the Dark, Shadow, Light, and Highlight zones are available to

switch among. Zone controls with adjustments made to them continue to affect the image even if

the controls are hidden.

�Delete Zone button: Deletes that zone. This is primarily useful when you’re creating your own

zone preset. At the time of this writing, you cannot delete any of the default zones found in the

default Zone preset.

Additionally, you have the option of adding zones, and saving zone presets to create your own

custom ways of adjusting the image.


Color | Chapter 132 HDR Palette

COLOR

To create a new zone:


Open the Zones panel.


Click Create Zone, at the bottom of the Zones sidebar.


When the Create Zone dialog appears, choose the Zone type you want that zone to have

(Dark/Min Zone or Light/Max Zone), enter a Name, and define the Range and Falloff values.

Range, Falloff, and Zone type are editable later, so don’t worry if you don’t set them up perfectly

the first time.

The Create Zone dialog


Click Create. That zone appears added to the list, which is sorted in the order in which Range is

defined, with Dark Zones appearing at the top, and Light Zones appearing at the bottom.

Zones Graph

The Zone graph is a key component of the HDR palette’s use. Along the bottom, a scale in stops

shows the range over which the HDR palette operates. At the top, handles let you adjust the editable

range boundaries that define the tonal range of each zone’s operation, superimposed over a

histogram showing the current image as input into the current node. Running through the middle of the

Zone graph, a curve shows you all the Global and Tonal color and contrast adjustments being made

by the HDR palette in the current grade.

The relationship of the range boundaries with the source image histogram in this graph is extremely

important. The range boundary for a particular zone must intersect with the part of the source

histogram you want to adjust for the controls of that zone to have any effect. If any zone boundaries

lie outside of the histogram, that zone’s controls will do nothing. In the screenshot above, the zone’s

range boundaries all lie inside of the visible histogram, so each zone’s controls will make a predictable

adjustment to the image data in that part of the histogram.

The Zone graph


Color | Chapter 132 HDR Palette

COLOR

In the following screenshot, the Zone graph shows that the Specular zone boundary lies outside of the

source histogram for the image, so adjustments made using the Specular controls will have no effect.

For this reason, it’s a good idea to check that the zone boundaries intersect the parts of the image you

want to adjust prior to manipulating the controls, but if you notice that a particular zone’s controls aren’t

having as much of an effect on the image as you’d like, you can always move the zone boundary after

the fact to expand the range of the image that’s affected by that zone.

The Specular zone boundary lies outside of the source histogram,

excluding the Specular controls from affecting the image.

Customizing zone boundaries in this way is one of the most powerful aspects of the HDR palette,

but don’t worry that you’ll be constantly dragging zone boundaries back and forth for every shot you

grade. Generally speaking, most well-photographed scenes have similar ranges of image tonality in

each shot, so zone boundaries that have been customized for one shot from that scene will likely be

good for most clips in that scene. That said, adjusting zone boundaries is another powerful way of

tailoring a grade specifically for a clip with a unique range of contrast.

Zone Controls

(Min/Max) Range: Defines the level of image tonality at which that zone’s adjustment starts.

This value is expressed in stops.

Falloff: Adjusts how softly the adjustment in that zone will blend into the image. A value of 0

results in an immediate transition to the adjustment created in the current zone, with the color

adjustment being a sharper effect. Higher values will blend the current zone’s adjustment into

the image more softly, resulting in a more gentle and seamless transition into the effect.

Customizing and Saving Presets

If you’ve customized the Zone graph in a way that’s potentially useful for other grading situations,

you can save a preset of the Zone settings for future use. Saving, recalling, and managing these

presets is simple.


Color | Chapter 132 HDR Palette

COLOR

Methods of managing presets:

�To save a preset: Customize the Zone graph to suit your needs, then choose Save As New Preset

from the HDR palette Option menu.

�To load a preset: Choose Presets > Name of Preset > Load Preset from the HDR palette

Option menu. A new preset will be saved.

�To update a preset: Load a preset, make any changes you need to from the Zone graph,

and then choose Presets > Name of Preset > Update Preset from the HDR palette Option menu.

�To delete a preset: Choose Presets > Name of Preset > Delete Preset from the HDR palette

Option menu.

�To select the default preset: Choose Default Preset > Name of Preset from the HDR palette

Option menu. This preset will now be the one loaded initially into the HDR palette on startup.

Resetting Color and Zone Adjustments

In the HDR palette’s Option menu, there’s a Reset submenu with three commands, Reset All, Reset

Color Adjustments, and Reset Zone Definitions, which are self-explanatory. These are important

because, during the course of developing a grade, there will be many times when you’ll want to reset

your color adjustments without changing how you’ve customized the Zone graph, or vice versa.

Additionally, each of the visible reset buttons in the GUI can be used with keyboard modifiers to

specifically target what to reset. The master reset button in the HDR palette’s title bar resets the entire

palette when clicked (similar to the Reset All command). However, using keyboard modifiers while

clicking this button changes what’s reset.

�Hold down Command+Shift while clicking the master reset button to reset only the Zone graph’s

Range and Falloff controls, without resetting your color adjustments.

�Hold down Command+Option while clicking the master reset button to reset only the color

adjustments, while leaving the zones alone.

Both of these modifiers also work with the zone-specific reset controls found in the Wheels panel,

letting you reset only the Zone controls or only the Color controls of each specific zone.


Color | Chapter 132 HDR Palette

COLOR

Chapter 133

Primary

Grading Controls

This chapter focuses on the more esoteric adjustments you can make, mixing

colors between channels using the RGB Mixer.

Contents

Introduction to the RGB Mixer Palette������������������������������������������������������������������������������������������������������������������������������������ 3102

Preserve Luminance������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3104

Resetting the RGB Mixer���������������������������������������������������������������������������������������������������������������������������������������������������������������� 3104

Swap Channels Buttons������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3104

Using the RGB Mixer in Monochrome Mode����������������������������������������������������������������������������������������������������������������������� 3105


Color | Chapter 133 Primary Grading Controls

COLOR