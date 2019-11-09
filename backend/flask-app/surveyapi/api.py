"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Survey, Question, Choice

api = Blueprint('api', __name__)


@api.route('/surveys/', methods=['GET'])
def fetch_surveys():
    surveys = Survey.query.all()
    return jsonify({'surveys': [s.to_dict() for s in surveys]})


@api.route('/surveys/', methods=['POST'])
def create_survey():
    data = request.get_json()
    survey = Survey(name=data['name'])

    questions = []
    for q in data['questions']:
        question = Question(text=q['text'])
        question.choices = [Choice(text=c['text'])
                            for c in q['choices']]
        questions.append(question)
    survey.questions = questions

    db.session.add(survey)
    db.session.commit()

    return jsonify(survey.to_dict()), 201


@api.route('/surveys/<int:id>/', methods=['GET'])
def get_survey(id):
    survey = Survey.query.get(id)
    return jsonify({'survey': survey.to_dict()})


@api.route('/surveys/<int:id>/', methods=['PUT'])
def update_survey(id):
    data = request.get_json()
    for q in data['questions']:
        choice = Choice.query.get(q['choice'])
        choice.selected = choice.selected + 1

    db.session.commit()
    survey = Survey.query.get(data['id'])

    return jsonify(survey.to_dict()), 201
