"""This module allows us to run the code on the internet"""
# pylint: disable=import-error
from app.app import app

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
