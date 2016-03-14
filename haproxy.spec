#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : haproxy
Version  : 1.5.16
Release  : 5
URL      : http://www.haproxy.org/download/1.5/src/haproxy-1.5.16.tar.gz
Source0  : http://www.haproxy.org/download/1.5/src/haproxy-1.5.16.tar.gz
Summary  : HA-Proxy is a TCP/HTTP reverse proxy for high availability environments
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: haproxy-bin
Requires: haproxy-config
Requires: haproxy-doc
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
HA-Proxy is a TCP/HTTP reverse proxy which is particularly suited for high
availability environments. Indeed, it can:
- route HTTP requests depending on statically assigned cookies
- spread the load among several servers while assuring server persistence
  through the use of HTTP cookies
- switch to backup servers in the event a main one fails
- accept connections to special ports dedicated to service monitoring
- stop accepting connections without breaking existing ones
- add/modify/delete HTTP headers both ways
- block requests matching a particular pattern

It needs very little resource. Its event-driven architecture allows it to easily
handle thousands of simultaneous connections on hundreds of instances without
risking the system's stability.

%package bin
Summary: bin components for the haproxy package.
Group: Binaries
Requires: haproxy-config

%description bin
bin components for the haproxy package.


%package config
Summary: config components for the haproxy package.
Group: Default

%description config
config components for the haproxy package.


%package doc
Summary: doc components for the haproxy package.
Group: Documentation

%description doc
doc components for the haproxy package.


%prep
%setup -q -n haproxy-1.5.16

%build
make V=1  %{?_smp_mflags} TARGET=linux2628 USE_PCRE=1 USE_OPENSSL=1 USE_ZLIB=1

%install
rm -rf %{buildroot}
%make_install PREFIX=/usr SBINDIR=/usr/bin DOCDIR=/usr/share/doc/haproxy
## make_install_append content
for contrib in halog iprange systemd; do
make V=1 %{?_smp_mflags} -C contrib/$contrib SBINDIR=/usr/bin
done
for contrib in halog iprange; do
cp contrib/$contrib/$contrib %{buildroot}/usr/bin
done
install -d %{buildroot}/usr/lib/systemd/system
cp contrib/systemd/haproxy.service %{buildroot}/usr/lib/systemd/system
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/halog
/usr/bin/haproxy
/usr/bin/iprange

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/haproxy.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/haproxy/*
%doc /usr/share/man/man1/*
