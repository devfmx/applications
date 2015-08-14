# Applications Platform

Management platform for Dev.f applications.

###### Requirements to run locally.
1. Have all environment variables defined ``(ask developers for the values)``.
2. Have a Postgres database for local development.
3. Update your environment libraries using the ```requirements.txt```file.
4. Run ```./manage.py runserver``` and have fun.

###### Github rules.
1. This repo have 2 main branches and all new features will be coded in branches per feature [(link)](https://www.google.com)
:
   * **master** (Only production code, everything here **must be deployable**.)
   * **staging** (Only staging code).
2. Commit **atomic** changes, not massive.
3. Always add a descriptive message to your commits.
4. All code must pass through **staging** and be **tested** before reaching **master**.
5. Do not talk about fight club, and have fun.

###### Code rules.
1. **Do not add sensitive data to the code!**
2. If you add a are using a new library, update the ```requirements.txt``` file using ```pip freeze > requirements.txt``` (Remember, you must be working on a virtual environment, do not push all your computer libraries to the file)