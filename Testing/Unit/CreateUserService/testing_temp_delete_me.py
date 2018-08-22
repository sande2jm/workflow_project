from subprocess import call

cmds = ['git submodule foreach git add * ', 
		'git submodule foreach git commit -m test',
		'git submodule foreach git push origin master']
for cmd in cmds:
	call(cmd.split(' '))