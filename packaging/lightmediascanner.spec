Name:       lightmediascanner
Summary:    Light media scanner is a media indexer for embedded devices
Version:    0.4.5
Release:    2
Group:      Multimedia/Libraries
License:    LGPL-2.1
Source:	    %{name}-%{version}.tar.gz
Url:	    https://github.com/profusion/lightmediascanner
BuildRequires: sqlite-devel
BuildRequires: gettext-tools
BuildRequires: libmp4v2-devel
BuildRequires: libtheora-devel
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(libtzplatform-config)
Requires: libmp4v2
Requires: libtheora
Requires: libtzplatform-config

%define testbindir %{_builddir}/%{name}-%{version}

%description
Description: %{summary}

%package devel
Summary: LMS headers, static libraries, and documentation
Requires: %{name} = %{version}

%description devel
Headers, static libraries, and documentation for LMS

%package test
Summary: LMS test programs
Requires: %{name} = %{version}

%description test
LMS test programs

%prep
%setup -q -n %{name}-%{version}

%build

%autogen

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

# Temporarily install test binaries
mkdir -p %{buildroot}/%{_bindir}
libtool --mode=install install -m 0755 %{testbindir}/src/bin/test %{buildroot}/%{_bindir}/lms-test
libtool --mode=install install -m 0755 %{testbindir}/src/bin/list-parsers %{buildroot}/%{_bindir}/lms-list-parsers

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS README
%license COPYING
%{_libdir}/*.so.*
%{_libdir}/lightmediascanner/plugins/*
%{_prefix}/share/dbus-1/services/*.service

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files test
%defattr(-, root, root)
%{_bindir}/*
