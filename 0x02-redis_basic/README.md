# 0x02. Redis Basics

### Learning Objectives

In this documentation, you will delve into the fundamentals of Redis, a powerful in-memory data store. By the end of this module, you will have acquired the following skills and knowledge:

- Basic Redis Operations: You will learn how to use Redis for basic operations, such as data storage, retrieval, and manipulation.

- Redis as a Simple Cache: Understand how to employ Redis as a simple and effective caching mechanism to enhance the performance and responsiveness of your applications.

Redis is a versatile tool with various use cases, and mastering its basic functionalities is a crucial step in harnessing its potential for a wide range of applications.

Requirements

Before you embark on using Redis for your project, make sure to meet the following requirements:

- *Operating System*: Your code will be interpreted/compiled on Ubuntu 18.04 LTS using `Python 3` (version 3.7).

- *File Endings*: Ensure that all your code files end with a newline character.

- *Documentation*: You must create a `README.md` file, and it should be placed at the root of your project folder.

- *Shebang Line*: The very first line of all your Python files must be `#!/usr/bin/env python3`.

- *Coding Style*: Your code should adhere to the `pycodestyle` style, with version 2.5 being the recommended style guide for maintaining code consistency.

- *Module Documentation*: All your Python modules must have documentation. You can generate module documentation using the following command:
```shell
python3 -c 'print(__import__("my_module").__doc__)'
```

- *Class Documentation*: Ensure that all your classes come with comprehensive documentation. You can generate class documentation using this command:
```shell
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```

- *Function and Method Documentation*: Document all your functions and methods. Use the following commands to generate function and method documentation:
	- For functions:
	```shell
	python3 -c 'print(__import__("my_module").my_function.__doc__)'
	```
	- For methods within a class:
	```shell
	python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
	```

- *Meaningful Documentation*: Documentation is more than just a word; it's a complete sentence explaining the purpose of the module, class, or method. Ensure that your documentation provides meaningful insights, and be aware that the length of the documentation will be checked for adequacy.

- *Type Annotations*: All your functions and coroutines must be properly type-annotated to enhance code clarity and maintainability.


### Installing Redis on Ubuntu 18.04

- To set up Redis on Ubuntu 18.04, follow these steps:

Install the Redis server:
```bash
$ sudo apt-get -y install redis-server
```
	
Install the Redis Python client:
```bash
$ pip3 install redis
```

Configure Redis to bind to 127.0.0.1:
```bash
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

### Using Redis in a Container

When using Redis within a container, keep in mind that the Redis server is initially stopped. To start the Redis server when initializing a container, use the following command:
```bash
$ service redis-server start
```

With Redis properly installed and configured, you can now begin employing it for basic operations and caching in your Python projects.
