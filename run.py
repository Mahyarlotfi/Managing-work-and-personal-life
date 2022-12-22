"""Flask Application entry point."""
from pms import app
from pms.extensions import db
from pms.models import (
    User,
    Bankname,
    Transitiontype,
    Transitionsubject,
    Transition
)


@app.shell_context_processor
def make_shell_context():
    """ Registers a shell context processor function """
    return {
    'db': db,
    'User': User,
    'Bankname': Bankname,
    'Transitiontype': Transitiontype,
    'Transitionsubject': Transitionsubject,
    'Transition': Transition
    }


if __name__ == '__main__':
    app.run(debug=True)
