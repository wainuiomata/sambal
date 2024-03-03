class SecurityHeaders:
    """Tween that sets various security headers in a single tween."""

    def __init__(self, handler, registry):
        self.handler = handler
        self.registry = registry

    def __call__(self, request):
        response = self.handler(request)

        # Default set of security headers needs to be really strict.
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

        # HSTS is optional and is not automatically turned on if https is on.
        if self.registry.settings["sambal.hsts"]:
            response.headers["strict-transport-security"] = "max-age=15768000"

        return response
