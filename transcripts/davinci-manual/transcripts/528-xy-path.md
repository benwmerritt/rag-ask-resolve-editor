---
title: "XY Path"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 528
---

# XY Path

The XY Path type uses two separate splines for the position along the X-axis and for the position

along the Y-axis.

To animate a coordinate control using an XY path, right-click the control and select Modify With >

XY Path from the contextual menu.

At first glance, XY paths work like Displacement paths. To describe the path, change frames and

position the control where it should be on that frame, and then change frames again and move the

control to its new position. Fusion automatically interpolates between the points. The difference is that

no keyframes are created on the onscreen path.

Look in the Spline Editor to find the X and Y channel splines. Changes to the control’s values are

keyframed on these splines. The advantage to the XY path is that it becomes very easy to work with

motion along an individual axis.

Inspector

XY Path modifier controls

X Y Z Values

These reflect the position of the animated control using X, Y, and Z values.

Center

The actual center of the path. This can be modified and animated as well to move the entire

path around.

Size

The size of the path. Again, this allows for later modification of the animation.

Angle

The angle of the path. Again, this allows for later modification of the animation.

Heading Offset

If another control (for example, a mask’s Angle) is connected to the path’s heading, this control allows

for adding or subtracting from the calculated angle.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Plot Path in View

Toggles whether or not the actual path is displayed in the views.

Switching Default Paths

You can change the Default Path type to XY path (if this is the preferred type of animation). Open

the Default category in the Global Preferences and locate the Point With drop-down menu. Change

this from the current value to XY Path. The next time Animate is selected from a Coordinate control’s

contextual menu, an XY path is used instead of a Displacement path.


Fusion Page Effects | Chapter 124 Modifiers

COLOR

Color

CONTENTS

125	 Introduction to Color Grading������������������������ 2953

126	 Using the Color Page����������������������������������������� 2965

127	 Viewers, Monitoring, and Video Scopes���� 2983

128	 Color Page Timeline and Lightbox��������������� 3023

129	 Automated Grading

Commands and Imported Grades���������������� 3038

130	 Camera Raw Palette������������������������������������������� 3052

131	 Primaries Palette�������������������������������������������������� 3058

132	 HDR Palette������������������������������������������������������������ 3077

133	 Primary Grading Controls����������������������������������� 3101

134	 Curves������������������������������������������������������������������������ 3107

135	 ColorSlice���������������������������������������������������������������� 3128

136	 Color Warper���������������������������������������������������������� 3135

137	 Secondary Qualifiers������������������������������������������� 3157

138	 Secondary Windows������������������������������������������� 3185

139	 Magic Mask������������������������������������������������������������� 3201

140	 Motion Tracking Windows�������������������������������� 3229


Using the Gallery������������������������������������������������� 3256

142	 Grade Management��������������������������������������������� 3273

143	 Node Editing Basics������������������������������������������� 3308

144	 Image Processing Order of Operations����� 3329

145	 Serial, Parallel, and Layer Nodes������������������ 3332

146	 Combining Keys and Using Mattes�������������� 3340

147	 Channel Splitting and

Image Compositing�������������������������������������������� 3365

148	 Keyframing in the Color Page������������������������ 3380

149	 Copying and Importing

Grades Using ColorTrace��������������������������������� 3395

150	 Using LUTs������������������������������������������������������������� 3405

Chapter 125

Introduction to

Color Grading

For over thirty years, DaVinci has pioneered the development of color

correction hardware and software designed to enhance visual images

acquired from film and video.

This release of DaVinci Resolve possesses our newest and most evolved professional color correction

tools yet. However, for all its technological sophistication, DaVinci Resolve is merely a tool that

requires the hands of a skilled artist to realize its full potential.

Subsequent chapters of this user manual cover the DaVinci Resolve grading tools in the Color page

in great detail, but before getting into the specifics of color balancing and contrast adjustment,

Power Windows, and Custom Curves, it’s important to step back and consider what these tools are for,

and why you’re learning to use this application in the first place.

This introduction is for those of you who are new to this process we call color correction,

or color grading. If you’re a veteran colorist then you might want to skip ahead, but if you’re just

starting out, the following sections are intended to describe the many goals of color correction, and

how the DaVinci Resolve toolset has been designed to address them; making it fast and efficient to

alter images in innumerable ways as we elevate raw footage to cinematic art.

Contents

The Goals of Color Correction���������������������������������������������������������������������������������������������������������������������������������������������������� 2954

Maximizing the Look of Your Media���������������������������������������������������������������������������������������������������������������������������������������� 2954

Emphasizing What’s Important�������������������������������������������������������������������������������������������������������������������������������������������������� 2957

Audience Expectations������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2958

Balancing Scenes������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 2959

Adding Style����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2960

Quality Control����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 2963

Never Stop Experimenting����������������������������������������������������������������������������������������������������������������������������������������������������������� 2964


Color | Chapter 125 Introduction to Color Grading

COLOR

The Goals of Color Correction

If reality is a fire hose of visual information, then digital cinema and broadcast would be represented

by a garden hose. Color correction, therefore, could be considered the process of choosing which

parts of the fire hose of raw image data to fit into the garden hose of our displays in order to create a

pleasing image for the viewer.

Maximizing the Look of Your Media

Clearly, the most fundamental aspect of the color correction process is that of making every clip

look its best. While the job of the cinematographer is to light and expose the image with an artistic

intent, your job is to realize this intent by making adjustments to the color and contrast of the

image, so that the final result is as close to what the director and cinematographer had in mind as

is humanly possible. In the process, you have the opportunity to overcome inconsistencies with

exposure and white balance that were, for various reasons, unavoidable. Furthermore, you can make

subtle adjustments to add warmth or contrast that was not available during the shoot, but that the

cinematographer would have liked.

Increasingly, color correction is seen as a critical stage in the post-production process. For example,

the newer generation of digital cinema cameras are capable of shooting raw colorspace image data,

or RGB image data with a log exposure, in order to preserve the maximum amount of image data for

manipulation during the color correction process. However, when you acquire image data this way,

it must be transformed into a viewable image via color correction in the same way that film negative

must first be developed and printed to positive film.

Log encoded source

Normalized and corrected

Source footage courtesy of Gianluca Bertone DP, www.bertonevisuals.com

Of course, there are also situations in which you may find it necessary to attempt to fix source media

with far more substantial problems in color and exposure. In these cases, the tools exist to make far

more involved adjustments to the image; however, the quality of your results will depend heavily on

the data quality and “latitude” of your source media.

For example, Blackmagic URSA, ARRI ALEXA, and RED DRAGON cameras record quite a bit of image

data, making extreme corrections far more possible than more heavily compressed camera formats

such as the Canon 5D. However, in either case, DaVinci Resolve provides the tools to process images

in many different ways to adjust the image for a better look.


Color | Chapter 125 Introduction to Color Grading

COLOR

Underexposed source

Balanced and gain corrected

Whether clips need changes large or small, the primary DaVinci Resolve toolset adjusts the

characteristics of hue, saturation, and contrast in a variety of ways. In the Color Wheels palette,

Color balance wheels let you adjust all three color channels at once, altering the color temperature

of the scene at specific ranges of tonal detail referred to as lift, gamma, and gain. Alternately, the

slider‑based Primaries Bars mode lets you make the same kinds of controls via independently

adjustable red, green, and blue lift, gamma, and gain controls.

Primary correction wheels, Primary correction bars


Color | Chapter 125 Introduction to Color Grading

COLOR

All of these controls let you adjust the color tone of the shadows, midtones, and highlights

independently from each other.

Cool look	Warm look

Meanwhile, the Master Lift, Gamma, and Gain wheels work together to let you alter image contrast in

different ways: deepening shadows, lightening highlights, and brightening or darkening the midtones

in between to create whatever image tonality you prefer for a given scene.

High contrast

Low contrast

Source footage courtesy of Gianluca Bertone DP, www.bertonevisuals.com

Separate saturation controls let you increase or decrease color intensity throughout the scene, while

the Lum vs. Sat and Sat vs. Sat curves give you the ability to fine-tune saturation very specifically.

High Saturation

Low Saturation

For more information on these controls, which are essential to the color correction process,

see Chapter 129, “Primaries Palette.”


Color | Chapter 125 Introduction to Color Grading

COLOR