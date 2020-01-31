from pusher.middleware import MIDDLEWARE_LIST


def apply_middleware(app):
    """Apply flask middleware"""
    for middleware in MIDDLEWARE_LIST:
        app.before_request(middleware)
