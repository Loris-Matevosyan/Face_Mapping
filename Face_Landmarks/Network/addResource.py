from .Endpoints.imageUrl import ProcessImage
from .Authentication.login import Login


def add_resource(api):
    api.add_resource(ProcessImage, '/image')
    api.add_resource(Login, '/login')