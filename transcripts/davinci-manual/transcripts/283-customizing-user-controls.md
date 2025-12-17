---
title: "Customizing User Controls"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 283
---

# Customizing User Controls

Each tool’s parameters are organized in a logical order in the Inspector. The most used controls are

closer to the top, and the more subtle refinement controls are lower in the list. Sometimes, though, you

may want to add, hide, or change the controls. You often need to do this for SimpleExpressions and

macros, but you may also do this for usability and aesthetic reasons for favorites and presets.

Custom controls can be added or edited via the Edit Control dialog, which you access by right-clicking

over the node’s name in the Inspector and choosing Edit Controls from the menu.

Choose Edit Controls to create and

customize parameters

In the Edit Control dialog, you use the ID menu to select an existing parameter or create a new one.

You can name the control and define whether it is a text field, number field, or a point using the Type

attributes list.

Edit Control dialog

You use the page list to assign the new control to one of the tabs in the Inspector. There are also

settings to determine the defaults and ranges, and whether it has an onscreen preview control. The

Input Ctrl box contains settings specific to the selected Type, and the View Ctrl attributes box contains

a list of onscreen preview controls to be displayed, if any.

All changes made using the Edit Controls dialog get stored in the current tool instance, so they can

be copied/ pasted to other nodes in the comp. However, to keep these changes for other comps, you

must save the node settings, and add them to the Bins in Fusion Studio or to your favorites.


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION

As an example, we’ll customize the controls for a DirectionalBlur:

The Inspector for a default direction blur

Let’s say we wanted a more interactive way of controlling a linear blur in the viewer, rather than using

the Length and Angle sliders in the Inspector. Using a SimpleExpression, we’ll control the length and

angle parameters with the Center parameter’s onscreen control in the viewer. The SimpleExpression

would look something like this:

For Length:

sqrt(((Center.X-.5)*(self.Input.XScale))^2+((Center.Y-.5)*(self.Input.YScale)*(self.

Input.Height/self.Input.Width))^2)

For Angle:

atan2(.5-Center.Y , .5-Center.X) * 180 / pi

DirectionalBlur controlled by the Center’s position.

This admittedly somewhat advanced function does the job fine. Dragging the onscreen control

adjusts the angle and length for the directional blur. However, now the names of the parameters are

confusing. The Center parameter doesn’t function as the center anymore. It is the direction and length

of the blur. It should be named "Blur Vector" instead. You no longer need to edit the Length and Angle

controls, so they should be hidden away, and since this is only for a linear blur, we don’t need the

Type menu to include Radial or Zoom. We only need to choose between Linear and Centered. These

changes can easily be made in the Edit Controls dialog.


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION

To change the Inspector parameters for the example above:


In the Edit Control dialog, select the Center from the ID list.


A dialog will appear asking if you would like to Replace, Hide, or Change ID. We’ll choose Replace.


Change the Name to Blur Vector.


Set the Type to Point.


Select Controls in the Page list. (Controls is the first tab in the Inspector, normally.)


Click OK.

DirectionalBlur Center parameter name changed to Blur Vector.

The new Blur Vector parameter now appears in the Inspector. The internal ID of the control is still

Center, so our SimpleExpressions did not change.

To hide the Length and Angle parameters in the Inspector:


In the Edit Control dialog, select the Length from the ID list.


Select Controls from the Page list.


In the input Ctrl list, select Node.


Click OK.


In the Edit Control dialog, select the Angle from the ID list.


In the input Ctrl list, select Node.


Click OK.

Finally, to remove Radial and Zoom options from the Type menu:


In the Edit Control dialog, select the Type from the ID list.


Select Controls from the Page list.


Select Radial from the Items list and click Del to remove it.


Select Zoom from the Items list and click Del to remove it.


Click OK.

The Type menu now includes only two options.

If you want to replace the Type menu with a new checkbox control, you can do that by creating a new

control and a very short expression.


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION

To create a new control:


In the Edit Control dialog, enter Center Blur in the Name field.


Select the New Control from the ID list.


Set the Type to Number, and set the Page to Controls.


Set the Input Ctrl to CheckboxControl.


Click OK.

To make this new checkbox affect the original Type menu, you’ll need to add a SimpleExpression to

the Type:

iif(TypeNew==0, 0, 2)

The "iif" operator is known as a conditional expression in Lua script. It evaluates something based on a

condition being true or false.

FusionScript

Scripting is an essential means of increasing productivity. Scripts can create new capabilities or

automate repetitive tasks, especially those specific to your projects and workflows. Inside Fusion,

scripts can rearrange nodes in a comp, manage caches, and generate multiple output files for

delivery. They can connect Fusion with other apps to log artist time, send emails, or update webpages

and databases.

FusionScript is the blanket term for the scripting environment in Fusion. It includes support for Lua as

well as Python 2 and 3 for some contexts. FusionScript also includes libraries to make certain common

tasks easier to do with Lua and Python within Fusion.

You can run interactive scripts in various situations. Common scripts include:

�Utility Scripts, using the Fusion application context, are found under the File > Scripts menu.

�Comp Scripts, using the composition context, are found under the Script menu or entered

into the Console.

�Tool Scripts, using the tool context, are found in the Tool’s context menu > Scripts.

Other script types are available as well, such as Startup Scripts, Scriptlibs, Bin Scripts, Event Suites,

Hotkey Scripts, Intool Scripts, and SimpleExpressions. Fusion Studio allows external and command-

line scripting as well and network rendering Job and Render node scripting.

FusionScript also forms the basis for Fuses and ViewShaders, which are special scripting-based

plugins for tools and viewers that can be used in both Fusion and Fusion Studio.

For more information about scripting, see the Fusion Scripting Documentation, accessible from the

Documentation submenu of the Help menu.


Fusion Fundamentals | Chapter 74 Using Modifiers, Expressions, and Custom Controls

FUSION

Chapter 75

Preferences

This chapter covers the various options that are

available from the Fusion Preferences Window.

Contents

Preferences Overview���������������������������������������������� 1537

Categories of Preferences�������������������������������������� 1538

Preferences In Depth������������������������������������������������� 1541

3D View����������������������������������������������������������������������������� 1541

AVI��������������������������������������������������������������������������������������� 1542

Defaults����������������������������������������������������������������������������� 1543

Flow������������������������������������������������������������������������������������ 1544

Frame Format���������������������������������������������������������������� 1546

General���������������������������������������������������������������������������� 1548

GPU������������������������������������������������������������������������������������ 1550

Layout��������������������������������������������������������������������������������� 1551

Loader������������������������������������������������������������������������������� 1552

Memory����������������������������������������������������������������������������� 1554

Network��������������������������������������������������������������������������� 1556

Path Maps������������������������������������������������������������������������ 1557

Preview������������������������������������������������������������������������������ 1561

QuickTime���������������������������������������������������������������������� 1562

Script��������������������������������������������������������������������������������� 1563

Spline Editor������������������������������������������������������������������ 1564

Splines������������������������������������������������������������������������������ 1565

Timeline���������������������������������������������������������������������������� 1567

Tweaks����������������������������������������������������������������������������� 1568

User Interface����������������������������������������������������������������� 1571

Video Monitoring �������������������������������������������������������� 1573

View������������������������������������������������������������������������������������ 1574

VR Headsets������������������������������������������������������������������� 1576

Bins/Security������������������������������������������������������������������ 1578

Bins/Server���������������������������������������������������������������������� 1579

Bins/Settings����������������������������������������������������������������� 1580

EDL Import������������������������������������������������������������������������ 1581

Customization ������������������������������������������������������������� 1582

Shortcuts Customization����������������������������������������� 1582

Customizing Preferences����������������������������������������� 1583


Fusion Fundamentals | Chapter 75 Preferences

FUSION