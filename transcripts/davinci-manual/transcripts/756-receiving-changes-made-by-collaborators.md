---
title: "Receiving Changes Made by Collaborators"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 756
---

# Receiving Changes Made by Collaborators

As you work collaboratively, it will be common for groups of compositing artists to be executing

multiple compositions at a time, while colorist and their assistants will be working on the grade, and an

editor and their assistants will be refining the edit, all working together within the same project.

Receiving Changes On the Edit Page

While compositors are compositing and colorists are grading clips within the same timeline of the

same project, each clip that’s adjusted in the Fusion or Color page triggers a Refresh badge to appear

in three areas of the Edit page, so the collaborating editor(s) can decide when to update their timeline

to see the changes that have been made.

At the upper-right corner of the Timeline Viewer. Clicking this badge refreshes

the composites and grades of all clips in the currently open Timeline.

A clickable “update” badge appears in the corner

of the Timeline Viewer for timelines with edits,

grades, and composites that have been updated

At the right of the bin containing the modified timeline in the Media Pool’s bin list.

Clicking this badge refreshes all clips in the Timeline within that bin.

A clickable “update” badge appears over bins

containing timelines in the Media Pool with edits,

grades, and composites that have been updated


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

At the upper-right corner of each modified clip in the Timeline.

A clickable “update” badge appears over clips in the Timeline

with edits, grades, and composites that have been updated

Receiving Changes On the Fusion and Color Pages

For collaborators working on the Fusion or Color pages, other badges indicate when editors have

made changes to the Timeline, or when other compositing artists or colorists have made changes to

other clips in that timeline.

Timelines that you’re locked out of because another collaborator has a lock on them are

indicated by a badge at the upper-right corner of the Viewer, while changes made to the

Timeline by editors on the Edit page are indicated by a refresh badge in the same location.

Clicking this badge refreshes all clips in the Timeline.

A badge in the Viewer shows that a

viewer has a lock on this timeline

If you open up the Media Pool, then a badge appears at the right of any bin in the

Bin List that’s been reorganized or that contains a modified timeline. Clicking this

badge refreshes all clips in the Timeline within that bin.

A badge appears to the right of bins in the

Media Pool containing timelines that have

been updated


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

A badge appears at the upper-right corner of each clip in the Thumbnail timeline

that’s been modified by a fellow compositing artist or colorist. Clicking a single clip’s

badge updates that clip alone.

A badge appears over clips in the Timeline

with grades that have been updated.

Clicking this badge refreshes just that clip.

Examples of Collaborators

Working Together

The first collaborator that opens a timeline is the only person that can make editorial changes to that

timeline in the Edit or Fairlight pages. Other collaborators who open that project are “locked out”

of making changes to the Edit or Fairlight pages, but they can see the Timeline, and they can make

grading changes in the Fusion or Color pages. This means in situations where you want multiple

editors to be working on a project, it can be ideal to organize your program into separate “reels,”

where each reel of a project is a separate timeline in a separate bin.

Multiple Editors Working Together

The first collaborator that opens a timeline is the only person that can make editorial changes to that

timeline in the Edit or Fairlight pages. Other collaborators who open that project are “locked out”

of making changes to the Edit or Fairlight pages, but they can see the Timeline, and they can make

grading changes in the Fusion or Color pages. This means in situations where you want multiple

editors to be working on a project, it can be ideal to organize your program into separate “reels,”

where each reel of a project is a separate timeline in a separate bin.

On the other hand, if two or more editors must both work on the same timeline, this can be

accomplished using duplicate timelines and then merging the changes back together later on. For

example, collaborating editor Anne can do the following to make changes to a timeline that editor Erin

is already working on:

�First, Anne can duplicate the locked timeline into a separate bin from the one Erin has a lock on.

Alternately, Erin could be proactive and duplicate the timeline into a separate bin in advance.

�Second, Anne will re-edit the duplicate timeline to make whatever changes are necessary to

a different scene than the one Erin is currently working on. Working on different scenes is the

cleanest and easiest way of using this workflow.

�Third, Anne uses Collaborative Chat to notify Erin that the changes are finished.

�Fourth, Erin then refreshes the project to see Anne’s updated duplicate timeline in the Media Pool,

right-clicks it, and chooses Compare With Current Timeline from the contextual menu to show

the Timeline Comparison window that makes it possible to merge the changed section of the

duplicate timeline with the original timeline that Erin already has open.


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

In the following screenshot, Erin’s highlighted changes (made while Anne was working) can be seen

at the left, and Anne’s highlighted changes can be seen at the right. Right-clicking within the right

highlighted area reveals an Accept Change command that lets that scene’s changes be merged from

the duplicate timeline back to Erin’s original timeline.

Using the Compare With Current Timeline command lets you see the differences

between two differently edited versions of the same timeline, and merge a scene’s

worth of changes that a collaborator has made (at right) back to the original timeline

For more information on comparing timelines, see Chapter 34, “Creating and Working with

Timelines.”

Editors and Assistant Editors Working Together

Collaborators can edit metadata, create new bins, and reorganize clips within unlocked bins only.

This means that your project should be organized so that an editor can lock the contents of the bins

they need to work with at a given point in time, while the assistants can work on additional timelines

and media within other bins in that project.

However, in addition to being able to copy timelines from a locked bin to a bin that you control, you

can also copy clips from one timeline to another. In this way, if you absolutely need to make changes

to source clips while the original source clips are locked, you can make your changes to copies of

these clips.

Editors and Compositing Artists Working Together

Editors and compositing artists can work together closely, since compositing artists can create

compositions for one or more clips in a timeline while it’s being edited, even though that timeline and

the bin it’s in are locked to other editors.

Here’s an example of an editor working on a commercial spot with a lot of greenscreen material

working together with one or more compositing artists.

�First, the editor cuts together each foreground clip with actors performing as a rough cut, and

once that rough cut is assembled, they edit in the background clips that accompany each

greenscreen clips to create a series of stack of clips.

�Second, the editor selects each stack of clips, one by one, and uses the New Fusion Clip

command to create Fusion clips that the compositing artists can work on. By making each of these

clips into Fusion clips, the editor is making it easy for the compositing artists to have access to all

the clips necessary for each composition from within the Fusion page, collaboratively.


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

�At this point, the editor uses collaborative chat to notify the compositing artists that there are

composites ready for them to work on, and the editor can then turn their attention back to

refining the edit.

�Upon being notified that they can begin work, one or more compositing artists start working

through the Fusion clip compositions while the editor is working, to create each multi-layered

composite that’s necessary. As each compositing artist finishes a clip and moves to a new clip

to begin work, the editor sees a notification badge at the upper-right corner of each clip in the

Timeline that’s been composited, as well as notification badges in the Bin List of the Media Pool,

and at the upper-right corner of the Timeline viewer. Clicking any of these badges will refresh one

or more of these clips, so the editor can see the changes.

Multiple Compositing Artists Working Together

To prevent versioning issues, only one compositing artist can work on a particular clip at a particular

time in the Fusion page, and the first compositing artist to select a clip puts a lock on that clip. Other

collaborators looking at the Thumbnail timeline in the Fusion page will see a small icon that shows

it’s locked, letting them know they can’t make any changes to it until whoever is working on that

composition moves to another clip.

A small icon indicates that you’re

locked out because another compositing

artist is working on that clip

This means that multiple compositing artists can’t work on the same composition at the same time.

However, an assisting compositing artist can do preparatory work on one composition, such as

doing rotosocoping, paint, particle system design, or any other time-consuming task, while a lead

compositing artist works on another shot in the meantime. Once the assisting compositor is done, they

can select another clip to work on and use collaborative chat to let the other compositor know they’re

done and that clip is ready for more work.

In order to prevent half-finished work from being disseminated to other collaborators, a clip that’s in

the process of being worked on in the Fusion page isn’t updated for anyone else who’s working on

that same timeline until the compositing artist who’s working on it selects another clip. Immediately

upon being deselected, all changes are automatically checked in and made available to all other

collaborators, who see notification badges in the Fusion page and the Edit page to alert them that

changes are available and that they can refresh their timeline to see the updates.

Editors and Colorists Working Together

Colorists and editors can work together very closely in DaVinci Resolve, as colorists can grade the

shots of a timeline that an editor is currently working on, even though that timeline and the bin it’s in

are locked to other editors.

From the colorist’s point of view, whenever the editor makes an alteration to the Timeline, a badge

appears at the upper-right corner of the Color page Viewer to indicate that a change has been made

to the timeline being graded. Clicking this badge updates the timeline the Colorist is working on.


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

In order to prevent half-finished work from being disseminated to the editor (or worse, being seen by

the client), clips that are in the process of being graded aren’t updated for other collaborators that

are looking at that timeline until the colorist who’s working on it “checks in” their work by selecting

another clip. So, from the editor’s point of view, whenever a colorist has finished grading a clip and

has selected another clip to grade, a series of badges appear in the Edit page, one on the clip that’s

been graded, one on the Timeline Viewer and one on the bin in the Bin List that contains the Timeline.

Clicking any of these badges updates the Timeline with the latest grades.