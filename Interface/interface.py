from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text

from Interface.Rich.gradientline import gradient_line
from Interface.Rich.ASCII import ASCII_art

console = Console()

def appBanner():

    line = gradient_line(120)

    logo = Text(
        """
__        __   _        ___      _
\ \      / /__| |__    / _ \  __| |_   _ ___ ___  ___ _   _
 \ \ /\ / / _ \ '_ \  | | | |/ _` | | | / __/ __|/ _ \ | | |
  \ V  V /  __/ |_) | | |_| | (_| | |_| \__ \__ \  __/ |_| |
   \_/\_/ \___|_.__/   \___/ \__,_|\__, |___/___/\___|\__, |
                                   |___/              |___/
        """,
        style="bright_white"
    )

   

    ascii_art = Panel(

        Text(ASCII_art, style="bright_yellow"),
        border_style="green"

    )

    banner = Group(line,
                    logo,
                    ascii_art,
                    line)

    console.print(banner)
    
def appInterface():


    console.print("""

    Selecione uma opção: 

    [dark_orange]1[/dark_orange]-[bright_white]Send Request[/bright_white]
    [dark_orange]2[/dark_orange]-[bright_white]History[/bright_white]
    [red3]0[/red3]-[bright_white]Exit[/bright_white]

    """)

