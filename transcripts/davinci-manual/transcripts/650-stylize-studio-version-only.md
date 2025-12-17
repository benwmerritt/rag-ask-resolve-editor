---
title: "Stylize (Studio Version Only)"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 650
---

# Stylize (Studio Version Only)

A plugin that lets you apply one of a variety of painterly styles to an image based on analyses of

different paintings, in such a way as to provide a temporally stable result for moving images as the

style strokes will appear to be applied to individual objects in the scene that move and flow in a

consistent way. There are two controls:

�Styles: A pop-up menu lets you choose an artistic style to apply to the image.

�Style Scale: This slider lets you adjust how large or small the applied art strokes

should be applied.

(Top) The original image, (Bottom) The image with Style Transfer

applied and set to Dance with a Style Scale of 4

TIP: This plugin is more flexible than you think, if you apply Style Transfer in a layered

way against the original image. You can do this using a duplicate layer in the Edit page, or

using two nodes representing the Style Transfer effect and original image connected with

a Merge node in the Fusion page or a Layer node in the Color page. Once that’s set up,

simply combine the Style Transfer output with the original image using composite modes

and opacity adjustments for more sophisticated blending. In particular, using the Luminosity

composite mode lets you combine the texture from the Style Transfer while retaining the

color of the original image, or using the Saturation composite mode lets you combine the

color from the Style Transfer while retaining the texture of the original clip.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Tilt-Shift Blur (Studio Version Only)

Simulates depth-of-field effects using a progressive blur that’s applied with a generated Z-depth map.

The default settings create a “miniaturization” illusion, where the image appears to be tiny due to the

top and bottom depth-of-field settings used.

Main Controls

These controls select and control the overall effect.

�Blur Type: You can choose between Fast Blur and Lens Blur (Lens Blur is the default).

�Blur Strength: A slider lets you adjust the amount of blur you add.

Lens Iris

The Lens Iris controls are only available when Blur Type is set to Lens Blur. This is a simplified set of

controls from those of the Lens Blur filter.

�Iris Shape: Lets you choose what type of apertures you want to use, with which to influence the

shape of the bokeh effect. Aperture Shape options include Triangle, Square, Pentagon, Hexagon,

Heptagon, or Octagon shaped aperture.

�Blade Curvature: (Only available with Real and Creative Apertures) Lets you round off the edges

of the Aperture Shape you selected.

�Rotation: Lets you adjust the angle the shape appears at.

�Anamorphism: Lets you adjust the aspect ratio of this effect in order to match the lens blur

created by anamorphic lenses.

�Highlights: Lets you adjust how the highlights of the image affect the blur, dilating or eroding the

image more or less depending on how high Smooth Strength is.

Depth of Field

Additional Depth of Field settings let you adjust the depth map being used to create the

depth-of-field effect.

�Map Source: Lets you choose the source for the depth map. Custom (default) lets you create the

depth map in the effect. From Alpha In and From Second Input allow you to import depth maps

created in other nodes.

�Center X, Center Y, and Angle: These parameters let you transform the depth map.

�Focus Sweep: Lets you dial in a region based on “distance” for isolation. White areas of the depth

map are affected by the blur, while black areas of the depth map are ignored.

�In Focus Range: Lets you expand or contract the black center of the depth map that defines the

blurred region.

�Near Blur Range and Far Blur Range: Two parameters let you individually adjust the falloff of the

white bottom and top of the depth map.

�Depth Map Preview: This checkbox lets you see the grayscale depth map directly while making

these adjustments. The white area will be blurred, while the black area will be unaffected.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

TIP: To create more believable Depth of Field adjustments, use the Depth Map effect in

conjunction with the Tilt-Shift Blur effect. You can feed the results of the depth map directly

into the Tilt-Shift Blur effect as a blur map, by connecting the key output of the Depth Map

node to the key input of the Tilt-Shift Blur node, and selecting “From Alpha In” in the Map

Source dropdown in the Depth of Field section of the effect. From there adjust the Focus

Sweep to dial in the area you want to isolate. If you’re not getting the expected results, try

inverting the depth map.

Watercolor (Studio Version Only)

A variation on the Abstraction filter, this filter reduces images into simplified washes of softly blended

colors, in a very painterly fashion.

�Channels: This pop-up menu lets you choose whether to use Luminance or RGB to derive the

smoothed color from.

�Show Gradient: This checkbox lets you see the boundaries that define each area of smooth color,

based on the value you choose from the Smoothness slider below.

�Smoothness: Adjusts the amount of detail in the final result. Low smoothness values result in

more detail in the smoothed result, while higher values result in larger pools of lower detail yet

smoother color.


Resolve FX Overview | Chapter 165 Resolve FX Stylize

COLOR

Chapter 166

Resolve FX

Temporal

DaVinci Resolve comes with several Resolve FX that focus on the application of

an effect over time.

Contents

Motion Blur (Studio Version Only)���������������������������������������������������������������������������������������������������������������������������������������������� 3600

Motion Trails (Studio Version Only)������������������������������������������������������������������������������������������������������������������������������������������� 3600

General��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3600

Advanced Options����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 3600

Move Trail������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3601

Smear (Studio Version Only)���������������������������������������������������������������������������������������������������������������������������������������������������������� 3601

Stop Motion������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3602


Resolve FX Overview | Chapter 166 Resolve FX Temporal

COLOR

Motion Blur (Studio Version Only)

This effect replicates the Motion Blur panel in the Color page’s Motion Effects palette. The Resolve

FX version allows you to use these tools across the other pages in the program. Motion Blur settings

use optical flow-based motion estimation to add artificial motion blur to clips that have none. This can

be useful in cases where a program was shot using a fast shutter speed, and you later decide that the

resulting video has too much strobing. By analyzing the motion within a clip, the Motion Blur settings

can selectively apply blurring to the image based on the speed and direction of each moving element

within the scene.

Three parameters let you set how much motion blur to add, and at what quality:

�Motion Est. Type: A setting of Better provides more accurate pixel mapping at the expense

of being more processor intensive. Faster provides a more approximate result but is less

processor intensive.

�Motion Range: Determines what speed of motion to consider when defining regions

being blurred.

�Motion Blur: Raise this parameter to add more motion blur to the image, lower it to add less.

The range is 0–100, where 0 applies no motion blur, and 100 applies maximum motion blur.

�Blur Direction: Allows you to chose which way the blur extends from the current frame.

The options are: Both Directions, From Previous Frame, and Towards Next Frame.

�Granularity: Adjusts how much detail is added to the blur.

Motion Trails (Studio Version Only)

The Motion Trails effect copies the image to create ghost-like trails on moving images. This effect can

be used to simulate clips shot with long shutter speeds and analog video feedback effects.

General

The first two sliders control the number and strength of the copied frames.

�Trail Length: Determines the number of copies that are used to create the trails.

�Dropoff: Sets the fade applied to each copied frame. The Dropoff value is compounded.

For instance, using a value of .5 applies 50% opacity to the first copy, 25% to the second, 12.5% to

the third, and so on.

Advanced Options

The advanced options are used to control how the overlapping copied frames are blended.

�Composite Gamma: The Composite Gamma menu provides four options for controlling the

brightness of the overlapping frames.

Timeline: Uses the Timeline Color Space setting in the Project Settings to control the overlapping

brightness. This setting, by default, is Rec. 709, Gamma 2.4.

Rec. 709: Uses a Rec. 709 color space with Gamma 2.2 to control the overlapping brightness.

Linear: Uses Linear Gamma, often producing much stronger highlights.

Custom: Provides a custom gamma slider which defaults to Gamma of 2.4. Setting this to a value

of 1.0 is the same as setting the menu to Linear.


Resolve FX Overview | Chapter 166 Resolve FX Temporal

COLOR

�Input Alpha: The choices in the Input Alpha menu determine how the Alpha channel is used for

blending the frames. All options assume there is an Alpha channel present on the clip that has the

Motion Trail applied.

Ignore: This is the default option and will cause the alpha channel to be ignored. Disabling the Use

Alpha checkbox when Ignore is selected will cause the Alpha to act as a stencil effect for the trails.

Use in Compositing: This option uses the Alpha channel for the trails and compositing over the

lower video track, assuming the Use Alpha checkbox is enabled.