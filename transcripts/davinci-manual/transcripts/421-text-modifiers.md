---
title: "Text+ Modifiers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 421
---

# Text+ Modifiers

Text+ modifiers

Text modifiers can be assigned by right-clicking in the Styled Text box and selecting a modifier from

the contextual menu. Once a modifier is selected, its controls are found in the Modifiers tab at the

top of the Inspector.

Character Level Styling

The Character Level Styling modifier works only on Text+ nodes. Once applied, individual characters

can be selected directly in the viewer, and different text attributes can be applied to them using the

controls in the Modifiers tab.

NOTE: Character Level Styling can only be directly applied to Text+ nodes, not to Text 3D

nodes. However, styled text from a Text+ node can be applied to a Text 3D node by copying

the Text+, right-clicking on the Text 3D, and choosing Paste Settings.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Inspector

Character Level Styling Modifiers tab

Text Tab

The Styled Text box in the Modifiers tab displays the same text in the Tools tab of the Text+ Inspector.

However, individual characters you want to modify cannot be selected in the Styled Text box; they

must be selected in the viewer. Once text is selected in the viewer, the Text tab includes familiar text

formatting options that will apply only to the selected characters.

Clear Character Styling on Selection

All changes made to the currently selected characters will be reset.

Clear All Character Styling

All character attributes will be reset to their original values.

Transform Tab and Shading Tab

For details on these Text+ tabs, see the “Text+” section above.

Comp Name

The Comp Name sets the styled text to become the current Composition Name. This is quite useful to

automate burn-ins for daily renderings. See also the TimeCode modifier. It can be applied by right-

clicking in the Styled Text field of a Text+ node and selecting Comp Name.

Controls

This modifier has no controls.

Follower

The Follower modifier allows sequencing text animations. The modifier is applied by right-clicking

in the Styled Text field of a Text+ node and selecting Follower. In the Modifiers tab, you start by

animating the parameters of the text (note that changing any parameter in the Modifiers tab will

not be visible unless a keyframe is added.) Then, in the Timing tab you set the animation’s delay

between characters.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Inspector

Follower Timing tab

Timing Tab

Once the text is animated using the controls in the Modifiers tab, the Timing tab is used to choose the

direction and offset of the animation.

Range

The Range menu is used to select whether all characters should be influenced or only a selected

range. To set the range, you can drag-select over the characters directly in the viewer.

Order

The Order menu determines in which direction the characters are influenced. Notice that empty

spaces are counted as characters as well. Available options include:

�Left to right: The animation ripples from left to right through all characters.

�Right to left: The animation ripples from right to left through all characters.

�Inside out: The animation ripples symmetrically from the center point of the

characters toward the margin.

�Outside in: The animation ripples symmetrically from the margin toward the center

point of the characters.

�Random but one by one: The animation is applied to randomly selected characters but only

influences one character at a time.

�Completely random: The animation is applied to randomly selected characters, influencing

multiple characters at a time.

�Manual curve: The affected characters can be specified by sliders.

Delay Type

Determines what sort of delay is applied to the animation. Available options include:

�Between Each Character: The more characters there are in your text, the longer the animation

will take to the end. A setting of 1 means the first character starts the animation, and the second

character starts 1 frame later, the third character starts 1 frame after the second, and so on.

�Between First and Last Character: No matter how many characters are in your text, the animation

will always be completed in the selected amount of time.

Clear All Character Styling

All character attributes will be reset to their original values.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Text Controls, Alignment, Transform, and Shading Tabs

In these tabs, the actual animation for the characters is done. Observe that simply changing a value in

these tabs will have no influence at all. The value must be animated for the effect to show.

For a detailed description on the various parameters, see the Text+ node documentation.

Text Scramble

The Text Scramble randomly replaces the characters with others from a user definable set. It can be

applied by right-clicking into the Styled Text field of a Text+ node and selecting Text Scramble.

The Controls for the Text Scramble are then adjusted in the Modifiers tab.

Inspector

Text Scramble modifier Controls tab

Controls Tab

The Controls tab in the Text Scramble modifier is used to enter text and scramble it using the

Randomness control. The scrambled characters are taken from the Substitute Chars field at the bottom

of the Inspector.

Randomness

Defines how many characters are exchanged randomly. A value of 0 will change no characters at

all. A value of 1 will change all characters in the text. Animating this thumbwheel to go from 0 to 1 will

gradually exchange all characters.

Input Text

This reflects the original text in the Text+ Styled Text field. Text can be entered either here or in the

Text+ node.

Animate on Time

When enabled, the characters are scrambled randomly on every new frame. This switch has no effect

when Randomness is set to 0.

Animate on Randomness

When enabled, the characters are scrambled randomly on every new frame, when the Randomness

thumbwheel is animated.

This switch has no effect when Randomness is set to 0.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION

Don’t Change Spaces

When enabled, spaces are not scrambled, allowing the length of the single words to stay the same,

although their characters get scrambled around.

Substitute Chars

This field contains the characters used to scramble the text.

Text Timer

The Text Timer makes the Text+ node either a Countdown, a Timer, or a Clock. This is useful for

onscreen real-time displays or to burn in the creation time of a frame into the picture. It can be applied

by right-clicking in the Styled Text field of a Text+ node and selecting Text Timer.

Inspector

Text Timer modifier Controls tab

Controls Tab

The Controls tab for the Text Timer modifier is used to set up the type of time display that is generated

by this modifier.

Mode

This menu sets the mode the timer is working in. The choices are CountDown, Timer, and Clock. In

Clock mode, the current system time will be displayed.

Hrs, Mins, Secs (Checkboxes)

Defines which parts of the clock should be shown onscreen.

Hrs, Mins, Secs (Sliders)

Sets the start time for the CountDown and Timer mode.

Start

Starts the Counter or Timer. Toggles to Stop once the timer is running.

Reset

Resets the Counter and Timer to the values set by the sliders.


Fusion Page Effects | Chapter 104 Generator Nodes

FUSION