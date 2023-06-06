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
```
commute-housing
├─ .dockerignore
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ HEAD
│  ├─ config
│  ├─ description
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ main
│  │     └─ remotes
│  │        └─ origin
│  │           └─ main
│  ├─ objects
│  │  ├─ 03
│  │  │  └─ af09018e92f849058ee3e131bf9820a94b31d5
│  │  ├─ 06
│  │  │  └─ dedf8f148c8fcf9c83b93f6c0c11e029623d70
│  │  ├─ 0b
│  │  │  └─ 4331b362b98a4e5947c491612f95a3c2e56686
│  │  ├─ 0e
│  │  │  └─ 038b5d996bba3a461ec30f20f66075ba827689
│  │  ├─ 17
│  │  │  └─ 263a16aca49f10a60cfa97c36d2197a15455d2
│  │  ├─ 20
│  │  │  └─ b03aad5d4cdc68c657308f2e2f20ce09d60e4d
│  │  ├─ 27
│  │  │  └─ d00bc7e78401d189d0c031d36de19f3d5455da
│  │  ├─ 32
│  │  │  └─ 68cd7e7b039c62d5638e2b92f583843bb9f4bc
│  │  ├─ 37
│  │  │  └─ a9ac52f95bf12ef475f4928e32a3f0b62ccf28
│  │  ├─ 3c
│  │  │  └─ 9ccfbf3ddf19b8ad4041366508eae3e4f84eff
│  │  ├─ 3e
│  │  │  └─ dbe1e8a314e654896024921dcf9e9e3651afb2
│  │  ├─ 41
│  │  │  └─ 85d360e9a725a190ddfd9b8cce8aeb0df64cc3
│  │  ├─ 42
│  │  │  └─ 016d515cb6e46c7efe63abc22bc2115fd7c1f2
│  │  ├─ 49
│  │  │  └─ 313893cbdbb406712a57cdb08ef5ae64bdfd44
│  │  ├─ 54
│  │  │  └─ 09a2574401b10794ec18930138b5c32d0124be
│  │  ├─ 63
│  │  │  └─ 22b0d8fdcd6e9e81a0a23405f65d8236b257c7
│  │  ├─ 68
│  │  │  └─ bc17f9ff2104a9d7b6777058bb4c343ca72609
│  │  ├─ 69
│  │  │  └─ 548bbe4b55445e55926f972e65e071d4e6b3b2
│  │  ├─ 6c
│  │  │  ├─ 2b6bb6dc0364f80cdaae10bc48fe6a858e0ae3
│  │  │  └─ a51c5f43e260dff30303fe9914f918f2889329
│  │  ├─ 6d
│  │  │  └─ e7c07c51b1400e828326f1f536974133fe6ac2
│  │  ├─ 76
│  │  │  └─ 8c6e4160893f1fad8738ea3d0c94848a3c036c
│  │  ├─ 7b
│  │  │  └─ ecfea9c5dda7868eebb8b98268c8a9501fe036
│  │  ├─ 81
│  │  │  └─ 15ae60bc647249211ecbd4bbf6aa65478e9b5c
│  │  ├─ 84
│  │  │  └─ 5f17ef88423bad9836c29344fa4bd93248d3c9
│  │  ├─ 87
│  │  │  └─ 8d1a5d7f11b61358f43a3737d80e1b6a2c61fd
│  │  ├─ 89
│  │  │  └─ 5c0e06049457356294c8e59c97820f7abcc002
│  │  ├─ 8d
│  │  │  └─ 07584b3859a55acc805eb4a9dbd93775bd7944
│  │  ├─ 8e
│  │  │  └─ fa5ed71d49711b9eb206e346f0a8bf46c4ba79
│  │  ├─ 9a
│  │  │  └─ 83572ac1f5d3ca5580841251745c21d7c727a7
│  │  ├─ 9b
│  │  │  └─ 3533be88da9ef3e12bacedab8dd3462bb2dc7d
│  │  ├─ 9d
│  │  │  └─ 1dcfdaf1a6857c5f83dc27019c7600e1ffaff8
│  │  ├─ a2
│  │  │  └─ f915ac5743168990620edbe246dfd640397e17
│  │  ├─ a5
│  │  │  └─ 13de9b125256253f8c6392f2f9f4ba21b85cb3
│  │  ├─ a8
│  │  │  └─ 1b8da09429c0481d2013fee9df2271b3005554
│  │  ├─ a9
│  │  │  └─ 4cd90bddedf9c9346acaec47972349a32b028d
│  │  ├─ b7
│  │  │  └─ a80f598efbac3152c6e1f43a217874d3d0a1e1
│  │  ├─ bd
│  │  │  └─ 13676e33c7fd142193506609048d3b7deb24b9
│  │  ├─ c1
│  │  │  └─ b26a539358a19ffbf783cf96daf102522fb9e1
│  │  ├─ c6
│  │  │  └─ 59ed6efa09ae58ca9ad4e31f1c9e0baf16933a
│  │  ├─ d8
│  │  │  └─ 438492d30f1d31d46207616493e38b192f8604
│  │  ├─ d9
│  │  │  └─ 46e37efbb17d8aed7f2d113971aff4825c59f8
│  │  ├─ e6
│  │  │  └─ 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│  │  ├─ e7
│  │  │  └─ 441bfb815bc8687c6c95965312c719f9579b69
│  │  ├─ ed
│  │  │  └─ d381db33afda27dbac4658cac520ee67d8676e
│  │  ├─ f0
│  │  │  ├─ 26898e14d9495809066d11b57f29578073040d
│  │  │  └─ daf78509ba5c84944a26f850b7b54f2094c8cc
│  │  ├─ f9
│  │  │  └─ bd80c8d9ffbda83b8c0181e4773e7b6d5ed5a0
│  │  ├─ ff
│  │  │  └─ 1885994c299ec34d522141541f0d294248ec82
│  │  ├─ info
│  │  └─ pack
│  └─ refs
│     ├─ heads
│     │  └─ main
│     ├─ remotes
│     │  └─ origin
│     │     └─ main
│     └─ tags
├─ .github
│  └─ workflows
│     └─ checks.yml
├─ .gitignore
├─ Dockerfile
├─ README.md
├─ app
│  ├─ .flake8
│  ├─ app
│  │  ├─ __init__.py
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  └─ wsgi.py
│  ├─ core
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ management
│  │  │  ├─ __init__.py
│  │  │  └─ commands
│  │  │     ├─ __init__.py
│  │  │     └─ wait_for_db.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  └─ tests
│  │     ├─ test_commands.py
│  │     └─ test_models.py
│  └─ manage.py
├─ docker-compose.yml
├─ requirements.dev.txt
└─ requirements.txt

```