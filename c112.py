import os
import shutil

from_dir = "C:/Users/hp/Downloads";
to_dir = "C:/Users/hp/Desktop";

list_of_dir = os.listdir(from_dir);
print(list_of_dir)

for file_name in list_of_dir:
    root, extension = os.path.splitext(file_name)
    if extension =="":
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir +"/"+ file_name
        path2 = to_dir +"/"+"ImageDownload"
        path3 = to_dir +"/"+"ImageDownload"+"/"+file_name
        
        if os.path.exists(path2):
            print("moving the"+file_name+"......")
            shutil.move(path1,path3)

        else:
            os.mkdir(path2)
            print("moving the"+file_name+"......")
            shutil.move(path1,path3)
            