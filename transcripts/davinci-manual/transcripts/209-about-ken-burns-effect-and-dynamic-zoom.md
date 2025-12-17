---
title: "About “Ken Burns Effect” and Dynamic Zoom"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 209
---

# About “Ken Burns Effect” and Dynamic Zoom

If you import a project from Final Cut Pro X with clips that use the Ken Burns effect for creating pan and

scan animation, then the Dynamic Zoom parameters (found in the Edit page Inspector when a clip is

selected) for each affected clip will be populated with an equivalent animated effect.

About Speed Effects

DaVinci Resolve supports the import of speed effects from different applications, but different project

formats have different speed effect support.

EDL: DaVinci Resolve only supports the import of linear speed effects when importing EDLs.

XML: DaVinci Resolve supports the import of both linear and variable speed effects when

importing XML project files from Premiere Pro, Final Cut Pro 7, and Final Cut Pro X. As of

DaVinci Resolve version 11.1, XML from Final Cut Pro X can also provide information about whether

frame blending or optical flow is used, as well as information about the Bezier curve transitions of

speed effects.

AAF: DaVinci Resolve supports the import of both linear and variable speed effects when importing

AAF files from Media Composer or Symphony that use Timewarp effects.

DaVinci Resolve has high-fidelity conversion of variable-speed speed effect data from other

applications, accomplished by creating one speed keyframe per frame for each affected clip.

However, you may see small variations between the resulting speed effect in DaVinci Resolve and an

offline reference movie exported from the original NLE if you haven’t set the Retime Process setting to

the same type of speed interpolation that the original NLE was using.

In other words, if you created a Timewarp speed effect in Media Composer that uses

FluidMotion to create smooth slow motion effects, then you’ll want to make sure to change

either the project-wide or clip-specific Retime Process setting to Optical Flow so that the

speed effects in DaVinci Resolve best match those in Media Composer.

For more information on speed effects in DaVinci Resolve, see Chapter 51, “Speed Effects.”

About Nested Sequences and Compound Clips

DaVinci Resolve supports the import of compound clips from Final Cut Pro X and of nested sequences

from legacy Final Cut Pro 7. Both appear within DaVinci Resolve as compound clips, in both the

Timeline and the Media Pool. Compound clips with mixed frame rates are supported, as well as multi-

cam and A/V synchronized clips from Final Cut Pro X, which are represented in DaVinci Resolve as

compound clips.

For more information about creating and using compound clips in DaVinci Resolve, see the

“Compound Clips” section of see Chapter 43, “Take Selectors, Compound Clips, and Nested

Timelines.”


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT

About Supported Composite Modes

When importing XML project files from Final Cut Pro 7, Premiere Pro, and Final Cut Pro X, DaVinci

Resolve supports the import of eight different composite modes. When importing AAF files from Media

Composer, the Overlay composite mode is supported when the source AAF file has a Superimpose

effect applied to it.

FCP 7/X XML

AAF

Add

Yes

No

Subtract

Yes

No

Difference

Yes

No

Multiply

Yes

No

Screen

Yes

No

Overlay

Yes

Yes

Lighten

Yes

No

Hardlight

Yes

No

Softlight

Yes

No

Darken

Yes

No

Supported composite modes with imported XML and AAF

About Supported Still Image Formats

DaVinci Resolve supports the import of greater-than-one-frame-in-duration TIF, JPG, PNG, DPX, TGA,

and DNG still image files that appear in Final Cut Pro X, Final Cut Pro 7, and Premiere Pro XML files,

and AAF files exported from Media Composer. These clips appear as ordinary clips in the DaVinci

Resolve Timeline. Export of still images is limited to Final Cut Pro 7 and Final Cut Pro X XML formats.

About Supported Alpha Channels

Media with embedded alpha channels is supported for any project as long as it’s in a media format that

DaVinci Resolve supports; this includes TIFF, OpenEXR image sequence formats, and four-channel

QuickTime formats such as ProRes 4444, DNxHR 444, and QuickTime Animation. Alpha channels are

automatically enabled, and can be used for compositing directly within the DaVinci Resolve Timeline.

Alpha channels can be exported in round-trip workflows when rendering individual source clips.

However, when rendering a program as a single clip, all composited effects are rendered together to

produce a single output media file.

For more information on rendering clips with alpha channels, see Chapter 185, “Delivery

Effects Processing.”


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT

About Imported Text Effects

DaVinci Resolve supports the import of text generators when importing XML project files from both

Final Cut Pro X and Final Cut Pro 7. All imported text effects appear in the DaVinci Resolve Timeline as

Basic text generators. Some, but not all, formatting parameters are imported, depending on the project

file format being imported.

About Imported Audio in AAF Projects

Any combination of audio track types, channel map order, MXF and QuickTime files, and rendered or

unrendered clips should import without problems.

NOTE: When exporting an AAF project, DaVinci Resolve is capable of writing mono media in

stereo tracks.

Preparing Unsupported Clips and Effects You Want to Grade

If there is an unsupported effect within your NLE of choice that you want to move into DaVinci Resolve

for grading (for example, clips with effects filters that are native to a particular NLE), here’s a simple

workflow to follow.

To “bake” an effect into a clip you’re sending to DaVinci Resolve:


Export that clip as a self-contained media file using whatever DaVinci Resolve-compatible

mastering codec you prefer.


Reimport the resulting media file into your project.


Edit it into your project’s timeline to replace the original effects clip.


Export a version of the resulting sequence for use in DaVinci Resolve.

This is a good way of prepping the titles and effects of projects that you want to finish in DaVinci

Resolve. If you create self-contained media files for all title clips and effects, then these elements

will import cleanly and easily, and you can export a complete, texted version of your program out of

DaVinci Resolve.

Additionally, if a composited clip is using unsupported effects (for example, a filtered still image with

animated position that’s superimposed using the Overlay composite mode and set to 70% opacity),

an ideal way to prep this clip for XML export to DaVinci Resolve is to set the composite mode to

Normal, set Opacity to 100%, and then export the resulting clip as a self-contained QuickTime movie.

Reimport the result, edit it back into the Timeline to replace the original superimposed clip, and then

set its composite mode to Overlay and its Opacity to 70% to match the original settings. Now the

unsupported effects are “baked” into the clip, but the effects that DaVinci Resolve does support are

still live, and can be readjusted in context while grading.


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT

Verifying Imported Timelines

Using Offline References

DaVinci Resolve has a specific interface for comparing two versions of a program. This eliminates the

need to edit a rendered version of a timeline as a superimposed clip within your timeline and provides

many other features to aid this comparison without cluttering your timeline.

By setting the Source Viewer in the Edit page to Offline mode, you can compare an Offline Reference

Clip or Timeline to a currently open timeline, with both playheads ganged together, either side by

side, or as a split screen, a box wipe, or difference operation, all of which will be visible via your video

output device. As you play the Timeline, the Offline Reference Clip or timeline plays as well, making it

easy to spot differences between the two.

IMPORTANT: You need to make sure that the media you’ve imported or are using as an

Offline Reference Clip has a valid timecode track with a start time that matches the timecode

of the Timeline you’re comparing to, otherwise there will be an offset between the Timeline

and offline reference that will make a comparison difficult to impossible. Small offsets can be

corrected via an offset field in the Source Viewer while in offline mode, but large offsets will

be impractical to correct.

Why Set Up An Offline Comparison?

However you set up an offline reference, this is a convenient way of comparing two versions of a

program. There are several reasons for comparing an Offline Reference Clip to a timeline:

�Verifying the clip order: If you’re unsure whether or not you’ve properly resolved reel conflicts or

other problems that occurred while you were conforming a timeline, you can compare each edit

to the offline version of the program to spot problems and identify the proper media that should

correspond to any clip.

�Recreating effects: If there are offline effects, such as temporary grades made in the NLE, or pan

and scan transforms that you want to check, the Offline reference mode lets you split-screen your

current grade against the Offline Reference Clip in the Color page.

�Comparing two versions of a timeline: You can make a visual comparison a timeline with another

version of that timeline to spot differences for evaluation.

�Filling holes in timelines with missing or unlinked clips:  Two options found in the Preferences

> User > Editing > General settings, “Show offline clips through conform gaps,” and “Show offline

clips through missing clips,” let you set DaVinci Resolve to display Offline Reference Clip media to

fill gaps in the Timeline or replace the contents of unlinked clips. This is typically done to resolve

emergency situations when you need to proceed with a screening or review session despite the

fact that you’re missing media for whatever reason.

For more information, see Chapter 4, “System and User Preferences.”

NOTE: Typically, the flattened version of the program you’re given uses a low-quality codec,

and contains effects and color correction that’s not final, which is why it’s called an Offline

Reference Clip.


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT

Assigning a Clip or Timeline for Offline Comparison

There are two ways you can assign an Offline Reference Clip or Timeline to a particular timeline for

comparison. The easiest and most flexible way is to open a timeline, and then drag and drop a clip or

timeline with matching timecode that you want to compare to from the Media Pool onto the Source

Viewer in Offline mode.

To assign any clip or timeline to a specific timeline for comparison:


Open the timeline you want to make the assignment to in the Edit page.


Set the Source Viewer to Offline mode.


Drag a clip or timeline with matching timecode that you want to assign onto the Source Viewer.

The clip or timeline you dragged is immediately assigned to the open timeline as an Offline

Reference Clip, and synced via timecode.


In the Media Pool, right-click the Timeline you want to review against the Offline Reference

Clip, and choose the reference clip or timeline you assigned from the Timelines > Link Offline

Reference Clip submenu of that timeline’s contextual menu.

You can also add a clip to the Media Pool specifically as an Offline Reference Clip, making it easy

to associate such a clip with a particular timeline by right-clicking that timeline in the Media Pool

and choosing it from the Link Offline Video submenu. The idea is that if you or your client exports

a flattened version of their edited sequence at the same time as they export the EDL, AAF, or XML

project file they want graded, then you can compare the project data that’s imported into DaVinci

Resolve to the actual video of the offline edit.

To assign an imported Offline Reference Clip to a specific timeline for comparison:


Open the Media page, and use the Media Storage browser to find the flattened Offline Reference

Clip that you want to use for comparison.


Right-click the Offline Reference Clip file and choose Add as Offline Reference Clip.


That clip appears with a small checkerboard badge in its icon in the Media Pool.

Checkerboard indicating an offline video


Open the Edit page, right-click the timeline you want to review against the Offline Reference

Clip, and choose the offline clip you imported from the Timelines > Link Offline Reference

Clip submenu.


Import and Conform Projects | Chapter 55 Preparing Timelines for Import and Comparison

EDIT

Selecting the offline video to link to the current Timeline.