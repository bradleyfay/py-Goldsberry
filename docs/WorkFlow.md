Work Flow
===

This is a proposed outline and description of the development of the `py-Goldsberry package`.

According to this [site](http://nvie.com/posts/a-successful-git-branching-model/), we should do all of our development in branches stemming from a `develop` branch. Once we have all of the features created and merged into the `develop` branch, we will merge that to the `master` and publish that package to PyPi.

To get started, it is necessary to clone the repository. Run the following command from the command line in a parent folder. *I think we both have permission to read and write so this should work. If not, you'll need to first fork it, then clone the fork you created. See [here](https://www.acquia.com/blog/getting-started-collaborative-development-git) for details.*

  git clone https://github.com/bradleyfay/py-Goldsberry.git
  cd py-Goldsberry

From here, you want to either checkout an existing branch to work on or create a new branch to work on depending on what your wanting to accomplish.

If you want to check out and work on an existing branch, run the following command:

  git checkout [branch-name]

If you want to create a new branch, run this command:

  git checkout -b [branch-name] develop
  git push origin [branch-name]

This last command creates a new branch based on the `develop` branch which, as stated earlier, will be the parent for all of our work and exist perpetually.
