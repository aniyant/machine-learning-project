# machine-learning-project
click below link to access the running application :
###[Application Active Web Url](https://ml-cicd-app.herokuapp.com/)

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = kumarsunny30066@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-cicd-app

>>>>>>> ba1fdb3221a67dd5595db0f7decfac52cfaca5f2

BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .
<<<<<<< HEAD
> Note: Image name for docker must be lowercase


To list docker image
docker images

Run docker image
docker run -p 5000:5000 -e PORT=5000 f8c749e73678

To check running container in docker
docker ps

Tos stop docker conatiner
docker stop <container_id>


To install setup.py or use directly pip install -r requirements.txt but make sure to add -e . int that.
python setup.py install
======

Install ipykernel
...
pip install ipykernel