---
title: "All Compositing Is Math"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 295
---

# All Compositing Is Math

The LUT applied to the viewer only solves the problem in the viewer. Now we come to the larger

problem. The image data is still using a log gamma curve. Fusion, and every other image-processing

application, operates with the assumption that the image data has linear gamma. The image-

processing filters you apply to images use standard math functions, like 1 + 1 = 2. Common operations

such as those that add pixels like Brightness, or divide pixels (a.k.a. “unpremultiply”), or composite

modes that include multiplication such as “screen,” and many other compositing tasks assume that 1 +

1 always equals 2. In other words, if you perform an operation that doubles the amount of brightness,

then every pixel should be twice as bright. However, if you are starting with a nonlinear gamma curve,

pixels are not being adjusted linearly, so some pixels might end up 1.2 x as bright, 1.7 x as bright, or

2.4 x as bright. Now the math is 1 + 1 = 3. The further your images are from linear gamma, the more

pronounced the math error. A Rec. 709 HD clip shows less error than a log gamma clip from a digital

cinema camera. However, an error is still an error, and the more compositing operations you perform

on the image, the more the error is compounded.

You can see a more practical example when you apply filtering effects, such as a blur, to an image

with any gamma setting. The image probably looks fine. However, if you convert the image to a linear

gamma first and then apply the blur, the images (especially those with extremely bright areas) are

processed with greater accuracy, and you should notice a different and superior result.

The answer to these problems is to manage your color before compositing.

Introducing Color Management in Fusion

Images loaded into Fusion by default are not color managed. The image is displayed directly from

the file to the viewer without any interpretation or conversion. However, Fusion includes nodes that

convert the output of each image to linear gamma at the beginning of your composite. The same

nodes can convert from linear back to your desired output gamma at the end of your composite, just

prior to the Saver or MediaOut node.

A log clip converted to linear and then converted for output

To manually set up a linear gamma workflow in Fusion:


Use a Gamut or CineonLog node after all MediaIn or Loader nodes to convert them to linear.


Apply a GAMUT View LUT to the viewers to correct the display of a linear image to sRGB

or Rec. 709.


Before a Saver or MediaOut node, insert a Gamut or CineonLog node to convert from linear to

your target output format.


Fusion Fundamentals | Chapter 77 Managing Color for Visual Effects

FUSION

Converting to Linear Gamma

Whether an image comes from the Edit page in DaVinci Resolve, or from a Loader in Fusion Studio,

the color and gamma are read directly into Fusion, with no modification. For some simple operations

on sRGB or Rec 709 clips, this may be fine, but it’s not always the ideal way to work, especially for

log-encoded media. The ideal way to work with log-encoded media is to convert images to linear

gamma, since the majority of image-processing operations in Fusion expect gamma to be linear and

will produce superior results.

TIP: 3D rendered CGI images are often generated as EXR files with linear gamma, and

converting them is not necessary. However, you should check your specific files to make sure

they are using linear gamma.

Fusion includes several kinds of nodes you can use to convert the image out of each MediaIn or

Loader node to linear gamma at the beginning of your composite, and then convert from linear back to

your desired output gamma at the end of your composite. These include:

�CineonLog node: The CineonLog node, found in the Film category of the Effects Library,

performs a conversion from any of the formats in the Log Type menu to linear, and also reverses

the process, adding log gamma back to a clip. This is most often used for images coming from

common digital cinema cameras like BlackMagic Design, Arri, or Red. The CineonLog node is

added directly after a MediaIn or Loader node. The Mode menu chooses the direction of the

conversion to or from linear.

Add a CineonLog tool to convert log gamma

curves to linear and vice versa.

�Gamut node: The Gamut node, found in the Color category of the Effects Library, lets you

perform linear conversions based on color space. This node converts to linear or from linear

and is often inserted after a MediaIn or Loader node or just before a MediaOut or Saver node.

Depending on where you insert the node, you either choose from the Source Space controls or

the Output Space controls.


Fusion Fundamentals | Chapter 77 Managing Color for Visual Effects

FUSION

Add a Gamut tool to convert gamma curves

to linear based on color space.

When converting media to linear gamma, set the Source Space menu to the color space of your

source material. For instance, if your media is full 1080 HD ProRes, then choose ITU-R BT.709

(scene) for gamma of 2.4. Then, enable the Remove Gamma checkbox if it isn’t already enabled, to

use linear gamma.

Source Space is used to convert to linear gamma.

When converting from linear gamma for output, you insert the Gamut node before your output

node, which is a Saver in Fusion Studio or a MediaOut node in DaVinci Resolve’s Fusion page.

Make sure the Source Space menu is set to No Change, and set the Output Space to your output

color space. For instance, if your desired output is full 1080 HD, then choose either sRGB or

ITU-R BT.709 (scene) for gamma of 2.4. Then, enable the Add Gamma checkbox if it isn’t already

enabled, to format the output of the Gamut node for your final output.


Fusion Fundamentals | Chapter 77 Managing Color for Visual Effects

FUSION

Output Space is used to convert from linear gamma.

�MediaIn and Loader nodes: MediaIn and Loader nodes have Source Gamma Space controls in

the Inspector that let you identify and remove the gamma curve without the need to add another

node. If your files include gamma curve metadata like RAW files, the Auto setting for the Curve

Type drop-down menu reads the metadata and uses it when removing the gamma curve. When

using intermediate files or files that do not include gamma curve metadata, you can choose either

a log gamma curve by choosing Log from the Curve Type menu or a specific color space using

the Space option from the menu. Clicking the Remove Curve checkbox then removes the gamma

curve, converting the image to linear gamma.

MediaIn and Loader nodes include a

Remove Curve checkbox in the Inspector.

�FileLUT node: The FileLUT node, found in the LUT category of the Effects Library, lets you do a

conversion using any LUT you want, giving you the option to manually load LUTs in the ALUT3,

ITX, 3DL, or CUBE format to perform a gamma and gamut conversion. Although LUTs are very

commonly placed at the end of a node tree for final rendering, you’ll get more accurate gamma

and color space conversions using the Gamut and CineonLog nodes to transform your MediaIn

and Loader nodes into linear.


Fusion Fundamentals | Chapter 77 Managing Color for Visual Effects

FUSION

Applying LUTs to a Viewer

Images converted to a linear gamma don’t look correct. They usually look very dark, with extremely

bright highlights and oversaturated colors. Happily, even though the image may appear to be

incorrect, the fact that Fusion can work entirely with floating-point color data means that you’re not

actually clipping or losing any image data. It just looks completely wrong when viewing the linear state

of your image data directly.

A clip displayed with a nonlinear, log gamma curve (left) and the clip transformed to linear gamma (right)

It would be impossible to work if you couldn’t view the image as it’s supposed to appear within

the final gamut and gamma you’ll be outputting. For this reason, each viewer has a LUT menu

that lets you enable a “preview” color space and/or gamma conversion, while the node tree is

processing correctly in linear gamma.

Apply a Gamut View LUT to preview the image

in your intended output color space.


Fusion Fundamentals | Chapter 77 Managing Color for Visual Effects

FUSION

To preview the images in the viewer using sRGB or Rec. 709 color space:


Enable the LUT button above the viewer.


From the Viewer LUT drop-down menu, choose either a Gamut View LUT, or a LUT from the VFX

IO category that transforms linear to Rec. 709 or sRGB.


If you choose the Gamut View LUT, then choose Edit from the bottom of the LUT menu to

configure the LUT.


In the LUT Editor, set the Output Space to the target color space you want.


Enable the Add Gamma checkbox to apply the gamma curve based on the selected color space.

Gamut View LUT Output Space set to Rec. 709 for

HD with the Add Gamma checkbox enabled

TIP: If your monitor is calibrated differently, you need to select a LUT

that matches your calibration.

Whether you use the Gamut View LUT or a LUT for your specific monitor calibration, you can save the

viewer setup as the default.

To Save the Gamut LUT setup as the default viewer setup:

•	 Right-click in the viewer, and then choose Settings > Save Defaults.

For every comp, the viewer will now be preconfigured based on the saved defaults.

For more information on Viewer LUTs, see Chapter 69, “Using Viewers.” in the DaVinci

Resolve Reference Manual or Chapter 7 in the Fusion Reference Manual.


Fusion Fundamentals | Chapter 77 Managing Color for Visual Effects

FUSION