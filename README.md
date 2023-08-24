<h1 align="center">⌨️ 🦾 Zsh Starcodex</h1>

<p align="center">
    AI in the command line.
</p>

<p align="center">
    <a href="https://github.com/tom-doerr/zsh_codex/stargazers"
        ><img
            src="https://img.shields.io/github/stars/tom-doerr/zsh_codex?colorA=2c2837&colorB=c9cbff&style=for-the-badge&logo=starship style=flat-square"
            alt="Repository's starts"
    /></a>
    <a href="https://github.com/tom-doerr/zsh_codex/issues"
        ><img
            src="https://img.shields.io/github/issues-raw/tom-doerr/zsh_codex?colorA=2c2837&colorB=f2cdcd&style=for-the-badge&logo=starship style=flat-square"
            alt="Issues"
    /></a>
    <a href="https://github.com/tom-doerr/zsh_codex/blob/main/LICENSE"
        ><img
            src="https://img.shields.io/github/license/tom-doerr/zsh_codex?colorA=2c2837&colorB=b5e8e0&style=for-the-badge&logo=starship style=flat-square"
            alt="License"
    /><br />
    <a href="https://github.com/tom-doerr/zsh_codex/commits/main"
		><img
			src="https://img.shields.io/github/last-commit/tom-doerr/zsh_codex/main?colorA=2c2837&colorB=ddb6f2&style=for-the-badge&logo=starship style=flat-square"
			alt="Latest commit"
    /></a>
    <a href="https://github.com/tom-doerr/zsh_codex"
        ><img
            src="https://img.shields.io/github/repo-size/tom-doerr/zsh_codex?colorA=2c2837&colorB=89DCEB&style=for-the-badge&logo=starship style=flat-square"
            alt="GitHub repository size"
    /></a>
</p>

<p align="center">
    <img src='https://github.com/tom-doerr/bins/raw/main/zsh_codex/zc4.gif'>
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
https://github.com/KukumavMozolo/zsh_codex.git ~/.oh-my-zsh/custom/plugins/zsh_codex 
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

5. Run `zsh`, start typing and complete it using `^X`([Ctrl] + X)!


## Troubleshooting 

### Unhandled ZLE widget 'create_completion'

```
zsh-syntax-highlighting: unhandled ZLE widget 'create_completion'
zsh-syntax-highlighting: (This is sometimes caused by doing `bindkey <keys> create_completion` without creating the 'create_completion' widget with `zle -N` or `zle -C`.)
```

Add the line 
```
zle -N create_completion
```
before you call `bindkey` but after loading the plugin (`plugins=(zsh_starcodex)`).

### Already exists and is not an empty directory
```
fatal: destination path '~.oh-my-zsh/custom/plugins'
```
Try to download the ZSH plugin again.
```
git clone https://github.com/tom-doerr/zsh_starcodex.git ~/.oh-my-zsh/custom/plugins/zsh_starcodex
```
---
<p align="center">
    <a href="https://www.buymeacoffee.com/TomDoerr" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
</p>

## More usage examples
<p align="center">
    <img src='https://github.com/tom-doerr/bins/raw/main/zsh_codex/update_insert/all.gif'>
    <p align="center">
    </p>
</p>

-------------------------------------------------------------------

[Fish Version](https://github.com/tom-doerr/codex.fish)

[Traffic Statistics](https://tom-doerr.github.io/github_repo_stats_data/tom-doerr/zsh_codex/latest-report/report.html)
