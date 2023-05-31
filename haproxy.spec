#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
Name     : haproxy
Version  : 2.0.31
Release  : 55
URL      : https://www.haproxy.org/download/2.0/src/haproxy-2.0.31.tar.gz
Source0  : https://www.haproxy.org/download/2.0/src/haproxy-2.0.31.tar.gz
Source1  : haproxy.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: haproxy-bin = %{version}-%{release}
Requires: haproxy-license = %{version}-%{release}
Requires: haproxy-man = %{version}-%{release}
Requires: haproxy-services = %{version}-%{release}
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : systemd-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The HAProxy documentation has been split into a number of different files for
ease of use.

%package bin
Summary: bin components for the haproxy package.
Group: Binaries
Requires: haproxy-license = %{version}-%{release}
Requires: haproxy-services = %{version}-%{release}

%description bin
bin components for the haproxy package.


%package doc
Summary: doc components for the haproxy package.
Group: Documentation
Requires: haproxy-man = %{version}-%{release}

%description doc
doc components for the haproxy package.


%package license
Summary: license components for the haproxy package.
Group: Default

%description license
license components for the haproxy package.


%package man
Summary: man components for the haproxy package.
Group: Default

%description man
man components for the haproxy package.


%package services
Summary: services components for the haproxy package.
Group: Systemd services
Requires: systemd

%description services
services components for the haproxy package.


%prep
%setup -q -n haproxy-2.0.31
cd %{_builddir}/haproxy-2.0.31
pushd ..
cp -a haproxy-2.0.31 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685551376
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}  TARGET=linux-glibc USE_PCRE=1 USE_OPENSSL=1 USE_ZLIB=1 USE_SYSTEMD=1

pushd ../buildavx2
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
make  %{?_smp_mflags}  TARGET=linux-glibc USE_PCRE=1 USE_OPENSSL=1 USE_ZLIB=1 USE_SYSTEMD=1
popd

%install
export SOURCE_DATE_EPOCH=1685551376
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/haproxy
cp %{_builddir}/haproxy-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/haproxy/99ea8073325ff4a755b6f2fa5862fc3e722f4647 || :
cp %{_builddir}/haproxy-%{version}/doc/gpl.txt %{buildroot}/usr/share/package-licenses/haproxy/9a13113b89f7985efe22a28b8e4ad1ace7f2b5d1 || :
cp %{_builddir}/haproxy-%{version}/ebtree/LICENSE %{buildroot}/usr/share/package-licenses/haproxy/caeb68c46fa36651acf592771d09de7937926bb3 || :
pushd ../buildavx2/
%make_install_v3 PREFIX=/usr SBINDIR=/usr/bin DOCDIR=/usr/share/doc/haproxy
popd
%make_install PREFIX=/usr SBINDIR=/usr/bin DOCDIR=/usr/share/doc/haproxy
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/haproxy.service
## install_append content
for contrib in halog iprange systemd; do
make V=1 %{?_smp_mflags} -C contrib/$contrib SBINDIR=/usr/bin
done

for contrib in halog iprange; do
cp contrib/$contrib/$contrib %{buildroot}/usr/bin
done

install -d %{buildroot}/usr/lib/systemd/system
cp contrib/systemd/haproxy.service %{buildroot}/usr/lib/systemd/system
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/haproxy
/usr/bin/halog
/usr/bin/haproxy
/usr/bin/iprange

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/haproxy/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/haproxy/99ea8073325ff4a755b6f2fa5862fc3e722f4647
/usr/share/package-licenses/haproxy/9a13113b89f7985efe22a28b8e4ad1ace7f2b5d1
/usr/share/package-licenses/haproxy/caeb68c46fa36651acf592771d09de7937926bb3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/haproxy.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/haproxy.service
