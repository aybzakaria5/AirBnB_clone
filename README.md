# AirBnB Clone - The Console

![AirBnB Clone Logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231106%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231106T232100Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=531bbc9f08ccb4575254a68da9cbec7e70f4659a35365eb69c397c305dc765db)

## Project Description
This project is a command-line interface (CLI) for an AirBnB clone implemented in Python. The CLI allows users to manage AirBnB objects and perform various operations on them. It serves as the foundation for a full-fledged AirBnB web application and provides essential functionality for creating, retrieving, updating, and deleting objects.

## Command Interpreter
The command interpreter is a shell-like interface that allows users to interact with the AirBnB clone. It provides the following features:

- Create new AirBnB objects (e.g., User, Place).
- Retrieve objects from storage (file or database).
- Perform operations on objects (e.g., count, compute statistics).
- Update attributes of objects.
- Delete objects.

## How to Start
To start the AirBnB clone command interpreter, run the `console.py` script as follows:
```bash
$ ./console.py
```

## How to Use
The command interpreter supports a variety of commands to manage AirBnB objects. You can access the list of available commands by typing `help` in the interpreter. Here are some common commands:

- `create <class>`: Create a new object of the specified class.
- `show <class> <id>`: Display information about an object by class and ID.
- `all <class>`: Show all objects of a specific class.
- `update <class> <id> <attribute> "<value>"`: Update the specified attribute of an object.
- `destroy <class> <id>`: Delete an object by class and ID.
- `quit`: Exit the command interpreter.

## Examples
Here are some examples of how to use the AirBnB clone command interpreter:

```bash
(hbnb) help
(hbnb) create User
(hbnb) show User 12345
(hbnb) all User
(hbnb) update User 12345 name "John Doe"
(hbnb) destroy User 12345
(hbnb) quit
```

## Repository Organization
We use branches and pull requests on GitHub to facilitate collaboration and organization of our work.

## Repository
- [GitHub Repository: AirBnB_clone](https://github.com/Lelaabk/AirBnB_clone)

Feel free to explore and contribute to the project!
