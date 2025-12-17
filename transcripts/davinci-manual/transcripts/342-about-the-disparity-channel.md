---
title: "About the Disparity Channel"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 342
---

# About the Disparity Channel

The Disparity channel stores the displacement vectors that match pixels in one eye to the other

eye. The left image’s Disparity channel will contain vectors that map left>right and the right image’s

Disparity channel will contain vectors that map right>left. For example:

(xleft, yleft) + (Dleft. x, Dleft. y) -> (xright, yright) (xright, yright) +

(Dright. x, Dright. y) -> (xleft, yleft)

You would expect for non-occluded pixels that Dleft = -Dright, although, due to the disparity

generation algorithm, this is only an approximate equality.

NOTE: Disparity stores both X and Y values because rarely are left/right images perfectly

registered in Y, even when taken through a carefully set up camera rig.

Both Disparity and Optical Flow values are stored as un-normalized pixel shifts. In particular, note

that this breaks from Fusion’s resolution-independent convention. After much consideration, this

convention was chosen so the user wouldn’t have to worry about rescaling the Disparity/Flow values

when cropping an image or working out scale factors when importing/exporting these channels to

other applications. Because the Flow and Disparity channels store things in pixel shifts, this can cause

problems with Proxy and AutoProxy. Fusion follows the convention that, for proxied images, these

channels store unscaled pixel shifts valid for the full-sized image. So if you wish to access the Disparity

values in a script or via a probe, you need to remember to always scale them by (image. Width/image.

OriginalWidth, image. Height/ image. OriginalHeight).

Viewing of Disparity and Vector Channels

Aux channels can be displayed directly in the viewers through the Channel viewer button’s menu.

The CopyAux node is used to copy those channels directly into the RGB channels for viewing or

further processing. The advantage of using the CopyAux node is that it does static normalization,

which reduces a lot of flicker that the viewer’s time-variant normalization causes. When viewing long

sequences of aux channels, the CopyAux node has the option to kill off aux channels and keep only

the current RGB channels, freeing up valuable memory so you can cache more frames.

TIP: Although you can use the Channel Booleans to copy any aux channel into RGBA, it

involves a few additional clicks when compared to CopyAux.

One thing to be aware of is that aux channels tend to consume a lot of memory. A float-32 1080p

image containing just RGBA uses about 32 MB of memory, but with all the aux channels enabled it

consumes around 200 MB of memory.


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

Stereo and Optical Flow Best Practices

How you create your composition, the images you are using, and the type of shot you are working on

can all have an impact on the success of the Disparity generation and Optical Flow analysis. Below,

we’ll look at some of the situations to be aware of and how you can avoid some pitfalls when dealing

with optical flow.

Semi-Transparent Objects

The Optical Flow and Disparity generation algorithms Fusion uses assume there is only one layer per

pixel when tracking pixels from frame to frame. In particular, transparent objects and motion blur will

cause problems. For example, a shot flying through the clouds with the semi-transparent clouds in the

foreground and a distant landscape background will confuse the Optical Flow/Stereo algorithms, as

they do not recognize overlapping objects with different motions. Usually the optical flow will end up

tracking regions of one object or the other. If the transparent object and the background are near the

same depth and consequently have the same disparity, then it is not a problem.

Motion Blur

Motion blur is also a serious problem for the reason explained in the previous point. The Disparity and

Optical Flow algorithms are unsure whether to assign a pixel in the motion blur to the moving object

or the background pixel. Because the algorithms used are global in nature, not only the vectors on the

motion blur will be wrong, but it will confuse the algorithm on regions close to the motion blur.

Depth of Field

Depth of field is also another problem related to the above two problems. The problem occurs when

you have a defocused foreground object over a background object that is moving (Optical Flow case)

or shifts between L/R (Stereo Disparity case). The blurred edges will confuse the tracking because

they can’t figure out that the edges are actually two separate objects.

Where to Calculate Disparity and Optical Flow?

Where you choose to generate optical flow or disparity in your composition can drastically affect

the results.

For example, if you have composited a lens flare in, it is better to compute OpticalFlow/

Disparity before that, since the semi-transparent lens flare will confuse the tracking algorithms.

If you are color correcting the left/right eyes to match or for deflickering, it is better to apply

the OpticalFlow/Disparity afterward, since it will be easier for the tracking algorithm to find

matches if the color matches between frames.

If you are removing lens distortion, think carefully about whether you want to do it before

or after Disparity computation. If you do it after, your Disparity map will also act as a lens

distortion map, combining the two effects as one.

As a general rule of thumb, it is best to use OpticalFlow/Disparity before any compositing

operations except an initial color matching correction and a lens distortion removal.


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

Cropping the Source

As a general tip, if you are cropping down your input images for any reason, it is probably better to

compute the optical flow or disparity before the crop and then afterward crop the flow/disparity along

with the color.

The reason is that flow/disparity matching works well when there is common pixel data to match in

both frames, but when there are pixels that show up in just one frame (or one eye), then the Disparity/

OpticalFlow nodes must make a guess and fill in the data. The biggest occlusions going from L <–> R

are usually pixels along the L/R edges of the images that get moved outside. This is similar for optical

flow when you have a moving camera.

Another thing to be aware of are black borders around the edges of your frames, which you should

crop away.

Nodes with Multiple Outputs

Many of the stereo nodes in the Fusion toolset have multiple outputs. This can cause some confusion

to new users. One particularly confusing thing is that when you drag a Stereo node to the view, it will

always display the left output. There is no way to view the right output without connecting another

node like BC (BrightnessContrast) to the right output and viewing that.

Picking from Aux Channels

Some nodes, like StereoAlign, allow one to drag pick from the Z or Disparity auxiliary channels. You

must pick from a node upstream of the StereoAlign, not from the output of the StereoAlign. If you try

to pick a disparity from the output of a StereoAlign node, you will get nothing because StereoAlign

consumes/destroys the Disparity aux channel (and even if it did not destroy the Disparity channel, you

would still be picking the wrong value since you would be picking from the aligned result).

The typical workflow for picking is:


View StereoAlign in the left view.


View the node upstream of StereoAlign in the right view.


Pick the Disparity value from the left eye in the right view.

Although this picking functionality does not operate any differently from normal picking of color

channels, this issue may cause some confusion. If it helps, the analogous workflow mistake with color

nodes would be a user trying to pick a gradient color for a Background node from a view showing the

Background node itself (you are trying to pick a color for a node from its own output).

Another issue that you need to be aware of is which eye you are picking. To avoid problems, it’s a

good idea to always pick from the left eye. The reason is that the Disparity channels for the left and

right eyes are different, and when you pick from a horizontal/vertical stereo stack, Fusion has no way

of knowing whether you picked the Disparity value from the left or right eye.

The above are not hard and fast rules; rather, they are guidelines to prevent foot shootings. If you

understood the above reasoning fully, you’ll realize there are exceptions, like picking disparity from the

left output of DisparityToZ and Z from the left/right output of ZToDisparity, where everything is okay.

Vector and Disparity Channels

The Vector and BackVector channels store the forward and reverse optical flow.

The Vector channel might be better named “forward vector” or “forward flow,” since the name

“Vector” to describe a channel is “not technically correct,” as the more mathematically-inclined user

might recognize that all the channels except the scalar channels Z/ID are technically “vector” channels.


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

A frames Vector aux channel will store the flow forward from the current frame to the next frame in the

sequence, and the BackVector aux channel will store the flow backward from the current frame to the

previous frame. If either the previous or next frames do not exist (either not on disk or the global range

of a Loader does not allow OpticalFlow to access them), Fusion will fill the corresponding channels

with zeros (transparent black).

The Disparity channel stores the displacement vectors that match pixels in one eye to the other

eye. The left image’s Disparity channel will contain vectors that map left > right and the right image’s

Disparity channel will contain vectors that map right > left.

For example:

(xleft, yleft) + (Dleft. x, Dleft. y) -> (xright, yright) (xright, yright) +

(Dright. x, Dright. y) -> (xleft, yleft)

You would expect for non-occluded pixels that Dleft = -Dright, although due to the disparity generation

algorithm, this is only an approximate equality. Note that Disparity stores both X and Y values because

rarely are left/right images perfectly registered in Y, even when taken through a carefully set up

camera rig.

Disparity and Optical Flow values are stored as un-normalized pixel shifts. In particular, note that this

breaks from Fusion’s resolution-independent convention. After much consideration, this convention

was chosen so the user wouldn’t have to worry about rescaling the Disparity/Flow values when

cropping an image or working out scale factors when importing/exporting these channels to other

applications. Because the Flow and Disparity channels store things in pixel shifts, this can cause

problems with Proxy and AutoProxy. The convention that Fusion follows is that, for proxied images,

these channels store unscaled pixel shifts valid for the full-sized image. So if you wish to access the

disparity values in a script or via a probe, you need to remember to always scale them by (image.

Width/image. OriginalWidth, image. Height/image. OriginalHeight).

When using Vector and BackVector aux channels, remember that all nodes expect these aux channels

to be filled with the flow between sequential frames.

More precisely, if you have sequence of three frames A, B, C, then:

B

Vector will contain the flow B>C

B

BackVector will contain the flow B>A

A

Vector will contain the flow A>B

A

BackVector is written with zeros as there is no frame before A

C

Vector is written with zeros as there is no frame D to flow C>D

C

BackVector will contain the flow C>B

When working with these channels, it is the user’s responsibility to follow these rules (or for clever

users to abandon them). Nodes like TimeStretcher will not function correctly since they still expect the

channels to contain flow forward/back by 1 frame.

NOTE: Currently DoD/RoI is not supported for all Fusion nodes.


Fusion Fundamentals | Chapter 88 Optical Flow and Stereoscopic Nodes

FUSION

FUSION

Fusion Page

Effects

CONTENTS


3D Nodes���������������������������������������������� 1867

90	 3D Light Nodes���������������������������������� 1985


3D Material Nodes��������������������������� 2004


3D Texture Nodes���������������������������� 2033


Blur Nodes������������������������������������������� 2058


Color Nodes���������������������������������������� 2083


Composite Nodes������������������������������ 2158

96	 Deep Image Nodes��������������������������� 2178


Deep Pixel Nodes������������������������������ 2197


Effect Nodes���������������������������������������� 2213


Film Nodes������������������������������������������ 2250

100	 Filter Nodes���������������������������������������� 2269

101	 Flow Nodes����������������������������������������� 2286

102	 Flow Organizational Nodes���������� 2289

103	 Fuses����������������������������������������������������� 2294

104	 Generator Nodes������������������������������ 2296

105	 I/O Nodes��������������������������������������������� 2336

106	 Layer Nodes��������������������������������������� 2363

107	 LUT Nodes�������������������������������������������� 2377

108	 Mask Nodes���������������������������������������� 2386

109	 Matte Nodes���������������������������������������� 2427

110	 Metadata Nodes������������������������������� 2498


Miscellaneous Nodes��������������������� 2506

112	 Optical Flow���������������������������������������� 2545

113	 Paint Node������������������������������������������� 2565

114	 Particle Nodes����������������������������������� 2575

115	 Position Nodes���������������������������������� 2635

116	 Resolve Connect������������������������������ 2654


Shape Nodes�������������������������������������� 2660

118	 Stereo Nodes������������������������������������� 2700

119	 Tracking Nodes��������������������������������� 2732

120	 Transform Nodes������������������������������ 2788

121	 USD Nodes������������������������������������������ 2816

122	 VR Nodes��������������������������������������������� 2869

123	 Warp Nodes���������������������������������������� 2880

124	 Modifiers����������������������������������������������� 2910