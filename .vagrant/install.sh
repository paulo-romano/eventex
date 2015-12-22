# Install essential packages from Apt
sudo apt-get update -y

#PyEnv requirements
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev git tree

#PyEnv install
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

#This is provisory. It will be in the .bash_aliases, but we need it know =D
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Updating PyEnv
pyenv update

# Install Python 3.5.0 and set it to be the default python
pyenv install 3.5.0
pyenv global 3.5.0

# Install Virtualenvwrapper plugin
git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper

# iPython notebook
pip install ipython[notebook]

# Copy bash_aliases
cp -p /vagrant_data/bash_aliases /home/vagrant/.bash_aliases

# Virtualenv
pip install virtualenv
#mkdir /home/vagrant/shared/wttd
#cd /home/vagrant/shared/wttd
#virtualenv .wttd --always-copy -p `which python`

# Heroku
sudo apt-get -y install python-dev python-psycopg2 libpq-dev
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku
heroku plugins:install git://github.com/ddollar/heroku-config.git
