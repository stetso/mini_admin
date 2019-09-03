# Mini Admin User Management Example

This is a small example application that allows the creation and viewing of users. The application consists of a backend written in Python with [Flask](https://palletsprojects.com/p/flask/) and a SPA-frontend written in [Svelte v3](https://svelte.dev). 

## Installation and usage

The application can be installed with `pip`. A Python version 3.5+ is recommended, although it may work with a lesser version (untested). If preferred create and activate a new [virtualenv](https://virtualenv.pypa.io/en/stable/) for the app.

Get the latest version from the [Releases page](https://github.com/stetso/mini_admin/releases) and unzip it at a location of you choice. A folder `mini_admin` is created. Now you can install the application using

```
pip install -e path/to/mini_admin
```

and afterwards start it from within your environment with

```
mini_admin run
```

You should see some logs that inform  you where the SQLite database has been created and instructions on how to access the admin interface. Then follow the instructions by navigating to `localhost:5000/admin` in your browser (it should be a reasonably recent browser, IE is probably not supported).

Here you can create users by filling in User information and see the details of all existing users in a list. 

### Uninstall

To uninstall the softwarte simply issue 

```
pip uninstall mini_admin
```

from within the environment where it was installed. Unfortunately, the database is currently not removed automatically, so you need to remove it by hand. It lives in the home folder in `~/.mini_admin/admin.db`.

## Todo and ideas

This is not a production ready system, rather a stub that shows one approach to designing a modular administration application. Svelte applications are very small so they are perfectly suitable for a dashboard-like, widget-heavy application where multiple widgets can be developed independently and get their data through a REST-like API. Here, only a single one is shown. Additionally, Tailwind CSS allows for a very easy and succint way to style the entire application consistently. It works quite well with the modular component-heavy SPA architecture although scoped styles are an alternative as well.

However, some things are missing and/or need to be improved:

- unit tests in back- and frontend - currently the application is relatively small but once it grows more complex, automated testing should be integrated
- better notification/messaging to the frontend about server-side errors
- a production web-server (currently the built-in development server from Flask is used)

## Development

Developing the application requires a few dependencies:

- NodeJS (a recent LTS version will do) and NPM
- Python 3.5+ and PIP
- setting up a [virtualenv](https://virtualenv.pypa.io/en/stable/) is probably a good idea

Start by cloning the repository and navigating to the folder. All development packages are part of the Node ecosystem so install them with `npm install`.

Within your virtualenv you can install the Python development dependencies with `pip install -r requirements.txt`.

Start the development Flask server with `npm run backend:dev`. To work on the frontend start the development server for the Svelte app in a separate process: `npm run frontend:dev`. If you encounter errors you may need to check the permissions of the running user, the process needs to be able to write to the home directory of the current user (the database is stored in `~/.mini_admin/admin.db`).
 
Navigate to `localhost:5000/admin` to see the administration interface. Changes to the code are automatically recompiled but a page reload is necessary as the files are served by Flask.

[Tailwind CSS](https://tailwindcss.com) is used to style the interface and changes are made to the `main.css` file by `@apply`ing Tailwind styles and aggregating them to a class (check their [docs](https://tailwindcss.com/docs/extracting-components) for details).