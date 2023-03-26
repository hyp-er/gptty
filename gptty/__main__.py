
"""
gptty: context-preserving chatGPT CLI wrapper

"""

__name__ = "gptty"
__author__ = "Sig Janoska-Bedi"
__credits__ = ["Sig Janoska-Bedi"]
__version__ = "0.1.3"
__license__ = "MIT"
__maintainer__ = "Sig Janoska-Bedi"
__email__ = "signe@atreeus.com"

# general packages
import click

# app specific requirements
from gptty.config import get_config_data
from gptty.gptty import create_chat_room

# Define color codes
CYAN = "\033[1;36m"
RED = "\033[1;31m"
RESET = "\033[0m"
# borrowed version callback from https://click.palletsprojects.com/en/7.x/options/#callbacks-and-eager-options
def print_version(ctx, param, value, version=__version__):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'gptty version {version}')
    ctx.exit()

@click.group()
@click.option('--version', '-v', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True, help="Show app version.")
def main():
  pass

@click.command()
def chat():
  """
  Run the gptty chat client
  """


  title = r"""
                 _   _         
     ____  ____ | | | |        
    / __ `/ __ \| |_| |_ _   _ 
   / /_/ / /_/ /| __| __| | | |
   \__, / .___/ | |_| |_| |_| |
  /____/_/       \__|\__|\__, |
                          __/ |
                         |___/ 
  """

  # Print the text in cyan
  click.echo(f"{CYAN}{title}\nWelcome to gptty (v.{__version__}), a ChatGPT wrapper in your TTY.\nType :help in the chat interface if you need help getting started.{RESET}\n")
  
  # load the app configs
  configs = get_config_data()
  
  # create the output file if it doesn't exist
  with open (configs['output_file'], 'a'): pass
  
  # Run the main function
  create_chat_room(configs=configs)


main.add_command(chat)

if __name__ == "__main__":
    main()
