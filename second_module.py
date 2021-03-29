import first_module

first_module.main()

# whenever python is running this file directly, it will print our
# string+ __main__
print("Second Module's name: {}".format(__name__))
