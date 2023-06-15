from flask import render_template, request, url_for, redirect
from app.questions import bp
from app.models.question import Question
from app.extensions import db
from app.questions.form import QuestionForm


@bp.route('/', methods=('GET', 'POST'))
def index():
    forma = QuestionForm()
    questions = Question.query.all()
    if request.method == 'POST' and forma.validate_on_submit() is True:
        new_question = Question(content=forma.content.data,
                                answer=forma.answer.data)
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('questions.index'))

    return render_template('questions/index.html', questions=questions, form=forma)
