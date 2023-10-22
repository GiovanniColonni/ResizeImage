# Technical Exercise

Exercise: 
```
We want users to upload a badge: an avatar within a circle. Create a function taking a png as input and verifying that:

- Size = 512x512
- The only non transparent pixels are within a circle.
- That the colors is the badge give a "happy" feeling.

Additionally, you can create a parallel function that converts the given image (of any format) into the specified object.
```

### Try solution


To run a random sample just type

    > python3 ./src/main.py

To run a specific sample just type the name without extension for PNG
 files or with extension for other files

    > python3 ./src/main.py <sample_name> 


### Solution

I'm new to image manipulation but to start to create something I immediatly choose Python as a first try, for conveniance of simplicity. I found Pillow (PIL) and after some tentatives I found that it was a good choise for me. 

I approach the problem by splitting it steps:

1. Find the image format and convert it if need

2. Check if the size is correct and in case resize

3. Create a circle of transparent pixels 

4. Find the color palette and determine if it's happy of not 

The **point 1.** was easy to address thanks to PIL and the possibility to convert the image by simply save it back in a different format.

`
    img.save(path,"PNG")
`

For the **point 2.** I found that PIL provide 2 ways of resizing an image, by using `Image.thumbnail()` or by using `Image.resize()`.
Even if `Image.thumbnail()` use a scaled approach and so the image is not cutted during resize, it does not provide alwasys an output of the correct target size (512x512) but it will rather be an approximated one. Since this I use `Image.resize()` with the algorithm `Lanczos` as antialias algorithm to kepp a good quality while resizing.

For the **point3** my intuition was to check the pixel transparency. In fact when you have an image that use the color space RGBA you can check the alpha channel to understand if the pixel is saturated or not. In case the pixel is not saturated then you can just substitude `(255,0,0,0)` to make it transparent.

For the **point4**, colors. In this case I could not manage to have the pallette using `Image.getpalette()` and so I iterate over the image to find all the colors to determine if the palette was an happy one or not.
My simple approach to determine if a pelette of colors is happy was to define which colors are happy, I decided that: *red, blue, yellow, green, pink and orange* were happy colors.
At this point we need a way to check if a given color is in the list of happy colors.
To determine this you should notice that `(255, 0, 0, 1)` is **red** even `(255, 1, 0, 1)` is **red** and even `(255, 0, 1, 0.9)`. is still **red**. 
I try with two approach (based on intuitions but also asking to GPT), the first one was based on considering just a section of the [HSL](https://en.wikipedia.org/wiki/HSL_and_HSV#/media/File:Hsl-hsv_models.svg
) an area of "happy" color. But the result of the categorization was not good (check `./src/logic.py:is_happy_old(rgba)`), but by dropping the information of the alpha channel (saturation) the categorization start to be acceptable (check `./src/logic.py:is_happy(rgba)`) at least in the space of the samples that I'm considering and so I stick for the approach.

Another problem is that an image can have a lot of colors, and not all of them can be considered relevant during the analysis. Given this unless the image has only few colors ,for example the `github` sample you can run, does not make sense too much to maitain this approach but we would like to take only the dominant colors. To solve this problem I use a very basic clustering algorithm **KMeans** from `sklearn.cluster`, the idea is to identify the most prominent colors of the image by grouping them in clusters and pick the center of this cluster (My datascience skills were a bit rusty). After this just following the same approach as before with the dominant colors of the palette. 
Finally, an image is happy is it has more happy then sad colors.

At this point from the exercise I also 


### Final consideration



## Side Notes 