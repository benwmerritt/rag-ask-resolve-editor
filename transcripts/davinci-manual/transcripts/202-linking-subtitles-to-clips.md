---
title: "Linking Subtitles to Clips"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 202
---

# Linking Subtitles to Clips

If you like, you can link one or more subtitles to their accompanying clip, so that if you re-edit

a subtitled scene, each clip’s subtitles move along with the clips. This arrangement doesn’t always

work the way you’d expect when trimming, but it works great when you’re rearranging clips.

To link a subtitle to another clip:


Select a clip and its subtitles all at once.

Selecting a video clip and its

accompanying subtitle to link them


Choose Clip > Linked Clips (Option-Command-L). A Link icon appears to show

that the subtitle clips are linked to the video/audio clip.

The now linked clip and subtitle have

link badges to show their state


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

Using Subtitles in Nested Timelines

Subtitles will come across with their original timelines as part of a nested timeline. Simply drag one

subtitled timeline either from the Media Pool or Source Viewer into a new timeline. If you want to add

the subtitles of the original timeline to the new timeline’s caption list, you must Decompose in Place

the nested timeline.

Subtitle Regions

Occasionally you will need to display multiple subtitles on the screen at the same time. A common

example of this is having two characters on screen with overlapping dialog. By arranging the subtitles

appropriately, their position on the screen can indicate which person is speaking each subtitle.

Subtitle regions allow you to have multiple subtitle clips active and overlapping at the same time, while

still being contained in a single overall subtitle track.

Adding and Deleting Subtitle Regions

By default, all subtitles created in a subtitle track are in Region 1 (R1) at the base layer of the track. If

you wish to add another subtitle region you must create a new subtitle region in the subtitle track. You

can have a maximum of three subtitle regions (R1, R2, R3) for any subtitle track, meaning you can have

up to three separate subtitles on screen concurrently.

To add a new subtitle region:


Right click inside the current subtitle track (not the track header, but timeline track itself).


Select Add Subtitle Region. This will split the subtitle track horizontally and create a new region.

To delete a subtitle region:


Right click inside the current subtitle track (not the track header, but timeline track itself).


Select Delete Subtitle Region, and select the region you want to delete from the submenu.

Adding and deleting subtitle regions from the subtitle track

Using Subtitle Regions

Once multiple regions are created, you can treat the subtitle track like a separate mini-timeline with

four layers. Each subtitle region has its own Captions list and Style settings, including font choice, and

most importantly, text position. This allows you to set up, say, the default region as your normal subtitle

layout, Region 2 for characters on the left hand side of the screen, and Region 3 for characters on

the right.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

When more than one region overlaps each other in the subtitle track, all subtitles at that position will

be visible. You can move a caption from region to region by dragging the subtitle clip up or down

inside the subtitle track.

For the example below there are two subtitles on a standard subtitle track. However, these two lines

are delivered in the same two-shot with both actors slightly overlapping each other, so it makes more

sense to see both subtitles at the same time rather than sequentially.

By adding an additional subtitle region and positioning the subtitle clip in the timeline exactly where

the actress steps on the actors line, you can link the timing of the caption to better reflect the

performance in the scene. Additionally, the new subtitle region’s text position was changed to appear

on the right hand side of the frame where the actress delivering the line is located. This helps indicate

which of the two actors is saying each line.

The initial sequential subtitle track

The same subtitle track but with a new region added, allowing both subtitles to be show concurrently


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

Naming Subtitle Tracks

If necessary, you can double-click the name of any subtitle track to rename it to something more

descriptive of what that subtitle track will contain, such as the language, and whether a particular track

is for subtitles or closed captions.

Depending on your workflow and delivery specifications, there are existing conventions for identifying

languages, such as ISO-639-1 (governing 2-letter codes) or ISO-639-2/B (governing 3-letter codes).

These codes can be found at the International Organization for Standardization website, at

http://www.loc.gov/standards/iso639-2/php/code_list.php.

Some naming conventions require both language code and country code. For example, Facebook

requires SubRip (.srt) files with the naming format “VideoFilename.[language code]_[country code].srt”

for proper embedding.

If you want to use these codes for subtitle track identification and output, here’s a representative list of

standardized language and country codes from around the world, in alphabetical order:

Language

ISO 639-1

Language Code

ISO 639-2

Language Code

ISO 3166-1

Country Code

Amharic

am

amh

ET (Ethiopia)

Arabic

ar

ara

EG (Egypt)

AE (United Arab Emirates)

LB (Lebanon)

Bengali

bn

ben

IN (India)

Chinese

zh

chi (B)

zho (T

CN (China)

HK (Hong Kong)

TW (Taiwan)

Danish

da

dan

DK (Denmark)

Dutch

nl

dut (B)

nld (T)

NL (Netherlands)

English

en

eng

GB (UK)

IN (India)

US (US)

Finnish

fi

fin

FI (Finland)

French

fr

fre (B)

fra (T)

CA (Canada)

FR (France)

German

de

ger (B)

deu (T)

DE (Germany)

Greek Modern

el

gre (B)

ell (T)

GR (Greece)

Hausa

ha

hau

NG (Nigeria)

TD (Chad)

Hebrew

he

heb

IL (Israel)

Hindi

hi

hin

IN (India)

Indonesian

id

ind

ID (Indonesia)


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT

Language

ISO 639-1

Language Code

ISO 639-2

Language Code

ISO 3166-1

Country Code

Italian

it

ita

IT (Italy)

Japanese

ja

jpn

JP (Japan)

Malay

ms

may (B)

msa (T)

MY (Malaysia)

Maori

mi

mao (B)

mri (T)

NZ (New Zealand)

Norwegian

no

nor

NO (Norway)

Polish

pl

pol

PL (Poland)

Portuguese

pt

por

BR (Brazil)

PT (Portugal)

Punjabi

pa

pan

IN (India)

Russian

ru

rus

RU (Russia)

Spanish Castilian

es

spa

CO (Columbia)

ES (Spain)

MX (Mexico)

Swahili

sw

swa

KE (Kenya)

Swedish

sv

swe

SE (Sweden)

Tagalog

tl

tgl

PH (Philippines)

Thai

th

tha

TH (Thailand)

Turkish

tr

tur

TR (Turkey)

Urdu

ur

urd

PK (Pakistan)

Vietnamese

vi

vie

VN (Vietnam)

Exporting Subtitles and Closed Captions

Once you’ve created one or more subtitle tracks filled with subtitles or captions, there are a few

different ways you can export subtitles once you’ve created them.

Exporting Subtitles Via the File Menu

Choose File > Export Subtitle, and use the export dialog to choose a location and file type for the

exported subtitle file. You can export subtitles in the .srt and .vtt formats.

Exporting Subtitles Via the Subtitle Track Header

Right-click on the track header of a subtitle track, and choose Export Subtitle from the contextual

menu. Use the export dialog to choose a location and file type for the exported subtitle file. You can

export subtitles in the .srt and .vtt formats.


Editing Effects and Transitions | Chapter 52 Subtitles and Closed Captioning

EDIT