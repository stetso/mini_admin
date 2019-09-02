# Mini Admin User Management Example

This is a small example application that allows the creation and viewing of users. The application consists of a backend written in Python with [Flask](https://palletsprojects.com/p/flask/) and a SPA-frontend written in [Svelte v3](https://svelte.dev). 

## Installation and usage



## Development

Developing the application requires a few dependencies:

- NodeJS and NPM
- Python 3.5+ and PIP
- setting up a virtualenv is probably a good idea

Start by cloning the repository and navigating to the folder. All development packages are part of the Node ecosystem so install them with `npm install`.

Within your virtualenv you can install the Python development dependencies with `pip install -r requirements.txt`.

Start the development Flask server with `npm run backend:dev`. To work on the frontend start the development server for the Svelte app in a separate process: `npm run frontend:dev`. If you encounter errors you may need to check the permissions of the running user, the process needs to be able to write to the home directory of the current user (the database is stored in `~/.mini_admin/admin.db`).
 
Navigate to `localhost:5000/admin` to see the administration interface. Changes to the code are automatically recompiled but a page reload is necessary as the files are served by Flask.

[Tailwind CSS](https://tailwindcss.com) is used to style the interface and changes are made to the `main.css` file by `@apply`ing Tailwind styles and aggregating them to a class (check their [docs](https://tailwindcss.com/docs/extracting-components) for details).