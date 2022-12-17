"""Flask Application entry point."""
from pms import app
from pms.extensions import db
from pms.models import User


@app.shell_context_processor
def make_shell_context():
    """ Registers a shell context processor function """
    return {'db': db, 'User': User}


if __name__ == '__main__':
    app.run(debug=True)
