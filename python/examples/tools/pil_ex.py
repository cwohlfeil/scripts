from PIL import ImageColor, Image

# Get RGB values for color names
ImageColor.getcolor('red', 'RGBA')
ImageColor.getcolor('RED', 'RGBA')
ImageColor.getcolor('Black', 'RGBA')
ImageColor.getcolor('chocolate', 'RGBA')
ImageColor.getcolor('CornflowerBlue', 'RGBA')

# Open image and get metadata
catIm = Image.open('zophie.png')
catIm.size
width, height = catIm.size
width
height
catIm.filename
catIm.format
catIm.format_description
catIm.save('zophie.jpg')

# Make new transparent image
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')

# Crop
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')

# Copy and paste in to another image
catCopyIm = catIm.copy()
faceIm = catIm.crop((335, 345, 565, 560))
faceIm.size
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted.png')

# Tile
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
        for top in range(0, catImHeight, faceImHeight):
            print(left, top)
            catCopyTwo.paste(faceIm, (left, top))

# Resize
width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('svelte.png')

# Rotate
catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')
catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')

# Flip
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

# Change a pixel
im = Image.new('RGBA', (100, 100))
im.getpixel((0, 0))
for x in range(100):
        for y in range(50):
            im.putpixel((x, y), (210, 210, 210))

for x in range(100):
    for y in range(50, 100):
            im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
im.getpixel((0, 0))
im.getpixel((0, 50))
im.save('putPixel.png')
