---
title: "Project vs. Clip Mode"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 57
---

# Project vs. Clip Mode

Two buttons at the top of the Data Burn window let you choose whether you want to edit one set of

burned-in metadata that will be displayed for the entire duration of the Timeline, or edit burned-in

metadata on a clip-by-clip basis. You can combine the two, having timeline-wide window burn settings

and separate clip-specific window burn settings for a handful of clips in that timeline at the same time.

When rendering in the Delivery page, window burns are applied both when rendering timelines as

individual source clips and when rendering as one single clip.

Two separate panels let you adjust project-wide

window burns vs. clip-specific window burns

Setting Up Burned-In Metadata

Setting up different clip and project metadata to output as a window burn is easy.

To set up a window burn:


Choose Workspace > Data Burn-In.


Click Project or Clip at the top of the Data Burn-In window.


Turn on the checkboxes of whatever items of metadata you want to display in the “Add to

Video Output” column. More information about the available items appears later in this chapter.

The first item of metadata is centered near the bottom of the frame, above Action Safe. Each

additional item of metadata you turn on for display is added above whichever items are already

displayed, regardless of their position in the “Add to Video Output” list.


Click any currently enabled item of metadata from the list to highlight it in black, and edit that

item’s Custom Output parameters at the right. More information about the available parameters

appears later in this chapter.

To reset the current window burn setup:

Click the Reset button next to the Option drop-down menu to reset the current mode of the

Data Burn window.

Saving and Loading Burn-In Presets

If there are common sets of metadata that you regularly use and switch among, you can save each set

up as a preset for future use.

To save a burn-in preset:


Click the Option menu and choose Save As New Preset.


Type a name into the Burn In Preset dialog that appears, and click OK. That preset is added to the

list of saved presets in the Option menu.


Setup and Workflows | Chapter 12 Data Burn-In

MEDIA

To delete a burn-in preset:


Choose a preset from the Option menu.


Click the Option menu, and choose Delete.


A dialogue box appears asking you to confirm the deletion.

To modify a burn-in preset:


Choose a preset from the Option menu.


Edit it however you like.


Click the Option menu, and choose Update.

Data Burn-In Metadata

The leftmost column in the Data Burn-In window contains a list of all the options that you can add to

the video output as a window burn. Each option has a checkbox that lets you turn it on or off. You

can also select in the Option drop-down if you would like the item name rendered as a prefix to the

burn-in data.

NOTE: If two clips overlap in the Timeline, the metadata that matches the currently visible clip

in the Viewer is what will be displayed in the window burn.

�Record Timecode: The timecode relative to the Timeline, as set in the Conform Options section of

the General Options panel of the Project Settings.

�Record Frame Number: The number of frames from the first frame of the Timeline.

�Source Timecode: Each clip’s individual timecode.

�Source Frame Number: The number of frames from the first frame of the clip.

�Record TC & Frame Num: Both metadata options combined in one line.

�Source TC & Frame Num: Both metadata options combined in one line.

�Source & Record TC: Both metadata options combined in one line.

�Feet + Frames 35mm: Displays a Feet + Frames conversion of the program’s record timecode,

calculated for 35mm film.

�Feet + Frames 16mm: Displays a Feet + Frames conversion of the program’s record timecode,

calculated for 16mm film.

�Audio Timecode: The timecode of the audio track of the clip.

�Keycode: Also referred to as edge-code, the identification codes running along the edge of film

stocks that provide an absolute reference for which digital frames correspond to which film frames.

�Source File Name: The full file path, including file name, of the media file that’s

linked to the current clip.

�Record File Name: The file name as defined in the Render Settings list of the Deliver page.

�Source Clip Name: The file name of the media file that’s linked to the current clip,

without the file path.

�	Synced Audio File Name: The file name of the audio clip that’s been synced to the clip.

�	Synced Audio Timecode: The timecode of the audio clip that’s been synced to the clip.


Setup and Workflows | Chapter 12 Data Burn-In

MEDIA

�Custom Text1: A line of text that you type into the Text field of the Custom Output parameters.

You can use any characters you like. When editing any of the three custom text fields that are

available, you can use “metadata variables” that you can add as graphical tags that let you

display clip metadata. For example, you could add the corresponding metadata variable tags

%scene_%shot_%take and the custom text would display “12_A_3” if “scene 12,” “shot A,” “take 3”

were its metadata.

For more information on the use of variables, as well as a list of all variables that are

available in DaVinci Resolve, see Chapter 16, “Using Variables and Keywords.”

�Custom Text2: A second line of text that you can customize.

�Custom Text3: A third line of text that you can customize.

�Logo1: Lets you superimpose a graphic over the image in a customizable location. Compatible

graphics formats include PNG, TGA, TIF, BMP, and JPG. Alpha channels are supported for

transparency in logos.

�Logo2: Lets you superimpose a second graphic.

�Logo3: Lets you superimpose a third graphic.

�Reel Name: The currently defined reel number for the current clip.

�Shot: Shot metadata, if it’s been written to the file by a camera, or entered into the Metadata Editor

on the Media page.

�Scene: Scene metadata, if it’s been written to the file by a camera, or entered into the Metadata

Editor on the Media page.

�Take: Take metadata, if it’s been written to the file by a camera, or entered into the Metadata

Editor on the Media page.

�Angle: Angle metadata, if it’s been written to the file by a camera, or entered into the Metadata

Editor on the Media page.

�Day: Day metadata, if it’s been written to the file by a camera, or entered into the Metadata Editor

on the Media page.

�Date: Date metadata, if it’s been written to the file by a camera, or entered into the Metadata

Editor on the Media page.

�Good Take: Corresponds to Good Take metadata, if it’s been written to the file by a camera, or

entered into the Metadata Editor on the Media page.

�Camera: Corresponds to the Camera metadata, if it’s been written to the file by a camera, or

entered into the Metadata Editor on the Media page.

�Roll/Card: Corresponds to the Roll/Card metadata, if it’s been written to the file by a camera, or

entered into the Metadata Editor on the Media page.

Custom Output Options

The parameters in the Custom Output panel let you modify the look, position, and in some

cases content, of the selected metadata item. Pan and Tilt are individually customizable for each

metadata item.

�Display During First x frames: Turning on this checkbox lets you specify a number of frames

during which the current item of metadata will be displayed before dissolving away over one

second. When enabled, the current item of metadata will cut onscreen with the beginning of each

new clip, remain onscreen for the duration specified, and then dissolve away.


Setup and Workflows | Chapter 12 Data Burn-In

MEDIA

�Display During Last x frames: Turning on this checkbox lets you specify a number of frames

before the end of each clip during which the current item of metadata will appear onscreen after

fading up over one second, before cutting away with the end of the clip.

�Font: Defaults to Courier, but you can choose any font that’s installed on your system.

�Size: Defaults to 48, but you can choose standard increments from 6 to 72.

�Alignment: Defaults to Center. The only other option is Left.

�Font (color): Defaults to white, but you can choose from a range of predefined colors in this

drop-down menu.

�Background: Defaults to black, although the apparent color is influenced by the Opacity

setting. For a more garish look, you can choose from a range of predefined colors in this

drop-down menu.

�Text Opacity: Defaults to 1.00. Lets you define the transparency of the burned-in metadata’s text.

�Background Opacity: Defaults to 1.00. Lets you define the transparency of the burned-in

metadata’s background color.

�X-Y Position: Lets you change the horizontal and vertical orientation of the current item of

metadata. The default horizontal value is the center of the frame, relative to the current project’s

frame size. The first item of metadata is centered vertically near the bottom of the frame, above

Action Safe. Each subsequent item of metadata you turn on is automatically placed above the

previous item of metadata, regardless of its order in the “Add to Video Output” list.

�Text: (only if one of the Custom Text options is checked) A text field that lets you enter custom text

to display as one of three possible custom text items.

�Logo: (only if one of the Logo options is checked) A field that displays the file path of any currently

selected graphic that you’re displaying as one of the three possible Logo graphics. Compatible

graphics formats include PNG, TGA, TIF, BMP, and JPG. Alpha channels are supported for

transparency in logos.

�Import File button: (only if one of the Logo options is checked) Lets you choose a graphics file to

use as a logo.

Gang Rendered Text Styles

You have the option of independently styling each item of metadata, depending on whether the Gang

Render Text Styles option is checked in the Data Burn-In window’s Option menu. When turned on, all

text metadata share the same font, size, color, background, justification, and opacity. When turned off,

each item of metadata can have individual settings.

Prefix Render Text

Another option in the Data Burn-In window’s Option menu lets you turn the prefixes, or headers, on or

off for all metadata that’s enabled to be burned in.


Setup and Workflows | Chapter 12 Data Burn-In

MEDIA

Chapter 13

Frame.io and

Dropbox Replay

Integration

DaVinci Resolve has sophisticated integrations with Frame.io, and Dropbox

Replay video review and collaboration services designed specifically for the

postproduction industry.

Contents

Enabling Frame.io Integration in Preferences����������������������������������������������������������������������������������������������������������������������� 304

Deliver and Upload to Frame.io���������������������������������������������������������������������������������������������������������������������������������������������������� 304

Frame.io Comments Sync with Timeline Markers��������������������������������������������������������������������������������������������������������������� 305

Importing Media from Frame.io���������������������������������������������������������������������������������������������������������������������������������������������������� 307

Linking Media Pool Clips and Timelines with Frame.io Clips���������������������������������������������������������������������������������������� 308

Enabling Dropbox Replay Integration in Preferences������������������������������������������������������������������������������������������������������� 308

Deliver and Upload to Dropbox Replay������������������������������������������������������������������������������������������������������������������������������������ 309

Upload New Versions to Dropbox Replay��������������������������������������������������������������������������������������������������������������������������������� 310

Dropbox Replay Comments Sync with Timeline Markers������������������������������������������������������������������������������������������������ 310

Working With Dropbox Markers������������������������������������������������������������������������������������������������������������������������������������������������������ 311


Setup and Workflows | Chapter 13 Frame.io and Dropbox Replay Integration

MEDIA