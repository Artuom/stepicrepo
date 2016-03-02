def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    query = environ['QUERY_STRING']
    list_of_arguments = query.replace("&", "\n")
    return list_of_arguments
