from moviepy.editor import VideoFileClip
from os import listdir, mkdir


def VideoToMp3(targetDir):

    """
    Takes a Path as an argument scans it and converts each Video file duration to an MP3

    P.S doesn't support filtering, creates output folder
    
    ** targetDir: the path to scan for files

    """

    # Lists all files in the provided Dir
    Files = listdir(str(targetDir))

    # declare the start of the conversion view number of files found
    print("Processing: " + str(len(Files)))
    
    # try creating the folder
    try:
        # Creates output folder in target dir
        mkdir(str(targetDir) + "Output")
    except:
        # declares the directory exists
        print("directory already exists")
    
    # initiate counting process
    for file in Files:
        
        # try operation
        try:
            # declare the current file for conversion
            clip  = VideoFileClip( str(targetDir) + file)

            # Convert the file
            clip.audio.write_audiofile(str(targetDir) + "Output/" + str(file.split('.')[0]) + ".mp3" )
        # if operation fails
        except:
            print("damaged or unsupported file")

    # declares the end of the process
    print("Process completed!")

VideoToMp3("temp/")