# 2023 - Week 2 - Programming Language
## 1. Python: Module, package, decorator
Follow this [instruction](docs/BDH-T04-01.Programminglanguage.pdf)
- Run simple my own python code with decorator, module & package
    - I created a folder named `python_practice`, a `main.py` file and a folder named `my_package` inside the `python_practice` folder
    - Inside `my_package`, I created [decorator.py](src/python_practice/my_package/decorator.py) and [my_module.py](src/python_practice/my_package/my_module.py) to test the decorator
- Run main folder to check the result
    ```bash
    python main.py
    ```
- The result should be
    ```
    This is some text!
    Hello, world!
    This is another text!
    ```
- **Working tree**
    ```
    └── python_practice
        ├── main.py
        └── my_package
            ├── decorator.py
            ├── my_module.py
    ```
## 2. Sanic framework
- Clone this API with Sanic Framework: [Pet store API](https://petstore.swagger.io/) (1/2 query/command)
- Clone data model
- Build data table with model
- Connect database with API
- Build API with Sanic 
- **Note**: For more details of this excercise, please refer [here](src/my_app/README.md)

## 3. Additional exercise
- The mentor asked me to write a **decorator** to check if the random status code return 400 or 401 we will catch that error and return some execption.
- The repository of this exercise [here](https://github.com/gotecq-huuphan/example-01) 
- Check my solution [here](src/example-01/decorator.py)