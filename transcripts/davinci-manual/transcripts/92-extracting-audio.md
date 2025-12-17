---
title: "Extracting Audio"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 92
---

# Extracting Audio

If the film you’re scanning also contains an optical sound track, you can extract the audio in a separate

step. There is a standard image frame to audio frame offset of 26 frames for 16mm and 21 frames for

35mm that DaVinci automatically aligns when extracting the audio. Select all of the clips that have

an optical sound track, then right-click one of the selected clips and choose ‘extract audio’. Resolve

analyzes the overlapping optical track area of each frame and automatically generates a matching

audio track, synchronized with the scanned image sequence.

Each clip’s audio will be automatically extracted, embedded in the clip and saved to the same

directory the scanned frames have been written to. A small audio icon will appear on the corner of

your clip’s thumbnail so you know there is a corresponding audio file.


Ingest and Organize Media | Chapter 25 Capturing From the Cintel Film Scanner

MEDIA

To make extraction easier, you can filter the clips in the media storage by name, resolution, date

modified or by film clips only. Filtering your clips makes it easier for you to find and select exactly what

you need. You can also make a large selection and extract audio from multiple clips at once by right

clicking on your selection and choosing ‘extract audio…’ from the menu. During audio extraction, an

information box indicates the progress. You can click the ‘stop’ button any time to stop the extraction.

You can filter the contents in the media storage to make it easier to manage them.

If the ‘timestamp prefix’ checkbox was deselected in the ‘capture info’ section when your clips

were scanned, and you want to have extracted audio automatically embedded in your clips, always

remember to extract audio from the clips inside the media pool.

Audio Extraction Settings

Normally, once you have selected the film type, the automatic features in DaVinci Resolve will extract

your optical audio perfectly. However, the condition of the optical track can vary with the condition of

the film being loaded and in some instances this can confuse the automation. If this happens, you can

bypass the automatic features and make adjustments manually.

For manual adjustments, simply open the ‘Audio Extraction’ settings window by clicking

on ‘Show Cintel Audio Settings’ in the inspector options near the top right of the viewer.


Ingest and Organize Media | Chapter 25 Capturing From the Cintel Film Scanner

MEDIA

Audio extraction settings let you make the following manual adjustments:

The Audio Extraction settings let you

make manual adjustments, if needed.

Show audio scan area

This checkbox turns the audio scan area guides on or off. The guides are displayed as a

box on the side of the frame covering the optical audio scan area and shows what optical

information will be used during extraction. The position of the guides will conform to the

film type you have selected. However, you can change the position manually if you need

to. The audio scan area guides are also great indicators to show you what is happening

during the extraction process so you can identify any potential troubles and make manual

adjustments.

Inside the box is a thin red line. This line is the mid point detector which detects the separation

between stereo audio channels. When mono sound is detected during audio extraction, the

mid point detector disappears and the guides will adjust automatically to suit the width of the

mono optical track.

TIP: If you need a closer inspection of the audio scan area guides, you can zoom into the

viewer and move the viewer position up or down, and left or right. Simply choose the amount

of zoom from the sizing options at the top left corner of the viewer, then click and drag the

viewer with your mouse or track pad.


Ingest and Organize Media | Chapter 25 Capturing From the Cintel Film Scanner

MEDIA

When ‘show audio scan area’ setting is turned on, the audio area guides will be visible so you

can see exactly what information is being used and monitor the extraction process.

Override audio scan area

This setting provides sliders for adjusting the horizontal and vertical positioning, width, and height of

the audio scan area guides.

These settings include:

�Left and Width: If your film type is such that audio appears on the right side of the frame, you

can simply adjust the ‘left’ slider to move the guide box to the right. Normally, this will happen

automatically if you have the corresponding film type selected, but the setting gives you more

flexibility for adjustments if you need it. Similarly, the ‘width’ setting is used to adjust the width of

the scan area.

These are helpful tools for making subtle adjustments to the side edges of the guide box if there

are unwanted elements inside the film’s optical audio area. This can happen due to perforation

wear and tear, or varying print qualities, and can sometimes interfere with the quality of the audio

extraction. You can help avoid this by making a subtle movement to the side edges to keep the

stray elements outside of the guide box.

�Top: This setting adjusts the vertical position of the guide box.

�Height: Sometimes film frames on older rolls of film may be slightly smaller than normal due

to shrinkage over time. When making manual adjustments to the guide box, you can make

adjustments for film shrinkage using the ‘height’ slider.


Ingest and Organize Media | Chapter 25 Capturing From the Cintel Film Scanner

MEDIA

�Auto adjust audio scan height: This setting is on by default and automatically adjusts the guide

box height to align with the audio waveform at the top of each frame. The automatic feature works

well for normal audio conditions, however, if during extraction you notice the box moving randomly

and the quality of the extraction is affected, it may be due to similar features in the audio track

overlapping between frames. If this occurs, deselect the checkbox and try the extraction again.

If deselecting the ‘Auto adjust audio scan height’ checkbox, make sure the ‘height’ setting places

the guide box at the optimal position for the frame. Making manual adjustments can help if you

need them, but don’t forget to turn the automatic features back on afterwards!

TIP: If deselecting the ‘Auto adjust audio scan height’ checkbox, make sure the ‘height’

setting places the guide box at the optimal position for the frame. Making manual

adjustments can help if you need them, but don’t forget to turn the automatic features

back on afterwards!

�Audio waveform color is white: Depending on the scanned film type, the audio waveform may be

black or white. If the waveform is white, make sure the corresponding checkbox is enabled. This

will ensure the white information in the waveform is used during audio extraction. If the waveform

is black and the surrounding audio area is white, disable the checkbox so DaVinci knows to use

the black information in the waveform. Other automatic features, such as mid point and mono

detection, also rely on this setting being set correctly.

�Override firmware stability: In rare instances, the condition of the film may have created large

movements in the frame due to the internal firmware stabilization. This can cause the audio

extraction guide box to misalign with the optical track. If this occurs, enabling ‘override firmware

stability’ lets the audio extraction guide box track the film perforations independently and adjust

its positioning for potentially better results.

�Variable density audio: If your film contains variable density audio, make sure you select the

‘Variable density audio’ checkbox so DaVinci Resolve knows the type of audio to extract. The

default state is set to ‘off’ for variable area audio soundtracks.

If you haven’t used variable density audio before, you can visually identify it as a tight sequence

of shaded lines, similar to a bar code with the lines squeezed closer together. By comparison,

‘variable area’ soundtracks appear as an audio waveform.

Color Space and Sizing

A pair of 1D LUTs, ‘Cintel Negative to Linear,’ and ‘Cintel Print to Linear,’ have been provided to help

you convert scanned media to a color space in which you can do further work. You can apply these

LUTs via a node in the ‘color’ page to convert the original scans to a Linear color space. However, if

you want to convert the image to Rec. 709 or to Cineon for further adjustment, you’ll want to apply a

second LUT in a second node. The default color space for print is a 2.2 gamma standard log curve,

and all others are 2.046 film density log gamma.

In general for negative film, it’s best to “color invert” after the second LUT is applied. Furthermore,

normally some grading is required on the Linear data to remove black offsets, due to Dmin, for proper

conversion into the destination color space. There are a variety of VFX IO LUTs available in the 3D LUT

submenu of each node’s contextual menu that let you convert an image from Linear color space to any

other color space you want to work within.


Ingest and Organize Media | Chapter 25 Capturing From the Cintel Film Scanner

MEDIA

Using three nodes to convert a film scan using LUTs; node 1 converts from Negative or Print to

Linear, node 2 converts from Linear to Rec. 709, and node 3, if required, inverts the color

NOTE: Applying a LUT within a node will clip any image data falling below 0 and

above 1. To prevent clipping, you can use the Lift/Gamma/Gain controls within any node

with a LUT applied to adjust your image levels prior to the transform applied by the

LUT within that node.

The format of the film you’re scanning and the way the material was originally shot both affect the

framing. You can adjust the final framing of your scanned clip by resizing, zooming, stretching,

panning, tilting, and more. On the ‘Color’ page, open the ‘Sizing’ palette and use the ‘Input Sizing’

mode to create the necessary framing. To save your sizing preferences as a preset, open the

menu, select ‘save as new preset’ and enter a name for your preset.

Once you’ve created an appropriate sizing preset for a given type of media, you can apply that

preset to multiple film scans all at once, in either the Color page or in the Media Pool using the

‘change input sizing preset’ command, found in the contextual menu of selected clips.

For more information on sizing, see Chapter 152, “Sizing and Image Stabilization.”

Creating a sizing preset in the Sizing palette of the Color page


Ingest and Organize Media | Chapter 25 Capturing From the Cintel Film Scanner

MEDIA

CUT