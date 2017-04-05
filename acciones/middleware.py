
class MyMiddleware:
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With'
        response['Access-Control-Max-Age'] = '3600'
        response['Access-Control-Allow-Methods'] = 'POST, GET'
        return response