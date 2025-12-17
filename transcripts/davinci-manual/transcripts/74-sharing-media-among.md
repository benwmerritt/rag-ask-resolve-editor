---
title: "Sharing Media Among"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 74
---

# Sharing Media Among

Projects Using Power Bins

Power Bins provide a way of importing and organizing media that you want to be available to all

projects in DaVinci Resolve. Power Bins reside in a separate area of the Media Pool, with resizable

dividers separating them from both the ordinary bins and Smart Bins areas. Power Bins are

hierarchical, just like regular bins, and you can nest as many as you like, one inside another.

Like regular bins, Power Bins must be manually created by right-clicking within the Power Bins area

and choosing Add Bin. The difference is that whatever clips you import into Power Bins are shared

among all projects in a single-user installation, or all projects belonging to a particular user in a multi-

user installation. In this way, they’re similar to Power Grades in the gallery of the Color page. This

makes Power Bins ideal for storing shared media that’s re-used often, such as stock video, sound

effects, stills, and things like company slates and network graphics and animations that go into every

show of a series.

The Power Bins area of the Bin list


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Power Bins are created and used like any other bin, using the procedures

described previously.

To show or hide the Power Bin area of the Bin list:

Choose Show Power Bins from the Media Pool option menu to toggle the visibility of all power

bins on and off.

Automated Organization Using Smart Bins

A completely automated way of organizing media in the Media Pool is to use Smart Bins that are either

automatically or manually created, in order to collect all clips and timelines in the Media Pool that have

commonalities based on any of the intrinsic or user-editable metadata that’s available in the Metadata

Editor and Media Pool. If you’re familiar with the Color page, Smart Bins work much the same way as

Smart Filters, and they’re created and edited using much the same procedures.

For more information about Smart Filters, see Chapter 124, “Using the Color Page.”

Smart Bins are incredibly flexible. Using one or more metadata-based rules, they can be as simple

or sophisticated as you require. They’re even capable of using multiple groups of multiple rules for

situations where you need to gather clips that match all of one set of criteria, but only one of a second

set of criteria. In this way, you can use Smart Bins to solve a wide variety of organizational needs as

you edit your program.

Smart Bins Are Only As Good As Your Metadata

It’s important to point out, however, that as much intrinsic metadata is available to every clip in DaVinci

Resolve automatically (clip properties such as frame rate, frame size, codec, file name, and so on), the

more time you take entering extra metadata in the Metadata Editor to prepare your project for editing

and grading, the more powerful Smart Bins can be in helping you to sift and sort through the contents

of a program you’re grading. Examples of metadata entry that will guarantee immediate benefits from

Smart Bins include the entry of scene, shot, and take information, keywords identifying key descriptors

(day and night, interior and exterior, framing, and so on), and using Face Detection to assign character

names. These categories of metadata can be used for the automatic creation of Smart Bins, but they

can also be used in combination when manually creating Smart Bins that are even more specific.

Imagine being able to gather all the clips in a particular scene, find all the interview clips for a particular

subject, or find all the edited timelines corresponding to a particular name, all by simply selecting a

Smart Bin that automatically examines the current contents of the Media Pool. If you or an assistant can

take the time to enter metadata for the source material in a project that identifies these characteristics,

you’ll be able to work even more quickly to find the clips you need for any given situation.

Smart Bins Update Their Contents Dynamically

Smart Bins are always dynamically up to date and include whatever new media is added to the Media

Pool. This makes it easy to stay organized, even when working on projects where new media is being

added to the Media Pool every day, such as when editing during a shoot. By using metadata entered

either in-camera, by the DIT or media wrangler managing ingest, or by an Assistant Editor who’s

working with you, Smart Bins will automatically include all clips in the Media Pool that have matching

criteria, whether they were added a month ago or a minute ago.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Automatic Smart Bin Creation

The process of adding metadata to your clips can be used for the automatic creation of sets of “Smart

Categories,” which are Smart Bins that are generated and organized by the presence of specific

categories of metadata and appear in the Smart Bins section of the Media Pool sidebar. To enable or

disable this behavior, open the Editing panel of the User Preferences, and use the checkboxes in the

Automatic Smart Bins group to choose which metadata automatically creates Smart Bins.

Preferences governing what metadata can automatically create Smart Bins

Metadata capable of creating Smart Bins include:

�Clip Keywords

�Marker Keywords

�People Keywords (added via People Detection)

�Scene metadata

�Shot metadata

These categories are hierarchically organized, with each category closed by default to save space.

Click the disclosure triangle of any category to reveal all Keyword, People, Scene, or Shot Smart Bins

that are available in the current project. Selecting the Smart Category’s top bin lets you see every clip

referenced by every Smart Bin inside of it, whereas selecting individual Smart Bins shows you only the

clips referenced by that Smart Bin.

A Smart Category seen in the Smart Bins

area of the Media Pool sidebar

Drag and Drop Clips to Assign Automatic Smart Bin Properties

Metadata entry does not need to be a one way process, starting with typing in the metadata editor.

For certain Automatic Smart Bin categories (keywords, shot, and scene), you can drag multiple clips

from the Media Pool on top of an existing smart bin to assign the properties of that bin to all the

clips at once.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

To automatically assign Smart Bin Properties to a range of clips:


Create a Smart Bin in one of the following categories: Keywords, Shot, or Scene.


Select all of the clips that you want to apply the Smart Bin property to.


Drag those clips from the Media Pool and drop them on top of the Smart Bin.

For example, you could make a smart bin with the Keyword: “Sunset.” That bin would

automatically show up under the Keywords category in the Smart Bins. Then you could select

all the sunset shots in your Media Pool, and drag them on top of that bin to apply the “sunset”

keyword to all the clips at the same time.

NOTE: Dragging and dropping clips to assign Smart Bin properties only works with the

Automatic Smart Bin Keywords, Shot, or Scene categories. Dragging clips to any other Smart

Bin will have no effect.

Manual Smart Bin Creation

It’s easy to manually create Smart Bins with customized rules to filter very specific collections of media

and timelines that you want to use.

To show or hide the Smart Bin area of the Bin list:

�Choose Show Smart Bins from the Media Pool option menu to toggle the visibility of

all Smart Bins on and off.

To create a Smart Bin:


If necessary, open the Bin list, choose Show Smart Bins from the Media Pool option menu, then

right-click anywhere in the background of the Smart Bin area of the Bin list, and choose Create

Smart Bin.


In the Create Smart Bin dialog, enter a name for the filter, and use the following controls to create

one or more filter criteria (you can have as many filter criteria as you like):

The Create Smart Bin dialog

�Show in all projects checkbox: Lets you create a persistent Smart Bin that appears in all projects

in your project library. Smart Bins created this way will be found in the User Smart Bins folder

inside every project’s Smart Bin area in the Media Pool.

�Match options: For multi-criteria filtering, choosing All ensures that every single criteria you

specify is met for a clip to be filtered. Choosing Any means that if only one out of several criteria is

met, that clip will be filtered.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

�Filter criteria enable checkbox: Lets you enable or disable any criteria without having to delete it.

�Metadata category drop-down: Lets you choose which category of metadata you want to select

a criteria from. Each category of metadata that’s available in the Metadata Editor is available from

this drop-down menu. Additionally, Color Timeline Properties (containing many properties unique

to the Color page timeline) and Media Pool Properties (containing every column in the Media Pool)

provide access to additional metadata you can use for filtering.

�Metadata type drop-down: For choosing which exact type of metadata to use, of the options

available in the selected metadata category.

�Metadata criteria drop-down: Lets you choose the criteria by which to filter, depending on

the metadata you’ve selected. Options include “true/false,” integer ranges, date ranges, string

searches, flag and marker colors, et cetera.

�Add filter criteria button: Lets you add additional criteria to create multi-criteria filters. You could

use multiple criteria to, for example, find all exterior clips, that also contain the keyword “Sunset,”

that aren’t closeups, in order to find all the exterior long and medium shots in sunset lighting.

Additionally, if you Option-click this button, you can add a nested match option in order to create

even more sophisticated filters, such as when the filter must match all of one set of criteria, and

any of another set of criteria.

A complicated Smart Bin with multiple criteria and a second match option setting

As you’re editing the filter criteria, the thumbnail timeline automatically updates to show you how

the Smart Bin you’re creating is working.


When you’re done editing the filter criteria, click Create Smart Bin. The resulting Smart Bin appears

in the Smart Bin area of the Bin list, at the left of the Media Pool’s browser area.

Once you’ve created a Smart Bin, it appears in the lower half of the Media Pool’s Bin list, alongside

every other Smart Bin in that project. This keeps them organized, separate from the manually created

bin shown above.

All Smart Bins appear together at the

bottom of the Media Pool’s Bin list


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Once you’ve created a Smart Bin, you can re-edit it whenever the situation requires.

Methods of modifying existing Smart Bins:

�To rename a Smart Bin: Right-click the Smart Bin you want to rename, choose Rename from the

contextual menu, enter a new name, and press Return.

�To edit a Smart Bin: Double-click the Smart Bin, then edit the filter criteria, and click OK.

�To duplicate a Smart Bin: Right-click any Smart Bin and choose Duplicate from the contextual

menu. This is a good way to create multiple variations of a Smart Bin that you created with

complex rules, where you need to create variations by modifying those rules without needing to

reinvent the wheel each time.

�To delete a Smart Bin: Right-click the Smart Bin you want to delete, choose Delete Smart Bin from

the contextual menu, and click Delete in the warning dialog. Deleting a Smart Bin does not delete

any gathered media associated with that bin.

Smart Bins Work Better With Metadata

Keep in mind that the more metadata you associate with each clip, the more methods

you have at your disposal for creating custom Smart Bins (for editing) and Smart Filters

(for grading) with which to zero in on the clips you need for any given situation. This will not

only make it easier to find what you need, but it’ll help you to work faster. At the very least,

it would be valuable for you to use the Metadata Editor to add information to each clip such

as a Description, Shot and Scene designations, take information, and possibly some useful

keywords such as character names, shot framing, interior or exterior keywords, and so on.

For example, if you’ve entered enough metadata, then you can create multi-criteria Smart Bins

or Smart Filters that let you find the equivalent of “every close-up of Sally inside the diner,”

or “every long shot of Antonio outside in the parking lot.” In a documentary, you could easily

isolate “every interview shot of Louis from camera 1,” or “every B-roll clip with Robyn.” All of

this will help you find media faster for editing, or quickly isolate similar clips that you need to

match together for grading.

For more information about using the Metadata Editor, see Chapter 19, “Using Clip Metadata.”