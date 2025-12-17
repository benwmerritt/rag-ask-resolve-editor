---
title: "Dolby Vision Metadata"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 735
---

# Dolby Vision Metadata

The Dolby Vision metadata from the imported DCP/IMF file can be reused by selecting

“Original Metadata” from the Tone Map Using dropdown menu of the Dolby Vision palette

in the Color Page

Setting a clip to Original Metadata in the Color Page

Alternatively, this metadata can be imported separately from an existing XML via the “Import

Metadata from XML” command in the option menu of the Dolby Vision palette in the Color page.

When successful, “Imported Metadata” will be enabled.

Exporting

You can export a supplemental package by turning on “Supplemental Package” in the the video panel

of the Deliver page Render Settings list.

Setting an export to be a

Supplemental Package

The codec type and profile will be automatically selected to match the original version of the DCP/IMF

package, and the audio tracks are set to match the Timeline tracks. Please ensure the rest of these

audio settings are matched to the original version, since they start out set to the default values.


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER

Setting the audio settings of a Supplemental Package export

Photon Validation of IMF Packages

Photon is Netflix’s validation software for IMF App2/App2e packages. The option for using Photon

validation will only be shown on Resolve Studio with JDK/JRE version 1.8 and above installed, which is

available at https://github.com/Netflix/photon.

NOTE: Please disable “Use easyDCP decoder” from “Preference” as there can be issues

decoding IMF packages without an easyDCP license.

Validating in the Media Pool

An existing IMF package can be validated with Photon by importing it into the Media Pool, then right-

clicking it and choosing “Perform Photon Validation” from the context menu.

Validating an IMF in the Media Pool


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER

A report dialog will be shown when the validation is completed.

A validation report

Validating on Export

Photon validation can be enabled in the File panel of the Deliver page Render Settings; choosing the

“IMF Netflix” preset will also enable this option. When enabled, DaVinci Resolve will perform Photon

validation after the IMF package is exported. The validation report will be saved to a text file in the IMF

package folder, and a report dialog will be shown if there is any error.

Enabling Photon validation on export


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER

Using and Licensing EasyDCP

Both DaVinci Resolve and DaVinci Resolve Studio include a demo version of easyDCP. Details of

operation and restrictions of the demo version can be found later in this chapter. The fully functional

version of easyDCP operates via licensing modules purchased from http://www.easyDCP.com (info@

easyDCP.com) and every new DaVinci Resolve system (server) needs its own license and specific

certificates for DCP and KDM generation and for playback of DCPs.

Requesting Your Server Certificate Set

For your DaVinci Resolve system to generate DCPs and KDMs you need to request a specific set of

configuration files called the Server Certificate Set. To begin, first purchase your encoding, encryption,

decoding, and decryption modules from easyDCP. They will provide a password to access your

easyDCP account.

Then, from the DaVinci Resolve File menu, select easyDCP > Request Server Certificate Set. Fill in

the detail listed on the request form and save the form to your desktop or somewhere it can be easily

found. This html file can be emailed to info@easyDCP.com. After sending the html, a customized

Server Certificate Set for your installation will be generated and made available for download in your

easyDCP Website User Account.

The Server Certificate Set generated for your DaVinci Resolve will contain files based on your

purchased modules and your specific DaVinci Resolve server hardware. The table below shows the

modules and the licenses and certificates generated, followed by a brief description of each item.

License

Server Certificate

Signer Certificate

DCP Encoder

X



X

DCP Encoder with Encryption

X

X

X

DCP Player

X

DCP Player with Encryption

X

X

License: The License is used to activate the purchased modules on a specific

hardware server.

Server Certificate: Each DCP render (referred in the industry as an “Instance”) using

encryption or decryption has an individual server certificate. This certificate is required to be

able to receive Key Delivery Messages (KDMs), which unlock encrypted DCPs.

Signer Certificate: A Signer Certificate is used to sign certain files within a DCP package and/

or Key Delivery Message (KDM) to verify which authority generated the DCP instance.

Importing Your Server Certificate Set

Once generated and downloaded to your DaVinci Resolve server, the Server Certificate Set needs to

be imported into DaVinci Resolve.


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER

To import your server certificate:


Choose File > easyDCP > Import License and Certificates.


Use the Import Server Certificate dialog to select the file, enter your Certificate Set password,

then click Import.


To verify your easyDCP license and the Server Certificates, choose easyDCP > About easyDCP.

From this point onward, you can use the controls from within the Settings window, the Deliver page,

and the File menu to master and play DCPs.

Limitations of the Demo Version of easyDCP

The demo version of the DCP encoder embeds visible DaVinci Resolve and easyDCP logo

watermarks in the rendered Digital Cinema Package (DCP) images. The demo version does

not include encryption so these DCPs can be used for screening in a digital equipped cinema.

The demo version of the DCP playback module will play 15 seconds in full quality. After that

playback quality reduces drastically. Furthermore, audio won’t be rendered after 15 seconds

of playback.

Switching Between Native DCP

and EasyDCP Encoding

A checkbox in the Configuration panel of the System Preferences, “Use EasyDCP Encoder,” lets you

choose whether to use the native DCP/IMF encoding in DaVinci Resolve, or your licensed EasyDCP

software. In either case, all set up happens from within the Deliver page of DaVinci Resolve.

EasyDCP Color Management

The Color Management panel of the Project Settings has a Timeline Colorspace dropdown menu that

is enabled for EasyDCP encoding regardless of whether or not DaVinci Resolve Color Management is

used for the current project (the same setting is used for both color management tasks). You should

set this to the color space used by your current DaVinci Resolve timeline. If, for example, you are

grading using a Rec. 709 monitor for television deliverables but also wish to make a DCP, select Rec.

709 Gamma 2.4 and DaVinci Resolve will render the DCP with the correct Rec. 709 to XYZ matrix.

EasyDCP Output in the Deliver Page

To master to a DCP in the Deliver page, use the following procedure, which walks you through all of

the easyDCP settings that are available in the Render Settings list.

To master a DCP or IMF:


Set “Render timeline as” to Single clip.


Choose easyDCP from the Video Format dropdown.


Choose the appropriate option from the Codec dropdown that corresponds to the type (DCP or

IMF) resolution (2K or 4K), and aspect ratio (native, scope, or flat) of your intended output.


Deliver | Chapter 188 Delivering DCP and IMF

DELIVER


Set the Composition Name. This field is intended to hold a standardized name for the DCP being

encoded. You can either type a name into this field directly, or you can press the “...” button to

open the easyDCP Composition Name Generator window. An editable Film Title field appears,

along with a number of dropdown menus that let you select various DCP attributes such as

content type, aspect ratio, language of audio and subtitles, and so forth. As you populate each

attribute, the name being generated appears at the top of the window, and clicking OK copies the

resulting Composition Name into the Composition Name field of the Render Settings.


If necessary, set the desired “Maximum DCP bit rate” by either typing or dragging within the field

(the range is 50 to 250 Mbit/sec). If you’re not sure what data rate to use, consult the client or

distributor to whom you’re delivering the DCP.


There are two DCP package types you can output, determined by the “Use Interop

packaging” checkbox:

�The standard package conforms to the “Interop” specifications for DCPs, which is turned on

by default. With “Use Interop packaging” turned on, however, the frame rate of your output is

limited to either 24fps or 48fps, so you need to make sure that your timeline conforms to these

frame rates.

�If you want to generate DCP packages with other frame rates to match your timeline, you

need to turn “Use Interop packaging” off to generate a SMPTE-standard DCP. This supports

additional frame rates including 25, 30, 50, and 60 fps. However, SMPTE-Standard-DCPs are not

supported on all JPEG2000-based playback systems so it’s generally recommended to use the

Interop standard unless you know the player supports the SMPTE-Standard DCPs.


Turn on the “Encrypt package” checkbox to encode an encrypted DCP. This sets the encoder

to generate a Digest containing the keys used during encryption. This Digest will allow you to

play the resulting DCP on your system, and to generate KDMs to allow that DCP to be played on

other servers.

NOTE: If you do not encrypt the DCP it can be played on any DCP player/decoder

without restriction.


Set the Subtitles Path. If you have a properly formatted subtitle file, click the Browse button to

link to it.


If you’re including an audio mix in the DCP, go to the Audio section, turn on the Render audio

checkbox, and choose the number of channels in the “Render channels of audio” dropdown menu

that corresponds to the number of Audio Mixer output channels defined in the Edit page.

10	 Click the Browse button under the “Render to” field, and choose a location for the resulting DCP.

Make sure you pick a drive with enough room for the estimated size of the final DCP.

11	 Choose all necessary options from the Output Options to ensure the quality you need.

12	 Click the Add Job to Render Queue button, and then click Start Render to create your DCP.

A DCP will be created and placed at the location you chose, ready for playback or delivery.