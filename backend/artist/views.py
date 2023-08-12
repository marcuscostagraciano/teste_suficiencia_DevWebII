from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.views import APIView
from .serializer import ArtistSerializer
from .models import Artist
# Create your views here.
class ArtistAPIView(APIView):
    serializer_class = ArtistSerializer

    def get(self,request):
        artist_id = request.query_params.get('q',None)
        if artist_id:
            artists = Artist.objects.filter(id=artist_id)
        else:
            artists = Artist.objects.all()
        
        if artists:
            artist_serializer = self.serializer_class(artists,many=True)
            return Response(artist_serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'message':'artist not found'},status=status.HTTP_404_NOT_FOUND)
        
        