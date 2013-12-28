This is a very simple script to automatically get historical weather
information.

All you have to do is run it with a start date and it will fetch the data and
write it out to stdout (one day per line). For example:

`python weather_history.py 2013-12-01`

will print all data from December 1st 2013 until today.  You can also provide an end date:

`python weather_history.py 2013-12-01 2013-12-07`


The format is `date,mean_temperature`. The date is YYYY-MM-DD and the
temperature is in Celsius.
