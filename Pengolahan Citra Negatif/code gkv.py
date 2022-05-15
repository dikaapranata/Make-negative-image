# Nama  : Handhika Pranata Kusuma Wardana
# Nim   : 24060121140112
# Kelas : D

# import Pillow modules
from PIL import Image

# Read pixels and apply negative transformation function
def Negativemaker(arrgambar):
    for i in range(0, arrgambar.size[0]-1):
        for j in range(0,arrgambar.size[1]-1):
            pixelColorVals = arrgambar.getpixel((i, j));
            # Invert color
            redPixel = 255 - pixelColorVals[0];  # Negate red pixel
            greenPixel = 255 - pixelColorVals[1];  # Negate green pixel
            bluePixel = 255 - pixelColorVals[2];  # Negate blue pixel
            arrgambar.putpixel((i, j), (redPixel, greenPixel, bluePixel));
    return arrgambar

# Load the  first image
img1 = Image.open(r"D:\Tugas1_GKV_D_Handhika Pranata Kusuma Wardana_24060121140112\image1.jpeg") 
# Display the first image
img1.show();
# Aplly function to make a negative image for first image
neg1 = Negativemaker(img1)
# Showing first negative image
neg1.show()

#Load the second image
img2 = Image.open(r"D:\Tugas1_GKV_D_Handhika Pranata Kusuma Wardana_24060121140112\image2.jpeg")  
# Display the second image
img2.show();
# Aplly function to make a negative image second image
neg2 = Negativemaker(img2)
# Showing second negative image
neg2.show()

#Load the third image
img3 = Image.open(r"D:\Tugas1_GKV_D_Handhika Pranata Kusuma Wardana_24060121140112\image3.jpeg") 
# Display the third image
img3.show();
# Aplly function to make a negative image for third image
neg3 = Negativemaker(img3)
# Showing third negative image
neg3.show()

#Load the fourth image
img4 = Image.open(r"D:\Tugas1_GKV_D_Handhika Pranata Kusuma Wardana_24060121140112\image4.jpeg")  
# Display the fourth image
img4.show();
# Aplly function to make a negative image for fourth image
neg4 = Negativemaker(img4)
# Showing fourth negative image
neg4.show()

#Load the fifth image
img5 = Image.open(r"D:\Tugas1_GKV_D_Handhika Pranata Kusuma Wardana_24060121140112\image5.jpeg")  
# Display the fifth image
img5.show();
# Aplly function to make a negative image for fifth image
neg5 = Negativemaker(img5)
# Showing fifth negative image
neg5.show()