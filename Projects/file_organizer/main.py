import os

def rename(files, ext):
    file_with_ext = [file for file in files if file.endswith(ext)]
    i = 1
    for i  in file_with_ext:
        os.rename(i, f"photo-{i}{ext}")
        i +=1
        
    print(file_with_ext)


if __name__ == "__main__":
    files = os.listdir()
    rename(files, ".jpg")