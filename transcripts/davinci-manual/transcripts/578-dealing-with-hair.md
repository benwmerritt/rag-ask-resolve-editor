---
title: "Dealing With Hair"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: 578
---

# Dealing With Hair

Wispy or frizzy hair, individual strands of hair being thrown back, and tips of dreadlocks or heavily

moussed hair that comes to points will often require special handling with this tool. Keep in mind

that the Magic Mask tool does not specialize in soft translucent mask edges like a keyer does.

When it comes to hair styles that are loose and free, in many situations you may be able to finesse

an acceptable result using the Matte Finesse controls to expand a softened version of the matte to

encompass the entire hairstyle.

If this interferes too much with the edges of other features of the subject you’re isolating, you can

create a dedicated hair mask in Features mode by drawing Hair strokes. You can then use the Matte

Finesse controls at the right of the palette to create softened edges that work well with the outer

boundary of the hair style you’re isolating.


Color | Chapter 139 Magic Mask

COLOR

Creating a soft-edged hair mask

At this point, you can try doing different color adjustments using two different correction nodes, one

for the subject’s hair, and another using Magic Mask to isolate everything but the hair.

Alternately, if you want a single matte with which to isolate the entire subject, you can then use

additional instances of the Magic Matte tool (one per node), using one node to isolate just the face and

body without the hair, and a third node to isolate the entire subject but with a very soft edge. Then,

you can use a Key Mixer node to combine all these masks together with the original hair mask you

created, with which to feed a complete key to another node used to make the correction.

(Left) Nodes 2, 3, and 4 are creating three different masks that are combined using a key mixer and connected

to the Key input of Node 5 to make an adjustment, (Right) The final result of this three-mask approach.

While hair with soft edges can be a challenge, Magic Mask excels at many elaborate hair styles

with detailed shapes and hair accessories, including jewelry and ribbons. For example, the stylized

hairstyles found in European and Chinese period movies and shows give the DaVinci Neural Engine

no trouble at all, particularly as these styles are usually tightly bound with no wispy hair.

Asymmetrical hairstyles may require extra strokes to identify hair that’s significantly longer on one

side of the face. This may also be true for unorthodox hair styles, such as hair that’s been sculpted into

distinct sculptural shapes. Lastly, tight braids that expose skin on the scalp are also challenging for

the kind of hard masks that Magic Mask produces, so you’re better off using Magic Mask as a garbage

matte and using a keyer to create a detailed soft mask to use in these instances.


Color | Chapter 139 Magic Mask

COLOR

About Hats

Magic Mask works with an incredibly wide variety of hats from all time periods. On hats, tassels or

details like feathers can be a problem (in testing, the feather on Errol Flynn’s cap in Robin Hood

couldn’t consistently be included, even though the cap itself was no problem). Additionally, veils

that are part of hats may or may not be easily identified, but an additional stroke usually solves

the problem.

Dealing With Accessories

Things that people are holding, such as handkerchiefs or umbrellas, are best selected in Object mode.

Jewelry and watches pose a special problem, as they’re typically so thin and small that they can be

difficult to omit, but you may not want to include them depending on the adjustment you’re trying

to make. Your results will vary with the thickness of the items and the framing of your subject, but in

general your results will probably be better if you simply add a stroke or two to include these items in

the isolation, since omitting fine detail like a necklace can be problematic.

Adding Strokes to Guide Mask Creation

Here are some tips for how to draw strokes to analyze the image. To identify people, try starting with a

single short positive stroke (blue), centered on the face or body.

Drawing the first stroke to identify an entire person

Depending on the result, more strokes may be needed to differentiate an arm or frizzy hair from the

background. If you’re adding a stroke to an arm or hair, don’t put it right at the edge; the goal is not to

trace the subject, but to use strokes within the body of the subject to clarify what features belong to

the subject, and which do not.


Color | Chapter 139 Magic Mask

COLOR

Adding a stroke to the arm to include it as well

As you do this, resist the urge to use too many strokes. One stroke might well be all you need, or you

might need two or three, but using more than five strokes for any subject or feature may cause more

problems than it solves.

Adding negative strokes to the reflection to remove

To identify faces, try starting with a single short stroke in the middle of the face, along the nose, or

from eyes to the lips. Depending on the result, you may need additional strokes to identify the chin, a

beard, or to distinguish the forehead from wispy hair.


Color | Chapter 139 Magic Mask

COLOR

Drawing strokes to identify a face; notice that additional strokes are needed to include the beard.

It’s a good idea to start with a single stroke, then track the stroke through the duration of the clip

(described later in this section). Over the entire clip, you’ll see which parts of the mask may exhibit

problems. This will guide where you put additional strokes, in order to more clearly identify the person

versus the background, in order to clean up the resulting mask. As you add additional strokes, track

those as well and see how things go.

If you notice parts of the background that are erroneously added to the mask, you can add a negative

stroke (red) to clarify that those parts of the image should not be isolated. Short strokes, longer

strokes, and zig zags are good for backgrounds. Since strokes just help the analysis update the mask,

you can try different types of strokes to see what works best, and delete any stroke that doesn’t give

good results. As with positive strokes, don’t use more strokes than are absolutely necessary to get the

result you want.

(Left) The microphone incorrectly identified as part of the woman being interviewed, (Right) Drawing negative

strokes to identify the microphone as background, using a zig-zag pattern to tag the entire microphone


Color | Chapter 139 Magic Mask

COLOR

Similarly, if you’re isolating features such as a face, and you find other features, such as hair, getting in

the way, you can draw a negative stroke on the hair to identify it as not part of the face.

If there’s a “hole” in the resulting mask that’s actually part of the background and not the subject, you

can try drawing a stroke connecting that hole to the rest of the background.

Drawing strokes to connect the background with itself,

to remove part of the mask that’s not part of the person

If there’s an “island” in the mask that’s actually part of the subject and not the background, you can try

drawing a stroke across the island that connects one solid part of the mask to itself.

Drawing strokes to fill an island

in the subject being isolated

Of course, extracting a mask using strokes is only the first part of creating a useful mask. The Quality,

Consistency, and Smart Refine controls let you refine the stroke analysis of the image to create the

best tradeoff between performance and quality for the type of mask you need. These controls work

hand in hand with the strokes you draw to extract a mask. A set of Mask Finesse controls then let you

adjust the resulting mask to manipulate and soften it, to better suit whatever adjustment you’re trying

to make. All of these controls are described earlier in this section.


Color | Chapter 139 Magic Mask

COLOR