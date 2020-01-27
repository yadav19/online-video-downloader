from vids import vid
print("PS: Currently downloading feature from youtube is not available.")
input("press ENTER to continue...")
url = input("Enter the Video URL: ")
save = input("Enter the save name: ")

vid_obj = vid.Onvid(url,save)
vid_obj.download()