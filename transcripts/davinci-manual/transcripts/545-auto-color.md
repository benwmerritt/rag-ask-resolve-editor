---
title: "Auto Color"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 545
---

# Auto Color

The Auto Color command provides a quick way to automatically balance the blacks and whites

of a clip based on the current frame at the position of the playhead. As of DaVinci Resolve 16, the

A button in the Primaries palette and the Shot Match command available from the Thumbnail Timeline

contextual menu both now use advanced algorithms, based on the DaVinci Neural Engine, to provide

superior results when automatically adjusting color balance and contrast. These controls have been

developed to provide optimal results when working in the Rec. 709 color space, and at a gamma

of 2.4, so they work well in conjunction with using Resolve Color Management (RCM) to normalize

media first.


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

�The A button performs an automatic analysis of the current frame at the playhead to give a more

consistently useful neutral starting point for further adjustment.

�The Shot Match command matches one or more clips to the color and contrast of a graded or

ungraded target clip. This updated version of Shot Match has been designed to be used after

you’ve used the A button on each clip in the operation, the clips you’re matching and the clip

you’re matching to.

If you’re in need of a fast neutral starting point for a range of clips, you can also use these

commands together, grading a target clip using the A button, and then using Shot Match to match

a range of clips in the same scene to the automatically graded example. Please note that these

commands are intended to provide you with a reasonably neutral starting point for continued

grading; they’re not meant to create creative or artistic grades.

The Auto Color button

To make an automatic correction, do one of the following:

�Open the Primaries palette to any mode, and click the A button in the lower left-hand corner.

�Choose Color > Auto Color (Option-Shift-C).

�Press the AUTO COLOR button on the T-bar panel.

The advantage of Auto Color is that it gives you an immediate result for any clip without the

requirement for sampling the image or having a specific test pattern to analyze, but the disadvantage

is that this lack of guidance makes the usefulness of this command somewhat hit-or-miss. When it

works, it can work very well to give you a neutral starting point for further grading. When it fails, you’re

better off resetting the resulting adjustment and grading the old fashioned way.

Legacy Auto Color

The previous methods for doing Auto Color and Shot Match are available from the Color panel

of the User Preferences, via two checkboxes named “Use Legacy Auto Color/Shot Match.”

With these enabled, DaVinci Resolve looks for the darkest levels in the image to neutralize

the RGB color balance in the blacks, and the brightest levels to neutralize the RGB color

balance in the highlights. Furthermore, Master Lift and Master Gain are adjusted to maximize

image contrast at the outer boundaries of 0 and 100 percent. Using this control with the

Primaries Bars mode open makes it easier to see what’s been changed after these automatic

adjustments are made.


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

Shot Match

The previously available automated color correction commands, Auto Color and Color Match, are

both useful for adjusting a selected clip to give it a clean, neutral starting point when you’re either in a

hurry, or if you’re having trouble manually working out a solution. However, this is only the first step in

grading a scene.

After you make a general adjustment to improve the color of a clip in a scene, one of the other

principal tasks of the colorist is to adjust all of the clips in that scene so that they match the clip you

started with, such that they all look like they were shot at the same time and in the same place. This is

called scene-to-scene color correction, scene balancing, or shot matching. While there are abundant

tools in DaVinci Resolve to ease the process of doing this manually, wouldn’t it be nice if you could just

select a series of clips that you want to match, and have the software do the work?

That’s exactly what Shot Match has been designed to do. Whether you’re a colorist in a hurry, trying to

blast through a low-budget feature with an absurd schedule, a DIT making best light dailies who just

wants to make them match a little more closely before sending media off to editorial, or an editor who

isn’t fast at color correction who needs to give a rough cut a quick color balance before showing the

project to the client for the first time, the Shot Match feature of DaVinci Resolve has been created to

quickly make different clips in a timeline match one another more closely, with a minimum of steps.

As of DaVinci Resolve 16, the Shot Match command available from the Thumbnail Timeline contextual

menu uses an advanced algorithm, based on the DaVinci Neural Engine, to provide superior results

when automatically adjusting color balance and contrast. This control has been developed to provide

optimal results when working in the Rec. 709 color space, and at a gamma of 2.4, so they work well in

conjunction with using Resolve Color Management (RCM) to normalize media first.

The updated version of Shot Match has been designed to be used after you’ve used the A button on

each clip in the operation, on both the clips you’re matching and the clip you’re matching to.

(Top) Original scene, (Bottom) After using shot match to match all selected clips to clip 62

Legacy Auto Color

The previous methods for doing Auto Color and Shot Match are available from the Color panel

of the User Preferences, via two checkboxes named “Use Legacy Auto Color/Shot Match.” With

these enabled, DaVinci Resolve looks for the darkest levels in the image to neutralize the RGB

color balance in the blacks, and the brightest levels to neutralize the RGB color balance in the

highlights. Furthermore, Master Lift and Master Gain are adjusted to maximize image contrast

at the outer boundaries of 0 and 100 percent. Using this control with the Primaries Bars mode

open makes it easier to see what’s been changed after these automatic adjustments are made.


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

Shot Match Guidelines

Keep in mind that Shot Match isn’t supposed to make your clips look good, it’s supposed to make

them look the same as the clip you choose to match to, or to at least get as close as possible without

creating a color correction that will do harm to the image. The purpose of Shot Match is to make it

easier for you to match a scene’s worth of clips together so you have a starting point for building the

rest of the look you want for that scene, on top of this initial match.

The clip you choose to match to may have a correction applied to it, but for the best results, you

should limit yourself to simple Lift/Gamma/Gain primary adjustments. If you make Custom curve

or secondary adjustments to the image, it will be much more difficult for Shot Match to give you a

good result.

Shot Match works best with normalized clips. If you’ve got a timeline edited with log-encoded clips,

you may want to use DaVinci Color Management to normalize all the clips in the Timeline before you

use Shot Match, to get the most accurate results. It’s certainly possible to use Shot Match with log-

encoded media, but the flat color signal of log-encoded media may make it harder to get good results,

depending on the scene.

Furthermore, Shot Match is not the right tool to use to try and match un-normalized log-encoded

clips that use different types of log encoding, such as LogC and RedLogCine, or to try and match

normalized and un-normalized clips. Because log-encoding is similar to a set of red, green, and blue

curve operations, Shot Match is not equipped to achieve a successful result in this situation.

Shot Match is not designed to apply corrections to clips that already have node adjustments. The

results will be unpredictable, and probably won’t match. While the clip you’re matching to may have

simple primary adjustments applied to it, the other selected clips that are being matched should be

completely ungraded.

Lastly, Shot Match has been designed to do no harm to the image. This means if you use Shot Match

to try and match an underexposed interior shot to an exterior shot exposed at high noon on a sunlit

day, the Shot Match algorithm will do its best to “split the difference” in order to make the difference

between these two clips less jarring, while at the same time taking care not to stretch the color and

contrast adjustments being made to the underexposed clips to the point where the image falls apart.

How to Use Shot Match

There’s no way to easily describe what Shot Match does. It’s a complex algorithm designed to try and

deal with an impossibly varied number of different situations. As a result, Shot Match doesn’t apply

adjustments to any of the user-editable controls in the Color page. Instead, the image adjustment

created by Shot Match is applied invisibly, as the very last adjustment to the node that was selected

when Shot Match was used, similar to a LUT.

A Shot Match adjustment

applied to a clip

The procedure for using Shot Match is deceptively simple. However, getting a good result requires

some careful thought in terms of choosing which clips to match to one another.


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

To match one or more selected clips to a specific clip:


Following the guidelines presented in this section, Command-click or Shift-click one or more

clips that you want to be matched. The clip you want to match to may or may not be part of the

selection. You may select as few as one clip, or as many as you like.

Selecting clips you want to be matched

TIP: If you want to make it easier to notice the before and after, you can turn on

Split Screen, and choose Selected Clips from the mode drop-down in the Viewer

Options. This lets you see all the clips you’re about to match in a grid.


Next, right-click the clip you want to match all of the selected clips to, and choose Shot

Match to This Clip.

Shot Match command used on the clip you

want to match the other selected clips to

If the resulting automated match looks good and plays well, then congratulations, you’ve got an

excellent starting point for additional grading. However, keep in mind that even if the resulting

match isn’t perfect, it may have taken care of enough inconsistencies between the clip you’re

matching to and the clips that are being matched, that you need only make smaller, easier-to-spot

adjustments in order to nail the final match between the shots in a scene. Either way, you can

save time.

Suggestions for Using Shot Match

It’s certainly possible to select every clip in a scene and use Shot Match, and the results may be

wonderful depending on what kind of visuals are in the scene. However, for other scenes, this may not

always get you the best results.

Be strategic about which clips you select to match to one another. Don’t use Shot Match on shots that

you know already have the same lighting, as you’ll risk having Shot Match make a minor adjustment

that may actually make the shots match less well. Think of Shot Match as a tool for matching

clips that look different.

It can also help to use Shot Match an angle at a time, and to do a small test before committing yourself

to matching a bunch of clips. For example, suppose you have a scene consisting of angle A (an over

of character 1), angle B (an over of character 2), and angle C (a master shot), and you want to match the

scene entire scene to angle C since it has the best lighting. First, match one shot from angle B to your

favorite shot from angle C, and see how you like the result. If it’s good, then go ahead and select every

angle B clip and match them to angle C, before moving on to test one shot from angle A. This way, if


Color | Chapter 129 Automated Grading Commands and Imported Grades

COLOR

there’s ever an angle that doesn’t work well using Shot Match, you can try matching it to one of the

other angles in the scene that you’ve already matched to see if you get a better result.

NOTE: Keep in mind that, since each clip in the Timeline has its own undo stack, you cannot

undo a shot match operation applied to multiple clips all at once.

Beware of clips with large areas of color in the background that don’t match any of the other angles in

a scene, such as a shot-reverse-shot sequence that cuts between someone standing in a back yard

and someone standing against a purple wall. You can try it to see what happens, but this kind of color

distribution can often throw Shot Match results off.