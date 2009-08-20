%define plymouthdaemon_execdir /sbin
%define plymouthclient_execdir /bin
%define plymouth_libdir /%{_lib}

Summary:	Graphical Boot Animation and Logger
Name:		plymouth
Version:	0.7.0
Release:	0.1
License:	GPL v2+
Group:		Base
Source0:	http://freedesktop.org/software/plymouth/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	f0b305c05129f3fd70de6583ed9cb9a4
Source1:	%{name}-logo.png
# Source1-md5:	6b38a868585adfd3a96a4ad16973c1f8
URL:		http://freedesktop.org/software/plymouth/releases
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.21.0
BuildRequires:	pkgconfig
Requires(post):	%{name}-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plymouth provides an attractive graphical boot animation in place of
the text messages that normally get shown. Text messages are instead
redirected to a log file for viewing after boot.

%package libs
Summary:	Plymouth libraries
Group:		Development/Libraries

%description libs
This package contains the libply and libplybootsplash libraries used
by Plymouth.

%package devel
Summary:	Libraries and headers for writing Plymouth splash plugins
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
This package contains the libply and libplybootsplash libraries and
headers needed to develop 3rd party splash plugins for Plymouth.

%package utils
Summary:	Plymouth related utilities
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains utilities that integrate with Plymouth including
a boot log viewing application.

%package scripts
Summary:	Plymouth related scripts
Group:		Applications/System

%description scripts
This package contains scripts that help integrate Plymouth with the
system.

%package gdm-hooks
Summary:	Plymouth GDM integration
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	gdm >= 1:2.22.0
Requires:	plymouth-utils

%description gdm-hooks
This package contains support files for integrating Plymouth with GDM
Namely, it adds hooks to show boot messages at the login screen in the
event start-up services fail.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-tracing \
	--disable-tests \
	--without-boot-entry \
	--with-logo=%{_pixmapsdir}/plymouth-logo.png \
	--with-background-start-color-stop=0x0073B3 \
	--with-background-end-color-stop=0x00457E \
	--with-background-color=0x3391cd \
	--enable-gdm-transition \
	--with-system-root-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} \;
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} \;

# Temporary symlink until rc.sysinit is fixed
(cd $RPM_BUILD_ROOT%{_bindir}; ln -s ../../bin/plymouth)

install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install %SOURCE1 $RPM_BUILD_ROOT%{_pixmapsdir}/plymouth-logo.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -f %{_localstatedir}/lib/plymouth/boot-duration ] || cp -f %{_datadir}/plymouth/default-boot-duration %{_localstatedir}/lib/plymouth/boot-duration

%postun
if [ $1 -eq 0 ]; then
    rm -f %{_libdir}/plymouth/default.so
fi

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/rhgb-client
%attr(755,root,root) %{_sbindir}/plymouth-set-default-theme
%dir %{_datadir}/plymouth
%{_datadir}/plymouth/themes
%dir %{_libexecdir}/plymouth
%dir %{_localstatedir}/lib/plymouth
%attr(755,root,root) %{plymouthdaemon_execdir}/plymouthd
%attr(755,root,root) %{plymouthclient_execdir}/plymouth
%attr(755,root,root) %{_bindir}/plymouth
%{_libdir}/plymouth/details.so
%{_libdir}/plymouth/fade-throbber.so
%{_libdir}/plymouth/label.so
%{_libdir}/plymouth/script.so
%{_libdir}/plymouth/space-flares.so
%{_libdir}/plymouth/text.so
%{_libdir}/plymouth/throbgress.so
%{_libdir}/plymouth/two-step.so
%{_localstatedir}/run/plymouth
%{_localstatedir}/spool/plymouth
%{_pixmapsdir}/plymouth-logo.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{plymouth_libdir}/libply.so
%{_libdir}/libplybootsplash.so
%{_pkgconfigdir}/plymouth-1.pc
%{_includedir}/plymouth-1

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{plymouth_libdir}/libply.so.*
%attr(755,root,root) %{_libdir}/libplybootsplash.so.*
%dir %{_libdir}/plymouth

%files scripts
%defattr(644,root,root,755)
%{_libexecdir}/plymouth/plymouth-update-initrd
%{_libexecdir}/plymouth/plymouth-populate-initrd

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plymouth-log-viewer

%files gdm-hooks
%defattr(644,root,root,755)
%{_datadir}/gdm/autostart/LoginWindow/plymouth-log-viewer.desktop
