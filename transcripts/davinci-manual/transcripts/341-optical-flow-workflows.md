---
title: "Optical Flow Workflows"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 341
---

# Optical Flow Workflows

The Optical Flow analysis is a non real-time process, and depending on your computer, the clip’s

resolution, and the duration of the clip, it can take some time. Because of this, the general idea is that

you pre-generate the motion vectors, either by performing the analysis overnight or using a render

farm, and save results into an OpenEXR sequence. The Optical Flow toolset is designed around four

types of nodes that either generate, destroy, pass through, or construct the motion vectors.

OpticalFlow

The Optical Flow node generates the Vector and BackVector data. Typically, for optimal performance,

you connect the Optical Flow output to a Saver to save the image as OpenEXR files with the motion

vectors stored in an aux channel.


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

TimeSpeed, TimeStretcher

You can create smooth constant or variable slow-motion effects using the TimeSpeed or

TimeStretcher nodes. When Optical Flow motion vectors are available in the aux channel of an image,

enabling Flow mode in the TimeSpeed or TimeStretcher Interpolation settings will take advantage of

the Vector and BackVector channels. For the Flow mode to work, there must be either an upstream

OpticalFlow node generating the hidden channels or an OpenEXR Loader bringing these channels

in. These nodes use the Vector/BackVector data to do interpolation on the motion channel and then

destroy the data on output since the input Vector/BackVector channels are invalid.

For more detail on TimeSpeed or TimeStretcher, see Chapter 111, “Miscellaneous Nodes,” in

the DaVinci Resolve Reference Manual and Chapter 51 in the Fusion Reference Manual.

SmoothMotion

SmoothMotion can be used to smooth the Vector and BackVector channels or smooth the disparity

in a stereo 3D clip. This node passes through, modifies, or generates new aux channels, but does not

destroy them.

Repair Frame, Tween

The Tween and Repair Frame nodes are different from standard optical flow nodes because they have

the OpticalFlow analysis and motion vector generation built in. Tween will compare two frames and

create an in-between frame, which is good for recreating a missing or flawed frame. Repair Frame

will look at frames on either side of the current frame and repair scratches, dust marks, and so on.

Because these nodes work with flow values between non-sequential frames, they cannot use the

optical flow stored in the input image’s Vector/BackVector channels, but rather must regenerate the

flow of each frame, do their processing, and then destroy the flow channels. This being the case, these

nodes are computationally expensive.

For more detail on Tween or Repair Frame, see Chapter 112, “Optical Flow,” in the DaVinci

Resolve Reference Manual or Chapter 52 in the Fusion Reference Manual.

Advanced Optical Flow Processing

The Optical Flow, Repair Frame, and Tween nodes include a faster GPU-based Optical Flow algorithm.

When you add the Optical Flow, Repair Frame, or Tween node to a comp, the Inspector includes a

Method drop-down menu where you can choose Advanced to enable the GPU-based algorithm. This

Advanced method is the same Optical Flow algorithm used in other DaVinci Resolve pages.

By choosing Classic from the Method drop-down menu in the Inspector, you can use the older CPU-

based algorithm to maintain compatibility with comps created in previous versions. This method may

also be better suited for some Stereo3D processing.


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

Stereoscopic Workflows

Disparity is the difference between the left and right image. The Disparity map is used by nodes to

align and massage the stereo pair of images.

The Disparity node analyzes a stereo pair of images and generates an X&Y disparity map.

The workflow is to load a left and right stereo image pair and process those in the Disparity node.

Once the Disparity map is generated, other nodes can process the images.

TIP: When connectng stereo pairs in the node tree, make sure that the left and right images

are connected to the left and right inputs of the Disparity node.

Disparity generation, like Optical Flow, is computationally expensive, so the general idea is that

you can pre-generate these channels, either overnight or on a render farm, and save them into an

EXR sequence.

The toolset is designed around this philosophy.

Stereo Camera

There are two ways to set up a stereoscopic camera. The common way is to simply add a Camera 3D

and adjust the eye separation and convergence distance parameters.

The other way is to connect another camera to the RightStereoCamera input port of the Camera 3D.

When viewing the scene through the original camera or rendering, the connected camera is used for

creating the right-eye content.


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

Stereoscopic cameras can be done with a

single camera or two connected cameras.

Stereo Materials

Using the Stereo Mix material node, it is possible to assign different textures per eye.

Material viewer showing stereoscopic material.

Disparity

The Disparity node does the heavy lifting of generating disparity maps. This generates the Disparity

channel and stores it in the hidden aux channels of their output image.

NewEye, StereoAlign

NewEye and StereoAlign use and destroy the Disparity channel to do interpolation on the

color channel.

The hidden channels are destroyed in the process because, after the nodes have been applied, the

original Disparity channels would be invalid.

For these nodes to work, there must be either an upstream Disparity node generating the hidden

channels or an OpenEXR Loader bringing these channels in.


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

DisparityToZ, ZToDisparity

These nodes pass through, modify, or generate new aux channels, but do not destroy any.

TIP: If the colors between shots are different, use Color Corrector or Color Curves to do a

global alignment first before calculating the Disparity map. Feed the image you will change

into the orange input and the reference into the green input. In the Histogram section of the

Color Corrector, select Match, and also select Snapshot Match Time. In the Color Curves’

Reference section, select Match Reference.

Separate vs. Stack

Stereo nodes can work in Separate or Stack modes. When in Stack mode, the left/right eyes are

stacked horizontally or vertically, forming one image with double width or height, respectively.

The advantage to using Stack mode is that you do not have to have duplicate branches of the Node

Editor for the left and right eyes. As a consequence, you will see Stereo nodes with two inputs and two

outputs labeled as “Left” and “Right.”

When in Stack mode, the stack should be connected to the left eye input and the Left output should

be used for connecting further nodes. In Stack mode, the respective Right eye inputs and outputs

are hidden.

Setting Up Stereo in the Node Editor

The disparity generation is the first operation. This can be configured in the Node Editor in two

different ways.

Two stereoscopic workflows.

In the above example, the workflow on the right takes the left and right eye, generates the disparity,

and then NewEye is used to generate a new eye for the image right away.

The example on the left renders the frames with disparity to intermediate EXR images. These images

are then loaded back into Stereo nodes and used to create the NewEye images.

By using Render nodes to compute the disparity first, the later processing of the creative operations

can be a much faster and interactive experience.


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

Although not shown in the above diagram, it is usually a good idea to color correct the right eye to be

similar to the left eye before disparity generation, as this helps with the disparity-tracking algorithm.

The color matching does not need to be perfect—for example, it can be accomplished using the

“Match” option in a Color Corrector’s histogram options.