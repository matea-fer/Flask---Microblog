from app import create_app, db, cli
from app.models import User, Post


app = create_app()
cli.register(app)


### registers the function as a shell context function
@app.shell_context_processor
def make_shell_context():
    ### The reason the function returns a dictionary
    ### and not a list is that for each item you have to 
    ### also provide a name under which it will be referenced in the shell,
    ### which is given by the dictionary keys.
    return {'db': db, 'User': User, 'Post': Post}