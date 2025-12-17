---
title: "Lighting and Shadows in 3D Viewers"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 260
---

# Lighting and Shadows in 3D Viewers

Before you add lights to a 3D scene, default lighting is provided. This basic, flat lighting allows you

to see the shading on objects without requiring you to add and set up lights as you work in the 3D

Viewer. Additionally, shadows are hidden by default. Once you start adding lights of your own, you

need to switch modes to see what they affect as you work.

To see the effects of the default light on the scene:

�Right-click within the 3D Viewer and choose 3D Options > Default Lights from the

contextual menu.

When you’re ready to add your own lighting to a scene, you can connect light nodes in various

ways to a Merge 3D node for the scene you’re working on. Once you connect a light to a Merge

3D node, you need to switch the 3D Viewer over to showing the new, proper lighting.

To toggle lighting rendering within a 3D scene:

�Right-click within the 3D Viewer and choose 3D Options > Lighting from the contextual menu.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

A 3D scene using default lights (top), and the same scene with lighting turned on (bottom)

TIP: Attempting to load a Light node into a viewer all by itself will result in an empty scene,

with nothing illuminated. To see the effects of lights, you must view the Merge 3D node the

light is connected to.

Similar to lights, the default 3D Viewer has shadows turned off. To see shadows cast from the lighting

you’ve created, you must turn them on.

To toggle shadows rendering within a 3D scene:

�Right-click within the 3D Viewer and choose 3D Options > Shadows from the contextual menu.

Enabling shadows will automatically turn on lighting, if it is not already turned on.

A 3D scene with shadows enabled along with the lights

Transparency in 3D Viewers

Image planes and 3D objects are obscured by other objects in a scene depending on the X, Y, and

Z position coordinates of each object in 3D space. The default method used to determine which

polygons are hidden and which are shown based on these coordinates is called Z-buffering.

Z-buffering is extremely fast but not always accurate when dealing with multiple transparent layers in

a scene. Fortunately, there is another option for more complex 3D scenes with transparency: Sorted.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

The Sorted method can be significantly slower in some scenes but will provide more accurate results

no matter how many layers of transparency happen to be in a scene.

The default behavior in the viewer is to use Z-buffering, but if your scene requires the Sorted method,

you can easily change this.

To choose a Sorted method of 3D compositing:

�Right-click anywhere within the 3D Viewer and choose one of the options in the Transparency

submenu of the contextual menu;

Full Sort: Renders every polygon in Z order to produce the most accurate rendering of

transparency.

Quick Sort: Reorders the polygons in the scene serially, from back to front, to produce a

reasonably accurate rendering of transparency.

Grid

The 3D Viewer displays a grid that’s used to provide a plane of reference in the 3D scene. By default,

the grid is 24 x 24 units in size, centered on the origin at (0,0,0), and subdivided into large squares of 2

units with small squares of 0.25 units each. These defaults can be altered in the 3D View panel of the

Fusion Settings window, available from the Fusion menu.

To toggle the grid on and off:

�Right-click anywhere within the 3D Viewer and choose 3D Options > Grid from the contextual menu.

The default grid of the 3D Viewer grid with its origin at x = 0, y = 0 and z = 0

Vertex Normals

Normals indicate what direction each vertex of 3D geometry is facing, and they are used when

calculating lighting and texturing on an object. When viewing any kind of 3D geometry, including an

image plane or a full FBX mesh, you can display the normals for each object in a scene.

To view the normals in a scene:

�Right-click anywhere within the viewer and choose 3D Options > Vertex Normals from

the contextual menu.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

The normals viewed in a 3D scene

Quad View

3D compositing often requires you to view the scene from different points of view to better control

transformations in three dimensions. While you can switch the 3D Viewer to different points of view,

doing so frequently can become cumbersome. Happily, you can instead enable a Quad view, which

divides the viewer into four panes. These panes can then display four different angles of the scene

at one time.

To toggle the display of the Quad view, do one of the following:

�Right-click anywhere within the viewer and choose Views > Quad View from the contextual menu.

�Press Shift-Q.

A Quad view of a 3D scene

While there are four panes in the Quad view, they all show the same scene. When assigning views

within a Quad view, you can choose between displaying Front, Left, Top, Bottom, and Perspective

orthographic views, or you can choose the view through any camera or spotlight that’s present in

the scene.


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

To assign different views to panes of a Quad view, do one of the following:

�Right-click directly on the POV label at the bottom left of the pane you want to reassign, and

choose another camera, light, or Point of View from the contextual menu.

Quad View Layouts

There are a variety of Quad view layouts, ranging from four equally sized panels to having three small

panels across the bottom of a larger single panel.

To switch to a different Quad view layout, do the following:


Enable the Quad view.


Right-click anywhere within the viewer and choose an option from the Views > Quad Layouts

submenu of the contextual menu.

Using Quad Views for 2D Scenes

Quad views aren’t only useful for 3D scenes. They can also be used with 2D scenes, with each pane

showing a different image channel or subview type. For example, one pane can show the image while

the other panes show the alpha channel, a vectorscope, and a histogram.

To assign different channels or subviews to panes of a Quad view for a 2D scene:


Right-click in a viewer and choose Views > Quad View.


Click once in the pane you want to reassign.


Do one of the following:

a)	 Choose a channel from the Channel Viewer menu.

b)	 Right-click in the viewer and choose Views, and then choose a Subview from the submenu.

Guides

Guides are onscreen overlays used to help you compose elements within a boundary or along the

center vertical and horizontal axes. While guides are displayed in the viewer, they’re not rendered

into the scene. There are four commonly used guides that can be displayed, including Monitor Safety,

Safe Title, Center, and Film.

The Guides submenu in the viewer’s contextual menu


Fusion Fundamentals | Chapter 69 Using Viewers

FUSION

Methods of using guides:

�To display guides in a viewer: Right-click in the viewer and then choose Guides > Show Guides

from the contextual menu, or press Command-G.

�To change the aspect ratio of the displayed guides: Right-click in the viewer and then choose

an option from the Guides > Frame Aspect submenu. The frame aspect is usually set to Default,

which forces the frame aspect to the same resolution as the image that’s displayed in the view.

However, when the frame aspect is set to a specific value, the guides will conform to the exact

boundaries of the specified format and any image area outside of that will be dark gray.

�To show or hide specific guides: Right-click in the viewer and then choose an option from the

Guides submenu. A variety of specific guides are provided, each of which can be individually

enabled and disabled.

Monitor Safety: Monitor Safety indicates the safe action area viewable on most monitors

and TV screens.

Safe Title: Safe Title indicates the safe area for titles viewable on all TV and monitor screens.

Center: Center shows a crosshair for the center point and x- and y-axis of the view.

Film: Some frame formats include film guides preset for you, whereas some will require

customization. The film guides can be customized in the Preferences > Frame Format window.