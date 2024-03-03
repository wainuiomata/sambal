class SecurityHeaders:
    """Tween that sets various security headers in a single tween."""

    def __init__(self, handler, registry):
        self.handler = handler
        self.registry = registry

    def __call__(self, request):
        response = self.handler(request)
        response.headers.update(
            {
                "Content-Security-Policy": "default-src 'self'",
                "Cross-Origin-Embedder-Policy": "require-corp",
                "Cross-Origin-Resource-Policy": "same-site",
                "Cross-Origin-Opener-Policy": "same-origin",
                "Referer-Policy": "same-origin",
                "X-Content-Type-Options": "nosniff",
                "X-Frame-Options": "DENY",
                "Vary": "Cookie",
            }
        )
        return response
