def pytest_addoption(parser):
	parser.addoption(
		'--env',
		action='store',
		# defalt='dev',
		help='Environment to run test against'
		)