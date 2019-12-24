import Pyyaml
with open('./config.yml','r') as f:
    print(f.load())