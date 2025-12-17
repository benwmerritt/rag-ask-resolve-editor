---
title: "Duplicating Clips and"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 150
---

# Duplicating Clips and

Transitions in the Timeline

One or more clips can be duplicated by making a selection, and then Option-dragging the selected

clips to another position and/or track in the Timeline. When duplicating clips in this way, you must hold

the Option key down until you release the mouse button.

Individual selected transitions can also be duplicated by Option-dragging them to another edit point.

Smart Reframe (Studio Version Only)

The Smart Reframe feature in DaVinci Resolve makes it easier to quickly reframe material across

extreme aspect ratio changes. It’s useful for situations where you’ve shot a 16:9 horizontal video and

find yourself needing to create a vertically-oriented 9:16 version for mobile phones and social media

deliverables, or using 4:3 archival footage in a 2.39:1 widescreen movie. Smart Reframe can be used

manually, or automatically executed using the DaVinci Resolve Neural Engine.

Smart Reframe in action, with the Reference Point bounding box active (right)

The Smart Reframe tool is found in the Sizing tab of the Inspector and is available in both the

Cut and Edit pages.

To use the Smart Reframe tool:


Duplicate your timeline, right-click the Timeline and choose Timelines > Timeline Settings, and click

Use Custom Settings to change the Timeline Resolution to the aspect ratio needed for delivery.

Make sure that “Mismatched resolution files” is set to “Scale full frame with crop,” and click OK.


Select one or more clips you want to reframe, and open the Inspector to the Sizing tab.


Open the Smart Reframe controls, leave the Object of Interest drop-down menu set to Auto (if

you’ve selected more than one clip, Auto is the only setting available), and click “Reframe.” DaVinci

Resolve will analyze your footage and should automatically adjust each individual clip’s position to

a more aesthetically pleasing framing.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT


(Optional) If the “Auto” setting does not give you desirable results for a particular clip, you can

manually select the main subject using the following steps.

a)	 To manually select the subject area, choose “Reference Point” from the Object of Interest

drop-down menu, and click the target icon just to the right of the menu. This automatically sets

the Viewer mode to Smart Reframe, exposing the onscreen controls for choosing a reference.

b)	 Drag the Reference Point bounding box around the main subject of interest in the frame. You

may use the Transform controls directly above in the Inspector to move the source clip around

if your subject is outside the current framing.

c)	 Click “Reframe.”

The Inspector’s Smart Reframe controls showing

the manual reference point selected

DaVinci Resolve locks onto and, if necessary, tracks your subject using the reference you’ve

selected, automatically panning and scanning the original clip as needed to keep the reference

within the new aspect ratio. While involving a bit of manual adjustment, this function still

dramatically reduces the time involved in pan and scanning footage by manually adjusting and

keyframing the sizing controls.

Split Photoshop PSD Layers

into Individual Timeline Tracks

You can right-click on an Adobe Photoshop Document (.psd) in a timeline and select Split PSD Layers

in Place to expand each layer of the file into it’s own track. The number of new tracks created will

correspond with the number of layers in the file.

You can split Photoshop PSD layers into individual tracks by right-

clicking on them and selecting Split PSD Layers in Place.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

The results of splitting a PSD file.

DaVinci Resolve reads and splits rasterized flattened layers, so some steps need to be taken when

preparing the underlying PSD asset before import. Merging layers in Photoshop to create flattened

layers is generally a manual process. The intention is to simplify the image structure, bake Photoshop-

specific effects and rasterize fonts to ensure compatibility with DaVinci Resolve. Here is a breakdown

of the process:

Rasterize transparency and effects

If your layers/fonts contain effects like shadows or gradients, merging them can sometimes

alter their appearance. Consider rasterizing before merging. To do this, select one or

more layers, right-click and choose Rasterize Layer Style. This is recommended for text

layers as well.

Merge and flatten similar layers

Arrange similar layers together and select the layers you want to merge. Right-click on the

selected layers and choose Merge Layers (Cmd/Control+E) to combine the selected layers

into one ‘flat’ layer. Depending on the complexity of the Photoshop document, consider using

the option: File > Scripts > Flatten All Layer Effects.

Name layers

Rename the layers to describe the underlying image, effect or element. Naming the flattened

layers at this stage allows DaVinci Resolve to use the names in the split clips.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

Apple Cinematic Mode (Mac OS Only)

Recent models of Apple iPhone have a Cinematic mode that use lidar to emulate the depth of field

characteristics of a lens iris. You can use this mode to artificially create shallow depth of field looks

or to pull focus from one focal point to another. This functionality can be accessed directly in the Edit

Timeline of DaVinci Resolve.

Apple Cinematic mode with an F-Stop of 16; note the in focus background. The Yellow square denotes the focus point.

Apple Cinematic mode with an F-Stop of 2; note the blurred background. The Yellow square denotes the focus point.

Using Apple Cinematic Mode in DaVinci Resolve

Using Cinematic footage recorded on an iPhone takes some additional steps to bring into

DaVinci Resolve and is only available on the MacOS version.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT

To import iPhone Cinematic footage into DaVinci Resolve:


On your iPhone, the camera mode must be turned to Cinematic before you record the video.


Once the video is finished, find the video in the Photos app and press the Share icon.

IMPORTANT: In the Share interface, select “Export Unmodified Original.” Sharing any

other way (like AirDrop) will remove the cinematic information from your video.


Choose a location to save to on your phone in the Files interface.


From the Files interface, find the cinematic video, tap it, and then select the Share button again.


Now export the cinematic video via AirDrop or other method to your computer.


Open DaVinci Resolve and import the cinematic video into the Media Pool as normal.

Put the Viewer Overlay in Cinematic mode (circled) in the drop-down menu.

To use the Cinematic tools in DaVinci Resolve:


Put a Cinematic Video clip on the timeline and select it.


In the Viewer Overlay, select Cinematic from the drop-down menu.


In the Video Inspector, the Cinematic toolset should appear at the bottom of the list.


Choose a recorded focus point in the Viewer, designated by a yellow rectangle.


Use the F-Stop controls to adjust the depth of field.


Edit | Chapter 38 Modifying Clips in the Timeline

EDIT