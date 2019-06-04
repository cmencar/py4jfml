# Py4JFML 1.0
A Python wrapper for [JFML](http://www.uco.es/JFML).

Py4JFML can be used in the same way of JFML (see [JFML documentation](http://www.uco.es/JFML/documentation)). To see how to use Py4JFML, have a look at the example files in the `testlib` folder.

## Installation
1. Download the file `py4jfml-1.0.tar.gz` from the `dist` folder
2. run 
	
	`$ pip3 install py4jfml-1.0.tar.gz`

If you want to test the library, you can extract the `testlib` folder from the archive and execute one of the contained scripts. For example:

`$ python3 CreateInvertedPendulumMamdaniExampleXML1.py` 
	
should carry out the follwing text (trunked):

```
FUZZY SYSTEM: invertedPendulum - MAMDANI
KNOWLEDGEBASE: 
  *Angle - domain[0.0, 255.0] - input
	very negative -  trapezoid [a: 0.0, b: 0.0, c: 48.0, d: 88.0]
	negative -  triangular [a: 48.0, b: 88.0, c: 128.0]
	zero -  triangular [a: 88.0, b: 128.0, c: 168.0]
	positive -  triangular [a: 128.0, b: 168.0, c: 208.0]
	very positive -  trapezoid [a: 168.0, b: 208.0, c: 255.0, d: 255.0]
	very negative or negative -  trapezoid [a: 0.0, b: 0.0, c: 88.0, d: 128.0]
	positive or very positive -  trapezoid [a: 128.0, b: 168.0, c: 255.0, d: 255.0]

(...)

RULEBASE:
  *mamdani - rulebase1: OR=MAX; AND=MIN; ACTIVATION=MIN
	RULE 1: rule1 - (0.0) IF Angle IS very negative or negative AND ChangeAngle IS very negative or negative THEN Force IS very negative [weight=1.0]
	RULE 2: rule2 - (0.0) IF Angle IS very negative AND ChangeAngle IS zero THEN Force IS very negative [weight=1.0]
	RULE 3: rule3 - (0.0) IF Angle IS very negative AND ChangeAngle IS positive THEN Force IS negative [weight=1.0]
	RULE 4: rule4 - (0.0) IF Angle IS very negative AND ChangeAngle IS very positive THEN Force IS zero [weight=1.0]
(...)
``` 

Also, the file `InvertedPendulumMamdani1.xml` should be generated and written in the current directory.

### Dependencies
Py4JFML depends on [`py4j`](https://www.py4j.org/), which is automatically downloaded and installed if necessary.

### Licence
Py4JFML is released under GPLv3 licence.

## Known issues
- Currently, `Py4JFML` does not implement the `compatibility` package of JFML. As a consequence, only the FML format is supported.
- In Windows, a `Py4JNetworkError` could arise when executing Py4JFML. This is a [known issue](https://github.com/bartdag/py4j/issues/200) of `py4j` and occurs when the library tries to shut down the py4j server before terminating. This problem does not affect the functionality of the library, but you may get a memory leakage due to the server still running after the program termination.

## Changelog
### 0.1 
First release
### 0.1.1
Installation documentation fix (pip)
### 1.0
First release. Interoperability experiment implemented.
