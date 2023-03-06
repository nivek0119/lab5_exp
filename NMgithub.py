from git import Repo

repo = Repo.clone_from("https://github.com/nivek0119/netman_Lab5.git", "/home/kevin/Netman/Lab_5_Midterm/")
remote = repo.create_remote(remote_name, url=another_url)
remote.push(refspec='{}:{}'.format(local_branch, remote_branch))

hello
