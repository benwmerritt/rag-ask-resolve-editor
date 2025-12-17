---
title: "Audio Transitions"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 191
---

# Audio Transitions

A single audio transition handles all of your crossfade needs.

Cross Fade +3/–3/0 dB: An audio-only transition that lets you fade from one audio clip to another.

Three different crossfades let you choose the power of the actual transition from one level to the other.

OpenFX Transitions

If you’ve installed one or more sets of OpenFX plugins on your DaVinci Resolve workstation, any

transitions within those sets will appear in the OpenFX panel of the Effects Library.

OpenFX transitions in the Effects Library


Editing Effects and Transitions | Chapter 48 Using Transitions

EDIT

Chapter 49

Titles, Generators,

and Stills

Using the Edit page, you can add titles, effects generators, and stills to your

timelines. You can also save customized titles, generators, and stills back to the

Media Pool for future use.

Contents

Adding Titles����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1038

Using Safe Area Overlays�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1039

Custom Action and Title Safe Areas������������������������������������������������������������������������������������������������������������������������������������������ 1039

Types of Title Generators��������������������������������������������������������������������������������������������������������������������������������������������������������������� 1040

DaVinci Resolve Title Generators���������������������������������������������������������������������������������������������������������������������������������������������� 1040

Editing Titles Within the Timeline Viewer������������������������������������������������������������������������������������������������������������������������������� 1040

Title Generator Panels���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1042

Shared Title Generator Parameters������������������������������������������������������������������������������������������������������������������������������������������� 1042

Title Generator Settings Parameters���������������������������������������������������������������������������������������������������������������������������������������� 1043

The Text+ Title Generator�������������������������������������������������������������������������������������������������������������������������������������������������������������� 1044

Text+ Viewer Controls���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1046

Fusion Titles and Fusion Templates������������������������������������������������������������������������������������������������������������������������������������������ 1047

MultiText Titles������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1047

Saving Titles in the Media Pool for Future Use������������������������������������������������������������������������������������������������������������������ 1048

Using Generators������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1049

ITU-R BT.2111-1 Color Bar Generators��������������������������������������������������������������������������������������������������������������������������������������� 1050

Fusion Generators������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1051

Using Stills���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1051

Photoshop File Support������������������������������������������������������������������������������������������������������������������������������������������������������������������� 1052


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

Adding Titles

There’s a collection of titles and generators in the Toolbox that you can use to create leader

when outputting to tape, add slates, create subtitles, and otherwise fulfill any textual needs your

program has.

To select and audition titles before you place them into the Timeline, ensure that “Hover Scrub

Preview” is checked in the Titles option menu, then simply hover your pointer over any thumbnail

in the Titles tab. If the title is animated  (i.e., Fusion titles), moving the pointer across the thumbnail

will preview the animation. Once you’ve chosen your title, you can drag it from the Titles tab to your

Timeline in the Edit page or in the Cut page to either the upper or lower Timelines, or use the editing

selection modes at the bottom of the tab.

Scrubbing over a Title Thumbnail previews the title in the Viewer.

Titles and generators can be edited much like any other clip. Furthermore, when selected, both titles

and generators expose the same Composite, Transform, and Cropping parameter groups as any other

clip; these parameters can be used to composite titles and fly them around in order to create different

text effects.

Methods of adding and editing generators and titles:

�To drag and drop a generator directly into the Timeline: If you simply drag and drop titles or

generators into the Timeline, the default duration of the resulting clip is 5 seconds. This duration

can be customized in the Edit panel of the User Preferences.

�To edit a generator using the edit overlays of the Timeline Viewer: Click the destination control

of the clip you want to edit a generator into, then set Timeline In and Out points to define the

duration of the resulting edit, and drag the generator you want to edit onto the edit overlay of the

Timeline Viewer that corresponds to the type of edit you want to perform.

�To reposition the text of a title in the Timeline Viewer: Select the title generator you want to

edit in the Timeline, then click the visible text in the Timeline Viewer so that its bounding box is

selected; in this state you can reposition, scale, and rotate the text item. As you reposition text, it

will snap to key regions of the frame such as the vertical and horizontal center of the Viewer; hold

the Option key down to suspend snapping if you want to freely position the text.

�To edit the text of a title in the Timeline Viewer: Select the title generator you want to edit in

the Timeline, then double-click the visible text in the Timeline Viewer to insert a text editing

cursor. At this point, you can select, delete, or add any text you want by typing directly in the

Timeline Viewer.

�To edit the parameters of a generator or title: Open the Inspector, and select the generator or

title you want to edit to open it into the Inspector.


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

Using Safe Area Overlays

This drop-down menu overlays many useful framing guides over the Viewer to let you see what part of

the image will be included and what will part will be cropped out if you change the Timeline’s aspect

ratio. The framing guides can be turned on and off by toggling the Safe Area Framing Guide icon in the

Viewer, and the exact guides can be selected in the drop-down menu.

Social Media: 1:1, 4:5, 9:16, 1.91:1, 16:9.

Broadcast and Film: Default (your current timeline aspect ratio), 1.33, 1.66, 1.77, 1.85, 2.35.

Safe Area Guides: These options add additional guide lines on the Viewer to protect your

composition from possibly being cut off at the extreme edges of a physical cathode ray

tube. While somewhat anachronistic in this age of flat screen digital televisions, many legacy

programs still adhere to these guidelines. Safe Areas still can be useful guides in ensuring

your image is not inadvertently cropped by the variety of mobile devices and social media

sites in use today.

•	 Action: Keep all movement and important action within this box.

•	 Title: Keep all on screen text within this box.

•	 Center: Designates the exact middle of the image.

The Safe Area Framing Guide icon (circled)

and the possible framing options

The safe area overlays

Custom Action and Title Safe Areas

The Editing panel of the User Preferences has a new “Use custom safe area overlays” checkbox that,

when turned on, displays Action Area and Title Area fields that let you set a custom percentage for

each. The default values are 93% for Action Area and 90% for Title Area.


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

Types of Title Generators

When opened into the Inspector, titles expose a set of text parameters that allow you to style the

contents of that clip’s Text field within the Inspector. Each of the titles supports rich text, so you can

individually style words, lines, or paragraphs of text using the available parameters including Color,

Font, and Size. Other attributes such as Alignment, Anchor, Position, and Shadow affect the entire title.

The following titles are available:

L Lower 3rd: (supports rich text) Automatically positions two lines of text at the bottom left

corner of title safe, each with a different set of rich text and Position/Zoom/Rotation controls

for independent sizing and animating.

M Lower 3rd: (supports rich text) Automatically positions two lines of text at the bottom middle

of title safe, each with a different set of rich text and Position/Zoom/Rotation controls for

independent sizing and animating.

R Lower 3rd: (supports rich text) Automatically positions two lines of text at the bottom right

corner of title safe, each with a different set of rich text and Position/Zoom/Rotation controls

for independent sizing and animating.

Scroll: (supports rich text) Automatically automates a scrolling title sequence from the bottom

to the top of the screen. The duration of the generator clip in the Timeline determines the

speed of the scroll. Identical parameters as the Simple title.

Text: (supports rich text) Useful for creating titles consisting of a word, line, or paragraph of

text. A single body of text shares one set of rich text controls that let you style selected parts

of the title text differently.

Text+: (does not support rich text) An advanced title generator based on the title generation

tools on the Fusion page. This generator has significantly more options for styling, rendering,

and animating than the simple title generator above, but all title text shares a single style.

Fusion Titles: A variety of pre-built title templates assembled in Fusion. DaVinci Resolve

comes with a library of pre-assembled Fusion titles, but you can also create your own to

appear in this category of the Effects browser.

DaVinci Resolve Title Generators

The original title generators that shipped with DaVinci Resolve all share similar controls, and they all

share the ability to support rich text styling.

Editing Titles Within the Timeline Viewer

Once you add a title generator to the Timeline, the original title generators that shipped with DaVinci

Resolve have onscreen controls that let you edit text and transform and position blocks of text directly

within the Timeline Viewer.


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT

Positioning and Transforming Text

So long as the Timeline playhead is positioned over a text generator that’s on top of one or more

background clips, clicking on the text in the Timeline Viewer reveals onscreen transform controls that

correspond to the Position, Zoom, and Rotation parameters in the Inspector.

Drag the text to position it in the Viewer

While dragging text to reposition it, snapping occurs at the X and Y center of the frame, as well as

around the outer third of the frame. Holding the Shift key down while dragging a text object constrains

movement to just the X or Y axes.

Editing Text

Double-clicking on text in the Timeline Viewer puts that text into an editable state, wherein you can

insert a text cursor or select characters to edit the text as you would in any text editor.

Double-click on the text to edit it in the Viewer


Editing Effects and Transitions | Chapter 49 Titles, Generators, and Stills

EDIT