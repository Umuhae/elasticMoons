from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from elasticsearch import Elasticsearch
from django.conf import settings


class SearchView(APIView):

    def get(self, request):
        es = Elasticsearch(hosts=settings.ELASTICSEARCH_SERVER)

        # 검색어
        search_word = request.query_params.get('search')

        if not search_word:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})

        docs = es.search(index='matjib',
                         body={
                             "query": {"query_string": {"query": search_word}}
                         })

        data_list = docs['hits']
        return Response(data_list)
