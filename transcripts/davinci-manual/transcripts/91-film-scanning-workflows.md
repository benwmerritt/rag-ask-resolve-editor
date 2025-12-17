---
title: "Film Scanning Workflows"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 91
---

# Film Scanning Workflows

The following sections describe how to scan film using DaVinci Resolve and to control the

Cintel scanner. Throughout, the features outlined in the previous section are presented in

the order in which you’ll perform each step of the scanning process.

Before You Begin

Before turning your scanner on and loading film, you should first dust the gate to make sure your scans

are as clean as possible. This can be accomplished using compressed air, but if the gate is extremely

dirty, you can remove it to give it a more thorough cleaning. Once that’s finished, turn on the Cintel

Scanner, open DaVinci Resolve and create the project you’ll be using to scan film, and then click the

‘Cintel scan’ button on the media page. Now click the ‘Film Scanner’ tab to select DaVinci Resolve’s

film scanner panel.

Before you load film into the scanner or do anything else, click the ‘calibrate’ button at the bottom

left of the film scanner panel. While you should always dust the gate of the scanner before loading a

new reel of film, clicking the calibrate button eliminates any unremovable blemishes in your scanner’s

optics from the scans you’re about to make.


Ingest and Organize Media | Chapter 25 Capturing From the Cintel Film Scanner

MEDIA

Load and Align the Film

Load the film you want to scan. In the presence of an image the scanner will automatically align a

frame. You should note that the image may be framed incorrectly if you first load blank film leader.

Next, choose the film type. If necessary, use the ‘perf nudge’ and ‘frame’ buttons to manually improve

the alignment of the framing bar to the scanner’s sensor such that the bottom of the previous frame

and the top of the next frame are just visible at the top and bottom of the viewer, and the current

frame is centered vertically. It’s important to make sure the image in the viewer is not zoomed in when

you do this.

Focus the Scanner

Just as you need to focus the lens on a camera, you’ll need to focus the projected film image on your

scanner’s sensor. To achieve perfect focus, turn on the Focus Assist checkbox in the Film Scanner

capture settings of DaVinci Resolve. This superimposes a focus peaking overlay over the Ultra HD

image that’s output from the scanner’s HDMI output, and is also displayed in DaVinci Resolve’s capture

window. For the best results, connect an Ultra HD display to your Cintel scanner so that you can

monitor at the maximum available resolution while you focus.

With Focus Assist turned on, focus peaking will detect the film grain of the scanned image whenever

the film plane is in perfect focus. This enables the operator to focus the scanner even if the film image

is out of focus. Simply monitor the Ultra HD output of the scanner while you turn the Cintel scanner’s

focus wheel. Your image will be in focus when the grain running throughout the image displays

peaking outlines.

You can verify the focal adjustments you’ve made by checking the edges of your film’s perforations.

When these are sharp, your film will be in focus.

Reset the Timecode

To set the timecode for the roll of film you’re about to scan, you need to locate the zero frame for

that roll. It’s standard practice to punch a small physical hole within the frame before the first frame

of necessary film on a roll, to use as a permanent reference for whenever that roll is scanned. This

is referred to as the marker frame, lab roll hole, or head punch. By always setting the first frame

of timecode to match the marker frame, subsequent film scans will have the same frame count as

previous scans, making it possible to rescan and reconform the same material whenever necessary.

To reset scanned timecode at the marker frame of a new film roll:


Use the transport controls under the viewer to locate the marker frame.


Click the ‘viewer’ option menu and choose ‘current frame timecode.’

Choosing Current Frame Timecode from the Viewer Option menu


Enter a timecode value in the dialog box that appears. For example, if you’re scanning the first

roll of a project, you can enter 01:00:00:00.


Ingest and Organize Media | Chapter 25 Capturing From the Cintel Film Scanner

MEDIA

The Set Current Frame Timecode dialog


When you’re done, click OK.

Timecode cannot be a negative value, so don’t set the start frame to zero. Another common

organizational technique is to change the hour number whenever you change rolls, to coincide with

the film roll’s number, which makes it easy to identify a scanned clip with the corresponding source roll

and frame range.

Your Cintel Scanner has built in ‘Options Interface’ ports for adding optional hardware in the future.

This offers the ability to add optional features such as reading KeyKode from the camera negative, or

optical/magnetic audio. For more information, see the ‘Optional Audio and KeyKode Reader’ section in

the Blackmagic Cintel manual.

Choose a Location to Save the Scanned Frames

Once all this is done, scroll down to the ‘capture info’ controls in DaVinci Resolve’s film scanner panel,

and click the ‘browse’ button to choose a location for the scanned files. You can use the other fields

in this section to set what prefix you want to add to the name of the scanned files and enclosing

folders. The ‘file name prefix’ updates the file name preview that’s shown at the top in the header. The

header also shows the file path, resolution, frame rate, duration, and the format. Specify what roll, reel,

clip, and program information you want associated with the scanned media. The ‘timestamp prefix’

checkbox in the ‘Capture info’ controls is selected by default and will save your clips to independent

sub-folders within the destination folder, together with a timecode prefix in the file name.

If you want to save all your clips together in one master destination folder, simply deselect the checkbox.

When you capture an HDR clip, the scanner completes a high exposure scan and saves it in a hidden

folder named .HDR inside the same folder as the standard scan. If you delete the .HDR folder, the scan

converts to a normal clip after refreshing it in the media storage and re-importing the clip into media

pool. This is useful if there is a problem with the HDR portion of the scan, as you can easily convert it

to a regular CRI clip.

Check the Codec

DaVinci Resolve selects the ‘Cintel Raw’ codec by default, or you can choose ‘Cintel Raw 3:1’.


Ingest and Organize Media | Chapter 25 Capturing From the Cintel Film Scanner

MEDIA

The Cintel Raw Format

The Cintel Raw Format Bayer pattern of each film frame scanned with your Cintel scanner’s

sensor is saved with embedded scanner metadata as a 12-bit linear Cintel Raw Image, or CRI,

image sequence. When grading in DaVinci Resolve, CRI images are automatically debayered

as 12-bit log encoded image data.

The logarithmic encoding is similar, but not identical to Cineon encoding. For example,

negative film is encoded using a Gamma of 2.046 for density, while print film is encoded

using a full range Gamma 2.2 curve to ensure that no image data is clipped. Both of these

logarithmic encodings can be converted to a linear color space using the ‘Cintel to Linear’

1D LUT, before converting to other color spaces you may want to work in.

The film is scanned using the full sensor area of 4096x3072 to keep the audio waveform

visible for optical audio and to accommodate perforation visibility for stabilization. The image

is then cropped and the resolution of the capture files depends on the source film format

after overscan for perforations and the audio area are removed. For more information about

scanning resolutions for different types of film, see the ‘specifications’ section.

The Cintel scanner creates Cintel Raw files with variable bitrate lossless compression by

default. This is visually lossless compression and achieves approximately 3:2 reduction in file

size depending on image content. However, Cintel Raw 3:1 uses lossy compression with a ratio

of approximately 3:1. This is still very high quality but may not always be visually lossless.

For example, files for 35mm 4 perf are approximately 12.5MB with Cintel Raw and

approximately 6.3MB with Cintel Raw 3:1. Files for 16mm are approximately 4MB with Cintel

Raw and approximately 2MB with Cintel Raw 3:1.

CinemaDNG Quality Settings

To control the quality of CRI files, use the ‘decode quality’ and ‘play quality’ CinemaDNG settings

located in the Camera Raw panel of the project Settings. These settings are ‘full’ by default. On

computers with low processor or memory resources, these settings may be lowered but this will affect

the quality of the final render.

Set the Timeline Resolution

DaVinci Resolve displays and renders the output from the scanner using the same resolution as the

timeline. For example, for 35mm 4 perforation film, a custom resolution of 4096x3072 would be

required for maximum resolution.

NOTE: If your timeline is set for HDR with the desired deliverable at Ultra HD, a loss of

resolution may occur.

For more information on the cropped image area resolutions for all film gauges, refer to the ‘effective

resolutions’ in the ‘specifications’ section. Alternatively, for the full native resolution of the captured

clip, access the ‘clips attributes’ in DaVinci Resolve.


Ingest and Organize Media | Chapter 25 Capturing From the Cintel Film Scanner

MEDIA

Adjusting the Color of the Scanner

DaVinci Resolve’s film scanner panel gives you control over the exposure and color temperature of the

light used to illuminate the film for scanning. You can adjust these via the light source master wheel

and RGB controls, in order to maximize the amount of information you’re extracting from each frame,

while preventing any part of the image from being irretrievably clipped. While it’s true that CRI is a raw

image format, there’s no latitude beyond the internal data range used by DaVinci, so be mindful that if

you’re clipping data in the built in video scopes while scanning, it might be clipped permanently in the

scanned media.

How often you’ll adjust the color and exposure of scanned shots depends on how much variety there

is in the scenes on a particular film roll. For example, some rolls may have many takes of the same

scene, all of which have the same lighting and which can share the same adjustments.

Meanwhile, other rolls may have a variety of different scenes with widely different lighting in each one,

necessitating you to make individual adjustments for each scanned clip to maximize data quality.

This is important because the light source master wheel and RGB controls cannot be automatically

changed between scanned clips in a log and capture workflow. This means that the current light

source settings will be used for all clips you scan until you manually change those settings again, even

for clips that you’ve logged from different parts of a film roll. This means that the log and capture style

of working is only advisable in situations where it makes sense to log multiple clips that share the

same light source master wheel and RGB control adjustments.

Otherwise, it’s recommended you make lighting adjustments on a clip by clip basis, as you scan each

clip, in situations where you need maximum image quality for finishing. Keep in mind that the goal for

these adjustments is to maximize image data from the scan, not to create the final look of the clips,

which you’ll accomplish later in the grading phase of work using the controls of the ‘color’ page.

To adjust the light source settings, find a typical image for the section of roll or for the first series of

shots you’re going to scan, and adjust the light source while viewing the built in video scopes.

Adjust the light source master wheel to set the intensity of the light source used to illuminate the film,

raising or lowering the level of the R, G, and B channels all at once. For a typical camera negative,

this lets you adjust the black point of the film image. In a negative print, the darkest part of the image

corresponds to the highlights of the film image. Set the light source master wheel to sit just above

the typical Dmin value of 95, as measured on the histogram of the video scopes, which guarantees

that the highlights won’t be clipped by the Cineon LOG conversion that DaVinci uses to debayer the

CRI image for grading. For positive film, manually adjust the light source levels so that no part of the

highlights or shadows of the signal is being clipped; typically 1000 in 10-bit or 4000 in 12-bit.

You can turn on ‘show reference levels’ in the waveform, RGB parade, or histogram scopes, and set

the ‘low’ value to indicate the digital Dmin value of 95.

Once that’s accomplished, adjust the RGB controls to rebalance all three color channels by varying

amounts to alter the color temperature of the light source used to illuminate the film, to produce the

most useful, or neutral, color balance in the scanned result.

Scanning One or More Sections of Film

After you’ve adjusted the light source, it’s a good idea to stay organized as you scan each clip by

entering all relevant metadata into the metadata editor as you go. The ‘capture info’ group of metadata

fields contains information for defining the file name prefix, roll, reel number, clip number, program

name, flags, and whether a particular take is good. If you populate these fields before scanning a clip,

that metadata will be written into the clip.

At the bottom of the ‘capture info’ panel, you will see four buttons for film scanning.


Ingest and Organize Media | Chapter 25 Capturing From the Cintel Film Scanner

MEDIA

With all of this accomplished, you can scan the film in one of four ways:

�Capture Now: Use the capture now button to capture long sections of a reel all at once. Clicking

‘capture now’ begins scanning near the current frame, ending whenever you click ‘stop’.

If ‘Enable 2 Pass HDR Scan’ is selected, click ‘Capture HDR’ after the capture has begun to let

DaVinci Resolve know you’ve reached the end of your desired clip so it can now proceed to capture

the high exposure pass. If you scan the entire reel without clicking ‘Capture HDR’, the scanner

automatically proceeds with the high intensity scan from where you started it until the end of the reel.

�Capture Clip: A more controlled means of scanning specific sections of film. After you’ve used the

transport controls and the In and Out button to define a section of film, clicking ‘capture clip’ scans

that one clip and then stops.

If ‘Enable 2 Pass HDR Scan’ is selected, the high intensity HDR scan uses the same In and Out

points as the initial scan.

�Batch Clips: A way you can log multiple clips in advance of scanning them all at once using the

current light source settings in DaVinci Resolve’s film scanner panel. Log each clip in advance by

setting In and Out points for each section of film you want to scan, and click the ‘log clip’ button

to save that frame range as an unscanned clip in the media pool. When you click ‘batch clips’, all

unscanned clips will be scanned one after the other until the job is complete. You can also select one

or more unscanned clips, and only the selected clips will be scanned. Furthermore, you can import

an EDL that corresponds to a particular film roll, and use the resulting logged clips for scanning.

NOTE: When you click the ‘log clip’ button, Cintel Scanner applies the same project

settings to all clips in the batch, and uses the newest project settings at the time of

capture. You are advised to confirm the scanner settings before starting the batch

capture.

If ‘Enable 2 Pass HDR Scan’ is selected, the high intensity HDR scan uses the same sets of In and

Out points as the initial batch of scans.

For more information on batch capture workflows, see Chapter 24, “Ingesting From Tape.”

�

Snapshot: Capture a single frame with normal exposure and current scanner settings.

Once scanning, if DaVinci Resolve detects that your storage bandwidth is too low to capture at the

selected speed, the scan speed will automatically adjust to ensure the capture is successful. If you

are using the optional Audio and KeyKode Reader accessory, the audio sample rate will also be

adjusted to maintain your chosen audio quality.