# NDJSON Logging | Twuni

Standalone logger for emitting NDJSON-formatted logs.

Part of the Twuni [Twelve-Factor App][12factor] suite for Python apps.

## Installing

To install directly:

```sh
pip install --index https://releases.twuni.dev/python/packages twuni_logging_ndjson
```

Alternatively, you can create a file with the following contents:

```
--index https://releases.twuni.dev/python/packages
twuni_logging_ndjson
```

...and install via that as a [requirements file][requirements.txt] using `pip install -r <file>`.

## Usage

For full documentation, see the [API Reference][docs].

Here's some example usage with comments:

```python
from twuni_logging_ndjson import Logger

logger = Logger(level="DEBUG")
# by setting the level to DEBUG (lowest priority), all log levels are emitted

logger.debug("example")
# prints {"event":{"type":"example"},"level":"DEBUG","timestamp":"<ISO-8601 timestamp>"} to standard output

logger.info("hello", {"message": "Hello, world!"})
# prints {"event":{"context":{"message":"Hello, world!"},"type":"hello"},"level":"INFO","timestamp":"<ISO-8601 timestamp>"} to standard output

# other logging levels are: warning, error, critical
```

[12factor]: https://12factor.net
[requirements.txt]: https://pip.pypa.io/en/stable/reference/requirements-file-format/
[docs]: https://releases.twuni.dev/python/packages/twuni-logging-ndjson/0.1.0/
