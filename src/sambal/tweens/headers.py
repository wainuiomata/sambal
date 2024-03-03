class SecurityHeaders:
    """Tween that sets various security headers in a single tween."""

    def __init__(self, handler, registry):
        self.handler = handler
        self.settings = registry.settings

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
        # It does not make sense to set this header if https is turned off.
        if self.settings["sambal.hsts"] and self.settings["sambal.https"]:
            response.headers["Strict-Transport-Security"] = "max-age=15768000"

        return response
