# "Retro Music" Playlist to "Windows Media Player" Playlist Converter

Converts playlists created in Retro Music (https://play.google.com/store/apps/details?id=code.name.monkey.retromusic&gl=US&pli=1) to playlists compatable with Windows Media Player

# How to use

**Legacy Media Player**

> python

> from converter import create_wpl_playlist

> create_wpl_playlist("playlist","playlist.m3u")

- Replace "playlist" with desired playlist name
- Replace "playlist,m3u" with filename of Retro Music playlist to convert

Copy new wpl playlist to Windows' music\playlist folder

**Windows 11 Media Player**

> python

> from converter import create_m3u8_playlist

> create_m3u8_playlist("playlist","playlist.m3u",music_directory)

- Replace "playlist" with desired playlist name
- Replace "playlist,m3u" with filename of Retro Music playlist to convert
- Replace "music_directory" with music location on PC, e.g "C:\\Files\\Music"

Copy new m3u8 playlist to Windows' music\playlist folder
