from core.router import Router, Route, CallBack

about_us = Route("About us", callback=CallBack("public.utils", "about_us"))
add_comment = Route("add_comment", callback=CallBack('file.models', 'create_comments'))
show_files = Route("show_files", callback=CallBack('file.models', 'show_file'))
delete_user = Route("delete_user", callback=CallBack("users.models", "delete_user"))
managers = Route('manager', callback=CallBack('users.models', 'log_in_manager'), children=(delete_user,))
add_files = Route("add_files", callback=CallBack('file.models', 'create_file'))
salesman = Route("salesman", children=(add_files,))
buy_files = Route("buy_files", callback=CallBack("users.models", "buy_files"))
normal_user = Route('normal user', callback=CallBack('users.models', 'log_in'), children=(show_files, buy_files))
login = Route("login", children=(normal_user, salesman, managers))
register = Route("register", callback=CallBack("users.models", "create_user"))
users = Route("users", children=(register, login))
main_menu = Route(
    "Main Menu",
    "Main menu description ...",
    children=(
        about_us,
        add_comment,
        show_files,
        users))

# main_menu =

router = Router("File Store Router", main_menu)
