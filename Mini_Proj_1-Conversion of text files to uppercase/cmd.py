import os
import time
import sys

arguments = sys.argv
if len(arguments) != 3:
    print("To Execute the script use the following syntax: ")
    print("python <nameoffile>.py indir outdir")
else :

    in_directory = arguments[1]
    out_directory = arguments[2]

    os.mkdir(out_directory)
    files = os.listdir(in_directory)
    start_time = time.time()
    for image in files:
        inputFile = open(f"{in_directory}/{file}","r")
        content = inputFile.read()
        outFile = open(f"{out_directory}/{file}","w")
        outFile.write(content.upper())

    end_time = time.time()
    print(f"Time Taken to Convert to Upper Case", end_time - start_time)
