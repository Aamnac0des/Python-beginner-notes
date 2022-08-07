import os
#print(dir(os))...shows all attributes and methods we have access to.
#print(os.getcwd())...get current working directory

##os.chdir("/home/aamnac0des")
##print(os.getcwd()) #...navigates

#print(os.listdir()) #...lists files and folders in the current directory

#to create a new folder
##os.mkdir("os-demo")
##os.makedirs("os-demo/sub-dir1") #..creates dir few levels deep..easier if you wanna create a tree struc
##print(os.listdir())


#to delete dir
##os.rmdir("os-demo") #...specifically deletes the exact dir
#os.removedirs("os-demo/sub-dir1") #..will delete all intermediate dir
##print(os.listdir())

#to rename a file or folder
##os.rename("Article.txt", "FILE.txt")
##print(os.listdir())

#looking at info about a file
##print(os.stat("FILE.txt")) #..prints gibberish..size
##print(os.stat("FILE.txt").st_size) #..prints only size value from the gibberish

#to print time in readable format (of when the file was last modified)
##from datetime import datetime
##mod_time = os.stat("FILE.txt").st_mtime
##print(datetime.fromtimestamp(mod_time))

#to see entire dir tree and files within
##for dirpath, dirnames, filenames in os.walk("/home/aamnac0des"): #..tuple of 3 values
##    print('current path:', dirpath)
##    print('directories:', dirnames)
##    print('files:', filenames)

#to print env variables of a dir..accessing home dir location by grabbing its env variable
##print(os.environ) #..prints all env variables
##print(os.environ.get("HOME")) #..prints only home env variable

#to check if a path exists..returns true/false
##print(os.path.exists("/tmp/test.txt"))

#to check if given path contains a file or directory..returns true/false
##print(os.path.isdir("/home/aamnac0des"))
##print(os.path.isfile("/home/os.py"))
##
##print(os.path.splitext("/home/os.py"))

##print(dir(os.path))
