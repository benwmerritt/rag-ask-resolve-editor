---
title: "Using Local Versions by Default"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 588
---

# Using Local Versions by Default

Since local versions are the default method of grading when you first create a new project (unless

you’ve edited your settings presets), you don’t need to do anything to enable this mode at first. As the

name implies, local versions are local to the Timeline in which they appear, so local versions are not

rippled to linked clips, and they’re not shared among different timelines. This makes it easy to avoid

accidentally having grades copied when you don’t want them to be, but you lose the conveniences

that automatic linking can provide.

However, you can always switch the clips in a timeline to use remote versions if you change your mind,

either individually, or all together.

Using Remote Versions to Enable Automatic Linking

Remote versions let all clips from the same source media file in the Media Pool share their grades

automatically, either within a single timeline, or across multiple timelines in the same project. However,

to enable the convenience of remote grades, you need to put DaVinci Resolve into this mode of

working using the Settings window.

To enable remote grades to be used:

�Open the Project Settings, open the General Options panel, and turn off “Use local version for

new clips in timeline” in the Color section.

Turning this option off only affects clips that are added to Timelines from that point onward.

You can keep track of which clips use remote versions by the (R) that appears when you

double‑click the area underneath the thumbnail to hide the codec name in the Thumbnail timeline.

Turning off “Use local version for new clips in timeline” to enable remote grades to be used by default

How Automatic Linking Works

When clips using remote versions have been added to a timeline, any other clips in any timeline that

a)	 use remote versions also, and

b)	 refer to the same file in the Media Pool are linked. Selecting a clip using a remote grade in the

Color page that is automatically linked to one or more clips displays a small “linked” badge at

the right of that clip’s timecode in the Thumbnail timeline.


Color | Chapter 142 Grade Management

COLOR

The linking arrow shows this clip

has the same source as the one

selected on the Timeline

TIP: The Timeline Filtering drop-down in the Color Page toolbar has an option named

“Common Media Pool Clips” that only shows clips in the Timeline that are linked to the

currently selected clip.

Adjustments that you apply to a remote version of one linked clip are automatically rippled to every

other clip it’s linked to, which can save you an enormous amount of time when you’re getting started

with a new program. For example, if every reverse angle from the same take in a particular angle of

coverage is automatically linked using remote versions, then the grade you apply to one reverse angle

clip will ripple to every other reverse angle clip throughout the Timeline.

Timeline with three automatically linked clips shown, and codec names hidden

to reveal the (R) that shows these clips are using remote grades

So long as remote versions are enabled, there are other ways that linked clip relationships are formed.

If, after conforming an AAF, XML, or EDL, you used the Split Clips button in the Color page to split one

conformed clip into many, each of the clips you split would be linked, since they too would share the

same source media in the Media Pool.

Finally, automated linking also occurs for clips that appear in multiple timelines that also use remote

versions. As a result, the grade you apply to one linked clip is automatically rippled to every other clip

it’s linked to.

NOTE: Media management or media consolidation operations that split large source media

files into many individual media files will defeat automatic linking within the same timeline,

since each clip will be conformed to its own individual media file.


Color | Chapter 142 Grade Management

COLOR

Starting with Remote Versions, Then Switching to Local Versions

It’s possible to combine the best aspects of remote and local versions into a single workflow,

taking advantage of your ability to freely switch from one to the other. Since remote versions

make it easy to copy grades among clips that are similar, you can switch to using remote

versions first, and then grade your way through the Timeline until you get to the point where

you need to start making much more specific changes to individual clips. Then, it’s easy to

either switch each linked clip that needs individual adjustment to use a local version, or to

use the Copy Remote Grades To Local command (described later) to copy the current remote

version of each and every clip to a local version, at which point you can make all the specific

tweaks you need to without worrying about changes being accidentally copied.

Creating a Master Timeline

DaVinci Resolve version 9 and earlier would automatically create a Master Timeline whenever you

added clips to the Media Pool. This changed in versions 10 and later, which by default have no Master

Timeline. However, if you want to create a Master Timeline in order to use it as you would have before,

this is easy to do.

If you want a Master Timeline to have a single timeline that always contains all clips currently in the

Media Pool, there’s a way you can create one. However, you need to do it immediately upon creating a

new project, before adding any media to the Media Pool. Once you’ve added one or more clips to the

Media Pool, the option you need to do so will be disabled.

To create a new Master Timeline:


Create a new project, open the General Options panel of the Project Settings, and turn on the

“Automatically match master timeline with media pool” checkbox in the Color section. If you also

want all clips to use Remote versions as you grade by default as in previous versions of DaVinci

Resolve, you can turn off the “Use local version for new clips in timeline” checkbox.


Click Save.


Open the Edit page, and choose File > New Timeline (Command-N).


When the New Timeline Properties window appears, turn the Empty Timeline checkbox off, and

click Create New Timeline.

Now, in addition to the new Timeline, a Master Timeline appears in the Timeline list.

Once created, the Master Timeline contains every clip in the Media Pool of the current project. If you

color correct the clips in the Master Timeline, you’ll find there’s only one set of versions available,

found underneath the Local submenu of the Color Page timeline’s contextual menu. It’s important

to understand that local versions within the Master Timeline are in fact the remote versions found in

every other timeline of that project.

In fact, it would be fair to say that the remote versions found in other timelines are actually the Master

Timeline’s versions. When you grade a clip in the Master Timeline, those grades ripple out to every

other instance of that clip, in every other timeline within that project, via remote versions.

Sharing of remote versions among the Master Timeline and newly conformed timelines is why you can

grade a collection of clips that you import into DaVinci Resolve without any editorial structure, grade

and output offline media, and then reimport a project file that relinks to the original clips along with

their grades. It’s also why you can grade clips in one timeline, and then import additional re-edited

timelines via AAF, XML, or EDL, which automatically inherit all remote versions of grades that were

created in previous timelines.


Color | Chapter 142 Grade Management

COLOR

Differentiating Clips with Individual Versions

If you’ve enabled DaVinci Resolve to add clips with remote versions, there are times when you may

want to suspend automatic linking. As convenient as automatic grade rippling among linked remote

versions is, there are many instances where you may need to stop it. For example, if the Media Pool

contains a source media file with the entire content of an interview, then every clip that has been

conformed to that source media will be linked, which is ordinarily good since you’d expect they’d all

share the same grade. However, if the DP fiddled with the exposure of the camera in the middle of

the interview, such that some clips are lighter and others are darker, you may find yourself needing to

make different adjustments to clips from different parts of the interview.

One way of doing this, which can be useful in timelines where you only need to make a few of these

kinds of changes, is to create a new remote version for every clip to which you need to make an

individual adjustment. Since each version is its own grade, and differently named versions don’t link to

one another, this is a simple solution.

To suspend linking by creating a new remote version:


Move the playhead to the clip you need to alter individually.


Do one of the following:

�Choose Color > Grade Version > Add (Command-Y).

�Right-click the thumbnail in the Timeline, and choose Remote Versions > Create New Version.


Grade the new version that’s appeared.

While this method works well, keep in mind that multiple linked clips using the same version number

will always be linked with one another. In other words, suppose Clip 1, Clip 3, and Clip 5 are linked

using the default Version 1, which has a strong blue grade applied.

Three clips automatically linked, sharing a blue grade

Then, you set Clip 3 to use Version 2 with a different grade, tinted red. Clip 3 is now unlinked from

Clips 1 and 5.

Setting the second of the three clips to use another version with a different remote grade sets it apart

However, switching Clip 5 to also use the red-tinted Version 2 means that Clip 3 and Clip 5 are now

linked together, but Clip 1 is no longer linked.


Color | Chapter 142 Grade Management

COLOR

Setting the third of these clips to share the same remote version as the second

clip now links those two together, omitting the first clip

Every new remote version you create, and every change you make, becomes available to all other

clips in all other timelines that comes from the same source Media Pool clip as the shot you’re working

on. However, any clip can use any version, and which version is used by a linked clip is not rippled.

For example, Timeline 1 contains a clip named Max CU, which has three remote versions. Timeline 5

also contains Max CU, which is currently set to use Version 2. If you open Timeline 1 and add one more

remote version to Max CU, that new version will also be available to Max CU in Timeline 5, but it will

still be set to use Version 2.

Switching Clips Between Local and Remote Versions

You can also suspend remote version grade linking by switching individual clips to use local versions.

This makes it easy to create a situation where some clips are linked, and other clips are not. Keep

in mind that each clip has both local and remote versions, so you can switch from one to the other

without losing anything.

To suspend linking by setting individual clips to use a local version:

Right-click a clip thumbnail, choose the submenu of the corresponding remote version you want

to copy, and choose Copy to Local. The remote version is copied to a local version, which now

appears as the current version that’s used.

You can also set every clip in the entire timeline to use local versions. If you switch an entire

timeline to local versions, then no clip in that timeline will be linked to any other unless you create

a group (covered later in this chapter). This is the default state, but it’s useful even when you’ve

switched to using remote versions when you want to grade one timeline differently from the others

in a project, for example when doing a trim pass for another video or stereo 3D format, or when

grading another cut, such as a trailer, that uses the same media but requires a different look.

To suspend linking by switching from remote versions to local versions:

Right-click any clip thumbnail, and choose one of the following commands;

Use Local Grades: Switches all clips to their local versions. If there are already local versions

defined for each clip, those will appear. If there are no local versions yet defined, each

clip will be ungraded.

Copy Remote Grades to Local: Copies the currently assigned remote version of each clip

to a local version.

Because Undo is used only for individual clip operations, the Use Local Grades and Copy Remote

Grades To Local commands cannot be undone. However, switching a timeline from remote to local

versions is not a one-way trip. You can select Use Remote Grades to switch every clip in a timeline

back to the remote versions at any time.

To switch a timeline back to using remote versions:

Right-click any clip thumbnail, and choose Use Remote Grades.


Color | Chapter 142 Grade Management

COLOR

Furthermore, you can also copy the local grades you made to be remote grades, for instances

where you started grading with local grades, and you want to switch to remote grading using your

local grades as a starting point. Be aware that when you do this in a timeline with many clips that

share the same source media, the grade of the very last shared clip in the Timeline will be the only

remote grade that’s used for those auto-linked clips.

To copy each clip’s local grade to a remote grade for every clip in the current timeline:

Right-click any clip thumbnail, and choose Copy Local Grades to Remote.

If you’re switching back and forth between local and remote versions,

keep the following rules in mind:

•	 If you select Use Remote Grades, change your remote grades, and then Copy Remote

Grades To Local on that timeline again, you’ll overwrite all of your previously graded local

versions. This is a good workflow if you don’t like what you’ve done with your local versions,

and you want to start over by recopying the remote versions.

•	 If you select Use Remote Grades, change your remote grades, and then select Use Local

Grades, you’ll return to your previously graded local versions, as they were before you

selected Use Remote Grades. This is a good workflow if you just want to switch back to your

remote versions in order to copy the remote versions of specific clips to local versions.