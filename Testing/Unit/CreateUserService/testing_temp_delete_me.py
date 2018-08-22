from subprocess import call

cmds = ['cd workflow_configuration',
		'git add * ', 
		'git commit -m test',
		'git push ']
for cmd in cmds:
	call(cmd.split(' '))