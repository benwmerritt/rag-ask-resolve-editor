---
title: "Tips for Properly Shooting a Color Chart"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 544
---

# Tips for Properly Shooting a Color Chart

The results you get using Color Match are completely dependent on how the charts were shot in the

field. If the charts were properly shot, you’ll get great results. If the charts were improperly shot, the

results will be unpredictable.

To get the best results using Color Match, adhere to the following guidelines:

�The chart must be lit evenly such that the lighting on each patch is the same intensity (level) and

color. Any shadows or changes in lighting color across the chart will result in Color Match trying to

compensate for these changes, and an inaccurate match will result. When viewing a chart being lit

prior to a shoot shooting via a waveform monitor, the top of each individual patch as seen on the

scope should appear as a rectangle with a “flat top.”

Poorly lit chart with irregularly topped waveforms

Well lit chart with flat-topped waveforms

�No patches on the chart should be clipped in any of the RGB color channels. A clipped channel

will force Color Match to use incorrect RGB values, and the resulting match will be inaccurate.


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

�The white patch on the recorded chart should be captured between 70–95 IRE/percent. Correct

exposure is essential to getting a good result, and while Color Match does allow for some

adjustment via the White Level option, this will only give accurate results if the original chart is

shot so that the white patch sits within the 70–95 IRE/percent range when viewed on a waveform

monitor. It is not recommended that a white patch be shot with a signal level above 95 IRE/

percent, since this usually means that one of the RGB channels is close to or actually clipping

which will cause an inaccurate match.

�The Source Gamma setting must be set to match the encoded OETF (opto-electrical transfer

function, or gamma) of the recorded image. To be able to create an accurate adjustment, the Color

Match function requires image data that is scene linear (linear to light). Most captured or recorded

image data is encoded with a tone curve (gamma curve) to maximize the efficiency of the bit

depth being used, and different cameras use different gamma curves to maximize the image data

from different sensors. Since the Color Match algorithm converts image data into a scene linear

space before creating an adjustment, it needs to undo the gamma curve created by the camera

or debayering process. If the wrong Source Gamma setting is selected in the Match Color palette,

then the data will not be linearized correctly and the resulting match will be inaccurate.

�Lighting in the scene with an unusual spectral response or a strong color cast can cause an

inaccurate match. Scenes lit with lights that have an unusual spectral response (such as cheap

fluorescent bulbs, cheap LED lighting, or mercury vapor fixtures that exhibit a very narrow or

spiky spectral power distribution) can cause metameric errors in both the camera’s response

and the Color Match function, resulting in the creation of an inaccurate adjustment. The most

accurate results are obtained when the scene uses lighting with a chromaticity that is close to

the black body locus (with a highly correlated color temperature) and a relatively smooth spectral

power distribution. In other words, use high-quality lighting that doesn’t have spikes in specific

parts of the spectrum.

�Large differences between the color temperature of the lighting shining directly on the chart and

ambient lighting elsewhere in the scene can cause perceptual errors. Often the problem is one of

perception and not an incorrect color adjustment. For example, outdoor scenes being artificially

lit with instruments shining extremely warm light (low color temperatures of 3200K or less) but

that have cooler ambient lighting may appear overly blue if matched with a Target Color Temp of

6500K. This happens because the chart under direct lighting is lit at the lower (yellower) color

temperature, but areas of the scene in shadow are much cooler because of the ambient “blue”

light from the sky; the result is an automatic color adjustment that’s correct for the chart, but

exaggerated in the background.

How to Use Color Match

The following procedure shows how to use the Color Match palette and overlay to

create a color correction.

The Color Match palette


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

To sample a color chart to make an automatic correction:


Select the clip with a chart you want to sample. If necessary, you can use the View > Show Current

Clip With Handles option to show additional frames at the beginning of the current clip to reveal a

color chart in the leader of your media.


If necessary, choose an option from the Source Gamma drop-down menu that corresponds to the

gamma with which the media was recorded.


Then, choose a target gamma and color space that corresponds to the format you want this clip to

be matched to.


Click the Viewer tool drop-down, choose the Color Chart overlay, and use its corner-pinning

controls to line the sampling boxes up with the color patches of the chart.

Aligning the Color Match target with the chart in the video


When you’re finished, click the Match button, and the clip will be automatically corrected.

A clip before and after automatic color matching


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

TIP: Keep in mind that not every shot needs to have a chart. If the lighting of the location

used in a scene is consistent, you really only need a single chart analysis to generate a

correction that you can copy to all other clips in the same scene. Of course, if you are using

multiple cameras in a scene, you should have a chart analysis for each separate camera if

you want to try and match them more closely together. If you’re shooting a scene that takes

all day, you may also want to shoot charts at significant time changes corresponding to the

lighting changes that are happening.

Configuration Controls

Here’s a more detailed explanation of each of the parameters found in the Color Match palette.

�Source Gamma: Defines the source gamma the media was recorded with. You must select the

correct gamma or the results will not be as accurate.

�Target Gamma: Lets you select a target gamma that you want the corrected clip to use. While this

will most likely be the gamma you’re outputting the finished program at, you can choose other

target gamma values for specialized workflows.

�Target Color Space: The color space you’ll be outputting the finished program with.

�Color Temp: An adjustable color temperature control that lets you manually adjust the target

color balance of the resulting correction to be warmer (lower values) or cooler (higher values).

The default is 6500K.

�White Level: A checkbox that’s disabled by default, which lets you manually choose the target

white point that the automatic correction should use. Raising or lowering this value will stretch or

compress the contrast of the final correction.

�Match button: Once you’ve chosen the appropriate settings, and aligned the color match target

with the chart that was recorded, click to execute the match.

�Chart type drop-down menu: You can choose from among the supported chart types in

this drop-down. At the time of this writing, these include the Datacolor SpyderCheckr24,

theChromaDuMonde 24+4, the DSC Labs SMPTE OneShot, the X-Rite ColorChecker Classic,

the X-Rite ColorChecker Classic - Legacy, the X-Rite ColorChecker Video, and the X-Rite

ColorChecker Passport Video.

�Reset All button: Resets all controls and adjustments in this palette.

Reset Controls

The Color Match option menu has a variety of commands you can use to reset your work in the

Color Match palette.

�Reset Match Configuration: Resets the Configuration parameters described above.

�Reset Applied Match: Resets the matching operation without resetting the Configuration controls.


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

Automatic Adjustments

in the Primaries Palette

There are four controls found in the Primaries palette that can be used for automatically making

different color adjustments, in order to give you a head start whenever you’re trying to neutralize a

color cast in the image or choose better black and white points for exposure.

White Balance Eyedropper

The White Balance eyedropper, found at the bottom-left corner of the Primaries palette next to the

Automatic Correction button, provides an automated way of neutralizing a color cast in your image that

you can guide by manually selecting a feature in the image that is supposed to be white.

To auto white balance an image with an undesirable color cast or tint:


Click the White Balance eyedropper button. The pointer turns into the White Balance eyedropper.

The White Balance eyedropper


In the Viewer, click on any feature that is supposed to be white such as a white wall, white trim

around a window, white blinds, a white shirt, and so on. As you drag the eyedropper around, the

RGB values appear as a tooltip to give you a better idea of what the color is of the feature you’re

about to click on. Make sure the feature you click on is (a) supposed to be white, and not off-white,

and (b) that it corresponds to an image detail that’s not clipped, because that can make parts of

the image seem white that aren’t really.

As a result, the white balance of the image should appear much more neutral than before. Note

that this adjustment is not applied via any of the controls in the Primaries palette; it’s an invisible,

self-contained adjustment.

Pick Black Point and Pick White Point

The Pick Black Point and Pick White Point eyedropper controls, found at the upper left-hand corner

of the Lift and Gain controls of the Wheels and Bars modes of the Primaries palette, let you adjust

contrast by lowering the black point or raising the white point of the image, and also correct for

unwanted color casts in the shadows or highlights of the image.

NOTE: It’s easy, using the Pick Black and White Point controls, to inadvertently boost the

highlights or lower the shadows so much that you end up clipping part of the image. To give

these controls the best chance of succeeding, it’s advisable to find the absolute brightest or

darkest parts of the image to sample, according to the following instructions.


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

To automatically adjust the black point of an image:


Click the Pick Black Point control. The pointer turns into the Black Point tool.

The Auto Pick Black Point control


In the Viewer, click on any feature that is supposed to be black such as the deepest part of a

shadow in the background or within a fold of clothing, black fabric, or something painted black.

As you drag the Black Point tool around, the RGB values appear as a tooltip to give you a better

idea of what the color is of the feature you’re about to click on. Make sure the feature you click on

is (a) supposed to be black, and not some very dark hue, and (b) that it corresponds to an image

detail that’s not clipped, because that can make parts of the image seem black that aren’t really.

As a result, the darkest parts of the image should appear much darker than before, and any color

imbalance in the shadows should be neutralized. Unlike the White Balance eyedropper, this

adjustment is applied via the Lift controls in the Wheels and Bars mode, which should appear with

some manner of adjustment as a result.

To automatically adjust the white point of an image:


Click the White Point control. The pointer turns into the White Point tool.

The Auto Pick White Point control


In the Viewer, click on any feature that is supposed to be white such as a white wall, white trim

around a window, white blinds, a white shirt, and so on. As you drag the White Point tool around,

the RGB values appear as a tooltip to give you a better idea of what the color is of the feature

you’re about to click on. Make sure the feature you click on is (a) supposed to be white, and not

off-white, and (b) that it corresponds to an image detail that’s not clipped, because that can make

parts of the image seem white that aren’t really.

As a result, the lightest parts of the image should appear much lighter than before, and any color

imbalance in the highlights should be neutralized. Unlike the White Balance eyedropper, this

adjustment is applied via the Gain controls in the Wheels and Bars mode, which should appear

with some manner of adjustment as a result.