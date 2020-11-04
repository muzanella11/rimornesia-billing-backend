from app.config.migrations import MigrationsConfig

class SeederPaymentLog(object):
    ACTION = MigrationsConfig().getAction()

    def __init__(self):
        super(SeederPaymentLog, self).__init__()
    
    def run(self):
        action = {}

        action['payment_log'] = {
            'action': self.ACTION.get('insert'),
            'command': (
                "LOCK TABLES `payment_log` WRITE;"
                "INSERT INTO `payment_log` (`action`, `value`, `created_at`) VALUES"
                " ('created', 'SUCCESS CREATED', now())"
                "UNLOCK TABLES"
            )
        }

        return action