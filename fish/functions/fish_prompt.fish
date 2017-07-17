function fish_prompt --description 'Write out the prompt'
    # save last status
    set -l last_status $status

    # last status
    set last_status_string ""
    if [ $last_status -ne 0 ]
        set last_status_string (set_color --bold $fish_color_error)"($last_status)"
    end

    # Pwd
    set -l home_escaped (echo -n $HOME | sed 's/\//\\\\\//g')
    set -l pwd (echo -n $PWD | sed "s/^$home_escaped/~/" | sed 's/ /%20/g')
    set -l pwd (set_color $fish_color_cwd)$pwd

    set -l hostname (set_color --bold $fish_color_host)(hostname -s)
    set -l normal_color (set_color $fish_color_normal)

    # Git
    set -g __fish_git_prompt_color_branch magenta
    set -l git (__fish_git_prompt)

    # prompt symbol
    switch $USER
        case root; set prompt_symbol '#'
        case '*';  set prompt_symbol '$'
    end
    set -l prompt_symbol (set_color $fish_color_cwd)$prompt_symbol

    printf "%s %s%s %s%s %s" $hostname $pwd $git $last_status_string $prompt_symbol $normal_color
end

