# -*- coding: utf-8 -*-

import os

import ckantoolkit as tk

from alembic.config import Config


def alembic_config():
    alembic_root = os.path.normpath(
        os.path.join(os.path.dirname(__file__), 'migration/workflow')
    )
    alembic_ini = os.path.join(alembic_root, 'alembic.ini')

    alembic_cfg = Config(alembic_ini)
    alembic_cfg.set_section_option(
        'alembic', 'sqlalchemy.url', tk.config.get('sqlalchemy.url')
    )
    alembic_cfg.set_section_option(
        'alembic', 'script_location', alembic_root
    )

    return alembic_cfg
