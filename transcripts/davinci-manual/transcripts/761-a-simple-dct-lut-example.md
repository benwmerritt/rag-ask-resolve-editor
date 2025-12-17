---
title: "A Simple DCT LUT Example"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 761
---

# A Simple DCT LUT Example

The following code shows an example of how to create a simple color gain transformation using the

DCT LUT syntax.

// Example to demonstrate simple color gain transformation

__DEVICE__ float3 transform(float p_R, float p_G, float p_B)

{

const float r = p_R * 1.2f;

const float g = p_G * 1.1f;

const float b = p_B * 1.2f;

return make_float3(r, g, b);

}

A Matrix DCT LUT Example

The following code shows an example of creating a matrix transform using the DCT LUT syntax.

// Example to demonstrate the usage of user defined matrix type to transform RGB to YUV in Rec. 709

__CONSTANT__ float RGBToYUVMat[9] = { 0.2126f ,  0.7152f , 0.0722f,

-0.09991f, -0.33609f, 0.436f,

0.615f  , -0.55861f, -0.05639f };

__DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y,

float p_R, float p_G, float p_B)

{

float3 result;

result.x = RGBToYUVMat[0] * p_R + RGBToYUVMat[1] * p_G + RGBToYUVMat[2] *

p_B;

result.y = RGBToYUVMat[3] * p_R + RGBToYUVMat[4] * p_G + RGBToYUVMat[5] *

p_B;

result.z = RGBToYUVMat[6] * p_R + RGBToYUVMat[7] * p_G + RGBToYUVMat[8] *

p_B;

return result;

}


Advanced Workflows | Chapter 200 Creating DCTL LUTs

DELIVER

A More Complex DCT LUT Example

The following code shows an example of creating a mirror effect, illustrating how you can access

pixels spatially.

// Example of spatial access for mirror effect

__DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, __

TEXTURE__ p_TexR, __TEXTURE__ p_TexG, __TEXTURE__ p_TexB)

{

const bool isMirror = (p_X < (p_Width / 2));

const float r = (isMirror) ? _tex2D(p_TexR, p_X, p_Y) : _tex2D(p_TexR, p_

Width - 1 - p_X, p_Y);

const float g = (isMirror) ? _tex2D(p_TexG, p_X, p_Y) : _tex2D(p_TexG, p_

Width - 1 - p_X, p_Y);

const float b = (isMirror) ? _tex2D(p_TexB, p_X, p_Y) : _tex2D(p_TexB, p_

Width - 1 - p_X, p_Y);

return make_float3(r, g, b);

}


Advanced Workflows | Chapter 200 Creating DCTL LUTs

DELIVER

Chapter 201

TCP Protocol for

DaVinci Resolve

Transport Control

This chapter describes how to create third-party utilities that

use Transport Control with DaVinci Resolve.

Contents

About the TCP Protocol Version 1.2����������������������������������������������������������������������������������������������������������������������������������������� 4216

Data Types �������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4216

Command Format ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 4216

Response Format ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4216

Communication Delays ������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4216

Status Response Values ������������������������������������������������������������������������������������������������������������������������������������������������������������������ 4217

TCP Protocol Stream ������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 4217

connect ���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4217

goto ����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4217

play ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 4217

gettc ���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4217

getframerate ����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 4217


Advanced Workflows | Chapter 201 TCP Protocol for DaVinci Resolve Transport Control

DELIVER

About the TCP Protocol Version 1.2

This protocol defines the communication standard between third-party applications (“Client”) and

DaVinci Resolve (“Server”) using the TCP protocol.

Port number 9060 will be used by the server. SSL will not be used in this protocol. Communication

takes the form of request-response messages, where the Client initiates a command, and the Server

responds appropriately.

To use this protocol, you must first type the following string into the Advanced panel of the DaVinci

Resolve System Preferences:

System.Remote.Control = 1

Data Types

The following data types are used in this protocol:

float (f): A 4-byte IEEE 754 single precision float

int (i): A 4-bytes signed int

unsigned char (uc): A 1-byte unsigned char (0–255)

string (s): A UTF-8 encoded string. No terminator is specified. The string is a composite type,

transmitted as a single int (i) specifying the number of characters in the string (N), followed by

N unsigned chars (uc) containing the letters of the string.

NOTE: The bytes of the float and int types are transmitted in little endian order.

Command Format

Commands are transmitted as a single string (using characters a–z (0x61 – 0x7A) only), followed by any

additional payload required by the command in the definition.

Response Format

The response to any command is composed of a status byte (unsigned char), followed by any

additional payload required by the response.

Communication Delays

Once the first byte of the command string is sent, the rest of the command string and the payload data

must follow without delay. At the end of COMMAND, the server must respond immediately. If there is a

delay of more than 5 seconds during this process, the party waiting for data may drop the connection

assuming that the peer has become unresponsive.

There is currently no limit on the delay between two consecutive commands.


Advanced Workflows | Chapter 201 TCP Protocol for DaVinci Resolve Transport Control

DELIVER

NOTE: Alternatively, a maximum allowable delay may be defined, in which case, the client

may issue periodic ‘connect’ commands to keep the connection alive.

Status Response Values

The meaning of the status values are as follows:

0x00: Command was executed successfully. Any additional payload is sent as expected.

0xFF: Command could not be executed successfully. No additional payload will follow.

TCP Protocol Stream

The following commands can be sent over the protocol stream.

connect

The client initiates the stream by sending a connect command string. There is no payload. The server

responds with a status value of 0x00.

goto

The client sends a goto command string followed by four unsigned chars representing the hour,

minute, second, and frame of the timecode.

The server responds with an appropriate status byte based on the execution of the command.

play

The client sends a play command string followed by a floating point value. Play in real-time is 1.0, stop

is 0.0, reverse is -1.0, 2x is 2.0, etc.

The server responds with an appropriate status byte based on the execution of the command.

gettc

The client sends a gettc command string.

The server responds with an appropriate status byte (status byte may be 0xFF if no timeline exists, for

instance). If the status byte is 0x00, it is followed by four unsigned chars representing the hour, minute,

second, and frame of the timecode.

getframerate

The client sends a getframerate command string.

The server responds with an appropriate status byte. If the status byte is 0x00, it is followed by a

floating point value for the frame rate.


Advanced Workflows | Chapter 201 TCP Protocol for DaVinci Resolve Transport Control

DELIVER