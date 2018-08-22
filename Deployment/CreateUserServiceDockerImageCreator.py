from .DockerImageCreator import DockerImageCreator

class CreateUserServiceDockerImageCreator(DockerImageCreator):
	def __init__(self):
		self.imageName = 'create_user_service'
		self.package = 'CreateUserService'
		self.username = 'sande2jm'
		self.tag = None



if __name__ == '__main__':
	test = CreateUserServiceDockerImageCreator()
	test.getStateFromRepo()
	test.run()
	test.updateVersion()