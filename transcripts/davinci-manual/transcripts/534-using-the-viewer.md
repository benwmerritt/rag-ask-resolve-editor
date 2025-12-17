---
title: "Using the Viewer"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 534
---

# Using the Viewer

The Viewer is your window into the Timeline. The clip and frame at the current position of the playhead

appears in the Viewer. The Viewer also provides a workspace for picking colors, adjusting Windows,

using split screen stills for reference, and many other display-oriented tasks. If you have a video out

interface connected to a broadcast display or projector, then the contents of the Viewer are typically

mirrored by the video output.

The Viewer Title Bar

The Viewer title bar has controls and indicators making it easy to control and keep track of what it is

you’re looking at.

The Color page title bar with its controls

The Viewer title bar has the following controls:

Zoom and Fit menu: Lets you zoom to a specific percentage, or choose Fit to fit the

image to the total available area of the Viewer.

Viewer Modes: Lets you switch the Viewer type to Image Wipe, Split Screen, or

Highlight modes.

Playback frame rate indicator: A dot shows green if playback performance matches the

frame rate of the project, or red if playback performance drops below real time. To the

right, the current frame rate is displayed.

Timeline name and selection drop-down: The name of the currently open timeline

is displayed. A drop-down to the right lets you open any other timeline in the current

project to take its place.

Timecode viewer and drop-down: A second timecode viewer lets you choose an

alternate timecode/frame count/KeyKode value to display simultaneously to the

timecode viewer next to the transport controls below. A drop-down lets you pick

whether to display source (clip) or record (timeline) timecode.

Proxy Handling: Lets you choose to use either proxies or original media for playback.

Bypass Color and Fusion and drop-down: Lets you disable grades and/or

Fusion effects.

Expand Viewer drop-down: Expands the Viewer to take up the full area of your

workstation’s display above the palettes.

Option menu: Has options that affect the Viewer’s functionality.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

The Color Viewer’s option menu,

showing all the Viewer-related commands

Highlight: Has options for activating the Highlight, Black and White, and Difference views.

Show RGB Picker Values In: Select if the RGB picker shows values in 8-bit or 10-bit scale.

Show Viewer Channels: Has options to select all or individual R, G, or B channels in the Viewer.

Split Screen: Has options for turning on and off and what to display in the Split Screen view.

Timeline Sort Order: Has options for how to order the timelines in the drop-down menu at the top

of the Viewer. Options are: Alphabetical, Creation Date, or Recently Used (shows the last 10 actively

used timelines).Previous Timeline: Opens the previous timeline in the Timeline drop-down menu list.

Next Timeline: Opens the next timeline in the Timeline drop-down menu list.

Show Viewer Options: Show or hide the second row of icons at the top of the Viewer, depending on

the mode you’re in.

Show Marker Overlays: Markers that intercept the playhead when playback is paused appear

superimposed in the Viewer.

Window Outline: Has options on how to display the window outline for a Power Window. On, Off, or

only on the UI viewer and not on your video output.

Video Output Options: Has options to choose what to display on your video output signal, Flags,

Markers, Keyer Overlays, and to Gang the Zoom level with the Viewer.

Markers: Displays any markers that have been set on the timeline. Select one in the list to go to that marker.

Show Reference Wipe: Turns on or off the reference wipe.

Reference Wipe Mode: Has options to change what sources are used in the reference wipe.

Wipe Style: Has options to change what type of reference wipe is used.

Invert Wipe: Inverts the current reference wipe.

Reference Reposition: Opens the Reference Sizing controls that allow you to resize and move the

reference clip.

Gang Timeline Wipe With Current Clip: Lets you maintain the offset between the current clip and a

timeline clip you’re wiping against when you move the current clip selection to other clips.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Turning Grades and/or Fusion Effects Off

The Bypass Color Grades and Fusion Effects button/drop-down commands in the Viewer’s title bar

are also available via View > Bypass Color and Fusion menu commands. Turning off Fusion effects in

the Color page is an easy way to improve playback performance on low power systems when you just

need to make a quick set of grading adjustments. Toggling grades off and on is also a convenient way

to quickly get a before-and-after look at a shot where the “before” goes all the way back to the source.

If you choose Toggle Bypass or click the Viewer control, you’ll turn off whatever is checked in the

optional menu, which lets you choose whether or not you want to bypass both Color and Fusion, or

just one or the other.

(Left) Menu commands for bypassing Color and Fusion, (Right) Edit page Timeline Viewer controls

TIP: If you’re giving your client a before and after look at work you’re doing on a grade, a

more effective technique is to select the specific nodes (one or more) that you want to toggle

on and off, and press Command-D (Enable/Disable Selected Nodes.)

Viewing Isolated Channels

Use the Show Viewer Channels submenu in the Viewer’s option menu to switch the Color page Viewer

among RGB, R, G, or B channels. This can be useful when evaluating a single channel of an image

for noise or other artifacts, or for doing color matching by comparing and adjusting the individual red,

green, and blue channels of two different clips.

The Viewer Toolbar

The Color page also exposes a toolbar at the top of the image (underneath the title bar) that makes

it easy to enable and disable image wipe, split screen, and highlight viewing by clicking one of

these buttons, which then exposes additional controls relating to each of these modes of operation

(described elsewhere in this chapter). Those options can be shown or hidden by clicking the Viewer

option menu and unchecking Show Viewer Options.

The Color page Viewer toolbar showing the

Wipe, Split Screen, and Highlight controls.

The Highlight options are seen in the bar below.

In the process, these buttons provide an easy

reference for when a comparison mode is

enabled. In each of these Viewer modes, the

appropriate controls for customizing that view

appear to the right of the Viewer toolbar.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

Showing Marker Overlays and Annotations

The Color page Viewer supports viewing Marker Overlays and Annotations for Timeline and Clip

markers. From the Viewer’s 3-dot option menu select Show Marker Overlays, or from the Viewer

overlay controls drop-down (bottom left) select the annotation mode.

When Show Marker Overlays is checked, the Color Viewer

will display any Marker Overlays (upper left) and annotations.

The Onscreen Control (OSC) Menu

The Onscreen Control drop-down menu lets you choose which onscreen controls you want to display

and adjust in the Viewer. Some palettes automatically enable corresponding onscreen controls when

you open them. For example, opening the Window palette displays the Power Window onscreen

controls, and opening the Qualifier palette displays the Qualifier onscreen controls.

The onscreen control

menu for the Viewer


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

There are a variety of choices, each corresponding to different adjustments you can make:

Off: All onscreen controls are hidden from view, giving you an unimpeded display of

the image in the Viewer.

Qualifier: Turns on the Color Sample cursor.

For more about using Color Sample controls, see Chapter 135, “Secondary Qualifiers.”

Power Window: Turns the Power Windows onscreen control on and off.

For more about adjusting windows in the Viewer, see Chapter 136,

“Secondary Windows.”

Image Wipe: Toggles mouse control of dragging the split screen directly on the

Viewer on and off.

For more about working with split screens, see “Comparing Clips in the Viewer” later in

this chapter.

Open FX Overlay: Shows and hides whatever onscreen controls are exposed by an

Open FX plugin in the currently selected node.

Color Chart: Shows and hides the color chart overlay that lets you identify a color

chart in the picture that you want to use with the Color Match palette to create an

automatic grade.

Annotations: Shows the annotation tools in the toolbar. Drawing annotations on a

frame without a marker creates a new Timeline marker.

For more about using Annotations, see Chapter 41, “Marking and Finding Clips in the

Timeline.”

TIP: As you work, you may find you want to temporarily hide or show the onscreen controls

so you can get an uncluttered look at the image you’re adjusting. You can toggle any set of

onscreen controls off and on without selecting Off in the menu by pressing Shift-` (tilde).

Toggling Viewer Overlays On and Off

Pressing Shift-` (Tilde) turns the current Viewer overlay on and off. The View > Viewer Overlay

submenu contains commands for showing, hiding, and switching different overlays in the Color page

Viewer. While most of the options in this menu are unassigned by default, they can be assigned to

keys using the Keyboard Customization window.

Onscreen Controls and External Displays

DaVinci Resolve has been designed for use with calibrated external displays connected to video

output interfaces, and for most colorists working on broadcast or theatrical programs, this is the

recommended way to work for color critical evaluation.

Because of this, many of the onscreen controls associated with tasks such as color sampling, window

adjustment, and key manipulation are mirrored to your video output, making it possible to hide the

Viewer on your computer’s monitor and work with only an external display.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR

To choose whether onscreen controls are mirrored to video out or disabled:

Choose an option from the Window Outline submenu in the Viewer’s option menu.

There are three options:

�Off: Hides the window outline on both the external display and the Viewer.

�On: The default, shows the window outline on both the external display and the Viewer.

�Only UI: Hides the window outline on your external display, but leaves it in the Viewer.

To show clip flags on video output:

Turn on the “Show clip flags on video output” checkbox option in the Color page Viewer’s option

menu. This enables drawing one or more small colored flag overlays in the bottom-left corner of

video output. This way, you can always see which clips are flagged on your grading hero display as

you work, if that helps you to keep track of whatever you’re using flags to stay on top of. This is off

by default.

Limitations When Grading With the Viewer on a Computer Display

Most computer displays do not operate at the color critical tolerances or specifications

required for quality control for streaming, broadcast, or theatrical delivery. An additional issue,

however, is that depending on your combination of workstation and computer display, the

Viewer does not necessarily display each clip’s image data as it is displayed by the calibration

that your operating system applies to your computer display, depending on which OS you’re

running DaVinci Resolve on. This makes your computer display potentially unsuitable for

monitoring projects destined for the sRGB standard of the web in its default state. For example,

if you grade a project using the Color page Viewer on your computer display, the resulting clip

may not look the same in the QuickTime player, or in other post-production applications.

You can address this in one of two ways:

•	 If you’re using DaVinci Resolve on macOS, you can turn on “Use Mac Display Color Profile

for viewers” in the Hardware Configuration panel of the System Settings. This lets DaVinci

Resolve use whichever of the color profiles you choose in the Color tab of the Displays

panel in the macOS System Preferences, thereby taking advantage of ColorSync on macOS

to let DaVinci Resolve display color the way your computer monitor does. This now works

for all color profiles that ship with macOS, as well as color profiles that have been generated

by calibration software, such as that available from X-rite, Datacolor, or other applications.

On supported computers, there’s also an option to “Use 10-bit precision in viewers,” if

available, that you can turn on. With this option enabled, rendered output displayed in

QuickTime Player will match what is seen in the DaVinci Resolve Viewer.

•	 Alternately, you can apply a dedicated Color Viewer LUT for calibration, using the 1D/3D

Color Viewer Lookup Table drop-down menu that’s found in the Color Management panel of

the Project Settings. This lets you analyze your computer display for calibration in the same

way you would calibrate an external display, using a probe and color management software,

and apply the resulting calibration LUT in DaVinci Resolve. Keep in mind that monitor

calibration can only make a high quality display standards compliant; it cannot make up for

a display gamut that’s too small. For more information, refer to “Lookup Tables” section see

Chapter 4, “System and User Preferences.”

Strictly speaking, if you’re doing professional work, you should restrict your grading using

a calibrated, 10- or 12-bit class A external broadcast display of some type, connected via a

Blackmagic Design video interface. Assuming everything is running properly, an image that is

output to video from DaVinci Resolve should match an image output to video from any other

post-production application you’re using, and this should be your basis for comparison when

examining the output of two different applications.


Color | Chapter 127 Viewers, Monitoring, and Video Scopes

COLOR