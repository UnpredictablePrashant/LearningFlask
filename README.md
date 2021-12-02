# Ultimate and quick guide to learn Flask


Warning: This is just a practice exercise please don't use it for production.<br><br>

<p>
This project is to learn flask. Make sure you have python3 installed into your computer.</p><br>

<p>
The project is devided into four main folder, `practice` which contains the template for students to practice a small project and learn concepts around the flask, `material` which contains the material for learning flask,  `solution` which contains the solution for the template folder, and finally the `project` folder, which contains the list of projects that you can try after completing this tutorial. (I will try to see if I can add up the solution of the projects but don't have your hopes high as I don't have much time to create projects out of it.)</p>


## Starting with Flask


The first code that we write whenever we learn any programming language or framework is "Hello World!", we will start the same with flask. But before that let's understand some of the basic structure of flask.

### Hello World

Flask is not a webserver but a framework which makes your life easy. Let's create a folder called as `learnflask` and inside this create a python file, lets say `app.py` and write the below code:

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
```

<p>In the above code, we first imported the `flask` library and then created instance of it naming `app` and then created route for it. Well, route is basically how the URL will look like, if you want your URL to be something like `http://localhost:5000/helloworld` then the route will become something like this `@app.route('/helloworld')`. Whatever function declared below the route will decide what would be the logic for this route, that is what the `helloWorld()` function is doing. Finally, run the `app` instance using `app.run()`.</p>
<br>
<p>Now go to the terminal, don't forget to go to the folder where you have kept your flask code inside the terminal and run `python run.py`. Visit, the link which appears which would be something like `http://127.0.0.1:5000` and you can see that you are able to print `Hello World!`. Congratulations! You have written your first flask code.</p>

## Practice real life scenario

<p>In this small practice session we will write a web app which will have a landing page, a register page and a login page. Visit the folder practice and you will see the structure already present with you. Objectives are mentioned in comment format. Skills that you will be required to complete this would be: `html`, `css`, `python`,and `postgres` or `mysql`. I will be updating my tutorial on `postgres`, so just in case you are interested then star this project and you will be updated when I create a repo for it.</p>

<p>In the template you will have to follow the order in which you have to write the code.
</p>


## How to run the solution

Install the libraries from requirements.txt (remember some of it just because I faced specific problem while calling some libraries, you might not need all of it.)

```
pip install -r requirements.txt
python app.py
```

You can also try to work with `virtual environment` which is recommended but not covered here.

Note: For windows user, if you are getting error in installing virtualenv then open powershell and run `Set-ExecutionPolicy unrestricted` and choose option `A` (yes to all).

Note: Make sure you have `postgres` or `mysql` installed before working with this project, if not then it will fail.

## Further Learning

I will keep adding and updating the links with my projects around python. If you are interested in implementing machine learning model with python then follow the project which I created for one of my class.<br>
[Implement machine learning algorithm with flask](https://github.com/UnpredictablePrashant/MachineLearninginFlask)

