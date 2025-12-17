---
title: "The Record Panel"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 667
---

# The Record Panel

This is where you actually run the ADR recording session you’ve set up, using the dialog cues you’ve

put into the Cue list. It presents controls for displaying and selecting which cues to record, previewing

and initiating recording, and adding metadata to rate the different takes you’ve recorded and to keep

track of which cues have been completed.

The Record panel of the ADR Interface


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

The Setup Panel

The Setup panel is where you configure your ADR session. Choose your audio input, your record track

and what tracks to monitor. Then access beeps, video streamers and onscreen text that the actors will

see on the video output display to help them keep their performance in sync.

The Setup panel of the ADR interface

For more information on using the ADR panel, see Chapter 174, “ADR (Automated Dialog

Replacement).”


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Sound Library Browser

A Sound Library panel is available from the Interface toolbar for browsing sound effects libraries

that you have available to you, on your system or on network storage you may be connected to (for

example, a SAN). It includes the capability of scanning specified file paths to catalog available sound

files and their metadata, storing this data within the currently selected project library (or another

project library that you select) to use when searching for the perfect sound effect within your library.

Once you’ve cataloged your sound effects collection, it’s easy to search for sounds, preview what’s

been found in the list, and edit the one you like best into the Timeline.

TIP: You can download the Fairlight sound library, a royalty-free collection of over

500 professionally recorded foley sounds that you can use in your own projects, which are

directly downloadable from the Sound Library panel. The Fairlight sound library features

everything from atmospheric ambient sounds to foley sounds such as foot steps, hits, effects,

and more. This free sound library is designed to work with the Fairlight FX Foley Sampler

plugin, which lets you use a MIDI keyboard to trigger sounds so they can be recorded at

precisely the right time in your program.

The Sound Library panel


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Library Controls

Clicking the Library button (to the right of the Search field) reveals a menu that lets you choose which

project library to use for searching (and cataloging) sound effects collections. Each network project

library can have a different catalog.

NOTE: The Sound Library results pane will be empty until a search is made.

The Sound Library is capable of using the Mapped Mount option in the Media Storage panel

of the Preferences, in order to access sound effects located on remote volumes using other

operating systems.

Choosing a library to search

To catalog all audio files within a given file path for searching using the Sound Library:


Using the Project Manager, create an empty network project library to store the sound

effects catalog.


Open a project, open the Edit or Fairlight pages, then open the Sound Library.


(Optional) Click the Library button (to the right of the Search field), and select the project library

you created using the dropdown menu that appears. The current project library is selected by

default. If you’re working within a local project library instead, the top compatible project library in

the list will be the default.


Do one of the following:

a)	 If you’ve not yet connected a library of sound effects, an Add Library button appears in the

center of the Sound Library. Click this button, and from the file dialog that appears, select the

top-most directory of a file path that contains sound effects; if you’ve selected a directory with

subdirectories inside, each subdirectory will be examined for content.

b)	 If you’re adding more sound effects to an existing library, then click the Option menu and

choose Add Library. From the file dialog that appears, select the top-most directory of a file

path that contains sound effects; if you’ve selected a directory with subdirectories inside, each

subdirectory will be examined for content.


Click Open.

A progress bar will show you how long the operation will take. When you’re finished, a dialog will

appear letting you know how many clips were added to the current library.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Display Controls and the Search Field

The Sound Library title bar has controls for sorting the sound effects list, showing it in List or Icon view,

and an Option menu with various other settings and commands.

Display controls let you choose how the contents

of the Sound Effects list are viewed

Underneath, a text field lets you enter search terms, while a dropdown menu to the right

lets you choose whether to search the current project library for sound effects by name,

description metadata, or all.

The Search field and Filter By menu

To search for a specific sound effect and edit it into the Timeline:

�Type a search term into the Search field. The case of search terms is ignored, except for

boolean operators.

To help you to eliminate false positives, the search field supports different kinds of searches, such as

literal searches, and/or/not boolean searches, wildcard searches, and ranges of characters.

NOTE: If you want to perform Boolean searches, the Boolean operators must be typed in all

upper caps, such as “AND,” “OR” and “NOT.” If lower case is used, “and,” “or” and “not” will be

treated as search terms but as regular words.

Or/And/Not Searches

Simply typing words separated by a space is treated as a series of OR searches for each word

independently of one another, either literally or as part of another word. For example, if you type either

of the following:

car door

car OR door

both yield the same results. Every sound effect in your library containing either the letters “car”

or “door” (or both) will appear, whether these letters appear independently, or within other words.

Results will include files such as “CarExDoorClose,” “Doormouse_Squeak,” “Carburetor dropped

on cement,” and “Carpet Shake.”


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

Using AND (it must be upper caps) lets you specify multiple criteria for a search, when each file

that’s returned should contain every word you type somewhere within, in any order. For example,

if you type:

car AND door

every sound effect in your library containing both the strings “car” and “door” will appear,

even if these words appear either singly, in combination, or within other words, such as

“NewCarDoorSlam” and “Carpet_Footsteps_Indoors,” and “GarageDoorHitsCar.”

Using NOT lets you omit sound effects that have a particular word. For example, if you type:

car NOT door

only sound effects with “car” will appear, and all sound effects with “door” will be omitted.

Literal Searches

Using quotations specifies a literal search for only the specified term, separated from other text by a

space. For example, if you type:

“cat”

every sound effect in your library with the standalone word “cat” appears. Sound effects with

“cats” and “caterpillar” will be omitted. Results will include “Space cat drone” or “Cat meowing.”

Wildcard and Range Searches

The * (asterisk) specifies a wildcard search of any number of characters. Adding an * between two

search terms identifies any sound effect with the two search terms connected by any number or

combination of characters with no spaces (even no characters). For example, if you type:

close*door

results include “Door-Wood Cheap-Wooden-Closet-Door-Kick-In-Flimsy-Rattle,”

“ElevatorCabinCloseDoor,” and “LatchSwingCloseSqueakDoorSecur.” If you instead type:

door*close

results include “DoorHvyMetalCloseSlam,” “DoorLidWoodenChestCloseAntique,” and

“ElevatorDoorCloseSlam.” If instead you type:

c*r

results include “lectrohummin,” “KiaShumaEXTBootCloseTrunkaka,” and “Ambience with

Piana, Louder.”

The ? (question mark) specifies wildcard search specifying only a single character. The number

of question marks you type specifies how many characters of wildcard searching you want to

perform. For example, if you type:

door?close

you may get no results at all, unless you have a sound effect named “door-close.” However,

if you type:

door????close

results include “DoorWoodClose” since the word wood is four letters, matching the number of

wildcard letters you’ve specified.


Fairlight | Chapter 170 Using the Fairlight Page

FAIRLIGHT

TIP: Typing “***” will show all of the files in your Sound Library