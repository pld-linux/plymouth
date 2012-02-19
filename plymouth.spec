# TODO
# - revisit subpackages
# - fix: Requires: /bin/bash
# - integrate with geninitrd
%define		snap	20120212
Summary:	Graphical Boot Animation and Logger
Summary(pl.UTF-8):	Graficzna animacja i logowanie startu systemu
Name:		plymouth
Version:	0.8.4
Release:	0.%{snap}.1
License:	GPL v2+
Group:		Base
#Source0:	http://www.freedesktop.org/software/plymouth/releases/%{name}-%{version}.%{snap}.tar.bz2
Source0:	%{name}-%{version}.%{snap}.tar.bz2
# Source0-md5:	6accf3a89fa9e5a99fbc4eb63909bcd5
Source1:	%{name}-logo.png
# Source1-md5:	6b38a868585adfd3a96a4ad16973c1f8
Source2:	%{name}.tmpfiles
URL:		http://www.freedesktop.org/wiki/Software/Plymouth
#BuildRequires:	autoconf >= 2.50
#BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	libdrm-devel
BuildRequires:	libpng-devel >= 1.2.16
#BuildRequires:	libtool >= 2:2.0
BuildRequires:	pango-devel >= 1:1.21.0
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires(post):	%{name}-scripts = %{version}-%{release}
Obsoletes:	plymouth-utils
Obsoletes:	plymouth-gdm-hooks
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plymouthdaemon_execdir	/sbin
%define		plymouthclient_execdir	/bin
%define		plymouth_libdir		/%{_lib}

%description
Plymouth provides an attractive graphical boot animation in place of
the text messages that normally get shown. Text messages are instead
redirected to a log file for viewing after boot.

%description -l pl.UTF-8
Plymouth zapewnia atrakcyjną animację w trakcie startu systemu zamiast
zwykle wyświetlanych komunikatów tekstowych. Komunikaty tekstowe
zamiast tego są przekierowywane do logu, który można obejrzeć po
uruchomieniu systemu.

%package libs
Summary:	Plymouth libraries
Summary(pl.UTF-8):	Biblioteki Plymouth
Group:		Libraries

%description libs
This package contains the libply and libplybootsplash libraries used
by Plymouth.

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki libply i libplybootsplash używane przez
Plymouth.

%package devel
Summary:	Header files for writing Plymouth splash plugins
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia wtyczek graficznych Plymouth
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the header files for libply and libplybootsplash
libraries needed to develop 3rd party splash plugins for Plymouth.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe bibliotek libply i
libplybootsplash, potrzebne do tworzenia wtyczek graficznych Plymouth.

%package scripts
Summary:	Plymouth related scripts
Summary(pl.UTF-8):	Skrypty pomocnicze do Plymouth
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description scripts
This package contains scripts that help integrate Plymouth with the
system.

%description scripts -l pl.UTF-8
Ten pakiet zawiera skrypty pomagające zintegrować Plymouth z systemem.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-tests \
	--enable-gdm-transition \
	--enable-systemd-integration \
	--enable-tracing \
	--with-background-start-color-stop=0x003194 \
	--with-background-end-color-stop=0x000063 \
	--with-background-color=0x0063c6 \
	--with-logo=%{_pixmapsdir}/plymouth-logo.png \
	--with-system-root-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/tmpfiles.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT{%{plymouth_libdir},%{_libdir}}/*.la \
	$RPM_BUILD_ROOT%{_libdir}/plymouth/*.la \
	$RPM_BUILD_ROOT%{_libdir}/plymouth/renderers/*.la

# Temporary symlink until rc.sysinit is fixed
ln -sf /bin/plymouth $RPM_BUILD_ROOT%{_bindir}/plymouth

install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/plymouth-logo.png
install %{SOURCE2} $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%postun
if [ $1 -eq 0 ]; then
	rm -f %{_libdir}/plymouth/default.so
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/rhgb-client
%attr(755,root,root) %{_sbindir}/plymouth-set-default-theme
%dir %{_sysconfdir}/plymouth
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/plymouth/plymouthd.conf
%{_mandir}/man8/plymouth.8*
%dir %{_datadir}/plymouth
%{_datadir}/plymouth/plymouthd.defaults
%{_datadir}/plymouth/themes
%dir %{_libexecdir}/plymouth
%dir %{_localstatedir}/lib/plymouth
%attr(755,root,root) %{plymouthdaemon_execdir}/plymouthd
%attr(755,root,root) %{plymouthclient_execdir}/plymouth
%attr(755,root,root) %{_bindir}/plymouth
%attr(755,root,root) %{_libdir}/plymouth/details.so
%attr(755,root,root) %{_libdir}/plymouth/fade-throbber.so
%attr(755,root,root) %{_libdir}/plymouth/label.so
%attr(755,root,root) %{_libdir}/plymouth/script.so
%attr(755,root,root) %{_libdir}/plymouth/space-flares.so
%attr(755,root,root) %{_libdir}/plymouth/text.so
%attr(755,root,root) %{_libdir}/plymouth/throbgress.so
%attr(755,root,root) %{_libdir}/plymouth/two-step.so
/usr/lib/tmpfiles.d/%{name}.conf
%{_localstatedir}/run/plymouth
%{_localstatedir}/spool/plymouth
%{_pixmapsdir}/plymouth-logo.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{plymouth_libdir}/libply.so.*.*.*
%attr(755,root,root) %ghost %{plymouth_libdir}/libply.so.2
%attr(755,root,root) %{plymouth_libdir}/libply-splash-core.so.*.*.*
%attr(755,root,root) %ghost %{plymouth_libdir}/libply-splash-core.so.2
%attr(755,root,root) %{_libdir}/libply-boot-client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libply-boot-client.so.2
%attr(755,root,root) %{_libdir}/libply-splash-graphics.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libply-splash-graphics.so.2
%dir %{_libdir}/plymouth
%dir %{_libdir}/plymouth/renderers
%attr(755,root,root) %{_libdir}/plymouth/renderers/drm.so
%attr(755,root,root) %{_libdir}/plymouth/renderers/frame-buffer.so
%attr(755,root,root) %{_libdir}/plymouth/renderers/x11.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{plymouth_libdir}/libply.so
%attr(755,root,root) %{plymouth_libdir}/libply-splash-core.so
%attr(755,root,root) %{_libdir}/libply-boot-client.so
%attr(755,root,root) %{_libdir}/libply-splash-graphics.so
%{_includedir}/plymouth-1
%{_pkgconfigdir}/ply-boot-client.pc
%{_pkgconfigdir}/ply-splash-core.pc
%{_pkgconfigdir}/ply-splash-graphics.pc

%files scripts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/plymouth/plymouth-generate-initrd
%attr(755,root,root) %{_libexecdir}/plymouth/plymouth-populate-initrd
%attr(755,root,root) %{_libexecdir}/plymouth/plymouth-update-initrd
