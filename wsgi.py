from gunicorn.app.base import BaseApplication

class FlaskApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(FlaskApplication, self).__init__()

    def load_config(self):
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

gunicorn_options = {
    'bind': '0.0.0.0:5000',  # Adjust the host and port as needed
    'workers': multiprocessing.cpu_count() * 2 + 1,
    'threads': 2,
    'loglevel': 'info'
}

FlaskApplication(app, gunicorn_options).run()