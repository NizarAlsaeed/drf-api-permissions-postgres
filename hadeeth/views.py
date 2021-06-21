from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Hadeeth
from .serializers import HadeethSerializer
# Create your views here.
class HadeethList(ListCreateAPIView):
    queryset = Hadeeth.objects.all()
    serializer_class = HadeethSerializer

class HadeethDetail(RetrieveUpdateDestroyAPIView):
    queryset = Hadeeth.objects.all()
    serializer_class = HadeethSerializer
