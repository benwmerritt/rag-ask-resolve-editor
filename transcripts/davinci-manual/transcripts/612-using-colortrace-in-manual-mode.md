---
title: "Using ColorTrace in Manual Mode"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 612
---

# Using ColorTrace in Manual Mode

Manual mode is ideal for situations where you want to copy grades between programs with clips that

have no timecode or reel name correspondence at all. The Manual ColorTrace interface is designed

to let you move through two different timelines, either a clip at a time, or in matching multiples of clips,

copying grades from the Source timeline to the Target timeline.

For example, if you’re trying to copy grades from a timeline that was conformed from individual media

files, to another timeline that was conformed from a flattened master media file, you can use the

ColorTrace Manual mode to accomplish this.

The manual interface consists of two sets of controls that correspond to the Source timeline (labeled

“Timeline to copy from”), and the Target timeline (labeled “Timeline to paste to”). The general idea is

that you move through both sets of timelines one clip at a time, or in matching multiples of clips at a

time, and copy grades from the “Copy from” timeline to the “Paste to” timeline.


Color | Chapter 149 Copying and Importing Grades Using ColorTrace

COLOR

ColorTrace Manual window

Manual mode has the following controls:

�Source timeline: Shows all clips in the Source timeline you selected; the clips you’re copying

grades from. Click any one clip thumbnail to select it, or click a thumbnail, and then Shift-click

another thumbnail to select a contiguous range of clips. You cannot select a noncontiguous

range of clips.

�Copy Range controls: Two fields show the range of clips in the current selection that you’ll be

copying from, referred to by their numeric position in the Source timeline. You can change the

range numerically by either entering new numbers in the fields, or by using the up/down arrow

buttons to alter the value by one. The First button automatically adds all clips from the first one in

the Timeline into the current selection. The Last button automatically adds every clip going to the

last one in the Timeline to the current selection.

�Target timeline: Shows all clips in the Target timeline you selected; the clips you’re pasting grades

to. Selecting clips works identically as with the Source timeline.

�Paste Range controls: Two fields show the range of clips in the current selection that you’ll be

pasting to, referred to by their numeric position in the Source timeline. All controls work identically

to the Copy Range controls.

�Attributes and options checkboxes: Turn off the checkboxes of any clip characteristics that you

don’t want to copy as part of the ColorTrace operation. A more complete description of these

options appears in the section on the Automatic ColorTrace mode.

�Paste button: Once you’ve selected one or more source clips and a matching number of

target clips, clicking Paste copies the grades, PTZR settings, and marks (depending on the

corresponding checkboxes).

�Undo Last: Lets you undo the most recent paste action.

�Undo All: Lets you undo all paste actions in Manual mode.

�Done: Finishes the operation and closes the ColorTrace window.

If you’re cherry picking individual grades from one timeline to paste into shots in another, you can copy

grades one at a time.

To copy one source grade to one target clip:

�Click a thumbnail in the Source timeline (on top) to copy from, then click a thumbnail in the Target

timeline (on the bottom), and click Paste.

You can also simultaneously copy the grades of entire scenes of clips from one timeline to another.

For example, if you’re copying grades from an originally graded timeline to a re-edited version of the

same program, you can copy every grade from a 10-clip scene in the Source timeline to the same 10

clips in the Target timeline which have been pushed back later in the Timeline.


Color | Chapter 149 Copying and Importing Grades Using ColorTrace

COLOR

To copy a group of source grades to a group of target clips:


Choose a continuous range of source clips by doing one of the following:

�Click the first clip in the range, and then Shift-click the last clip in the range.

�Enter the clip number of the first clip in the left “Copy Range” field, and then enter the clip

number of the last clip in the right field.

�Click a clip, and then click First to select every clip from that one to the first clip in the Timeline.

�Click a clip, and then click Last to select every clip from that one to the last clip in the Timeline.


Choose a continuous range of Target clips by using the same procedures as in the previous step,

but using the “Paste Range” controls.

IMPORTANT: You must select the same number of target clips as you did source clips for

the Paste button to become enabled.

Group copy and paste of grades


When you’ve made your selections, click Paste.

The grade settings from the source clips are pasted to the destination clips, in order. In other

words, if you copy from clips 5 through 9 to clips 11 through 15, then grade 5 is copied to shot 11,

grade 6 is copied to shot 12, grade 7 is copied to shot 13, and so on.

Importing CDL Data Using ColorTrace

The ColorTrace CDL command lets you import ASC CDL file formats from other applications into

DaVinci Resolve. DaVinci Resolve also has the ability to read DRX filenames from CDL files, allowing a

CDL to load exported DaVinci Resolve grades.

There are three supported file formats:

CMX EDL: An EDL with comments referring to CCC/CDL XML files, or even Slope, Offset, and

Power (SOP) data within the comment area.

CCC and CDL XML: A file format that contains various color correction looks, and

even references.


Color | Chapter 149 Copying and Importing Grades Using ColorTrace

COLOR

To import CDL data into DaVinci Resolve:


If you’re importing CCC/CDL XML correction looks:

�Open the Gallery page, right-click anywhere within the Stills tab, and choose Import from the

contextual menu.

�When the Import Stills dialog appears, open the CDL/CCC files. When these are finished

importing into the Gallery, an ASC logo will appear along with them.


Open the Edit page and select the Timeline you want to use ColorTrace with in the Timeline list.


Right-click anywhere within the Timeline, and choose ColorTrace from CDL.


Select an EDL using the Select EDL dialog, and click Open.


Select its corresponding CDL and CCC files using the Select CDL Files dialog. If there are no

CDL or CCC files (which is the case if there are inline SOP comments within the EDL), you should

click Cancel.


Using the ColorTrace With CDL window, copy the source grades from the CMX EDL/CCC & CDL

XML files to the Target timeline.

At this point, the ColorTrace window works identically as previously described.

For formatting reference, here are some examples of CMX, CCC, and CDL files.

Example CMX EDL File

TITLE: Final EDL FCM: NON-DROP FRAME 010 001 V C 01:19:28:16 01:19:28:16

01:00:41:18 01:00:42:18 *ASC_CC_XML test_cc.102 011 001 V C 00:00:00:00

01:19:28:16 01:00:42:18 01:00:43:18 *ASC_SOP (0.9 1.2 0.5)(0.4 -0.5 0.6)

(1.0 0.8 1.5)

Example CCC File

<ColorCorrectionCollection xmlns:”urn:ASC:CDL:v0.5” >

<InputDescription> test corrections for ref_input_image.1920

</InputDescription> <ViewingDescription>

for mathematical analysis only </ViewingDescription>

<ColorCorrection id=”test_cc.100”> <SOPNode>

<Description> for ref_output_image.0100 </Description> <Slope> 1.0 1.0 1.0

</Slope> <Offset> 0.0 0.0 0.0 </Offset> <Power> 1.0 1.0 1.0 </Power>

</SOPNode> </ColorCorrection>

<ColorCorrection id=”test_cc.101”> <SOPNode>

<Description> for ref_output_image.0101 </Description> <Slope> 1.0 1.5 0.6

</Slope> <Offset> 0.0 -0.1 0.01 </Offset> <Power> 1.0 1.5 0.5 </Power>

</SOPNode> </ColorCorrection>

</ColorCorrectionCollection>

Example CDL File

<ColorDecisionList xmlns=<94>urn:ASC:CDL:v0.5<94> >

<InputDescription> GeneralProducts M1 std thru GP M1 LUT4 </

InputDescription> <ViewingDescription> GP P1, DCI P3, Pathe color emul </

ViewingDescription> <ColorDecision>

<MediaRef ref=<94>/some/Project/frame%250900-0954%5B.dpx<94>/>

<ColorCorrection id=”cc03340”>


Color | Chapter 149 Copying and Importing Grades Using ColorTrace

COLOR

<SOPNode> <Description>change +1 red, contrast boost</Description>

<Slope>1.2 1.3 1.4</Slope> <Offset>0.3 0.0 0.0</Offset> <Power>1.0 1.0

1.0</Power>

</SOPNode> </ColorCorrection>

</ColorDecision> </ColorDecisionList>

Using CDL Adjustments

Once you’ve imported a CDL (Color Decision List), then the CDL adjustment for each clip is made

available to you via a contextual menu command in the Thumbnail timeline of the Color page.

Calculating CDL Functions

To turn the SOP values into a primary correction, the following math is used by DaVinci Resolve:

Output = (Input * Slope + Offset)Power

Output refers to the final grade. Input is the value of each pixel within each color channel (on a

scale from 0–1). The detent value for Slope is 1. The detent value for Offset is 0. The detent value for

Power is 1.


Color | Chapter 149 Copying and Importing Grades Using ColorTrace

COLOR