import pytube

video_list = []
print("Enter urls (Terminate by 'Stop')")
while True:
    url = input("")
    if url == 'Stop':
        break
    video_list.append(url)

for x , video in enumerate(video_list):
    v = pytube.YouTube(video)
    stream = v.streams.get_by_itag(22)
    print(f"Download video {x}...")
    stream.download()
    print("done")