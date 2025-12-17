---
title: "Scene Cut Detection on the Timeline"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 87
---

# Scene Cut Detection on the Timeline

(Studio Version Only)

If you need to break down a previously edited video into its component clips for re-editing or color

correction, you can now do so directly in an Edit or Cut page Timeline. Using the DaVinci Neural

Engine, DaVinci Resolve can automatically analyze and split up an edited video into individual clips.

If you prefer, you can continue to use the original Scene Cut Detection tool found in the Media Pool

and described later in this chapter.

To use Scene Cut Detection on the Timeline:


Put one or more clips you want to split on the Timeline. If you have clips on more than one video

track, you can selectively lock/unlock tracks or enable/disable the Auto Track Selectors to limit the

scene detection to specific video tracks. Additionally, you can limit Scene Cut Detection to just a

portion of a clip by setting In and Out points on the Timeline around the section you want to analyze.


Choose Timeline > Detect Scene Cuts.

A dialogue box appears, “Detecting scene cuts in clips x of x.” This process can take some time,

depending on the length, number, and complexity of the clips you’ve selected. When the Scene Cut

Detection has finished, the clip you selected will be broken up into a number of through edits that now

can be used as independent clips.

Checking and Fixing Your Results

If the Neural Engine has made an error, you can fix it manually by navigating to the cut using the Up

and Down Arrow keys to go back and forth in the Timeline, and by then doing one of the following:

�To remove a Cut: Click the through edit to select it, and press the “Delete” key.

�To make a New Cut: Place the timeline indicator at the cut point, and choose Timeline >

Split Clips (Command-\).

A single clip of a finished edit, consisting of multiple cuts before the Detect Scene Cuts command

Multiple individual clips extracted from the edited clip via Detect Scene Cut; the operation has been

contained by the In and Out points, and one of the resulting through edits has been highlighted in green.


Ingest and Organize Media | Chapter 23 Using Scene Detection

MEDIA

Scene Detection in the Media Page

You can still perform automatic scene detections using the original tools in the Media page. When

using the original Media page Scene Detection, it’s important to note that the analysis and splitting of

the selected clip is done in the Media Storage panel, before the clip is added to the Media Pool.

To open a clip into the Scene Detect window:


Open the Media page, and use the Media Storage browser to find and select the clip you need to

split apart. Do not add a clip you want to use scene detection on to the Media Pool first. You need

to use Scene Detection before the clip has been imported.


Right-click the file and choose Scene Cut Detection.


The Scene Detect window opens up, containing the clip you selected.


Press the Auto Scene Detect button in the lower left of the interface.

DaVinci Resolve scans through the selected scene and analyzes the media for possible cut points.

The Scene Detect Window Interface

The Scene Detect window is divided into three main areas, the viewers, the Graph, and the Cut List.

Together, these controls let you analyze the movie, examine the automatically found cuts, and manage

the Cut List in preparation for sending back to your project.

Scene Detect window

The Scene Detect Viewers

A set of three viewers appear at the top of the Scene Detect window, one main viewer and two smaller

picture-in-picture (PiP) viewers. These three viewers are designed to make it easy to test whether

the playhead in the Scene Detect Graph is on a cut point or not. The leftmost PiP viewer is the last

outgoing frame of a detected cut point. The main viewer shows the first incoming frame of that cut

point, and the rightmost PiP viewer shows the second incoming frame of that cut point.


Ingest and Organize Media | Chapter 23 Using Scene Detection

MEDIA

If the playhead in the Scene Detect Graph is directly on top of an edit point, the leftmost viewer

should show a completely different frame than the center and rightmost viewers, which should be very

similar to one another. If this is the case, you have found a correct cut point. This can be seen in the

following example.

The Scene Detect viewers show the last frame of the outgoing clip, and the first two frames of the incoming clip.

If the left viewer is significantly different than the main and right viewers, this indicates a correct cut point.

If all three viewers appear to display a continuous series of frames, then you’re not looking at a

cut point.

No scene cut here as all images are almost the same

Underneath the viewers are a series of controls.

The Scene Detect viewer transport controls

�Transport controls: A set of seven transport controls include first frame, step back, play reverse,

stop, play forward, step forward, and last frame.


Ingest and Organize Media | Chapter 23 Using Scene Detection

MEDIA

The In, Out, Prune, and Show Cut List controls

�In: Lets you set an In point, with which to define a range of the Scene Detection Graph to prune.

�Out: Lets you set an Out point, with which to define a range of the Scene Detection

Graph to prune.

�Prune: If you’ve identified a large number of false positive scene cuts (for example, a cluster of

cuts corresponding to a dissolve from one shot to another), use the In and Out buttons to surround

the undesirable range of scene cuts in the Scene Detect Graph, and then click Prune to eliminate

all scene cuts between these points that are within one frame of another scene cut. Within the

group of identified cuts, the highest probability cut will remain while the other cuts are deleted.

(Left) Isolating scene cuts to prune with In and Out points, (Right) The result of

clicking the Prune button to eliminate all unwanted scene cuts but one

�Show Cut List: Shows and hides the Cut List, which shows the currently detected scene cuts.

The Scene Detect Graph

The majority of the bottom half of the Scene Detect window, to the left, consists of the Scene Detect

Graph, which shows the scene detect analysis results after you’ve clicked the Start button.

Frames that DaVinci Resolve thinks are cut points appear as green vertical “scene cuts” of various

heights. The height of each scene cut corresponds to the likelihood that frame is really an edit point,

and not a swish pan, sudden jump in the motion of the frame, or abrupt change in color or lighting, all

of which can fool the scene detection algorithm.

A horizontal magenta confidence bar lets you choose the threshold of confidence required for

scene cuts to be added to the Cut List. If you drag this bar up above any shorter scene cuts of low

confidence, those lines turn gray and are omitted from the Cut List.


Ingest and Organize Media | Chapter 23 Using Scene Detection

MEDIA

Detection graph displays potential scene cuts

NOTE: Dissolves and other transitions are not automatically detected, although dissolves

most often appear as a triangular cluster of lines peaking in the middle.

Four controls appear underneath the graph.

�Auto Scene Detect: This initiates the scene cut detection process.

�Add: Lets you manually add a scene cut at the current position of the playhead. Sometimes two

adjacent clips with similar color and lighting will appear to be a single clip to the scene detection

algorithm. This lets you add scene cuts at frames where they weren’t initially found.

�Delete: Lets you manually delete a scene cut located at the position of the current frame indicator

within the graph.

�Zoom slider: Lets you zoom into and out of the Scene Detect Graph to see more or less detail as

you examine the results.

Cut List

At the lower right of the Scene Detect window, the Cut List displays one entry for each of the scene

cuts that intersect the confidence bar.

The Cut List shows all

currently detected cuts

Three columns show each cut’s order number, frame number, and timecode

value. You can select items in the Cut List to evaluate each cut using the

three viewers above. Whenever you select a new item in the Cut List, the

playhead jumps to that frame in the Scene Detect Graph.

To select items in the Cut List:

�Click any item in the Cut List.

�Press N (next) or the Down Arrow to select the next item down.

�Press P (previous) or the Up Arrow to select the next item previous.

As you move up and down the list, you can delete items that you can confirm

aren’t real cuts using the viewers above. If it’s a long list and you don’t have

time to check it all at once, it can be saved for later recall using commands

found in the Scene Detect Options drop-down menu.

Once you’re finished checking the list and are satisfied that each cut is

accurate, you can use it to split the media file into individual clips in the

Media Pool by clicking “Add Cuts to Media Pool,” located immediately below.


Ingest and Organize Media | Chapter 23 Using Scene Detection

MEDIA