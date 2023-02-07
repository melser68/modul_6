list_img = ['.JPEG', '.jpeg', '.PNG', '.png',
            '.JPG', '.jpg', '.SVG', '.svg']

list_archives = ['.rar', '.RAR', '.zip', '.ZIP',
                 '.gz', '.GZ', '.tar', '.TAR', '.7z', '.7Z']

list_videos = ['.AVI', '.avi', '.MP4', '.mp4',
               '.MOV', '.mov', '.MKV', '.mkv']

list_documents = ['.DOC', '.doc', '.DOCX', '.docs',
                  '.TXT', '.txt', '.PDF', '.pdf', '.XLSX', '.xlsx',
                  '.PPTX', '.pptx', '.xml', '.XML']

list_musics = ['.MP3', '.mp3', '.OGG', '.ogg',
               '.WAV', '.wav', '.AMR', '.amr']

suffix = '.txt'


dict_suffix = {
    'images': list_img,
    'archives': list_archives,
    'videos': list_videos,
    'musics': list_musics,
    'documents': list_documents
}

dict_rez = dict()

for k,i in dict_suffix.items():
    for y in i:
        if suffix == y:
            dict_rez.update({'images':suffix})
print(dict_rez)




