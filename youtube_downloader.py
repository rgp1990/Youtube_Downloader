from pytube import Playlist
from pytube import YouTube

prompt = '\nEnter "v" to download video, "p" to download playlist or "q" to quit: '

def download_playlist(link):
    p = Playlist(link)

    print(f'Downloading: {p.title}')

    for video in p.videos:
        video.streams.get_highest_resolution().download()

def download_video(link):
    v = YouTube(link)

    print(f'Downloading: {v.title}')

    v.streams.get_highest_resolution().download()

options = {
    'v': download_video,
    'p': download_playlist
}

def menu():
    selection = input(prompt)
    
    while selection != 'q':
        link = input('Add URL: ')
        if selection in options:
            selected_function = options[selection]
            selected_function(link)
        else:
            print('Unknown command. Please try again.')
        
        selection = input(prompt)

menu()
