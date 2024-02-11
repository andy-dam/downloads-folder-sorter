import os
import filetype

class FileSorter:
    def __init__(self, path):
        self.path = path
        self.files = [f for f in os.listdir(path) if os.path.isfile(path + f)]
        self.folders = [f for f in os.listdir(path) if os.path.isdir(path + f)]

    def sort_file(self, file) -> str:
        extension = filetype.guess(self.path + file)
        current_path = self.path + file
        if extension is None:
            if not os.path.exists(self.path + "Miscellaneous"):
                os.makedirs(self.path + "Miscellaneous")
            new_path = self.path + "Miscellaneous\\" + file
        else:
            extension = extension.extension
            if not os.path.exists(self.path + extension):
                os.makedirs(self.path + extension)
            new_path = self.path + extension + "\\" + file
        os.rename(current_path, new_path)
        return new_path
    
    def sort_files(self):
        for file in self.files:
            self.sort_file(file)
    
def main():
    path = "C:\\Users\\" + os.getlogin() + "\\Downloads\\"
    unsorted_files = FileSorter(path)
    print(path)
    
if __name__ == "__main__":
    main()