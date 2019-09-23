Summary: Single binary providing simplified versions of system commands
Name: busybox
Version:    1.31.0+git2
Release: 1
License: GPLv2
Source0: http://www.busybox.net/downloads/%{name}-%{version}.tar.bz2
#Source1: rpm/udhcpd.service
Source2: busybox.config
#Source2: busybox-static.config
#Source3: busybox-sailfish.config
#Patch0:  0001-Copy-extended-attributes-if-p-flag-is-provided-to-cp.patch
#Patch1:  0002-applets-Busybox-in-usr-bin-instead-of-bin.patch
URL: https://github.com/cxl000/busybox-mer
#BuildRequires: glibc-static
BuildRequires: libselinux-devel libsepol-devel
BuildRequires: pcre

Obsoletes: time <= 1.7
Provides: time > 1.7

# Providing only part of iputils, but should be enough for us. 
Obsoletes: iputils <= 20101006
Provides: iputils > 20101006

%define debug_package %{nil}

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Busybox user guide.

%prep
%setup -q -n %{name}-%{version}/upstream
#%patch0 -p1
#%patch1 -p1

%build
# TODO: This config should be synced with the dynamic config at some point
# currently the features differ quite a bit
cp %{SOURCE2} .config

yes "" | make oldconfig
make %{_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}/usr/bin
install -m 755 busybox %{buildroot}/usr/bin/busybox

mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 644 -t %{buildroot}/%{_docdir}/%{name}-%{version} \
        docs/BusyBox.html docs/BusyBox.txt

%files
%defattr(-,root,root,-)
%license LICENSE
/bin/busybox
%{_bindir}/busybox

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}

