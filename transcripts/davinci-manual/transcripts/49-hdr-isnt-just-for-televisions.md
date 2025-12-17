---
title: "HDR Isn’t Just for Televisions"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 49
---

# HDR Isn’t Just for Televisions

Lest you think that living room televisions and projectors are the only way to watch HDR content,

certain flagship iOS and Android phones and tablets have implemented HDR viewing capabilities that

are capable of meeting or even exceeding the UltraHD requirements for HDR content on an OLED

display. This makes HDR, surprisingly, a widely available mobile experience.

The Different Ways of Mastering HDR

While different HDR technologies use different methods to map the video levels of your program to

an HDR display’s capabilities, they all output a “near-logarithmically” encoded signal that requires a

compatible television that’s capable of correctly stretching this signal into its “normalized” form for

viewing. This means if you look at an HDR signal that’s output from the video interface of your grading

workstation on an SDR display, it will look flat, desaturated, and unappealing until it’s plugged into your

HDR display of choice.

A graded HDR image being output looks similar to a log-encoded image

At the time of this writing, there are five principal approaches to mastering HDR that DaVinci Resolve is

capable of supporting, including:

�Dolby Vision®

�HDR10

�HDR10+

�HDR Vivid

�Hybrid Log-Gamma (HLG)


Setup and Workflows | Chapter 10 HDR Setup and Grading

MEDIA

Each of these HDR standards define how an HDR signal is encoded for export and later mapped to the

visible output of an HDR or SDR display. Grading to each of these standards requires some degree of

color management, and DaVinci Resolve gives you three main ways to handle this:

�The easiest way is to enable Resolve Color Management (RCM) or ACES in the Color Management

panel of the Project Settings, and use the Color Space conversion options that are available.

There are options there for each supported type of HDR.

�The transforms that are available in RCM are also available as Resolve FX operations, if you want to

organize your grading pipeline more manually using the Color Transform Resolve FX adjustment.

�LUTs are also available to accomplish each of these color space conversions if you want to develop

your own specific image processing pipeline based on custom-made LUT or DCTL transforms.

Overall, Resolve Color Management and ACES are reliable and recommended approaches to handling

HDR grading in DaVinci Resolve in most instances.

For more information about Resolve Color Management, see Chapter 9, “Data Levels, Color

Management, and ACES.”

What Do I Do With HDR?

While these standards make HDR mastering and distribution possible, they have nothing to say about

how these HDR-strength levels should be used creatively. That’s up to you, because the question of

how to utilize the expansive headroom for brightness and saturation that HDR enables is fully within

the domain of the colorist, as a series of creative decisions that must be made regarding how to assign

the range of highlights that are available in your source media to the above-100 nit HDR levels you’re

mastering to as you grade, given the peak luminance level that you’re assigned to master with. Which

HDR peak luminance level you use (1000 nit, 3000 nit, 4000 nit) probably depends on which display

you have access to and who’s distributing the resulting program.

Analyzing HDR Signals Using Video Scopes

When you’re using waveform scopes of any kind, including parade and overlay scopes, the signal will

fit within the 10-bit scale used to analyze the signal much differently owing to the way HDR is encoded.

The following chart of values will make it easier to understand how each level in “nits” (i.e., cd/m2)

corresponds to a code value within the 10-bit image scale:

10-Bit Code

Nearest

Value in cd/m2

HDR Display Peak Luminance Capability

1019†

10,000

No commercially available display


Outdoor LED Displays


Professional HDR Displays from Sony, Dolby, Flanders Scientific, EIZO, etc.


Professional HDR Displays from Sony, Dolby, Flanders Scientific, EIZO, etc.


Professional HDR Displays from Sony, Dolby, Flanders Scientific, EIZO, etc.


Virtual Production Wall Panels


Professional HDR Displays from Sony, Dolby, Flanders Scientific, EIZO, etc.


OLED mobile phone brightness


Minimum standard for an “UltraHD” OLED display


Setup and Workflows | Chapter 10 HDR Setup and Grading

MEDIA

10-Bit Code

Nearest

Value in cd/m2

HDR Display Peak Luminance Capability


Professional SDR displays in “HDR preview mode”


BT.2408 recommendation for diffuse white of SDR content being intercut

with 1000 nit max HDR content


Dolby Cinema projector


Standard peak luminance for SDR displays


Standard peak luminance for SDR DCI projection, Dolby Cinema 3D peak

luminance

4†


Absolute black

† 0–3 and 1020–1023 are reserved values

While this table of values is useful for understanding where HDR nit levels fall on legacy external

scopes, if you’re monitoring with the built-in video scopes in DaVinci Resolve, you can turn on

“HDR (ST.2084/HLG)” in the Waveform Scale Style settings in the Scopes option menu, which

replaces the 10-bit scale of the video scopes with a scale based on nit values (or cd/m2) instead.

The video scopes with HDR (ST.2084/HLG) on in the Waveform Scale Style settings in the Scopes option menu

TIP: If you’re unsatisfied with the amount of detail you’re seeing in the 0–519 range

(0–100 nits) of the video scope graphs, then you can use the 3D Scopes Lookup Table setting

in the Color Management panel of the Project Settings to assign the appropriate “HDR X nits

to Gamma 2.4 LUT,” with X being the peak nit level of the HDR display you’re using. This

converts the way the scopes are drawn so that the 0–100 nit range of the signal takes up the

entire range of the scopes, from 0 through 1023. This will push the HDR-strength highlights

up past the top of the visible area of the scopes, making them invisible, but it will make it

easier to see detail in the midtones of the image.


Setup and Workflows | Chapter 10 HDR Setup and Grading

MEDIA

HDR Viewers

You can display the native viewers in DaVinci Resolve in HDR on Mac and Windows systems.

The setting affects all DaVinci Resolve viewers, including the main page viewers, Cinema Mode,

Fairlight Floating Viewer, Scene Cut Dialog, and the Video Clean Feed.

You will need an HDR-capable display and to turn on HDR in your OS:

�Activate the Windows HDR display settings (System > Display > HDR).

�Activate the Mac HDR display settings (System Settings > Displays > High Dynamic Range).

�In DaVinci Resolve Preferences > System > General, you will need to check the “Use 10-bit

precision in viewers if available” box.

NOTE: The general controls/UI and non-viewer dialogs (e.g., secondary screen, project

manager, floating Media Pool) are not affected.

Dolby Vision®

Long a pioneer and champion of HDR for enhancing the consumer video experience,

Dolby Laboratories has developed a method for mastering and delivering HDR called Dolby Vision.

As with most HDR standards discussed in this chapter, Dolby Vision uses the PQ (perceptual quantizer)

electrical-optical transfer function (EOTF, which defines how an electronic video signal is presented on

a display), which is defined by SMPTE ST.2084, along with a hierarchy of metadata that’s embedded

alongside the video stream. All metadata used by Dolby Vision is organized into levels, of which the

following are important to the colorist:

�Level 0 metadata, which is global metadata that defines the Mastering Display (what the colorist is

using), including aspect ratio, frame rate, color encoding and information on all the target displays

that are used for the Level 2 and Level 8 trim metadata below.

�Level 1 metadata, which is the Dolby Vision v2.9 analysis metadata that’s generated automatically

when you use the Dolby Vision controls to analyze the clips in the timeline. The controls for

automatically generating Level 1 metadata are available to all DaVinci Resolve Studio users.

�Level 2 metadata, which is the Dolby Vision v2.9 trimming metadata that’s set by the colorist via

the version 2.9 trim controls available in the Dolby Vision palette of the Color page. This trimming

allows adjustment of how the Dolby Vision image is to be mapped to a target display (such as

a 100 nit BT.709 display) that’s different from the mastering display (such as a 1000 nit BT.2020

display). The purpose of this metadata is to maintain a program’s artistic intent by providing

guidance from the colorist over how the program’s signal should be fit into the differing luminance

ranges of a variety of displays with different peak luminance capabilities. Manually adjustable

Level 2 metadata is only available to DaVinci Resolve Studio users via a license obtained from Dolby.

�Level 3 metadata, which is the offset for Dolby Vision v4.0 added to Level 1 metadata generated

by the analyze buttons in the Dolby Vision controls. It also stores the mid tone offset data.

�Level 5 metadata, which provides information about the aspect ratio of the deliverable format, and

the aspect ratio of the actual image within that format. This metadata is also applicable at the per

clip level.


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

�Level 6 metadata, which stores the MaxCLL and MaxFALL levels required by the HDR10 mastering

standard of HDR.

�Level 8 metadata, which is the updated Dolby Vision v4.0 trimming metadata that’s set by the

colorist via the v4.0 trim controls available in the Dolby Vision palette of the Color page. This

evolved set of trimming commands allows more detailed adjustment of how the Dolby Vision

image is to be mapped to a target display (such as a 100 nit BT.709 display) that’s different from

the mastering display (such as a 1000 nit BT.2020 display). Just like Level 2 metadata, the purpose

of Level 8 metadata is to maintain a program’s artistic intent by providing guidance from the

colorist over how the program’s signal should be fit into the differing luminance ranges of a variety

of displays with different peak luminance capabilities. Manually adjustable Level 8 metadata is

only available to DaVinci Resolve Studio users via a license obtained from Dolby. Whether you

use Level 2 trim controls or Level 8 trim controls depends on the Dolby Vision version setting you

choose in the Color Management panel of the Project Settings.

NOTE: It’s currently recommended for all users to choose Dolby Vision v4.0 for analysis

and trimming, as it provides superior results. If you’re required to deliver Dolby Vision v2.9

metadata when mastering for backwards compatibility, DaVinci Resolve can now export v2.9

metadata from projects using v4.0 workflows.

The metadata levels described above are current of this writing. However Dolby Vision

is a rapidly evolving technology, and as Dolby adds new features and metadata levels

you should reference Dolby’s website to keep track of the latest developments: https://

professionalsupport.dolby.com/s/article/Dolby-Vision-Metadata-Levels?language=en_US

For the foreseeable future, the current consumer display landscape encompasses a wide variety of

differently performing televisions and projectors that are guaranteed to improve year over year. This

means that mastering for today’s displays may render content less vibrant than content that emerges

five years from now. This can be especially vexing for narrative content that will have a long lifespan on

streaming services as new generations of viewers discover them. While one way of solving this would

be to re-grade your program many times at a variety of nit levels to create deliverables suitable to a

range of display capabilities, that’s an enormous amount of work.

Dolby Vision offers a shortcut by using sophisticated algorithms to derive automatically analyzed

metadata that intelligently guides how an image graded at one nit level (say 4000 nits) can be

adjusted to be perceptually similar to viewers watching a 1000 nit display. Highlights and saturation

that are too bright for a particular display will be adjusted to provide as close to the same experience

without clipping or flattening image detail.

Furthermore, this automatic analysis can be manually trimmed by a colorist to account for the artistic

intentions of the authors of a program, in cases where the automatic analysis doesn’t do exactly what’s

wanted. This combination of auto-analysis and manual trimming is key to how Dolby Vision streamlines

the process of mastering programs to accommodate backward compatibility with SDR displays, as

well as the varying peak luminance capabilities of different makes and models of HDR consumer

displays, both now and in the future. You’re only required to make a 100 nit trim pass to guide the HDR

program’s conversion all the way down to SDR, and the Dolby Vision system can use that information

to guide how intermediate presentations (such as at 700 or 1200 nits) should be adjusted. You can

even do multiple trim passes at specific nit levels, such as a 100 nit pass and a 1000 nit pass, to give

the Dolby Vision system more information to accurately guide intermediate presentations on different

displays. Additionally, you don’t have to trim every clip. If the analysis is good, you can skip those clips

and only trim clips that need it. The overall system has been created to make it as efficient as possible

for colorists to ensure that the widest variety of viewers see the image as it’s meant to be seen.

This, in a nutshell, is the advantage of the Dolby Vision system. You can grade a program on a more

future-proofed 4000 nit display, and use auto-analysis plus one or two manual trim passes to make


Setup and Workflows | HDR Viewers HDR Setup and Grading

MEDIA

the program backward compatible with SDR televisions, and capable of intelligently scaling the HDR

highlights to provide the best representation of the mastered image for whatever peak luminance and

color volume a particular television is capable of. All of this is guided by decisions made by the colorist

during the grade.

At the time of this writing, all seven major Hollywood studios are mastering in Dolby Vision for cinema.

Studios that have pledged support to master content in Dolby Vision for home distribution include

Universal, Warner Brothers, Sony Pictures, and MGM. Content providers that have agreed to distribute

streaming Dolby Vision content include Netflix, Vudu, and Amazon. If you want to watch Dolby Vision

content on television at home, consumer television manufacturers LG, TCL, Vizio, HiSense, Sony,

Toshiba, and Bang & Olfusen have all shipped models with Dolby Vision support.