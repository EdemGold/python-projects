# CONTRIBUTION GUIDELINES

We are very excited to have you with us!

## Project Guidelines

- Use the `[Title Case Name](link)` format.
- All Folders should contain `-` inplace of ` ` or `_`.
- All Files should contain `_` inplace of ` ` or `-`
- Use concise descriptions.
- Pull requests should have a useful title.
- To add any Project, create a folder in the projects folder with a relevant category.
- Add the Project with detailed explanations in README.md file.
- If there are packages to be installed, create a `requirements.txt` file stating out the packages to be installed.
- Each folder should contain an `README.md` file.
  - The file should contain a brief introduction to project.
  - Any other resource or blog you think is appropriate or explains the meaning of your folder.
- Please mention It's difficulty level.
- Codes can be contributed using Jupyter Notebooks and `.py`, `.r` or `.jl` files. But Python and Jupyter Notebooks will be much appreciated because they support a clear explanation of code.


## Steps To Follow

- **Star** the repository.
- On the [GitHub page for this repository](https://github.com/gaurtvin/python-projects), click on the Button "**Fork**".
   ![fork image](https://help.github.com/assets/images/help/repository/fork_button.jpg)
- Create clone ***your forked repository*** on your local machine.
   ![code ui](https://docs.github.com/assets/images/help/repository/code-button.png)

    For example, run this command inside your terminal:

    ```bash
    git clone https://github.com/<your-github-username>/python-mini-projects.git
    ```

    **Replace \<your-github-username\>!**

    Learn more about [forking](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) and [cloning a repo](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).
- Before you make any changes, [keep your fork in sync](https://www.freecodecamp.org/news/how-to-sync-your-fork-with-the-original-git-repository/) to avoid merge conflicts:

    ```bash
    git remote add upstream https://github.com/gaurtvin/python-projects.git
    git fetch upstream
    git pull upstream master
    git push
    ```

- If you run into a **merge conflict**, you have to resolve the conflict. There are a lot of guides online, or you can try this one by [opensource.com](https://opensource.com/article/20/4/git-merge-conflict).

- Checkout to development branch (*name your branch according to the issue name*).

    ```bash
    git checkout -b <branch-name>
    ```

- Create a folder in
  [projects directory](https://github.com/gaurtvin/python-projects/tree/master/projects)
  according to issue name.
- Write your code and add to the respective folder in the projects directory, locally.
- Don't forget to add a `README.md` in your folder.
- Add the changes with `git add`, `git commit` ([write a good commit message](https://chris.beams.io/posts/git-commit/), if possible):

    ```bash
    git add -A
    git commit -m "<your message>"
    ```

- Push the code *to your repository*.

    ```bash
    git push origin <branch-name>
    ```

- Go to the GitHub page of _your fork_, and **make a pull request**:

    ![pull request image](https://help.github.com/assets/images/help/pull_requests/choose-base-and-compare-branches.png)

    Read more about pull requests on the [GitHub help pages](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
- Now wait, until one of us *reviews your Pull Request*! If there are any conflicts, you will get a notification.

## Other Rules

- Any contribution is welcomed such as fixing grammatical errors, fixing broken links, fixing bugs, etc.
- Before contributing, here's our [Code of Conduct](./Code-Of-Conduct.md) which must be adhered to.
- Verify that any project(s) to be added isn't already present in the repository, as yours may be a duplicate.
