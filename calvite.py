from datetime import datetime, date, time
from time import struct_time
import click


class Config(object):
    def __init__(self):
        self.calendar = None


pass_config = click.make_pass_decorator(Config, ensure=True)
date_formats = ['%Y-%m-%d', '%Y-%m-%d', '%Y%m%d', '%m%d', '%m-%d']
time_formats = ['%H:%M', '%H:%M:%S', '%H%M', '%H%M%S']


@click.group()
@pass_config
def cli(config):
    if config.calendar is None:
        # prompt user to connect to their calendar
        click.echo("Please connect your Google Calendar")


@cli.command()
@click.argument('start-date', type=click.DateTime(formats=date_formats), default=str(date.today()))
@click.argument('end-date', type=click.DateTime(formats=date_formats), default=str(date.today()), required=False)
@click.option('--start-time', type=click.DateTime(formats=time_formats), default=str(datetime.min.time()))
@click.option('--end-time', type=click.DateTime(formats=time_formats), default=str(datetime.min.time()))
@click.option('--between')
@pass_config
def event(config, start_date, end_date, start_time, end_time, between):
    """This creates a new Calendar event"""

    # If no user-specified year, change to this year instead of 1900
    start_date = start_date.replace(
        year=(date.today().year if start_date.year == 1900 else start_date.year))
    end_date = end_date.replace(
        year=(date.today().year if end_date.year == 1900 else end_date.year))

    # Make sure end is at least start
    end_date = max(end_date, start_date)
    end_time = max(end_time, start_time)

    # Stripping the datetimes, combining them
    start_date = start_date.date()
    end_date = end_date.date()
    start_time = start_time.time()
    end_time = end_time.time()
    start = datetime.combine(start_date, start_time)
    end = datetime.combine(end_date, end_time)

    click.echo(
        f"I'd like to create an event between {start_date} and {end_date} between {start_time} and {end_time}")
