---
title: "Create Subtitles from Audio Language Support"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 201
---

# Create Subtitles from Audio Language Support

As of this writing, Create Subtitles from Audio supports the following languages:

�Chinese (Simplified Mandarin), Danish, Dutch, English, French, German, Italian, Japanese, Korean,

Norwegian, Portuguese, Russian, Spanish, and Swedish.

�Many other languages are also available by using the Extended AI Transcription Support

Package in the Extras Downloads Manager. These include: Afrikaans, Arabic, Armenian,

Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Croatian, Czech, Estonian, Finnish, Galician,

Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Kannada, Kazakh, Latvian, Lithuanian,

Macedonian, Malay, Marathi, Maori, Nepali, Persian, Polish, Romanian, Serbian, Slovak, Slovenian,

Swahili, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.

Editing Subtitles and Captions

Subtitle clips can be selected singly or together, and slipped, slid, resized, rolled, and rippled just

like any other clip in the Timeline, using the mouse or using keyboard commands, with either the

Selection, Trim, or Razor tools. You can select subtitle clips in their entirety, or just their edit points,

in preparation for nudging or dynamic trimming. In short, subtitle clips can be edited, in most ways, just

like any other clips.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

Styling Subtitles and Captions

When it comes to styling subtitle text, there are a wealth of styling controls in the Track Style panel

of the Inspector.

To modify the styling of all titles on a particular subtitle track:


Click on the header of the subtitle track you’ll be working on, or select a clip on a particular

subtitle track either in the subtitle track or in the subtitle list of the Captions panel in the Inspector.


Open the Inspector, and then open the Track panel that appears within.


Edit whatever parameters you need to set the default style of all subtitles and closed captions that

appear on that track. The Track panel has many more options than the Captions panel, including

a group of Style and Position controls over Font and Font Face, Color, Size, Line Spacing, and

Kerning, Alignment, Position X and Y, Zoom X and Y, Opacity, and Text Anchoring.

Selecting a Font Case in the Track tab

of the Subtitle Inspector

Keep in mind that there are additional groups of controls that let you add a Drop Shadow, Stroke,

and/or Background to all text on that track, which can be found at the bottom of the Track panel of

the Inspector.

You can also modify the look of each subtitle clip individually, even down to changing a single

word or letter, regardless of the settings in the Track panel.

To modify the styling of a single subtitle on a particular subtitle track:


Select a clip on a particular subtitle track, either in the subtitle track or in the subtitle list of the

Captions panel in the Inspector.


Select the Customize Caption check box under the Caption.


Edit whatever parameters you need to set the style of only this single subtitle. All other titles in the

track will remain in the original track style.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

To modify the styling of a single word or words in a particular subtitle:


Select a clip on a particular subtitle track, either in the subtitle track or in the subtitle list of the

Captions panel in the Inspector.


Select the Customize Caption check box under the Caption.


Highlight the text that you want to change in the Caption panel.


Edit whatever parameters you need to set the style of the highlighted text on this subtitle. All other

titles in the track will remain in the original track style.

Checking the Customize Caption box reveals the tools for changing the look of an individual subtitle or text.

Using Subtitle Track Style Presets

If you want to save and re-use a specific subtitle style, you can add it to the Subtitle Style Preset menu,

accessed by clicking on the Subtitle option menu (3 dots) in the upper right corner of the Subtitle

Inspector. You can also export and import presets to share a subtitle style between systems.

To add a new subtitle style preset:


Create a subtitle track and adjust its style in terms of fonts, position, colors, etc.


Click on the option menu (3 dots) in the upper right corner of the Subtitle Inspector.


Select Save Track as Preset from the drop-down menu.


Give your preset a new name.

Your subtitle style preset will now appear in the Subtitle Inspector’s option menu.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

To change a subtitle track to another style preset:


Select an existing subtitle track that you want to change.


Click on the option menu (3 dots) in the upper right corner of the Subtitle Inspector.


Select the subtitle style preset from the drop-down menu.


Select Load Preset from the submenu.

Your subtitle track will instantly be updated to the new style preset. This command is undoable.

To update a subtitle style preset:


Load a subtitle style preset from the Subtitle Inspector option menu.


Make any changes you need to the style in terms of fonts, position, colors, etc.


Click on the option menu (3 dots) in the upper right corner of the Subtitle Inspector.


Select the subtitle style preset you wish to update from the drop-down menu.


Select Update Preset in the submenu.


Select Update from the dialog box.

Your subtitle style preset will replace the existing preset of the same name. There is no undo for

this action.

To delete a subtitle style preset:


Click on the option menu (3 dots) in the upper right corner of the Subtitle Inspector.


Select the subtitle style preset you wish to delete from the drop-down menu.


Select Delete Preset in the submenu.


Select Delete from the dialog box.

The subtitle style preset will be removed from the Subtitle Inspector’s option menu. There is no

undo for this action.

To export a subtitle style preset:


Click on the option menu (3 dots) in the upper right corner of the Subtitle Inspector.


Select the subtitle style preset you wish to export from the drop-down menu.


Select Export Preset in the submenu.


Choose the location to save the “.preset” file from the file browser.


Press Save.

The subtitle style preset file will be saved to the user’s computer. The file will have the name of the

preset with a .preset extension.

To import a subtitle style preset:


Click on the option menu (3 dots) in the upper right corner of the Subtitle Inspector.


Select Import Preset in the submenu.


Choose the location of the “.preset” file from the file browser.


Press Open.

The subtitle style preset will be added to the Subtitle Inspector’s option menu.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

The Subtitle Style Preset menu, found in the

option menu of the Subtitle Inspector

AI Animated Subtitles (Studio Version Only)

There is a set of Fusion Title Templates called Animated in the Titles tab. These templates can be

added to subtitle tracks, allowing you to easily create animated subtitle effects. These effects work

in conjunction with DaVinci Resolve’s transcription engine to match and highlight spoken audio with

subtitle timing.

You can audition the prebuilt templates in the Animated section of the Titles tab, and of course using

Fusion you can crate your own custom templates as well.

To animate your subtitles, simply drag the animated template from your Titles library on top of the

header of the subtitle track. You can customize their parameters in the Inspector.

The Word Highlight animated template has been applied, highlighting each word in red as it is spoken in the clip.

Subtitle Tracks Using Fusion Templates for Styling

You can style a subtitle track using a Fusion template. To style a subtitle track, just drag any Fusion

title template from the effects library on the subtitle track header. The Fusion effects now override any

track or per-caption styling applied to the track via the Inspector, allowing you to create fine-tuned text

looks from the underlying Fusion compositions.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

Using a Fusion template to create stylized subtitles