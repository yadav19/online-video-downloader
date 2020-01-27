# Onvid (online video downloader)

## Description:
    Onvid is a class module {inside vids package} built on python solely made for downloading one file video streaming files into a user specified name
    
## Implementation:
    implementing the onvid class is very easy.
    this has been illustrated by onvid.py    

### > Onvid Components:
    data members:
        - url : the url to the stream video
        - save_name : the preferred name of the file after downloading
    member functions:
        - constructor:
            -- can be called with class name with two positional arguments {url , save} 
                e.g. : yt = onvid("-url-to-the-video","downloaded-video")
        - download :
            -- takes no argument.
            -- main downloading engine is defined here

### PS: all downloaded file are by default .mp4
