from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class VoteForm(FlaskForm):
    show = SelectField(u'Show',
    choices=[('Ain\'t Too Proud', 'Ain\'t Too Proud'),
    ('Chicago', 'Chicago'),
    ('Girl from the North Country', 'Girl From the North Country'),
    ('Hamilton', 'Hamilton (Best Choice)'),
    ('In the Heights', 'In the Heights'),
    ('Jesus Christ Superstar', 'Jesus Christ Superstar (Great Choice)'),
    ('The Book of Mormon', 'The Book of Mormon')], default='Hamilton')
    submit = SubmitField('Vote')
