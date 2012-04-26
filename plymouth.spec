# TODO
# - revisit subpackages
# - fix: Requires: /bin/bash
# - integrate with geninitrd
# - pldize recent update
Summary:	Graphical Boot Animation and Logger
Summary(pl.UTF-8):	Graficzna animacja i logowanie startu systemu
Name:		plymouth
Version:	0.8.4
Release:	1
License:	GPL v2+
Group:		Base
Source0:	http://www.freedesktop.org/software/plymouth/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	6f370cd69bd6d0c67657d243a99dc260
Source1:	%{name}-logo.png
# Source1-md5:	6b38a868585adfd3a96a4ad16973c1f8
Source2:	%{name}.tmpfiles
Source3:	charge.%{name}
Source4:	boot-duration
Source5:	%{name}-set-default-plugin
Source6:	%{name}-update-initrd
Patch0:		check_for_consoles.patch
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
Requires:	%{name}-graphics-libs = %{version}-%{release}
Requires(post):	%{name}-scripts = %{version}-%{release}
Obsoletes:	plymouth-gdm-hooks
Obsoletes:	plymouth-utils
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
Requires:	%{name}-graphics-libs = %{version}-%{release}

%description devel
This package contains the header files for libply and libplybootsplash
libraries needed to develop 3rd party splash plugins for Plymouth.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe bibliotek libply i
libplybootsplash, potrzebne do tworzenia wtyczek graficznych Plymouth.

%package system-theme
Summary:	Plymouth default theme
Group:		Base
Requires:	%{name}(system-theme) = %{version}-%{release}
Provides:	%{name}-system-plugin = %{version}-%{release}
Obsoletes:	plymouth-system-plugin < %{version}-%{release}
Obsoletes:	rhgb < 1:10.0.0

%description system-theme
This metapackage tracks the current distribution default theme.

%package core-libs
Summary:	Plymouth core libraries
Group:		Development/Libraries
Conflicts:	%{name}-libs < 0.8.4-0.20120319.1

%description core-libs
This package contains the libply and libply-splash-core libraries used
by Plymouth.

%package graphics-libs
Summary:	Plymouth graphics libraries
Group:		Development/Libraries
Requires:	%{name}-core-libs = %{version}-%{release}
Provides:	%{name}-graphics-libs = %{version}-%{release}
Obsoletes:	plymouth-libs < %{version}-%{release}
Conflicts:	%{name}-libs < 0.8.4-0.20120319.1

%description graphics-libs
This package contains the libply-splash-graphics library used by
graphical Plymouth splashes.

%package scripts
Summary:	Plymouth related scripts
Summary(pl.UTF-8):	Skrypty pomocnicze do Plymouth
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	coreutils
Requires:	cpio
#Requires:	dracut
Requires:	findutils
Requires:	gzip

%description scripts
This package contains scripts that help integrate Plymouth with the
system.

%description scripts -l pl.UTF-8
Ten pakiet zawiera skrypty pomagające zintegrować Plymouth z systemem.

%package plugin-label
Summary:	Plymouth label plugin
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}

%description plugin-label
This package contains the label control plugin for Plymouth. It
provides the ability to render text on graphical boot splashes using
pango and cairo.

%package plugin-fade-throbber
Summary:	Plymouth "Fade-Throbber" plugin
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}

%description plugin-fade-throbber
This package contains the "Fade-In" boot splash plugin for Plymouth.
It features a centered image that fades in and out while other images
pulsate around during system boot up.

%package theme-fade-in
Summary:	Plymouth "Fade-In" theme
Group:		Base
Requires:	%{name}-plugin-fade-throbber = %{version}-%{release}
Requires(post):	%{name}-scripts = %{version}-%{release}
Obsoletes:	plymouth-plugin-fade-in

%description theme-fade-in
This package contains the "Fade-In" boot splash theme for Plymouth. It
features a centered logo that fades in and out while stars twinkle
around the logo during system boot up.

%package plugin-throbgress
Summary:	Plymouth "Throbgress" plugin
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}
Requires:	%{name}-plugin-label = %{version}-%{release}

%description plugin-throbgress
This package contains the "throbgress" boot splash plugin for
Plymouth. It features a centered logo and animated spinner that spins
repeatedly while a progress bar advances at the bottom of the screen.

%package theme-spinfinity
Summary:	Plymouth "Spinfinity" theme
Group:		Base
Requires:	%{name}-plugin-throbgress = %{version}-%{release}
Requires(post):	%{name}-scripts = %{version}-%{release}
Obsoletes:	plymouth-plugin-spinfinity

%description theme-spinfinity
This package contains the "Spinfinity" boot splash theme for Plymouth.
It features a centered logo and animated spinner that spins in the
shape of an infinity sign.

%package plugin-space-flares
Summary:	Plymouth "space-flares" plugin
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}
Requires:	%{name}-plugin-label = %{version}-%{release}

%description plugin-space-flares
This package contains the "space-flares" boot splash plugin for
Plymouth. It features a corner image with animated flares.

%package theme-solar
Summary:	Plymouth "Solar" theme
Group:		Base
Requires:	%{name}-plugin-space-flares = %{version}-%{release}
Requires(post):	%{name}-scripts = %{version}-%{release}
Obsoletes:	plymouth-plugin-solar

%description theme-solar
This package contains the "Solar" boot splash theme for Plymouth. It
features a blue flamed sun with animated solar flares.

%package plugin-two-step
Summary:	Plymouth "two-step" plugin
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}
Requires:	%{name}-plugin-label = %{version}-%{release}

%description plugin-two-step
This package contains the "two-step" boot splash plugin for Plymouth.
It features a two phased boot process that starts with a progressing
animation synced to boot time and finishes with a short, fast one-shot
animation.

%package theme-charge
Summary:	Plymouth "Charge" plugin
Group:		Base
Requires:	%{name}-plugin-two-step = %{version}-%{release}
Requires(post):	%{name}-scripts = %{version}-%{release}
Provides:	%{name}(system-theme) = %{version}-%{release}

%description theme-charge
This package contains the "charge" boot splash theme for Plymouth. It
features the shadowy hull of a Fedora logo charge up and and finally
burst into full form.

%package plugin-script
Summary:	Plymouth "script" plugin
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}

%description plugin-script
This package contains the "script" boot splash plugin for Plymouth. It
features an extensible, scriptable boot splash language that
simplifies the process of designing custom boot splash themes.

%package theme-script
Summary:	Plymouth "Script" plugin
Group:		Base
Requires:	%{name}-plugin-script = %{version}-%{release}
Requires(post):	%{_sbindir}/plymouth-set-default-theme

%description theme-script
This package contains the "script" boot splash theme for Plymouth. It
it is a simple example theme the uses the "script" plugin.

%package theme-spinner
Summary:	Plymouth "Spinner" theme
Group:		Base
Requires:	%{name}-plugin-two-step = %{version}-%{release}
Requires(post):	%{name}-scripts = %{version}-%{release}

%description theme-spinner
This package contains the "spinner" boot splash theme for Plymouth. It
features a small spinner on a dark background.

%prep
%setup -q
%patch0 -p1

# Change the default theme
sed -i -e 's/fade-in/charge/g' src/plymouthd.defaults

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
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{systemdtmpfilesdir}}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/plymouth/default-boot-duration
> $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth/boot-duration

# FC: Add charge, our new default
install -d $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
cp $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/glow/{box,bullet,entry,lock}.png $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge

# FC: Glow isn't quite ready for primetime
rm -rf $RPM_BUILD_ROOT%{_datadir}/plymouth/glow
rm -f $RPM_BUILD_ROOT%{_libdir}/plymouth/glow.so
# FC: Drop glow, it's not very Fedora-y
rm -rf $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/glow

# FC: Override plymouth-update-initrd to work dracut or mkinitrd
cp -p %{SOURCE6} $RPM_BUILD_ROOT%{_libdir}/plymouth/plymouth-update-initrd

# FC: Add compat script for upgrades
install -p %{SOURCE5} $RPM_BUILD_ROOT%{_sbindir}

%{__rm} $RPM_BUILD_ROOT{%{plymouth_libdir},%{_libdir}}/*.la \
	$RPM_BUILD_ROOT%{_libdir}/plymouth/*.la \
	$RPM_BUILD_ROOT%{_libdir}/plymouth/renderers/*.la

# Temporary symlink until rc.sysinit is fixed
ln -sf /bin/plymouth $RPM_BUILD_ROOT%{_bindir}/plymouth

install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/plymouth-logo.png
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%postun
if [ $1 -eq 0 ]; then
	rm -f %{_libdir}/plymouth/default.so
fi

%post	core-libs -p /sbin/ldconfig
%postun	core-libs -p /sbin/ldconfig
%post	graphics-libs -p /sbin/ldconfig
%postun	graphics-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/rhgb-client
%dir %{_sysconfdir}/plymouth
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/plymouth/plymouthd.conf
%{_mandir}/man8/plymouth.8*
%dir %{_datadir}/plymouth
%dir %{_datadir}/plymouth/themes
%dir %{_datadir}/plymouth/themes/details
%dir %{_datadir}/plymouth/themes/text
%{_datadir}/plymouth/plymouthd.defaults
%{_datadir}/plymouth/default-boot-duration
%dir %{_libdir}/plymouth
%dir %{_libdir}/plymouth/renderers
%dir %{_localstatedir}/lib/plymouth
%attr(755,root,root) %{plymouthdaemon_execdir}/plymouthd
%attr(755,root,root) %{plymouthclient_execdir}/plymouth
%attr(755,root,root) %{_bindir}/plymouth
%attr(755,root,root) %{_libdir}/plymouth/details.so
%attr(755,root,root) %{_libdir}/plymouth/text.so
%attr(755,root,root) %{_libdir}/plymouth/renderers/drm.so
%attr(755,root,root) %{_libdir}/plymouth/renderers/frame-buffer.so
%{_datadir}/plymouth/themes/details/details.plymouth
%{_datadir}/plymouth/themes/text/text.plymouth
%{systemdtmpfilesdir}/%{name}.conf
%{_localstatedir}/run/plymouth
%{_localstatedir}/spool/plymouth
%{_pixmapsdir}/plymouth-logo.png
%ghost %{_localstatedir}/lib/plymouth/boot-duration

%files core-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{plymouth_libdir}/libply.so.*.*.*
%attr(755,root,root) %ghost %{plymouth_libdir}/libply.so.2
%attr(755,root,root) %{plymouth_libdir}/libply-splash-core.so.*.*.*
%attr(755,root,root) %ghost %{plymouth_libdir}/libply-splash-core.so.2
%attr(755,root,root) %{_libdir}/libply-boot-client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libply-boot-client.so.2
%dir %{_libdir}/plymouth

%files graphics-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libply-splash-graphics.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libply-splash-graphics.so.2

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
%attr(755,root,root) %{_sbindir}/plymouth-set-default-plugin
%attr(755,root,root) %{_sbindir}/plymouth-set-default-theme
%attr(755,root,root) %{_libdir}/plymouth/plymouth-generate-initrd
%attr(755,root,root) %{_libdir}/plymouth/plymouth-populate-initrd
%attr(755,root,root) %{_libdir}/plymouth/plymouth-update-initrd

%files plugin-label
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/label.so

%files plugin-fade-throbber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/fade-throbber.so

%files theme-fade-in
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/fade-in
%{_datadir}/plymouth/themes/fade-in/bullet.png
%{_datadir}/plymouth/themes/fade-in/entry.png
%{_datadir}/plymouth/themes/fade-in/lock.png
%{_datadir}/plymouth/themes/fade-in/star.png
%{_datadir}/plymouth/themes/fade-in/fade-in.plymouth

%files theme-spinner
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/spinner
%{_datadir}/plymouth/themes/spinner/*.png
%{_datadir}/plymouth/themes/spinner/spinner.plymouth

%files plugin-throbgress
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/throbgress.so

%files theme-spinfinity
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/spinfinity
%{_datadir}/plymouth/themes/spinfinity/box.png
%{_datadir}/plymouth/themes/spinfinity/bullet.png
%{_datadir}/plymouth/themes/spinfinity/entry.png
%{_datadir}/plymouth/themes/spinfinity/lock.png
%{_datadir}/plymouth/themes/spinfinity/throbber-[0-3][0-9].png
%{_datadir}/plymouth/themes/spinfinity/spinfinity.plymouth

%files plugin-space-flares
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/space-flares.so

%files theme-solar
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/solar
%{_datadir}/plymouth/themes/solar/*.png
%{_datadir}/plymouth/themes/solar/solar.plymouth

%files plugin-two-step
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/two-step.so

%files theme-charge
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/charge
%{_datadir}/plymouth/themes/charge/*.png
%{_datadir}/plymouth/themes/charge/charge.plymouth

%files plugin-script
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/script.so

%files theme-script
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/script
%{_datadir}/plymouth/themes/script/*.png
%{_datadir}/plymouth/themes/script/script.script
%{_datadir}/plymouth/themes/script/script.plymouth

%files system-theme
%defattr(644,root,root,755)
