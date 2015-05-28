# Load in our dependencies
import sublime
import sublime_plugin

# Define constant to know when to continue looping silencing
loop_delay = 60 * 1000  # 1 minute
settings = {
    'silencing': False,
}


# Set up our hooks
def plugin_loaded():
    """On module load, start silencing completions"""
    # Run our cleaner immediately
    # DEV: We must use an object, otherwise the local variable wouldn't reach our module one
    settings['silencing'] = True
    silence_query_completions()


def plugin_unloaded():
    """On module unload, stop silencing completions"""
    settings['silencing'] = False


# Set up our logic
def silence_query_completions():
    """Silence on_query_completions via Sublime's internal API"""
    # If we are not silencing any more, then stop
    if settings['silencing'] is False:
        return

    # Otherwise, run our silencer and loop again
    # https://github.com/twolfson/sublime-files/blob/3083.0.0/sublime_plugin.py#L19-L22
    # https://github.com/twolfson/sublime-files/blob/3083.0.0/sublime_plugin.py#L352-L369
    sublime_plugin.on_query_completions = []
    sublime.set_timeout(silence_query_completions, loop_delay)
