---
title: "Paste and Remove Attributes"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 686
---

# Paste and Remove Attributes

The Fairlight page has Paste Attributes and Remove Attributes commands that allow for the copying

and resetting of audio parameters and effects, similar to the same commands on the Edit page.

Clip Attributes Naming

By double-clicking any clip in the Timeline, you can access the Clip Attributes window to rename the

clip. You can still access this window with a right-click, revealing the dropdown menu of options.

Copying and Pasting Clip Attributes

For clips, this works as simply as copying a clip, then selecting one or more audio clips and right-

clicking another clip and choosing Paste Attributes from the contextual menu. A dialog appears letting

you choose which audio attributes you want to paste before clicking Apply.

The Paste Attributes dialog in the Fairlight page

Copying and Pasting Track Attributes

For tracks, it works a little differently. Right-click on a track header and choose Copy Attributes to copy

all track settings and effects. Then, select one or more other track headers, right-click the selection,

and choose Paste Attributes. A dialog appears letting you choose which track attributes you want to

paste before clicking Apply.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

The Paste Attributes dialog in the Fairlight page, used

to copy attributes from one track to another

Removing Attributes

For either clips or tracks, you can right-click and choose Remove Attributes to open a dialog with

which to choose which attributes you want to reset to their default settings.

NOTE: By choosing the Volume check box in Remove Attributes you will delete all of the

Clip Gain keyframes that have been added to a clip.

EQ, Level, and AI Dialogue Matching

To help provide a solid foundation for a great mix, Fairlight offers three features for matching the

tonal characteristics (EQ profile), volume level, or sonic characteristics of disparate timeline clips as

described below.

EQ Matcher

EQ Matcher can be used in situations where, for example, you need to quickly apply the tonal

characteristic (EQ Profile) of on-location dialogue recorded with one type of microphone to newly

recorded dialogue recorded in post using a completely different microphone.

To capture and apply an EQ Profile:


Right-click the timeline clip you want to match and choose Clip Operations > EQ Matching >

Capture EQ Profile from the contextual menu.

Timeline clip EQ Matcher contextual menu


Apply the captured EQ Profile to another audio clip in one of the following ways:

Apply to Clip EQ: This applies the same EQ setting to the Clip EQ plugin for each selected clip on

the destination track.

Apply to Track EQ: Applies the EQ profile to the whole track. The applied EQ curve will appear in

the EQ section of the corresponding Mixer channel strip.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

New EQ curve displayed

in a Mixer channel strip

Apply to Automated Track EQ: This option is useful when you have multiple clips on a track,

each requiring its own unique EQ setting to maintain the correct tonal match during playback.

This selection lets you quickly write automation data, which adjusts the Track EQ curve for each

clip as required.

To apply the EQ profile to an automated track EQ:


Right-click the timeline clip you want to match and choose Clip Operations > EQ Matching >

Capture EQ Profile from the contextual menu.


Ensure the Toggle Automation button to the right of the transport control is active (red), then select

an EQ parameter from the Automation drop-down in the destination Track Header, for example,

EQ > Band 3 > Gain.


Right-click the first clip you want to apply the EQ profile to and choose Clip Operations > EQ

Matching > Apply to Automated Track EQ. Repeat this step for subsequent clips on the track.

�As you repeat the this step, you will notice the automation curve changing with each application

of the EQ Profile.

�During playback, the EQ Curve display in the corresponding mixer channel strip will change

based on the automation data and Playhead position.

Level Matcher

Level Matcher lets you quickly and accurately match the volume of disparate timeline clips to

each other.

To match your clip levels with the Level Matcher:


Right-click on the timeline clip you want to match and choose Clip Operations > Level Matching >

Capture Level Profile.

Timeline clip Level Matcher contextual menu


Right-click on a timeline clip you want to adjust and choose Clip Operations > Level Matching >

Apply Level Profile. Repeat this step for any other timeline clips you want to change.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

AI Dialogue Matcher

AI Dialogue Matcher is helpful when you need to match the ambient quality of one timeline clip to

another. For example, in a dialogue replacement scenario, you may need to make the newly recorded

dialogue sound like it was recorded in the same room as the rest of the on-location dialog.

Timeline clip AI Dialog Matcher contextual menu

To apply AI Dialogue Matcher:


Right-click the timeline clip you want to match and choose AI Tools > Dialogue Matcher > Capture

Dialogue Profile from the contextual menu.


When the audio has been analyzed, right-click the timeline regions you want to apply the profile to

and choose AI Tools > Dialogue Matcher > Apply Dialogue Profile from the contextual menu.

Once the dialogue profile is applied, you will see a checkmark next to the Enabled option in the

Dialogue Matcher contextual menu.

�Clicking this checkmark toggles the dialogue profile on and off.

�Selecting Remove Profile removes the profile from the clip entirely.

Audio Clip Layering

Audio layering is a special audio editing mode that lets you superimpose multiple audio clips in the

same track, with audio clips edited into the top layers muting overlapping sections of audio clips

appearing on lower layers. With audio layering enabled, superimposed audio clips are treated similarly

to superimposed video clips that have opacity set to 100%, with clips on top obscuring (or muting)

clips underneath.

An example of multiple audio performance editing using layers, where the top

layer mutes overlapping sections of audio clips in lower layers

Audio layering is incredibly useful for any situation where you’re combining segments of multiple

takes together to create a single voiceover, audio vocal track, or dramatic performance, as you can

choose which segments to use via their superimposed position in the stack of clips appearing in that

track, while at the same time you’re preserving the other takes underneath in case you might want

them later.

TIP: Track layering can be used on the Edit page as well.


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT

To enable audio layering:

�Choose Timeline > Layered Audio Editing so that a check mark appears by the command. All

overlapping audio will be layered instead of overwritten from that point forward.

To view audio layering:


Choose View > Show Audio Track Layers to reveal track layers for each audio track (and each lane

within a given audio track) in the Timeline. When layering is on, space appears at the top of each

track in the Timeline which provides a region into which you can edit layered audio clips.


To edit an audio clip or segment as a layer within a particular audio track, drag it from elsewhere

in the Timeline or from the Media Pool, and drop it into the empty area above whatever audio is

already in that track.

Dragging an audio clip to become layered above another clip


Edit the different superimposed layers of audio such that the segments of each take that you

like are on top. Only the topmost clip segments will be audible. Audio segments that overlap

underneath are silent. To put another layer on top, drag it from its current position to the empty

area at the top of the track.

Dragging a bottom audio layer to appear on top


When you’re finished editing clips in track layers, choose View > Show Audio Track Layers again

to hide the individual layers, so that only the topmost clips appear as a flat sequence in each

track and lane.

Hiding layers makes all audio layers appear on a single track, as if the top clips are

overwriting what’s underneath, except the muted material underneath is preserved


Fairlight | Chapter 175 Editing Basics in the Fairlight Page

FAIRLIGHT