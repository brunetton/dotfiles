# Workaround to disable copy on delete (https://github.com/fish-shell/fish-shell/issues/772)
set FISH_CLIPBOARD_CMD "cat"

alias s="cd .."
alias nemo="nemo ."
alias atom="atom ."
alias gitg="gitg --all "
alias gg="git log --oneline --abbrev-commit --all --graph --decorate --color"
