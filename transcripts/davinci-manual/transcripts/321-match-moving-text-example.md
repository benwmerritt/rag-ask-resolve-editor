---
title: "Match Moving Text Example"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 321
---

# Match Moving Text Example

This example takes you through a complete motion tracking task, and shows how you can create a

very simple match-moving effect using the Tracker node, which is the Swiss army knife of trackers

in Fusion.

Adding a Layer to Match Move

In the example composition, we have a Text1 node that’s creating a “Switzerland” title that’s

composited over a drone shot flying over and around a mountain bridge. With the Text1 node selected,

the onscreen controls that let you position the text it’s generating are visible in the viewer, and the text

is positioned where we’d like it to start. Note that, with the Text node selected, even the part of the

text that’s offscreen can still be seen as an outline showing us where it is.

Some text superimposed against a background, ready to track

Our goal for this composition is to motion track the background image so that the text moves along

with the scene as the camera flies along.

Setting Up Motion Tracking

To set up for the motion track, we’ll begin by creating a disconnected Tracker node, using another

method other than those seen previously. Right-click anywhere in the background of the Node Editor

(preferably where you want the new node to appear), and choose Add Tool > Tracking > Tracker from

the contextual menu to create a new Tracker1 node underneath the MediaIn node (or Loader node if

you are using Fusion Studio).


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Creating a new node using the Node Editor contextual menu

Next, we’ll drag a connection from the MediaIn1 node to the Tracker1 node to automatically

connect the source clip to the Tracker1 background input. This branches the output from the

MediaIn1 node to the Tracker node so that the Tracker1 node processes the image separately

from the rest of the node tree. This is not required, but it’s a nice organizational way to see

that the Tracker node is doing an analysis that must be referred to in a way other than a

“physical” connection.

Branching a Tracker node to use to analyze an image


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

A Simple Tracking Workflow

The Tracker node is the simplest tracking operation the Fusion page has, and while there are several

ways of using it, an extremely common workflow is to use the Tracker node controls to analyze the

motion of a subject in the frame with motion you want to follow, and then use the resulting motion path

data by “connecting” it to the Center parameter of another node that’s capable of transforming the

image you want to match move.

Positioning the Tracker Onscreen Control

When the Tracker node is selected, a single green box appears in the viewer, which is the default

onscreen control for the first default tracker that node contains (seen in the Tracker List of the

Inspector controls). Keep in mind that you only see onscreen controls for nodes that are selected, so if

you don’t see the onscreen tracker controls, you know you need to select the tracker you want to work

with. Loading the tracker you want to work with into the viewer is also the safest way to make sure

you’re positioning the controls correctly relative to the actual image that you’re tracking.

If you position your pointer over this box, the entire onscreen control for that tracker appears, and if you

click the onscreen control to select that tracker, it turns red. As with so many other tracker interfaces

you’ve likely used, this consists of two boxes with various handles for moving and resizing them:

�The inner box is the “pattern box,” which identifies the “pattern” in the image you’re tracking and

want to follow the motion of. The pattern box has a tiny handle at its upper-left corner that you use

to drag the box to overlap whatever you want to track. You can also resize this box by dragging

any corner, or you can squish or stretch the box by dragging any edge to make the box better fit

the size of the pattern you’re trying to track. The center position of the tracker is indicated via X

and Y coordinates.

�The outer box is the “search box,” which identifies how much of the image the tracker needs to

analyze to follow the motion of the pattern. If you have a slow-moving image, then the default search

box size is probably fine. However, if you have a fast-moving image, you may need to resize the

search box (using the same kind of corner and side handles) to search a larger area, at the expense

of a longer analysis. The name of that tracker is shown at the bottom right of the search box.

The onscreen controls of a selected

tracker seen in isolation

It’s worth saying a second time that the handle for moving a tracker’s onscreen control is a tiny dot

at the upper-left corner of the inner pattern box. It’s really easy to miss if you’re new to Fusion. You

must click on this dot to drag the tracker around.

The handle for dragging the tracker

boxes to move them around


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

In this example, we’ll drag the onscreen control so the pattern box overlaps a section of the

bridge right over the leftmost support. As we drag the onscreen control, we see a zoomed-

in representation of the part of the image we’re dragging over to help us position the tracker

with greater precision. For this example, the default sizes of the pattern and search box are

fine as is.

The zoomed-in preview that helps you position the pattern box as you drag it

Using the Tracker’s Inspector Controls to Perform the Analysis

At this point, let’s look at the Tracker node’s controls in the Inspector. There are a lot of controls, but for

this simple example we only care about the main Tracker panel, with the tracking analysis buttons at

the top, the tracking options below those, and the Tracker List underneath those. The Tracker List also

has buttons for adding and deleting trackers; you have the option of adding multiple trackers that can

be analyzed all at once for different workflows, but we don’t need that for now.

Tracker Inspector controls, with the tracking

analysis buttons at top, the tracker options in

the middle, and the Tracker List below


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Additional controls over each tracker and the image channels being analyzed appear at the bottom,

along with offset controls for each tracker, but we don’t need those now (at least not yet).

Again, this track is so simple that we don’t need to change the default behaviors that much, but

because the drone is flying in a circular pattern, the shape of the pattern area is changing as the clip

plays. Fortunately, we can choose Every Frame from the Adaptive Mode menu to instruct the tracker to

update the pattern being matched at every frame of the analysis, to account for this.

Changing the Adaptive Mode of the Tracker node to Every

Frame to account for the camera’s shift of perspective

Now, we just need to use the tracker analysis buttons at the top to begin the analysis. These buttons

work like transport controls, letting you start and stop analysis as necessary to deal with problem

tracks in various ways. Keep in mind that the first and last buttons, Track from Last Frame and Track

from First Frame, always begin a track at the last or first frame of the composition, regardless of the

playhead’s current position, so make sure you’ve placed your tracker onscreen controls appropriately

at the last or first frame.

The analysis buttons, left to right: Track from Last Frame, Track

Backward, Stop Tracking, Track Forward, Track from First Frame

For now, clicking the Track from Beginning button will analyze the entire range of this clip, from the first

frame to the last. A dialog lets you know when the analysis is completed, and clicking the OK button

dismisses it so you can see the nice clean motion path that results.

The analyzed motion path resulting from tracking a

section of the bridge as the camera flies past


Fusion Fundamentals | Chapter 82 Using the Tracker Node

FUSION

Viewing Motion Track Data in the Spline Editor

This is not a necessary part of the tracking workflow, but if you have an otherwise nice track with a

few bumps in it, you can view the motion tracking data in the Spline Editor by viewing that tracker’s

Displacement parameter curve. This curve is editable, so you can massage your tracking data in a

variety of ways, if necessary.

Viewing motion tracking analysis data in the Spline Editor