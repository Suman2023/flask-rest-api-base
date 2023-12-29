from flask import request, jsonify, Blueprint

from app import app, db
from app.models.post import Post, PostSchema

post_bp = Blueprint(name="post", import_name=__name__, url_prefix="/post")


@post_bp.route("/", methods=["POST"])
def create_post():
    try:
        data = request.get_json()
        post_schema = PostSchema()
        post_data = post_schema.load(data=data)
        new_post = Post(**post_data)
        db.session.add(new_post)
        db.session.commit()
        new_post = post_schema.dump(new_post) 
        return new_post, 201
    except Exception as e:
        app.logger.error(e)
        return str(e), 400


@post_bp.route("/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post_schema = PostSchema()
    post_exist = Post.query.get(post_id)
    if post_exist:
        return jsonify(post_schema.dump(post_exist))
    return "Not Found", 404


@post_bp.route("/<int:post_id>", methods=["PATCH"])
def update_post(post_id):
    post_schema = PostSchema()
    data = request.get_json()
    post_exist = Post.query.get(post_id)
    if post_exist:
        post_exist.text = data.get("text", post_exist.text)
        post_exist.is_sensitive = data.get("is_sensitive", post_exist.is_sensitive)

        db.session.commit()

        return jsonify(post_schema.dump(post_exist))
    else:
        return "Not Found", 404


@post_bp.route("/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post_exist = Post.query.get(post_id)
    if post_exist:
        db.session.delete(post_exist)
        db.session.commit()
        return post_id, 200
    return "Not Found", 404


@post_bp.route("/all", methods=["GET"])
def get_posts():
    post_schema = PostSchema()
    return jsonify(post_schema.dump(Post.query.all(), many=True))
