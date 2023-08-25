#!/usr/bin/env python3

import os
import json
import subprocess
import sys

conf = None
home_directory = os.path.expanduser('~')
with open(home_directory + '/.oh-my-zsh/custom/plugins/zsh_starcodex/config.json') as f:
    conf = json.load(f)

top_k = conf["top_k"]
top_p = conf["top_p"]
temp = conf["temp"]
n = conf["n"]
main = conf["path_to_lama.cpp"] + "main"
model = conf["path_to_lama.cpp"] + conf["model_name"]
system = """
You are the leading linux shell expert for writing the shortest commands possible, please help me to complete the command defined between then <|start|> and <|end|> tokens. 
Be brief, add nothing more. There will be only one question and one answer.
Here is an example of the required format:
<|start|> list files in current directory <|end|>
```ls```
"""
# params = f"--top_k {top_k} --top_p {top_p} --temp {temp} -n {n}"

start = '<|start|>'
end = '<|end|>'
eos = '[end of text]'
user = start + str(sys.argv[1]) + end
query = main + ' -m ' + model + ' --prompt \'' + system + user + '\''

pipe_path = "/tmp/tmp_pipe"
log = home_directory + '/.oh-my-zsh/custom/plugins/zsh_starcodex/info.log'
with open(pipe_path, 'w') as pipe, open(log, 'w') as log:
    log.write(f"------------Query------------ \n {query} \n ------------Outputs------------\n")
    process = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                               bufsize=1)
    with process.stdout:
        counter = 0
        push = False
        for line in iter(process.stdout.readline, ''):
            if push:
                pipe.write(line)
                pipe.flush()
            if "```ls```" in line:
                push = True
            if eos in line:
                push = False
            log.write(line)