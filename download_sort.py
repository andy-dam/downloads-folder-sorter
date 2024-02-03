import os

def main():
    path = "C:\\Users\\" + os.getlogin() + "\\Downloads\\"
    files = [f for f in os.listdir(path) if os.path.isfile(path + f)]
    print(files)
    
if __name__ == "__main__":
    main()