"""docstring for run.py app import create_app."""
import os
from app import create_app

config_name = os.getenv("FLASK_ENV")
app = create_app(config_name)

if __name__ == "__main__":
    app.run(threaded=True)
