"""Flask Application entry point."""
from app import app, db
from app.models import User


@app.shell_context_processor
def make_shell_context():
    """ Registers a shell context processor function """
    return {'db': db, 'User': User}


if __name__ == '__main__':
    app.run(debug=True)
