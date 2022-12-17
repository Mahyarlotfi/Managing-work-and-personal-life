"""Run This File For Deployment Tasks And Migrating Database To Latest Revision"""
from flask_migrate import (
    upgrade,
    migrate,
    init,
    stamp
    )

from pms import app

from pms.extensions import db

from pms.models import User


def deploy():
    """Run deployment tasks."""
    app.app_context().push()
    db.create_all()
    # migrate database to latest revision
    init()
    stamp()
    migrate()
    upgrade()


deploy()
