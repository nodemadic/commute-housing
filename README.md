Leverage real estate and transportation data to create a service that provides a tool for people looking for housing based on commute times to a given address:

TODO:

1. Setup development environment: Setup Django, Docker, and Swagger in local environment. Django will be used for building the API, Docker for containerization, and Swagger for documenting API.

2. Design Django models: Models to include `User`, `Property`, `Commute`, etc.

3. Access Zillow's public data: Zillow provides public APIs that can be used to fetch real estate data. Serivce needs to fetch this data and store it in database. Normalize the data and store it in a structured format that aligns with Django models.

4. Access Boston's Muni service data: Fetch transportation data from Boston's Muni service. Use this data to compute commute times from each property to the given destination.

5. Create an API endpoint for the user's search: When a user inputs their destination and other search parameters, service should fetch relevant properties from database and compute commute times from each property to the given destination using the transportation data. This computation can be done in the backend.

6. Present the results: Service should return the list of properties, sorted by commute time, to the user. Include other relevant details about the property and the commute in the response.

7. Implement Docker: Dockerize application. This will ensure that application can run in any environment with Docker installed.

8. Document API with Swagger: Make your API more professional and easier to use.

10. Deploy your application: Deploy application to a public server so that others can use it using AWS for deployment.