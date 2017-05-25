#! /bin/env/python
# Operate config file
import configparser
from fuzzyweather.util.logger import log

config = configparser.RawConfigParser()
config.read('setting.ini')

if not config.has_section('credentials'):
    config.add_section('credentials')
    config.set('credentials', 'token', '')
    config.set('credentials', 'channel_id', '@')

if not config.has_section('configs'):
    config.add_section('configs')
    config.set('configs', 'MORNING_ALARM_TIME', '8')
    config.set('configs', 'EVENING_ALARM_TIME', '20')

with open('setting.ini', 'w') as setting:
    config.write(setting)
    setting.close()

TOKEN = config.get('credentials', 'token')
CHANNEL_ID = config.get('credentials', 'channel_id')

MORNING_ALARM_TIME = 8
EVENING_ALARM_TIME = 20
try:
    MORNING_ALARM_TIME = config.getint('configs', 'MORNING_ALARM_TIME')
    EVENING_ALARM_TIME = config.getint('configs', 'EVENING_ALARM_TIME')
except ValueError as e:
    log.warn("알람 타임이 비어있습니다!")
