---
title: "Searching for Keyboard Shortcuts"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 24
---

# Searching for Keyboard Shortcuts

Whether you’re looking to see what keyboard shortcuts are available or looking for a particular

command you want to customize, a Search field above the Commands list is available for searching

whichever group of commands you want (including All Commands).

To search for specific keyboard shortcuts:


Choose DaVinci Resolve > Keyboard Customization.


Choose a command group from the Commands list to search within. If you want to search all of

DaVinci Resolve, choose “All Commands.”


Type a term into the Search field, and the Command/Keystroke list will update to show whatever

commands match the search criteria you’ve entered.

Selecting “All Commands” and searching for every keyboard

shortcut corresponding to the word “ripple”


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

Managing Keyboard Mappings

DaVinci Resolve provides the following methods for creating and managing keyboard mappings in the

Option menu of the Keyboard Customization menu:

The Option menu of the Keyboard Customization window

lets you export, import, and delete keyboard mappings

�To create a new keyboard mapping: Choose a keyboard mapping from the drop-down to use as

your starting point, choose Save As New Preset from the Keyboard Customization Option menu,

then enter a preset name in the dialog, and click OK. That preset will now appear in the preset

drop-down menu.

�To export a keyboard shortcut file for use by another DaVinci Resolve workstation: Choose a

preset from the Export Preset submenu of the Keyboard Customization Option menu, then choose

a name and a location for the new file, and click Save.

�To import a keyboard shortcut file: Choose Import Preset from the Keyboard Customization

Option menu, choose a DaVinci Resolve keyboard shortcut file, and click Open.

�To delete a keyboard mapping: Choose a keyboard mapping preset you want to delete, then click

the trash can button.

Remapping a Command to One or More Keys

Changing the keyboard mapping for any given command is easy. You can even map a single

command to multiple keys, if necessary. In DaVinci Resolve, actions can be application-wide or

specific to Media Pool, or Timeline, or other panels. The right column in the key customization dialog

shows application-level and panel-level actions. When a panel is in focus, hotkeys prioritize panel-

local actions. This allows you to reuse the same key shortcut in the application level and within each

panel at the same time.

To change the keyboard shortcut for a particular command:


Find the command you want to remap in the Commands list by selecting a category. If necessary,

use the Search field. Whether a command is mapped generally to the entire application or

specifically to a particular panel depends on what you’ve selected from the list.

a)	 If you want the keyboard character you plan to map to work application-wide, choose a menu

name from underneath the Application category of the Commands list. Each menu shows all

commands associated with it and can be individually searched.

b)	 If you want the keyboard character you plan to map to this command to be specific to a

particular panel, then choose one from the Panels category underneath. Each panel shows all

commands associated with it and can be individually searched.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA


Click within the Keystroke column of the list, to the right of the command, and when a selection

appears type a new character using any combination of modifier keys you like.

Clicking to select a keyboard shortcut you want to modify

Please note that if you remap a key that was already assigned to another command, you’ll see a

warning that the key you’re about to remap is already assigned to another command, giving you a

chance to cancel and change key assignments if you like.

The warning you see if you try to map the same key to multiple commands

You can override the warning and make the assignment, but having the same character or

combination applied to multiple commands can cause problems, so a warning badge appears

next to affected commands. Clicking on this badge makes it easy to see where the duplicate is by

highlighting the keys on the keyboard, so you can remap one or the other command as necessary.

To resolve a shortcut conflict:

�Click the yellow warning icon next to the action. This shows all actions for that hotkey

in the left panel.

�Click on the other conflicting actions at the same level to reveal them in the right pane.

�Change or unset these values so as not to conflict with your new key assignment.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA


(Optional) You also have the option of assigning multiple keyboard shortcuts to a single command.

For example, if you want to use keys on the numeric keypad of an extended keyboard in addition

to other keys for a particular command, you can now set this up by clicking the “plus” button to the

right of a currently assigned keyboard shortcut. This makes another highlight appear, within which

you can type any secondary character or combination you like to make the additional assignment.

You can do this as many times as you like. When you’re done, all keyboard shortcuts applied to

that command appear, separated by commas.

You can map multiple keys to the same command, if necessary


When you’re finished changing keyboard shortcuts, click the Save button at the bottom right of the

Keyboard Mapping list, and then click Close to close the window.

For example, if you set ‘Option-G’ to:

a)	 The Media Pool-specific Clip Attributes,

b)	 The application-wide Mark > Add Flag > Green to ‘Option-G’.

When you are focused on the Media Pool, you cannot add green flags with a hotkey. You will need

to manually add them via the Mark menu.

In addition, the application-wide Color > Nodes > Add serial node with polygon power window

also has the same hotkey (Option-G), so action b will cause the the key customization dialog to

show a warning with the conflicting action name and display an icon on both actions.

If you save this state as a preset (with conflicts), DaVinci Resolve will still try to parse your shortcuts

logically. For example, on the Edit and Fairlight timelines, Option-G adds a green flag (as color

node actions are not applicable). But in the Color page, Option-G can refer to both actions and the

user needs to resolve the conflict to make the action work correctly.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA

DaVinci Resolve Extras Download Manager

As DaVinci Resolve evolves to incorporate more AI-based models, there is a tradeoff in application file

size. These AI models tend to be large datasets that not all users will want or need to use. To help with

this decision, DaVinci Resolve has the Extras Download Manager, allowing you to pick and choose

which optional functionality you want to add to DaVinci Resolve.

The Extras Download Manager can be found at DaVinci Resolve > Extras Download Manager.

The Extras Download Manager

To use the Extras Download Manager, simply view the packages available and select download.

You can remove a package in the same interface by clicking on the trashcan icon next to the package

name. Downloads will happen in the background while you continue to work. From time to time these

packages will be updated, and you will be notified here if your current package is out of date.

Currently, the Download Manager contains packages for AI Voice Training and Extended AI

Transcription Support Languages.


Setup and Workflows | Chapter 4 System and User Preferences

MEDIA