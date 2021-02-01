# Oddup Backend Assignment

## Overview

The supplied JSON file for this assignment has been placed here: `customers/fixtures/fixtures.json`. The file has been modified slightly in order for it to match the standard Django fixture format. The data contained within is used as seed data for this application.

This is a simple REST API built using Django REST Framework, with SQLite 3 as the database. As per the assignment statement, it can perform the following operations:
- Create a new customer entry in the database.
- Check the balance of a customer’s account.
- Update the balance of the customer’s account after a transaction.
- Delete a customer from the database.
- Store a new transaction in the database.

## Installation instructions (Linux/OSX):

It is assumed that **Docker** and **docker-compose** are installed on the machine.

The application is Dockerized and has been **built and tested** on Ubuntu 20.04. In order to run it, please use the following commands:
1. `docker-compose build`
2. `docker-compose up -d` [the `-d` flag can be used to run the app in background and is optional]

## Questions

The assignment called for the following questions, they are enlisted with answers:

- What technology did you choose for building the API, and why?
I chose Python as the language and Django REST Framework as the technology for the following reasons:
	- It supports rapid development with the backing of fully blown framework level features that offers standard features out of the box such as serialization, and validation
	- Django REST Framework also features a powerful ORM that helps speed up the overall development with easy model design and querying system
	- The customization offered by the framework is very straightforward and easy to implement and offers the chance for the developer only to focus on the logic and not on other nuances such as formatting and rendering a response.

- If you were to deploy this to production, how would you go about doing that?

	- First consideration would be to containerize the application (already done in this test as well using Docker), this would help in easier setup across any kind of environment and very convenient dependency management.
	- I'd use a CI/CD tool such as GitHub CI or Gitlab Runner that would perform CI for us and also deploy it to our server automatically upon pushing the code.
	- All the environment variables would need to be configured securely over the CI tool
	- On the server, I'd use `nginx` and `gunicorn/uwsgi` (they are commonly used with WSGI applications) to serve the application
	- I'd also apply SSL certificate for the website

- What potential issues would you need to be aware of for a project like this?

	- **Authentication and Authorization**: This aspect would be the first thing that we would need to keep in mind in order to prevent application misuse
	- **Security** - Data needs to be completely secure since it contains users' personal information
	- **Data Consistency** - Since we are working with transactions here, they should be atomic and consistent at bare minimum so that the project is less error prone
	- **Scalability**  - The architecture of the application should be laid such that it doesn't crumble under increased load

- How would you ensure stability and performance under increased load?

	- **Database Architecture** - The database architecture of the application should be built in such a way that optimal number of queries are made to get data.
	- **On-demand Scaling** - Many services offer on-demand up-scaling of the infrastructure in use. It can be leveraged in order to save costs. However, horizontal scaling would be more useful in an application like this since it may involve some computation when 
