from haystack import indexes
from .models import LodgingOffer


class LodgingOfferIndex(indexes.SearchIndex, indexes.Indexable):

    # Cada SearchIndex requiere que uno de sus campos tenga document=True.
    # La convención es llamar a este campo text, y es el campo primario de
    # búsqueda
    # Con use_template=True le estamos diciendo a Haystack que este campo se
    # renderizará a una plantilla de datos para construir el documento que el
    # motor de búsqueda indexará
    text = indexes.CharField(document=True, use_template=True)

    # Tambien indexaremos ad_title to filter searchs by title
    # Con el parámetro model_attr indicamos que este campo
    # corresponde al campo patient del modelo
    ad_title = indexes.CharField(model_attr='ad_title', null=True)
    room_type_offered = indexes.CharField(model_attr='room_type_offered', null=True)

    # El método get_model()  devuelve el modelo para los documentos que serán
    # almacenados en éste índice.
    def get_model(self, using=None):
        return LodgingOffer

    # El metodo inxdex_queryset, retorna el QuerySet para los objetos
    # que serán indexados.
    # Podemos personalizar este query para que se retornen solo
    # las ofertas de alojamiento no tomadas.
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
