---
title: "General"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 286
---

# General

The sections contained in the General preferences affect the behavior of the Inspector as well as

some other user interface elements.

The General preferences

Usability

Usability has a number of project, Node Editor, and user interface settings that can make the

application easier to work with, depending on your workflow.

�Auto Clip Browse: When this checkbox is enabled, the File Browser is automatically displayed

when a new Loader or Saver is added to the Node Editor.

�New Comp on Startup: When checked, a new, empty project is created each time Fusion Studio is

launched. This has no effect in DaVinci Resolve’s Fusion page.

�Summarize Load Errors: When loading node trees or “comps” that contain unknown tools

(e.g., comps that have been created on other computers with plugins not installed on the current

machine), the missing tools are summarized in the console rather than a dialog being presented

for every missing tool.

�Save Compressed Comps: This option enables the saving of compressed node trees, rather than

ASCII based text files. Compressed node trees take up less space on disk, although they may take

a moment longer to load. Node trees containing complex spline animation and many paint strokes

can grow into tens of megabytes when this option is disabled. However, compressed comps

cannot be edited with a text editor unless saved again as uncompressed.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

�Show Video I/O Splash: This toggles whether the Splash image will be displayed over the video

display hardware. This is only applies to Fusion Studio.

�Use Simplified Copy Names: This option reduces the occurrence of underscores in tool names

when copying.

�Show Render Settings: When this checkbox is selected, the Fusion Render Settings dialog will be

displayed every time a render is started in Fusion Studio. Holding Shift while starting a render will

prevent the display of the dialog for that session, using whatever settings were applied during the

last render. Disabling this option reverses this behavior.

�Mouse Wheel Affects the Window Under the Pointer: Normally the mouse wheel or trackpad

swiping works in the currently active window. With this option enabled, it will work in the window

underneath the cursor, so you don’t have to click into a window first to make it active.

�Frames Start From: This designates the starting frame number for clip times in the Loader and its

Clip list.

�Show Color As: This setting determines the numeric scale used to represent colors. The available

options are Normalized (0 to 1), 8-bit (0 to 255), and 16-bit (0 to 65,535). This does not affect the

actual processing or quality of the image, but it can make the mental math sometimes used to

figure out adjustments a bit easier.

Auto Save

The Auto Save settings only apply to Fusion Studio. To set auto backups for the Fusion page in

DaVinci Resolve, use the DaVinci Resolve Project Load and Save Preferences.

When Auto Save is enabled in Fusion Studio, comps are automatically saved to a backup file at regular

intervals defined by the Delay setting. If a backup file is found when attempting to open the comp, you

are presented with the choice of loading either the backup or the original.

If the backup comp is opened from the location set in the Path Map preference, saving the backup

will overwrite the original file. If the backup file is closed without saving, it is deleted without

affecting the original file.

�Save Before Render: When enabled, the comp is automatically saved before a preview or final

render is started.

�Delay: This preference is used to set the interval between Auto Saves. The interval is set using

mm:ss notation, so entering 10 causes an Auto Save to occur every 10 seconds, whereas entering

10:00 causes an Auto Save every 10 minutes.

Proxy

�Update All, Selective, No Update: The Update mode button is located above the toolbar. You

can use this preference to determine the default mode for all new comps. Selective is the usual

default. It renders only the tools needed to display the images in the Display view. All will render

all tools in the composition, whereas None prevents all rendering.

�Standard and Auto: These sliders designate the default ratio used to create proxies when the

Proxy and Auto Proxy modes are turned on. These settings do not affect the final render quality.

Even though the images are being processed smaller than their original size, the image

viewing scales in the viewers still refer to original resolutions. Additionally, image processing

performed in Proxy Scale mode may differ slightly from full-resolution rendering.

The Proxy and Auto Proxy size ratios may be changed from within the interface itself by right-

clicking on the Prx and APrx buttons above the toolbar and selecting the desired value from

the contextual menu.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

GPU

The GPU preference is only available in Fusion Studio. In DaVinci Resolve, you can configure the GPU

processing in Resolve’s Memory and GPU preferences.

In Fusion Studio, the GPU preference is used to specify the GPU acceleration method used for

processing, based on your computer platform and hardware capabilities. It is also used for enabling

caching and debugging GPU devices and tools.

The GPU preferences

Options

The GPU options include radio buttons to select whether the GPU is used when processing and, if so,

which computer framework is used for communicating with the GPU.

�GPU Tools: This preference has three settings: Auto, Disable, and Enable. When set to Disable, no

GPU acceleration is used for tools or third-party plugins. Fuses may still require GPU acceleration.

If Enable is selected, GPU acceleration is available for tools and plugins, if appropriate

drivers are installed.

�API: The API setting selects the GPU processing method to use.

�Device: The Device setting determines which GPU hardware to use in the case of multiple GPUs.

The Auto setting gives priority to GPU processing; however, if it is unavailable, Fusion uses the

platform default. Currently, both the AMD and CPU options require either the AMD Catalyst 10.10

Accelerated Parallel Processing (APP) technology Edition driver or the ATI Stream SDK 2.1 or later

to be installed. The Select setting allows you to choose the device explicitly.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Debugging

The more advanced preferences located in this section are designed for diagnostics and analyzing

GPU operations.

�Verbose Console Messages: Enabling this option causes information to be shown in the Console.

For example, Startup Logs, Compiler Warnings, and Messages.

�OpenGL Sharing: Enabling this option shares system RAM with onboard GPU RAM to create a

larger, but slower, OpenGL memory pool.

�Clear Cache Files: This option will clear already compiled GPU code and then

recompile the kernels.

Layout

The Layout preferences are only available in Fusion Studio. To save a Layout in DaVinci Resolve’s

Fusion page, use the Workspace > Layout Presets menu. The Layout options are used to control the

layout, size, and position of various windows in Fusion’s interface at startup or when a comp is created.

The Layout preferences

There are a lot of options, but in practice, you simply organize the interface the way you prefer it

on startup and when a new composition is created, then open this Preferences panel and click on

the three buttons to grab the Program Layout, the Document Layout and the Window Settings.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

Program Layout

The Program Layout is used to save the overall Fusion interface window and any open floating

windows. Each new composition you open within the larger overall Fusion interface window will

adhere to these preferences.

�Grab Program Layout: Pressing this button stores the application’s overall current

position and size.

�Run Mode: This menu is used to select the application’s default mode at startup.

You choose between a Maximized application window, a Minimized application, or a Normal

application display.

�Use the Following Position and Size: When checked, the values stored when Grab Program

Layout was selected will be used when starting Fusion Studio.

�Create Floating Views: When checked, the position and size of the floating viewers will be saved

when the Grab Program Layout button is used.

Document Layout

The Document Layout is used to save the layout of panels and windows for the current Fusion comp.

�Recall Layout Saved In Composition: When checked, all Document Layout settings in the controls

below will be recalled when a saved composition is loaded.

�Grab Document Layout: Pressing this button stores the entire interface setup, including all the

internal positions and sizes of panels and work areas.

�Window: When multiple windows on the same composition are used, this menu is used to select

the window to which the Window Settings will apply.

Window Settings

Rather than saving entire comp layouts, you can save position and size for individual floating windows

and panels within a comp using the Window Settings.

�Automatically Open This Window: When checked, the selected window will automatically be

opened for new flows.

�Grab Window Layout: Pressing this button stores the size and position of the selected window.

�Run Mode: Select the default run mode for the selected window. You can choose between a

Maximized window, a Minimized window, or a Normal window display.

�Use Grabbed Position and Size: When checked, the selected window will be created using the

stored position and size.

Loader

The Loader preferences are only available in Fusion Studio. Using the Loader preferences, you can set

options for the default Loader’s color depth and aspect ratio as well as define the local and network

cache settings.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

The Loader preferences

Defaults

The Defaults section includes two settings to determine how color depth and aspect ratio are handled

for Loaders.

�Loader Depth: The Loader Depth defines how color bit depth is handled when adding a Loader.

Choosing Format means that the correct bit depth is automatically selected, depending on the

file format and the information in the file’s header. Choosing Default sets the bit depth to the value

specified in the Frame Format preferences.

Cache

The Cache preferences allow you to control how disk caching operates in Fusion. You can set how and

where the cache is generated, when the cache is removed, how the cache reacts when source files

are not available, as well as many other cache related options. This is not to be confused with RAM

cache, which is controlled in the Memory preferences.

�Disable All Local Caching: This setting disables local caching.

�Cache Files from Network DiskCaches: If a tool has disk caching enabled, and the disk cache

files are stored remotely on the network, then enabling this option will use a local copy of those

cache files, similarly to the local cache on a networked Loader.

�Enable Local Caching of Loaders: Files will be copied into the LoaderCache path set below or in

the Path Maps preferences.


Fusion Fundamentals | Chapter 75 Preferences

FUSION

�Cache Multi-Frame Files: Files like AVI or QuickTime will be copied into the LoaderCache path.

This may take some time if the file is large.

�Don’t Cache Files from Local Disks: Files that do not sit on a network drive will not be copied into

the LoaderCache path. You can disable this option if you have, for example, a fast SSD cache drive

and want to use it for local files as well to speed up file access while working interactively.

�Only Files Smaller Than xxx MB.: Files larger than the value set here will not be copied into the

LoaderCache path.

�Cache Path Separator Character: When Enable Local Caching of Loaders is enabled, you can use

this setting to rebuild the path of the original files in LoaderCache.

For instance, given the default “!” character, the original path X\Project\MyShots\ Shot0815\ will be

translated into X!Project!MyShots!Shot0815! in the LoaderCache path. Other separator characters

may be used, including the “\” character, which will use subdirectories in LoaderCache: X\Project\

MyShots\Shot0815\.

�If Original File Is Missing: This setting provides three options to determine the caching behavior

when the original files can’t be found. The Fail option behaves exactly as the Default Loader in

Fusion. The Loader will not process, which may cause the render to halt. The Load Cache option

loads the cache even though no original file is present.The Delete Cache option clears missing

files from the cache.

�Cache Location: For convenience, this is a copy of the LoaderCache path set in the

Path Maps preferences.

�Explore: This button opens the LoaderCache path in the macOS X Finder window

or a Windows Explorer window.

�Clear All Cache Files: This button deletes all cached files present in the LoaderCache path.