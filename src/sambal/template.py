from .encoders import JSONEncoder


def includeme(config):
    """Configure the Jinja2 template environment.

    Register any custom template filters and custom tags here.
    """

    def setup_jinja2_env():
        """Configure Jinja2 tojson filter to use the custom JSONEncoder."""
        env = config.get_jinja2_environment()

        # Jinja2 cannot use adapters so use a custom JSONEncoder instead.
        env.policies["json.dumps_kwargs"].update(
            {
                "cls": JSONEncoder,
                "indent": 2,
                "sort_keys": True,
            }
        )

    config.action(None, setup_jinja2_env, order=999)
