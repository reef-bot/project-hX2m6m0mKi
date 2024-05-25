# settings.py

import os

# Discord bot settings
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = '!'
MOD_ROLE = 'Moderator'
LOG_CHANNEL = 'mod-logs'

# Filtering settings
FILTER_WORDS = ['bad_word1', 'bad_word2', 'bad_word3']

# Machine learning model settings
MODEL_PATH = 'models/machine_learning_model.pkl'

# Automated tasks settings
SCHEDULED_TASKS = {
    'task1': {
        'interval': 60,  # in seconds
        'action': 'mute',
        'target': 'user_id'
    },
    'task2': {
        'interval': 3600,  # in seconds
        'action': 'ban',
        'target': 'user_id'
    }
}