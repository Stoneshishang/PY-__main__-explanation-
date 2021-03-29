# if the first_module.py is being imported, then the string would be
# string+<file name>, so __name__ = first_module
print("First Module's name is: {}, this will always be run.".format(__name__))


def main():
    print("First Module's main() method: {}".format(__name__))


# It is checking to see if this file is run directly by python or
# it is being imported.If it is imported, __name__ = <file name> instead of '__main'
if __name__ == "__main__":
    main()
    print("Run Directly")
else:
    print("Run from Import")
