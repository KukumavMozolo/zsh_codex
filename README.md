<h1 align="center">⌨️ 🦾 Zsh Starcodex</h1>

<p align="center">
    AI in the command line.
</p>

<p align="center">
    </a>
    </a>
    <a href="https://github.com/tom-doerr/zsh_codex/blob/main/LICENSE"
        ><img
            src="https://img.shields.io/github/license/tom-doerr/zsh_codex?colorA=2c2837&colorB=b5e8e0&style=for-the-badge&logo=starship style=flat-square"
            alt="License"
    /><br/>
</p>

<p align="center">
https://github.com/KukumavMozolo/zsh_starcodex
    <img src='https://github.com/KukumavMozolo/rep/raw/main/images/starcodex.gif'>
    <p align="center">
        You just need to write a comment or variable name and the AI will write the corresponding code.
    </p>
</p>


## What is it?

This is a ZSH plugin that enables you to use starcoder in the command line. No internet connection required. Tested with linux only though.

## How do I install it?
### Manual Installation
1. Install https://github.com/bigcode-project/starcoder.cpp and quantize the ```HuggingFaceH4/starchat-beta``` model.

2. Download the ZSH plugin.

```
https://github.com/KukumavMozolo/zsh_starcodex.git ~/.oh-my-zsh/custom/plugins/zsh_starcodex 
```

3. Add the following to your `.zshrc` file.

Using oh-my-zsh:
```
    plugins=(zsh_starcodex)
    bindkey '^X' create_completion
```
Without oh-my-zsh:
```
    # in your/custom/path you need to have a "plugins" folder and in there you clone the repository as zsh_starcodex
    export ZSH_CUSTOM="your/custom/path"
    source "$ZSH_CUSTOM/plugins/zsh_starcodex/zsh_starcodex.plugin.zsh"
    bindkey '^X' create_completion
```

4. Edit the config.json in ```~/.oh-my-zsh/custom/plugins/zsh_starcodex/``` so that ```path_to_starcoder_cpp_main``` points
to your starcoder.cpp directory

5. Run `zsh`, start typing and complete it using `^X`([Ctrl] + X)! and use Tap select an option
