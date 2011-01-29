from browserdetect import Browser


class BrowserDetectMiddleware:

    def process_request(self, request):
        request.browser = Browser(request)
        return None
