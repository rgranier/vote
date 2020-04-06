'''
    This version requires that we do db.create_all() to set up the database
    before we do anything else.  The creation of the account is optional.
    How can we create the db dynamically using Flask-SQLAlchemy?

'''

# Import database info
from voteapp import db
from voteapp.models import Member, Vote

# Create the tables in the database
# (Usually won't do it this way!)
db.create_all()

defaultpw = 'L1n!M@nuel'

users = ['joseph', 'hasan', 'helbongo', 'jim', 'joel', 'ming', 'randall', 'sujata',
        'arshad', 'mike', 'saji']

for user in users:
    member = Member(user, 'password-clear')
    member.passwordHash = member.genPassword(defaultpw)
    db.session.add(member)
    db.session.commit()

vote = Vote('randall', 'Hamilton', '7')
db.session.add(vote)
db.session.commit()

print ("Setup complete.")
