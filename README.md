# social-computing-tokachu-backend

### Setup on Ubuntu

- get sudo access, run command `su`
- `apt install git`
- `git clone https://github.com/rivernews/social-computing-tokachu-backend.git`
- cd into project.
- `python3 -m venv venv && pip install -r requirements.txt`

- Setup database model

- Prepare local credentials
- Create AWS account
- Create [IAM user](http://www.1strategy.com/blog/2017/05/23/tutorial-django-elastic-beanstalk/)
- Modify `~/.aws/config`, [See this post](https://stackoverflow.com/questions/29190202/how-to-change-the-aws-account-using-the-elastic-beanstalk-cli)

- Create new key pair...
- No permission creating service link role? [See this post.](https://www.reddit.com/r/aws/comments/97q92g/aws_educate_how_to_create_rds_instance/) Setup [Servie link role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html)

- `ENV NAME` is `sctokachudev`