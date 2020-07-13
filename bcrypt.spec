#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : bcrypt
Version  : 3.1.7
Release  : 57
URL      : https://files.pythonhosted.org/packages/fa/aa/025a3ab62469b5167bc397837c9ffc486c42a97ef12ceaa6699d8f5a5416/bcrypt-3.1.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/fa/aa/025a3ab62469b5167bc397837c9ffc486c42a97ef12ceaa6699d8f5a5416/bcrypt-3.1.7.tar.gz
Source1  : https://files.pythonhosted.org/packages/fa/aa/025a3ab62469b5167bc397837c9ffc486c42a97ef12ceaa6699d8f5a5416/bcrypt-3.1.7.tar.gz.asc
Summary  : Modern password hashing for your software and your servers
Group    : Development/Tools
License  : Apache-2.0
Requires: bcrypt-license = %{version}-%{release}
Requires: bcrypt-python = %{version}-%{release}
Requires: bcrypt-python3 = %{version}-%{release}
Requires: cffi
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
bcrypt
======

.. image:: https://img.shields.io/pypi/v/bcrypt.svg
    :target: https://pypi.org/project/bcrypt/
    :alt: Latest Version

.. image:: https://travis-ci.org/pyca/bcrypt.svg?branch=master
    :target: https://travis-ci.org/pyca/bcrypt

.. image:: https://dev.azure.com/pyca/bcrypt/_apis/build/status/bcrypt-CI?branchName=master
    :target: https://dev.azure.com/pyca/bcrypt/_build/latest?definitionId=8&branchName=master

Good password hashing for your software and your servers


Installation
============

To install bcrypt, simply:

.. code:: bash

    $ pip install bcrypt

Note that bcrypt should build very easily on Linux provided you have a C compiler, headers for Python (if you're not using pypy), and headers for the libffi libraries available on your system.

For Debian and Ubuntu, the following command will ensure that the required dependencies are installed:

.. code:: bash

    $ sudo apt-get install build-essential libffi-dev python-dev

For Fedora and RHEL-derivatives, the following command will ensure that the required dependencies are installed:

.. code:: bash

    $ sudo yum install gcc libffi-devel python-devel

Alternatives
============

While bcrypt remains a good choice for password storage depending on your specific use case you may also want to consider using scrypt (either via `standard library`_ or `cryptography`_) or argon2id via `argon2_cffi`_.

Changelog
=========

3.1.7
-----

* Set a ``setuptools`` lower bound for PEP517 wheel building.
* We no longer distribute 32-bit ``manylinux1`` wheels. Continuing to produce
  them was a maintenance burden.

3.1.6
-----

* Added support for compilation on Haiku.

3.1.5
-----

* Added support for compilation on AIX.
* Dropped Python 2.6 and 3.3 support.
* Switched to using ``abi3`` wheels for Python 3. If you are not getting a
  wheel on a compatible platform please upgrade your ``pip`` version.

3.1.4
-----

* Fixed compilation with mingw and on illumos.

3.1.3
-----
* Fixed a compilation issue on Solaris.
* Added a warning when using too few rounds with ``kdf``.

3.1.2
-----
* Fixed a compile issue affecting big endian platforms.
* Fixed invalid escape sequence warnings on Python 3.6.
* Fixed building in non-UTF8 environments on Python 2.

3.1.1
-----
* Resolved a ``UserWarning`` when used with ``cffi`` 1.8.3.

3.1.0
-----
* Added support for ``checkpw``, a convenience method for verifying a password.
* Ensure that you get a ``$2y$`` hash when you input a ``$2y$`` salt.
* Fixed a regression where ``$2a`` hashes were vulnerable to a wraparound bug.
* Fixed compilation under Alpine Linux.

3.0.0
-----
* Switched the C backend to code obtained from the OpenBSD project rather than
  openwall.
* Added support for ``bcrypt_pbkdf`` via the ``kdf`` function.

2.0.0
-----
* Added support for an adjustible prefix when calling ``gensalt``.
* Switched to CFFI 1.0+

Usage
-----

Password Hashing
~~~~~~~~~~~~~~~~

Hashing and then later checking that a password matches the previous hashed
password is very simple:

.. code:: pycon

    >>> import bcrypt
    >>> password = b"super secret password"
    >>> # Hash a password for the first time, with a randomly-generated salt
    >>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    >>> # Check that an unhashed password matches one that has previously been
    >>> # hashed
    >>> if bcrypt.checkpw(password, hashed):
    ...     print("It Matches!")
    ... else:
    ...     print("It Does not Match :(")

KDF
~~~

As of 3.0.0 ``bcrypt`` now offers a ``kdf`` function which does ``bcrypt_pbkdf``.
This KDF is used in OpenSSH's newer encrypted private key format.

.. code:: pycon

    >>> import bcrypt
    >>> key = bcrypt.kdf(
    ...     password=b'password',
    ...     salt=b'salt',
    ...     desired_key_bytes=32,
    ...     rounds=100)


Adjustable Work Factor
~~~~~~~~~~~~~~~~~~~~~~
One of bcrypt's features is an adjustable logarithmic work factor. To adjust
the work factor merely pass the desired number of rounds to
``bcrypt.gensalt(rounds=12)`` which defaults to 12):

.. code:: pycon

    >>> import bcrypt
    >>> password = b"super secret password"
    >>> # Hash a password for the first time, with a certain number of rounds
    >>> hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
    >>> # Check that a unhashed password matches one that has previously been
    >>> #   hashed
    >>> if bcrypt.checkpw(password, hashed):
    ...     print("It Matches!")
    ... else:
    ...     print("It Does not Match :(")


Adjustable Prefix
~~~~~~~~~~~~~~~~~

Another one of bcrypt's features is an adjustable prefix to let you define what
libraries you'll remain compatible with. To adjust this, pass either ``2a`` or
``2b`` (the default) to ``bcrypt.gensalt(prefix=b"2b")`` as a bytes object.

As of 3.0.0 the ``$2y$`` prefix is still supported in ``hashpw`` but deprecated.

Maximum Password Length
~~~~~~~~~~~~~~~~~~~~~~~

The bcrypt algorithm only handles passwords up to 72 characters, any characters
beyond that are ignored. To work around this, a common approach is to hash a
password with a cryptographic hash (such as ``sha256``) and then base64
encode it to prevent NULL byte problems before hashing the result with
``bcrypt``:

.. code:: pycon

    >>> password = b"an incredibly long password" * 10
    >>> hashed = bcrypt.hashpw(
    ...     base64.b64encode(hashlib.sha256(password).digest()),
    ...     bcrypt.gensalt()
    ... )

Compatibility
-------------

This library should be compatible with py-bcrypt and it will run on Python
2.7, 3.4+, and PyPy 2.6+.

C Code
------

This library uses code from OpenBSD.

Security
--------

``bcrypt`` follows the `same security policy as cryptography`_, if you
identify a vulnerability, we ask you to contact us privately.

.. _`same security policy as cryptography`: https://cryptography.io/en/latest/security/
.. _`standard library`: https://docs.python.org/3/library/hashlib.html#hashlib.scrypt
.. _`argon2_cffi`: https://argon2-cffi.readthedocs.io
.. _`cryptography`: https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/#cryptography.hazmat.primitives.kdf.scrypt.Scrypt

%package license
Summary: license components for the bcrypt package.
Group: Default

%description license
license components for the bcrypt package.


%package python
Summary: python components for the bcrypt package.
Group: Default
Requires: bcrypt-python3 = %{version}-%{release}

%description python
python components for the bcrypt package.


%package python3
Summary: python3 components for the bcrypt package.
Group: Default
Requires: python3-core
Provides: pypi(bcrypt)

%description python3
python3 components for the bcrypt package.


%prep
%setup -q -n bcrypt-3.1.7
cd %{_builddir}/bcrypt-3.1.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582850014
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bcrypt
cp %{_builddir}/bcrypt-3.1.7/LICENSE %{buildroot}/usr/share/package-licenses/bcrypt/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bcrypt/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
