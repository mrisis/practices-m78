from core.router import Router, Route, CallBack

about_us = Route("About us", callback=CallBack("public.utils", "about_us"))
show_files = Route("show_files", callback=CallBack('file.models', 'show_file'))
# main_menu =

router = Router("File Store Router", Route(
    "Main Menu",
    "Main menu description ...",
    children=(
        about_us,
        show_files,

        Route("users",
              children=(Route("register",
                              callback=CallBack("users.models", "create_user")),
                        Route("login",
                              children=(Route('normal user',
                                              callback=CallBack('users.models', 'log_in'),
                                              children=(
                                                  Route("show files", callback=CallBack("file.models", "show_file"),
                                                        children=(Route("buy_files", callback=CallBack("users.models",
                                                                                                       "buy_files")),)),)),
                                        Route('salesman',
                                              callback=CallBack('users.models', 'log_in_salesman'),
                                              children=(
                                                  Route("add_files",
                                                        callback=CallBack('file.models', 'create_file')),)),

                                        Route('manager',
                                              callback=CallBack('users.models', 'log_in_manager')),
                                        )))

              )
    )))
