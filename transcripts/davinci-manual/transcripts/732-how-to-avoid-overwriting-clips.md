---
title: "How to Avoid Overwriting Clips"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 732
---

# How to Avoid Overwriting Clips

When Rendering Output Media

Three of the options described previously, “Use unique filenames,” “Place clips in separate folders,”

and “Use commercial workflow,” are all ways of organizing your rendered media to avoid overwriting

rendered clips that happen to share the same file name. These options are necessary because each

clip has one logical range of timecode, and because multiple clips often refer to a single source media

file with one name.

When rendering a clip, DaVinci Resolve automatically overwrites any other media files that have the

same name. So, in instances where you’re trying to preserve the previous filename of the source

media file, or where you’re rendering out multiple versions of the same clip, it’s entirely likely that the

clips you’re trying to output will overwrite one another, leaving you with the last clip you rendered.

The three options mentioned previously prevent this in different ways.

Defining a Range of Clips

and Versions to Render

Once you’ve defined the Render Settings, now you need to decide how much of the Timeline you

need to render. A Mini-Timeline and Thumbnail timeline are available to help you navigate your

project’s clips in order to choose which ones you want to render. Track controls let you enable and

disable whole tracks from being output; for example if you need to render a textless version of a

timeline in which all the title clips are on track V4, you can disable track V4. Furthermore, you can also

use these controls to choose which clip versions you want to render.

To render the entire Timeline:

�Choose Entire Timeline from the Render dropdown in the Deliver page timeline. This option only

appears if clips are not filtered.

To disable a video or audio track to exclude those clips from being rendered:

�Click the Video or Audio Disable Track button for the tracks you want to exclude.

To render a filtered subset of clips in the Timeline:


Open the Color timeline, if it’s not already shown, and choose an option from the Timeline

Filter dropdown to the right of the Clips button in the Interface toolbar.

The contents of the Thumbnail timeline are restricted to show only the clips matching the selected

criteria. For example, if you’ve already rendered a session, but you’ve since made some changes,

you can use one of the “Show Modified Clips” options to display only the clips that have changed

within a particular timeframe. Another possibility is to choose the “Show Unrendered Clips” option

to show all clips that have not yet been rendered.


Choose “All Filtered Clips” from the Render dropdown in the Timeline toolbar.


Deliver | Chapter 187 Rendering Media

DELIVER

To clear clip filtering:

�Choose All Clips from the Timeline Filter dropdown to the right of the Clips button in

the Interface toolbar.

To define a continuous range of clips to render:


To define the first clip in the range you want to render, do one of the following:

�Right-click a clip thumbnail in the Thumbnail timeline and choose Mark In.

�Position the playhead in the Timeline or the Viewer, and press the I key, or right-click the

Timeline ruler and choose Mark In.


To define the last clip in the range you want to render, do one of the following:

�Right-click a clip thumbnail (in the Color timeline) or a clip (in the Edit timeline) in the Thumbnail

timeline and choose Mark Out.

�Position the playhead in the Timeline or the Viewer, and press the O key, or right-click the

Timeline ruler and choose Mark Out.

In and Out points appear within the Timeline ruler, and an orange bar shows the range you’ve selected

to render. The In and Out fields update with the first and last frame numbers, in timecode and frame

count, and the Duration field updates with the total number of frames you’ll be rendering.

IMPORTANT: If you’re in Individual Clips mode, In and Out points automatically snap to the

nearest clip In or Out point in the Timeline. You cannot render partial clips in Individual Clips

mode, but you may do so in Single Clip mode.

To render a single clip:

�Open the Thumbnail timeline if it’s not open already, Right-click any clip thumbnail, and choose

Render This Clip.

�An orange bar in the Timeline ruler shows that clip is selected for rendering. If you need to render

several clips individually, you can select each clip one at a time to add as individual jobs to the

Render Queue.

Choosing Which Versions to Render for Each Clip

By default, the currently selected version that was set in the Color page is rendered for each clip. If

you want to render a different version, the easiest thing to do is to make sure they’re selected on the

Color page Timeline before you open the Deliver page.

However, a Versions submenu, within the Thumbnail timeline’s contextual menu for each thumbnail,

also provides options to manage grade versions. These commands are duplicates of options that are

available from the Thumbnail timeline of the Color page.

To choose which version to render:

�Right-click any clip thumbnail in the Thumbnail timeline, and choose a version from

the Versions submenu.

TIP: You can right-click a clip in the Thumbnail timeline of the Color or Render screen and

rename any version of a grade. This can assist a facility’s workflow when sharing material

between suites and applications.


Deliver | Chapter 187 Rendering Media

DELIVER

Using the Render Queue

Once you’ve defined the settings necessary to render the type of media you require, and the range

of the current session you want to render, you need to add all that information as a job to the Render

Queue. You can add as many jobs to the Render Queue as you need, depending on what files you

need to output.

Each job can have individually specified ranges of clips and individual clip settings, which can include

different render directories, different formats, resolutions, data levels, burn-in settings, and so on. As

a result, you can use the Render Queue to queue up the render of multiple sections of the current

session, or multiple versions of the same media. Furthermore, you can queue up multiple sessions, if

you have several differently graded sessions.

To add a job to the Render Queue:


Select a timeline.


Choose the settings you require in the Render Settings, using one of the Presets, or by choosing

your own custom settings.


Choose a range of clips to render using the Deliver page Timeline using the procedures described

in the previous section.


Click the Add to Render Queue button at the bottom of the Render Settings.


If you haven’t chosen a location for the render yet, you’ll be prompted to do so now via a File

Destination dialog, so choose a location and click Ok. If there’s already media in the render

location you’ve specified, you may also see a dialog telling you “This render may overwrite

existing clips in this folder.” If you want to continue, click Yes, otherwise click No.

That render setup is now added as a job to the Render Queue, showing the project and timeline name,

and location path where the render will be written to.

A selected job in the Render Queue

Media Offline Warning in Render Queue

When you attempt to add a job to the Render Queue with a timeline that contains any offline material,

DaVinci Resolve automatically gives you a warning. You may choose to either cancel adding the job, or

to add it anyway, knowing you’re about to render one or more offline clips.

Media Offline warning box that appears if your timeline contains

offline clips or frames and is added to the Render Queue


Deliver | Chapter 187 Rendering Media

DELIVER

To show more details about jobs in the Render Queue:

Click the Render Queue Option menu (at the upper right-hand corner) and choose Show Job Details.

Each job now lists the frame size, format, frame rate, audio channels and sample rate, and duration

below the name and location path.

A selected job in the Render Queue with job details shown

To rename a job:

Jobs can be given custom names simply by clicking on the default job name (Job 1, Job 2, and

so on) and typing a new name of your own. This can be useful for setting up jobs that you may be

re-rendering over and over as you work on a project.

To start rendering:


If you want to restrict rendering to only selected jobs in the Render Queue, then select one or

more jobs by clicking on one, and then Command-clicking on others to choose discontinuous

jobs, or Shift-clicking on another to select an entire range of jobs. When you select one or more

jobs, only the selected jobs will be rendered. If no jobs are selected, then all jobs in the queue will

be rendered.


Click the Start Render button, underneath the Viewer to the right of the interface.


If there are jobs in the Render Queue that have already been rendered, a dialog will appear asking

“Selected items contain already rendered items. Do you want to re-render them?” Clicking Yes will

re-render all jobs in the Render Queue. Clicking No only renders the jobs that have not yet been

rendered. Clicking Cancel cancels the entire rendering operation.

Rendering begins, starting with the highest job in the list. The Overall Progress bar starts to fill

up, from right to left, indicating how much of what’s been queued up has been rendered so far.

While rendering is in progress, the Start Render button changes to the Stop Render button, which

can be clicked at any time to halt rendering.

TIP: While rendering is in progress, a small progress bar will appear on the DaVinci

Resolve icon in the dock of Mac OS X, or on the taskbar of Windows.

To remove jobs from the Render Queue, do one of the following:

�To clear a specific job: Click the X at the upper right-hand corner of a job’s entry in

the Render Queue.

�To clear all previously rendered jobs: Click the Render Queue Option menu (at the upper right-

hand corner) and choose Clear Rendered.

�To clear all jobs: Click the Render Queue Option menu (at the upper right-hand corner) and

choose Clear All.


Deliver | Chapter 187 Rendering Media

DELIVER

To change a job that has been rendered to appear unrendered again:

Right-click any rendered job, and choose Clear Render Status. You can also select multiple jobs to

change their rendered status all at once. This makes it easy to re-render the exact same job.

To edit a job that has or has not been rendered:


Click the Pencil button in the Render Queue to select it.

Clicking the pencil icon to edit a

job in the Render Queue

The selected Render Queue’s settings repopulate the Render Settings list, and resets the

selected range of the Timeline corresponding to that job.


Change whichever settings you need to.


When you’re finished editing the job, click the Update Job button that appears at the bottom of the

Render Settings, or you can click Add New Job to create a new job with the changes you’ve made,

leaving the previous job untouched.

NOTE: If you click the Pencil button again without clicking Update Job, you’ll be prompted to

Save, Cancel, or Don’t Save.

To review clips that correspond to rendered jobs:

�To show a rendered clip in the Media Storage browser: Right-click any rendered job, and choose

Reveal in Media Storage.

�To show a rendered clip in your computer’s file system (Mac OS only): Right-click any rendered

job, and choose Reveal in Finder.

Rendering Jobs from

Multiple Projects at Once

You can also add multiple projects from the currently open PostgreSQL or local project library to the

render queue all at once. This can be exceptionally useful in situations where you’ve broken a program

into multiple reels, with each reel being a different project.

To render output from multiple projects at once:


Open each project, set up whatever jobs you want to render in the Render Queue, and save that

project without rendering.


When you’ve set up the last project, click the Render Queue Option menu (at the upper right-hand

corner) and choose Show All Projects.

All queued items in projects belonging to the currently selected user (if using a network project

library) or in the currently specified disk location (if using a local project library) now appear in the

Render Queue.


Click Start Render to begin rendering every job from every project in the queue.


When you’re finished, turn Show All Projects off to go back to displaying only the current project’s

render queue items.


Deliver | Chapter 187 Rendering Media

DELIVER