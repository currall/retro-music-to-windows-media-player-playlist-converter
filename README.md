# "Retro Music" Playlist to "Windows Media Player" Playlist Converter

Converts playlists created in Retro Music (https://play.google.com/store/apps/details?id=code.name.monkey.retromusic&gl=US&pli=1) to playlists compatable with Windows Media Player

# Windows Media PLayer (Legacy)

> python

> from converter import create_wpl_playlist

> create_wpl_playlist("playlist","playlist.m3u")

- Replace "playlist" with desired playlist name
- Replace "playlist,m3u" with filename of Retro Music playlist to convert

Copy new wpl playlist to Windows' music\playlist folder

# Media Player (Windows 11 version)

> python

> from converter import create_m3u8_playlist

> create_m3u8_playlist("playlist","playlist.m3u",music_path)

- Replace "playlist" with desired playlist name
- Replace "playlist,m3u" with filename of Retro Music playlist to convert
- Replace "music_path" with music location on PC, e.g "C:\\\Files\\\Music"
  - Use double backslashes for sub-directories
  - No need to include backslashes at end of path

Copy new m3u8 playlist to Windows' music\playlist folder
