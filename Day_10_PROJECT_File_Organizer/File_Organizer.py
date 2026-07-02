import os
import shutil

categories = {
    "Images" : [".jpg", ".jpeg", ".png", ".avif"],
    "Videos" : [".mp4", ".mkv"],
    "Documents" : [".docx", ".pdf", ".txt", ".pptx", ".csv", ".ipynb", ".xls"],
    "Applications" : [".exe", ".apk"],
    "Music" : [".mp3", ".wav"],
    "Code" : [".py", ".html", ".c", ".js"],
    "Zip Files" : [".zip"]
}

folder = "messy_folder"

# print(os.listdir(folder))
for filename in os.listdir(folder):
    name, ext = os.path.splitext(filename)
    # print(os.path.splitext(filename))
    
    for category, extension in categories.items():
        if ext in extension:
            os.makedirs(f"{folder}/{category}", exist_ok=True)
            shutil.move(f"{folder}/{filename}", f"{folder}/{category}/{filename}")