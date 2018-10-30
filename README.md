# social-computing-tokachu-backend

### Setup dev env

- `cd` into project root folder.
- `python3 -m venv venv && . ./venv/bin/activate && pip install -r requirements.txt`
  - If you got error `Could not find a version that satisfies the requirement in python`, [follow this SO post](https://stackoverflow.com/questions/49745995/pip-install-django-results-in-no-matching-distribution-found-for-django), run this:

```bash
curl https://bootstrap.pypa.io/get-pip.py | python
pip install --upgrade setuptools
```

  - Then, run `pip install -r requirements.txt` again.

- If you got error when installing `mysqlclient`, try this:
  - Did you install mysql? If not, run:
    - `brew install mysql@5.7 && brew link --force mysql@5.7`
    - `echo 'export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"' >> ~/.bash_profile or ~/.zshrc`
    - `export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"`
    - `brew services start mysql@5.7`
    - Remove the `venv` and start over again (from the top of this section).

- Did you recently upgrade to Macos Mojave?
  - If so, run `sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /`
  - Remove the `venv` and start over again (from the top of this section).


- copy `credentials.py` if you haven't had one under `django_backend/`
- `eb init`
- For region choose `14`.
- If prompt to enter `aws_access_key_id` & `aws_secret_access_key`, use those in `aws-shaungc-gmail-credentials.csv`.
- `Select an application to use`, choose the one that says `sctokachudev`.
- `Do you wish to continue with CodeCommit? (y/N)`, say `N` or hit enter.

### Start coding!

- Make changes.
- Test how it works `./manage.py runserver`
- `git add . && git commit -m "fix" && git push`
- `eb deploy`. Wait for it to finish. 
- `eb open` to open the website / server.

### ~~Initial Setup~~

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