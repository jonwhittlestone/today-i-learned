
# git

Today I learnt ...

## ... how to use the ssh `.config file` to specify different SSH keys in `git push`

> 2023-01-09T19:38:34+00:00
>
> As a consultant with two different clients, and two different GitHub users, with their own ssh keys, how can we `git push` ?

### Recipe

If the user and hostname are the same but you must user a different SSH key:

1. Set up the `~/.ssh/config` file as follows

    ```bash
    Host github-as-client1
            HostName github.com
            User git
            IdentityFile ~/.ssh/id_ed25519.client1
            IdentitiesOnly yes

    Host github-as-client2
            HostName github.com
            User git
            IdentityFile ~/.ssh/id_ed25519.client2
            IdentitiesOnly yes
    ```

2. Instead of the real hostname, use the following in your `git remote`

    ```bash
    # client 1's repo
    git remote add origin git@github-as-client1:your-repo.git

    # client 2's repo
    git remote add origin git@github-as-client2:your-repo.git
    ```

#### Resources

- https://thucnc.medium.com/how-to-specify-different-ssh-keys-for-git-push-for-a-given-domain-bef56639dc02