from moviepy import VideoFileClip

clip = VideoFileClip("video.mp4")
clip.write_gif("video.gif", fps=10)