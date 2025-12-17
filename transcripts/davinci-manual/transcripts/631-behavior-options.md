---
title: "Behavior Options"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 631
---

# Behavior Options

These controls adjust the fundamental parameters and modes of the 3D Keyer.

�Colorspace: This drop-down menu lets you choose whether you’re sampling colors in YUV, HSL,

HSP, or LAB colorspaces. YUV is the default, but if you find you’re not getting satisfactory results,

you can choose another colorspace from the drop-down menu to see if that works any better.

These have various theoretical differences but the best choice always depends on the task.

�Soft: Provides a softer edge to the key that is more forgiving of Chroma and Luma adjustments.

The more gentle drop-off is suitable for situations like subtle light changes across a face. Use

the Shadow/Midtone/Highlight Matte Finesse controls in conjunction with this mode to fine tune

the result.

�Flat: The default mode. Each color selected is 100% keyed, and adjustments are made for small

color variations. This is the recommended mode for chroma keying a green or blue screen.

Additionally, turning up the Pre-Filter setting in the Matte Finesse controls can make for a

smoother, flatter key.

�Tight: Only keys the exact color range picked and does not apply any softening based on color

ranges. Single pixel sharpness levels are expected. This can be used for difficult keying jobs,

requiring adjusting the filter and softness manually in the Matte Finesse controls.

�Luma: Functions similar to the Tight setting but ignores all chroma data, letting you key by

brightness level and not color.

�Despill: If you’re using the 3D qualifier to pull a blue or green screen key to create transparency,

this slider lets you adjust color correction that eliminates blue or green spill from the image, while

retaining the image’s original color.

Usage Options

The Key Map, shown in the upper left, showing a qualifier that attempts to select the sand

in the background (blue lines), while deselecting the pirate’s hats (red lines)

These settings control the user feedback tools from the 3D Keyer in the Viewer. In the Edit page, the

Timeline Viewer Overlay must be set to Open FX.

�Show Paths: A checkbox that lets you turn on and off the visibility of the lines you’re drawing to

sample the image. Turning lines off does not affect the key.


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR

�Smart Show Paths: With this checkbox enabled, the lines will only be visible as they are being

drawn, and disappear when the mouse button is released.

�Auto-B/W Highlight: With this checkbox enabled, the Viewer automatically switches to Highlight

B/W mode while drawing a line, to better show you the resulting key in real time. When the mouse

button is released, the Viewer switches back to its original viewing mode.

�Show Key Map: Check this box to show the Key Map in the Viewer. The Key Map is composed of

the Color Space box, and the Brightness Range. The Color Space box is laid out roughly in the

same manner as the Color Wheels, with primary colors laid out around its edge. The exact colors

and layout is determined by the Color Space that you choose in the 3D Keyer. The Brightness

Range is represented as a bar underneath the Color Space, with left being black and right being

white. Inside the Color Space and Brightness Range lie the individual colors that you chose with

the pickers in the Strokes List.

�Key Map Zoom: Controls the zoom level of the Key Map, so you can see finer detail, if necessary.

Key Adjustments

This set of tools allows you to manually adjust the generation of the key from the sampled colors.

Feedback from these tools can be seen in the Key Map, if enabled.

�Chroma Tolerance: Click and drag left and right to expand or contract the range of colors selected

by the key.

�Chroma Softness: Click and drag left and right to change the sensitivity to similar colors selected

by the key. This determines whether the key is a hard cutoff or a soft selection of similar colors.

�Adaptive Chroma Softness: Checking this box allows the keyer to operate consistently in both

highly saturated and desaturated regions of the image at the same time. The majority of the time

you will want to leave this on. The exception is if you are having difficulty in manually adjusting

chroma softness in Soft or Flat mode, then turning Adaptive Chroma Softness off will give you

more range to work with. Adaptive Chroma Softness is automatically disabled in Tight and Luma

modes as it is contrary to those mode’s functionality.

�Chroma Tilt: Moves your selected color region within the color space, changing its chroma based

on its vertical position.

�Chroma Shift: Moves your selected color region within the color space, changing its chroma

based on its horizontal position.

�Chroma Rotate: Moves your selected color region within the color space, changing its tint and

temperature based on its rotation around the central origin point.

�Luma Low: Expands or contracts the dark areas of the key in the brightness range.

�Luma High: Expands or contracts the bright areas of the key in the brightness range.

�Low Softness: Controls how well defined the low end of the brightness range is. This determines

whether the key is a hard cutoff or a soft selection of similar brightness levels.

�High Softness: Controls how well defined the high end of the brightness range is. This determines

whether the key is a hard cutoff or a soft selection of similar brightness levels.

TIP: All of the parameters above are key-framable, allowing you to animate the key over time.

For example, you may have qualified a shirt where the actor walks through different colored

light in a scene. By key framing the parameters above, you can hold the same key on the shirt

as it changes colors over time.


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR

Matte Finesse

You may find that sampling the screen color is not enough to overcome some problems. Issues such

as chattery edges, holes, or noise can sometimes be fixed using the Matte Finesse controls. These

controls filter the output of the Keyer and are adjustments that are made to the matte itself, modifying

the key using the frame’s content.

�Pre Filter: This slider attempts to clean up the image before colors are sampled. This adjustment

can be useful when you have footage containing MPEG blocking artifacts.

�Clean Black: Clean Black is a specialized operation that eliminates noise seen as white speckling

in the black area of a key. Raising Clean Black lets you “fill holes” in the background portion of a

key and erode translucent edges.

�Clean White: Clean White is another specialized operation that eliminates noise (seen as black

speckling when viewing a high-contrast highlight) in the white portion of a key that includes

areas of the image you’re isolating and expands the key by making light parts of a key lighter the

higher you raise this parameter, pushing light gray areas of the key toward white. The practical

result is that raising Clean White lets you “fill holes” in the foreground portion of a key and grow

translucent edges.

�Black Clip: Raising Black Clip applies a “lift” adjustment such that translucent areas of the matte

(gray areas when viewing a high-contrast highlight) are pushed toward black. The range is 0 to

100, with 0 being the default setting.

�White Clip: Lowering White Clip applies a “gain” adjustment such that translucent areas of the

matte (gray areas when viewing a high-contrast highlight) are pushed toward white. The range is 0

to 100, with 100 being the default setting.

�Blur Radius: In small amounts, blurring a key does well to take the edge off problem edges.

However, blurring a key can also feather the edges of a key past the border of the subject you’re

keying, with the result being a visible “halo” around your subject, depending on the adjustment

you’re making. The range is 0 to 2000, with 0 being the default. With such a large maximum blur

radius, combined with the capabilities that the In/Out Ratio provides in customizing the direction of

spread, you can turn some pretty precarious mattes into surprisingly smooth and useful results.

�In/Out Ratio: Using In/Out Ratio can help eliminate fringing. Raising In/Out Ratio will fill in small

black holes in the matte, while lowering In/Out Ratio below 0 will eliminate speckling by pushing

small white bits of the matte toward black.

�Morph Operation: You can choose Shrink or Grow to dilate or erode the edges of the matte, or

you can choose Opening or Closing to plug or expand holes to clean up a ragged matte.

�Morph Radius: Adjusts how much to shrink, grow, open, or close the key.

�Denoise: Provides a distinct way to post-process extracted keys to selectively reduce the noise

in a key, getting rid of stray areas of qualification and softly filling holes in a matte.

�Shadow: Adjusts key strength based on the darker parts of the original image.

�Midtone: Adjusts key strength based on the midtones of the original image.

�Highlight: Adjusts key strength based on the brighter parts of the original image.

�Post Filter: Performs a final clean-up of the key, using the original image for reference; useful for

bringing back some fine detail in sharp edges or hair.


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR

Garbage Matte

These controls let you crop out other unwanted things in the frame, such as lighting fixtures, boom

microphones, tracking patches, etc.

�Matte Shape: You can choose either a Rectangle or Ellipse with which to crop around the subject

you’re keying. Choosing None turns off Garbage Matte. When a garbage matte is enabled, the

Open FX Overlay mode of the Viewer shows an on-screen control for adjusting the shape and

position of the garbage matte.

�Edge Softness: Lets you soften the edges. Defaults to 50; the range is 0 (no softening) to 100

(maximum softening).

�Invert: Inverts the garbage matte.

�Center X and Y: Lets you adjust and keyframe the position of a garbage matte.

�Bounding Width and Height: Lets you adjust the width and height of the garbage matte.

�Rotation: Lets you adjust the angle of the garbage matte.

Output

The Output controls let you choose how the image is output, composited, and displayed in the Viewer.

�Output: This menu offers three options for which channels are output from the effect.

Alpha Highlight: Displays the transparent part of an Alpha channel as gray and the solid part of an

alpha channel in full color.

Alpha Highlight B/W: Displays the black and white Alpha channel, which is often helpful when

sampling additional areas to key.

Final Composite: The keyed image is displayed composited over any video track below it.

�Use Alpha: A common control in many Resolve FX and 3rd party Open FX plugins; this checkbox

determines if the Alpha channel is used when compositing over another video track. It can be

used instead of choosing RGB Only (Blank Alpha) from the Output menu.

To use the 3D Keyer in the Edit page:


Apply the 3D Keyer to a green screen or blue screen clip that’s on a higher track than the

background.


In the Inspector, enable the Show Paths checkbox to view the sampled areas once you begin.


From the Viewer Overlay menu in the lower-left corner of the Timeline Viewer, choose Open

FX Overlays.


In the Viewer, click and drag to draw a sampling stroke across the screen color you want

to remove.


The transparency immediately takes effect, showing the keyed subject against whatever clip

appears on the video track underneath it in the Timeline as a composite. To see the matte you

created for further adjustment, choose Alpha Highlight or Alpha Highlight B/W from the Output

drop-down menu.


If necessary, you can add or subtract areas from the screen color selection using the add/subtract

Color range controls. Alternatively, with the default Sample eyedropper selected, you can hold

down Shift to add to the screen color selection or hold down the Option key to remove from the

screen color selection.


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR

Alpha Matte Shrink and Grow

(Studio Version Only)

This filter lets you refine the edges of alpha and key mattes in a variety of ways, shrinking and growing

the edges, and opening and closing holes that appear within a matte. In the Color page, this filter can

be applied to Qualifier or Window keys that have been routed to the RGB input of a corrector node, for

adjustment and refinement, before connecting the result to the key input of a subsequent node for use

isolating an adjustment.

Applying the Alpha Matte Shrink and Grow filter to a key

matte that’s fed to the RGB input of a separate node

�Morph Operation: A drop-down menu lets you choose how you want to modify the

Alpha channel/key. You can choose Shrink or Grow to dilate or erode the edges of the matte with

great accuracy. Or, you can choose Opening or Closing to plug or expand holes within the key to

clean up a ragged matte.

�Shape: A drop-down menu lets you choose how corners and angles in the edges of the key

are handled when you grow or shrink it. Circle is the default, and results in even expansion

around the surface of the key that eventually averages all angles into a circular shape if you use

extreme Radius settings. Square averages all angles into a more rectangular shape if you use

extreme Radius settings. Diamond averages all angles into a diamond shape if you use extreme

Radius settings.

�Radius: A slider adjusts how much to Shrink, Grow, Open, or Close the key.

�Process: Lets you select specific channels to apply the Morph Operation to. Options are RGB

(Blank Alpha), Alpha (RGB Unaffected), and RGB + Alpha.

Preview Alpha: Checking this box lets you quickly see the Alpha channel that will be output from

the node.

�Manual Iteration Control: Checking this box gives you direct control on how the

operators are applied.

Operator Radius: A slider that controls the size of the operator.

Repeat Operation: A slider alters the effect of the Operator Radius setting to

create more extreme adjustments.


Resolve FX Overview | Chapter 159 Resolve FX Key

COLOR