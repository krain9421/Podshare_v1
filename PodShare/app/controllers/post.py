import uuid
from flask import session, request
from app.models.post import Post
from app import db
from app.utils.response import generate_response
from app.utils.constants import HTTP_201_CREATED, HTTP_200_OK

class PostController:
    def all_posts(self):
        posts = db.session.query(Post).all()
        return generate_response(data=[post.to_json() for post in posts], status_code=HTTP_200_OK)

    def feed(self):
        posts = db.session.query(Post).order_by(Post.created_at).all()[:10]
        posts = [post.to_json() for post in posts]
        return generate_response(data=posts, message='User feed', status_code=HTTP_200_OK)
    
    def upload(self):
        audio = request.files.get('audio')
        caption = request.form.get('caption')
        audio_path = f'audio/{str(uuid.uuid4())}.{audio.filename.split(".")[1]}'
        post = Post(audio=audio_path, caption=caption, user_id=session.get('user').get('id'))
        audio.save(audio_path)
        db.session.add(post)
        db.session.commit()
        return generate_response(data=post.to_json(), message='Post Uploaded', status_code=HTTP_201_CREATED)
    
    def get_post(self, post_id):
        post = db.session.query(Post).filter_by(id=post_id).first()
        return generate_response(data=post.to_json(), message='Post', status_code=HTTP_200_OK)
