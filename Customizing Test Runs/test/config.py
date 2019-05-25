class Config:
	def __ini__(self, env):

		# SUPPORTED_ENVS = ['dev', 'qa']

		# if env.lower() not in SUPPORTED_ENVS:
		# 	raise Exception(f'{env} is not supported environment. Supported envs is {SUPPORTED_ENVS}' )

		self.base_url = {
		'dev': 'https://mydev_env.com',
		'qa': 'https://myqa_nenv.com'
		}[env]

		self.app_port = {
		'dev': 8080,
		'qa': 80
		}[env]