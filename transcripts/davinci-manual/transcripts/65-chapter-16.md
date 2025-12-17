---
title: "Chapter 16"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 65
---

# Chapter 16

Using Variables

and Keywords

This chapter describes how to use metadata variables and keywords to help you

manage your clips.

Contents

Using Metadata Variables��������������������������������������������������������������������������������������������������������������������������������������������������������������� 344

Where Variables Can Be Used������������������������������������������������������������������������������������������������������������������������������������������������������� 344

How to Edit Metadata Variables���������������������������������������������������������������������������������������������������������������������������������������������������� 344

Using Keywords������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 345

Keyword Dictionary����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 346

Assign and Apply Favorite Keywords to Clips and Markers������������������������������������������������������������������������������������������ 348


Setup and Workflows | Chapter 16 Using Variables and Keywords

MEDIA

Using Metadata Variables

If you’re an enthusiastic user of clip metadata (and you should be), you can use “metadata variables”

that you can add into supported text fields that let you reference other metadata for that clip. For

example, you could add the combination of variables and text seen in the following screenshot.

Variables, once they’ve been entered, are represented as graphical tags shown with a background,

while regular text characters that you enter appear before and after these tags.

Variables and text characters entered to create a display name based on a clip’s metadata

As a result, that clip would display “12_A_3” as its name if scene “12,” shot “A,” and take “3” were

its metadata. When you do this, you can freely mix metadata variables with other characters (the

underscore, as in the example above) to help format the metadata to make it even more readable.

Be aware that, for clips where a referenced metadata field is empty, no characters appear for that

corresponding metadata variable’s tag wherever it happens to be used.

Where Variables Can Be Used

Metadata variables are extremely flexible, and can be used to procedurally add metadata to several

functions in DaVinci Resolve. Here’s a partial list of where you can use variables.

�Clip names: You can use variables in the Clip Name column of the Media Pool in List view, or in

the Clip Name field of the Clip Attributes window’s Name panel, to use each clip’s metadata to

generate a more readable and useful display name.

�Other metadata fields in the Metadata Editor: You can use variables to reference metadata in

other fields.

�Automatic labeling of stills in the Gallery: You can choose an option from the Color group in the

General Options panel of the Project Settings to “Automatically label Gallery stills” in the Gallery,

and you can use variables to do so.

�Custom text in the Data Burn palette: You can use variables to automatically populate metadata

in different combinations as a window burn.

�The Filename field of the Render Settings in the Deliver page: Using variables, you can

automatically set the name of rendered clips to follow any metadata that’s associated with a

timeline or individual clip. This is especially useful when you want to generate specific file names

when rendering individual source clips.

How to Edit Metadata Variables

Every single item of metadata that’s available in the Metadata Editor can be used as a variable, and

several other clip and timeline properties such as the version name of a clip’s grade, a clip’s EDL event

number, and that clip’s timeline index number can be also referenced via variables.


Setup and Workflows | Chapter 16 Using Variables and Keywords

MEDIA

To add a variable to a text field that supports the use of variables:


Type the percentage sign (%) and a scrolling list appears showing all variables that are available.


To find a specific variable quickly, start typing that variable’s name and this list automatically filters

itself to show only variables that contain the characters you’ve just typed.


Choose which variable you want to use using the Up and Down Arrow keys, and press Return to

choose that variable to add.

As soon as you add one or more metadata variables to a field and press Return, the string is replaced

by its corresponding text. To re-edit the metadata string, simply click within that field to edit it, and the

metadata variables will reappear as the graphical tags that they are.

The variable list that appears when you type the % character

To remove a metadata variable:

�Click within a field using variables to begin editing it, click a variable to select it, and press Delete.

Using Keywords

While most metadata in the Metadata Editor is edited via text fields, checkboxes, or multiple button

selections (such as Flags and Clip Color), the Keyword field is unique in that it uses a graphical “tag”

based method of data entry. The purpose of this is to facilitate consistency with keyword spelling by

making it easy to reference both a built-in list of standardized keywords, as well as other keywords that

you’ve already entered to other clips.

Once added, keywords are incredibly useful for facilitating searching and sorting in the Media Pool,

for creating Smart Bins in the Media and Edit pages, and for use in Smart Filters on the Color page.

Reaping these benefits by adding and editing keywords is simple and works similarly to the method of

entering metadata variables that’s described above.

To add a keyword:


Select one or more clips, then click in the Keyword field of the Metadata Editor, and begin typing

the keyword you want to use. As you begin typing, a scrolling list appears showing all keywords

that are available using the string of characters you’ve just typed.


To find a specific keyword in the list, start typing that keyword’s name and this list automatically

filters itself to show only keywords that contain the characters you’ve just typed. Choose which

keyword you want to use in the list using the Up and Down Arrow keys, and press Return to

choose that keyword to add.


Setup and Workflows | Chapter 16 Using Variables and Keywords

MEDIA


If you selected multiple clips, don’t forget to click Save or you’ll lose your changes. If you only

selected a single clip, your changes will be saved automatically.

The keyword list that appears when

you type within the Keyword field

As soon as you add one or more keywords, they appear as a graphical tag. To re-edit any keyword,

simply click anywhere within the Keyword field to edit it.

To edit a keyword:

�Double-click any keyword to make it editable, then edit it as you would any other piece of text,

and press Return to make it a graphical keyword tag again.

To remove a keyword:

�Click any keyword to select it, and press Delete.

Keyword Dictionary

DaVinci Resolve comes with a suggested set of built in keywords, but by using the Keyword

Dictionary, you can add a new set of keywords or delete previously entered keywords that no longer

are applicable to your project.

To access the Keyword Dictionary go to Workspace > Keyword Dictionary.

The Keyword Dictionary presents a list of all currently suggested and assigned keywords, a search

field, and the ability to add your own keywords to the list.

Any keyword that you add will be added to both the Project and User keyword dictionaries.

�To switch between Keyword Dictionaries, select Project or User from the menu on the toolbar.

The User Dictionary

The User Dictionary shows keywords that will be remembered and suggested for autocomplete across

all projects in this library. The User Dictionary is always based on the last inputs entered.

The Project Dictionary

The Project Dictionary shows keywords that will be remembered and suggested for autocomplete

for only this project.

You can also Import and Export keywords in .txt format into and out of the Project Dictionary.

This lets you prepare a list of custom keywords in any text editor and import them all at once into the

Keyword Dictionary.


Setup and Workflows | Chapter 16 Using Variables and Keywords

MEDIA

The Keyword Dictionary

To Import a .txt File into the Keyword Dictionary:


Create a plain text file (.txt) of your keywords, either one word per line or as comma-

separated values.


In the Keyword Dictionary Option Menu (three dots), select Import Project Dictionary.


Navigate to your .txt file in the file browser and press Open.

You can also export any custom keywords in the Keyword Dictionary to a plain text file (.txt) of your

keywords, one word per line.

To Export a .txt File from the Keyword Dictionary:


In the Keyword Dictionary Option Menu (three dots), select Export Project Dictionary.


Navigate to where to want your .txt file to be saved in the file browser and press Save.

You can add your own keywords, one at a time as needed, to the Keyword Dictionary.

To Add a Keyword to the Keyword Dictionary:


Press the Add Keyword button.


Type in the new keyword into the text field and hit return.

The new keyword is initially added to the bottom of the Keyword list for easy access, but

once the Keyword Dictionary has been closed and reopened, the new keyword will appear in

alphabetical order.

You can also remove a keyword from the Keyword list if it is no longer applicable, or misspelled.


Setup and Workflows | Chapter 16 Using Variables and Keywords

MEDIA

To Delete a Keyword from the Keyword Dictionary:


Hover the pointer over the keyword that you want to delete.


Press the trashcan icon to the right of the keyword.

The keyword will instantly be removed from the list, and this action is not undoable. Please note

that the default keyword set that comes with DaVinci Resolve cannot be deleted.