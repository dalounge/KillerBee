for band in music_list.keys():
    band_dir = os.path.join(current_dir, band)
    
    if not os.path.exists(band_dir):
        os.mkdir(band_dir)
    else:
        print('Already Exists')
        print(band)
        
    for albums in music_list[band].keys():
        album_dir = os.path.join(band_dir, albums)
        if not os.path.exists(album_dir):
            os.mkdir(album_dir)
        else:
            print('ALBUM location already exists faggot')
        for songs in music_list[band][albums]:
            song_mp3 = os.path.join(album_dir, songs + '.mp3')
            if not os.path.exists(song_mp3):
                file = open(song_mp3, 'w')
                file.close()
            else:
                print(f'{songs} exists already')
