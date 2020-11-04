from app.config.migrations import MigrationsConfig

class DatabaseStructure(object):
    ACTION = MigrationsConfig().getAction()
    TABLES = {}

    def __init__(self):
        super(DatabaseStructure, self).__init__()

    def init_structure(self):
        self.payment_table()
        self.payment_log_table()
        self.payment_session_table()

        return self.TABLES

    def payment_table(self):
        self.TABLES['payment'] = {
            'action': self.ACTION.get('create'),
            'command': (
                "CREATE TABLE IF NOT EXISTS `payment` ("
                "   `id` int(100) unsigned NOT NULL AUTO_INCREMENT,"
                "   `code` varchar(100) DEFAULT '',"
                "   `user_id` int(100) DEFAULT NULL,"
                "   `amount` bigint(20) DEFAULT NULL,"
                "   `unique_code` int(20) DEFAULT NULL,"
                "   `booking_id` int(100) DEFAULT NULL,"
                "   `booking_code` varchar(100) DEFAULT NULL,"
                "   `type` varchar(50) DEFAULT NULL,"
                "   `transaction_id` text,"
                "   `transaction_time` datetime DEFAULT NULL,"
                "   `transaction_status` varchar(50) DEFAULT NULL,"
                "   `payment_token` varchar(100) DEFAULT NULL,"
                "   `created_at` datetime DEFAULT NULL,"
                "   `updated_at` datetime DEFAULT NULL,"
                "   PRIMARY KEY (`id`)"
                ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci"
            )
        }

    def payment_log_table(self):
        self.TABLES['payment_log'] = {
            'action': self.ACTION.get('create'),
            'command': (
                "CREATE TABLE IF NOT EXISTS `payment_log` ("
                "   `id` int(100) unsigned NOT NULL AUTO_INCREMENT,"
                "   `action` varchar(50) DEFAULT NULL,"
                "   `value` text,"
                "   `created_at` datetime DEFAULT NULL,"
                "   `updated_at` datetime DEFAULT NULL,"
                "   PRIMARY KEY (`id`)"
                ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci"
            )
        }

    def payment_session_table(self):
        self.TABLES['payment_session'] = {
            'action': self.ACTION.get('create'),
            'command': (
                "CREATE TABLE IF NOT EXISTS `payment_session` ("
                "   `id` int(100) unsigned NOT NULL AUTO_INCREMENT,"
                "   `token` varchar(100) DEFAULT NULL,"
                "   `expired` text,"
                "   `created_at` datetime DEFAULT NULL,"
                "   `updated_at` datetime DEFAULT NULL,"
                "   PRIMARY KEY (`id`)"
                ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci"
            )
        }