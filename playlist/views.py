from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView

from .forms import VideoModelForm
from .models import VideoModel


# Create your views here.
def home(req):
    return render(req, 'playlist/index.html', {'salom': 'salaomaaaa'})


def HomeViews(request):
    video=VideoModel.objects.all()
    return render(request, 'playlist/index.html', {'video': video})


class VideoDetailView(DetailView):
    model = VideoModel
    template_name = 'playlist/detail.html'
    context_object_name = 'video'


class VideoPostView(CreateView):
    model = VideoModel
    template_name = 'playlist/download.html'
    fields = ['name', 'video']
    success_url = '/'
    context_object_name= 'video'



# def VideoDownloadViews(request):
#     from pytube import YouTube                                    

#     video_url = 'https://youtube.com/shorts/SzxQByYBPjs?si=SHBTC41gXFhqDMhv'
#     yt = YouTube(video_url)
#     stream = yt.streams
#     vid = stream.get_by_itag(137)
#     # vid2 = yt.streams.get_highest_resolution()
#     vid.download()

#     print("Video downloaded successfully!")
#     return render(request, 'playlist/download.html')




#
# from pytube import YouTube
# from pytube.exceptions import RegexMatchError


# def download_video(request):
#     if request.method == 'POST':
#         link = request.POST['link']
#         try:
#             video = YouTube(link)
#             stream = video.streams.get_highest_resolution()
#             stream.download()
#             return render(request, 'playlist/success.html')
#         except RegexMatchError:
#             return render(request, 'playlist/video-down.html', {'error': 'Noto\'g\'ri URL manzili. Iltimos, to\'g\'ri URL manzilini kiriting.'})
#         except Exception as e:
#             return render(request, 'playlist/video-down.html', {'error': f'Xato yuz berdi: {str(e)}'})
#     return render(request, 'playlist/video-down.html')


# from pytube import *
  
  
# defining function 
# def youtube(request): 
  
#     # checking whether request.method is post or not 
#     if request.method == 'POST': 
        
#         # getting link from frontend 
#         link = request.POST['link'] 
#         video = YouTube(link) 
  
#         # setting video resolution 
#         stream = video.streams.get_highest_resolution() 
          
#         # downloads video 
#         stream.download() 
  
#         # returning HTML page 
#         return render(request, 'playlist/video-down.html') 
#     return render(request, 'playlist/video-down.html')



            ################################################          
from django.views.generic import View
from pytube import YouTube
from django.shortcuts import render,redirect


class home(View):
    def __init__(self,url=None):
        self.url = url

    def get(self,request):
        return render(request,'playlist/test1.html')  
    
    def post(self,request):
        # for fetching the video
        if request.POST.get('fetch-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            vidTitle,vidThumbnail = video.title,video.thumbnail_url
            qual,stream = [],[]
            for vid in video.streams.filter(progressive=True):
                qual.append(vid.resolution)
                stream.append(vid)
            context = {'vidTitle':vidTitle,'vidThumbnail':vidThumbnail,
                        'qual':qual,'stream':stream,
                        'url':self.url}
            return render(request,'playlist/test1.html',context)

        # for downloading the video
        elif request.POST.get('download-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            stream = [x for x in video.streams.filter(progressive=True)]
            video_qual = video.streams[int(request.POST.get('download-vid')) - 1] 
            video_qual.download(output_path='../../Downloads')
            return redirect('home-dev')

        return render(request,'playlist/test1.html')
