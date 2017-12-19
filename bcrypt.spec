#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : bcrypt
Version  : 3.1.4
Release  : 26
URL      : http://pypi.debian.net/bcrypt/bcrypt-3.1.4.tar.gz
Source0  : http://pypi.debian.net/bcrypt/bcrypt-3.1.4.tar.gz
Source99 : http://pypi.debian.net/bcrypt/bcrypt-3.1.4.tar.gz.asc
Summary  : Modern password hashing for your software and your servers
Group    : Development/Tools
License  : Apache-2.0
Requires: bcrypt-legacypython
Requires: bcrypt-python3
Requires: bcrypt-python
Requires: cffi
Requires: pytest
Requires: six
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
======

%package legacypython
Summary: legacypython components for the bcrypt package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the bcrypt package.


%package python
Summary: python components for the bcrypt package.
Group: Default
Requires: bcrypt-legacypython
Requires: bcrypt-python3

%description python
python components for the bcrypt package.


%package python3
Summary: python3 components for the bcrypt package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bcrypt package.


%prep
%setup -q -n bcrypt-3.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507746318
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1507746318
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
