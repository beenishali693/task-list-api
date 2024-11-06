from flask import Blueprint, abort, make_response, request
from ..db import db
from app.models.goal import Goal

goals_bp = Blueprint("goals_bp", __name__, url_prefix="/goals")

@goals_bp.post("")
def create_goal():
    request_body = request.get_json()

    try:
        title = request_body["title"]
        new_goal = Goal(title=title)
    except KeyError as error:
        response = {"details": "Invalid data"}
        abort(make_response(response, 400))

    db.session.add(new_goal)
    db.session.commit()

    response = {"goal": new_goal.to_dict()}

    return response, 201

@goals_bp.get("")
def get_all_goals():
    goals = db.session.scalars(db.select(Goal).order_by(Goal.id))
    goals_response = [goal.to_dict() for goal in goals]
    return goals_response

