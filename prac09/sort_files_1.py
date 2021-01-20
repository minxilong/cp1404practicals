import shutil
import os

def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('FilesToSort')
    file_list = os.listdir('.')
    ext_list = []
    for file in file_list:
        if os.path.isdir(file):
            continue
        # Get extension
        ext = os.path.splitext(file)[1]
        ext_list.append(ext)
        try:
            os.mkdir(ext.strip('.'))
        except:
            pass
        shutil.move(file, os.path.join(ext.strip('.'), os.path.basename(file)))

main()