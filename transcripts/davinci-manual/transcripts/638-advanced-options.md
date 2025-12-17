---
title: "Advanced Options"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 638
---

# Advanced Options

These controls tell the Depth Map how to handle various blanking issues.

�Blanking Regions: These controls tell the Depth Map how to handle letter and pillar boxing

regions in the effect.

Process Entire Frame: Tells the AI to ignore any information about the timeline shape and just

process all the visible pixels.

Handle Automatically (default): The AI will process only the area that DaVinci Resolve

knows your media is in.

Auto + Extra Crop: This is recommended for cropping away black bars; it uses DaVinci Resolve’s

knowledge of which pixels were occupied by your media but lets you crop out the framing or

letterboxing relative to its shape. This is recommended because it will stay consistent as you

adjust Timeline settings.

Manual Cropping: Simply lets you override whatever the framing of the content is, ignoring any of

DaVinci Resolve’s knowledge of the shape of your media.

For example, say you have footage shot of a person on a rainy day, but the background is too

distracting and contrasty. By creating a depth map that isolates only the foreground person,

we can then apply a Fast Noise smoke effect to only the background, making it look like a

foggy mist, and less distracting.

The original footage with a distracting background

The same footage with a Fast Noise Smoke effect node to simulate a fine mist,

however it covers the entire frame, including the main subject. The mist belongs in

the background only to be more realistic.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

By placing a node with Depth Map applied between the original nodes, you can use

the effect to pull a key based solely on “distance” from the camera. In this case, we

have selected the background (white) and excluded the woman with the umbrella

(black). Note the fine detail in the furry coat, which would be difficult to get with an

HSL or window qualifier.

The final result of the process shows the main subject in the foreground

with the Fast Noise smoke effect limited only to the background.

TIP: To create more believable Depth of Field adjustments, use the Depth Map effect in

conjunction with the Tilt-Shift Blur effect. You can feed the results of the Depth Map directly into

the Tilt-Shift Blur effect as a blur map by connecting the key output of the Depth Map node to

the key input of the Tilt-Shift Blur node and selecting “From Alpha In” in the Map Source drop-

down in the Depth of Field section of the effect. From there adjust the Focus Sweep to dial in the

area you want to isolate. If you’re not getting the expected results, try inverting the Depth Map.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

Face Refinement (Studio Version Only)

The Face Refinement effect has been improved with better tracking, profile handling, and smooth skin

options. The newly revised effect is described below.

Face Refinement is an incredibly sophisticated, yet easy-to-use, filter that lets you quickly make very

targeted adjustments to people’s complexions.

In order to use the face refinement toolset, the first thing you need to do is to identify the face (or

faces) you wish to work on, and then analyze and track that face through the clip.

Identifying a face is done by clicking on the Detect Faces in Frame button. If faces are present in the

frame at the position of the playhead, then this results in boxes being drawn over each detectable

face. Click any of these boxes to choose which face you want to refine, and that box will be highlighted

in green to indicate which face you’ll be refining.

When multiple faces are detected, you can click a

box to choose which one to work on.

After you’ve selected which face to work on, you need to use the tracking controls to track the face

through the clip, and an outline of the face’s major features appears to let you follow its progress.

The Face Refinement filter detecting a performer’s face


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

The basic tracking controls usually work well enough to track faces in most instances. However, in

some tricker cases if the subject’s head tilts away, or if it’s occluded by something else in the frame,

you may have to manually adjust the track. You can do this by going to the last known good point of

the track and then checking the Interpolate (Keyframed) box. This will add keyframes automatically

for the frame and turn the outlines blue to let you know you are in manual mode. Then you can go to

the problematic frames and click and drag to manually adjust the entire face or select and adjust each

individual feature as needed. Once you get to a point where the automatic tracking works again, you

simply uncheck the Interpolate box and let the automatic tracker take it from there.

Manually adjusting an eyebrow in

the Interpolate (Keyframed) mode

Once the face has been tracked, you’re ready to work. This plugin divides the tracked face into

different zones for common operations colorists often perform to quickly eliminate blemishes, adjust

the hue and saturation of complexions in regionally appropriate ways, modify lighting, sharpen

desirable detail, and refine makeup. Because all adjustments are fit to the proportions of the face

that’s been detected and tracked, all you need to do is make the adjustments you need and DaVinci

Resolve takes care of the rest.

Main Controls

The top controls let you initiate the Face Refinement process.

The tracking controls for Face Refinement

�Detect Faces in Frame: This button initiates the process of using the facial detection of the

Face Refinement plugin to detect the face you want to make adjustments for.

Tracking Controls: Basic tracking controls to identify facial features motion through the clip

Track Reverse: Identifies the face and tracks it backward through the clip.

Track Reverse 1 Frame: Identifies the face and tracks it backward 1 frame.

Find in Frame: Identifies the face in the current frame.

Track Forward then Reverse: Identifies the face then tracks it forward from

the current position and then reverse from that position.

Track Forward 1 Frame: Identifies the face and tracks it forward 1 frame.

Track Forward: Identifies the face and tracks it forward through the clip.

�Show overlay: To impress your clients and see how well Face Detection is tracking the face you’re

working on, you can turn on this checkbox, which turns on the wireframe tracking that shows you

which facial details are being detected.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR

Face Location

These controls let you adjust the strength of the effect, as well as make manual adjustments to the

face and its features position in the frame.

�Effect Strength: This slider determines the relative strength of the adjustments made with the

original image. 1.000 is full strength, while 0 turns the effect completely off.

�Interpolate (Keyframed): Checking this box lets you make manual adjustments to the face and

feature tracking in the Viewer, and automatically keyframes any changes. Click and drag in the

Viewer to move the entire face. Shift-click and drag to reframe the face. Click on any individual

feature to adjust, or any dot to move its position.

Skin Isolation

These controls let you adjust the skin mask this plugin automatically generates in order to limit the

effect to only the face of the person you’re targeting.

Adjusting the key with the face mask active

�Show mask: This checkbox makes the face mask being generated visible, which can be helpful to

see while you’re tuning it.

�Skin Mask Source: Lets you select the source for the skin mask. DaVinci Resolve’s Internal

Skin Model is the default, but there is the ability to use the Input Alpha if you’ve qualified the skin

tones in another node. None disables the mask.

�Shadow Range: This control lets you extend or erode the shadows of the face detected by

the skin model.

�Tint Range: This control lets you extend or erode the tint range detected by the skin model.

�Temp Range: This control lets you extend or erode the color temperature of the face detected by

the skin model.

�Limit to Face Region: Turning on this checkbox places a circular garbage mask that follows the

face to eliminate any accidental qualification of areas outside the face.

�Region Size: Lets you adjust the size of the face mask.

�Region Softness: Lets you adjust the edge softness of the face mask.

�Flat Skin Areas Only: Checking this box will exclude the nose and eye socket regions from the

mask, allowing you to work only on the facial skin itself.

�Exclude Mouth: Checking this box will exclude the mouth region from the mask, allowing you to

work only on the facial skin itself and not the lips.

�Denoise mask: This slider lets you fill in areas of small detail in the mask.

�Refine mask: This slider lets you adjust the face mask to smooth or eliminate gaps in the key.


Resolve FX Overview | Chapter 162 Resolve FX Refine

COLOR