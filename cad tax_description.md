Package: cadtax
Sub-packages: taxrates and objectprice

### Sub-package: objectprice

***Module: objectprice*** 

This module is responsible for creating the object in question for the user to buy and calculates and returns a statement about the object and the total price with tax.
This module has a class ODBCInterface which contains the following methods:

```__init__``` takes the object name, price, and province name (as its abbreviation) and stores it in an object assigned by the user.

```getprice``` takesthe information of the object and calls on our taxrates module to give a statement about the total price of the object.

***Module: calctax***

This module is responsible for calculating the tax of the object based on the province and price given for the object.

```__init__``` takes the object name, price, and province name (as its abbreviation).

```tax``` uses an if statement to apply the different amounts of tax to the price and create a new total price.

### Sub-Package: taxrates
This module presents the user with a dataframe of the tax rates in Canadian provinces:

***Module: taxrates***
This module contains the following methods to give the user tax information in Canada:

```taxrates``` takes a dataframe created by the package designer and presents it to the user.
