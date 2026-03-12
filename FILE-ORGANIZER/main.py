import os

def arrange_files(files, ext):
    files_with_extension = [file for file in files if file.endswith(ext)]
    print(files_with_extension)
    i = 1
    for file in files_with_extension:
        os.rename(file, f"photo-{i}{ext}")
        i += 1

if __name__ == "__main__":
    files = os.listdir()
    arrange_files(files, ".jpg")  # Pass extension with a leading dot