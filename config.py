class Config:
    def __init__(self, env):
        self.base_url = {
            'dev': 'https://mydev-env.com',
            'qa': 'https://myqa-env.com'
        }[env]