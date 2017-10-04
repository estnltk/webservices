# Installation

Below are instructions on how to setup bare CentOS7 instance to run estnltk webservices software.

```
yum update
yum install wget screen swig epel-release nginx firewalld
yum groupinstall 'Development Tools'

# Setup firewall
firewall-cmd --set-default-zone=public
firewall-cmd --permanent --add-service=ssh
firewall-cmd --permanent --add-service=http
firewall-cmd --add-port=8000/tcp --permanent
firewall-cmd --reload
firewall-cmd --list-all
systemctl enable firewalld

# Setup nginx
systemctl start nginx
systemctl enable nginx

# Install conda
cd /opt
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
mkdir -p  /opt/anaconda/miniconda3
bash Miniconda3-latest-Linux-x86_64.sh
rm  Miniconda3-latest-Linux-x86_64.sh
adduser anaconda
chown -R anaconda:anaconda /opt/anaconda
chmod -R go-w /opt/anaconda
chmod -R go+rX /opt/anaconda
conda create -n estnltk_webservices python=3.5 ipython

# Install estnltk
source activate estnltk_webservices
cd /home/sass/
git clone https://github.com/estnltk/estnltk
cd estnltk
git checkout devel_1.6
pip install lxml
python setup.py build
python setup.py install

# Install webservices
source activate estnltk_webservices
cd /home/sass/
git clone git@github.com:estnltk/webservices.git
cd webservices
pip install django==1.11.5 uwsgi

ln -s /home/sass/webservices/mysite/mysite_nginx.conf /etc/nginx/sites-enabled/

# SELlinux
setenforce 0
setsebool -P httpd_can_network_connect 1

# Run uwsgi server
source activate estnltk_webservices
cd /home/sass/webservices/weblicht/mysite
uwsgi --ini mysite_uwsgi.ini
```