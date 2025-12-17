---
title: "Chapter 18"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 70
---

# Chapter 18

Adding and

Organizing Media

with the Media Pool

Before you can edit or grade media, you need to add it to the Media Pool, which is

the central repository of clips in DaVinci Resolve. The Media Pool is a feature-rich

environment, giving you many different methods of importing clips into your project

and organizing them.

Contents

Copying Media Using the Clone Tool���������������������������������������������������������������������������������������������������������������������������������������� 370

Adding Media to the Media Pool��������������������������������������������������������������������������������������������������������������������������������������������������� 371

Basic Methods for Adding Media in the Media Page���������������������������������������������������������������������������������������������������������� 372

Adding Subclips From the Media Storage Panel������������������������������������������������������������������������������������������������������������������ 373

Adding Individual Frames From Image Sequences�������������������������������������������������������������������������������������������������������������� 374

Adding Media Based on EDLs��������������������������������������������������������������������������������������������������������������������������������������������������������� 374

Splitting Clips Based on EDLs�������������������������������������������������������������������������������������������������������������������������������������������������������� 375

Import Clips With Metadata Via Final Cut Pro 7 XML���������������������������������������������������������������������������������������������������������� 375

Adding Media With Offset Timecode������������������������������������������������������������������������������������������������������������������������������������������ 376

Import Blackmagic Cloud Shared Folders to Media Pool����������������������������������������������������������������������������������������������� 376

Sync Media Pool Bins with File System Folders������������������������������������������������������������������������������������������������������������������ 378

Adding Media to the Cut, Edit, Fusion, and Fairlight Pages������������������������������������������������������������������������������������������ 380

Removing Media From the Media Pool������������������������������������������������������������������������������������������������������������������������������������� 380

Removing Unused Media from a Project���������������������������������������������������������������������������������������������������������������������������������� 381

Adding and Removing External Mattes������������������������������������������������������������������������������������������������������������������������������������� 381

What Are Mattes For?������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 383

Adding Mattes���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 383

Using Embedded Mattes in OpenEXR Files���������������������������������������������������������������������������������������������������������������������������� 384


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Adding Offline Reference Movies����������������������������������������������������������������������������������������������������������������������������������������������� 384

Extracting Audio in Media Storage��������������������������������������������������������������������������������������������������������������������������������������������� 385

Manually Organizing the Media Pool����������������������������������������������������������������������������������������������������������������������������������������� 385

To Select Clips in the Media Pool������������������������������������������������������������������������������������������������������������������������������������������������� 385

Organizing Media into Bins�������������������������������������������������������������������������������������������������������������������������������������������������������������� 385

Import and Export DaVinci Resolve Project Bins (.drb)����������������������������������������������������������������������������������������������������� 386

Import and Export DaVinci Resolve Timelines (.drt)����������������������������������������������������������������������������������������������������������� 387

Sharing Media Among Projects Using Power Bins������������������������������������������������������������������������������������������������������������� 388

Automated Organization Using Smart Bins��������������������������������������������������������������������������������������������������������������������������� 389

Smart Bins Are Only As Good As Your Metadata����������������������������������������������������������������������������������������������������������������� 389

Smart Bins Update Their Contents Dynamically������������������������������������������������������������������������������������������������������������������� 389

Automatic Smart Bin Creation�������������������������������������������������������������������������������������������������������������������������������������������������������� 390

Manual Smart Bin Creation��������������������������������������������������������������������������������������������������������������������������������������������������������������� 391

Organizing Smart Bins������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 393

Duplicating Clips in the Media Pool������������������������������������������������������������������������������������������������������������������������������������������� 394

Duplicating Timelines������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 394

Choosing How to Display Bins������������������������������������������������������������������������������������������������������������������������������������������������������ 395

Showing Bins in Separate Windows�������������������������������������������������������������������������������������������������������������������������������������������� 395

Using the Media Pool in Thumbnail View��������������������������������������������������������������������������������������������������������������������������������� 395

Custom Sort of Clip Thumbnails in the Media Pool������������������������������������������������������������������������������������������������������������� 396

Working With Columns in List View��������������������������������������������������������������������������������������������������������������������������������������������� 396

Editable Name, Description, Keyword, and Comments Columns��������������������������������������������������������������������������������� 399

Using Metadata View in the Media Pool����������������������������������������������������������������������������������������������������������������������������������� 400

Finding Clips, Timelines, and Media������������������������������������������������������������������������������������������������������������������������������������������ 402

Finding Clips and/or Timelines Within the Media Pool������������������������������������������������������������������������������������������������������� 402

Finding Synced Audio������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 403

Finding Timeline Clips in the Media Pool���������������������������������������������������������������������������������������������������������������������������������� 403

Finding Timelines in the Media Pool������������������������������������������������������������������������������������������������������������������������������������������� 403

Finding Media in the Media Storage Panel and Finder ����������������������������������������������������������������������������������������������������� 403

Going Immediately to a File System Location in the Media Browser�������������������������������������������������������������������������� 404

Tracking Media Usage����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 404

Thumbnail Clip Usage Indicators�������������������������������������������������������������������������������������������������������������������������������������������������� 404

List View Clip Usage Column���������������������������������������������������������������������������������������������������������������������������������������������������������� 404

Relinking Media Simply��������������������������������������������������������������������������������������������������������������������������������������������������������������������� 405

Relink Media�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 405

Relink Selected Clips�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 406

Change Source Folder����������������������������������������������������������������������������������������������������������������������������������������������������������������������� 407


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Copying Media Using the Clone Tool

One of the few things you may want to do before you add media to your project is to clone all camera

original media onto a safe set of backup volumes, for redundancy in case any one volume fails.

Additionally, you should consider cloning all media to an off-site backup as well.

Whether you’re on-set working as a DIT, or doing data ingest at a post facility, the Clone Tool in the Media

page lets you safely and accurately copy media from SD cards, SSDs, or disk drives, to multiple destinations,

with a checksum report (based on a choice of six checksum options) written to the root of each destination

volume that verifies the absolute accuracy of the duplicate media saved to each destination.

To duplicate media using the Clone Tool:


Open the Clone Tool by clicking the Clone button at the far left of the Media Pool toolbar, which

reveals the Clone Tool palette.


Click the Add Job button at the bottom left to create a new job. A job item appears within the

Clone Tool palette, with overlays to guide you through its use.


Drag a volume or folder from the Media Storage panel to the “Drop source here” drop zone. Alternately,

you can right-click any volume or folder in the Media Storage panel and choose Set As Clone Source.


Next, drag one or more volumes or folders from the Media Storage panel to the “Drop destination

here” drop zone. Alternately, you can right-click any volume or folder in the Media Storage panel

and choose Set As Clone Destination. You can have more than one destination.


If you want to preserve the top level folder name from the source volume or folder, click the Clone

Tool panel’s option menu, and choose “Preserve Folder Name.” The overall folder structure of the

cloned media is always preserved.


If you want to change the checksum method used by DaVinci Resolve to verify that each clip

has copied properly, you can choose an option from the Checksum submenu of the Clone Tool’s

option menu. Each option is a tradeoff between the speed of your file copy operation and the

security of the verification process. Greater security generally means a slower copy operation.

The options are:

None: Disables data verification, sacrificing safety for speed.

File Size: Fast, but minimal data verification. Data verification is done simply by comparing the file

size of a duplicate file with that of the original. “Collision resistance” refers to whether two files (or a

file and an incorrectly duplicated file) may coincidentally have the same comparison value (be it file

size, an error-detecting code, or a hash). File Size is very fast, but it’s minimally collision resistant.

CRC 32: Faster than MD5, but less secure. An error-detecting code rather than the hash used

by the next three options. A “check value” is generated based on the remainder of a polynomial

division of the file’s contents. By comparing the check value derived from an original file with that

derived from a copy, data integrity can be verified. This is a much faster data verification scheme

than MD5 (the default), but it is significantly less collision resistant.

MD5: This is the default setting. A reasonable tradeoff between speed and security. A hash

function generates a 128-bit value that’s unique to a particular file; Data integrity is checked by

comparing the hash value generated by the original file to that generated by the copied file. MD5

is not as collision resistant as the SHA options, but it’s a faster operation, and the probability of

such collisions in conventional film and video workflows is probably small.

SHA 256, SHA 512: Slower, but more secure. SHA is a more collision resistant hash function

than MD5; options are provided for 256- and 512-bit value generation, with 512 being even more

collision resistant than 256. However, these options are progressively slower than MD5, and will

result in significantly slower copy times. Similarly to MD5, data integrity is checked by comparing

the hash value generated by the original file to that generated by the copied file.


When you’re ready, click the Clone button to initiate the cloning process.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

To duplicate media quickly using the Clone Tool:


Right-click any volume or folder in the Media Storage panel, and choose Set as Clone Source.

A job item appears within the Clone Tool palette, populated by the volume or folder you selected.


Next, right-click any volume or folder in the Media Storage panel, and choose Set As Clone

Destination. You can do this more than once because you can have more than one destination.


If you want to preserve the top level folder name from the source volume or folder, click the Clone

Tool panel’s option menu, and choose “Preserve Folder Name.” The overall folder structure of the

cloned media is always preserved.


When you’re ready, click the Clone button to initiate the cloning process.

The Clone tool with a job set up

Adding Media to the Media Pool

At minimum, you’ll be using the Media page to add clips to a project to begin editing, in preparation

to create dailies, or as a prelude to conforming a project using an EDL. All clips you want to work with

must first be added to the Media Pool to be available for grading and processing in DaVinci Resolve,

regardless of whether or not there’s edited project data to go along with it.

If you import XML or AAF projects, you can choose to automatically import all accompanying media

as part of the import process you initiate in the Edit page. However, if you find yourself needing to

replace updated effects or stock footage in the Timeline, or you’re called upon to add additional media

such as animated titles or superimposed clips for compositing, then you’ll still need to use the Media

page to do so.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Whatever kind of project you’re working on, you can add clips to the Media Pool from as many different

volumes as you need. All imported clips are linked to the original media on whichever disks you found

them; files are not moved, copied, or otherwise transcoded when you add them to the Media Pool.

Consequently, it’s a good idea to make sure that all media you want to import into your project has

already been copied to a suitably fast volume before importing it.

Basic Methods for Adding Media in the Media Page

There are several ways of adding clips to the Media Pool.

To add individual clips from the Media Storage panel to the Media Pool:


Use the Media Storage panel to find a media file to import.


If you have multiple bins available in the Bin list, choose the bin you want to add the

incoming media to.


Do one of the following:

Shift-click or Command-click multiple files, then right-click one of the selected files and

choose “Add into Media Pool.”

Drag a clip from the Media Storage panel browser to the Media Pool or to a specific

bin in the Bin list.


If a dialog appears asking if you want to change your project to match the criteria, click “Change”

to alter the project’s settings, or click “Don’t Change” to continue importing the media while

leaving the project at its previous frame rate. Once clips have been imported into the Media Pool,

the frame rate cannot be changed again, so choose carefully.

You also have the option of dragging media directly from the file system of supported platforms into

the Media Pool.

To drag one or more clips from the File System to the Media Pool (supported platforms only):


Select one or more clips in your File System.


Drag those clips into the Media Pool of DaVinci Resolve or to a specific bin in the Bin list.

Those clips are added to the Media Pool of your project.

If you need to add the contents of all directories and subdirectories to the Media Pool as a flat group

of media, that’s easily accomplished. A good example of this is when you’re importing camera original

media from a cloned file structure, in which clips are organized into subdirectories that are many levels

deep. DaVinci Resolve can easily import all of these clips and put them all into the same bin.

To add the entire contents of one or more directories of clips to the Media Pool:


Use the Media Storage panel to find and select one or more directories containing media files you

need to import.


If you have multiple bins available in the Bin list, select the specific bin you want to add the

incoming media to.


Do one of the following:

Right-click the selected directory or directories in the Media Storage panel, and choose

“Add Folder into Media Pool” to add only clips from the selected directory. Subdirectories

are ignored.

Right-click the directory in the Media Storage panel, and choose “Add Folder and

SubFolders into Media Pool” to add clips from the selected directory and those from all

subdirectories within.


Ingest and Organize Media | Chapter 18 Adding and Organizing Media with the Media Pool

MEDIA

Drag one or more selected directories you want from the Media Storage panel’s browser area

to the browser area of the Media Pool to add its contents, and the contents of all subdirectories

within, to the currently selected bin in the Bin list.

You also have the option of using the directories and subdirectories that organize media in

your file system as bins in the Media Pool, so that you can preserve the original organization

of your media.

To add all clips and folders in a directory organized into matching folders in the Media Pool:


Use the Media Storage panel to find the directory containing the files you need to import.


Do one of the following:


Right-click the directory and choose “Add Folder and SubFolders into Media Pool (Create Bins)”


Drag the folder you want to import from the Media Storage panel to the Bin list of the Media Pool

to add that folder, and all subfolders within, as a new bin in the Bin list.

A folder appears in the Media Pool with the same name as the folder you dragged in. All clips and all

subdirectories appear within, nested hierarchically in the Media Pool as they were in the file system.

Import Hierarchically Organized Nests of Empty Directories

You can also import a nested series of directories and subdirectories that constitutes a default

bin structure you’d like to bring into projects, even if those directories are empty, by dragging

them from your file system into the Media Pool Bin list of a project. The result is a hierarchically

nested series of bins that mimics the structure of the directories you imported. This is useful if

you want to use such a series of directories as a preset bin structure for new projects.