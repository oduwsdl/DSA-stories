apt-get update
add-apt-repository ppa:webupd8team/java
apt-get -y install oracle-java8-installer
apt-get -y install libgmp3-dev
apt-get -y install libxml2-dev libxmlsec1-dev
docker pull erikaris/memento-damage
git clone https://github.com/oduwsdl/DSA-stories.git
cd DSA-stories
pip install --upgrade pip
apt remove python-setuptools
pip install -r requirements.txt

