# july3 - Build tool for deployment automation

july3 is [Make](https://en.wikipedia.org/wiki/Make) with Python syntax. See this july3file.py example.

    @Target('test-build/' + env.project_name, dependencies=['files/nginx-site.mako', 'test-build'])
    def nginx_site_file(target):
        with open(target.name, 'w') as f:
            f.write(Template(filename=target.dependencies[0]).render(**env))


    @Target('test-build')
    def build_dir(target):
        os.makedirs(target.name)
                
You can build target like this:

    july3 nginx_site_file
    
july3file.py and `july3` command works like Makefile and `make` command.


## Why july3?
july3 is developed to substitute [Fabric](http://www.fabfile.org/). It's a good deployment automation tool, but the writer of fabric is trying to separate it as two parts, ssh streamline and task managemant. ssh streamline part will be fabric 2.0, and task management became [invoke](http://www.pyinvoke.org/). I agree with the direction of changes, but I don't like invoke. It doesn't provide reliable dependency management, so each task should take care of idempotence by itself.

However, `Make` provides good way to define and calcuate dependencies. Actually you can write decent build description with `Make`. It has better design than modern automation tools like Maven, Gradle, Ansible, Chef and etc. You can define targets and dependencies in declarative way but write commands in programmtic way. So you don't need writing some kind of plugins to define new type of targets.

On of the weak points of `Make` is unfriendly syntax. Of course the target-dependencies-command structure is easy and clear, but the symbols like `$<` or `$@` are hard to remember, and shell script syntax is not familiar. I always google how to use if statement in bash.  `Make` only provides timestamp of file based dependencies. It works for most cases, but a few cases need other way of detect dependency, like service is running or package installed.

Therefore, I wrote july3 as more friendly `Make`, not as yet another Ant, Maven, Gradle, Fabric, Ansible or some other modern build tools.

## Install
july3 only support Python 3.x.

	pip install july3
	

## Batteries included
Because july3 is started as deployment automation tool and it's syntax is based on Python, it provides some contrib packages related to deployment of python tools.

 * python, pip, virtualenv
 * nginx, uwsgi
 * aiohttp
 * celery
 * postgres
 * ubuntu package
 
