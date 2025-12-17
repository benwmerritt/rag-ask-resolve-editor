---
title: "Chapter 190"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 738
---

# Chapter 190

Exporting Timelines

to Other Applications

Once you’ve completed editing and grading a program, you may need to export

your final graded timeline as EDL, AAF, XML, or OTIO files in order to send it to

another application for further finishing, effects work, or to complete a round trip

from an NLE.

To send a graded project to another application, you need to render the graded clips first using

the controls on the Deliver page to render the Timeline as individual source clips. In this mode, the

reel name and timecode metadata of each rendered clip is mirrored by the exported project file, to

maintain the correlation between exported EDL, XML, AAF, or OTIO data and the rendered media.

For detailed information about rendering in the Deliver page, see Chapter 184, “Rendering Media.”

If you render using the Easy Setups that correspond to Final Cut Pro XML or Avid AAF round trips,

then an XML or AAF will be exported to the same directory you’ve rendered to. However, you can still

export an XML, AAF, or EDL file separately should the need arise.

Alternately, if you’ve edited a project from scratch in DaVinci Resolve and need to move a timeline

to another application, you can export any timeline to any format for purposes of project exchange,

without the need to render new media (depending on your workflow).

Even in situations where you’ve imported a timeline from another application, the robust project

compatibility of DaVinci Resolve makes it possible to import one type of project exchange file, such

as XML, and then export a completely different kind, such as AAF or EDL. This lets you use DaVinci

Resolve as a project exchange utility.

Contents

Exporting Timelines from DaVinci Resolve�������������������������������������������������������������������������������������������������������������������������� 4091

Exporting to OTIO������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 4091

Exporting to AAF/XML�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4092

More About Exporting to AAF���������������������������������������������������������������������������������������������������������������������������������������������������� 4093

Exporting an EDL������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4093

Exporting a Missing Clips EDL��������������������������������������������������������������������������������������������������������������������������������������������������� 4094

Exporting Timeline Markers to EDL����������������������������������������������������������������������������������������������������������������������������������������� 4094

Exporting to CDL������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4095

Exporting the Edit Index as a CSV or TXT File������������������������������������������������������������������������������������������������������������������ 4096


Deliver | Chapter 190 Exporting Timelines to Other Applications

DELIVER

Exporting Timelines from DaVinci Resolve

Modern post-production is not a one-stop process. It’s a common need for timelines and assets to be

moved between many different applications from a multitude of companies. While DaVinci Resolve has

its own proprietary .drt format for use in passing timelines between DaVinici Resolve workstations, the

program also offers a robust toolset for moving your assets to many other popular applications.

As of this writing, the most reliable way to pass DaVinci Resolve timelines between

applications is as follows:

From DaVinci Resolve to/from another DaVinci Resolve workstation: Export/Import a

DaVinci Resolve Timeline file (.drt)

From DaVinci Resolve to/from another application: Export/Import an OpenTimelineIO file

(.otio, .otioz), if supported. If not supported, fall back to using XML or AAF flies instead.

Exporting to OTIO

DaVinci Resolve supports the Open Timeline IO (.otio) format for importing and exporting timelines

between applications. OTIO is an open source media and timeline interchange format created by the

Academy Software Foundation. It’s designed to be application and platform agnostic, allowing you to

pass your timeline and its media assets between programs with more compatibility than AAF or XML.

There are two different OTIO formats supported by DaVinci Resolve:

.otio: These files contain just the metadata about the timeline and no associated media.

They are small, portable, and require the end user to link the timeline to their own copies of

the media.

.otioz: These bundle files contain both the timeline metadata and all of the timeline’s media

assets zipped together into one file. As a result, this file can be very large, as it contains the

full length media files of all assets used in the timeline. However it assures that whoever

imports the file has all the media needed and is linked automatically to replicate the timeline

on their machine without error.

To Export an OpenTimelineIO (.otio, .otioz) file:


Select File > Export > Timeline (Shift-Command-O).


Type in a name for the timeline file.


In the file browser select either .otio files or .otioz bundle files in the format selector.


Click Save.

Exporting to ALE�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4096

Exporting to ALE with CDL����������������������������������������������������������������������������������������������������������������������������������������������������������� 4098

Exporting Timeline Markers to EDL����������������������������������������������������������������������������������������������������������������������������������������� 4099

Exporting and Importing Media Pool Metadata���������������������������������������������������������������������������������������������������������������� 4099


Deliver | Chapter 190 Exporting Timelines to Other Applications

DELIVER

NOTE: If you selected to export .otioz bundle files, an additional step of creating the OTIO

bundle will occur as it adds each complete media file from all clips in the timeline to the final

bundled file. This can take a long time and may need additional storage based on the length

and amount of media assets used.

Exporting to AAF/XML

Whether you’ve edited your project from scratch inside of DaVinci Resolve, or you’re doing a round trip

with an application that uses AAF, Final Cut Pro 7 XML, or Final Cut X XML project exchange formats,

you can export any DaVinci Resolve timeline in the Edit page to any project format DaVinci Resolve

supports. Whatever your workflow, keep the following in mind:

�Timelines are automatically exported when you render a timeline in the Deliver page: When you

use the “Final Cut Pro Round-Trip” or “Avid AAF Round-Trip” render setting presets, or a preset

created from one of them, a corresponding XML or AAF file is automatically exported along with

the media you render.

�Even if you’ve imported a project from another application, you can re-edit imported projects

before export: If necessary, you can freely re-edit projects you’re planning to export. When you

export an AAF or XML file, the Timeline will be sent back to the originating NLE, or onward to the

finishing application of choice.

�Unsupported effects are sometimes preserved in Round Trip workflows: If there were effects or

clip constructs in the original sequence that were not compatible with DaVinci Resolve, how those

effects will be handled depends on the project format you’re exporting to, and whether or not

you’ve edited the project. For XML projects, unsupported effects are saved internally by DaVinci

Resolve, and are exported with the XML file that you output no matter what. Consequently, they

should reappear when you reopen the exported file in the originating NLE. For AAF projects, you

can export unsupported effects as long as you don’t re-edit the project. However, if you do re-edit

the project, then you can only export an AAF file that’s been stripped of all unsupported effects.

�Project formats can be converted to other formats: Using DaVinci’s Export commands,

compatible project formats can be converted from one format to another. For example, an

imported EDL can be output as Final Cut Pro X XML. For that matter, Final Cut Pro 7 XML can

be imported and then exported as Final Cut X XML. Or, an AAF file from Media Composer can

be imported and then exported as a Final Cut Pro XML file to be opened in any NLE or finishing

application compatible with that format, such as Premiere Pro or Smoke.

To export an AAF or XML file after you’ve rendered the graded clips:

Do one of the following:


To export the current Timeline, choose File > Export AAF, XML, or press Shift-Command-O.

�Open the Edit page, right-click the Timeline you want to export in the Media Pool, and choose

Timelines > Export > AAF/XML.

�When the Export XML dialog appears, type a name for the file and choose a location for the

exported XML file, then click Save.


An XML version of that timeline is saved, complete with references to the graded media you

rendered, and is ready for import into an NLE or finishing application.


Deliver | Chapter 190 Exporting Timelines to Other Applications

DELIVER

More About Exporting to AAF

When you export to AAF, there are actually two options that are available to you, depending on

whether you made editorial changes to the Timeline in the Edit page:

If you didn’t make any editing changes to the Timeline you imported: You can choose

File > Export AAF, XML, and choose “AAF Files” from the Format dropdown menu. This

exports all audio and effects using data from the original AAF file that was exported from

Media Composer, regardless of whether or not they’re supported in DaVinci Resolve. When

you export an unedited AAF, DaVinci Resolve uses the Avid AAF file that you originally

imported to create an updated one; make sure it’s still in the same location as it was when you

first imported it into DaVinci Resolve.

If you made editing changes to the Timeline you imported, or you’re exporting a project

that wasn’t AAF to begin with: Then you need to right-click the Timeline you want to export

in the Media Pool and choose Timelines > Export > Generate New AAF. This option creates a

brand new AAF file, but audio and effects that are not supported in DaVinci Resolve in an AAF

import are discarded.

Exporting an EDL

DaVinci Resolve is also capable of exporting EDLs that can be reimported into other applications.

For more information about EDL workflows, see Chapter 24, “Ingesting From Tape.” see

Chapter 56, “Conforming and Relinking Clips.” and Chapter 60, “Conforming EDL Files.”

To export an EDL:


Open the Edit page and select the Timeline you want to export an EDL from in the Media Pool.


Exported EDLs only have a single video track. For timelines with multiple tracks, only the events

on the video track with the destination control assigned to it will be exported (the destination

control is the first control at the left in the track header). If you want to export a track other than

Video 1, you can assign the destination control to the specific track you need to export.


Right-click the Timeline in the Media Pool, and choose Timelines > Export > AAF/XML/EDL from

the contextual menu.


When the Export Timeline dialog appears, type a name, choose a location for the exported EDL,

and choose EDL Files from the dropdown menu at the bottom, then click Save. An EDL

is exported.


Deliver | Chapter 190 Exporting Timelines to Other Applications

DELIVER

Exporting a Missing Clips EDL

This command lets you export a quick report listing all clips that are offline in the currently selected

track of the Timeline in the Edit page. This report is in EDL format, with one event for each clip that’s

offline, which describes the reel number and source timecode of the missing media, as well as the

record timecode of the missing media’s position on the Timeline.

Here’s an example of an exported Missing Clips EDL:

TITLE: ( no title )


A001_C002_0820GA_001 V

C

10:28:27:03

10:28:28:00

01:00:00:00

01:00:00:21


A004_C012_0820MC_001 V

C

14:07:31:21

14:07:35:13

01:00:12:13

01:00:16:05


A017_C001_0820CV_001 V

C

21:16:14:22

21:16:15:00

01:00:16:05

01:00:16:07

Once you’ve exported this information, you can hand it off to whomever can help you track down the

missing media.

To export a Missing Clips EDL:


Open the Edit page and open the Timeline you want to export a Missing Clips EDL for in the

Timeline browser.


For timelines with multiple tracks, only the events on the video track with the destination control

assigned to it will be examined for missing clips. If you want to examine a track other than Video 1,

you can assign the destination control to the specific track you need to examine for missing clips.


Right-click the Timeline in the Media Pool, and choose Timelines > Export > Missing Clips EDL

from the contextual menu.


When the Save Missing Clips EDL dialog appears, type a name and choose a location for the

exported EDL, then click Save.

Exporting Timeline Markers to EDL

If you keep notes about a project within the notes field of Timeline markers, found in the Timeline ruler,

then it’s possible to export those notes as an EDL.

To export timeline markers as an EDL:


Right-click that timeline in the Media Pool, and choose Timelines > Export > Timeline

Markers to EDL.


Choose a location and export format from the Export Edit Index dialog, and click Save. Each

Timeline marker is listed in the resulting EDL, with any notes included along with a duration,

where applicable.


Deliver | Chapter 190 Exporting Timelines to Other Applications

DELIVER