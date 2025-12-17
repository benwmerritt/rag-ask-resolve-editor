---
title: "Recording Mix Automation"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 704
---

# Recording Mix Automation

Recording mix automation uses many of the same techniques as drawing but allows you to capture

a performance where you are moving the controls you want to automate. This can be flexible and

creative as you “perform to picture” to get the results you want.

To get started, you’ll need to ensure that Automation recording is enabled (see “Enabling and Viewing

Automation” above) and that one or more parameters are enabled for automation recording.

Clicking the Automation

Controls button displays

the Automation toolbar


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Automation Controls

The Automation Controls button, to the right of the transport controls, lets you show and hide the

Automation toolbar.

The Automation toolbar has buttons for each option that’s available for preparing to record automation

in your mix.

Automation toolbar options

The Automation toolbar displays the following options:

�Automation Modes: Controls how automation data is recorded.

Write: Records absolute changes to a control’s position, replacing any data that was there

previously.

Trim: Records relative changes to a control’s position, maintaining relative existing levels

created over time, but increasing or reducing those levels overall. This can be very useful when

incrementally refining a mix.

�Touch Modes: Defines what happens when an automatable control is moved during a mix.

Off: No automation is recorded.

Latch: Automation is recorded once a control is moved and continues recording after the control is

released until the transport is stopped.

Snap: Automation is recorded once a control is moved and then smoothly glides back to the pre-

existing level at the point it was released, to create a seamless transition.

At the point where the glide transition ends, automation is no longer recorded unless the control

is moved once again while the transport is playing. You can continue to capture additional

automation with Snap until the transport is stopped.

The time for the glide transition can be set in milliseconds in Preferences > User > Fairlight >

Automation. The default is 250 ms.

Snap Latch: A combination of Snap and Latch modes, where faders operate in Snap and all other

controls operate in Latch. This can be useful when dynamically changing fader levels through

a mix pass are desired, while other controls “stick” when they’re moved. It is particularly useful

when working with Fairlight mix control surfaces where faders and rotary controls can be changed

simultaneously during a mix pass.

�On Stop: Defines what happens when entering Stop at the end of an automation pass.

Event: The last recorded automation value overwrites previous levels to the start of the next

available recorded automation data (or event) in that track.

Hold: Deletes all previously recorded mixing data after what you’ve just recorded, to hold the last

recorded level for the rest of that track.

Return: The last recorded automation value is interpolated to ramp back to the previously

recorded automation values on that track.

�Enables: The following buttons let you enable or disable different controls for recording automation.

Fader: Automates track and bus volume.

Mute: Automates the mute button.

Pan: Automates all pan controls.

EQ: Automates all EQ controls.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Comp: Automates just the Compressor controls in the Dynamics window.

Gate: Automates just the Gate controls in the Dynamics window.

Lim: Automates just the Limiter controls in the Dynamics window.

Sends: Automates the Send controls in the Sends window.

Plugins: Automates all Fairlight, VST, or Audio Unit (AU) plugins.

Misc: Automates Buss on/off, Insert, and Direct Out controls. If a project is using the Fairlight

legacy Fixed Bus configuration, it allows automation of fixed bus Main and Sub bus enables.

How to Record Automation

There are two different ways you can set up the recording of automation for levels, panning, EQ,

Dynamics, and other audio controls in the mixer.

Recording Automation for Multiple Tracks

You can use the following steps to record automated changes to any audio control in any control strip:


Open the Automation toolbar, and do the following three preparatory steps:

a)	 Choose whether you’re going to write new automation, or trim automation that’s already

recorded. Write mode is appropriate when you’re recording automation for the first time, or

when you’re overwriting previous automation with brand new values. Trim mode is appropriate

when you’re making incremental changes to previously recorded automation. Note that Trim

mode works as a delta trim system only with fader positions at zero (unity) on Fairlight control

surfaces at this time.

b)	 Next, choose Touch and On Stop behaviors that are appropriate for the kind of automation

recording you need to do.


Move the playhead to the beginning of the section of the timeline you want to record

automation for.


Next, initiate playback using any method (Spacebar, L, Play button, Fairlight or third-party audio

control surface), and make whatever adjustments you want to the controls you’ve enabled

automation recording for. As you make adjustments, the affected fader control turns red to let you

know you’re recording automation.


When you’re finished, stop playback using any method (Spacebar, K, Stop button, third-party or

Fairlight audio control panel). Automation recording stops as well.

Recording Automation for Specific Individual Tracks

You can use the following steps to record automated changes to controls in specifically armed

control strips:


Open the Automation toolbar, and do the following three preparatory steps:

a)	 Choose whether you’re going to write new automation, or trim automation that’s already

recorded. Write mode is appropriate when you’re recording automation for the first time, or

when you’re overwriting previous automation with brand new values. Trim mode is appropriate

when you’re making incremental changes to previously recorded automation.

b)	 Next, set Touch to Off, which disables across-the-board automation recording and requires

you to arm specific tracks that you want to automate.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT


Click the automation arm button above the fader of any Mixer track or any track header to which

you want to record automation. Even though the Touch control is set to off, moving a control on an

armed channel strip will record automation in Latch mode.

The automation

arming button above

a fader in the Mixer

The automation arming

button in the track header


Move the playhead to the beginning of the section of the timeline you want to record

automation for.


Next, initiate playback using any method (Spacebar, L, Play button, Fairlight or third-party audio

control panel), and make whatever adjustments you want to the controls for which you’ve enabled

automation recording. While you make adjustments, the affected fader control turns red to let you

know you’re recording automation. If you’re displaying the same automation data in the Timeline

that you’re recording, you can see the new automation being drawn in real time, in red.

New automation line in red while being recorded


When you’re finished, stop playback using any method (Spacebar, K, Stop button, Fairlight or third-

party audio control panel). Automation recording stops as well. Displayed automation turns green

once recording has stopped.

If you don’t like what you’ve done, you can undo and start over, or you can edit the automation

using methods described later in this chapter. Or, you can back the playhead up and overwrite

automation at any time with new automation.

Automation Preview Mode

Preview is an additional mix automation workflow, specifically for working across scene-based

material. When enabled, mix items that are in preview are not controlled by pre-recorded automation,

so they respond manually to their controls. These can subsequently be placed into write (or trim) to

write actual automation.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

Typically, Preview mode is used to audition new mix settings for one particular section of a timeline,

while other sections already have recorded automation data. Preview mode prevents pre-recorded

automation from moving the controls you are trying to adjust in a targeted section. As soon as you’re

happy with the new adjustments, they can be written to the targeted section.

Preview mode frees the faders (and other controls) from automation control, and lets you move them

freely while you experiment with different levels and settings. Ordinarily, moving one or more controls

implies writing automation data for those controls, but entering Preview mode lets you play with

the controls as much as you like without committing to anything, only writing automation data when

you’re ready.

To engage the Preview state on enabled mix items,

first enter Preview mode by doing one of the following:

�Toggle Preview in the Automation toolbar.

�Press the Preview key on the Mix page of the Fairlight controller.

Once Preview is engaged:

�Individual parameters can be switched into Preview Touch Latch.

�You can use the AUTO key next to a fader to preview all enabled parameters on a channel.

�You can use the Auto button on the screen mixer strips.

�When you’re in Preview mode, all parameters in Preview are indicated by a

BLUE automation indicator.

Once in Preview mode, mix items can be placed into write (or trim) by:

�Dropping in manually via the Fairlight > Automation > Punch In menu choice.

�Dropping in manually with the In key on the Fairlight controller.

�Automatically using the Active In and Out points on the Fairlight controller.

Once enabled for Preview, parameters remain in that state regardless of transport starts and

stops. This is different from putting mix items into WRITE, which must be done again after each

transport stop.

Other Preview-related operations include:

�Filling a range defined by In and Out points with all parameters currently in Preview.

�Gliding all parameters from their existing values at the Range In point to the Preview values at the

Range Out point.

Automation Active Range

The Automation Active Range allows you to set only a specific range on the timeline to record

automation to, so that everything outside of that range is “write protected” and will not be disturbed.

�To enable the Active Range, choose Fairlight > Automation > Active Range, where you can mark

the Active Range In/Out points, or enable or disable the Active Range.

�Once a range is defined, automation writing will only take place within the range.

�You can set the automation mode you wish to work in (e.g., Snap).

�Once playback begins, all automation data produced prior to the range automatically occurs in

Preview mode (without having to enable the Preview switch), up and until you reach the Active

Range in point. Once inside the Active range, automation recording will start.

�At the end of the range, automation recording is automatically punched out.

�The Active Range can be disabled by unchecking Fairlight > Automation > Active Range > Enable.


Fairlight | Chapter 178 Mix Automation

FAIRLIGHT

NOTE: Any controls in Read mode will play back their automation regardless of the status of

the Active Range.

Active Range shown in the ruler with red bar; Automation data being written within the range