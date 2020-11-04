from app.core.migrations import Migrations
from app.migrations.seeder.seeder_payment_log import SeederPaymentLog
from app.migrations.seeder.seeder_regencies import SeederRegencies
from app.migrations.seeder.seeder_districts import SeederDistricts
from app.migrations.seeder.seeder_villages import SeederVillages
import os

DB_NAME = os.environ.get('DB_NAME')

migrate = Migrations()
reconnect = False

# Create or Use database
migrate.create_database(DB_NAME)

# Seeder Data Payment Log
migrate.create_begin_process('Seeder Data Payment Log')
migrate.execute_command(
    SeederPaymentLog().run()
)
migrate.create_end_process('Seeder Data Payment Log')

# Reconnect db because `cursor.execute` cannot run multiple queries
reconnect = True

# Close Connection
migrate.close_connection()