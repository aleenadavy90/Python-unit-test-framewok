# Python-unit-test-framewok

# To Spin up Ubuntu Server 16.04 using Amazon AWS

   Choose AMI Ubuntu Server 16.04 Lts (HVM), SSD, Volume type-ami- 2ef48339 from AWS Ec2 instance

   To access ssh -i keypair.pem ubuntu@public ip

# To Install web server Nginx on the VM instance

   sudo apt-get update
   sudo apt-get install nginx
   sudo ufw app list
   sudo ufw allow 'Nginx HTTP'

# To see if the server is running

  systemctl status nginx

  When server's IP address or domain is availble, enter it into your browser's address bar
  http://server_domain_or_IP

# Testing framework used

  Python-UnitTest-Selenium

# Prerequisite

  Python 2.7.13
  Firefox browser 46.0.1
  Selenium 2.53.2
  pip install necessary packages

# Running tests

  Run the NginxTestSuite in nginxtests package or from the commandline

  python NginxTestSuite.py
