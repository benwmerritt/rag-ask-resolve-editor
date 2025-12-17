---
title: "Using Markers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 746
---

# Using Markers

There are three ways to make your opinion known on a clip in Presentations. The first is speaking

directly through video conferencing as described above, the second and third are through

markers and chat.

The Markers column

Markers allow you to make written comments attached to a specific frame of video. This lets you give

targeted advice exactly where it needs to be. The main benefit of using markers is that they also

immediately transfer to the DaVinci Resolve timeline used to make the clip. This ensures that your

comments make it back to the editor/colorist/audio engineer as they work on the project.

To Add a Marker to a Clip at the Playhead Position, do one of the following:

�Click on the Add Marker icon in the Viewer.

�Tap the letter M on your keyboard.

�In the Markers column, write your comment in the text box at the bottom, and click on the Add

Marker button.

Markers will show up as a triangle that is the same color as the colored dot associated with the user’s

thumbnail in the Video Conferencing pane.

To Edit the Text Contents of a Marker:


Hover over the marker in the Markers column, and tap on the Pencil icon.


Write your comment in the text box.


Click on save.


Blackmagic Cloud | Chapter 193 Blackmagic Cloud Presentations

DELIVER

To Delete a Marker from a Clip:


Hover over the marker in the Markers column, and tap on the Trashcan icon.


Click on Delete in the warning dialog.

Using Chat

The Chat column gives you a simple text-based conversation tool that is persistently saved. This lets

you leave notes, comments, and refer back to previous sessions if necessary. The Chat column is not

tied to any specific clip but to the presentation as a whole.

The Chat column

To Leave a Chat Comment:


Write your message in the text box at the bottom of the Chat column.


Press the Send icon.

Your message will appear in the chat window in chronological order. Chat messages you’ve

sent will be unattributed and right justified. Messages other members sent will be left justified

and have their names and User icon attached to them.

Currently, the chat is visible to all members of the presentation, and there is no way to delete a

chat message once it is sent, so be kind.


Blackmagic Cloud | Chapter 193 Blackmagic Cloud Presentations

DELIVER

Presentations in DaVinci Resolve

The Presentations application is designed to work in conjunction with DaVinci Resolve. Each “clip” in

Presentations is linked to a DaVinci Resolve timeline. Any markers added by members in Presentations

are updated to the timeline in DaVinci Resolve automatically and vice versa.

Sending a Timeline to Presentations

Each “clip” in Presentations is a DaVinci Resolve timeline. In order to populate the Clips column with

footage to work with, you will first need to export your timeline from DaVinci Resolve to Presentations.

The Presentations Render Preset in the Deliver page.

To Send a DaVinci Resolve Timeline to Presentations:


Make sure you are signed into your Blackmagic Cloud account in the Internet Accounts section of

the DaVinci Resolve Preferences.


Make sure you are a member of the presentation you wish to send the timeline to.


Open the timeline you wish to send.


In the Deliver page, select the Presentations render preset.


In the File Name field, type in a name for your timeline to appear as in Presentations.


In the Upload to field, select the presentation you wish to upload the timeline to. If the presentation

is not in the list, see steps 1 and 2.


Click on the Add to Render Queue button at the bottom of the Render Settings.


Click on the Render All button under the Render Queue.

There are no video or audio codec parameters to set, and DaVinci Resolve will proceed to

render your timeline and upload it automatically to the selected presentation. Any member

can upload a timeline to a presentation, not just the administrator.

The timeline will now appear as a “clip” in the Clips column of the presentation.


Blackmagic Cloud | Chapter 193 Blackmagic Cloud Presentations

DELIVER

Using Markers Between Presentations and DaVinci Resolve

A key benefit of Presentations is persistent markers between a presentation and a DaVinci Resolve

timeline. Once a timeline has been uploaded to a presentation, it’s automatically linked behind the

scenes and any markers added, either in the Presentations app or in DaVinci Resolve, will sync with

each other.

On the DaVinci Resolve side, the sync occurs when a timeline is open, and the user is logged in

to the Blackmagic Cloud. For example, markers can be added by members the previous night and

will then sync when the editor opens the timeline in the morning. You can also collaborate live

with a presentation if the members are online and the editor is working in the timeline, updating

markers in real time.

Presentations markers are circular in shape and are synced

between the timeline and its associated Presentations clip.

Markers that are linked to Presentations display as circular on the DaVinci Resolve timeline to

differentiate them from normal markers that are triangular in shape. Presentations Markers will also

reflect the color of the member creating the marker.

Markers don’t just travel one way from Presentations to DaVinci Resolve. While working on a timeline

in DaVinci Resolve, the user can add special Presentations markers that will sync and show up in the

Presentations application, to be viewed by all members.

To Add a Presentations marker on a DaVinci Resolve Timeline:


You must have already uploaded a timeline to Presentations as described above.


Place the playhead in the Timeline where you want the Presentations marker.


Select Mark > Add Marker > Presentations.

To Delete a Presentations marker on a DaVinci Resolve Timeline:


Select the circular Presentations marker on the Timeline.


Press the Delete key.


Click on the Delete button in the warning dialog.

Deleting a Presentations marker will remove it from both the Timeline and the presentation

itself. This operation is not undoable. The timeline user is able to delete a Presentations

marker from any member, not just their own.


Blackmagic Cloud | Chapter 193 Blackmagic Cloud Presentations

DELIVER

Chapter 194

Blackmagic Cloud

Organizations

If you are a large company with many collaborators, setting up an Organization

in the Blackmagic Cloud lets you manage users, storage, licenses, and centralize

billing from one easy interface.

Contents

Organizations��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4139

Creating an Organization Account��������������������������������������������������������������������������������������������������������������������������������������������� 4139

Home��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4140

Members������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4140

Groups�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4141

Project Servers�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4143

Blackmagic Server vs. Dedicated Server�������������������������������������������������������������������������������������������������������������������������������� 4144

Licenses��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4145

Storage����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4146

Presentations����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4147

Billing�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4148

Settings���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4148


Blackmagic Cloud | Chapter 194 Blackmagic Cloud Organizations

DELIVER