---
title: "Chapter 124"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 521
---

# Chapter 124

Modifiers

This chapter details the modifiers available in Fusion.

Contents

Modifiers������������������������������������������������������������������������� 2911

Anim Curves����������������������������������������������������������������� 2912

Bézier Spline���������������������������������������������������������������� 2914

B-Spline�������������������������������������������������������������������������� 2916

Calculation�������������������������������������������������������������������� 2916

CoordTransform Position�������������������������������������� 2919

Cubic Spline���������������������������������������������������������������� 2920

Custom Poly����������������������������������������������������������������� 2921

Expression�������������������������������������������������������������������� 2923

From Image������������������������������������������������������������������ 2928

Gradient Color����������������������������������������������������������� 2930

Key Stretcher Modifier�������������������������������������������� 2931

MIDI Extractor������������������������������������������������������������ 2932

Natural Cubic Spline����������������������������������������������� 2935

Offset (Angle, Distance, Position)���������������������� 2936

Path���������������������������������������������������������������������������������� 2939

Perturb��������������������������������������������������������������������������� 2940

Probe������������������������������������������������������������������������������� 2942

Publish��������������������������������������������������������������������������� 2944

Resolve Parameter�������������������������������������������������� 2945

Shake������������������������������������������������������������������������������ 2945

Track�������������������������������������������������������������������������������� 2947

Vector Result�������������������������������������������������������������� 2948

XY Path�������������������������������������������������������������������������� 2950


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Modifiers

Modifiers are extensions to a node’s standard set of parameters found in the Inspector; in fact,

modifiers are designed to control other parameters. They can be as simple as a motion path or linking

two parameters. However, they can also be elaborate expressions, procedural functions, external

data, third-party plugins, or scripted Fuses. You can add modifiers by right-clicking over a parameter in

the Inspector and choosing a modifier from the menu. Alternatively, you can right-click a control in the

viewer. Not all modifiers are displayed in the right-click menu for all parameters. Some modifiers work

only on specific parameter types.

NOTE: Text3D and Text+ have additional text-specific modifiers, which are covered in

their nodes’ sections.

Modifiers right-click menu


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Anim Curves

The Animation Curves modifier (Anim Curves) is used to dynamically adjust the timing, values,

and acceleration of an animation, even if you decide to change the duration of a comp. Using this

modifier makes it infinitely easier to stretch or squish animations, create smooth motion, add bouncing

properties, or mirror animations curves without the complexity of manually adjusting splines.

The Inspector for the Anim Curves modifier

When creating Fusion templates for the Edit and Cut page in DaVinci Resolve, the Anim Curves

modifier allows the keyframed animation you’ve created in Fusion to stretch and squish appropriately

as the transition, title, or effect’s duration changes on the Edit and Cut page Timelines.

Curve Shape Controls

The controls for the Anim Curves modifier appear in the modifier’s tab of the Inspector. The Curve

Shape controls determine the acceleration or shape of the animation curve.

�Source: This drop-down menu has three options based on how the comp is created from DaVinci

Resolve’s Edit page.

Transition: This setting is automatically selected when the comp is created from an Edit page

transition effect. If the duration of the transition is updated in the Edit page, the timing of the

animation updates as well.

Duration: Use this setting when the comp is created from a clip on the Edit page. The animation

timing will update if the clip’s duration changes by trimming.

Custom: Displays an Input dial to manually control the timing.

�Input: This dial is only visible when Source is set to Custom. It is used to change the

input keyframe value.

�Curve: The Curve drop-down menu selects the interpolation method used between keyframes.

The three choices are: linear, easing, or custom.

Linear: The default Linear interpolation method maintains a fixed, consistent acceleration between

keyframes.

Easing: Displays interpolation menus for both the start of the curve (In) and the end of

the curve (Out).

Custom: Opens a mini Spline Editor to customize the interpolation from the start of the animation

to the end.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

�Mirror: Plays the animation forward, and after reaching the end, it returns to the starting value.

This causes the initial animation to be twice as fast, since the second half of the comp is used for

the reverse animation.

�Invert: Flips the animation curve upside-down so that the values start high and end low.

Scaling

The Scale parameters modify the animation values using relative adjustments.

�Scale: This number is a multiplier applied to the value of the keyframes. If the Scale value is 2

and a keyframe has a value of 0, it remains 0. If the Scale value is 2 and a keyframe has a value

of 10, the result is as if the keyframe is set to 20. This can be thought of as the ending value for the

animation. It is best to set this while viewing the last frame in the comp.

�Offset: The offset is added to the keyframe values and can be thought of as the starting value for

the animation. It is best to set this while viewing the first frame in the comp.

�Clip Low: Ensures the output value never dips below 0.0.

�Clip High: Ensures the output value never exceeds 1.0.

Timing

The Timing parameters adjust the animation timing using relative values.

�Time Scale: Stretches or squishes the animation, causing it to run faster or slower. A value of 1.0

keeps the animation running for the comp’s duration (unless you have customized the animation

using other controls in the Modifier).

�Time Offset: This value delays the animation as a fraction of its total duration. A value of

0.0 applies no delay. A value of 0.5 delays the animation starting point midway into the

comp’s duration.

Using the Anim Curves Modifier to Create a Custom Transition

To understand how to use the Anim Curves modifier for a transition, let’s create a simple

scaling dissolve.


Add a standard cross dissolve in the Edit page Timeline.


Right-click over the transition and choose Convert to Fusion Cross Dissolve.


Right-click over the transition again and choose Open in Fusion page.


Add a Transform node to MediaIn1 and to MediaIn2.


Select the Transform node attached to the MediaIn2.


In the Inspector, right-click the Size control, then choose Modify With > Anim Curves from

the contextual menu. Adding this modifier to the Size control will cause the slider to animate

from 0 to 1 for the Cross Dissolve’s duration.


Select the Transform node attached to the MediaIn1.


In the Inspector, right-click the Size control, then choose Modify With > Anim Curves from the

contextual menu.


At the top of the Inspector, click the Modifier tab and click the Invert button. Inverting the

animation curves causes MediaIn1 to scale opposite of MediaIn2.

10	 In the Modifiers tab, set the Curve drop-down menu to Easing, and experiment with the different

ease-in ease-out curve types from the In/Out drop-down menus.

Once you create a Macro from this node tree and save it as a Transition template, you can apply it in

the Edit page Timeline. If you change the transition duration in the Edit page, the animation timing will

update appropriately.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Using the Anim Curves Modifier with Paths

To understand how to use the Anim Curves modifier’s with a Path modifier, let’s use the premise that

you want to create text that falls from the top of the frame and bounces as it reaches the bottom of

the frame.


In Fusion, create two keyframes that cause text to start at the top of the frame and drop to the

bottom. This automatically creates a Path modifier.


In the Inspector’s Modifier tab, right-click over the Displacement parameter and choose Insert >

Anim Curves. The animation is normalized to the duration of the comp.


Set the Source menu to Duration, since this is not a transition and we are not customizing

the duration.


From the Curve menu, choose Easing, then for the Out menu, choose Bounce.


Play the animation to see the Bounce animation.


To make the bounce occur halfway down the frame, change the Scale to .05.


To make the animation run twice as fast, enter 2.0 in the Time Scale parameter.

Once you create a macro from this node tree and save it as a Title template, you can apply it in the

Edit page Timeline. If you change the title’s duration in the Edit page, the animation timing will update

appropriately.

TIP: To view the resulting animation curve in the Spline Editor, select the parameter name in

the Spline Editor’s header. The spline is updated as you change the controls.

Bézier Spline

The Bézier Spline is one of the animation modifiers in Fusion and is typically applied to numerical

values rather than point values. It is automatically applied when you keyframe a parameter or each

time you right-click a number field and select Animate.

Bézier Spline modifier menu

Usage

You can add the Bézier Spline to the Spline Editor by right-clicking a number field and selecting

BezierSpline. Since this is the most common choice for animation splines, it is separated from the

Modify With menu for quicker access. Selecting BezierSpline from the menu adds a keyframe at the

current location and displays a Bézier Spline in the Spline Editor.


Fusion Page Effects | Chapter 124 Modifiers

FUSION

Bézier Spline Editor

Unlike most modifiers, this modifier has no actual Controls tab in the Inspector. However, the Spline

Editor displays the Bézier Spline, and it can be controlled there. The Bézier Spline offers individual

control over each control point’s smoothness using Bézier handles. The smoothness is applied in

multiple ways:

�To make the control points smooth, select them, and press Shift-S. The handles can be used to

modify the smoothness further.

�To make the control points linear, select them, and press Shift-L. These operations can also be

performed using the contextual menu.

�Select the control point(s), right-click, and select Smooth or Linear. The menu also allows the user

to smooth a spline using a convolution analysis called a Savitzky-Golay filter. Select the control

point(s), right-click, and select Smooth Points -Y Dialog.

Ease In/Out

Traditional Ease In/Out can also be modified by using the number field virtual sliders in the Spline

Editor. Select the control points you want to modify, right-click, and select Ease In/Out... from the

contextual menu. Then use the number field virtual sliders to control the Ease In/Out numerically.

Spline Ease In/Out modifier


Fusion Page Effects | Chapter 124 Modifiers

FUSION