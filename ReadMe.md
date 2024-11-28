## Ejemplo Python Selene Appium Request Cucumber Framework

Herramientas a utilizar en el proyecto:
1. **Python**
2. **Cucumber** como framework
3. **Appium** para la automatización mobile
3. **PIP3** 
4. **VSCode** 

#### Getting Started
Setup your machine.
1. Python > 3.7 
2. Install VSCode & open the repo
3. On Terminal, navigate to repo and run following commands
    a. Create Virtual Env ```python3 -m venv behavex-env```
    b. Activate Virtual Env ```source behavex-env/bin/activate```
    c. Install Packages ```pip3 install -r requirements.txt```

#### Running tests
* Run tests in Sequence: ```browser=chrome behavex```
* Run tests in Parallel: ```browser=chrome behavex --parallel-processes 5 --tags @test```

#### Report
* Report will be found here: ```/output/report.html```
---


