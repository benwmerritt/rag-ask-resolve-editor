---
title: "Legacy Bus Sends – “Auxiliaries”"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 698
---

# Legacy Bus Sends – “Auxiliaries”

Prior to DaVinci Resolve 17, the Bus Send panel was called Auxiliaries. Any projects created prior to

DaVinci Resolve 17 will use the legacy Fixed Busing. The only difference between the two is the use of

“Aux” to refer to sends in the windows and titles.

Pan

The Fairlight Mixer provides 2D and 3D pan controls that support various audio formats ranging from

mono and stereo to conventional 5.1 and 7.1 surround, as well as advanced immersive formats such as

Dolby Atmos, Ambisonics, Auro 3D, and NHK 22.2.

Channel Strip Pan Controls

The Pan section of each Channel Strip includes a Panning Indicator offering visualization and panning

control of left, right, front, and back.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Although you can open the Panner to access additional parameters by double-clicking the

Panning indicator, you can also do the following in the channel strip Pan section while the

Panner is closed:

Click and drag within the Pan Indicator to adjust the basic panning position.

•	 Single click to bypass panning.

•	 Command-drag to adjust the width on multichannel tracks.

•	 View the Boom level for surround channels, which is displayed as a horizontal blue line at

the bottom of the Panning Indicator.

Channel strip

Pan Indicator for

a stereo track

2D Panner Controls

Default View

The Pan window’s control set varies based on the mapping of the source audio. Panning adjustments

can be made by dragging the icons in the Panner Viewer or using the controls on the left side of

the window.

The Panner control window – Default 2D view


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

The default 2D version of the Audio Pan window includes the following controls:

�Pan Enable: Switches the Panner on and off.

�Spherical: This button changes the Panner interface from the default 2D view to the 2D Spherical

top-down view.

�3D: Clicking this button switches the interface to the 3D Cartesian view, offering controls for

working with immersive audio formats such as Dolby Atmos, Ambisonics, Auro 3D, and NHK 22.2,

as described in the 3D Pan Controls section below.

�Clicking the Spherical and 3D buttons switches the interface to the 3D Spherical view.

�Left/Right: Changes the balance of the signal between the left and right speakers, depending on

the speaker configuration you’re mixing for.

�Front/Back: Lets you adjust the balance of the signal between the front and rear speakers based

on the surround format you’re mixing in.

�Rotate: This controller rotates the sound source (or sources) around the listening position in the

center of the sound field.

�Spread: In the case of multichannel audio, this adjusts the spread or distance between the sound

sources. This is measured on a numeric scale of 1-99, where 1 is labeled PNT (“Point”) and 99 is

labeled FULL.

�Divergence: Determines the amount of signal bleed or spillover of a signal from one speaker into

adjacent loudspeakers, allowing the sound to occupy more of the sound field, with less focus

toward a single speaker position. The amount of signal bleed is represented by green horizontal

lines emanating from either side of each speaker position that increases in length as you raise the

parameter value.

2D: Clicking this button changes the appearance of the divergence indicators to circles.

�Boom: This adjusts the send level to the LFE part of the mix (the Low-Frequency Extension

subwoofer system).

On: Enables the Boom output.

Pre: Routes the LFE signal pre-fader.

Boom parameter

TIP: To constrain left/right position as you adjust panning, hold down the Shift key.

You can reset any rotary control to its default value by double-clicking it.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Spherical View

The Panner control window – Spherical view

Clicking the Spherical button at the top of the 2D Panner changes the interface to Spherical view,

which has the controls listed below including two parameters for Ambisonic panning:

�Azimuth: This control lets you rotate the sound source around the circumference of the sphere.

�Distance: This control adjusts the distance between the signal source and the listening position at

the center of the sphere.

�Rotate: This controller rotates the sound source (or sources) around the listening position in the

center of the sound field.

� Spread: In the case of multichannel audio, this adjusts the spread or distance between the sound

sources. This is measured on a numeric scale of 1-99, where 1 is labeled PNT (“Point”) and 99 is

labeled FULL.

�Size: This parameter is not active at the time of writing.

�2D: This parameter is not active at the time of writing.

�Boom: This adjusts the send level to the LFE part of the mix (the Low-Frequency Extension

subwoofer system).

�On: Enables the Boom output.

�Pre: Routes the LFE signal pre-fader.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

3D Panner Controls

DaVinci Resolve includes 3D Cartesian and Spherical versions of this Panner, which lets you do spatial

audio positioning when working in advanced surround formats such as Dolby Atmos, Ambisonics, Auro

3D, and NHK 22.2.

Cartesian View

The 3D Panner control window - Default Cartesian view

Clicking the 3D button changes the Panner interface to the default Cartesian view, which includes a

few more controls than the 2D Pan window:

�Pan enable: Toggles the Panner on and off.

�Snap: This button toggles Speaker Snap mode on and off for a given object. During playback,

Speaker Snap mode moves an audio object to the active speaker nearest its established location,

to prevent issues like phantom panning.

�Panner viewer: A large 3D representation of the virtual room, with a blue sphere representing the

position of the track’s audio.

Perspective Buttons: These buttons let you view the room from different preset angles. You

can freely rotate it by holding down Command-Option-Shift (Ctrl + Alt + Shift in Windows) while

dragging it. If you want to return to a default view, click one of the perspective buttons.

�Front panner: A 2D panning control that lets you make adjustments along the horizontal Left/Right

axis and the vertical Down/Up axis.

�Side panner: A 2D panning control that lets you make adjustments along the horizontal Front/Back

axis and the vertical Down/Up axis.

�Top panner: A 2D panning control that represents the horizontal left/right axis the vertical front/

back axis, letting you make these specific spatial adjustments.

�Left/Right: Changes the balance of the signal between the left and right speakers, depending on

the speaker configuration you’re mixing for.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

�Front/Back: Lets you adjust the balance of the signal between the front and rear speakers based

on the surround format you are mixing in.

�Down/Up: This lets you change the position of a sound source along the vertical axis.

�Height Mode Presets: Located to the right of the Down/Up control, these three height presets

lock the interaction of the Front/Back and Down/Up parameters together, providing fixed panning

paths that raise the height of a sound source to its maximum (100U), while moving it from one end

of the sound field to the other.

Freeform: This is the default setting for this section, which lets you adjust the Down/Up and Front/

Back controls independently.

Flyover: Moves the sound source upwards in a sharp arc to 100U, and then from one end of the

sound field to the other while maintaining maximum height.

Triangular: This preset moves the source diagonally up to 100U and immediately back down again

as it travels from one end of the sound field to the other.

Arc: Moves the sound source upwards in an arc to 100U and immediately back down in the same

manner as it travels from one end of the sound field to the other.

�Rotate: This controller rotates the sound source or mix around the listening position in the center

of the sound field.

�Tilt: This knob tilts a sound source or mix up to ninety degrees to either side so that it vertically

rotates or “swings” around the listening position in the center of the sound field.

�Spread: In the case of multichannel audio, this adjusts the spread or distance between the

sound sources. This is measured on a numeric scale of 1-99, where 1 is labeled PNT (“Point”) and

99 is labeled FULL.

�Divergence: Determines the amount of signal bleed or spillover of a signal from one speaker into

adjacent loudspeakers, allowing the sound to occupy more of the sound field, with less focus

toward a single speaker position. The amount of signal bleed is represented by green horizontal

lines emanating from either side of each speaker position that increases in length as you raise the

parameter value.

2D: Clicking this button changes the appearance of the divergence indicators to circles.

�Boom: This adjusts the send level to the LFE part of the mix (the Low-Frequency Extension

subwoofer system).

On: Enables the Boom output.

Pre: Routes the LFE signal pre-fader.

Only: Allows the panner to output an LFE signal only from the channel. The Boom level line in the

channel strip Pan Indicator is gray when this button is active.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Cartesian View — Dolby Atmos

The 3D Panner control window - Cartesian view – Dolby Atmos

When working in a Dolby Atmos workflow, the 3D Cartesian view of the Panner includes all the

features mentioned above for the default Cartesian view, with the addition of the following controls

located at the top of the interface:

NOTE: These controls are not available on Dolby Atmos busses.

�Elevation Button: This button hides and reveals the four top speakers in the Viewer.

�Zone: In addition to the option to view all speakers this dropdown menu offers five others that let

you include or exclude certain speakers from this object’s mix:

No Back: Hides the rear surround speakers.

No Sides: Hides the side surround speakers.

Center Back: Shows only the Center and Rear speakers.

Screen Only: Shows only the Center and Left and Right Front speakers.

Surr (Surround) Only: Show only the Surround speakers.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT

Spherical View

The 3D Spherical Panner control window

The 3D Spherical Panner lets you position your source anywhere in the sound field, including above

and below the listener. Spherical panning is based on Azimuth, Elevation, and Distance.

This view of the 3D panner offers the following controls:

�Azimuth: This control rotates the sound source around the circumference of the sphere.

�Elevation: This raises and lowers the sound source towards the top and bottom of the sphere,

which allows you to place it above or below the listener if you want.

�Distance: This control adjusts the distance between the signal source and the listening position at

the center of the sphere.

�Rotate: Rotates the sound source (or sources) around the listening position in the center of the

sound field.

�Spread: This control adjusts the spread or distance between the sound sources. This is measured

on a numeric scale of 1-99, where 1 is labeled PNT (“Point”) and 99 is labeled FULL.

�Size: This parameter is not active at the time of writing.

�Room: This parameter is not active at the time of writing.

�Pitch: This knob tilts the sound source or mix, forward or backward while rotating or “swinging” it

up to ninety degrees around the center listening position.

�Roll: This knob tilts a sound source or mix, up to ninety degrees to either side so that it vertically

rotates or “swings” around the center listening position.

�Panner viewer: A large 3D representation of the spherical sound field, with a blue sphere

representing the position of the track’s audio.

�Perspective Buttons: These buttons let you view the Sphere from different preset angles. You

can freely rotate it by holding down Command-Option-Shift (Ctrl + Alt + Shift in Windows) while

dragging it. If you want to return to a default view, click one of the perspective buttons.


Fairlight | Chapter 177 Mixing in the Fairlight Page

FAIRLIGHT