# -*- coding: utf-8 -*-
import logging
import subprocess

logger = logging.getLogger(__name__)


GIT_CMD = 'git describe --always --tags --long --dirty'


def test_tokenize_command():
    expected = [
        'git',
        'describe',
        '--always',
        '--tags',
        '--long',
        '--dirty'
        ]
    assert tokenize_command(GIT_CMD) == expected


def tokenize_command(cmd):
    tokens = [token.strip() for token in cmd.split(' ')]
    return tokens


def get_git_revision_string():
    tokens = tokenize_command(GIT_CMD)
    revision_string = subprocess.check_output(tokens).strip().decode('utf-8')
    return revision_string


def get_git_revision():
    """Return the current git revision data as a named-tuple."""
    revision_string = get_git_revision_string()
    parts = revision_string.split('-')
    logger.debug('Got revision: `{0}`'.format(parts))
    return parts
