class BaseController:
    def __init__(self):
        # Initialize any common attributes or resources here
        pass

    def handle_request(self, request):
        # Common request handling logic can be implemented here
        raise NotImplementedError("Subclasses should implement this method")

    def send_response(self, response):
        # Common response sending logic can be implemented here
        return response

    def handle_error(self, error):
        # Common error handling logic can be implemented here
        return {"error": str(error)}