# Nuxt + DRF + Nginx

Nuxt js + DRF Producttion/Development Deployment

# Technologies used

* Django Rest Framework
* Nuxt js
* Docker/Docker Compose
* Nginx
* Gunicorn

## Getting started

- Clone the repo:

  ```
  git clone https://github.com/pylvin/nuxt-drf-template
  ```

## Production

- First change DEBUG=True to `False` in `.env` file

> .env file https://github.com/pylvin/nuxt-drf-template/blob/master/back/.env

- Then just build

```bash
  docker-compose -f docker-compose.prod up --build -d
```

## Development

- First change DEBUG=False to `True` in `.env` file

> .env file https://github.com/pylvin/nuxt-drf-template/blob/master/back/.env

- Then just build

```bash
  docker-compose -f docker-compose.dev up --build -d
```

## Changelog

[Go to Github Releases](https://github.com/pylvin/nuxt-drf-template/releases)

## License

Copyright (c) 2021 Alvin Aliev. Released under
the [MIT License](https://github.com/pylvin/nuxt-drf-template/blob/master/LICENSE).

Made with &#x2764; by [Alvin](https://github.com/pylvin).
