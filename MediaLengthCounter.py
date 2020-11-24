from moviepy.editor import VideoFileClip
from os import listdir


def MediaLengthCounter(targetDir):

    """
    Takes a Path as an argument scans it and reads each Video file duration to generate a report of the total amount

    P.S doesn't support filtering
    

    ** targetDir: the path to scan for files

    """

    # Lists all files in the provided Dir
    Files = listdir(str(targetDir))

    # starting value for the progress tracker
    valueHolder = 0

    # declare the start of the counting process and view number of files found
    print("Processing: " + str(len(Files)))
    
    # initiate counting process
    for file in Files:

        # try operation
        try:
            # add the current file duration to the last value
            valueHolder = valueHolder + VideoFileClip( str(targetDir) + file).duration

            # show progress
            print("Processing: " + str(Files.index(file)) + "/" + str(len(Files)), end= '\r')
        # if opertaion fails
        except:
            print("damaged or unsupported file")
    # declares the end of the process
    print("Process completed!")

    # report number of files scanned
    print("Files scanned : " + str(len(Files)))

    # report duration in seconds
    print("Time in second: " + str(valueHolder))

    # report duration in Minutes
    print("Time in Minutes: " + str(valueHolder / 60))

    # report duration in Hours
    print("Time in Hours: " + str(valueHolder / 60 / 60))

MediaLengthCounter("temp/")