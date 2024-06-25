""" Calendar task manager """
from flet import flet,Page, Column, Row, Container, padding

def main(page:Page):
    

    #
    _main = Container(
        width = 290,
        height = 590,
        bgcolor = "black",
        padding = 8,
    )



    page.add(_main)
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.update()





if __name__ == "__main__": 
    flet.app(target=main)
