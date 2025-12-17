---
title: "Inputs"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 445
---

# Inputs

The Primatte node includes six inputs in the Node Editor. Unlike every other tool in Fusion, the primary

orange input is labeled as the Foreground input, since it accepts the green-screen or blue-screen

image. The background input on the Primatte node is the green input; this is an optional input that

allows Primatte to create the final merged composite.

Foreground Input: The orange input accepts a 2D image that contains blue or green screen.

Background Input: The green (optional) input accepts a 2D image layered as the background in the

composite. If no image is connected, Primatte outputs the keyed foreground. Connecting an image to

the background input activates Primatte’s advanced edge blending options.

Replacement Image: The magenta (optional) input accepts a 2D image used as a source of Primatte’s

spill suppression color correction.

Garbage Matte: The gray garbage matte input accepts a mask shape created by polylines, basic

primitive shapes, paint strokes, or bitmaps masks. Connecting a mask to this input causes areas of the

image that fall within the matte to be made transparent. The garbage matte is applied directly to the

alpha channel of the image.

Solid Matte: The white solid matte input accepts a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input causes areas of the image

that fall within the matte to be fully opaque.

Effect Mask: The optional blue input expects a mask shape created by polylines, basic primitive

shapes, paint strokes, or bitmaps masks. Connecting a mask to this input limits the pixels where the

keying occurs. An effects mask is applied to the tool after the tool is processed.

NOTE: Connecting the background input without connecting the replacement image input

uses the background image as the replacement image surf spill suppression.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Basic Node Setup

A single Primatte keyer can rarely get perfect results because most green- or blue-screen shots have

problems the keyer is not made to handle. Keyers often need the help of garbage mattes or solid

mattes created with a Polygon or B-Spline node. Shots can also require more than just one keyer

to achieve perfect results. Below, the Primatte node has the blue-screen content connected to the

orange input. Unlike other Fusion nodes, the foreground gets connected to the orange input. The

result is an image with alpha that can then be connected into the foreground of a Merge node.

A Primatte node combined with a polygon matte as a garbage

matte and connected to the foreground of a Merge

Primatte Tab View Mode

At the top of the Inspector is the View Mode menu. The default selection shows the final Composite

result. You can change the view to see various intermediate stages of the keying process.

The Primatte tab View mode

�Black: Displays the foreground subject on a black or transparent background.

�Composite: The final keyed image with spill suppression, composited over the image connected

to the green Background Input on the node.

�Defocus Foreground: Displays the output of the Pre Matte key.

�Processed Foreground: Displays the alpha of the key before being combined with solid and

garbage masks. When displaying the matte, set the viewer to show the alpha channel.

�Hybrid Matte: Displays the matte generated when the Hybrid Rendering checkbox is enabled.

Best viewed when adjusting the Hybrid Blur and Hybrid Erode sliders.

�Lighting Foreground: Displays the foreground subject over the optimized artificial backing screen

that the Adjust Lighting mode creates.

�Lighting Background: Displays the optimized artificial backing screen that the Adjust Lighting

mode creates.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

The Primatte tab Inspector

Primatte Tab

The core functionality for Primatte is found in the Primatte tab. The basic workflow is based on

selecting one of the operational mode buttons and then scrubbing over areas in the viewer.

Lock Color Picking

Activate this button once you finished adjusting your key to prevent making accidental changes in

the viewer.

Auto Compute

The Auto Compute button is likely the first button pressed when starting to key your footage. Primatte

automagically analyzes the original foreground image, determines the backing color, and sets it as the

central backing color. Then, using that information, another analysis determines the foreground areas.

A Clean FG Noise operation is performed using the newly determined foreground areas, and Primatte

renders the composite.

NOTE: The Auto Compute button may make the next three buttons—Select Background

Color, Clean Background Noise, and Clean Foreground Noise—unnecessary and make your

keying operation much more straightforward. Clicking Auto Compute automatically senses

the backing screen color, eliminates it, and even gets rid of some foreground and background

noise. If you get good results, then jump ahead to the Spill Removal tools. If you don’t get

satisfactory results, continue from this point using the three buttons described below.

Select Background Color

Clicking the Select Background Color button allows you to select the screen color by scrubbing in the

viewer. It uses the traditional Primatte method of taking the sampled backing screen color, projecting


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

a line in the opposite direction on the hue wheel, and generating artificial pixels that may represent

the FG object. Then, using the artificially generated foreground pixels, it internally does the Clean

FG Noise operation and creates the shape of the middle and outer polyhedrons. It then renders the

composite using these generated polyhedrons. This does not automatically use the Adjust Lighting

functionality, as it must be selected in a separate operation.

Clean Background Noise

Clicking this button helps to remove any white regions in the dark screen area (“noise”), or shades of

the screen color that did not get picked up on the first sample. Once you click the button, scrub the

mouse pointer over areas in the viewer to sample white-ish noise regions.

Clean Foreground Noise

If there are dark transparent regions in the middle of the mostly white opaque foreground object, click

the Clean Foreground Noise button and scrub over the dark pixels in the foreground area until that

area is as white as possible.

Spill Sponge

The Spill Sponge is the quickest method for removing color spill on your subject. Click the Spill

Sponge button and scrub the mouse pointer over a screen color pixel, and the screen color

disappears from the selected color region and is replaced by a complementary color, a selected color,

or a color from a replacement image. These options are set in the Replace tab. Additionally, use the

tools under the Fine Tuning tab or use the Spill(+) and Split(-) features to adjust the spill.

Matte Sponge

Sometimes in the Primatte operation, a 100% opaque, foreground area (all white) becomes slightly

transparent (gray). To clean those transparent areas, click the Matte Sponge button and scrub over the

transparent pixels. All the spill-suppression information remains intact.

Restore Detail

Clicking Restore Detail and scrubbing over background regions in the viewer turns completely

transparent areas translucent. This operation is useful for restoring lost hair details, thin wisps of

smoke, and the like.

Make Foreground Transparent

When this button is selected, the opaque foreground color region sampled in the viewer becomes

slightly translucent. This operation is useful for the subtle tuning of foreground subjects, which are

otherwise 100 percent covered with smoke or clouds. It can be used only one time on a particular

color. For a more flexible way to thin out a color region, and to be able to take multiple samples, use

the Matte(-) tool.

Spill(+)

Clicking the Spill(+) button returns the color spill to the sampled pixel color (and all colors like it) in

the amount of one Primatte increment. This tool can be used to move the sampled color more in the

direction of the color in the original foreground image. It can be used to nullify a Spill(-) step.

Spill(-)

Clicking the Spill(-) button removes from the sampled pixel color (and all colors like it) in the amount of

one Primatte increment. If spill color remains, another click using this operational mode tool removes

more of the color spill. Continue using this tool until all color spill has been removed from the sampled

color region.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Matte(+)

Clicking the Matte(+) button makes the matte more opaque for the sampled pixel color (and all colors

like it) in the amount of one Primatte increment. If the matte is still too translucent or thin, another click

using this operational mode tool makes the sampled color region even more opaque. This can be

used to thicken smoke or make a shadow darker to match shadows in the background imagery. It can

only make these adjustments to the density of the color region on the original foreground image. It can

be used to nullify a Matte(-) step.

Matte(-)

Clicking the Matte(+) button makes the matte more translucent for the sampled pixel color (and all

colors like it) in the amount of one Primatte increment. If the matte is still too opaque, another click

using this operational mode tool makes the sampled color region even more translucent. This can be

used to thin out smoke or make a shadow thinner to match shadows in the background imagery.

Detail(+)

When this button is selected, the foreground detail becomes less visible for the sampled pixel color

(and all colors like it) in the amount of one Primatte increment. If there is still too much detail, another

click using this operational mode tool makes more of it disappear. This can be used to remove smoke

or wisps of hair from the composite. Sample where detail is visible, and it disappears. This is for

moving color regions into the 100% background region. It can be used to nullify a Detail(-) step.

Detail(-)

When this button is selected, foreground detail becomes more visible for the sampled pixel color (and

all colors like it) in the amount of one Primatte increment. If detail is still missing, another click using this

operational mode tool makes detail more visible. This can be used to restore lost smoke or wisps of

hair. Sample where the smoke or hair just disappears and it returns to visibility. Use this for restoring

color regions that were moved into the 100% background region. It may start to bring in background

noise if shooting conditions were not ideal on the foreground image.

Algorithms

There are three keying algorithms available in the Primatte keyer:

�Primatte: The Primatte algorithm mode delivers the best results and supports both the Solid Color

and the Complement Color spill suppression methods. This algorithm uses three multifaceted

polyhedrons (as described later in this section) to separate the 3D RGB colorspace. It is also

the default algorithm mode and, because it is computationally intensive, it may take the longest

to render.

�Primatte RT: Primatte RT is the simplest algorithm and therefore the fastest. It uses only a single

planar surface to separate the 3D RGB colorspace (as described later in this section) and, as

a result, does not separate the foreground from the backing screen as carefully as the above

Primatte algorithm. Another disadvantage of the Primatte RT algorithm is that it does not work well

with less saturated backing screen colors, and it does not support the Complement Color spill

suppression method.

�Primatte RT+: Primatte RT+ is in between the above two options. It uses a six planar surface color

separation algorithm (as described later in this section) and delivers results in between the other

two options in both quality and performance. Another disadvantage of the Primatte RT+ algorithm

is that it does not work well with less saturated backing screen colors, and it does not support the

Complement Color spill suppression method.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Hybrid Rendering

After sampling the backing screen color and producing acceptable edges around the foreground

object, you sometimes find a transparent area within the foreground subject. This can occur when

the foreground subject contains a color that is close to the backing screen color. Removing this

transparency with the Clean FG Noise mode can cause the edge of the foreground subject to pick

up a fringe that is close to the backing screen color. Removing the fringe is very difficult without

sacrificing quality somewhere else on the image. The Hybrid Render mode internally creates two

keying operations: Body and Edge. The optimized Edge operation gets the best edge around the

foreground subject without any fringe effect. The Body operation deals with transparency within the

foreground subject. The resultant matte is created by combining these two mattes, and then blurring

and eroding the foreground subject in the Body matte and combining it with the edge matte.

To use Hybrid Rendering, start by keying the main foreground area using the Select Background Color

mode (or any of the other Primatte backing screen detection methods). Activate the Hybrid Rendering

checkbox. Lastly, select the Clean FG Noise button and scrub over the transparent area. The Hybrid

Render mode performs the “Body/Edge” operation. The result is a final composite with perfect edges

around the foreground subject with a solid foreground subject.

Hybrid Blur

Blurs the Body matte that has been automatically generated when Hybrid Rendering is activated.

Hybrid Erode

This slider dilates or erodes the Hybrid matte. You can view the results by selecting Hybrid matte in

the View Mode menu.

Adjust Lighting

Before applying the Adjust Lighting operation, it is necessary to determine the backing screen color

using Auto Compute or Select Background Color. After performing one of those operations, click

on the Adjust Lighting button. Primatte generates an artificial clean plate and uses it to generate an

evenly lit backing screen behind the foreground object. The default setting should detect all the areas

that contain foreground pixels and deliver a smooth backing screen for the keying.

Lighting Threshold

Should Adjust Lighting fail to produce a smoother backing screen, adjust the Lighting Threshold slider

while viewing the Lighting Background setting in the View Mode menu. This displays the optimized

artificial backing screen that the Adjust Lighting mode creates.

Crop

This button reveals the Crop sliders to create a rectangular garbage matte with the Primatte node. As

opposed to Fusion’s Crop tool, this does not change the actual image size.

Reset

Resets all the Primatte key control data back to a blue- or green-screen.

Soft Reset

Resets just the Primatte parameters used since the Select Background Color operation

was last completed.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

The Primatte Fine Tuning tab

Fine Tuning Tab

The Fine Tuning tab can make refined adjustments to the spill suppression, density of the matte, and

semitransparent areas. These sliders provide a bit more granularity over the Spill(+)(-), Matte(+)(-) and

Detail(+)(-) buttons in the Primatte tab.

Selected Color

This shows the color selected (or registered) by the scrubbing in the viewer while the Fine Tuning tab

is selected.

Fine Tuning Sliders

The color of the scrubbed pixel is registered as a reference color for fine tuning. It is displayed in the

Color swatch. To perform the tuning operation, sample a color region on the image, and adjust one of

the Fine Tuning sliders to achieve the desired effect.

Spill

The Spill slider can be used to remove spill from the selected color region. The more to the right the

slider moves, the more spill is removed. The more to the left the slider moves, the closer the color

component of the selected region is to the color in the original foreground image. If moving the slider

to the right does not remove the spill, resample the color region and move the slider again.

These slider operations are additive. The result achieved by moving the slider to the right can also be

achieved by clicking on the color region using the Spill(-) operational mode.

Transparency

The Transparency slider makes the matte more translucent in the selected color region. Moving

this slider to the right makes the selected color region more transparent. Moving the slider to the

left makes the matte more opaque. If moving the slider to the right does not make the color region

translucent enough, resample the color region and again move the slider to the right. These slider

operations are additive. The result achieved by moving the slider to the right can also be achieved by

clicking on the color region using the Matte(-) operational mode.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Detail

The Detail slider can be used to restore lost detail. After selecting a color region, moving this slider to

the left makes the selected color region more visible. Moving the slider to the right makes the color

region less visible. If moving the slider to the left does not make the color region visible enough,

resample the color region and again move the slider to the left.

These slider operations are additive. This result achieved by moving the slider to the left can also be

achieved by clicking on the color region using the Detail(-) operational mode.

The Primatte Replace tab

Replace Tab

The Replace tab allows you to choose between the three methods of color spill replacement as

covered in detail in the Spill Sponge section above. There are three options for the replacement color

when removing the spill. These options are selected from the Replace mode menu.

Replace Mode

�Complement: Replaces the spill color with the complement of the screen color. This mode

maintains fine foreground detail and delivers the best-quality results. If foreground spill is not a

significant problem, this mode is the one that should be used. However, If the spill intensity on

the foreground image is rather significant, this mode may often introduce serious noise in the

resultant composite.

�Image: Replaces the spill color with colors from a defocused version of the background image or

the Replace image, if one is connected to the Replace input (magenta ) on the node. This mode

results in a good color tone on the foreground subject even with a high-contrast background.

On the negative side, the Image mode occasionally loses the fine edge detail of the foreground

subjects. Another problem can occur if you later change the size of the foreground image against

the background. Since the background/foreground alignment would change, the applied color

tone from the defocused image might not match the new alignment.

�Color: Replaces the spill color with a solid color. When this option is selected, a color swatch

and R,G,B sliders are displayed for selecting the color. Changing the palette color for the solid

replacement, you can select a good spill replacement that matches the composite background. Its

strength is that it works fine with even severe spill conditions. On the negative side, when using

the Solid Color Replacement mode, fine detail on the foreground edge tends to be lost. The single

palette color sometimes cannot make a good color tone if the background image has some

high‑contrast color areas.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

The Primatte Degrain tab

Degrain Tab

The Degrain tab is used when a foreground image is highly compromised by film grain. As a result

of the grain, when backing screen noise is completely removed, the edges of the foreground object

often become harsh and jagged, leading to a poor key.

Grain Size

The Grain Size selector provides a range of grain removal from Small to Large. If the foreground image

has a large amount of film grain-induced pixel noise, you may lose a good edge to the foreground

object when trying to clean all the grain noise with the Clean Background Noise Operation Mode.

These tools clean up the grain noise without affecting the quality of the key.

�None: No degraining is performed.

�Small: The average color of a small region of the area around the sampled pixel. This should be

used when the grain is very dense.

�Medium: The average color of a medium-sized region of the area around the sampled pixel. This

should be used when the grain is less dense.

�Large: The average color of a larger region of the area around the sampled pixel. This should be

used when the grain is very loose.

Grain Tolerance

Adjusting this slider increases the effect of the Clean Background Noise tool without changing the

edge of the foreground object.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

The Primatte Matte tab

Matte Tab

The Matte tab refines the alpha of the key, combined with any solid and garbage masks connected

to the node. When using the Matte tab, set the viewer to display the alpha channel of Primatte’s

final output.

Filter

This control selects the filtering algorithm used when applying blur to the matte.

�Box: This is the fastest method but at reduced quality. Box is best suited for minimal

amounts of blur.

�Bartlett: Otherwise known as a Pyramid filter, Bartlett makes a good compromise between speed

and quality.

�Multi-Box: When selecting this filter, the Num Passes slider appears and lets you control the

quality. At 1 and 2 passes, results are identical to Box and Bartlett, respectively. At 4 passes and

above, results are usually as good as Gaussian, in less time and with no edge “ringing.”

�Gaussian: The Gaussian filter uses a true Gaussian approximation and gives excellent results, but

it is a little slower than the other filters. In some cases, it can produce an extremely slight edge

“ringing” on floating-point pixels.

Blur

Matte Blur blurs the edge of the matte based on the Filter menu setting. A value of zero results in a

sharp, cutout-like hard edge. The higher the value, the more blur applied to the matte.

Blur Inward

Activating the Blur Inward checkbox generates the blur toward the center of the foreground subject.

Conventional blurring or defocus affects the matte edges in both directions (inward and outward) and

sometimes introduces a halo artifact around the edge in the composite view. Blur Inward functions

only in the inward direction of the foreground subject (toward the center of the white area). The final

result removes small and dark noise in the screen area without picking them up again in the Clean

Background Noise mode. It can sometimes result in softer, cleaner edges on the foreground objects.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Contract/Expand

This slider shrinks or grows the semitransparent areas of the matte. Values above 0.0 expand the

matte, while values below 0.0 contract it.

This control is usually used in conjunction with the Matte Blur to take the hard edge of a matte and

reduce fringing. Since this control affects only semitransparent areas, it will have no effect on a matte’s

hard edge.

Gamma

Matte Gamma raises or lowers the values of the matte in the semitransparent areas. Higher values

cause the gray areas to become more opaque, and lower values cause the gray areas to become

more transparent. Completely black or white regions of the matte remain unaffected.

Since this control affects only semitransparent areas, it will have no effect on a matte’s hard edge.

Threshold

This range slider sets the lower threshold using the handle on the left and sets the upper threshold

using the handle on the right.

Any value below the lower threshold setting becomes black or transparent in the matte.

Any value above the upper threshold setting becomes white or opaque in the matte. All values within

the range maintain their relative transparency values.

This control is often used to reject salt and pepper noise in the matte.

Restore Fringe

This restores the edge of the matte around the keyed subject. Often when keying, the edge of the

subject where you have hair is clipped out. Restore Fringe brings back that edge while keeping the

matte solid.

Invert Matte

When this checkbox is selected, the alpha channel created by the keyer is inverted, causing all

transparent areas to be opaque and all opaque areas to be transparent.

Solid Matte

Solid mattes are mask nodes or images connected to the solid matte input on the node. The solid

matte is applied directly to the alpha channel of the image. Generally, solid mattes are used to hold out

keying in areas you want to remain opaque, such as someone with blue eyes against a blue screen.

Enabling Invert inverts the solid matte before it is combined with the source alpha.

Garbage Matte

Garbage mattes are mask nodes or images connected to the garbage matte input on the node. The

garbage matte is applied directly to the alpha channel of the image. Generally, garbage mattes are

used to remove unwanted elements that cannot be keyed, such as microphones and booms. They are

also used to fill in areas that contain the color being keyed but that you wish to maintain.

Garbage mattes of different modes cannot be mixed within a single tool. A Matte Control node is

often used after a Keyer node to add a garbage matte with the opposite effect of the matte applied to

the keyer.

Enabling Invert inverts the garbage matte before it is combined with the source alpha.

Post-Multiply Image

Select this option to cause the keyer to multiply the color channels of the image against the alpha

channel it creates for the image. This option is usually enabled and is on by default.


Fusion Page Effects | Chapter 109 Matte Nodes

FUSION

Deselect this checkbox and the image can no longer be considered premultiplied for purposes

of merging it with other images. Use the Subtractive option of the Merge node instead of the

Additive option.

For more information on these Merge node settings, see Chapter 95, "Composite Nodes," in

the DaVinci Resolve Reference Manual, or Chapter 35 in the Fusion Reference Manual.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Matte nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.