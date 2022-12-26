# DNS-practice

Name of Domain: fzaidi.tech <br>
A-Record Settings: Host Name: @, Value: 34.172.65.212, TTL: 7200 <br>
Cloud Vendor: GCP <br>

Instructions: <br>

Use External IP address from VM (34.172.65.212) <br>
Go to Manage Orders, select DNS Management, select Manage DNS <br>
Add A record with Hostname: @; Destination: (public IP address); TTL: 7200 <br>

GCP SSH browser: <br>
$ sudo apt-get update<br>
$ sudo apt install python3-pip <br>
$ pip3 install flask <br>
$ git clone https://github.com/zf81/DNS-practice <br>
$ cd DNS-practice <br>
$ sudo python3 app.py <br>
