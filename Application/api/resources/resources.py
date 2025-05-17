from ..endpoints.login_url import Login
from ..endpoints.image_url import ProcessImage


def add_resource(api):
    api.add_resource(Login, '/login')
    api.add_resource(ProcessImage, '/image')