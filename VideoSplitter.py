from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip, ffmpeg_extract_audio

ffmpeg_extract_subclip("temp/qaran.mp4", 28800 , 43200 , targetname="qaran43200.mp4")

#ffmpeg_extract_audio("temp/qaran.mp4", "qaran.mp3")