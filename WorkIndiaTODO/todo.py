from app import app,db
from app.models import user, todo

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': user, 'Todo': todo}