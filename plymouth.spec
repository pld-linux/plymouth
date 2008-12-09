%define plymouthdaemon_execdir /sbin
%define plymouthclient_execdir /bin
%define plymouth_libdir /%{_lib}

Summary:	Graphical Boot Animation and Logger
Name:		plymouth
Version:	0.6.0
Release:	0.1
License:	GPL v2+
Group:		Base
Source0:	http://freedesktop.org/software/plymouth/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	e29e754e942e6fcaf5185772d18fd97e
URL:		http://freedesktop.org/software/plymouth/releases
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.21.0
Requires(post):	%{name}-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plymouth provides an attractive graphical boot animation in place of
the text messages that normally get shown. Text messages are instead
redirected to a log file for viewing after boot.

%package system-plugin
Summary:	Plymouth default plugin
Group:		Base
Requires:	plymouth(system-plugin) = %{version}-%{release}
Provides:	rhgb = 1:10.0.0
Obsoletes:	rhgb < 1:10.0.0

%description system-plugin
This metapackage tracks the current distribution default plugin.

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
Requires:	nash

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

%package plugin-label
Summary:	Plymouth label plugin
Group:		Base
Requires:	%{name}-libs = %{version}-%{release}

%description plugin-label
This package contains the label control plugin for Plymouth. It
provides the ability to render text on graphical boot splashes using
pango and cairo.

%package plugin-fade-in
Summary:	Plymouth "Fade-In" plugin
Group:		Base
Requires(post):	%{_sbindir}/plymouth-set-default-plugin
Requires:	%{name}-libs = %{version}-%{release}

%description plugin-fade-in
This package contains the "Fade-In" boot splash plugin for Plymouth.
It features a centered logo that fades in and out while stars twinkle
around the logo during system boot up.

%package plugin-pulser
Summary:	Plymouth "Pulser" plugin
Group:		Base
Requires(post):	%{_sbindir}/plymouth-set-default-plugin
Requires:	%{name}-libs = %{version}-%{release}

%description plugin-pulser
This package contains the "Pulser" boot splash plugin for Plymouth. It
features a pulsing text progress indicator centered in the screen
during system boot up.

%package plugin-spinfinity
Summary:	Plymouth "Spinfinity" plugin
Group:		Base
Requires(post):	%{_sbindir}/plymouth-set-default-plugin
Requires:	%{name}-libs = %{version}-%{release}
Requires:	plymouth-plugin-label

%description plugin-spinfinity
This package contains the "Spinfinity" boot splash plugin for
Plymouth. It features a centered logo and animated spinner that spins
in the shape of an infinity sign.

%package plugin-solar
Summary:	Plymouth "Solar" plugin
Group:		Base
Requires(post):	%{_sbindir}/plymouth-set-default-plugin
Requires:	%{name}-libs = %{version}-%{release}
Requires:	plymouth-plugin-label
Provides:	plymouth(system-plugin) = %{version}-%{release}

%description plugin-solar
This package contains the "Solar" boot splash plugin for Plymouth. It
features a blue flamed sun with animated solar flares.

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
	--without-default-plugin \
	--with-logo=%{_pixmapsdir}/system-logo-white.png \
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

%postun plugin-spinfinity
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-plugin)" == "spinfinity" ]; then
        %{_sbindir}/plymouth-set-default-plugin --reset
    fi
fi

%postun plugin-fade-in
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-plugin)" == "fade-in" ]; then
        %{_sbindir}/plymouth-set-default-plugin --reset
    fi
fi

%post plugin-solar
export LIB=%{_lib}
if [ $1 -eq 1 ]; then
    %{_sbindir}/plymouth-set-default-plugin solar
fi

%postun plugin-solar
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-plugin)" == "solar" ]; then
        %{_sbindir}/plymouth-set-default-plugin text
    fi
fi

%postun plugin-pulser
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-plugin)" == "pulser" ]; then
        %{_sbindir}/plymouth-set-default-plugin --reset
    fi
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%dir %{_datadir}/plymouth
%dir %{_libexecdir}/plymouth
%dir %{_localstatedir}/lib/plymouth
%{plymouthdaemon_execdir}/plymouthd
%{plymouthclient_execdir}/plymouth
%attr(755,root,root) %{_bindir}/plymouth
%attr(755,root,root) %{_bindir}/rhgb-client
%{_libdir}/plymouth/details.so
%{_libdir}/plymouth/text.so
%{_localstatedir}/run/plymouth
%{_localstatedir}/spool/plymouth
#%ghost %{_localstatedir}/lib/plymouth/boot-duration

%files devel
%defattr(644,root,root,755)
%{plymouth_libdir}/libply.so
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
%attr(755,root,root) %{_sbindir}/plymouth-set-default-plugin
%{_libexecdir}/plymouth/plymouth-update-initrd
%{_libexecdir}/plymouth/plymouth-populate-initrd

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plymouth-log-viewer

%files gdm-hooks
%defattr(644,root,root,755)
%{_datadir}/gdm/autostart/LoginWindow/plymouth-log-viewer.desktop

%files plugin-label
%defattr(644,root,root,755)
%{_libdir}/plymouth/label.so

%files plugin-fade-in
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/fade-in
%{_datadir}/plymouth/fade-in/bullet.png
%{_datadir}/plymouth/fade-in/entry.png
%{_datadir}/plymouth/fade-in/lock.png
%{_datadir}/plymouth/fade-in/star.png
%{_libdir}/plymouth/fade-in.so

%files plugin-pulser
%defattr(644,root,root,755)
%{_libdir}/plymouth/pulser.so

%files plugin-spinfinity
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/spinfinity
%{_datadir}/plymouth/spinfinity/box.png
%{_datadir}/plymouth/spinfinity/bullet.png
%{_datadir}/plymouth/spinfinity/entry.png
%{_datadir}/plymouth/spinfinity/lock.png
%{_datadir}/plymouth/spinfinity/throbber-[0-3][0-9].png
%{_libdir}/plymouth/spinfinity.so

%files plugin-solar
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/solar
%{_datadir}/plymouth/solar/*.png
%{_libdir}/plymouth/solar.so

%files system-plugin
%defattr(644,root,root,755)
