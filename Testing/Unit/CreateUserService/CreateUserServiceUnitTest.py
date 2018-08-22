from context import Deployment
from Deployment import CreateUserServiceDockerImageCreator
import os
import unittest

class CreateUserServiceUnitTest(unittest.TestCase):
    
	def setUp(self):
		self.config = CreateUserServiceDockerImageCreator()
		# self.config.getStateFromRepo()
		# self.config.run()
		# self.config.updateVersion()

	# def load_docker_image(self):
	# 	cmd = 'docker pull '+ self.config.username + '/' + self.config.imageName + ':' + self.config.tag
	# 	call(cmd.split(' '))

	# def run_docker_image(self):
	# 	cmd = 'docker run -d -p 4000:80 ' + self.config.imageName + ':' + self.tag
	# 	call(cmd.split(' '))
	def test_change_state_and_push(self):
		self.config.getStateFromRepo()
		self.config.updateVersion()
		self.config.cleanupStateRepo()
		prevTag = float(self.config.tag)
		self.config.getStateFromRepo()
		self.assertEqual(self.config.tag, str(prevTag + 0.1))

	def tearDown(self):
		self.config.cleanupStateRepo()

	# def test_service_is_running(self):
	# 	self.assertEqual(1,1)

	# def test_tag_value(self):
	# 	self.assertEqual(self.config.tag, '0.1')	


if __name__ == '__main__':
	unittest.main()

