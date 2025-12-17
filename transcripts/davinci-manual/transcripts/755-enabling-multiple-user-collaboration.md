---
title: "Enabling Multiple User Collaboration"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 755
---

# Enabling Multiple User Collaboration

Enabling Multiple User collaboration mode on a project is required to use the collaboration toolset.

To open a project and initiate a collaborative workflow:


Open DaVinci Resolve on a computer that’s connected to a remote project library or

Blackmagic Cloud server.


Open any project on the remote project library DaVinci Resolve is connected to using the

Project Manager.


When the project is open, choose File > Multiple User Collaboration.

Once collaboration is enabled, two additional buttons appear at the lower-right corner of

the DaVinci Resolve interface, next to the Project Manager and Project Setting buttons.

These are the Collaboration Chat and Collaboration buttons.

The Collaboration Chat button (far left) and the

Collaboration button (second from left)

NOTE: When you enable collaboration, the “Auto conform missing clips as media is added

to Media Pool” option in the General Options panel of the Project Settings is automatically

disabled, as it interferes with collaborative workflow. Also, Live Save is automatically turned

on in the Auto Save panel of the User Preferences, to ensure that all collaborators’ work is

saved regularly to avoid conflicts between collaborators.

Opening Projects to Collaborate

Projects that have Collaboration enabled appear with a badge on their thumbnail in the Project

Manager to let you know that project is available for collaboration.

An icon indicates that a project in the

Project Manager is available for collaboration

At this point, anyone else who has access to this remote project library server can simply open

this project up and work collaboratively with you. Whenever a collaborator opens the same

project you’re working in, the Collaboration Chat button at the bottom of the DaVinci Resolve

UI highlights to let you know you have a message.


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

The Collaboration Chat button

highlights to let you know you

have a message

Opening the Collaboration Chat window shows who’s collaborating with you.

A new message in the Collaboration Chat window lets you

know who else has opened the project you’re working on

Customizing Your Collaborator Identification

Once you’ve set up a project for collaboration, you want to make sure it’s easy to tell all your

collaborators apart. Clicking the Collaboration button opens a list of all collaborators, or project

members, working in that project.

Opening the Collaboration list shows

all the current project members

The top member is you, and you can change the name you use by editing the text field. Your user icon

is set automatically based on the image you chose either in your Blackmagic Cloud account or the

DaVinci Resolve Project Server. If you haven’t chosen an image, it defaults to the first two letters of

your user name. Additionally, you can see the other member’s workstation OS revealed as an icon to

the right of their name.


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

How Collaboration Works

At its simplest, collaborative workflow uses a “first come, first served” model to manage who has

can make changes to what. Essentially, the first collaborator to select a bin in the Media Pool, open a

timeline, or select a clip in the Fusion page or Color page gets a “lock” on that item. Once an item is

locked (indicated by a colored collaborator badge), other collaborators can look at it, but they cannot

make changes. This prevents versioning conflicts from occurring.

Bin and clip locks are released when a collaborator selects a different bin or timeline in the Media or

Edit pages, or a different clip in the Fusion page or Color page. At that point, the changes that have

been made to the previously locked item are “checked in” and made available to all collaborators

once they refresh their project (by clicking a circular refresh icon that appears to the right of bins in the

Media Pool or in the corner of the Edit page Viewer).

All changes that collaborators make are automatically saved to the project as they’re made, so no work

will ever be lost as you collaborate with your team. However, each collaborator gets to decide when

they want to update the bin, timeline, or clip they’re currently working on to see the changes made by

everyone else, in order to prevent a kaleidoscope of constant alterations to compositions and grades

from being a distraction while you’re working.

The following sections describe Bin and Timeline locking and Clip locking in more detail.

Automatic Bin and Timeline Locking

Whenever a collaborator opens a particular bin, that bin and its contents are locked, preventing any

other collaborators who open that project from making alterations to anything inside that same bin.

This prevents versioning conflicts while work is in progress. When a bin is locked, you can still view its

contents, if for instance you just need to figure out where a particular clip has been put, but you can’t

make changes.

Collaborators can open locked bins and see the contents for reference, but they cannot make any

organizational or editorial changes. The only things that can be changed once a bin and its contents

are locked are the creation or alterations of clip compositions in the Fusion page, and alterations to

clip grades in the Color page.

You can always tell when a collaborator has a lock on a bin and its contents because a badge appears

to the right of the bin in the Bin list, and in the corner of timeline thumbnails that are visible in the

Media Pool browser area. Hovering the mouse over that badge in the Bin list reveals a tooltip with that

collaborator’s name.

An icon indicates that another collaborator has a lock on the Projects bin.


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

Once a collaborator (someone other than you) makes changes to a bin’s contents or to a timeline, you’ll

see a circular “refresh” badge appear by each affected bin in the Bin list of the Media Pool, alongside

their collaborator icon. Click these badges whenever you want to update your version of the shared

project with all organizational and editorial changes made by others in that bin.

To release a bin or timeline, simply select another bin or timeline. It’s that simple.

An icon indicates that another collaborator

has made changes; clicking it refreshes

your project to show those changes

Managing Bin Locks Manually

You can also manually control the locked state of bins, during instances where you want to keep

bins locked for future use or prevent them from becoming locked when you only want to browse

the contents.

Keeping Bins Locked

If you want to lock one or more bins that you know you’re going to be switching among to either

prevent other collaborators from making changes or so that nobody else inadvertently prevents you

from having access, you can right-click one or more selected bins and choose Lock Bins to lock them.

Bins locked in this way remain locked, even when you deselect them, until you right-click them again

and choose Unlock Bins. Other users will see your collaboration icon as well, so they will know who

currently has the bin locked.

Manually locked bins stay locked even

when they’re not selected

Keeping Bins Unlocked

Additionally, you can choose to keep bins unlocked when selected. For example, you may just want

to examine the contents of a bin without keeping someone else from editing its contents. In this case,

simply Option-click any bin to open that bin in read-only mode, which is indicated by an eyeball badge

to the left of that bin in the Bin list. In this mode, any other collaborator can still lock that bin while

you’re examining its contents. Selecting any other bin will clear this read-only status.

Selecting a bin in read only mode

allows collaborators to lock that

bin while you examine its contents


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

TIP: While a bin is open but manually unlocked by you, you can still open clips into the

Source Viewer and add markers to them, so long as another user doesn’t select that same bin

and lock you out.

Manually Locking and Unlocking Timelines

You can also manually manage the locking of timelines. Opening a timeline automatically locks other

collaborators out of making changes to that timeline, but it does allow other users to modify the bin

that timeline appears within. This allows for greater flexibility in setting up your Media Pool and avoids

locking media or other timelines in the same folder. You can still manually choose to lock individual

Media Pool bins to secure their contents independently.

To unlock a timeline to let other collaborators work on it:

�Right-click that timeline in the Media Pool and choose Timelines > Unlock Timeline from the

contextual menu.

To lock a timeline preventing other collaborators from working on it:


Right-click that timeline in the Media Pool and choose Timelines > Lock Timeline from the

contextual menu.


Other collaborators will be unable to modify the timeline while you have a lock on it, however they

will be able to modify any other clips and timelines in the bin.

Automatic Clip Locking

Clip locking in the Fusion and Color pages works similarly. As multiple compositing artists work in the

Fusion page, and multiple colorists work in the Color page, the first compositing artist or colorist to

select any given clip has an automatic lock on that clip. Other compositing artists or colorists will see

a badge on that clip in the Thumbnail timeline showing that it’s locked as well as letting them know

who has the lock. In the following screenshot, the SO badge in the corner of clip 7 in the Color page

Thumbnail timeline indicates that clip is locked.

Badges in the Thumbnail timeline indicate which

clips are locked because a collaborator is grading them

Automatically Checking In Work When You Change Clips

When you’re finished with the clip you’re working on, you need only select another clip for the

changes you made to the previously selected clip to be automatically saved and pushed to all other

colorists who are working on that timeline in the Color page. No refresh is needed. This is the main

difference between clip locking in the Color page and bin locking.


Project Libraries, Collaborative, and Remote Workflows | Chapter 197 Collaborative Workflow

DELIVER

Compositing Artists and Colorists Can Work Together

The Fusion page and Color page each maintain separate clip locks. This means that for any given pool

of compositing artists, only one will be able to work on a given clip at a time, while in the Color page

only a single colorist will be able to work on a clip at a time.

However, because Fusion and Color page clip locking is maintained separately, that means that one

compositing artist and one colorist can work on a single clip in the timeline simultaneously, even while

an editor is working on that timeline.