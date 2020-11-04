from app.core.migrations import Migrations
from app.migrations.db_structure import DatabaseStructure
import os

DB_NAME = os.environ.get('DB_NAME')

migrate = Migrations({
    'database': ''
})

# Create or Use database
migrate.create_database(DB_NAME)

# Close Connection
migrate.close_connection()