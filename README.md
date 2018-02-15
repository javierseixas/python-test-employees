# Employees salary calculation

## Application

The application calculates the total salary for all given employees, considering the salaried, hourly and volunteer types.

### Given employees

```
* 2 salaried employees with 3000 and 5000 fees (8000)
* 1 volunteer (0)
* 1 hourly employee with 150 fee per hour, and 10 hours (1500)
* 1 hourly employee with 200 fee per hour, and 20 hours (4000)
```

The expected total amount is 13500 fees.

Run `python app.py` to get the result printed.


### Design explanations

* `app.py` is the orchestrator for the calculation
* Each employee has its own logic to calculate the salary
    * The hourly employee has a more complex way to calculate its salary. Despite that, I don't think the class requires another class to calculate it.
* Each file has a test, except `card.py` that has no logic at all.
* There is the `employee.py` which accomplish the role of interface.

## Tests

You'll need nose to run all tests:
```
sudo pip install nose
```

Then execute nosetests to run all them:
```
nosetests
```
