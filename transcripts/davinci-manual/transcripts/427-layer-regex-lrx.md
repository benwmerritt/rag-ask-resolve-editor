---
title: "Layer Regex  [LRx]"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 427
---

# Layer Regex  [LRx]

The Layer Regex node

Layer Regex Node Introduction

This tool uses complex expressions to filter out layers of multilayer files based on layer naming. Once a

filter has been defined, layers that meet the "expression" can be renamed, kept, or removed.

Inputs

The Layer Regex tool uses two inputs.

Image 1: This orange input is connected from a node with multilayer data that you want to filter.

Image 2: This green input is connected from a node with multilayer data that you want to filter.

Basic Node Setup

The Layer Regex node receives two nodes with multilayer data and lets you filter them using Regex

based on the layer names.


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

Layer Regex filters layers from two multi layer images.

Inspector

Layer Regex controls

Controls Tab

The Controls tab includes parameters for selecting layers to be used.

�Expression: Is the filter used for matching/locating characters.

�Mode: Lets you adjust how the expression will be applied.

Transform: Is the act of renaming/replacing characters.

Keep: Keeps the layers specified in the Expression rule.

Remove: Removes the layers specified in the Expression rule.

�Name Template: Is the rule applied to the “Expression," allowing you to replace characters or

rename layers.

�Unmatched: Determines how to deal with layers that don’t match the expression.

Keep: Any layers that don't match the Expression are kept; all the layers remain.

Remove: Any layers that don't match the Expression are removed. This isolates the layers that are

impacted by the expression.


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

�Tester: A simple tool to view the results of your expression as you change the parameters.

�Conflicts: Use this control to switch between either Image 1 or Image 2, the two inputs on this tool;

the selected Image will be output as the tool’s Default/[Main] layer.

Examples

Add a prefix to existing layer names

Expression: (.*)

Name Template: Right.$1

This will add Right. at the beginning of each of the layer names, giving you Right.Layer1 ,

Right.Layer2

NOTE: To add a suffix, change the order in the Name Template, $1.Right. This will give you

Layer1.Right , Layer2.Right

Find specific characters/words in the existing layers names, then add a prefix

Expression: (Right.*)

Name Template Stereo-$1

This will locate the layers which contain the word Right, then add the word Stereo- at the

beginning of each of the layer names, giving you Stereo-Right.Layer1

Find and replace

Expression: right(.*)

Name Template: Left$1

This will locate any layer names containing right and will then replace that layer name

with Left. So, layers labeled right.1 , right.2 , right.3 will be renamed to Left.1 ,

Left.2 , Left.3 .

Keep in mind, when using this method, any layer name that contains the letters right

(e.g., copyright) will be impacted by the expression and will be renamed. To specify a string of

characters, use the following expression ^right(.*)

NOTE: The ^ means match the start of the text. That will make it filter right but not copyright

because it has a copy at the start.

Find either word, then remove (or keep)

Expression: (copy|right)

Mode: Remove


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

(copy|right) locates copy and right , when the mode is set to Remove, layers containing

copy or right, are then removed from the layer list. This expression can be useful for locating

variations of a word, for example (copy|Copy|COPY)

NOTE: Setting the mode to Keep will retain layers that meet the Expression. Using the above

example, if the Mode is set to Keep, layers containing copy or right will remain and all other

layers are removed.

Find characters, ignoring case

Expression: (?i)(right)

This will capture all the characters in the word right, even if they are upper case. This means

any capitalized variation of the word right: Right, RIGHT or riGth will be captured.

RegEx Cheat Sheet

For more information on using RegEx https://www.debuggex.com/cheatsheet/regex/pcre

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Layer nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.

Layer Remover  [LRm]

The Layer Remover node

Layer Remover Node Introduction

This tool provides a simple way to disable/remove layers from a connected source.

Inputs

The Layer Remover tool uses one input.

Image 1: This orange input is connected from a node with multilayer data that you want to remove a

layer from.


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION

Basic Node Setup

The Layer Remover node receives a node with Multilayer data and lets you strip out specific layers

before passing on the image.

Layer Remover lets you disable specific layers of a multilayer file.

Inspector

Layer Remover controls

Controls Tab

The Controls tab presents a simple checklist of all the layers in the multilayer clip. Checking the box

will disable/remove layer(s) from the layer list.

Common Controls

Settings Tab

The Settings tab in the Inspector is also duplicated in other Layer nodes. These common controls are

described in detail at the end of this chapter in “The Common Controls” section.


Fusion Page Effects | Chapter 106 Layer Nodes

FUSION