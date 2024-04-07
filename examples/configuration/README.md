# Configuration Management

Managing application configuration can be challenging and complex.

There are several methods available, including config files, environment variables, and configuration servers. However, these methods can have drawbacks, such as the need to run an additional server or writing extensive code to parse environment variables properly.

A practical solution is to leverage [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) to create a system-wide, flexible configuration while avoiding common pitfalls.

## The Solution

1. **Define Custom Config Classes**: Structure your configuration with custom classes.
2. **Override Defaults with Environment Variables**: Easily modify your configuration without changing your codebase by setting environment variables.

## Examples

- `config.py`: Contains an example configuration demonstrating how to set up and use `pydantic-settings`.
- `test_config.py`: Includes pytest test cases to ensure the configuration operates as expected.

## Getting Started

To use these examples:

```bash
# install requirements
pip install -r requirements.txt

# run tests
pytest
```
