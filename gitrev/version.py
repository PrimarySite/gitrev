# -*- coding: utf-8 -*-
import logging
import subprocess

# Django
from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger(__name__)


GIT_CMD = 'git describe --always --dirty'


def get_command():  # noqa: D103
    command = getattr(settings, "GITREV_CMD", None)
    if not command:
        raise ImproperlyConfigured("GITREV_CMD is not defined in your settings.")
    return command


def test_tokenize_command(command):
    expected = [
        'git',
        'describe',
        '--always',
        '--dirty'
        ]
    assert tokenize_command(command) == expected


def tokenize_command(cmd):
    tokens = [token.strip() for token in cmd.split(' ')]
    return tokens


def get_git_revision_string(command):  # noqa: D103
    tokens = tokenize_command(command)
    revision_string = subprocess.check_output(tokens).strip().decode("utf-8")  # nosec
    return revision_string


def get_git_revision():
    """Return the current git revision data as a named-tuple."""
    revision_string = get_git_revision_string()
    parts = revision_string.split('-')
    logger.debug('Got revision: `{0}`'.format(parts))
    return parts


@register.simple_tag
def git_revision():  # noqa: D103
    try:
        command = get_command()
    except ImproperlyConfigured:
        logger.exception("Unable to get command to execute.")
        return ""

    try:
        result = get_git_revision_string(command)
    except Exception:
        logger.exception("Unable to get_git_revision_string.")
        return ""

    return result
