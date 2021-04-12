import json
import secrets

from redisary import Redisary
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from temlink.serializers import LinkSerializer

links = Redisary(db=1)


class GenerateLinkView(GenericAPIView):
    serializer_class = LinkSerializer

    # noinspection PyMethodMayBeStatic
    def post(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = secrets.token_urlsafe(4)
        links[token] = json.dumps(request.data)

        return Response(data={'token': token})


class LinkView(GenericAPIView):
    def get(self, request: Request, token: str) -> Response:
        if token not in links:
            raise Exception()

        link = json.loads(links[token])
        return Response(data=link)
