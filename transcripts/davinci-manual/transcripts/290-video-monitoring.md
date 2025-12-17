---
title: "Video Monitoring"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 290
---

# Video Monitoring

This setting is only available in Fusion Studio. Control over video hardware for the Fusion Page is

done in the DaVinci Resolve preferences. The Video Monitoring preferences are used to configure

the settings of Blackmagic Design capture and playback products such as DeckLink PCIe cards and

UltraStudio i/O units.

The Video Monitoring preferences

Video Output

This group of drop-down menus allows you to select the type of video I/O device you have installed,

the output resolution, and the pixel format. These settings have nothing to do with your rendered

output; it is only for your display hardware.

The Output HDR over HDMI settings are used to output the necessary metadata when sending high

dynamic range signals over HMDI 2.0a and have it correctly decided by an HDR capable video display.

The Auto setting detects the image’s values and outputs HDR. This will not affect non HDR images.

The Always setting forces HDR on all the time. This can can be useful when checking non HDR and

HDR grades.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

When Auto or Always is selected, you can then set the “nit” level (slang for cd/m2) to whatever peak

luminance level your HDMI connected HDR display is capable of.

Stereo Mode

This group of settings configures the output hardware for displaying stereo 3D content.

�Mono will output a single non stereo eye.

�Auto will detect which method with which the stereo images are stacked.

�Use the Vstack option if the stereo images are stacked vertically as left on top and

right at the bottom.

�Use the Hstack option if the stereo images are stacked horizontally as left and right.

The Swap eyes checkbox will swap the eyes if stereo is reversed.

View

The View preferences are used to manage settings and default controls for viewers.

The View preferences


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Saved View Settings

The area at the top of the view preferences lists the currently saved settings that you create

from the viewer’s contextual menu. You can use the Rename and Delete buttons to manage the

selected entries in the list.

For more information on the viewer and its contextual menu, see Chapter 69, “Using

Viewers.” in the DaVinci Resolve Reference Manual or Chapter 7 in the Fusion

Reference Manual.

Settings for View

Each viewer has its own preferences. The Settings for View drop-down menu is used to select the

viewer you want to configure.

Control Colors

The Control Colors setting allows you to determine the color of the active/inactive onscreen controls.

Color Picking Area Size

You can use these width/height controls to set the number of pixels sampled when using the Color

Picker in the viewers.

Displayed Depth Range

The Displayed Depth Range setting controls the view normalization of the Z-Channel.

Fit Margin

The Fit Margin setting determines how much padding is left around the frame when the Fit button is

pressed or Fit is selected from the viewer’s contextual menu.

�Display LUT Plugins

This list shows the available display LUTs and activates the selected one as default.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

VR Headsets

The VR Headsets preferences allow configuration of any connected Virtual Reality headsets, including

how stereo and 3D scenes are viewed.

The VR Headsets preferences

Headset Options

The Headset options are used to select the type of VR headset you are using to view the composite

as well as the video layout of the 360° view.

API

•	 Disabled: Disabled turns off and hides all usage of headsets.

•	 Auto: Auto will detect which headset is plugged in.

•	 Oculus: Oculus will set the VR output to the Oculus headset.

•	 OpenVR: OpenVR will support a number of VR headsets like the HTC Vive.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

360° Video Format

•	 Auto: Auto will detect the incoming image layout from the metadata and image

frame aspect.

•	 VCross and HCross: VCross and HCross are the six square faces of a cube laid out in a

cross, vertical or horizontal, with the forward view in the center of the cross, in a 3:4 or

4:3 image.

•	 VStrip and HStrip:  VStrip and HStrip are the six square faces of a cube laid vertically or

horizontally in a line, ordered as Left, Right, Up, Down, Back, Front (+X, -X, +Y, -Y, +Z, -Z),

in a 1:6 or 6:1 image.

•	 LatLong: LatLong is a single 2:1 image in equirectangular mapping.

•	 Enable Mirror Window: Enable Mirror Window will show a window displaying the headset

user’s live view.

Stereo

Similar to normal viewer options for stereo 3D comps, these preferences control how a stereo 3D

comp is displayed in a VR headset.

Mode

•	 Mono: Mono will output a single non stereo eye.

•	 Auto: Auto will detect the method with which the stereo images are stacked.

•	 Vstack: Vstack stereo images are stacked vertically as left on top and right at the bottom.

•	 Hstack: Hstack stereo images are stacked horizontally as left and right.

•	 Swap Eyes: Swap eyes will swap the eyes if stereo is reversed.

3D

Similar to normal viewer options for 3D comps, these preferences control how a 3D comp is displayed

in a VR headset.

Light

•	 Disabled lighting is off.

•	 Auto will detect if lighting is on in the view.

•	 On will force lighting on in the VR view.

Sort Method

•	 Z buffer sorting is the fast OpenGL method of sorting polygons.

•	 Quick Sort will sort the depth of polygons to get better transparency rendering.

•	 Full Sort will use a robust sort and render method to render transparency .

•	 Shadows can be on or off.

•	 Show Matte Objects will make matte objects visible in view or invisible.


Fusion Fundamentals | Chapter 75 Preferences

FUSION