---
title: "Multicam Keyboard Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 166
---

# Multicam Keyboard Controls

There’s also a full set of keyboard shortcuts that can be used for multicam editing.

�Multicam Cut: (Clip > Multicam Cut submenu) Pressing the 1 through 9 number keys performs a

cut-and-switch operation, the same as if you’d clicked on an angle button of a multicam clip in the

Source Viewer.

�Multicam Switch: (Clip > Multicam Switch submenu) Pressing Option-1 through 9 performs a

switch operation, the same as if you’d Option-clicked an angle button of a multicam clip in the

Source Viewer.

�Previous/Next Angle: (Edit > Multicam submenu) Pressing Command-Shift-Left or Right Arrow lets

you switch to the previous or next angle. These controls will also loop back around to the first or

last angles in the multicam clip.

�Audio/Video Switching: (Edit > Multicam submenu) Pressing Option-Shift-[ sets the Multicam

Viewer to cut or switch both Video and Audio at the same time. Pressing Option-Shift-] sets the

Multicam Viewer to cut or switch Video only. Pressing Option-Shift-\ sets the Multicam Viewer to

cut or switch Audio only.

�Previous/Next Page: (Edit > Multicam submenu) Pressing Option-Shift-Left or Right Arrow lets

you move to the previous or next page of multicam angles, if there are more angles than can be

displayed in the Viewer’s current multi-angle setting.


Edit | Chapter 42 Multicam Editing

EDIT

Editing Multicam Clips in the Timeline

When it comes to editing and trimming, there’s no functional difference between multicam clips and

any other kind of clip. Because you’re technically adding through edits to a single clip, you have the

option or deleting any edit by selecting it and pressing the Delete key.

But multicam clips are special in that you always have the option of switching angles, either using the

Multicam Viewer, or right in the Timeline via each clip’s contextual menu.

To switch the angle of any multicam clip in the Timeline:

�Right-click any clip and choose a new angle from the “Switch Multicam Clip Angle” submenu.

This also allows you to change angles without needing to use the Multicam Viewer.

In the event that you want to eliminate all unused angles from a multicam clip and “flatten”

it to simply be a single clip in the Timeline, there’s a command for that.

To flatten a multicam clip in the Timeline:

�Right-click any clip and choose Flatten Multicam Clip from the contextual menu. Select either

Copying Multicam Grades to apply the existing color grade to the flattened multicam angles, or

Retaining Grades from Angles to keep any color grades done on individual angles. All unused

angles are deleted, the clip becomes shorter if it included black tails because of another unused

angle, and you end up with a single ordinary clip in the Timeline.

To Match Frame to the angle of any multicam clip in the Timeline:

�Place the playhead over the frame in the Timeline you want to match and press F. The exact

frame of the mulitcam clip referenced will appear in the Source Viewer with the appropriate angle

already selected.

To Match Frame to the multicam clip in the Source Viewer:

�Open the multicam clip in the Source Viewer. Navigate to the frame you want to find using the jog

bar and press F. The playhead in the Timeline will move to the exact frame of the mulitcam clip

referenced in the Source Viewer. If the frame you selected is not in the Timeline, when you press F

nothing will happen.

To edit an angle of any multicam clip directly from the Source Viewer:

�You can click and drag any multicam angle directly from the Source Viewer to the Timeline.

The length of the clip is bounded by the In and Out point selection of the clip.

Referencing a Line Cut

You may sometimes be provided with what’s called a “line cut” from a production.

This is a pre-edited version of the program, cut live with the switcher and recorded during

the performance or event, that’s meant to be used as a reference for what you’re doing. If you

want to reference a line cut that’s been given to you as a movie file, you can add it as an

Offline Reference Movie, and compare it to the Timeline using the Offline Reference Movie

mode of the Source Viewer in the Edit page.

For more information on using an Offline video to compare with a timeline in the Edit page,

see Chapter 55, “Preparing Timelines for Import and Comparison.”


Edit | Chapter 42 Multicam Editing

EDIT

Multicam SmartSwitch (Studio Version Only)

DaVinci Resolve 20 has a new AI-powered multicam tool called Multicam SmartSwitch, which will

analyze all multicam camera angles and automatically cut to the most appropriate angle, based on

who is the active speaker. Multicam SmartSwitch doesn’t just use the audio track to determine which

angle is best but includes other video related traits, such as lip movement in the frame, and if the shot

is a wide or close up. Trained on thousands of hours of multicam footage, Multicam SmartSwitch is

great for giving you a good first pass and letting you finesse the rest.

Selecting a multicam clip to be used with Multicam SmartSwitch

To use Multicam SmartSwitch to automatically cut your multicam clip:


Create a multicam clip in the Media Pool of all the individual camera angle clips, as described

previously in this chapter.


Edit the multicam clip into the timeline.


Right-click on the multicam clip, and select Multicam SmartSwitch from the context menu.


Select the appropriate settings and parameters from the Multicam SmartSwitch tool.


Click Analyze.

Multicam SmartSwitch analyzing the multicam clip

At this point, Multicam SmartSwitch will analyze all your video angles and audio tracks and choose

what it thinks the best angle is under the circumstances. This can take quite some time, depending on

the length and number of cameras angles used in the multicam shoot.


Edit | Chapter 42 Multicam Editing

EDIT

Multicam SmartSwitch finished cut on the timeline

When it is finished, you will have a fully cut version of your multicam clip available in the timeline. If you

don’t like a choice that Multicam SmartSwitch made, you can easily switch the camera angle by right-

clicking on it and selecting a new one from the Switch Multicam Clip Angle context menu, or using the

standard trim tools to change the edit point.

The Multicam SmartSwitch tool


Edit | Chapter 42 Multicam Editing

EDIT

Multicam SmartSwitch Settings

You can set parameters for the Multicam SmartSwitch tool that modifies how it makes its cut decisions.

Angle Switching: Adjusts the timing of the edits.

�Minimum Edit Duration: Sets the minimum length of an edit. Regardless of what happens in the

cut, Multicam SmartSwitch won’t change angles before the end of this duration.

�Edit Change Delay: This lets you set the amount of time between the person speaking and the

edit changing.

Wide Angle Setup: Just like a technical director, Multicam SmartSwitch will tend to use wide angles to

cover things like people talking over each other and silences. You can tweak those settings here.

�Automatically detect wide angles: Check this box to have Multicam SmartSwitch automatically

choose what it considers to be wide shots.

�Wide Angle: If you have a specific wide shot you want to use for coverage, you can manually

select it here.

�Wide Angle Frequency: How often should Multicam SmartSwitch cut back to the wide shot.

Choices are Low, Medium, and High.

�Use wide angle for intro and outro: Check this box to open and close the multicam

clip on a wide shot.

�Use wide angle for silence: Check this box to go back to the wide shot when no one is speaking.

SmartSwitch Setup: Determines what media types to use for the analysis.

�Switch: You can choose for the cuts to be Video Only or cut Video and Audio tracks together.

�Use Audio Only Fast Analysis: Check this box to use an analysis that uses only the audio to make

its decisions, rather than analyze the video as well. This runs much faster and is only available in

certain modes.

Grading Multicam Clips

Multicam clips appear like any other clip in the Color page. However, each angle within a multicam

clip has its own grade (unlike the Take Selector described later, in which all takes share the same

grade). If you grade a multicam clip, you’re actually editing the grade of the specific angle that’s

currently exposed in that clip.

If you want access all of the angles within a multicam clip for grading, right-click it and choose “Open

in Timeline” to expose each angle within a superimposed stack. Then you can open the Color page

and grade whatever angles you want, whether they’re visible back in the Edit page or not. You might

do this to make the different angles match one another better, or to pre-grade all of the angles to give

them the look you want prior to multicam editing. You also need to use “Open in Timeline” in order to

access and manipulate the camera RAW settings if your footage was shot in a RAW format.

An open multicam clip in the Color page exposes all of its angles for individual grading


Edit | Chapter 42 Multicam Editing

EDIT

Because opening multicam clips in the Timeline results in a vertical stack of superimposed clips,

you’ll want to turn on Unmix in the Color page viewer so that you can actually see the currently

selected angle in the Thumbnail Timeline while you work.

The Unmix control lets you see only

one of a superimposed stack of clips

When flattening a multicam clip, you can choose to grade individual angles or the multicam clip as a

whole. In the Edit page, select Flatten Multicam Clip and either Copying Multicam Grades to apply the

existing color grade to the flattened multicam angles, or Retaining Grades from Angles to keep any

color grades done on individual angles.

When you’re done grading, go back to the Edit page, and use the path control at the bottom left-hand

corner of the Timeline to return to your edited Multicam timeline.


Edit | Chapter 42 Multicam Editing

EDIT