## Version 3.2.3

* Fixed issue with `WWW-Authenticate` header not being included in 401
  responses.

## Version 3.2.2

* Added missing method `get` on `Token` base class.

## Version 3.2.1

* Simplified some blacklist app code.
* Resolved possible race condition.

## Version 3.2

* Added ``TokenObtainSerializer.get_token`` method to facilitate customization
  of token claims.
* Added ``TokenVerifyView`` to allow verification of HMAC-signed tokens by API
  users who have no access to the signing key.
* Renamed ``AUTH_HEADER_TYPE`` setting to ``AUTH_HEADER_TYPES``.  This setting
  now contains either a single valid auth header type or a list or tuple of
  valid auth header types.  If authentication fails, and more than one string is
  present in this tuple or list, the first item in the list will be used to
  build the "WWW-Authenticate" header in the response.

## Version 3.1

* Moved handling of TokenError exceptions from inside of serializer `validate`
  methods into token view `post` methods.

## Version 3.0

* Added support for refresh token rotation via ``ROTATE_REFRESH_TOKENS`` and
  ``BLACKLIST_AFTER_ROTATION`` settings.  See README for details.
* Added `BlacklistMixin.blacklist` method to make it easier to blacklist tokens
  regardless of whether or not they are present in the outstanding token list.
* In token blacklist app, changed `OutstandingToken.jti` field to char field to
  better reflect JWT spec.
* Renamed `AUTH_TOKEN_CLASS` setting to `AUTH_TOKEN_CLASSES`.  This setting now
  specifies a list of token classes (or class paths) which are used to verify
  tokens which are submitted for authorization.  This will hopefully help
  anyone wishing to gradually migrate between using different token types.
* Removed support for extensible JWT backends.  We're just going to use PyJWT
  exclusively to simplify things.
* Added support for more crypto algorithms.  All HMAC and RSA variants from
  PyJWT now supported.
* Renamed `SECRET_KEY` setting to `SIGNING_KEY`.
* The renamed `SIGNING_KEY` setting now acts doubly as a symmetric
  signing/verification key for HMAC algorithms and as a private key for RSA
  algorithms.
* Added `VERIFYING_KEY` setting for use with RSA algorithms.
* Removed undocumented `TOKEN_BACKEND_CLASS` setting.

## Version 2.1

* Switched to using [PyJWT](https://github.com/jpadilla/pyjwt) as the
  underlying library for signing and verifying tokens.
