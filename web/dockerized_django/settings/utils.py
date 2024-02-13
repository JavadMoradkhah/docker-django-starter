import os

def env_file(var_name, *args, **kwargs):
    """
    Read the content of a file that has been set to an environment variable
    """
    value = os.getenv(var_name, *args, **kwargs)

    if value and os.path.isfile(value):
        with open(value) as f:
            return f.read()

    return ""


def split_env(var_name, separator, default):
    value = os.environ.get(var_name)
    return value.split(separator) if value is not None else default