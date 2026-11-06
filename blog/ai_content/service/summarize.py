from blog.models import Post
from ..client import ContentClient

MAX_SUMMARY_LENGTH = 500
_client = ContentClient()


class PostNotFoundError(ValueError):
    """Subclass of ValueError so the service keeps one error contract."""


def _build_prompt(text: str) -> str:
    return (
        f"Summarize the following blog post in at most "
        f"{MAX_SUMMARY_LENGTH} characters. Return only the summary.\n\n{text}"
    )


def summarize_post(post_id):
    if isinstance(post_id, bool) or not isinstance(post_id, int) or post_id <= 0:
        raise ValueError("post_id must be a positive integer.")

    post = Post.objects.filter(pk=post_id).first()
    if post is None:
        raise PostNotFoundError(f"Post with id {post_id} does not exist.")

    if not post.content or not post.content.strip():
        raise ValueError("Post content is empty.")

    summary = _client.generate(_build_prompt(post.content)).strip()
    if not summary:
        raise ValueError("The model returned an empty summary.")
    summary = summary[:MAX_SUMMARY_LENGTH].strip()

    return {
        "post_id": post.pk,
        "title": post.title,
        "summary": summary,
        "length": len(summary),
    }