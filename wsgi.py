# -*- coding: utf-8 -*-
from simpleappps import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(threaded=True, port=5000)
