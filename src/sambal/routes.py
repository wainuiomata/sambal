from sambal.resources import RootFactory


def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)
    config.set_root_factory(RootFactory)
    config.add_route("login", "/login/")
    config.add_route("logout", "/logout/")
