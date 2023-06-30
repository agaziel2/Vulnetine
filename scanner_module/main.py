```python
from scanner_module.scanner import scanner
from scanner_module.scenarios import scenarios

def main():
    for scenario in scenarios:
        scanner(scenario)

if __name__ == "__main__":
    main()
```