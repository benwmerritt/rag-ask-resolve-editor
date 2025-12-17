---
title: "The Transcription Window"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 157
---

# The Transcription Window

The Transcription window is where the text is displayed, along with its timecode, options, and editing tools.

For ease of use the Transcription window is freely movable around the GUI, even to another monitor.

The Trascription window showing multiple clips with the Search pane open. The searched

for text is highlighted in yellow. The In and Out range of the clip is highlighted in teal, and

the current playhead position in the Viewer is indicated by a red triangle.


Edit | Chapter 40 Text Based Editing

EDIT

To access the Transcription window:

�Right-click on a clip or clips that have been transcribed, and select Transcribe Audio from the

contextual menu. Or click on the Transcribe Audio icon in the Media Pool toolbar.

The Transcription window is comprised of the following sections and tools:

Export: Clicking this icon will launch a file browser, where you can save a .txt file of the

transcription results for use in other programs.

Search: Clicking this icon will expose a Search and Replace dialog, letting you find

specific words or phrases across all the selected clips in the Clips panel. Found words

will be highlighted in yellow. You can also search and replace using partial words in the

Transcription window. To change the parameters of the search, open the search bar

and select either Contains or Full Word from the drop-down menu to the left.

You can also search for partial words in the  Transcription window by using the Contains option.

Options Menu: Reveals the Transcription window options.

�Speaker Detection: Enabling this option will analyze and assign a speaker number

to a specific voice. This speaker is subsequently remembered across all clips in

a project.

�Display Speakers: Turns the Speaker column on or off in the Transcription window.

�Transcribe Missing Clips in Timeline: If you’ve added any clips into the timeline

that haven’t yet been analyzed for speech to text (transcription pending),

selecting this option will transcribe them and place them appropriately in the

Transcription window.

�Remove Silent Portions: Removes all silences (…) detected from the

Transcription window.

�Create Subtitles from Audio (Timeline only): Creates a new Subtitle track and

places subtitles automatically.

For more information on the Create Subtitles from Audio feature,

see Chapter 52, “Subtitles and Closed Captioning.”

�Import Subtitles (Clip only): Allows you to import a subtitle in .srt format

(described later in this chapter).

�Export Subtitles: Allows you to export your subtitles in .srt format

(described later in this chapter).

�Reset Speaker Data: Removes all saved speaker detection data from the project.

Clips: This panel shows all the selected clips that you’ve chosen to see the

transcription for. Clicking on a thumbnail loads that clip’s transcription into the Transcript

window. The selected clip is outlined in orange. If you only selected one clip, this panel

does not appear.

Transcript: Displays the transcription text. You can also use this box to select the

playhead position, and set in and out points of a clip as described in the Text Based

Editing section below.


Edit | Chapter 40 Text Based Editing

EDIT

Remove Silent Portions: Removes all detected silences (…) from the transcript.

Text View Controls: Allows you to control the font size and the high contrast settings of

the text in the Transcript window.

Create Subclip: Creates a new subclip of the shot based on the In and Out points set

by the highlight in the Transcript window.

Marker: Places a marker at the word location that is highlighted in red, or if an In/Out

range is highlighted, it will place a duration marker for the range instead.

Stop: Stops playback of the clip in the Viewer.

Play: Plays the clip forward realtime in the Viewer.

Play in to Out: Plays forward only between the set In and Out range.

Place on Top: Performs a Place on Top edit of the selected range into the timeline.

Insert: Performs an Insert edit of the selected range into the timeline.

Append: Performs an Append edit of the selected range to the end of the timeline.

Editing Text in the Transcription Window

Not everything transcribed in the audio of a clip is useful or wanted in the final transcription.

Crew chatter, flubbed lines, and long silences can all be edited out, as well as mistakes fixed in the

Audio Transcription process itself.

Selecting Text

In order to edit text, you first need to select it in the Transcription window. There are a few ways of

doing so, depending on how much text you wish to select.

To select a specific word in the transcription:

Double-click on the word to select it and highlight it in teal.

To select a range of text in the transcription:

Click and drag over the text you want to edit to select it and highlight it in teal.


Edit | Chapter 40 Text Based Editing

EDIT

To select a sentence in the transcription:

Click on any word in the sentence and press the X key to select the whole

sentence and highlight it in teal.

To select an entire paragraph in the transcription:

Triple-click on any word in the paragraph to select the whole paragraph and highlight it in teal.

To select all the text in the transcription:

Press Command-A to select all of the text and highlight it in teal.

To deselect select all the text in the transcription:

Press Option-X to deselect the all of the text and highlight it in teal.

Editing Text

Once any text is selected (highlighted in teal), you can right-click on it to bring up the editing options.

Clicking on any of the editing tools, executes the action.

The Transcription window editing tools (l-r): Edit, Delete, Undelete, Copy,

and Assign To, are accessed by right-clicking on any selected text.

Edit: Clicking on this tool brings up a text field, where you can perform simple edits

on the selected text. You can use this to correct the transcription in terms of wrong

words, spelling mistakes and adjusting proper names. Radically altering the text,

such as replacing an entire paragraph with a two or three word summary will have

unpredictable effects if used for editing. This action is undoable.

Delete: Clicking this tool does not delete the selected text from the Transcription

window as in a word processor, instead it will mark the text in orange with a strike-

through. Any text thus marked will not appear in the exported transcript, nor will its

range be inserted into the Timeline with any edit operation. This means a cut will

appear in the Timeline where the deleted text range is in the transcript. Since the words

are all still there in the audio clip as they were recorded, it may be easier to think of this

as an “exclude” operation rather than a deletion.

Undelete: Clicking on this tool reverses any previous deletion. It changes the orange

strike-through text back into normal text, allows it back into the exported transcription,

and re-includes its range for editing purposes.

Copy: Copies the selected range for use in other applications. There is no

Paste command for the Transcription window.

Assign To: If the automatic speaker detection has made an error in who is saying

this line, you can manually assign it to a different speaker by selecting one from the

drop-down menu.


Edit | Chapter 40 Text Based Editing

EDIT

Understanding Silence (…) in the Transcription Window

In most shots, a significant portion of the audio clip will have no dialog at all. These silences are

marked in the Transcription window as ellipses (…). As important as knowing where the dialog is, it’s

also useful to know where it isn’t. These silences (…) can be treated just like words in the Transcription

window, meaning they can be deleted, and thus excluded from any editing operation.

For example, say you have a long interview with frequent pauses between questions. You could cut

this long clip up manually by setting In and Out points and picking out the individual questions and

answers. But, by using Audio Transcription and deleting all the silences (…) in the Transcription window

and then editing that range into the Timeline, you would instantly have a series of individual clips

laid down comprised of only the questions and the answers. This lets you automatically insert all of

the relevant clips at once, without all the tedious scrubbing and setting of edit points for every single

section of the clip in the Viewer.

The original Interview clip (Tracks V1, A1 violet) and the same media with all silences removed using the Transcription

window (Tracks V2, A2). Note how it is automatically broken into individual question and answer clips.

Removing silences in the Transcript window has many useful applications for both exporting a

transcript and in text based editing, and so has a dedicated tool for deleting them all.

To delete all the silences (…) in the Transcription window:

•	 Click on the Remove Silent Portions icon just to the left of the Font Controls,

in the Transcription window.

•	 Click on the Option menu (three dots) in the upper right of the Transcription window, and

select Remove Silent Portions from the contextual menu.

Detect Speakers During Transcription (Studio Version Only)

DaVinci Resolve can now detect individual speakers when transcribing a clip, showing their specific

timecode range as well as the text for each speaker. Speaker detection can not only create more

useful text transcription exports but can be used for text based editing references.

Speaker Detection is project specific, so once you turn it on, it will remain on for all further transcription

operations, either for clips or timelines.


Edit | Chapter 40 Text Based Editing

EDIT

Turning on Speaker Detection in a clip’s context menu.

To Enable Speaker Detection for Transcriptions:

•	 Right-click on a clip or timeline and select AI Tools > Audio Transcription >

Speaker Detection.

•	 Or select Speaker Detection from the Transcription window’s Option menu.

•	 Click on the Transcribe option to start the operation.

Transcription and Speaker Detection in Timelines

You can also choose to Transcribe and Detect Speakers for a timeline. This will analyze the timeline

and transcribe the underlying media. It will then give you a timeline transcription based off the In and

Out points of each clip in the timeline and assign speakers to each segment. Timeline Transcriptions

are opened in Timeline Transcription mode, as described below.

The Transcription window with Display Speakers active. You can change the name of a

speaker by double-clicking the name and entering a new one in the text field.


Edit | Chapter 40 Text Based Editing

EDIT

With Speaker Detection enabled, any subsequent audio transcriptions you generate for clips and

timelines will detect individual speakers. All the speaker’s voice signatures are remembered at the

project level across multiple clips. If you come back the next day to add more audio clips to your

project, DaVinci Resolve will remember the voices you analyzed previously, and automatically assign

them to the appropriate speaker. If you want to remove the saved speakers from your project, select

Reset Speaker Data, from the Transcription window’s Option menu.

In the Transcription window, speakers will initially be listed numerically (Speaker 1, 2, 3 etc.). You can

change the name of the speaker by double-clicking on the speaker name and entering a new name in

the text field. All other instances of that speaker will be changed to the new name.

If the Speaker Detection made an error about who is speaking, you can manually re-assign a text to

another speaker by selecting the text, right-clicking on it and choosing the Assign To icon from the

pop-up menu. Then another dialog box will appear letting you change the attribution to any of the

other detected speakers.

You can manually change the speaker attribution by right-clicking on the text and selecting the Assign To icon.

If you wish to hide the speakers again, in order to declutter the Transcription Window you can toggle

their view on or off in the Transcription window’s Option menu, under Display Speakers. Toggling this

feature does not remove the speaker associations that have already been set.