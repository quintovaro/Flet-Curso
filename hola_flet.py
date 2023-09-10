import flet as ft


def main(page: ft.Page):
    page.add(ft.Text("¡Hola mundo Flet!"))


# Ejecutar en escritorio
# ft.app(main)

# Ejecutar en navegador
ft.app(main, view=ft.WEB_BROWSER)