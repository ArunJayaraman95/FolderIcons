from PIL import Image

imgInput = input("Enter Name of Picture: ")


# Open Images
folderImg = Image.open(r"BaseFolder.png").convert("RGBA")
overImg = Image.open(fr"{imgInput}.png").convert("RGBA")

# Set Widths
overW = overH = 400

fX = fY = 1080
mid = fX / 2
overX = int(mid - overW // 2)
overY = int(mid + 50 - overH // 2)
# Crop Overlay Image
overImg = overImg.resize((overW, overH))



# Overlay Coords
overlayCoords = (overX, overY, overX + overW, overY + overH)
folderImg.paste(overImg, overlayCoords, mask = overImg)

folderImg.show()

folderImg.save(fr"C:\Users\ripar\Pictures\Icons\{imgInput}.ico", format='ICO', sizes=[(256,256)])