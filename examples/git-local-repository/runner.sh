#! /bin/bash

# There's not a great way to add a git repository inside a git repository,
# so we'll create one in this script.

# initialize git, if needed
if [[ ! -d my/local/repo/.git ]]; then
  pushd my/local/repo
  git init
  git add -A
  git commit -m "initial commit"
  popd
fi

# now run snapcraft
snapcraft
