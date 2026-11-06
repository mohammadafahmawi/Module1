import data
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ai_content.service.summarize import summarize_post, PostNotFoundError
from ..ai_content.service import _generate_post




@api_view(["POST"])
def summarize_post_view(request, post_id):
    try:
        return Response(summarize_post(post_id), status=status.HTTP_200_OK)
    except PostNotFoundError as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def generate_post(request:{data}):
    title = request.data.get("title", "")
    tone = request.data.get("tone")

    try:
        result = _generate_post(title, tone)
        return Response(result, status=status.HTTP_200_OK)
    except ValueError as exc:
        return Response({"error": str(exc)}, status=status.HTTP_400_BAD_REQUEST)