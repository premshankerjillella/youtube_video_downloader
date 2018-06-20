import pytube

print("Enter the link of the video")
link=input()

yt = pytube.YouTube(link)
videos = yt.get_videos()

s=1
for v in videos:
	print(str(s)+" ."+str(v))
	s+=1

print("Enter the number of the video")
n=int(input())
vid=videos[n-1]


destination="C:\\Users\\PC\\Desktop"
vid.download(destination)

print("File has been succesfully downloaded")
