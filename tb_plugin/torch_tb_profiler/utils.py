# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# --------------------------------------------------------------------------
import logging

from . import consts


def get_logger():
    logger = logging.getLogger(consts.PLUGIN_NAME)
    logger.setLevel(logging.INFO)
    return logger


def is_chrome_trace_file(path):
    return path.endswith(consts.TRACE_GZIP_FILE_SUFFIX) or path.endswith(consts.TRACE_FILE_SUFFIX)
