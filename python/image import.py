from PIL import Image
import time
from PIL import Image, ImageFilter, ImageEnhance

# all of the block images that are used
B_block = Image.open('Block.jpg')
B_mine = Image.open('BlockMine.jpg')
B_colors = Image.open('BlockColors.jpg')
B_ice = Image.open('BlockIce.jpg')
B_insanecolor = Image.open('BlockInsaneColors.jpg')
B_lego = Image.open('BlockLego.jpg')
B_lights = Image.open('BlockLights.jpg')
B_normal = Image.open('BlockNormal.jpg')
B_small = Image.open('BlockSmall.jpg')
B_transparent = Image.open('BlockTransparent.jpg')

# the codes for the images
BLOCK_PICS = ('''[1] for Block 
[2] for BlockMine
[3] for BlockColors
[4] for BlockIce
[5] for BlockInsaneColors
[6] for BlockLego
[7] for BlockLights
[8] for BlockNormal
[9] for BlockSmall
[10] for BlockTransparent''')

#this lets you save as png
def blockchoicepng():
    print(BLOCK_PICS)
    choiceofblock = input("choose the block you want to convert to png: ")

    if choiceofblock == "1":
        B_block.save('png\Block.png')
        time.sleep(1)
        print ('Block.png has been saved to the png folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "2":
        B_mine.save('png\BlockMine.png')
        time.sleep(1)
        print ('BlockMine.png has been saved to the png folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "3":
        B_colors.save('png\BlockColors.png')
        time.sleep(1)
        print ('BlockColors.png has been saved to the png folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "4":
        B_ice.save('png\BlockIce.png')
        time.sleep(1)
        print ('BlockIce.png has been saved to the png folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "5":
        B_insanecolor.save('png\BlockInsaneColors.png')
        time.sleep(1)
        print ('BlockInsaneColors.png has been saved to the png folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "6":
        B_lego.save('png\BlockLego.png')
        time.sleep(1)
        print ('BlockLego.png has been saved to the png folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "7":
        B_lights.save('png\BlockLights.png')
        time.sleep(1)
        print ('BlockLights.png has been saved to the png folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "8":
        B_normal.save('png\BlockNormal.png')
        time.sleep(1)
        print ('BlockNormal.png has been saved to the png folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "9":
        B_small.save('png\BlockSmall.png')
        time.sleep(1)
        print ('BlockSmall.png has been saved to the png folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "10":
        B_transparent.save('png\BlockTransparent.png')
        time.sleep(1)
        print ('BlockTransparent.png has been saved to the png folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)

def pngsave():
    if input("do you want to save the images as a PNG? [Y] Or do you want to go back to the choices [N] ") == 'y':
        blockchoicepng()
    else:
        choice
#this lets you save as black and white
def blockchoiceBW():
    print(BLOCK_PICS)
    choiceofblock = input("choose the block you want to convert to black and white: ")

    if choiceofblock == "1":
        B_block.convert(mode='L').save('BlackWhite\BWBlock.jpg')
        time.sleep(1)
        print ('BWBlock.jpg has been saved to the BlackWhite folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "2":
        B_mine.convert(mode='L').save('BlackWhite\BlockMine.jpg')
        time.sleep(1)
        print ('BlockMine.jpg has been saved to the BlackWhite folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "3":
        B_colors.convert(mode='L').save('BlackWhite\BlockColors.jpg')
        time.sleep(1)
        print ('BlockColors.jpg has been saved to the BlackWhite folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "4":
        B_ice.save('BlackWhite\BlockIce.jpg')
        time.sleep(1)
        print ('BlockIce.jpg has been saved to the BlackWhite folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "5":
        B_insanecolor.convert(mode='L').save('BlackWhite\BlockInsaneColors.jpg')
        time.sleep(1)
        print ('BlockInsaneColors.jpg has been saved to the BlackWhite folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "6":
        B_lego.convert(mode='L').save('BlackWhite\BlockLego.jpg')
        time.sleep(1)
        print ('BlockLego.jpg has been saved to the BlackWhite folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "7":
        B_lights.convert(mode='L').save('BlackWhite\BlockLights.jpg')
        time.sleep(1)
        print ('BlockLights.jpg has been saved to the BlackWhite folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "8":
        B_normal.convert(mode='L').save('BlackWhite\BlockNormal.jpg')
        time.sleep(1)
        print ('BlockNormal.jpg has been saved to the BlackWhite folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "9":
        B_small.convert(mode='L').save('BlackWhite\BlockSmall.jpg')
        time.sleep(1)
        print ('BlockSmall.jpg has been saved to the BlackWhite folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "10":
        B_transparent.convert(mode='L').save('BlackWhite\BlockTransparent.jpg')
        time.sleep(1)
        print ('BlockTransparent.jpg has been saved to the BlackWhite folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)

def BWsave():
    if input("do you want to save the images as black and white? [Y] Or do you want to go back to the choices [N] ") == 'y':
        blockchoiceBW()
    else:
        choice
#this lets you save as a rotated image
def blockrotated():
    print(BLOCK_PICS)
    choiceofblock = input("choose the block you want to rotate: ")
    UserNumber = int(input("put number here for rotating: "))
    if choiceofblock == "1":
        rotatedB_block = B_block.rotate(UserNumber)
        rotatedB_block.save('Rotate\Block.jpg')
        time.sleep(1)
        print ('Block.jpg has been saved to the Rotate folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "2":
        rotated_mine = B_mine.rotate(UserNumber)
        rotated_mine.save('Rotate\BlockMine.jpg')
        B_mine.save('Rotate\BlockMine.jpg')
        time.sleep(1)
        print ('BlockMine.jpg has been saved to the Rotate folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "3":
        rotated_colors = B_colors.rotate(UserNumber)
        rotated_colors.save('Rotate\BlockColors.jpg')
        time.sleep(1)
        print ('BlockColors.jpg has been saved to the Rotate folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "4":
        rotated_ice = B_ice.rotate(UserNumber)
        rotated_ice.save('Rotate\BlockIce.jpg')
        time.sleep(1)
        print ('BlockIce.jpg has been saved to the Rotate folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "5":
        rotated_insanecolor = B_insanecolor.rotate(UserNumber)
        rotated_insanecolor.save('Rotate\BlockInsaneColors.jpg')
        time.sleep(1)
        print ('BlockInsaneColors.jpg has been saved to the Rotate folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "6":
        rotated_lego = B_lego.rotate(UserNumber)
        rotated_lego.save('Rotate\BlockLego.jpg')
        time.sleep(1)
        print ('BlockLego.jpg has been saved to the Rotate folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "7":
        rotated_lights = B_lights.rotate(UserNumber)
        rotated_lights.save('Rotate\BlockLights.jpg')
        time.sleep(1)
        print ('BlockLights.jpg has been saved to the Rotate folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "8":
        rotated_normal = B_normal.rotate(UserNumber)
        rotated_normal.save('Rotate\BlockNormal.jpg')
        time.sleep(1)
        print ('BlockNormal.jpg has been saved to the Rotate folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "9":
        rotated_small = B_small.rotate(UserNumber)
        rotated_small.save('Rotate\BlockSmall.jpg')
        time.sleep(1)
        print ('BlockSmall.jpg has been saved to the Rotate folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "10":
        rotated_transparent = B_transparent.rotate(UserNumber)
        rotated_transparent.save('Rotate\BlockTransparent.jpg')
        time.sleep(1)
        print ('BlockTransparent.jpg has been saved to the Rotate folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)

def rotatesave():
    if input("do you want to rotate a image? [Y] Or do you want to go back to the choices [N] ") == 'y':
        blockrotated()
    else:
        choice
#this lets you save as a blured image
def blockblur():
    print(BLOCK_PICS)
    choiceofblock = input("choose the block you want to blur: ")
    if choiceofblock == "1":
        blurB_block = B_block.filter(ImageFilter.BLUR)
        blurB_block.save('Blur\Block.jpg')
        time.sleep(1)
        print ('Block.jpg has been saved to the Blur folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "2":
        blurB_mine = B_mine.filter(ImageFilter.BLUR)
        blurB_mine.save('Blur\BlockMine.jpg')
        time.sleep(1)
        print ('BlockMine.jpg has been saved to the Blur folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "3":
        blurB_colors = B_colors.filter(ImageFilter.BLUR)
        blurB_colors.save('Blur\BlockColors.jpg')
        time.sleep(1)
        print ('BlockColors.jpg has been saved to the Blur folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "4":
        blurB_ice = B_ice.filter(ImageFilter.BLUR)
        blurB_ice.save('Blur\BlockIce.jpg')
        time.sleep(1)
        print ('BlockIce.jpg has been saved to the Blur folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "5":
        blurB_insanecolor = B_insanecolor.filter(ImageFilter.BLUR)
        blurB_insanecolor.save('Blur\BlockInsaneColors.jpg')
        time.sleep(1)
        print ('BlockInsaneColors.jpg has been saved to the Blur folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "6":
        blurB_lego = B_lego.filter(ImageFilter.BLUR)
        blurB_lego.save('Blur\BlockLego.jpg')
        time.sleep(1)
        print ('BlockLego.jpg has been saved to the Blur folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "7":
        blurB_lights = B_lights.filter(ImageFilter.BLUR)
        blurB_lights.save('Blur\BlockLights.jpg')
        time.sleep(1)
        print ('BlockLights.jpg has been saved to the Blur folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "8":
        blurB_normal = B_normal.filter(ImageFilter.BLUR)
        blurB_normal.save('Blur\BlockNormal.jpg')
        time.sleep(1)
        print ('BlockNormal.jpg has been saved to the Blur folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "9":
        blurB_small = B_small.filter(ImageFilter.BLUR)
        blurB_small.save('Blur\BlockSmall.jpg')
        time.sleep(1)
        print ('BlockSmall.jpg has been saved to the Blur folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "10":
        blurB_transparent = B_transparent.filter(ImageFilter.BLUR)
        blurB_transparent.save('Blur\BlockTransparent.jpg')
        time.sleep(1)
        print ('BlockTransparent.jpg has been saved to the Blur folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)

def blursave():
    if input("do you want to blur a image? [Y] Or do you want to go back to the choices [N] ") == 'y':
        blockblur()
    else:
        choice
#this lets you save as a different thumbnail size
def blockthumbnail():
    print(BLOCK_PICS)
    choiceofblock = input("choose the block you want to change the thumbnail size: ")
    UserNumber = int(input("put number here for thumbnail size: "))
    SIZE = (UserNumber, UserNumber)
    if choiceofblock == "1":
        ThumbnailB_block = B_block
        ThumbnailB_block.thumbnail(SIZE)
        ThumbnailB_block.save('Thumbnail\Block.jpg')
        time.sleep(1)
        print ('Block.jpg has been saved to the Thumbnail folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "2":
        ThumbnailB_mine = B_mine
        ThumbnailB_mine.thumbnail(SIZE)
        ThumbnailB_mine.save('Thumbnail\BlockMine.jpg')
        time.sleep(1)
        print ('BlockMine.jpg has been saved to the Thumbnail folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "3":
        ThumbnailB_colors = B_colors
        ThumbnailB_colors.thumbnail(SIZE)
        ThumbnailB_colors.save('Thumbnail\BlockColors.jpg')
        time.sleep(1)
        print ('BlockColors.jpg has been saved to the Thumbnail folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "4":
        ThumbnailB_ice = B_ice
        ThumbnailB_ice.thumbnail(SIZE)
        ThumbnailB_ice.save('Thumbnail\BlockIce.jpg')
        time.sleep(1)
        print ('BlockIce.jpg has been saved to the Thumbnail folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "5":
        ThumbnailB_insanecolor = B_insanecolor
        ThumbnailB_insanecolor.thumbnail(SIZE)
        ThumbnailB_insanecolor.save('Thumbnail\BlockInsaneColors.jpg')
        time.sleep(1)
        print ('BlockInsaneColors.jpg has been saved to the Thumbnail folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "6":
        ThumbnailB_lego = B_lego
        ThumbnailB_lego.thumbnail(SIZE)
        ThumbnailB_lego.save('Thumbnail\BlockLego.jpg')
        time.sleep(1)
        print ('BlockLego.jpg has been saved to the Thumbnail folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "7":
        ThumbnailB_lights = B_lights
        ThumbnailB_lights.thumbnail(SIZE)
        ThumbnailB_lights.save('Thumbnail\BlockLights.jpg')
        time.sleep(1)
        print ('BlockLights.jpg has been saved to the Thumbnail folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "8":
        ThumbnailB_normal = B_normal
        ThumbnailB_normal.thumbnail(SIZE)
        ThumbnailB_normal.save('Thumbnail\BlockNormal.jpg')
        time.sleep(1)
        print ('BlockNormal.jpg has been saved to the Thumbnail folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "9":
        ThumbnailB_small = B_small
        ThumbnailB_small.thumbnail(SIZE)
        ThumbnailB_small.save('Thumbnail\BlockSmall.jpg')
        time.sleep(1)
        print ('BlockSmall.jpg has been saved to the Thumbnail folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "10":
        ThumbnailB_transparent = B_transparent
        ThumbnailB_transparent.thumbnail(SIZE)
        ThumbnailB_transparent.save('Thumbnail\BlockTransparent.jpg')
        time.sleep(1)
        print ('BlockTransparent.jpg has been saved to the Thumbnail folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)

def thumbnailsave():
    if input("do you want to change the thumbnail size? [Y] Or do you want to go back to the choices [N] ") == 'y':
        blockthumbnail()
    else:
        choice
#this lets you save as a different color
def blockcolor():
    print(BLOCK_PICS)
    choiceofblock = input("choose the block you want to enhance the color of: ")
    if choiceofblock == "1":
        ColorB_block = B_block
        ColorB_block = ImageEnhance.Color(B_block)
        ColorB_block.enhance(8.0).save('Color\Block.jpg')
        time.sleep(1)
        print ('Block.jpg has been saved to the Color folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "2":
        ColorB_mine = B_mine
        ColorB_mine = ImageEnhance.Color(B_mine)
        ColorB_mine.enhance(8.0).save('Color\BlockMine.jpg')
        time.sleep(1)
        print ('BlockMine.jpg has been saved to the Color folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "3":
        ColorB_colors = B_colors
        ColorB_colors = ImageEnhance.Color(B_colors)
        ColorB_colors.enhance(8.0).save('Color\BlockColors.jpg')
        time.sleep(1)
        print ('BlockColors.jpg has been saved to the Color folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "4":
        ColorB_ice = B_ice
        ColorB_ice = ImageEnhance.Color(B_ice)
        ColorB_ice.enhance(8.0).save('Color\BlockIce.jpg')
        time.sleep(1)
        print ('BlockIce.jpg has been saved to the Color folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "5":
        ColorB_insanecolor = B_insanecolor
        ColorB_insanecolor = ImageEnhance.Color(B_insanecolor)
        ColorB_insanecolor.enhance(8.0).save('Color\BlockInsaneColors.jpg')
        time.sleep(1)
        print ('BlockInsaneColors.jpg has been saved to the Color folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "6":
        ColorB_lego = B_lego
        ColorB_lego = ImageEnhance.Color(B_lego)
        ColorB_lego.enhance(8.0).save('Color\BlockLego.jpg')
        time.sleep(1)
        print ('BlockLego.jpg has been saved to the Color folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "7":
        ColorB_lights = B_lights
        ColorB_lights = ImageEnhance.Color(B_lights)
        ColorB_lights.enhance(8.0).save('Color\BlockLights.jpg')
        time.sleep(1)
        print ('BlockLights.jpg has been saved to the Color folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "8":
        ColorB_normal = B_normal
        ColorB_normal = ImageEnhance.Color(B_normal)
        ColorB_normal.enhance(8.0).save('Color\BlockNormal.jpg')
        time.sleep(1)
        print ('BlockNormal.jpg has been saved to the Color folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "9":
        ColorB_small = B_small
        ColorB_small = ImageEnhance.Color(B_small)
        ColorB_small.enhance(8.0).save('Color\BlockSmall.jpg')
        time.sleep(1)
        print ('BlockSmall.jpg has been saved to the Color folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)
    elif choiceofblock == "10":
        ColorB_transparent = B_transparent
        ColorB_transparent = ImageEnhance.Color(B_transparent)
        ColorB_transparent.enhance(8.0).save('Color\BlockTransparent.jpg')
        time.sleep(1)
        print ('BlockTransparent.jpg has been saved to the Color folder')
        time.sleep(2)
        print ('You will now return to the choices')
        time.sleep(2)

def colorsave():
    if input("do you want to enhance the color of an image? [Y] Or do you want to go back to the choices [N] ") == 'y':
        blockcolor()
    else:
        choice

#this is where you choose what you want to convert
while True:
    choice = input('''What do you want to do today? 
[1] convert all jpg to png?
[2] turn an image to black and white? 
[3] rotate an image to any size? 
[4] decide what size should be the thumbnail?
[5] blur any of the images?
[6] enhance the color of any of the images?
''')
#the choices of what you picked
    if choice == "1":
        pngsave()
    elif choice == "2":
        BWsave()
    elif choice == "3":
        rotatesave()
    elif choice == "4":
        thumbnailsave()
    elif choice == "5":
        blursave()
    elif choice == "6":
        colorsave()