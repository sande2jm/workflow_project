import abc
from subprocess import call
import sys

class DockerImageCreator(abc.ABC):

	def getVersion(self):
		path = 'workflow_configuration' + '/' + self.imageName + '_version.txt' 
		with open(path, 'r+') as f:
			tag = f.readline()
		return tag.rstrip()

	def updateVersion(self):
		path = 'workflow_configuration' + '/' + self.imageName + '_version.txt' 
		with open(path, 'w') as f:
			f.write(str(round(float(self.tag)+ 0.1,1)))
		self.pushStateRepo()

	def getStateFromRepo(self):
		cmds = ['git submodule add --force https://sande2jm@github.com/sande2jm/workflow_configuration.git']
		self.runCommands(cmds)
		self.tag = self.getVersion()

	def cleanupStateRepo(self):
		cmds = ['git rm -rf workflow_configuration']
		self.runCommands(cmds)

	def pushStateRepo(self):
		cmds = ['git submodule foreach git add * ', 
				'git submodule foreach git commit -m test',
				'git submodule foreach git push origin master']

		self.runCommands(cmds)


	def runCommands(self, cmds):
		for cmd in cmds:
			cmd = cmd.split(' ')     
			call(cmd)
	
	def run(self):
		cmds = ['docker build -t '+ self.imageName + ' ../' + self.package, 
				'docker tag ' + self.imageName + " " + self.username + '/' + self.imageName + ':' + self.tag,
				'docker push ' + self.username + '/' + self.imageName + ':' + self.tag]

		self.runCommands(cmds)


	def __repr__(self):
		return " ".join(map(str, [self.imageName, self.package, self.tag, self.username]))