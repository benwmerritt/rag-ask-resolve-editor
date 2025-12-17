---
title: "Frame Interpolation"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 28
---

# Frame Interpolation

These settings determine the default state for all retiming and speed change effects, including when

clips are in mixed frame rate timelines.

�Retime Process: This drop-down menu lets you choose a default method of processing clips

that don’t match the project frame rate in mixed frame rate timelines and clips with speed effects

(fast forward or slow motion) applied to them, throughout the project. Since each clip in every

timeline defaults to “Project Settings,” changing this setting will change the way most mixed frame

rate and speed effected clips will be processed, except for those with custom settings selected.

There are three options:

Nearest: The most processor efficient and least sophisticated method of processing; frames are

either dropped for fast motion, or duplicated for slow motion.

Frame Blend: Also processor efficient, but can produce smoother results; adjacent duplicated

frames are dissolved together to smooth out slow or fast motion effects. This option can provide

better results when Optical Flow displays unwanted artifacts.

Optical Flow: The most processor intensive, but highest quality method of speed effect

processing. Using motion estimation, new frames are generated from the original source frames

to create slow or fast motion effects. The result can be exceptionally smooth when motion in a clip

is linear. However, two moving elements crossing in different directions or unpredictable camera

movement can cause unwanted artifacts.

�Motion estimation mode: When using mixed frame rate clips in a timeline that has Optical Flow

retiming enabled, when using Optical Flow to process speed change effects, or when using Image

Stabilization or Temporal Noise Reduction controls in the Color page, the Motion Estimation drop-

down of the Master Settings (in the Project Settings window) lets you choose options that control

the trade-off between speed and quality.

There are additional “Enhanced” Optical Flow settings available in the “Motion estimation mode”

drop-down in the Master Settings panel of the Project Settings. The “Standard Faster” and

“Standard Better” settings are the same options that have been available in previous versions

of DaVinci Resolve. They’re more processor-efficient and yield good quality that are suitable for

most situations. However, “Enhanced Faster” and “Enhanced Better” should yield superior results

in nearly every case where the standard options exhibit artifacts, at the expense of being more

computationally intensive, and thus slower on most systems.

“Speed Warp Faster” and “Speed Warp Better” are available for even higher-quality slow motion

effects using the DaVinci Neural Engine. Your results with this setting will vary according to the

content of the clip, but in ideal circumstances this will yield higher visual quality with fewer artifacts

than even the Enhanced Better setting.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

New improved Motion estimation mode settings in

the Master Settings panel of the Project Settings

�Motion range: When using mixed frame rate clips in a timeline that has Optical Flow retiming

selected, or when using Optical Flow to process speed change effects, this drop-down menu lets

you choose the default setting to use, small, medium or large motion, for all speed and motion

related calculations so you can try and improve the result by matching the type of motion in the

source media. This setting can also be changed on a clip by clip basis in the Edit page Inspector.

Image Scaling

The Image Scaling panel contains settings that determine how and when clips are resized for

various reasons.

Image Scaling

These settings affect the methods used to resize clips in various situations.

�Resize Filter: The first group of settings lets you choose the filter method used to interpolate

image pixels when resizing clips:

Smoother: May provide higher quality for projects using clips that must be scaled down to fit an

SD resolution frame size.

Bicubic: While the Sharper and Smoother options are slightly higher quality, Bicubic is still an

exceptionally good resizing filter and is less processor intensive than either of those options.

Bilinear: A lower quality setting that is less processor intensive. Useful for previewing your work

on a low-performance computer before rendering, when you can switch to one of the higher

quality options.

Sharper: Usually provides the best quality in projects using clips that must be scaled up to fill a

larger frame size or scaled down to HD resolutions.

Custom: This setting lets you take control of the exact algorithm used in all resizing operations.

The custom Resize Filter options available are: Bessel, Box, Catmul-Rom, Cubic, Gaussian,

Lanczos, Mitchell, Nearest Neighbor, Quadratic, and Sinc. In practice, the difference between

these methods can be quite subjective. However, if you need to match a specific resizing method

used from another application, you can do it here. For everyday use, the normal resizing filters in

DaVinci Resolve should be sufficient.

�Override input scaling: Checking this box lets you choose an Input Sizing preset to

apply to the project.

�Override output scaling: Checking this box lets you choose an Output Sizing preset to

apply to the project.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

�Anti-alias edges: A second group of settings lets you choose how to handle edge anti-aliasing for

source blanking.

Auto: Adds anti-aliasing when any of the Sizing controls are used to transform the image.

Otherwise, anti-aliasing is disabled.

On: Forces anti-aliasing on at all times.

Off: Disables anti-aliasing. It might be necessary to turn anti-aliasing off if you notice black blurring

at the edges of blanking being applied to an image.

�Deinterlace quality: (only available in Studio version) A fourth group of settings lets you choose

the quality/processing time tradeoff when deinterlacing Media Pool clips using the Enable

Deinterlacing checkbox in the Clip Attributes window.

There are three settings:

Normal: A high-quality deinterlacing method that is suitable for most clips. For many clips, Normal

is indistinguishable from High. Normal is always used automatically during playback in Resolve.

High: A more processor-intensive method that can sometimes yield better results, depending on

the footage, at the expense of slower rendering times.

DaVinci Neural Engine: This option uses the advanced machine learning algorithms of the DaVinci

Neural Engine to analyze motion between the fields of interlaced material and reconstructs them

into a single frame. This option is very computationally intensive but, ideally, will deliver an even

more aesthetically pleasing result than the “high” setting.

Input Scaling

Contains one setting, Mismatched resolution files, that lets you choose how clips that don’t match the

current project resolution are handled. There are four options:

�Center crop with no resizing: Clips of differing resolution are not scaled at all. Clips that are

smaller than the current frame size are surrounded by blanking, and clips that are larger than the

current frame size are cropped.

�Scale full frame with crop: Clips of differing resolution are scaled so that the clip’s shortest

dimension is fit to match the frame. Excess pixels are cropped.

�Scale entire image to fit: The default setting. Clips of differing resolution are scaled so that the

clip’s longest dimension is fit to match the frame. The shorter dimension has blanking inserted

(letterboxing or pillarboxing).

�Stretch frame to all corners: Useful for projects using anamorphic media. Clips of differing

resolutions are squished or stretched to match the frame size in all dimensions. This way,

anamorphic media can be stretched to match full raster, or full raster media can be squished

to fit into an anamorphic frame. An added benefit of this setting is that it makes it easy to mix

anamorphic and non-anamorphic clips in the same project.

Output Scaling

These settings let you optionally choose a different resolution to be output via your video output

interface, for monitoring, outputting to tape, or rendering. In particular, if you set the resolution in

the Render Settings list of the Deliver page to something other than the Timeline Resolution, these

settings are used to make the change (for example, if you’re rendering a downconversion of the

current timeline). This can be used in situations where you’re working on a high resolution 4K project,

but you want to monitor using an HD display and output HD resolution media for approval.

�Match timeline settings: Turned on by default, so that these settings mirror the Timeline

Resolution, Image Scaling, and Input Image Scaling settings described above. Turning this

checkbox off lets you choose different settings for monitoring, outputting to tape, or rendering,

using the other settings in this group.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

�Output resolution: Lets you choose an alternate resolution.

�For: Lets you specify a different custom alternate resolution.

�Pixel aspect ratio: Lets you specify an alternate pixel aspect ratio to match the alternate

timeline format.

�Mismatched resolution files: Lets you choose an alternate way of handling mismatched resolution

files given the alternate resolution you’ve chosen. These options work identically to those of the

“Input Image Scaling” group.

�Super Scale: Sets a very processor-intensive and high quality upscaling algorithm that actually

creates new pixels for the resized image. The possible values are: None, 2-3-4x, 2-3-4x Enhanced,

and Auto. For more information on Super Scale, see Chapter 11, “Image Sizing and Resolution

Independence.”

For more information on Super Scale, see Chapter 11, “Image Sizing and Resolution

Independence.”

Color Management

The various options found in the Color Management panel let you configure DaVinci Color

Management (RCM) or ACES if you have either enabled, and they also allow you to pre- or post-

process the DaVinci Resolve image processing pipeline using LUTs and Broadcast Safe settings, in

order to accommodate a wide range of different color workflows.

Color Space and Transforms

If you choose DaVinci YRGB Color Managed or ACES in the Color Science menu at the top, then the

other drop-down menus in this section become enabled.

For more information about DaVinci Resolve Color Management and ACES, see Chapter 9,

“Data Levels, Color Management, and ACES.” If you’re new to color or color management,

you’re strongly recommended to read this chapter.

If you choose to use Resolve Color Management (RCM), ACEScc, or ACEScct, the settings in this

panel give you extensive control over how color is transformed, starting with choosing the default

color settings for the source media in your project (via the Input Color Space), through choosing how

you want your grading controls in DaVinci Resolve to behave (via the Timeline Color Space), and then

specifying how the final color will look on your monitor and output device (via the Output Color Space).

�Color science: There are four options that let you choose whether to work with manual or

automated color management.

DaVinci YRGB color science: DaVinci Resolve’s original color science, in which you manage

all and any color transforms from one color space to another manually, using either LUTs or

manual adjustments.

DaVinci YRGB Color Managed: Enables the Resolve color-managed workflow (RCM) for grading.

DaVinci ACEScc or ACEScct: Both of these are standardized color management schemes that

are available for facilities using ACES workflows. Of the available settings, ACEScct is the most

intuitive way of working for most colorists, as it handles the lifting of shadows in a creatively

useful way.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

For more information about Color Management and ACES, see Chapter 9, “Data Levels, Color

Management, and ACES.”

�ACES version: This drop-down only appears if you choose one of the DaVinci ACES options from

the Color science drop-down menu. Lets you switch between different versions of the ACES

specification. This lets you choose the appropriate older version of ACES whenever you open an

older project.

�Use Separate Color Space and Gamma: If this checkbox is turned off (the default), the

Color Management panel of the Project Settings exposes one drop-down each for the Input,

Timeline, and Output Color Space settings, and each setting simultaneously transforms the

gamut and gamma, depending on which option you choose. If you turn this checkbox on, then the

Color Management panel changes so that the Input, Timeline, and Output Color Space settings

each display two pop-ups. The first drop-down lets you explicitly set the gamut, while the second

drop‑down lets you explicitly set the gamma.

To provide more detailed information, the simple and advanced global controls available for

Resolve Color Management (RCM) are covered in a dedicated chapter.

For more information, see Chapter 9, “Data Levels, Color Management, and ACES.”

Dolby Vision™

DaVinci Resolve includes a GPU-accelerated software version of the Dolby Vision CMU (Content

Mapping Unit) for doing Dolby Vision grading and finishing workflows right in either the free version

of DaVinci Resolve or in DaVinci Resolve Studio. This is enabled and set up in the Color Management

panel of the Project Settings with the Enable Dolby Vision checkbox.

s

Dolby Vision settings in the Color Management panel of the Project Settings

There are five controls available:

�Enable Dolby Vision: Turns Dolby Vision on and off. When on, this checkbox enables the

Dolby Vision palette in the Color page.

�Dolby Vision version drop-down: Lets you choose which version of the Dolby Vision algorithms to

use. Options at the time of this writing include 2.9 and 4.0.

�Analysis tuning: Choose from a variety of options for how Dolby Vision will analyze and control

highlight retention.

�Master Display drop-down: Lets you choose the nit level and gamut of the master HDR display

you’re grading on.

�Use External CMU: A checkbox lets you choose whether to use the built-in software CMU or a

hardware CMU that you have connected to your DaVinci Resolve workstation.


Setup and Workflows | Chapter 6 Project Settings

MEDIA

NOTE: Dolby Vision controls are available to all DaVinci Resolve users for monitoring and

automatically generating Dolby Vision metadata for creating other HDR and SDR deliverables

from the HDR grade you’ve made. However, if you want to be able to make manual trims on

top of this automatic analysis, you must email dolbyvisionmastering@dolby.com for more

information on obtaining a license.