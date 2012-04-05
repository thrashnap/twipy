# twipy

A Python library for accessing the Twitter API. It is designed to be extensible and comprehensive. It closely resembles the way twitter 
has grouped their methods.

## Requirements

	Python Version >= 2.5, No support for 3 yet

## Examples

Basic usage:
	from twipy import Twipy
    twipy = Twipy()
    home_timeline = twipy.timelines.home_timeline(count=20, since_id=18700887835, include_entities='true')