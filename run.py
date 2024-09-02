from app import create_app

from logging_setup import logging_setup

logging_setup()

app = create_app()

if __name__ == '__main__':
    app.run(debug=False, port=4000)