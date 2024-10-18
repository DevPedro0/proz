from django.shortcuts import render

    
class Podcasts:
    @staticmethod
    def PodCast(requests):
        return render(
            requests,
            'app/podcast.html'
        )
        
        
def Canais(requests):
    return render(
        requests,
        'app/canais.html'
    )
    

def Enquetes(requests):
    return render(
        requests,
        'app/enquetes.html'
    )