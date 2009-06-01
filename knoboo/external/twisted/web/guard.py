# Copyright (c) 2001-2008 Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Resource traversal integration with L{twisted.cred} to allow for
authentication and authorization of HTTP requests.
"""

# Expose HTTP authentication classes here.
from knoboo.external.twisted.web._auth.wrapper import HTTPAuthSessionWrapper
from knoboo.external.twisted.web._auth.basic import BasicCredentialFactory
from knoboo.external.twisted.web._auth.digest import DigestCredentialFactory

__all__ = [
    HTTPAuthSessionWrapper.__name__,

    BasicCredentialFactory.__name__, DigestCredentialFactory.__name__]