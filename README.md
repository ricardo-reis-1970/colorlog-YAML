# YAML Config for `colorlog`

This is a small example using [Sam Clements](https://borntyping.co.uk/)' excellent [`colorlog`](https://github.com/borntyping/python-colorlog), with a YAML config.

The ideas were:

1. to have a single logger for a broader application
: it is a module imported from both `main` and `app`
2. to have multiple loggers withy different configs
: the config is external
3. to eventually have some of the logs coloured

After a few attempts, I think I got it right. This is very likely incomplete and possibly not too good. Contributions are welcome.

## Installing

I did not spend time on a virtual environment and requirements. You will need:
- colorlog
- yaml
- logging
- os

This was tested with Python 3.9.

## Running

`python main.py` and `python app.py` will showcase the intended effect.

## Notes
This example might grow into something more ellaborate, including filters, `secondary_log_colors` and custom log levels. May the 🌈 be with you!

## License
This is FREE, as is `colorlog`.