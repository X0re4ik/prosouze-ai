_register_models = ["promty"]


import_models = [
    "src.entities." + _register_model for _register_model in _register_models
]
