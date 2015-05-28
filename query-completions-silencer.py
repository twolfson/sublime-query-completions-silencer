# Load in our dependencies
import sublime

# Define constant to know when to continue looping silencing
initial_delay = 5 * 1000  # 5 seconds
loop_delay = 60 * 1000  # 1 minute
settings = {
    'silencing': False
}


# Set up our hooks
def plugin_loaded():
    """On module load, start silencing completions"""
    # Wait for a few other plugins to load, then run our cleaner
    # DEV: We must use an object, otherwise the local variable wouldn't reach our module one
    settings['silencing'] = True
    sublime.set_timeout(silence_query_completions, initial_delay)


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
    print('silence2')
    sublime.set_timeout(silence_query_completions, loop_delay)
