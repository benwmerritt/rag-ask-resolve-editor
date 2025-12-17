---
title: "Memory"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 287
---

# Memory

The Memory preferences are only available in Fusion Studio. To control Fusion’s memory when using

the Fusion page in DaVinci Resolve, open DaVinci Resolve’s Memory and GPU preferences.

Occasionally, it will be necessary to adjust the Memory preferences in order to make the best use

of available memory on the computer. For example, some people prefer a higher cache memory

for faster interactive work, but for final renders the cache memory is often reduced, so there’s more

memory available for simultaneous processing of tools or multiple frames being rendered at once.

Caching Limits

The Caching Limits include options for Fusion’s RAM cache operation. Here, you can determine how

much RAM is allocated to the RAM cache for playing back comps in the viewer.

�Limit Caching To: This slider is used to set the percentage of available memory used for the

interactive tool cache. Available memory refers to the amount of memory installed in the computer.

When the interactive cache reaches the limit defined in this setting, it starts to remove lower

priority frames in the cache to clear space for new frames.

�Automatically Adjust In Low Memory Situations: This checkbox will set the caching to adjust

when memory is low. The console will display any cache purges.

�Leave At Least X MBytes: This setting is used to set the hard limit for memory usage. No matter

what the setting of the Cache Limit, this setting determines the amount of physical memory

available for use by other applications. Normally, this value should not be smaller than 25 MBytes.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

The Memory preferences

Interactive Render

The Interactive Render option allows you to optimize Fusion’s processing based on the amount of

RAM you have installed in your system.

�Simultaneous Branching: When checked, more than one tool will be processed at the same time.

Disable this checkbox if you are running out of memory frequently.

Final Render

These settings apply to memory usage during a rendering session, either preview or final, with no

effect during an interactive session.

�Render Slider: This slider adjusts the number of frames that are rendered at the same time.

�Simultaneous Branching: When checked, more than one branch of a node tree will be

rendered at the same time. If you are running low on memory, turn this off to increase

rendering performance.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Network

The Network preferences are only available in Fusion Studio. These preferences are used to set

up and control network rendering in Fusion Studio. The majority of settings are found in the Render

Manager dialog.

The Network preferences

Submit Network Render Compositions

In these fields, you enter the Master Name and IP address of the computer that will manage all

network renders sent from this machine. If a standalone render master is in use on the network, these

fields may be pre-filled and may not be editable. This is done to prevent multiple unauthorized render

masters from being created by each person in a facility.

To re-enable editing of the master name and IP, create the environment variable FUSION_

NO_ MANAGER and set the value to True. Check your operating system user guide for how to

create environment variables.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

General

The General preferences are designed with the most used options at the top in the General section.

These options determine in what capacity the system is used during network rendering.

�Make This Machine a Render Master: When enabled, Fusion will accept network render

compositions from other computers and manage the render. It does not necessarily mean that this

computer will be directly involved in the render, but it will submit the job to the render nodes listed

in the Render Manager dialog.

�Allows This Machine to Be Used as a Network Slave: When enabled, this computer can be used

as a Render node and will accept compositions for network rendering. Deselect it to prevent other

people from submitting compositions to render on this computer.

�Render on All Available Machines: Enable this checkbox to ignore groups and priorities

configured in the Render Manager. Compositions submitted from this computer for network

rendering will always be assigned to every available slave.

Email Notification

You can use the Email Notification section to set up who gets notified with status updates regarding

the render jobs and the network.

�Notify Options: These checkboxes cause emails to be sent when certain render events take

place. The available events are Queue Completion, Job Done, and Job Failure.

�Send Email to: Enter the address or addresses to which notifications should be sent. You separate

multiple addresses with a semicolon.

�Override Sender Address: Enter an email address that will be used as the sender address. If this

option is not selected, no sender address is used, which may cause some spam filters to prevent

the message from being delivered to the recipient.

Server Settings

This section covers Clustering and Network Rendering.

For more information on these settings and clustering, see Chapter 66, “Rendering Using

Saver Nodes,” in the DaVinci Resolve Reference Manual or Chapter 4 in the Fusion

Reference Manual.

Path Maps

Path Maps are virtual paths used to replace segments of file paths with variables. For example, define

the path ‘movie_x’ as actually being in X\Shows\Movie_X. Using this example, Fusion would understand

the path ‘movie_x\scene_5\ scan.000.cin’ as actually being X:\Shows\ Movie_X\scene_5\scan.000.cin.

For Fusion Studio, there are two main advantages to virtual path maps instead of actual file paths. One

is that you can easily change the path to media connected to Loaders (for example, when moving a

comp from one drive to another), without needing to make any changes in the composition. The other

advantage is when network rendering, you can bypass the different OS filename conventions.

�Enable Reverse Mapping of Paths Preferences: This checkbox is at the top of the Path Map

settings. When enabled, Fusion uses the built-in path maps for entries in the path’s settings

when applying mapping to existing filenames. The main benefit is for Fusion Studio. Enabling

this checkbox causes Loaders to automatically use paths relative to the location of the saved

composition when they are added to the Node Editor.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

For more information on using relative paths for Loaders, see Chapter 105, “I/O Nodes,” in the

DaVinci Resolve Reference Manual or Chapter 45 in the Fusion Reference Manual.

As with other preferences in Fusion Studio, paths maps are available in both Global and Composition

preferences. Global preferences are applied to all new compositions, while Composition path maps

are only saved with the current composition. Composition path maps will override Global path maps

with the same name.

The Path Map preferences

The Global paths maps are divided into three sections:

�System Path Maps: The operating system determines system path maps, and they define Fusion’s

global locations. You can override specific System path maps using the Defaults or current

Composition Path Map settings. If you change your mind at a later time, you are always able to

return to Fusion’s “factory” defaults using the System path maps. There are several top-level path

maps established in the System Path Map settings.

AllData: The folder where Fusion saves all shared application data.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

AllDocs: The folder where Fusion saves the public/shared document folder.

AllLUTs: The nested LUTs path in the Defaults section, where Fusion saves LUTs.

Fusion: The folder where Fusion Studio app is installed. For example, if you open Fusion from  C:\

Program Files\Fusion, then the path Fusion:\Help refers to C:\Program Files\Fusion\Help. If you

instead used a copy of Fusion found in \\post-server\fusion\16, then Fusion:\Help would expand to

\\post-server\fusion\16\Help.

FusionLibs: The Fusion libraries used for the application.

Profile: The folder where default Fusion preferences file is saved.

Profiles: The folder where Fusion individual user preferences are saved.

Programs: The location of Fusion Studio or DaVinci Resolve.

SystemFonts: The folder where the OS saves fonts that appear for Text+ and Text 3D nodes.

Temp: The system’s temporary folder.

UserData: The folder where Fusion saves all user-specific miscellaneous roaming data.

The individual elements included in the roaming data are listed in the Default Path Maps section.

For Fusion Studio on Windows, this is “C:\Users\username\AppData\Roaming\”. On Linux, this

will be “$HOME/Blackmagic/Fusion”. On macOS, this is “Users/UserName/Library/Application

Support/Blackmagic Design/Fusion”.

UserDocs: The folder where Fusion saves the user’s document folders.

�Default Path Maps: The Defaults are user-editable path maps. They can reference the System

paths, as part of their paths. For instance. the Temp folder is defined in the System path and used

by the Default DiskCache path map to refine the nested location (Temp:DiskCache). Default path

maps can also redirect paths without using the Global System path maps. After you change a

Default, the updated setting can be selected in the Preferences window, and a Reset button at the

bottom of the Preferences window will return the modified setting to the System default.

AutoSaves: This setting determines the Fusion Comp AutoSave document’s location, set in the

Fusion General preferences.

Bins: Sets the location of Fusion Studio bins. Since the bins use pointers to the content, the

content is not saved with the bin. Only the metadata and pointers are saved in the bins.

Brushes: Points Fusion to the folder that contains custom paintbrushes.

Comps: The folder where Fusion Studio compositions are saved. On macOS or Windows, the

default location is in Users/YourUserName/Documents/Blackmagic Design/Fusion.

Config: Stores Configuration files used by Fusion Studio during its operation.

Defaults: Identifies the location of node default settings so they can be restored if overwritten.

DiskCache: Sets the location for files written to disk when using the Cache to Disk feature. This

location can be overridden in the Cache to Disk window.

Edit templates: The location where  Fusion macros are saved in order to appear as templates in

the DaVinci Resolve Effects Library.

Filters: Points to a folder containing Convolution filters like sharpen, which can be used for the

Custom Filter node.

Fonts: The default path map for Fonts points to the operating system fonts folders. Changing this

will change the fonts that are available in the Text+ or Text 3D nodes as well as any Fusion Title

Template. In DaVinci Resolve. This path map does not affect the five additional Edit page titles

(L Lower 3rd, R Lower 3rd, M Lower 3rd, Scroll, and Text.)

Fuses: Points to a folder containing Fusion Fuses plugins.

FusionTemplates: Location where Fusion macros are saved in order to appear as templates in

Fusion’s Effects Library.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Guides: Location where custom viewer guide overlays are stored.

Help: Identifies where Fusion Studio PDF files are located.

Layouts: Location where Fusion Studio custom window layouts are saved.

Libraries: Points to a support folder where custom Effects Library items can be stored.

LoaderCache: The Fusion Studio Loader preferences allow the Loader to cache when

reading from a slow network. This path map point to the local drive location for that cache.

LuaModules: Location for Lua Scripting modules.

LUTs: Points to a folder containing Look Up Tables (LUTs).

Macros: Points to the location for user created macros. The macros saved to this location appear

in the macros category of the Effects Library and in the right-click Edit Macro contextual menu.

Plugins: This refers to user specific OpenFX plugins that you do not want loaded for all users.

Previews: Path map used for the older style, file sequence flipbook previews.

Queues: Location of the Render manager list.

Scripts: Location of Lua and Python scripts. This path can be further refined into specific scripts for

tools (nodes), comps, and other specific script types.

Settings: Location where custom Node settings are saved.

Stamps: Location for preview movies generated in a Fusion Studio bin. This is an outdated path

map since bins now include the Studio Player.

Templates: Location of the Templates folder. Saving Macros to the Template folder will cause them

to appear in the Effects Library in a Templates category. In Fusion Studio, the Templates category

does not appear until a Macros is saved into the folder.

Thumbs: Location for clip thumbnails generated in a Fusion Studio bin. This is an outdated path

map since bins include now include the Studio Player.

UserPaths: Used for locations of studio- or facility-specific tools, like custom plugins and scripts

located on a central server.

�User Path Maps: User paths are new paths that you have defined that do not currently exist in the

Defaults settings.

Comp refers to the folder where the current composition is saved. For instance, saving media

folders within the same folder as your Fusion Studio comp file is a way to use relative file paths for

Loaders instead of actual file paths.

Modifying a System Path Map

To modify an existing System path map, select the path map in the System section. Click the folder

icon at the bottom of the Preferences window, and enter the name of the path map in the From field

below. Enter the value of the path map in the To: field.

Modifying a Default Path Map

To modify an existing Default path map, select the path map in the Default section. Click the folder

icon at the bottom of the Preferences window, and enter the name of the path map in the From field

below. Enter the value of the path map in the To: field.

Creating a User Path Map

To create a path map, click on the New button and enter the name of the path map in the From field

below. Enter the value of the path map in the To: field.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Deleting a Path Map

To delete a user-created path map, select it from the list and click the Delete button. System and

Default path maps cannot be deleted; only user created path maps can be removed from the

Path Maps list.

Nesting Path Maps

When defining your own path map, you can use an existing path map in the new definition.

For example, define a path map called ‘Episode’ that maps to MyDrive\ Projects\Episode1. Then create

new path maps called Renders and Stills that map to Episode\ Renders_v1 and Episode\Stills_v1.