---
title: "Chapter 2"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 11
---

# Chapter 2

Using the

DaVinci Resolve

User Interface

This chapter provides an overview of the various unspoken conventions and

interaction methods employed by the DaVinci Resolve graphical user interface (GUI).

These include how the various buttons of your mouse, pen and tablet, or trackpad are used by different

windows and interface widgets, how commands are distributed throughout the application using the

menu bar, contextual menus, and option menus, and how to interact with fields and other controls.

While many of these conventions overlap with common user interface conventions found in the file system

of your platform of choice, and with other media applications, some of these are unique to DaVinci Resolve,

so this chapter is worth reviewing even if you consider yourself an expert user of other applications.

Contents

Basic Documentation Terminology������������������������ 57

What Is the “UI” or “GUI”���������������������������������������������� 57

What Is “the Pointer”������������������������������������������������������ 57

About Keyboard Shortcuts������������������������������������������ 57

Customizing the DaVinci Resolve Interface������ 57

Working Full Screen vs.

Within a Floating Window�������������������������������������������� 57

Panels and Panel Focus������������������������������������������������ 57

Showing and Hiding Panels

Using the Interface Toolbar���������������������������������������� 58

Showing and Hiding Panels in

the Workspace Submenu��������������������������������������������� 59

Adjusting the Size of Different Panels������������������� 59

Using Single- vs. Dual-Monitor Layouts����������������� 61

Using the Full Screen

Timeline Option in the Edit Page����������������������������� 62

Video Clean Feed (Studio Version Only)�������������� 63

Saving Custom Screen Layouts�������������������������������� 63

Resetting to the Default Layout�������������������������������� 63

Undocking Specific Panels of the Interface�������� 63

DaVinci Resolve User Interface Conventions��� 65

Contextual Menus������������������������������������������������������������ 65

Drop-Down Menus���������������������������������������������������������� 66

Adjusting Parameters���������������������������������������������������� 67

Using a Mouse or Other Input Device������������������ 68

Mouse, Trackpad, and Tablet Behaviors������������� 69

Timeline Scroll Behavior����������������������������������������������� 69

Viewer Behavior��������������������������������������������������������������� 70

Keyboard Shortcuts�������������������������������������������������������� 71

Undo and Redo in DaVinci Resolve����������������������� 72


DaVinci Resolve Interface | Chapter 2 Using the DaVinci Resolve User Interface

INTRO

Basic Documentation Terminology

Here is a brief word about some of the basic terminology used in this manual for brand new users.

What Is the “UI” or “GUI”

In this documentation, UI refers to “user interface,” while GUI refers to “graphical user interface.”

This refers to the windows, screens, and controls that let you create in DaVinci Resolve. If you didn’t

know this, don’t be embarrassed, you’d be surprised how many times this question gets asked.

What Is “the Pointer”

Whenever this documentation refers to “the pointer,” the reference is to the on-screen arrow you use

to click on elements of the user interface, which is controlled by the mouse, trackpad, pen and tablet,

trackball, or any other device you may be using. Because there are so many different ways to control

computers, simply referring to “the mouse” is inaccurate.

About Keyboard Shortcuts

This manual presents all keyboard shortcuts using the macOS conventions of the Command key

and the Option key. For compatibility with Windows and Linux, the Control key in macOS is not

used by default for any keyboard shortcuts (although it can be assigned if you customize your

keyboard shortcuts).

All keyboard shortcuts that use the Option key in macOS use the ALT key in Windows and Linux,

and all keyboard shortcuts that use the Command key in macOS use the Control key in Windows

and Linux.

Customizing the DaVinci Resolve Interface

While the DaVinci Resolve interface may not seem very customizable at first, there are actually many

ways in which you can tailor the panels found within each page to your specific needs.

Working Full Screen vs. Within a Floating Window

Depending on how you like to work, you can choose to work with DaVinci Resolve in a floating window

with a title bar that can be resized, moved, minimized, and used alongside other windows. Or, you can

choose Workspace > Full Screen to put DaVinci Resolve into Full Screen mode, where the title bar

disappears and DaVinci Resolve takes up the full dimensions of your computer display.

Editors may prefer to work within a window if they’re working among multiple applications.

Colorists and mixers may prefer Full Screen mode as it hides the light-colored title bar that some find

distracting and provides a tiny bit more screen real estate for the rest of the application.

Panels and Panel Focus

Each page of DaVinci Resolve consists of multiple panels. Each panel contains all the controls and

information necessary for a particular aspect of that page’s functionality. In the following partial

screenshot of the top of the Media page, the Media Storage panel lets you browse files, the Viewer is

a panel that lets you watch video, and the Audio panel lets you see the strength of audio playing back

via a set of audio meters. Each of these panels has separate controls, but they all appear within the

main window of the DaVinci Resolve user interface.


DaVinci Resolve Interface | Chapter 2 Using the DaVinci Resolve User Interface

INTRO

Three panels side by side on the Media Page, showing Media Storage, the Viewer, and the Audio panel

Each panel you use has “focus,” meaning that clicking an item or control within a particular panel

makes that panel the active panel, which serves to direct keyboard shortcuts that are shared among

many panels to the particular panel you’re using. If you want to see which panel is in focus, you can

turn on the “Show focus indicators in the User Interface” checkbox in the UI Settings panel of the User

Preferences. When on, a red line at the top of the active panel indicates that it has focus.

A red line at the top of the Media Pool in the Edit page shows that it has focus

Showing and Hiding Panels Using the Interface Toolbar

Each page in DaVinci Resolve has an Interface Toolbar that runs along the top. This toolbar contains

buttons that let you show and hide different panels of functionality to accomplish different things:

�You can show panels that aren’t displayed by default, since most pages have many available

panels of functionality that are hidden until you need them.

�You can assign keyboard shortcuts to show and hide individual panels in your workspace for

instant configuration of the UI. Keyboard shortcuts to toggle these panels on or off can be

assigned using the Keyboard Customization window.

�You can switch which panel appears within a particular geographical location of the UI, for

example switching between showing the Media Pool or Effects in the upper-lefthand corner of the

Cut or Edit pages.

�You can hide panels you don’t need in order to create more room in the specific panels

you’re working within.


DaVinci Resolve Interface | Chapter 2 Using the DaVinci Resolve User Interface

INTRO

The Interface toolbar for the Color page lets you customize the Color page controls

If you right-click anywhere within the UI toolbar, two options appear: “Show Icons and Labels” and

“Show Icons Only.” If you show icons only, the UI toolbar becomes less cluttered.

Each page has a different set of options that reflect the capabilities of that page.

The UI Toolbar for the Edit page, showing icons only, to save space

Showing and Hiding Panels in the Workspace Submenu

This function provides the ability to turn on or off panels by choosing them in the Workspace >

Show Panel in Workspace drop-down menu. The exact panels, such as Inspector, Media Pool,

Metadata, etc., are dependent on which page you are working in. Alternatively, you can assign these

panels keyboard shortcuts as well.

Adjusting the Size of Different Panels

You can resize adjacent panels in the interface by positioning the pointer at the border between any

two panels, and dragging it to enlarge one and shrink the other.

(Before/After) Resizing UI regions

Certain panels and palettes can be expanded, in the process rearranging another part of the UI, by

clicking a small gray Expand button. For example, an expand button at the top right of the Keyframe

Editor in the Color page can be clicked to make the Keyframe Editor wider, while at the same time

hiding controls at the center to make room.

(Before/After) Expanding the Keyframe Editor


DaVinci Resolve Interface | Chapter 2 Using the DaVinci Resolve User Interface

INTRO

Certain vertically oriented panels, such as the Media Pool, Effects Library, Metadata Editor, and

Inspector, can be set to either half-display-height or full-display-height sizes to quickly create more or

less room for contents or controls whenever necessary. This is done by clicking a small button in the

UI toolbar that toggles between expanding or contracting the UI element it controls.

The button for expanding

a panel to full height

The button for contracting

a panel to half height

The result is that the panel in question expands or contracts. The following screenshots show the

Inspector of the Edit page in half height mode, where the Timeline is given room to expand, and in full

height mode, where the Timeline becomes shorter, but there’s more room in the Inspector to see all of

the controls.

(Left) A half-height Inspector with more room for the Timeline,

(Right) A full-height Inspector with more room for controls


DaVinci Resolve Interface | Chapter 2 Using the DaVinci Resolve User Interface

INTRO