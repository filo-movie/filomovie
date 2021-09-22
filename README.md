# Filomovie


# 1. Clone the repo and cd to the project root directory
```
git clone https://github.com/filo-movie/filomovie.git
```

Set default heroku app
```
heroku git:remote -a filomovie

```


# 2. Create a virtual env: (Or use pycharm to create a virtual enviornment and install the requirements.txt file)

(I used Git Bash for the following operations)

## 2.1. In Git Bash, type: 
```
mkdir flask_memchache
export FLASK_APP=filomovie 	
cd flask_memcache
python -m venv venv
```

## 2.2. Go into virtual env and install required dependencies (Flask, Postgres, etc) locally. In Git Bash, type:
```
source venv/Scripts/activate
pip install -r requirements.txt
```

# 3. Test locally
```
flask run
heroku local
heroku local web
```


# 4. Deployment methods

## 4.1. Push to Git
```
git add .
git commit -m "message"
git push origin development
``` 

## 4.2. Push to heroku

