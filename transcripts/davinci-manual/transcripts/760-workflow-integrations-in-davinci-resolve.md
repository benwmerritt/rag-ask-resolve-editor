---
title: "Workflow Integrations in DaVinci Resolve"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 760
---

# Workflow Integrations in DaVinci Resolve

(Studio Version Only)

DaVinci Resolve allows third parties to create their own custom interface plugins using scripting

languages. This makes possible a direct integration between DaVinci Resolve and other software

programs, for a variety of uses. More than one Integration plugin can be active at the same time.

After installation, plugins can be enabled in DaVinci Resolve by going to Workspace > Workflow

Integrations, and selecting your plugin from the dropdown menu.

Creating Workflow Integration Plugins

Users can write their own Workflow Integration Plugin (an Electron app), using Resolve Javascript’s

API, and  Python or Lua scripts. For more information on how to create a Workflow Integration Plugin

go to Help > Documentation > Developer, and open up the Workflow Integrations folder for technical

details and sample code.

Workflow Integration Plugins

There are several Media Asset Management (MAM) systems that can now directly be accessed

through DaVinci Resolve using the Workflow Integration Plugins.

EditShare

EditShare has created a workflow integration plugin that allows DaVinci Resolve to interface directly

with their FLOW media management system. This plugin allows you to comment, search, and preview

media in FLOW without leaving DaVinci Resolve. You can also upload revisions, manage proxy media,

and maintain full metadata support throughout the process.

For more information on this plugin and how FLOW works with DaVinci Resolve go to:

editshare.com/say-hello-to-flow-and-davinci-resolve-studio/

EditShare’s FLOW Integration Plugin


Advanced Workflows | Chapter 199 Workflow Integrations

DELIVER

Studio Network Solutions (SNS)

Studio Network Solutions (SNS) created the ShareBrowser Integration Plugin to interface between

DaVinci Resolve and their ShareBrowser media asset management software, included with

SNS EVO media servers. This plugin allows your team to search, tag, preview, comment, organize, and

import media without leaving the DaVinci Resolve interface. Your team can directly import the media

into a DaVinci Resolve project and the metadata you entered carries over along with the media.

For more information on this plugin and how SNS’s high-speed server or cloud solutions work

with DaVinci Resolve, go to: www.studionetworksolutions.com.

SNS ShareBrowser Integration Plugin


Advanced Workflows | Chapter 199 Workflow Integrations

DELIVER

Codec Plugins (Studio Version Only)

Codec plugins allow third parties to install new codecs for encoding in the Deliver page that are not

currently supported in the main DaVinci Resolve software. This opens the door for extremely specific

deliverables that would normally require passes through multiple programs to deliver.

MainConcept

The MainConcept Codec Plugin allows you to render your DaVinci Resolve Studio timelines in a variety

of new codecs:

•	 AS-11 UK SD, AS-11 UK HD along with an included XML metadata file to create AS-11 UK DPP

compliant content.

•	 MainConcept’s software HEVC Main and Main 10 profiles, allowing H.265 files in 8-bit/10-bit

4:2:0/4:2:2 at up to 8K resolution.

•	 MainConcept MXF and MP4, allowing encoding into the native camera formats used by

Sony XAVC/XDCAM and Panasonic P2 AVC based cameras.

More information on the MainConcept Codec Plugin for DaVinci Resolve can be found here:

www.mainconcept.com/blackmagic-plugins

The MainConcept Codec Plugin for DaVinci Resolve

options in the Deliver page


Advanced Workflows | Chapter 199 Workflow Integrations

DELIVER

Chapter 200

Creating DCTL LUTs

This chapter describes how to create DCTL LUTs to perform your own custom

mathematical transformations in DaVinci Resolve.

Contents

About DCTL�������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4211

DCTL Syntax������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 4211

A Simple DCT LUT Example��������������������������������������������������������������������������������������������������������������������������������������������������������� 4213

A Matrix DCT LUT Example����������������������������������������������������������������������������������������������������������������������������������������������������������� 4213

A More Complex DCT LUT Example����������������������������������������������������������������������������������������������������������������������������������������� 4214


Advanced Workflows | Chapter 200 Creating DCTL LUTs

DELIVER

About DCTL

DCTL files are actually color transformation scripts that DaVinci Resolve sees and applies just like

any other LUT. Unlike other LUTs, which are 1D or 3D lookup tables of values that approximate image

transformations using interpolation, DCTL files are actually comprised of computer code that directly

transforms images using combinations of math functions that you devise. Additionally, DCTL files run

natively on the GPU of your workstation, so they can be fast.

Anyone with the mathematical know-how can make and install a DCTL. Simply enter your

transformation code, using a syntax that’s similar to C (described in more detail below), into any text

editor capable of saving a plain ASCII text file, and make sure its name ends with the “.dctl” (DaVinci

Color Transform Language) file extension. Once that’s done, move the file to the LUT directory of your

workstation. Where that is depends on which OS you’re using:

On Mac OS X: Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/

On Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT

On Linux: /home/resolve/LUT

When DaVinci Resolve starts up, assuming the syntax of your .dctl is correct, they appear in the

Color page Node contextual menu within the DaVinci CTL submenu.

DCTL Syntax

Users need to put __DEVICE__ in front of each function they write. For example:

__DEVICE__ float2 DoSomething()

The main entry function (transform) should come after all other functions, with the following

format argument:

__DEVICE__ float3 transform(float p_R, float p_G, float p_B)

The main entry function must also have a float3 return value.

For the following floating point math functions, please use the described syntax:

float _fabs(float)

// Absolute Value

float _powf(float x, float y

// Compute x to the power of y

float _logf(float)

// Natural logarithm

float _log2f(float)

// Base 2 logarithm

float _log10f(float)

// Base 10 logarithm

float _exp2f(float)

// Exponential base 2

float _expf(float)

// Exponential base E

float _copysignf(float x, float y)

// Return x with sign changed to sign y

float _fmaxf(float x, float y)

// Return y if x < y

float _fminf(float x, float y)

// Return y if x > y


Advanced Workflows | Chapter 200 Creating DCTL LUTs

DELIVER

float _saturatef(float x, float

minVal, float maxVal)

// Return min(max(x, minVal), maxVal)

float _sqrtf(float)

// Square root

int   _ceil(float

// Round to integer toward + infinity

int   _floor(float)

// Round to integer toward - infinity

float _fmod(float x, float y)

// Modulus. Returns x – y * trunc(x / y)

float _fremainder(float x, float y)

// Floating point remainder

int   _round(float x)

// Integral value nearest to x rounding

float _hypotf(float x, float y)

// Square root of (x^2 + y^2)

float _atan2f(float x)

// Arc tangent of (y / x)

float _sinf(float x)

// Sine

float _cosf(float x)

// Cosine

float _acosf(float x)

// Arc cosine

float _asinf(float x)

// Arc sine

float _fdivide(float x, float y)

// Return (x / y)

float _frecip(float x)

// Return (1 / x)

The following functions support integer type:

min, max, abs, rotate

Other supported C Math functions include:

acosh, acospi, asinh, asinpi, atan, atanh, atanpi, atan2pi, cbrt, cosh, cospi,

exp10, expm1, trunc, fdim, fma, lgamma, log1p, logb, rint, round, rsqrt,

sincos, sinh, sinpi, tan, tanh, tanpi, tgamma

Vector types float2, float3, and float4 are supported. The data fields are:

float x

float y

float z

float w

To generate a vector value, use make_floatN() where N = 2, 3, or 4.

Users can define their own structure using “typedef struct.” For example:

typedef struct

{

float c00, c01, c02;

float c10, c11, c12;

} Matrix;


Advanced Workflows | Chapter 200 Creating DCTL LUTs

DELIVER

To declare constant memory, use __CONSTANT__. For example:

__CONSTANT__ float NORM[] = {1.0f / 3.0f, 1.0f / 3.0f, 1.0f / 3.0f};

To pass the constant memory as a function argument, use the __CONSTANTREF__ qualifier, e.g.:

__DEVICE__ float DoSomething(__CONSTANTREF__ float* p_Params)

A float value must have the ‘f’ character at the end (e.g. 1.2f).