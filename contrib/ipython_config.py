# Configuration file for ipython.
c = get_config()

# Whether to display a banner upon starting IPython.
c.TerminalIPythonApp.display_banner = False

# Remove those annoying newlines between each input
c.TerminalInteractiveShell.separate_in = ''

# Set to confirm when you try to exit IPython with an EOF (Control-D in Unix)
c.TerminalInteractiveShell.confirm_exit = False

# Enable auto setting the terminal title.
c.TerminalInteractiveShell.term_title = True

# Output prompt.
c.PromptManager.out_template = '--> '

# Bring back the classic Python REPL prompt.
c.PromptManager.in_template = '>>> '

# Continuation prompt.
c.PromptManager.in2_template = '... '

# Activate greedy completion
# This will enable completion on elements of lists, results of function calls,
# etc., but can be unsafe because the code is actually evaluated on TAB.
c.IPCompleter.greedy = True