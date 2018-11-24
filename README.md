# Colorizer
Easily print colored text.

## Examples
```python
>>> from colorizer import Colorizer
>>> from colors import RED, GREEN
>>> c = Colorizer()
>>> c.print('{hello} {world!}', RED, GREEN)
```
Prints: <span style='color:red'>hello</span> <span style='color:green'>world!</span> 

## Disclaimer
Colorizer may not work on certain systems (e.g., Windows) or with certain terminals.

## Dependencies
Colorizer is built on top of colorama : https://github.com/tartley/colorama

## Future plans
* Generate code in colors.py with a script instead of at runtime
    * Allow code completion
    * Remove annoying error messages
* Add support for reusing colors by index, e.g. c.print('{0:oh} {1:hai} {0:there}', colors.RED, colors.BLACK)
