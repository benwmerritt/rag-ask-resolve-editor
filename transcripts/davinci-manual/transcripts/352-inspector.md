---
title: "Inspector"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 352
---

# Inspector

Projector 3D controls

Controls Tab

Enabled

When this checkbox is enabled, the projector affects the scene. Disable the checkbox to turn off the

projector. This is not the same as the red switch in the upper-left corner of the Inspector. The red

switch disables the tool altogether and passes the image on without any modification. The Enabled

checkbox is limited to the effect part of the tool. Other parts, like scripts in the Settings tab still process

as normal.

Color

The input image is multiplied by this color before being projected into the scene.

Intensity

Use this slider to set the Intensity of the projection when the Light and Ambient Light projection modes

are used. In Texture mode, this option scales the Color values of the texture after multiplication by

the color.

Decay Type

A projector defaults to No Falloff, meaning that its light has equal intensity on geometry, despite the

distance from the projector to the geometry. To cause the intensity to fall off with distance, set the

Decay type to either Linear or Quadratic modes.

Angle

The Cone Angle of the node refers to the width of the cone where the projector emits its full intensity.

The larger the angle, the wider the cone angle, up to a limit of 90 degrees.

Fit Method

The Fit Method determines how the projection is fitted within the projection cone.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

The first thing to know is that although this documentation may call it a “cone,” the Projector 3D

and Camera 3D nodes do not project an actual cone; it’s more of a pyramid of light with its apex

at the camera/projector. The Projector 3D node always projects a square pyramid of light—i.e., its

X and Y angles of view are the same. The pyramid of light projected by the Camera 3D node can

be non‑square depending on what the Film Back is set to in the camera. The aspect of the image

connected into the Projector 3D/Camera 3D does not affect the X/Y angles of the pyramid, but rather

the image is scaled to fit into the pyramid based upon the fit options.

When both the aspect of the pyramid (AovY/AovX) and the aspect of the image (height * pixelAspectY)/

(width * pixelAspectX) are the same, there is no need for the fit options, and in this case the fit options

all do the same thing. However, when the aspect of the image and the pyramid (as determined by the

Film Back settings in Camera 3D) are different, the fit options become important.

For example, Fit by Width fits the width of the image across the width of the Camera 3D pyramid. In

this case, if the image has a greater aspect ratio than the aspect of the pyramid, some of the projection

extends vertically outside of the pyramid.

There are five options:

�Inside: The image is uniformly scaled so that its largest dimension fits inside the cone. Another

way to think about this is that it scales the image as big as possible subject to the restriction that

the image is fully contained within the pyramid of the light. This means, for example, that nothing

outside the pyramid of light ever receives any projected light.

�Width: The image is uniformly scaled so that its width fits inside the cone. Note that the image

could still extend outside the cone in its height direction.

�Height: The image is uniformly scaled so that its height fits inside the cone. Note that the image

could still extend outside the cone in its width direction.

�Outside: The image is uniformly scaled so that its smallest dimension fits inside the cone. Another

way to think about this is that it scales the image as small as possible subject to the restriction

that the image covers the entire pyramid (i.e., the pyramid is fully contained within the image). This

means that any pixel of any object inside the pyramid of light always gets illuminated.

�Stretch: The image is non-uniformly scaled, so it exactly covers the cone of the projector.

Projection Mode

�Light: Projects the texture as a diffuse/specular light.

�Ambient Light: Uses an ambient light for the projection.

�Texture: When used in conjunction with the Catcher node, this mode allows re-lightable texture

projections. The projection strikes only objects that use the catcher material as part of their

material shaders.

One useful trick is to connect a Catcher node to the Specular Texture input on a 3D Material node

(such as a Blinn). This causes any object using the Blinn material to receive the projection as part

of the specular highlight. This technique can be used in any material input that uses texture maps,

such as the Specular and Reflection maps.

Shadows

Since the projector is based on a spotlight, it is also capable of casting shadows using shadow maps.

The controls under this reveal are used to define the size and behavior of the shadow map.

�Enable Shadows: The Enable Shadows checkbox should be selected if the light is to produce

shadows. This defaults to selected.

�Shadow Color: Use this standard Color control to set the color of the shadow.

This defaults to black (0, 0, 0).

�Density: The Shadow Density determines the transparency of the shadow. A density of 1.0

produces a completely transparent shadow, whereas lower values make the shadow transparent.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

�Shadow Map Size: The Shadow Map Size control determines the size of the bitmap used to create

the shadow map. Larger values produce more detailed shadow maps at the expense of memory

and performance.

�Shadow Map Proxy: The Shadow Map Proxy determines the size of the shadow map used for

proxy and auto proxy calculations. A value of 0.5 would use a 50% shadow map.

�Multiplicative/Additive Bias: Shadows are essentially textures applied to objects in the scene,

so there is occasionally Z-fighting, where the portions of the object that should be receiving the

shadows render over the top of the shadow instead.

�Multiplicative and Additive Bias: Bias works by adding a small depth offset to move the shadow

away from the surface it is shadowing, eliminating the Z-fighting. Too little bias and the objects can

self-shadow themselves. Too much bias and the shadow can become separated from the surface.

Adjust the multiplicative bias first, then fine tune the result using the additive bias control.

�Force All Materials Non-Transmissive: Normally, an RGBAZ shadow map is used when rendering

shadows. By enabling this option, you are forcing the renderer to use a Z-only shadow map.

This can lead to significantly faster shadow rendering while using a fifth as much memory. The

disadvantage is that you can no longer cast “stained-glass”-like shadows.

�Shadow Map Sampling: Sets the quality for sampling of the shadow map.

�Softness: Soft edges in shadows are produced by filtering the shadow map when it is

sampled. Fusion provides three separate filtering methods that produce different effects when

rendering shadows.

None: Shadows have a hard edge. No filtering of the shadow map is done at all. The advantage

of this method is that you only have to sample one pixel in the shadow map, so it is fast.

Constant: Shadow edges have a constant softness. A filter with a constant width is used when

sampling the shadow map. Adjusting the Constant Softness slider controls the size of the

filter. Note that the larger you make the filter, the longer it takes to render the shadows. If the

Softness is set to constant, then a Constant slider appears. It can be used to set the overall

softness of the shadow.

Variable: The softness of shadow edges grows the farther away the shadow receiver is from

the shadow caster. The variable softness is achieved by changing the size of the filter based

on the distance between the receiver and caster. When this option is selected, the Softness

Falloff, Min Softness and Max Softness sliders appear.

Softness Falloff: The Softness Falloff slider appears when the Softness is set to variable.

This slider controls how fast the softness of shadow edges grows with distance. More precisely,

it controls how fast the shadow map filter size grows based on the distance between shadow

caster and receiver. Its effect is mediated by the values of the Min and Max Softness sliders.

Min Softness: The Min Softness slider appears when the Softness is set to variable. This slider

controls the Minimum Softness of the shadow. The closer the shadow is to the object casting

the shadow, the sharper it is up to the limit set by this slider.

Max Softness: The Max Softness slider appears when the Softness is set to variable. This slider

controls the Maximum Softness of the shadow. The farther the shadow is from the object

casting the shadow, the softer it is up to the limit set by this slider.

Common Controls

Transform and Settings Tabs

The remaining Transform and Settings tabs are common to many 3D nodes. Their descriptions can be

found in “The Common Controls” section at the end of this chapter.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Renderer 3D [3Rn]

The Renderer 3D node

Renderer 3D Node Introduction

The Renderer 3D node converts the 3D environment into a 2D image using either a default

perspective camera or one of the cameras found in the scene. Every 3D scene in a composition

terminates with at least one Renderer 3D node. The Renderer node includes a software and OpenGL

render engine to produce the resulting image. Additional render engines may also be available via

third-party plugins.

The software render engine uses the system’s CPU only to produce the rendered images. It is usually

much slower than the OpenGL render engine, but produces consistent results on all machines, making

it essential for renders that involve network rendering. The Software mode is required to produce soft

shadows, and generally supports all available illumination, texture, and material features.

The OpenGL render engine employs the GPU processor on the graphics card to accelerate the

rendering of the 2D images. The output may vary slightly from system to system, depending on the

exact graphics card installed. The graphics card driver can also affect the results from the OpenGL

renderer. The OpenGL render engines speed makes it possible to provide customized supersampling

and realistic 3D depth of field options. The OpenGL renderer cannot generate soft shadows. For soft

shadows, the software renderer is recommended.

Like most nodes, the Renderer’s motion blur settings can be found under the Common Controls tab.

Be aware that scenes containing particle systems require that the Motion Blur settings on the pRender

nodes exactly match the settings on the Renderer 3D node.

Otherwise, the subframe renders conflict producing unexpected (and incorrect) results.

NOTE: The Open GL renderer respects the Color Depth option in the Image tab of the

Renderer 3D node. This can cause slowdowns on certain graphics cards when rendering to

int16 or float32.

Inputs

The Renderer 3D node has two inputs on the node. The main scene input takes in the Merge 3D or

other 3D nodes that need to be converted to 2D. The effect mask limits the Renderer 3D output.

SceneInput: The orange scene input is a required input that accepts a 3D scene that you want to

convert to 2D.

EffectMask: The blue effects mask input uses a 2D image to mask the output of the node.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Basic Node Setup

All 3D scenes must end with a Renderer 3D node. The Renderer 3D node is used to convert a

3D scene into a 2D image. Below, the Renderer 3D node takes the output of a Merge 3D node, and

renders the 3D scene into a 2D image.

Renderer 3D connected directly after a Merge 3D, rendering the 3D scene to a 2D image

Inspector

Render 3D controls

Controls Tab

Camera

The Camera menu is used to select which camera from the scene is used when rendering. The Default

setting uses the first camera found in the scene. If no camera is located, the default perspective view

is used instead.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Eye

The Eye menu is used to configure rendering of stereoscopic projects. The Mono option ignores

the stereoscopic settings in the camera. The Left and Right options translate the camera using the

stereo Separation and Convergence options defined in the camera to produce either left- or right-eye

outputs. The Stacked option places the two images one on top of the other instead of side by side.

Layers allows the left and right eyes to be output as individual layers.

Reporting

The first two checkboxes in this section can be used to determine whether the node prints warnings

and errors produced while rendering to the console. The second set of checkboxes tells the node

whether it should abort rendering when a warning or error is encountered. The default for this node

enables all four checkboxes.

Renderer Type

This menu lists the available render engines. Fusion provides three: the software renderer, OpenGL

renderer, and the OpenGL UV render engine. Additional renderers can be added via third-party plugins.

All the controls found below this drop-down menu are added by the render engine. They may change

depending on the options available to each renderer. So, each renderer is described in its own

section below.

Software Controls

Output Channels

Besides the usual Red, Green, Blue, and Alpha channels, the software renderer can also embed the

following channels into the image. Enabling additional channels consumes additional memory and

processing time, so these should be used only when required.

�RGBA: This option tells the renderer to produce the Red, Green, Blue, and Alpha color channels of

the image. These channels are required, and they cannot be disabled.

�Z: This option enables rendering of the Z-channel. The pixels in the Z-channel contain a value that

represents the distance of each pixel from the camera. Note that the Z-channel values cannot include

anti-aliasing. In pixels where multiple depths overlap, the frontmost depth value is used for this pixel.

�Coverage: This option enables rendering of the Coverage channel. The Coverage channel

contains information about which pixels in the Z-buffer provide coverage (are overlapping with

other objects). This helps nodes that use the Z-buffer to provide a small degree of anti-aliasing.

The value of the pixels in this channel indicates, as a percentage, how much of the pixel is

composed of the foreground object.

�BgColor: This option enables rendering of the BgColor channel. This channel contains the color

values from objects behind the pixels described in the Coverage channel.

�Normal: This option enables rendering of the X, Y, and Z Normals channels. These three channels

contain pixel values that indicate the orientation (direction) of each pixel in the 3D space. A color

channel containing values in a range from [–1,1] represents each axis.

�TexCoord: This option enables rendering of the U and V mapping coordinate channels. The pixels

in these channels contain the texture coordinates of the pixel. Although texture coordinates are

processed internally within the 3D system as three-component UVW, Fusion images store only UV

components. These components are mapped into the Red and Green color channel.

�ObjectID: This option enables rendering of the ObjectID channel. Each object in the 3D

environment can be assigned a numeric identifier when it is created. The pixels in this floating-

point image channel contain the values assigned to the objects that produced the pixel. Empty

pixels have an ID of 0, and the channel supports values as high as 65534. Multiple objects can

share a single Object ID. This buffer is useful for extracting mattes based on the shapes of objects

in the scene.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

�MaterialID: This option enables rendering of the Material ID channel. Each material in the 3D

environment can be assigned a numeric identifier when it is created. The pixels in this floating-

point image channel contain the values assigned to the materials that produced the pixel. Empty

pixels have an ID of 0, and the channel supports values as high as 65534. Multiple materials

can share a single Material ID. This buffer is useful for extracting mattes based on a texture; for

example, a mask containing all the pixels that comprise a brick texture.

Lighting

�Enable Lighting: When the Enable Lighting checkbox is selected, objects are lit by any lights in

the scene. If no lights are present, all objects are black.

�Enable Shadows: When the Enable Shadows checkbox is selected, the renderer produces

shadows, at the cost of some speed.

OpenGL Controls

Render 3D Open GL controls

Output Channels

In addition to the usual Red, Green, Blue, and Alpha channels, the OpenGL render engine can also

embed the following channels into the image. Enabling additional channels consumes additional

memory and processing time, so these should be used only when required.

�RGBA: This option tells the renderer to produce the Red, Green, Blue, and Alpha color channels of

the image. These channels are required, and they cannot be disabled.

�Z: This option enables rendering of the Z-channel. The pixels in the Z-channel contain a value that

represents the distance of each pixel from the camera. Note that the Z-channel values cannot

include anti-aliasing. In pixels where multiple depths overlap, the frontmost depth value is used for

this pixel.

�Normal: This option enables rendering of the X, Y, and Z Normals channels. These three channels

contain pixel values that indicate the orientation (direction) of each pixel in the 3D space. A color

channel containing values in a range from [–1,1] is represented by each axis.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

�TexCoord: This option enables rendering of the U and V mapping coordinate channels. The pixels

in these channels contain the texture coordinates of the pixel. Although texture coordinates are

processed internally within the 3D system as three-component UVW, Fusion images store only UV

components. These components are mapped into the Red and Green color channels.

�ObjectID: This option enables rendering of the ObjectID channel. Each object in the 3D

environment can be assigned a numeric identifier when it is created. The pixels in this floating-

point image channel contain the values assigned to the objects that produced the pixel. Empty

pixels have an ID of 0, and the channel supports values as high as 65534. Multiple objects can

share a single Object ID. This buffer is useful for extracting mattes based on the shapes of objects

in the scene.

�MaterialID: This option enables rendering of the Material ID channel. Each material in the

3D environment can be assigned a numeric identifier when it is created. The pixels in this

floating‑point image channel contain the values assigned to the materials that produced the pixel.

Empty pixels have an ID of 0, and the channel supports values as high as 65534. Multiple materials

can share a single Material ID. This buffer is useful for extracting mattes based on a texture—for

example, a mask containing all the pixels that comprise a brick texture.

Anti-Aliasing

Anti-aliasing can be enabled for each channel through the Channel menu. It produces an output image

with higher quality anti-aliasing by brute force, rendering a much larger image, and then rescaling

it down to the target resolution. Rendering a larger image in the first place, and then using a Resize

node to bring the image to the desired resolution can achieve the exact same results. Using the

supersampling built in to the renderer offers two distinct advantages over this method.

The rendering is not restricted by memory or image size limitations. For example, consider the steps

to create a float-16 1920 x 1080 image with 16x supersampling. Using the traditional Resize node

would require first rendering the image with a resolution of 30720 x 17280, and then using a Resize to

scale this image back down to 1920 x 1080. Simply producing the image would require nearly 4 GB of

memory. When anti-aliasing is performed on the GPU, the OpenGL renderer can use tile rendering to

significantly reduce memory usage.

The GL renderer can perform the rescaling of the image directly on the GPU more quickly than

the CPU can manage it. Generally, the more GPU memory the graphics card has, the faster the

operation is performed.

Interactively, Fusion skips the anti-aliasing stage unless the HiQ button is selected in the Time Ruler.

Final quality renders always include supersampling, if it is enabled.

Because of hardware limitations, point geometry (particles) and lines (locators) are always rendered

at their original size, independent of supersampling. This means that these elements are scaled down

from their original sizes, and likely appear much thinner than expected.

Anti-Aliasing of Aux Channels in the OpenGL Renderer

The reason Fusion supplies separate anti-aliasing options for color and aux channels in the Anti-

Aliasing preset is that supersampling of color channels is quite a bit slower than aux channels. You

may find that 1 x 3 LowQ/HiQ Rate is sufficient for color, but for world position or Z, you may require 4 x

12 to get adequate results. The reasons color anti-aliasing is slower are that the shaders for RGBA can

be 10x to even 100x or 1000x more complex, and color is rendered with sorting enabled, while aux

channels get rendered using the much faster Z-buffer method.

TIP: For some things, sometimes using an SS Z-buffer improves quality, but for other things

like using the merge’s PerformDepthMerge option, it may make things worse.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Do not mistake anti-aliasing with improved quality. Anti-aliasing an aux channel does not mean it’s

better quality. In fact, anti-aliasing an aux channel in many cases can make the results much worse.

The only aux channels we recommend you enable anti-aliasing on are WorldCoord and Z.

TIP: We strongly recommend disabling Anti-Aliasing on Material ID and Object ID channels,

TexCoord, Normal, BackVector, and Vector channels. The issue arises when you have

multiple 3D surfaces with radically different TexCoord values in one pixel. The anti-aliasing

does not restrict itself to sampling the main surface but samples both surfaces. For example,

if one surface has TexCoords that are approximately (u,v) = (0, 0) within that pixel, and the

other surface has (0.5, 0.5), you get a blending of these two. The blended area of the texture

could have colors like (0, 0) or (0.5, 0.5), resulting in an oddly colored pixel artifact being

output from the 2D Texture node. The same problem can happen for normals.

Enable (LowQ/HiQ)

These two check boxes are used to enable anti aliasing of the rendered image.

Supersampling LowQ/HiQ Rate

The LowQ and HiQ rate tells the OpenGL render how large to scale the image. For example, if the rate

is set to 4 and the OpenGL renderer is set to output a 1920 x 1080 image, internally a 7680 x 4320

image is rendered and then scaled back to produce the target image. Set the multiplier higher to get

better edge anti-aliasing at the expense of render time. Typically 8 x 8 supersampling (64 samples per

pixel) is sufficient to reduce most aliasing artifacts.

The rate doesn’t exactly define the number of samples done per destination pixel; the width of the

reconstruction filter used may also have an impact.

Filter Type

When downsampling the supersized image, the surrounding pixels around a given pixel are often

used to give a more realistic result. There are various filters available for combining these pixels. More

complex filters can give better results but are usually slower to calculate. The best filter for the job

often depends on the amount of scaling and on the contents of the image itself.

The functions of these filters are shown in the image above. From left to right these are:

Box

This is a simple interpolation scale of the image.

Bi-Linear (triangle)

This uses a simplistic filter, which produces relatively clean and fast results.

Bi-Cubic (quadratic)

This filter produces a nominal result. It offers a good compromise between

speed and quality.

Bi-Spline (cubic)

This produces better results with continuous tone images but is slower

than Quadratic. If the images have fine detail in them, the results may be

blurrier than desired.

Catmul-Rom

This produces good results with continuous tone images which are scaled

down, producing sharp results with finely detailed images.

Gaussian

This is very similar in speed and quality to Quadratic.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Mitchell

This is similar to Catmull-Rom but produces better results with finely detailed

images. It is slower than Catmull-Rom.

Lanczos

This is very similar to Mitchell and Catmull-Rom but is a little cleaner

and also slower.

Sinc

This is an advanced filter that produces very sharp, detailed results, however,

it may produce visible `ringing' in some situations.

Bessel

This is similar to the Sinc filter but may be slightly faster.

Window Method

The Window Method menu appears only when the reconstruction filter is set to Sinc or Bessel.

�Hanning: This is a simple tapered window.

�Hamming: Hamming is a slightly tweaked version of Hanning.

�Blackman: A window with a more sharply tapered falloff.

Accumulation Effects

Accumulation effects are used for creating depth of field effects. Enable both the Enable Accumulation

Effects and Depth of Field checkboxes, and then adjust the quality and Amount sliders.

The blurrier you want the out-of-focus areas to be, the higher the quality setting you need.

A low amount setting causes more of the scene to be in focus.

The accumulation effects work in conjunction with the Focal plane setting located in the Camera 3D

node. Set the Focal Plane to the same distance from the camera as the subject you want to be in

focus. Animating the Focal Plane setting creates rack of focus effects.

Lighting

�Enable Lighting: When the Enable Lighting checkbox is selected, any lights in the scene light

objects. If no lights are present, all objects are black.

�Enable Shadows: When the Enable Shadows checkbox is selected, the renderer produces

shadows, at the cost of some speed.

Texturing

�Texture Depth: Lets you specify the bit depth of texture maps.

�Warn about unsupported texture depths: Enables a warning if texture maps are in an

unsupported bit depth that Fusion can’t process.

Lighting Mode

The Per-vertex lighting model calculates lighting at each vertex of the scene’s geometry.

This produces a fast approximation of the scene’s lighting but tends to produce blocky lighting on

poorly tessellated objects. The Per-pixel method uses a different approach that does not rely on the

detail in the scene’s geometry for lighting, so it generally produces superior results.

Although the per-pixel lighting with the OpenGL renderer produces results closer to that produced by

the more accurate software renderer, it still has some disadvantages. The OpenGL renderer is less

capable of dealing correctly with semi-transparency, soft shadows, and colored shadows, even with

per-pixel lighting. The color depth of the rendering is limited by the capabilities of the graphics card in

the system.


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Transparency

The OpenGL renderer reveals this control for selecting which ordering method to use when

calculating transparency.

�Z Buffer (fast): This mode is extremely fast and is adequate for scenes containing only opaque

objects. The speed of this mode comes at the cost of accurate sorting; only the objects closest

to the camera are certain to be in the correct sort order. So, semi-transparent objects may not be

shown correctly, depending on their ordering within the scene.

�Sorted (accurate): This mode sorts all objects in the scene (at the expense of speed)

before rendering, giving correct transparency.

�Quick Mode: This experimental mode is best suited to scenes that almost exclusively

contain particles.

Shading Model

Use this menu to select a shading model to use for materials in the scene. Smooth is the shading

model employed in the viewers, and Flat produces a simpler and faster shading model.

Wireframe

Renders the whole scene as wireframe. This shows the edges and polygons of the objects. The edges

are still shaded by the material of the objects.

Wireframe Anti-Aliasing

Enables anti-aliasing for the Wireframe render.

OpenGL UV Renderer

The OpenGL UV renderer is a special case render engine. It is used to take a model with existing

textures and render it out to produce an unwound flattened 2D version of the model. Optionally,

lighting can be baked in. This is typically done so you can then paint on the texture and reapply it.

Render 3D Open GL UV controls


Fusion Page Effects | Chapter 89 3D Nodes

FUSION

Below are some issues to be aware of when using the OpenGL UV renderer.

Baked-in lighting: After you have baked lighting into a model’s texture, you need to be careful

to turn lighting off on the object later when you render it with the baked-in lighting texture.

Single textures/multiple destinations: Beware of cases where a single area of the texture

map is used on multiple areas of the model. This is often done to save texture memory and

decrease modeling time. An example is the texture for a person where the artist mirrored

the left side mesh/uvs/texture to produce the right side. Trying to bake in lighting in this case

won’t work.

Unwrapped more the one mesh: Unwrapping more than one mesh at once can cause

problems. The reason is that most models are authored so they make maximum usage

of (u,v) in [0,1] x [0,1], so that in general models overlap each other in UV space.

Seams: When the UV gutter size is left at 0, this produces seams when the model is

retextured with the unwrapped texture.

UV Gutter Size: Increase this value to hide seams between faces.

Common Controls

Image and Settings Tabs

The remaining controls for the Image and Settings tabs are common to many 3D nodes.

Their descriptions can be found in “The Common Controls” section at the end of this chapter.