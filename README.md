# Employees salary calculation

## Application

The application calculates the total salary for all given employees, considering the salaried, hourly and volunteer types.

### How it works

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
* `Accountant` works as a wrapper of `Staff` since doesn't need to have more logic, but it represents a realworld role that may evolve.

#### Applied patterns

* `Staff` and `Employee` applies **Composite pattern**


## Tests

You'll need `mock` and `nose` library:
```
pip install -r requirements.txt
```

Then execute nosetests to run all them:
```
nosetests
```

## Aspectes not taken into account

* If an employee changes his contract, in the real world the time of the month that was in the previous type of contract should be taken into account to calculate its salary
* The card could have have state with a `paid` attribute
* A card could register more info about how hours have been tracked. Here is simplified.

## Other considerations

* The calculator logic could be inside the contract classes and would be also funcional. It has been separated in another class since I've consider the `Contract` classes as model data.