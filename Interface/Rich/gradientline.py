from rich.console import Console
from rich.text import Text
console = Console()


def gradient_line(length):

    if type(length) == int:

        cores = [

            "green1" ,
            "green3",            
            "green",
            "sea_green2",
            "chartreuse3",
            "chartreuse2",
            "green4" ,
            "dark_green" ,



        ]


        text = Text("="*length)

        for i in range(0, len(text.plain), 3):

            cor=cores[(i // 3) % len(cores)]
            text.stylize(cor, i, i+3)

        return text

        

        