import os

class FileSorter:
    def __init__(self, path):
        self.path = path
        self.files = [f for f in os.listdir(path) if os.path.isfile(path + f)]
        self.folders = [f for f in os.listdir(path) if os.path.isdir(path + f)]

    def sort_file(self, file):
        pass

def main():
    path = "C:\\Users\\" + os.getlogin() + "\\Downloads\\"
    unsorted_files = FileSorter(path)
    for file in unsorted_files.files:
        print(file)
    print(unsorted_files.files)
    print(unsorted_files.folders)
    
if __name__ == "__main__":
    main()