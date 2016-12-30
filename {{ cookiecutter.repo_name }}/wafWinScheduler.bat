@pushd \\{{ server }}\{{ fileshare }}$\
@cd {{ cookiecutter.github_username }}\{{ cookiecutter.project_slug }}
@python -x "%~dp0waf" configure build %* & exit /b
