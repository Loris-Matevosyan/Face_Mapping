from api.connection.connection import ApiConnection
from api.resources.resources import add_resource
from api.endpoints.login_url import Login
from api.endpoints.image_url import Image



apiConnection = ApiConnection()
api = apiConnection.getApi()
add_resource(api)

apiConnection.initialize()