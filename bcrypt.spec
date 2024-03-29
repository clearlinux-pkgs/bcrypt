#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : bcrypt
Version  : 3.2.0
Release  : 75
URL      : https://files.pythonhosted.org/packages/d8/ba/21c475ead997ee21502d30f76fd93ad8d5858d19a3fad7cd153de698c4dd/bcrypt-3.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d8/ba/21c475ead997ee21502d30f76fd93ad8d5858d19a3fad7cd153de698c4dd/bcrypt-3.2.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/d8/ba/21c475ead997ee21502d30f76fd93ad8d5858d19a3fad7cd153de698c4dd/bcrypt-3.2.0.tar.gz.asc
Summary  : Modern password hashing for your software and your servers
Group    : Development/Tools
License  : Apache-2.0
Requires: bcrypt-license = %{version}-%{release}
Requires: bcrypt-python = %{version}-%{release}
Requires: bcrypt-python3 = %{version}-%{release}
Requires: cffi
Requires: mypy
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : mypy
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
======

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
Requires: pypi(cffi)
Requires: pypi(six)

%description python3
python3 components for the bcrypt package.


%prep
%setup -q -n bcrypt-3.2.0
cd %{_builddir}/bcrypt-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635706555
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
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
cp %{_builddir}/bcrypt-3.2.0/LICENSE %{buildroot}/usr/share/package-licenses/bcrypt/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c
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
