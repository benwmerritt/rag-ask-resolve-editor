---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 482
---

# Inspector

The sRender Image tab

Image Tab

The controls in this tab are used to set the resolution, color depth, and pixel aspect of the image

produced by the sRender node.

Process Mode

Use this menu control to select the Fields Processing mode used by Fusion to render the resulting

image. The default Full Frames option is appropriate for progressive formats.

Width/Height

This pair of controls are used to set the Width and Height dimensions of the image to be created by

the sRender node.

Pixel Aspect

This control is used to specify the Pixel Aspect ratio of the created images. An aspect ratio of 1:1 would

generate a square pixel with the same dimensions on either side (like a computer display monitor), and

an aspect of 0.9:1 would create a slightly rectangular pixel (like an NTSC monitor).

NOTE: Right-click on the Width, Height, or Pixel Aspect controls to display a menu listing the

file formats defined in the preferences Frame Format tab. Selecting any of the listed options

will set the width, height, and pixel aspect to the values for that format, accordingly.

Auto Resolution

When this checkbox is selected, the width, height, and pixel aspect of the image created by the node

will be locked to values defined in the composition’s Frame Format preferences. If the Frame Format

preferences change, the resolution of the image produced by the node will change to match. Disabling

this option can be useful to build a composition at a different resolution than the eventual target

resolution for the final render.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Depth

The Depth button array is used to set the pixel color depth of the image created by the Creator node.

32-bit pixels require 4X the memory of 8-bit pixels but have far greater color accuracy. Float pixels

allow high dynamic range values outside the normal 0..1 range, for representing colors that are brighter

than white or darker than black.

Source Color Space

You can use the Source Color Space menu to set the Color Space of the footage to help achieve a

linear workflow. Unlike the Gamut tool, this doesn‘t perform any actual color space conversion, but

rather adds the source space data into the metadata, if that metadata doesn‘t exist. The metadata can

then be used downstream by a Gamut tool with the From Image option, or in a Saver, if explicit output

spaces are defined there. There are two options to choose from:

�Auto: Automatically reads and passes on the metadata that may be in the image.

�Space: Displays a Color Space Type menu where you can choose the correct color

space of the image.

Source Gamma Space

Using the Curve Type menu, you can set the Gamma Space of the footage and choose to remove it by

way of the Remove Curve check box when working in a linear workflow. There are three choices in the

Curve Type menu

�Auto: Automatically reads and passes on the metadata that may be in the image.

�Space: Displays a Gamma Space Type menu where you can choose the correct gamma

curve of the image.

�Log: Brings up the Log/Lin settings, similar to the Cineon tool.

For more information, see Chapter 99, "Film Nodes," in the DaVinci Resolve Reference Manual,

or Chapter 39 in the Fusion Reference Manual.

Remove Curve

Depending on the selected Gamma Space or on the Gamma Space found in Auto mode, the Gamma

Curve is removed from, or a log-lin conversion is performed on, the material, effectively converting it

to a linear output space.

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

sStar

The sStar node

The sStar node is used to create multi-point star shapes. Like almost all Shape nodes, you can only

view the sStar node’s results through a sRender node.

External Inputs

This node generates shapes and does not have any inputs.

Basic Node Setup

The sStar node is a shape generator, meaning it generates a shape and therefore has no inputs. The

output of the sStar can go into a sRender for viewing and further compositing or, more likely, connect

to another shape node like sGrid or sDuplicate.

An sStar node connecting to an sDuplicate node, and then viewed using an sRender node

Inspector

The sStar Controls tab

Controls

The Controls tab is used to define the star shape’s characteristics, including number of points, depth,

fill, border, size, and position.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Points

This slider determines the number of points or arms on the star.

Depth

The depth slider controls the inner radius or width of the arms. A depth of 0.001 makes hair-thin arms,

while a depth of 1.0 makes a faceted circle.

Solid

When enabled, the Solid checkbox fills the star shape with the color defined in the Style tab. When

disabled, an outline created by the Border Width control is displayed, and the center is made

transparent.

Border Width

This parameter expands or contracts the border around the shape. Although it can be used when the

Solid checkbox is enabled, it is primarily used to determine the outline thickness when the checkbox

is disabled.

Border Style

The Border Style parameter controls how the sides of the star join at the corners. There are three

styles provided as options. Bevel squares off the corners. Round creates rounded corners. Miter

maintains pointed corners.

Cap style

When the Solid checkbox is disabled, three cap style options are displayed. The cap styles can create

lines with flat, rounded or squared ends. Flat caps have flat, squared ends while rounded caps have

semi-circular ends. Squared caps have projecting ends that extend half the line width beyond the end

of the line.

The caps are not visible unless the length is below 1.0.

Position

The Position parameter is only displayed when the Solid checkbox is disabled. It allows you to position

the starting point of the shape. When used in conjunction with the length parameter, it positions the

gap in the outline.

Length

The Length parameter is only displayed when the Solid checkbox is disabled. A length of 1.0 is a

closed shape. Setting the length below 1.0 creates an opening or gap in the outline. Keyframing the

Length parameters allows you to create write-on style animations.

X and Y Offset

These parameters are used to position the shape left, right, up, and down in the frame. The shape

starts in the center of the frame, and the parameters are used to offset the position. The offset

coordinates are normalized based on the width of the frame. So an X offset of 0.0 is centered and a

value of 0.5 places the center of the shape directly on the right edge of the frame.

Width/Height

The Width and Height parameters determine the vertical and horizontal size of the star. If the values

are identical, then all arms of the star are of equal length.

Angle

The Angle parameter rotates the shape based on the center axis.


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Style Tab

The sStar Style tab

Style

The Style tab is used to assign color to the shape and control its transparency.

Color

The Color controls determine the color of the fill and border from the sStar node. To choose a shape

color, you can click the color disclosure arrow and use the color swatch, or drag the eye dropper into

the viewer to select a color from an image. The RGBA sliders or number fields can be used to enter

the value of each color channel or the strength of the Alpha channel.

Allow Combining

When this checkbox is enabled, the Alpha channel value is maintained even when passing through

other nodes downstream that may cause the shape to overlap with copies of itself. When disabled, the

Alpha channel value may increase when the shape overlaps itself. For instance, if a star Alpha channel

is set to .5, enabling the Allow Combining checkbox maintains that value even if the shape passes

through a duplicate or grid node that causes the shape and Alpha channel to overlap. Disabling the

checkbox causes the Alpha channel values to be compounded at each overlapping area.

Allow Combining Enabled (left), Allow Combining Disabled (right)


Fusion Page Effects | Chapter 117 Shape Nodes

FUSION

Common Controls

Settings tab

The Settings tab in the Inspector is common to all Shape nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.