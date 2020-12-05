import pytube


url = ''

playlist = pytube.Playlist(url)
for url in playlist:
    video = pytube.Youtube(url)
    stream = video.streams.get_by_tag(22)
    stream.download()
    