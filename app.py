import os
from . import create_app # from __init__ file

app = create_app()

from .users import routes

if __name__ == "__main__":
    app.run()
