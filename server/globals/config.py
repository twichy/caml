import os

from dotenv import dotenv_values

CONFIG = {
    **os.environ,
    **dotenv_values('.env'),
    **dotenv_values('../.env'),
}

CONFIG['CAML_PORT'] = CONFIG.get('CAML_PORT', "3333")
CONFIG['CAML_DOMAIN'] = CONFIG.get('CAML_DOMAIN', "0.0.0.0")
