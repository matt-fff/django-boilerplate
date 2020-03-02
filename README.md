# django-boilerplate
A baseline template for my Django experiments and examples.


#### Build Local Docker Environment
```bash
docker-compose build
```

#### Run Local Docker Environment
```bash
docker-compose up
```

#### Run Unit Tests
```bash
docker-compose run app python manage.py test
```

#### Run Specific Test
```bash
docker-compose run app python manage.py test app.tests.views.test_things
```

## Code Quality
### Run Black Formatting
The optional `--check` flag will make the formatter check if the code is already formatted.
```bash
docker-compose run app python manage.py black --check
```

### Run PyLint
```bash
docker-compose run app python manage.py pylint
```

### Run pycodestyle
```bash
docker-compose run app python manage.py pycodestyle
```

### Run All Checks
Runs all of the above commands.
```bash
docker-compose run app python manage.py quality
```

### Passing Filename/Directory
Our code quality commands support all the filename/directory params laid out below. 

#### A Complete Run
```bash
docker-compose run app python manage.py <whateverCommand>
```

#### By Filename
You can specify the filename (no path necessary) or regex for the file you want.

e.g. to run the command on all files containing "some" followed by "thing" in the name:
```bash
docker-compose run app python manage.py <whateverCommand> --filename *some*thing*
```

#### By Directory
You can specify the path for the file you want.

e.g. to run the command on all files in the "test/example" folder:
```bash
docker-compose run app python manage.py <whateverCommand> --directory test/example
```

#### By Combination
Both parameters work together.

e.g. to run the command on all files in "buzzwords" with "cloud" in the name:
```bash
docker-compose run app python manage.py <whateverCommand> --directory buzzwords --filename *cloud*
```
