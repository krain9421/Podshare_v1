from flask import session
from app import db
from app.models.like import Like
from app.utils.response import generate_response
from app.utils.constants import HTTP_201_CREATED


class LikeController:
    def like(post_id, post=True):
        current_user_id = session.get("user").get("id")
        new_like = Like(user_id=current_user_id)
        if post:
            new_like.post_id = post_id
        else:
            new_like.comment_id = post_id
        db.session.add(new_like)
        db.session.commit()
        return generate_response(
            data={}, message=f"{post_id} Liked", status_code=HTTP_201_CREATED
        )
