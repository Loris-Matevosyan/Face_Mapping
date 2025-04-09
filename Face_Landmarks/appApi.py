from Network.apiConnection import ApiConnection
from Network.addResource import add_resource
from Network.Endpoints.imageUrl import ProcessImage
from Network.Authentication.login import Login



apiConnection = ApiConnection()
api = apiConnection.getApi()
add_resource(api)

apiConnection.initialize()
