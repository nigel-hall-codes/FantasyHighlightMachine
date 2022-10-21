from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=-BLZb9Xt2Xw&ab_channel=NFL')
yt.streams.first().download()