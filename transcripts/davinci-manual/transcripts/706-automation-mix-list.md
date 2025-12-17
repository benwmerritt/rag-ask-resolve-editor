---
title: "Automation – Mix List"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 706
---

# Automation – Mix List

The Mix List allows you to create and manage multiple mix “passes” and complete routing and effects

setups for a single Timeline. Each stored mix can have totally different mix automation data that is

changing over time, routing, plugin setup, track grouping, etc.

This capability is incredibly powerful and allows a lot of creative freedom for creating different

versions of mixes (for example moving between stereo, 5.1, and Dolby Atmos as formats), or between

using totally different plugin effects or different creative approaches to the mix itself using all of the

automated parameters.

The Mix List Window


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

So the Mix List’s utility is not limited to storing mix automation data; it can be used to store a dynamic

preset of literally anything about the setup of the Mixer.

Keep in mind that the Mix List is particular to a single Timeline and also cannot be shared between

projects. However, using the Mix List can be more convenient than saving multiple different versions of

timelines or projects.

The Mix List can act as a floating window where you can see the various mixes, or it can be hidden

until you need to load or save a new version.

Using the Mix List Window

�Set up your mix, including all routing and automation as you like.

�When you’re ready to save a mix version, choose Fairlight > Automation > Mix List, then choose

“Save Mix” and give it a name, along with any notes you make want to add.

�You can then change your mix automation, any routing, etc. you wish and save a new version, load

a different version, or delete an existing mix.

�The “System” preset is an internal system preset that can’t be altered; it can be ignored.

The “New Mix” Dialog

For “New Mix” in the Mix List window, a dialog appears with the following options:

�Cancel: Lets you cancel the operation.

�Write All: Writes present levels of all controls to their automation curves establishing a baseline

“snapshot” of all parameters.

�Empty Mix: Clears all automation data from the mix, leaving only the assignments, routing,

track group enables, etc. This option offers a simple way to start “fresh” with a mixer setup on

a new mix.

New Mix dialog

Playing Automation

After you’ve automated a mix, playing it back is as simple as moving the playhead to an area of the

timeline prior to the recorded automation, and initiating playback. As the timeline plays, the onscreen

controls for each automated parameter are shown in green. They move and update to show their

recorded levels.

Controls that have recorded

automation during playback

are shown in green.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Chapter 179

Track Groups

Track Groups let you make adjustments and modifications to your mix across

multiple tracks at the same time.

Contents

Editing with Track Groups�������������������������������������������������������������������������������������������������������������������������������������������������������������� 3917

Mixing with Track Groups��������������������������������������������������������������������������������������������������������������������������������������������������������������� 3917

Creating and Editing Track Groups�������������������������������������������������������������������������������������������������������������������������������������������� 3919

The Mixer and Track Groups�������������������������������������������������������������������������������������������������������������������������������������������������������� 3920


Fairlight | Chapter 179 Track Groups

FAIRLIGHT

Editing with Track Groups

Track groups let you switch focus from individual tracks to groups of tracks, which can range from a

small number of tracks to a large multitrack sub-mix group.

When a group is enabled, editing operations apply to all tracks in the group. However, some

operations that involve moving clip boundaries or trimming do not.

For example, pressing the Up and Down arrows to navigate to a clip boundary obeys the boundaries

of the individual tracks within the group, regardless of their vertical position in the timeline.

Groups can be disabled, allowing you to change focus back to the individual tracks within them.

But when smaller groups are “nested” within a larger one, turning off the larger group does not affect

the smaller group.

In situations where an edit group contains clips of differing lengths, the group behavior still applies,

such that all edits, such as trim, cut, or paste, will follow the group at its present boundaries.

Mixing with Track Groups

When mixing with track groups, changes to one channel are simultaneously made to all others in the

group. This includes fader movements, panning, send levels, automation, and changes to the mute,

solo, and record-arm buttons.

NOTE: Plugin controls cannot be added to Mix groups.

Showing the Groups List

Clicking the Groups button in the Interface Toolbar opens and closes the Groups list. If the Track Index

or other Index tabs are already open, the Groups list will appear beneath them.

This list remains open when you close the Track Index or click one of the other Index tabs.

Groups list


Fairlight | Chapter 179 Track Groups

FAIRLIGHT

Groups List Controls

Group Name: The group name or “ID” appears in this column.

Groups Switch: Toggles all groups on or off, allowing you to switch easily from

working with groups to working with individual tracks.

Selected Checkbox: When checked, all tracks that are members of the group are

selected. If some members are selected, a hyphen is shown.

Action Icons on Hover: These icons only appear when hovering over the group

row. The Tools icon accesses the Modify Groups dialog, and the Trash icon deletes

the group.

The All Group

The All Group contains all tracks Mixer channels, making it easy to perform edit or mix tasks on all

tracks at once. This group is always present at the top of the Groups list.

The Selected Checkbox

Clicking the Selected Checkbox adds a checkmark, signifying that all tracks within the group are

selected. This makes it easy to add to a current group (shift-clicking to add more members and

using Create Group) or control the routing of all selected tracks at once by holding down the Option

(Alt Windows) keys while assigning or unassigning.

For example, let’s say we have Group 1 with six tracks and Group 2 with 10. Just click on the Selected

checkbox for Group 1, and all tracks in Group 1 are selected. Hold down Shift and click on the

checkbox next to Group 2. Now, all members of both groups are selected, and you can create a new

Group 3 that contains all members.

�A hyphen (“-“) is shown if only some tracks are selected.

�Clicking the checkbox to remove the checkmark or hyphen deactivates the group.

NOTE: The Selected checkbox operates independently of whether a group is enabled or

disabled; it’s a separate control not directly tied to grouping.

Group Key Commands

Activate or deactivate Groups using Command + num keypad 0 key (Control on Windows).

You can use Command (Control on Windows) + num keypad number 1-9 to activate or

deactivate the first nine groups.

Use Command (Control Win) + num keypad * key to toggle the All Group.


Fairlight | Chapter 179 Track Groups

FAIRLIGHT