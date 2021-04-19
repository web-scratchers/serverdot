import os

os.system("sudo apt-get install -y openssl libssl-dev build-essential gdb tmux zlib1g-dev python3-pip")
os.system("ssh-keygen -t ed25519 -C \"amarjayr@umich.edu\" -q -N \"\" -f ~/.ssh/index")
os.system("ssh-keygen -t ed25519 -C \"amarjayr@umich.edu\" -q -N \"\" -f ~/.ssh/crawler")
os.system("ssh-keygen -t ed25519 -C \"amarjayr@umich.edu\" -q -N \"\" -f ~/.ssh/set")
os.system("ssh-keygen -t ed25519 -C \"amarjayr@umich.edu\" -q -N \"\" -f ~/.ssh/vector_string")

f = open("/home/boss/.ssh/config", "x")

config = """Host index
    Hostname github.com
    IdentityFile=~/.ssh/index

Host crawler
    Hostname github.com
    IdentityFile=~/.ssh/crawler

Host set
    Hostname github.com
    IdentityFile=~/.ssh/set

Host vector_string
    Hostname github.com
    IdentityFile=~/.ssh/vector_string"""

f.write(config)
f.close()

print("Index: ")
os.system("cat ~/.ssh/index.pub")
print("\n")

print("Crawler: ")
os.system("cat ~/.ssh/crawler.pub")
print("\n")

print("Set: ")
os.system("cat ~/.ssh/set.pub")
print("\n")

print("VectorString: ")
os.system("cat ~/.ssh/vector_string.pub")
print("\n")

input("Done? ")

os.system("cd ~; git clone git@crawler:web-scratchers/crawler.git")
os.system("cd ~; git clone git@index:web-scratchers/index.git")
os.system("cd ~/crawler; git config submodule.Vector_String.url git@vector_string:web-scratchers/Vector_String.git")
os.system("cd ~/index; git config submodule.Vector_String.url git@vector_string:web-scratchers/Vector_String.git")
os.system("cd ~/index; git config submodule.set.url git@set:web-scratchers/set.git")
os.system("cd ~/crawler; git submodule update --init")
os.system("cd ~/index; git submodule update --init")

os.system("curl -sSO https://dl.google.com/cloudagents/add-monitoring-agent-repo.sh && sudo bash add-monitoring-agent-repo.sh && sudo apt-get update && sudo apt-get install -y stackdriver-agent && sudo service stackdriver-agent start")
os.system("curl -sSO https://dl.google.com/cloudagents/add-logging-agent-repo.sh && sudo bash add-logging-agent-repo.sh && sudo apt-get update && sudo apt-get install google-fluentd && sudo apt-get install -y google-fluentd-catch-all-config && sudo service google-fluentd start")

os.system("mkdir ~/.config")
os.system("mkdir ~/.config/apport")
os.system("touch ~/.config/apport/settings")
os.system("""echo \"[main]
	unpackaged=true > ~/.config/apport/settings""")

os.system("sudo sysctl -w net.ipv4.ip_local_port_range=\"15000 64000\"")
os.system("sudo sysctl -w net.core.somaxconn=8192")
os.system("sudo sysctl --system")

os.system("pip3 install psutil")
os.system("pip3 install flask")