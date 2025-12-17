---
title: "Managing Resolution In Fusion"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 293
---

# Managing Resolution In Fusion

There is no formal resolution for a comp in Fusion.

�In the Fusion page, the default resolution for Fusion-generated images, like the Background tool,

Fast Noise, and Text+, etc., is determined by the Timeline resolution.

�In Fusion Studio, the resolution for generators is set in Preferences > Frame Format, where you

can select a standard resolution from the drop-down menu, or set the Width and Height manually.

�The resolution of a composition in the Fusion page is initially determined by the source resolution

of the input image.

For example, if you have a Timeline set to HD resolution (1920 x 1080) and have a clip on the

timeline whose source resolution is UHD (3840 x 2160), opening this clip in the Fusion page

will set the composition’s resolution to UHD (3840 x 2160).

All Fusion-generated images in this composition will be UHD resolution.

HD Timeline

UHD

Source

Media

Resize

Scale

Crop

Letterbox

Fusion Page

UHD

HD res

Fusion timeline sizing for the Fusion page

TIP: The output of the Fusion page is placed back into the Edit page Timeline based on

DaVinci Resolve’s Image Sizing setting. By default, DaVinci Resolve uses an image sizing

setting called Scale to Fit. This means that even if the Fusion page outputs a 4K composition,

it conforms to 1920 x 1080 if that is what the project or a particular Timeline is set to.

Changing the image sizing setting in DaVinci Resolve’s Project Settings affects how Fusion

compositions are integrated into the Edit page Timeline.

Changing the Resolution of a Clip

If your comp uses a single image, you can change the pixel output resolution in several ways. Three

common tools that change the pixel resolution of a clip are the Resize, Scale, and Crop nodes. A fourth

node, Letterbox, is less commonly used but also changes the pixel resolution of a clip.

These four nodes are located in the Transform category of the Effects library. Resize is also located in

the toolbar.

�Crop: Sets the output resolution of the node using a combination of X and Y size along with X and

Y offset to cut the frame down to the size you want. Crop removes pixels from the image, so if you

later use a Transform node and try to move the image, those pixels are not available.

�Letterbox: Sets the output resolution of the node by adding horizontal or vertical black edges

where necessary to format the frame size and aspect ratio.

�Resize: Sets the output resolution of the node using absolute pixels.

�Scale: Sets the output resolution of the node using a relative percentage of the current input

image size.


Fusion Fundamentals | Chapter 76 Controlling Image Processing and Resolution

FUSION

TIP: To change resolution and reposition a frame without changing the pixel

resolution of a clip, use the Transform node.

Compositing with Different-Resolution Clips

When you composite images with different resolutions using the Merge node, the image that’s

connected to the orange background input determines the output resolution of the Merge node.

Often, it’s easiest to control the comp resolution right at the start by connecting a node with

the desired output resolution you want to the orange background input on the Merge node.

A Background node is often used in this situation because it consumes meager system resources.

A Background node determines the output resolution of the merge

The Background node sets the output size, and the foreground image is cropped if it is larger.

A Background node created at 1280 x 720 crops the larger foreground.

However, all the pixels of the larger foreground are available for repositioning.

Sizing Between DaVinci Resolve Pages

The order of sizing operations between DaVinci Resolve pages is a bit more nuanced. It’s important to

understand which sizing operations happen in the Fusion page, and which happen after, so you know

which effects alter the image that’s input to the Fusion page, and which effects alter the page’s output.


Fusion Fundamentals | Chapter 76 Controlling Image Processing and Resolution

FUSION

For example, lens correction, while not strictly sizing, is nonetheless an effect that changes how the

image begins in your Fusion composition. However, the Edit or Cut page stabilization function is an

effect that comes after the Fusion page, so it does not appear in the composition you’re creating.

The order of sizing effects in the different pages of DaVinci Resolve can be described as follows:

Edit/Cut Page

Transforms

Input

Sizing

Output

Sizing

Super

Scale

Edit/Cut Page

Lens

Correction

Fusion

Transforms

Sizing with Compound and Fusion Clips

Another way to modify the resolution before clips get handed off from the Edit page to the Fusion

page is to create a compound clip or a Fusion clip. Both compound clips and Fusion clips change the

working resolution of the individual clips to match the Timeline resolution. For instance, if two 4K clips

are stacked one on top of the other in an HD timeline, creating a compound or Fusion clip resizes

the clips to HD. The full resolution of the individual 4K clips is not available in Fusion and is therefore

handed off to the Color page at the rescaled size. To maintain the full resolution of source clips, bring

only one clip into the Fusion page from the Edit or Cut page Timeline, and then bring other clips into

the Fusion composition using the Media Pool. Of course, if your clips are full HD and your timeline is

full HD, then creating a Fusion clip or compound clip does not affect the resolution.

Timeline

HD Resolution

UHD

Source

Media

Fusion Page

Timeline Resolution

Fusion Clip

Compound Clip

Fusion timeline sizing for Fusion and Compound clips

Color Bit Depths

The term bit depth describes how many colors are available in the color palette used to make up an

image. The higher the bit depth, the greater the precision of color in the image, and therefore the

greater the color reproduction. The higher precision is most apparent in gradients with subtle changes.

Lower bit-depth gradients have noticeable banding artifacts, whereas higher bit-depth images can

reproduce more colors, so fewer, if any, banding artifacts occur. The Fusion page within DaVinci

Resolve always uses 32-bit float bits per channel precision to process images. However, in Fusion

Studio you can choose to process images with 8-bit integer, 16-bit integer, 16-bit float, and 32-bit float

bits per channel. Although always working at 16-bit float or 32-bit float will produce the best quality,

it may be more efficient to use a lower bit depth if your images are 8-bit or 16-bit integer formats to

begin with.

Understanding Integer vs. Float

Generally, 8-bit integer color processing is the lowest bit depth you’ll come across for video

formats. 8-bit images come from older or consumer-grade video equipment like mobile phones and

camcorders. If you try to perform any significant gamma or color correction on 8-bit images, you can

often see more visible banding.

16-bit integer color depth doubles the amount of precision, eliminating problems with banding.

Although you can select 16-bit integer processing for an 8-bit clip, it does not reduce banding that

already exists in the original file. Still, it can help when adding additional effects to the clip. This sounds

like the best solution until you realize that many digital cameras like Blackmagic Design URSA Mini Pro


Fusion Fundamentals | Chapter 76 Controlling Image Processing and Resolution

FUSION

and others record in formats that can capture over-range values with shadow areas below 0.0 and

super highlights above 1.0, which are truncated in 16-bit integer.

The 16-bit float color depth sacrifices a small amount of the precision from standard 16-bit integer color

depth to allow storage of color values less than 0 and greater than 1.0. 16-bit float, sometimes called

half-float, is most often found in the OpenEXR format and contains more than enough dynamic range

for most film and HDR television purposes yet requires significantly less memory and processing time

than is required for full float, 32-bit images.

Preserving over-range values allows you to change

exposure while maintaining highlights

Processing at 32-bit float can work with shadow areas below 0.0 and highlights above 1.0,

similar to 16-bit float, except with a much greater range of precision but also much greater

memory and processing requirements.

Setting Color Depth in Fusion Studio

As we said earlier, DaVinci Resolve always processes at 32-bit float bits per channel; however, you can

use less memory and still achieve more-than-acceptable results using the Performance Mode setting

located in the User > Playback Preferences panel.

Fusion Studio automatically uses the color depth that makes the most sense for each file format.

For example, if you read in a JPEG file from disk, then the color depth for the Loader is set to 8 bits per

channel. Since the JPEG format is an 8-bit format, loading the image at a greater color depth would

generally be wasteful. If a 16-bit TIFF is loaded, the color depth is set to 16 bits. Loading a DPX file

defaults to 32-bit float, whereas OpenEXR generally defaults to 16-bit float. However, you can override

the automatic format color depth using the settings found in the Import tab of the Loader node’s

Inspector. The Loader’s Inspector, as well as the Inspector for images generated in Fusion (i.e., text,

gradients, fast noise, and others), has a Depth menu for 8-bit, 16-bit integer, 16-bit float, and 32‑bit float.

The Loader’s Inspector Color Bit Depth settings


Fusion Fundamentals | Chapter 76 Controlling Image Processing and Resolution

FUSION

Configuring Default Color Depth Preferences

The default color depth setting forces the tool to process based on the settings configured in the

Node Editor’s Frame Format preferences. These are used to set a default value for color depth,

applied when a Generator tool is added to the Node Editor. There are three drop-down menus to

configure color depth in the preferences. They specify the different color depths for the interactive

session, final renders, and preview renders.

To improve performance as you work on your comp, you can set the Interactive and Preview depth to

8-bits per channel, while final renders can be set to 16-bit integer. However, if your final render output

is 16-bit float or 32-bit float, you should not use the integer options for the interactive setting. The final

results may look significantly different from interactive previews set to integer options.

The Frame Format Color Depth settings

If you aren’t sure what the color depth process is for a tool, you can position the pointer over the

node’s tile in the Node Editor, and a tooltip listing the color depth for that node will appear on the

Status bar.

Hover over a node to view its Color Bit Depth setting.

TIP: When working with images that use 10-bit or 12-bit dynamic range or greater, like

Blackmagic RAW or Cinema DNG files, set the Depth menu in the Inspector to 16-bit float or

32-bit float. This preserves highlight detail as you composite.


Fusion Fundamentals | Chapter 76 Controlling Image Processing and Resolution

FUSION