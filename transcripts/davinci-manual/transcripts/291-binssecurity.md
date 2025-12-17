---
title: "Bins/Security"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 291
---

# Bins/Security

Bins preferences are only available in Fusion Studio. These preferences are used to manage the Bin

users and their permissions.

The Bins Security preferences

Users List

The Users List is a list of the users and their permissions. You can select one of the entries to edit their

settings using the User and Password edit boxes.

�Add: The Add button is used to add a new user to the list by entering a username and password.

�Remove: Click this button to remove the selected entry.

User

This editable field shows the username for the selected Bin Server item. If the username is unknown,

try “Guest” with no password.

Password

Use this field to enter the password for the Bin user entered in the Users list.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Permissions

The administrator can set up different permission types for users.

�Read: This will allow the user to have read-only permission for the bins.

�Create: This will allow the user to create new bins.

�Admin: This gives the user full control over the bins system.

�Modify: This allows the user to modify existing bins.

�Delete: This allows the user to remove bins.

Bins/Server

These preferences are used to add Bin Servers to the list of bins Fusion will display in the Bins dialog.

The Bin Servers preferences

Servers

This dialog lists the servers that are currently in the connection list. You can select one of the entries

to edit its settings.

�Add: Use this button to add a new server to the list.

�Remove: Click this button to remove the selected entry.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Server

This editable field shows the name or IP address of the server for the selected entry in the list.

User

This editable dialog shows the username for the selected Bin Server item.

Password

Use this field to enter the password for the server entered in the Server list.

Library

The Library field lets you name the bins. If you wanted to create a bin for individual projects, you would

name it in the Library field and each project would gets its own bin.

Application

The Application field allows larger studios to specify some other program to serve out the Bin requests.

Bins/Settings

These preferences are used to control the default behavior of bins.

The Bins Settings preferences


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Stamp Quality

The Stamp Quality is a percentage slider that determines the compression ratio used for Stamp

thumbnail creation. Higher values offer better quality but take up more space.

Stamp Format

This drop-down list determines whether the Stamp thumbnails will be saved as compressed or

uncompressed.

Options

�Open Bins on Startup: When Open Bins on Startup is checked, the bins will open automatically

when Fusion is launched.

�Checker Underlay: When the Checker Underlay is enabled, a checkerboard background is used

for clips with alpha channels. When disabled, a gray background matching the Bin window is used

as the clip’s background.

EDL Import

The EDL Import options are used to determine how compositions are created from imported

CMX‑formatted EDL files.

The EDL Import preferences


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Flow Format

This drop-down menu provides three options that determine how the node tree is constructed for the

imported EDL file.

�Loader Per Clip: A Loader will be created for each clip in the EDL file.

�A-B Roll: A node tree with a Dissolve tool will be created automatically.

�Loader Per Transition: A Loader with a Clip list will be created, representing the imported EDL list.

Use Shot Names

When checked, shot names stored in the EDL file are used to locate the footage.

Customization

The following section covers the customization of preferences that are not technically part of the

Preferences window. Using Fusion Studio’s Hotkey Manager window, you can customize the keyboard

shortcuts, making the entire process of working in Fusion not only faster but potentially more familiar if

you are migrating from another software application. You can also customize Fusion with environment

variables to switch between different preferences files, allowing different working setups based on

different users or job types. Both of these customization options are only available in Fusion Studio.

Shortcuts Customization

Keyboard shortcuts can be customized in Fusion Studio. You can access the Hotkey Manager by

choosing Customize HotKeys from the View menu.

The Hotkey Manager

Fusion has active windows to focus attention on those areas of the interface, like the Node Editor,

the viewers, and the Inspector. When selected, a gray border line will outline that section. The

shortcuts for those sections will work only if the region is active. For example, Command-F in the


Fusion Fundamentals | Chapter 75 Preferences

FUSION

View will scale the image to fit the view area; in the Flow view, Command-F will open the Find tool

dialog; and in the Spline editor, it will fit the splines to the window.

On the right is a hierarchy tree of each section of Fusion and a list of currently set hotkeys. By

choosing New or Edit, another dialog will appear, which will give specific control over that hotkey.

The Hotkey Editor

Creating a new keyframe will give you the key combo to press, and this Edit Hotkey dialog will

appear where the Action can be defined at top right: pressed, repeated, or released. The Name and

abbreviated Short Name can be set, as can the Arguments of the action.