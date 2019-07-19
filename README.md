# xyfny - a z-machine intepreter

This is based closely upon theinternetftw's `xyppy`.

Where that is geared towards an interactive simulation of a good ol'-fashioned Z-machine
experience, this is intended to be plugging into event-driven systems (for instance,
chat systems like Slack).

All of the terminal handling is stripped out. Rather, the z-machine runs until it attempts
to read input from the user. At that point, it'll exit with an interrupt - _unless_ there
is user input pending in its buffer.

The basic gist of how this might be used:

    # Initialise
    env = make_env(file)
    intro = do_step(env, line)
    
    # Output the introductory text to the user
    output(intro)
    
    # On receiving an input event from the user:
    response = do_step(env, event_text)
    output(response)
    
### References

- [xyppy - infocom's z-machine in python](https://github.com/theinternetftw/xyppy)
