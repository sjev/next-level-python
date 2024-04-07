FROM python:3.12-slim-bullseye



COPY dist /dist

# install package
RUN pip install /dist/*.whl


# Command to run the server
CMD ["python", "-m", "{{ cookiecutter.package_name }}"]
