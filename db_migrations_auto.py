import os
from alembic.config import Config
from alembic import command
from datetime import datetime


class DBMigrations:
    @classmethod
    def autogenerate_and_run(cls):
        alembic_cfg = Config(os.path.join(os.path.dirname(__file__), "alembic.ini"))

        # Dynamic migration name
        message = f"auto_migration_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # 1️⃣ Generate migration script
        command.revision(alembic_cfg, message=message, autogenerate=True)

        # 2️⃣ Apply all migrations
        command.upgrade(alembic_cfg, "head")
