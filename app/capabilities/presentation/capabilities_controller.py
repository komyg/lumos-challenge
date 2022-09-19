from flask import Flask


def create_capabilities_handler(app: Flask):
    def get_capabilities():
        capabilities = {}
        for rule in app.url_map.iter_rules():
            if rule.endpoint != "static":
                capabilities[rule.rule] = list(rule.methods)

        return capabilities

    return get_capabilities
