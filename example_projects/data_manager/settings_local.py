# This settings file is intended to be used as the second-half of a 
# SplitSetting as described on the django wiki. See:
# http://code.djangoproject.com/wiki/SplitSettings#Multiplesettingfilesimportingfromeachother
# It will be imported at the end of settings.py
# Here you should define your database and email connection settings, as well
# as any GeoDjango settings. You can also specify where media is located on
# your filesystem. Settings defined here will override those in settings.py.

# At the very least, ensure that production setups have their own SECRET_KEY
# that is kept hidden from public repositories.
# SECRET_KEY = '6c(kr8r%aqf#r8%arr=0py_7t9m)wgocwyp5g@!j7eb0erm(2+sdklj23'

# The following Google key is for localhost:
# GOOGLE_API_KEY = 'ABQIAAAAu2dobIiH7nisivwmaz2gDhT2yXp_ZAY8_ufC3CFXhHIE1NvwkxSLaQmJjJuOq03hTEjc-cNV8eegYg' 

# You'll want to specify any database connection info here:
DATABASE_NAME = 'data_manager'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'd0nkey'

MEDIA_URL = '/media/'
#MEDIA_ROOT = '/Users/jaredkibele/Documents/workspace/lingcod_trunk/media/'