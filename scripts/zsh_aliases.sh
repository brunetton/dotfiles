alias ggui='git gui &!'
alias gig='gitg --all &!'
alias gitg-reflog='gitg --all `git reflog | cut -c1-7`&!'
alias ll="ls -lh"
alias la="ls -al"
alias s="cd .."
alias vi="vim"
alias start_jupyter-notebook-dbnomics="jupyter notebook --notebook-dir ~/dev/jailbreak/dbnomics/notebooks/ --no-browser --NotebookApp.token=''"
alias start_jupyter-notebook-here="jupyter-notebook --notebook-dir . --no-browser --NotebookApp.token=''"
alias less="less -R"  # Less with colors enabled
alias fd="fdfind"
alias lsblk='lsblk -o NAME,TYPE,SIZE,FSAVAIL,RO,MOUNTPOINT | grep -P "^loop" -v'

docker-rm-stopped() {
    docker rm $(docker ps -a -q)
}

docker-bash-i() {
    if [[ "$1" == "" ]]; then
        echo "Usage: $0 [image_id]"
        return 0
    fi
    docker run --rm -it "$1" bash
}

docker-bash-c() {
    if [[ "$1" == "" ]]; then
        echo "Usage: $0 [container_id]"
        return 0
    fi
    docker exec -it "$1" bash
}

c() {
    if [[ "$1" == "" ]]; then
        code .
    else
        code --new-window "$( dirname "$1" )" "$1"
    fi
}


# alias yay-list-package-files="yay -Ql"
# alias yay-search-file="yay -Qo"
# alias yay-show-all-packages="yay -Qq | fzf --preview 'yay -Qil {}' --layout=reverse --bind 'enter:execute(yay -Qil {} | less)'"
# alias yay-show-installed="yay -Qi"
# alias yay-show-non-installed="yay -Si"
# alias yay-uninstall="yay -Rs"
# alias yay-update="yay -Sy"

# alias z='cd ` ~/dev/dbnomics/custom-scripts/print_fetcher_dir.py`'
# alias zj='cd ` ~/dev/dbnomics/custom-scripts/print_fetcher_dir.py -j `'
# alias zs='cd ` ~/dev/dbnomics/custom-scripts/print_fetcher_dir.py -s `'
