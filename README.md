# Personal-Management-System

The purpose of creating this program is to create a Personal Management System and learning programming

Hello friends
This is the first program that I am writing and I am currently developing it. I sincerely thank everyone who helps in the development of this program.


## Set up & Installation.

### 1 .Clone/Fork the git repo and create an environment 
                    
**Windows**
          
```bash
git clone https://github.com/Mahyarlotfi/Personal-Management-System.git
cd Personal-Management-System
py -3 -m venv venv

```
          
**macOS/Linux**
          
```bash
git clone https://github.com/Mahyarlotfi/Personal-Management-System.git
cd Personal-Management-System
python3 -m venv venv

```

### 2 .Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 3 .Install the requirements

Applies for windows/macOS/Linux

```
pip install -r requirements.txt
```
### 4 .Migrate/Create a database

```python manage.py```

### 5. Run the application 

**For linux and macOS**

```python run.py```

**On windows**
```
set FLASK_APP=routes
flask run
```
