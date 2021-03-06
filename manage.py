from  flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager
from app import app, models, db
from app.models import User, Role, Pitch

app = app
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role, Pitch = Pitch )
if __name__ == '__main__':
    manager.run()