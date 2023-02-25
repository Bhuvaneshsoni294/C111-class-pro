import os
import shutil
#print(dir(os))

#os.getcwd()
#os.mkdir("Images")
#os.listdir()
#os.path.exists("pi")

path = "Desktop/whitehat jr/C111 Image/feather.jfif"
root, extension = os.path.splitext(path);
print("the root element are: ",root);
print("the extension element are: ",extension);

#os.listdir()
#source = "C:/hp/Desktop/whitehat jr/C111 Image/feather.jfif"
#destination = "C:/hp/Desktop/copy-father.jfif"
#dest = shutil.copy(source,destination)
#print(os.listdir(dest))
