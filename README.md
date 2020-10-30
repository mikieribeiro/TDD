### Test Driven Development

Read TDDPresentation.pdf for a brife introduction to Test Driven Developement

### Requirements
```
$ pip install PyYAML
```

### Exercise
```
1 - Hello world string test, based on --> https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/
    Create a simple test for the method hello_world() -> str that expects the string "hello world" to be returned
    
    Expected: "hello world"
```
```
2 - Find order:
    Create a simple test for the method get_order() -> str that reads the file Mock_dump, extracts the order1 value and returns it as a string.
    
    Expected: "3,12,3,6,8,8,13,9,8,10,11,11,12,13,14"
```
```
3 - Validate order :
    Create a simple test for the method is_order_valid(order: str) -> bool that receives an order as an argument and validates that its size is exactly 15 and       that each of its individual values is between 0 and 14
    Note: after validating the order gotten from the previous exercise, mock a new one called Order2 and give it values that are higher than 14 so you can also       test and invalid order.
    
    Expected: True (order1)|
    Expected: False (order2)|
```  

### Notes

    Mock all expected results on a config.yaml file and read them into the test class



