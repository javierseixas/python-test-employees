# Employees salary calculation

## Application

The application calculates the total salary for all given employees, considering the fixed, hourly and volunteer types.

```
python app.py
```

You can also run it using a flag to simulate a contract change.

```
python app.py -c
```


### How it works

```
* 2 fixed employees with 3000 and 5000 fees (8000)
* 1 volunteer (0)
* 1 hourly employee with 150 fee per hour, and 10 hours (1500)
* 1 hourly employee with 200 fee per hour, and 20 hours (4000)
```

The expected total amount is **13500** fees.

Run the program to get the total printed.

#### Change of contract simulation

Using the flag `-c` it is simulated that one hourly employee changes its contract to fixed with `2500` of salary.

In that case, the expected fees will be **16000**.

In *[Aspects not taken into account](#aspects-not-taken-into-account)* section it is explained the limitation of the system.


### Design explanations

* `app.py` is the orchestrator for the calculation
* The logic to calculate the salary is in the calculator, where **Composition** is applied.
    * It case of changing the way of calculate salaries, only is needed to change the `calculator` accordingly.
* `Accountant` works as a wrapper of `Staff` since it doesn't need to have more logic, but it represents a realworld role that may evolve.

#### Applied patterns

* `Staff` and `Employee` applies **Composite pattern**
* `VoluntaryCalculater` applies **Null-Object pattern**
* In `App` there is the private method to create Employees. It applies the **Factory Method pattern**

## Tests

You'll need `mock` and `nose` library:
```
pip install -r requirements.txt
```

Then execute nosetests to run all them:
```
nosetests
```

## Aspects not taken into account

* If an employee changes his contract, in the real world the time of the month that was in the previous type of contract should be taken considering dates. Here I'm not considering dates neither proportional pays.
* The card could have have state with a `paid` attribute
* A card could register more info about how hours have been tracked. Here is simplified.

## Other considerations

* The calculator logic could be inside the contract classes and would be also functional. It has been separated in another class since I've consider the `Contract` classes as model data.
* Classes like `Accountant` or `Employee` doesn't have test because they don't have enough logic to need a test. This is my opinion about optimizing test maintenance.
* `Employee` has the method `obtain_salary` for different reasons:
    * For using the Composite pattern with staff
    * Because the accountant cannot calculate (or at least I don't know the way) the salary of all employees without `if` conditional for checking employees types.
