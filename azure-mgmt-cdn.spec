#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-mgmt-cdn
Version  : 4.0.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/fe/72/77100acae55cf1b20ad78d6650934d4df4a9a699e9d6e826d3ac82d294d5/azure-mgmt-cdn-4.0.0.zip
Source0  : https://files.pythonhosted.org/packages/fe/72/77100acae55cf1b20ad78d6650934d4df4a9a699e9d6e826d3ac82d294d5/azure-mgmt-cdn-4.0.0.zip
Summary  : Microsoft Azure CDN Management Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-mgmt-cdn-python = %{version}-%{release}
Requires: azure-mgmt-cdn-python3 = %{version}-%{release}
Requires: azure-common
Requires: msrest
Requires: msrestazure
BuildRequires : azure-common
BuildRequires : buildreq-distutils3
BuildRequires : msrest
BuildRequires : msrestazure

%description
==============================
        
        This is the Microsoft Azure CDN Management Client Library.
        
        Azure Resource Manager (ARM) is the next generation of management APIs that
        replace the old Azure Service Management (ASM).
        
        This package has been tested with Python 2.7, 3.5, 3.6 and 3.7.
        
        For the older Azure Service Management (ASM) libraries, see

%package python
Summary: python components for the azure-mgmt-cdn package.
Group: Default
Requires: azure-mgmt-cdn-python3 = %{version}-%{release}

%description python
python components for the azure-mgmt-cdn package.


%package python3
Summary: python3 components for the azure-mgmt-cdn package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_cdn)
Requires: pypi(azure_common)
Requires: pypi(msrest)
Requires: pypi(msrestazure)

%description python3
python3 components for the azure-mgmt-cdn package.


%prep
%setup -q -n azure-mgmt-cdn-4.0.0
cd %{_builddir}/azure-mgmt-cdn-4.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588788932
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3*/site-packages/azure/mgmt/__init__.py
rm -f %{buildroot}/usr/lib/python3*/site-packages/azure/mgmt/__pycache__/__init__.cpython-3*.pyc

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
