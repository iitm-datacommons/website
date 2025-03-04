#!/bin/bash

# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -e

# export NODE_OPTIONS=--openssl-legacy-provider

function setup_python {
  python3 -m venv .env
  source .env/bin/activate
  pip install --upgrade pip
  pip3 install -r server/requirements.txt -q
}

# Run test for client side code.
function run_npm_test {
  cd static
  npm run test
  cd ..
}

# Tests if lint is required on client side code
function run_npm_lint_test {
  cd static
  npm list eslint || npm install eslint
  if ! npm run test-lint; then
    echo "Fix lint errors by running ./run_test.sh -f"
    exit 1
  fi
  cd ..
}

# Fixes lint
function run_lint_fix {
  echo -e "#### Fixing client-side code"
  cd static
  npm list eslint || npm install eslint
  npm run lint
  cd ..

  echo -e "#### Fixing Python code"
  python3 -m venv .env
  source .env/bin/activate
  if ! command -v yapf &> /dev/null
  then
    pip3 install yapf -q
  fi
  yapf -r -i -p --style=google server/ tools/ -e=*pb2.py
  deactivate
}

# Build client side code
function run_npm_build () {
  cd static
  if [[ $1 == true ]]
  then
    echo -e "#### Only installing production dependencies"
    npm install --only=prod
  else
    npm install
  fi
  npm run-script build
  cd ..
}

# Run test and check lint for Python code.
function run_py_test {
  setup_python
  cd server
  export FLASK_ENV=test
  python3 -m pytest tests/**.py -s --ignore=sustainability
  # TODO(beets): add tests for other private dc instances
  # export FLASK_ENV=test-sustainability
  # python3 -m pytest tests/sustainability/**.py
  cd ..
  echo -e "#### Checking Python style"
  if ! yapf --recursive --diff --style=google -p server/ tools/ -e=*pb2.py; then
    echo "Fix lint errors by running ./run_test.sh -f"
    exit 1
  fi
}

# Run test for webdriver automation test codes.
function run_webdriver_test {
  printf '\n\e[1;35m%-6s\e[m\n\n' "!!! Have you generated the prod client packages? Run './run_test.sh -b' first to do so"
  setup_python
  cd server
  if [ ! -d dist  ]
  then
    echo "no dist folder, please run ./run_test.sh -b to build js first."
    exit 1
  fi
  export FLASK_ENV=webdriver
  export GOOGLE_CLOUD_PROJECT=datcom-website-dev
  python3 -m pytest -n 10 webdriver_tests/tests/**.py
  cd ..
}

function run_all_tests {
  run_py_test
  run_npm_build
  run_webdriver_test
  run_npm_lint_test
  run_npm_test
}

function help {
  echo "Usage: $0 -pwblcsaf"
  echo "-p       Run server python tests"
  echo "-w       Run webdriver tests"
  echo "-o       Build for production (ignores dev dependencies)"
  echo "-b       Run client install and build"
  echo "-l       Run client lint test"
  echo "-c       Run client tests"
  echo "-a       Run all tests"
  echo "-f       Fix lint"
  exit 1
}

# Always reset the variable null.
while getopts tpwotblcsaf OPTION; do
  case $OPTION in
    p)
        echo -e "### Running server tests"
        run_py_test
        ;;
    w)
        echo -e "### Running webdriver tests"
        run_webdriver_test
        ;;
    o)
        echo -e "### Production flag enabled"
        PROD=true
        ;;
    b)
        echo -e "### Build client-side packages"
        run_npm_build $PROD
        ;;
    l)
        echo -e "### Running lint"
        run_npm_lint_test
        ;;
    c)
        echo -e "### Running client tests"
        run_npm_test
        ;;
    s)
        echo -e "### Running screenshot tests"
        run_screenshot_test
        ;;
    f)
        echo -e "### Fix lint errors"
        run_lint_fix
        ;;
    a)
        echo -e "### Running all tests"
        run_all_tests
        ;;
    *)
        help
    esac
done

if [ $OPTIND -eq 1 ]
then
  help
fi