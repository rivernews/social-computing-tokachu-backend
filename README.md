# social-computing-tokachu-backend

### Setup dev env

- `python3 -m venv venv && . ./venv/bin/activate && pip install -r requirements.txt`
- copy `credentials.py` if you haven't had one under `django_backend/`
- `eb init`
- For region choose `14`.
- If prompt to enter `aws_access_key_id` & `aws_secret_access_key`, use those in `aws-shaungc-gmail-credentials.csv`.
- `Select an application to use`, choose `1`.
- `Do you wish to continue with CodeCommit? (y/N)`, say `N` or hit enter.

### Start coding!

- Make changes.
- `git add . && git commit -m "fix" && git push`
- `eb deploy`. Wait for it to finish. 
- `eb open` to open the website / server.

### ~~Initial Setup on Ubuntu~~

- get sudo access, run command `su`
- `apt install git`
- `git clone https://github.com/rivernews/social-computing-tokachu-backend.git`
- cd into project.
- `python3 -m venv venv && . ./venv/bin/activate && pip install -r requirements.txt`

- Setup database model

- Prepare local credentials
- Create AWS account
- Create [IAM user](http://www.1strategy.com/blog/2017/05/23/tutorial-django-elastic-beanstalk/)
- Modify `~/.aws/config`, [See this post](https://stackoverflow.com/questions/29190202/how-to-change-the-aws-account-using-the-elastic-beanstalk-cli)

- Create new key pair...
- No permission creating service link role? [See this post.](https://www.reddit.com/r/aws/comments/97q92g/aws_educate_how_to_create_rds_instance/) Setup [Servie link role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html)
  - You should now be able to craete a db on RDS! MySQL may not require ssl so just comment out that in django `settings.py`.

- `ENV NAME` is `sctokachudev`