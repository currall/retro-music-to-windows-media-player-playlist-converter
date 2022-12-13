def get_filelist(playlist_m3u,raw):

    playlist2 = []

    f = open(playlist_m3u,"r")
    playlist = f.readlines()
    playlist[-1] = playlist[-1] + "\n"

    for i in range(len(playlist)):
        if playlist[i][0] == "/": # remove lines that arent filenames
            j = 0
            while playlist[i][j-5:j] != "Music":
                j += 1

            filename_raw = playlist[i][j:-1]
            
            if raw:
                filename = filename_raw.replace("/","\\")# filter out illegal characters
                playlist2.append(filename)
            else: # apply filter if using old media player
                filename = filename_raw.replace("/","\\")# filter out illegal characters
                filename = filename.replace("&","&amp;") 
                filename = filename.replace("'","&apos;")
                playlist2.append(filename)
            
        else:
            playlist[i] = ""

    return(playlist2)

def create_wpl_playlist(name,m3u):

    m3u = get_filelist(m3u,False)

    f = open(name+".wpl","a") # create wpl playlist

    playlist = [
'<?wpl version="1.0"?>\n', # default wmp playlist junk
'<smil>\n',
    '\t<head>\n',
        '\t\t<meta name="Generator" content="Microsoft Windows Media Player -- 12.0.22621.1"/>\n',
        '\t\t<meta name="ItemCount" content="'+str(len(m3u))+'"/>\n',
        '\t\t<author/>\n',
        '\t\t<title>'+str(name)+'</title>\n',
    '\t</head>\n',
    '\t<body>\n',
        '\t\t<seq>\n'
        ]

    for i in range(len(m3u)):
        playlist.append('\t\t\t<media src="..\All Music'+m3u[i]+'"/>\n')

    playlist.append('\t\t</seq>\n')
    playlist.append('\t</body>\n')
    playlist.append('</smil>\n')

    for i in range(len(playlist)):
        f.write(playlist[i])

def create_m3u8_playlist(name,m3u,music_dir):

    m3u = get_filelist(m3u,True)

    f = open(name+".m3u8","a") # create m3u8 playlist

    playlist = [
'#EXTM3U\n',
'#'+name+'.m3u8\n'
        ]

    for i in range(len(m3u)):
        playlist.append(music_dir+m3u[i]+'\n')

    for i in range(len(playlist)):
        f.write(playlist[i])

# Enter Playlist Name and Retro Music Playlist filename
# Example commands:

#create_wpl_playlist("playlist","playlist.m3u")
#create_m3u8_playlist("playlist","playlist.m3u","C:\\Files\\Music")
