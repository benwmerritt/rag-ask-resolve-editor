---
title: "Importing Subtitles and Captions"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 200
---

# Importing Subtitles and Captions

Oftentimes, adding subtitles or closed captions to a DaVinci Resolve timeline will involve importing

a subtitle file that’s been prepared elsewhere. Currently, DaVinci Resolve supports subtitle files in

multiple formats such as .srt, .srtx, .vtt, .xml, and .ttml.

To import a subtitle or closed captioning file using the Media Pool:


Open the Media Pool.


Navigate to the folder containing your subtitles. Compatible subtitles will show up as a blank clip

icon with a subtitle icon in the lower left corner.


Add the subtitle to the Media Pool by dragging, importing via the contextual menu, or any other

method identical to adding video clips into the Media Pool.

To import a subtitle or closed captioning file using the Import Subtitle function:


Open the Media Pool.


Right-click on any bin in the Bin list, or anywhere in the background of the Media Pool browser,

and choose Import Subtitle.


In the resulting file dialog, find and select the subtitle file you want to import, and click Open.


The subtitle file appears as a subtitle clip in the Media Pool, ready for editing into a subtitle track.

A badge indicates that it’s a subtitle clip.

An imported .srt subtitle file

TIP: Subtitle files can be relinked in the Media Pool, just like video clips.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

To add a subtitle clip to the Timeline:


To add a subtitle clip to a timeline automatically and match its position via timecode:

�Right click on the subtitle and select “Insert Selected Subtitles to Timeline Using Timecode.”

The subtitle clip will decompose into individual subtitles appearing in the subtitle track, and each

subtitle will be aligned with the timeline’s timecode.


To add a subtitle clip to a timeline manually if you don’t have matching timecode,

do one of the following:

�Drag a subtitle file you’ve imported into the unused gray area at the top of your video tracks,

and a subtitle track will automatically be created for adding those subtitles into

�Drag a subtitle file you’ve imported into a pre-existing subtitle track

As you drag the subtitle clip, it’ll immediately be decomposed so that each title is added to the

Timeline as an individual subtitle clip, with its timing offset relative to the position of the first

frame of the first subtitle in that file.

The original Timeline

The Timeline after dragging a subtitle file has created a new subtitle track


Position the imported subtitles so that they align with the first frame of your program that they’re

supposed to, and drop the titles into the track. If you inadvertently misplace the subtitles, don’t

worry, you can always select them all and slide them earlier or later, just like any other clips.


If you’ve added a new subtitle track, you can rename it to identify what language and country that

track corresponds to. Please note that subtitle track names are used when exporting or encoding

subtitles, so please make sure your tracks are named appropriately prior to export/delivery.


If you want to restyle all of the subtitles you’ve just added, for example to make them smaller or

change the font, then click on the header of the subtitle track you’ll be working on, open the Track

panel of the Inspector, and select the formatting you want that track to use.

To see a list of every subtitle clip you’ve added, you can select the header of the subtitle track you’ve

just added and open the Captions panel in the Inspector. A list at the bottom of the Captions panel

gives you a convenient way of navigating the subtitles in a given track (using the Prev and Next

buttons) and making selections. If you set the Inspector to be full height, you’ll have even more room

for browsing the subtitle list.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

The Captions list shows you

every caption or subtitle on

a track, for selecting, editing,

deleting, or navigating

Adding Subtitles and Captions Manually

Other times, you may need to create subtitles on your own. Before doing so, you’ll need to add one

or more subtitle tracks. Once those tracks are created, you can add subtitle generators to them in a

variety of ways. You can add as many subtitle tracks as you need, one for each language you require.

To add new subtitle tracks:

�Right-click in any track header of the currently open timeline, and choose Add Subtitle Track.

An empty subtitle track will appear at the top of the Timeline, named “Subtitle 1,” and if Subtitle

Tracks were hidden, they’re now shown. Once you’ve added a new subtitle track, you can rename

it to identify what language and country that track corresponds to. Please note that subtitle track

names are used when exporting or encoding subtitles, so please make sure your tracks are

named appropriately prior to export/delivery.

You can show and hide subtitle tracks in case you need to free up room in the Timeline for

working on other tracks. Subtitles on the currently selected subtitle track continue to be visible,

however, regardless of whether or not the subtitle tracks are shown.

Showing and hiding subtitles tracks:

�Open the Timeline View options, and click on the Subtitle button to toggle the visibility of subtitles

tracks on and off.

The show/hide subtitle

tracks button in the

Timeline View Options


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

To add individual subtitles to a subtitle track:


If you want to adjust the default style of a particular subtitle track before you start adding subtitles,

then click on the header of the subtitle track you’ll be working on, open the Track panel of the

Inspector, and select the formatting you want that track to use.


If you have multiple subtitle tracks, click the destination control of the subtitle track you want to

add titles to. They’re labeled ST1, ST2, ST3, etc.


Move the playhead to the frame where you want the new subtitle to begin.

Positioning the playhead where you want a new subtitle to begin


To add a new subtitle clip, do one of the following:

�Open the Inspector and click Create Caption in the Captions panel of the Inspector. If there’s

already one or more captions in that subtitle track, click the Add New button above the caption

list, instead.

�Right-click anywhere on the subtitle track and choose Add Subtitle to add a subtitle clip starting

at the position of the playhead

�Open the Effects Library, click the Titles category, and drag a Subtitle generator to the Subtitle

track you want it to appear on.

Manually adding a subtitle


If necessary, you can now edit the clip to better fit the dialog that’s being spoken or the sound

that’s being described, by dragging the clip to the left or right, or dragging the beginning or end of

the clip to resize it.


While the new subtitle clip you’ve created is selected, use the Captions panel in the Inspector to

type the text for that particular subtitle. The text appears on the subtitle clip as you type it.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

Editing the text of the subtitle we just created

Every time you add a subtitle, an entry is added to the subtitle list at the bottom of the

Captions panel in the Inspector. This list gives you another convenient way of navigating the

subtitles in a given track (using the Prev and Next buttons) and making selections.

Create Subtitles from Audio

(Studio Version Only)

Due to recent advances in AI and expert system technologies, it’s become possible to get remarkably

accurate and perfectly timed subtitles of spoken text using DaVinci Resolve’s Create Subtitles from

Audio function. Create Subtitles from Audio will analyze the speech in a timeline and automatically

create a subtitle track with all the spoken dialog converted into text subtitle clips.

Create Subtitles from Audio just doesn’t directly translate phonetic speech to text. It will also correctly

analyze the context of that speech and translate that into proper punctuation and grammar for the

subtitle. For example, Create Subtitles from Audio will pick out proper names and capitalize them, it will

add a question mark to the end of sentence if your subject is asking a question, it will add quotation

marks in the correct locations if your subject is quoting something, and if it detects music in the

background, it will add a [Music Playing] subtitle. It handles accents and knows when there are multiple

people speaking in the same scene. You may find it surprising just how accurate the Create Subtitles

from Audio tool can be.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

Create Subtitles from Audio fully automates the subtitling process.

To Create Subtitles from Audio for a timeline:


Open the Timeline you want to Create Subtitles from Audio in the Edit page.


Select an In-Out range for the subtitles on the Timeline, or leave blank to Create Subtitles from

Audio  for the entire Timeline.


Select Timeline > AI Tools > Create Subtitles from Audio.


In the Create Subtitles from Audio dialog, select the following options:

�Language: The language of the spoken text. Auto lets DaVinci Resolve detect the language

automatically.

�Caption Preset: The Caption Preset style you wish the subtitles to be formatted to.

�Max Characters per Line: The maximum number of characters per line in the subtitle. Larger

numbers create longer lines of text on the screen. Smaller numbers create shorter lines of text.

�Lines: Sets the choice between a single line or double lines of text for the subtitle.

�Gap Between Subtitles: The amount of frames inserted between subtitle clips. 0 is the default.


Click the Create button.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

The Create Subtitles

from Audio options

Create Subtitles from Audio will then start to transcribe the spoken text, and a dialog box will

show you its progress. When it’s finished, the resulting subtitles will be added to the Subtitle

track. If there is no Subtitle track on your Timeline, it will automatically make one for you. If

there is more than one subtitle track on your Timeline, Create Subtitles from Audio will always

use the highest track to write to.

The one area where the Create Subtitles from Audio tool will still commonly fail is having

overlapping dialog clips on multiple tracks. To work around this, you can mute any audio track

on the Timeline you don’t want used in the subtitle analysis.

Once the Create Subtitles from Audio is complete, you can manually edit the captions to

fix any minor errors using the tools described above in the Adding Subtitles and Captions

Manually section.