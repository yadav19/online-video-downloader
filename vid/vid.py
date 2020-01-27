import requests

class onvid:
    def __init__(self,url,save_name):
        self.min_size = 256 #in bytes
        self.save_name = save_name
        self.url = url
        # self.download(self.url,self.save_name)

    def download(self):
        self.vid_data = requests.get(self.url, Stream=True)
        with open("{}.mp4".format(self.save_name),"wb") as vid_file:
            for pieces in self.vid_data.iter_content(chunk_size = min_size):
                vid_file.write(pieces) 
