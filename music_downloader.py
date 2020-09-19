#!/usr/bin/env python3

from segevmusic.tagger import Tagger
from segevmusic.applemusic import AMFunctions
from segevmusic.deezer import DeezerFunctions
from segevmusic.wetransfer import WTSession
from segevmusic.utils import ask
from shutil import rmtree
from sys import argv
from os.path import exists


def main(songs_path='./Songs'):
    app = DeezerFunctions.login(songs_path)
    tagger = Tagger(songs_path)
    songs = []
    songs_files = []
    to_continue = True
    # Adding songs
    while to_continue:
        try:
            songs.append(AMFunctions.search_song())
        except KeyError:
            print("--> ERROR: Nothing found; Check spelling errors.")
            continue
        to_continue = ask("--> Another song? (y/n): ")
    # Generate Deezer URLs
    songs_links = [DeezerFunctions.amsong_to_url(song) for song in songs]
    # Download songs
    DeezerFunctions.download(songs_links, app)
    # Tagging songs
    for song in songs:
        # Check if song was downloaded
        song_path = tagger.generate_isrc_path(song)
        if not exists(song_path):
            print(f"--> ERROR: Song {song.name} was not downloaded!")
            continue
        # Tag song
        tagger.tag_song(song)
        # Rename song file name
        song_file = tagger.rename_isrc_path(song)
        songs_files.append(song_file)
    # Upload files to WeTransfer
    wt_link = WTSession().upload(songs_files, f"Your {len(songs_files)} songs!")
    print("--> DONE!")
    print(f"--> Your download is available at {wt_link} and {songs_path}")
    # Remove deemix config files
    rmtree('./config', ignore_errors=True)


if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
    else:
        main()
