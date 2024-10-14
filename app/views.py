from django.shortcuts import render

    
class Podcasts:
    @staticmethod
    def PodCast(requests):
        return render(
            requests,
            'app/podcast.html'
        )