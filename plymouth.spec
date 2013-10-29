# TODO
# - integrate with geninitrd
# - pldize recent update (r1.18)
# - verify if systemd services have to be installed for targets,
#	and remove the symlinks if not
#
# Conditional build:
%bcond_without	drm_intel	# disable building with libdrm_intel support
%bcond_without	drm_radeon	# disable building with libdrm_radeon support
%bcond_with	drm_nouveau	# enable building with libdrm_nouveau support
%bcond_without	kms		# disable building with libkms support

Summary:	Graphical Boot Animation and Logger
Summary(pl.UTF-8):	Graficzna animacja i logowanie startu systemu
Name:		plymouth
Version:	0.8.8
Release:	4
License:	GPL v2+
Group:		Base
Source0:	http://www.freedesktop.org/software/plymouth/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	38f5e613e5ab17806b950cee2d0d0d4e
Source1:	%{name}-logo.png
# Source1-md5:	6b38a868585adfd3a96a4ad16973c1f8
Source2:	%{name}.tmpfiles
Source3:	charge.%{name}
Source4:	boot-duration
Source5:	%{name}-set-default-plugin
Source6:	%{name}-update-initrd
Source7:	systemd-ask-password-plymouth.path
Source8:	systemd-ask-password-plymouth.service
Patch0:		text-colors.patch
Patch1:		path-udevadm.patch
URL:		http://www.freedesktop.org/wiki/Software/Plymouth
BuildRequires:	cairo-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
%if %{with drm_intel} ||  %{with drm_radeon} ||  %{with drm_nouveau} ||  %{with kms}
BuildRequires:	libdrm-devel
%endif
BuildRequires:	libpng-devel >= 2:1.2.16
BuildRequires:	pango-devel >= 1:1.21.0
BuildRequires:	pkgconfig
Requires:	%{name}-graphics-libs = %{version}-%{release}
Requires(post):	%{name}-scripts = %{version}-%{release}
Requires:	/etc/os-release
Requires:	systemd-units
Obsoletes:	plymouth-gdm-hooks
Obsoletes:	plymouth-utils
Obsoletes:	systemd-plymouth
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

%package core-libs
Summary:	Plymouth core libraries
Summary(pl.UTF-8):	Podstawowe biblioteki Plymouth
Group:		Libraries
Conflicts:	plymouth-libs < 0.8.4-0.20120319.1

%description core-libs
This package contains the libply and libply-splash-core libraries used
by Plymouth.

%description core-libs -l pl.UTF-8
Ten pakiet zawiera biblioteki libply i libply-splash-core
wykorzystywane przez Plymouth.

%package graphics-libs
Summary:	Plymouth graphics libraries
Summary(pl.UTF-8):	Biblioteki graficzne Plymouth
Group:		Development/Libraries
Requires:	%{name}-core-libs = %{version}-%{release}
Provides:	%{name}-graphics-libs = %{version}-%{release}
Obsoletes:	plymouth-libs < %{version}-%{release}
Conflicts:	plymouth-libs < 0.8.4-0.20120319.1

%description graphics-libs
This package contains the libply-splash-graphics library used by
graphical Plymouth splashes.

%description graphics-libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę libply-splash-graphics wykorzystywaną
przez graficzne ekrany Plymouth.

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

%package plugin-fade-throbber
Summary:	Plymouth "Fade-Throbber" plugin
Summary(pl.UTF-8):	Wtyczka Plymouth "Fade-Throbber"
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}

%description plugin-fade-throbber
This package contains the "Fade-Throbber" boot splash plugin for
Plymouth. It features a centered image that fades in and out while
other images pulsate around during system boot up.

%description plugin-fade-throbber -l pl.UTF-8
Ten pakiet zawiera wtyczkę ekranu startowego Plymouth "Fade-Throbber".
Cechuje się ona środkowym obrazkiem, który płynnie pojawia się i
wygasa, podczas gdy inne obrazki pulsują w trakcie startu systemu.

%package plugin-label
Summary:	Plymouth label plugin
Summary(pl.UTF-8):	Wtyczka Plymouth z etykietami
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}

%description plugin-label
This package contains the label control plugin for Plymouth. It
provides the ability to render text on graphical boot splashes using
pango and cairo.

%description plugin-label -l pl.UTF-8
Ten pakiet zawiera wtyczkę Plymouth sterującą etykietami. Daje ona
możliwość renderowania tekstu na graficznych ekranach startowych przy
użyciu bibliotek pango i cairo.

%package plugin-script
Summary:	Plymouth "script" plugin
Summary(pl.UTF-8):	Wtyczka Plymouth "script"
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}

%description plugin-script
This package contains the "script" boot splash plugin for Plymouth. It
features an extensible, scriptable boot splash language that
simplifies the process of designing custom boot splash themes.

%description plugin-script -l pl.UTF-8
Ten pakiet zawiera wtyczkę ekranu startowego Plymouth "script".
Odznacza się ona rozszerzalnym, skryptowym językiem ekranu startowego,
upraszczającym proces projektowania własnych motywów ekranów
startowych.

%package plugin-space-flares
Summary:	Plymouth "space-flares" plugin
Summary(pl.UTF-8):	Wtyczka Plymouth "space-flares"
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}
Requires:	%{name}-plugin-label = %{version}-%{release}

%description plugin-space-flares
This package contains the "space-flares" boot splash plugin for
Plymouth. It features a corner image with animated flares.

%description plugin-space-flares -l pl.UTF-8
Ten pakiet zawiera wtyczkę ekranu startowego Plymouth "space-flares".
Odznacza się ona umieszczonym w rogu obrazkiem z animowanymi
promieniami.

%package plugin-two-step
Summary:	Plymouth "two-step" plugin
Summary(pl.UTF-8):	Wtyczka Plymouth "two-step"
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}
Requires:	%{name}-plugin-label = %{version}-%{release}

%description plugin-two-step
This package contains the "two-step" boot splash plugin for Plymouth.
It features a two phased boot process that starts with a progressing
animation synced to boot time and finishes with a short, fast one-shot
animation.

%description plugin-two-step -l pl.UTF-8
Ten pakeit zawiera wtyczkę ekranu startowego Plymouth "two-step".
Odznacza się ona dwuetapowym procesem startu, rozpoczynającym się
postępującą animacją synchronizowaną z czasem uruchamiania, a kończy
krótką, jednorazową animacją.

%package plugin-throbgress
Summary:	Plymouth "Throbgress" plugin
Summary(pl.UTF-8):	Wtyczka Plymouth "Throbgress"
Group:		Base
Requires:	%{name}-graphics-libs = %{version}-%{release}
Requires:	%{name}-plugin-label = %{version}-%{release}

%description plugin-throbgress
This package contains the "throbgress" boot splash plugin for
Plymouth. It features a centered logo and animated spinner that spins
repeatedly while a progress bar advances at the bottom of the screen.

%description plugin-throbgress -l pl.UTF-8
Ten pakiet zawiera wtyczkę ekranu startowego "Throbgress" do Plymouth.
Cechuje się ona umieszczonym pośrodku logiem oraz animowanym kręcącym
się kółkiem, podczas gdy pasek postępu przesuwa się na dole ekranu.

%package system-theme
Summary:	Plymouth default theme
Summary(pl.UTF-8):	Domyślny motyw Plymouth
Group:		Base
Requires:	%{name}(system-theme) = %{version}-%{release}
Provides:	%{name}-system-plugin = %{version}-%{release}
Obsoletes:	plymouth-system-plugin < %{version}-%{release}

%description system-theme
This metapackage tracks the current distribution default theme.

%description system-theme -l pl.UTF-8
Ten metapakiet śledzi domyślny motyw dystrybucji.

%package theme-charge
Summary:	Plymouth "Charge" theme
Summary(pl.UTF-8):	Motyw Plymouth "Charge"
Group:		Base
Requires:	%{name}-plugin-two-step = %{version}-%{release}
Requires(post):	%{name}-scripts = %{version}-%{release}
Provides:	%{name}(system-theme) = %{version}-%{release}

%description theme-charge
This package contains the "charge" boot splash theme for Plymouth. It
features the shadowy hull of a Fedora logo charge up and and finally
burst into full form.

%description theme-charge -l pl.UTF-8
Ten pakiet zawiera motyw ekranu startowego Plymouth "Charge". Odznacza
się on cieniowaną łupiną loga Fedory, która rośnie, a ostatecznie
wybucha do pełnej postaci.

%package theme-fade-in
Summary:	Plymouth "Fade-In" theme
Summary(pl.UTF-8):	Motyw Plymouth "Fade in"
Group:		Base
Requires(post):	%{name}-scripts = %{version}-%{release}
Requires:	%{name}-plugin-fade-throbber = %{version}-%{release}
Obsoletes:	plymouth-plugin-fade-in

%description theme-fade-in
This package contains the "Fade-In" boot splash theme for Plymouth. It
features a centered logo that fades in and out while stars twinkle
around the logo during system boot up.

%description theme-fade-in -l pl.UTF-8
Ten pakiet zawiera motyw ekranu startowego Plymouth "Fade-In".
Odznacza się on umieszczonym pośrodku logiem, które w trakcie startu
systemu płynnie pojawia się i wygasa, podczas gdy wokół loga migoczą
gwiazdy.

%package theme-script
Summary:	Plymouth "Script" theme
Summary(pl.UTF-8):	Motyw Plymouth "Script"
Group:		Base
Requires(post):	%{name}-scripts = %{version}-%{release}
Requires:	%{name}-plugin-script = %{version}-%{release}

%description theme-script
This package contains the "script" boot splash theme for Plymouth. It
it is a simple example theme the uses the "script" plugin.

%description theme-script -l pl.UTF-8
Ten pakiet zawiera motyw ekranu startowego Plymouth "Script". Jest to
prosty przykład wykorzystujący wtyczkę "script".

%package theme-solar
Summary:	Plymouth "Solar" theme
Summary(pl.UTF-8):	Motyw Plymouth "Solar"
Group:		Base
Requires(post):	%{name}-scripts = %{version}-%{release}
Requires:	%{name}-plugin-space-flares = %{version}-%{release}
Obsoletes:	plymouth-plugin-solar

%description theme-solar
This package contains the "Solar" boot splash theme for Plymouth. It
features a blue flamed sun with animated solar flares.

%description theme-solar -l pl.UTF-8
Ten pakiet zawiera motyw ekranu startowego Plymouth "Solar". Odznacza
się on słońcem w niebieskich płomieniach z animowanymi promieniami
słonecznymi.

%package theme-spinfinity
Summary:	Plymouth "Spinfinity" theme
Summary(pl.UTF-8):	Motyw Plymouth "Spinfinity"
Group:		Base
Requires(post):	%{name}-scripts = %{version}-%{release}
Requires:	%{name}-plugin-throbgress = %{version}-%{release}
Obsoletes:	plymouth-plugin-spinfinity

%description theme-spinfinity
This package contains the "Spinfinity" boot splash theme for Plymouth.
It features a centered logo and animated spinner that spins in the
shape of an infinity sign.

%description theme-spinfinity -l pl.UTF-8
Ten pakiet zawiera motyw ekranu startowego Plymouth "Spinfinity".
Odznacza się on umieszczonym pośrodku logiem i animowanym kółkiem
kręcącym się po kształcie znaku nieskończoności.

%package theme-spinner
Summary:	Plymouth "Spinner" theme
Summary(pl.UTF-8):	Motyw Plymouth "Spinner"
Group:		Base
Requires(post):	%{name}-scripts = %{version}-%{release}
Requires:	%{name}-plugin-two-step = %{version}-%{release}

%description theme-spinner
This package contains the "spinner" boot splash theme for Plymouth. It
features a small spinner on a dark background.

%description theme-spinner -l pl.UTF-8
Ten pakiet zawiera motyw ekranu startowego Plymouth "Spinner".
Odznacza się on małym kółkiem kręcącym się na ciemnym tle.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# Change the default theme
sed -i -e 's/fade-in/charge/g' src/plymouthd.defaults

%build
%configure \
	%{__enable_disable drm_intel libdrm_intel} \
	%{__enable_disable drm_radeon libdrm_radeon} \
	%{__enable_disable drm_nouveau libdrm_nouveau} \
	%{__enable_disable kms libkms} \
	--disable-silent-rules \
	--disable-static \
	--disable-tests \
	--disable-gdm-transition \
	--enable-systemd-integration \
	--enable-tracing \
	--without-rhgb-compat-link \
	--with-background-start-color-stop=0x009431 \
	--with-background-end-color-stop=0x006300 \
	--with-background-color=0x00c663 \
	--with-logo=%{_pixmapsdir}/plymouth-logo.png \
	--with-release-file=/etc/os-release \
	--with-system-root-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{systemdtmpfilesdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/plymouth/default-boot-duration
> $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth/boot-duration

# FC: Add charge, our new default
install -d $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
cp $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/glow/{box,bullet,entry,lock}.png $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge

# FC: Drop glow, it's not very Fedora-y
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/glow

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

cp -p %{SOURCE7} $RPM_BUILD_ROOT%{systemdunitdir}/systemd-ask-password-plymouth.path
cp -p %{SOURCE8} $RPM_BUILD_ROOT%{systemdunitdir}/systemd-ask-password-plymouth.service

# install plymouth services for targets
# http://cgit.freedesktop.org/systemd/systemd/commit/?id=26cbf29c52a36b6ad9d1ccc16d8f7adccefeddca
install -d $RPM_BUILD_ROOT%{systemdunitdir}/{halt,kexec,poweroff,reboot,sysinit,multi-user}.target.wants
ln -sf ../plymouth-start.service $RPM_BUILD_ROOT%{systemdunitdir}/sysinit.target.wants/plymouth-start.service
ln -sf ../plymouth-read-write.service $RPM_BUILD_ROOT%{systemdunitdir}/sysinit.target.wants/plymouth-read-write.service
ln -sf ../plymouth-quit.service $RPM_BUILD_ROOT%{systemdunitdir}/multi-user.target.wants/plymouth-quit.service
ln -sf ../plymouth-quit-wait.service $RPM_BUILD_ROOT%{systemdunitdir}/multi-user.target.wants/plymouth-quit-wait.service
ln -sf ../plymouth-reboot.service $RPM_BUILD_ROOT%{systemdunitdir}/reboot.target.wants/plymouth-reboot.service
ln -sf ../plymouth-kexec.service $RPM_BUILD_ROOT%{systemdunitdir}/kexec.target.wants/plymouth-kexec.service
ln -sf ../plymouth-poweroff.service $RPM_BUILD_ROOT%{systemdunitdir}/poweroff.target.wants/plymouth-poweroff.service
ln -sf ../plymouth-halt.service $RPM_BUILD_ROOT%{systemdunitdir}/halt.target.wants/plymouth-halt.service

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_reload

%postun
if [ $1 -eq 0 ]; then
	rm -f %{_libdir}/plymouth/default.so
fi
%systemd_reload

%post	core-libs -p /sbin/ldconfig
%postun	core-libs -p /sbin/ldconfig
%post	graphics-libs -p /sbin/ldconfig
%postun	graphics-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/plymouth
%dir %{_sysconfdir}/plymouth
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/plymouth/plymouthd.conf
%{_mandir}/man8/plymouth.8*
%attr(755,root,root) %{plymouthdaemon_execdir}/plymouthd
%attr(755,root,root) %{plymouthclient_execdir}/plymouth
%attr(755,root,root) %{_libdir}/plymouth/details.so
%attr(755,root,root) %{_libdir}/plymouth/text.so
%attr(755,root,root) %{_libdir}/plymouth/renderers/drm.so
%attr(755,root,root) %{_libdir}/plymouth/renderers/frame-buffer.so
%dir %{_datadir}/plymouth
%dir %{_datadir}/plymouth/themes
%dir %{_datadir}/plymouth/themes/details
%dir %{_datadir}/plymouth/themes/text
%{_datadir}/plymouth/plymouthd.defaults
%{_datadir}/plymouth/default-boot-duration
%{_datadir}/plymouth/themes/details/details.plymouth
%{_datadir}/plymouth/themes/text/text.plymouth
%{_pixmapsdir}/plymouth-logo.png
%{systemdtmpfilesdir}/%{name}.conf
%dir %{_localstatedir}/lib/plymouth
%ghost %{_localstatedir}/lib/plymouth/boot-duration
%{_localstatedir}/run/plymouth
%{_localstatedir}/spool/plymouth

%{systemdunitdir}/plymouth-halt.service
%{systemdunitdir}/plymouth-kexec.service
%{systemdunitdir}/plymouth-poweroff.service
%{systemdunitdir}/plymouth-quit-wait.service
%{systemdunitdir}/plymouth-quit.service
%{systemdunitdir}/plymouth-read-write.service
%{systemdunitdir}/plymouth-reboot.service
%{systemdunitdir}/plymouth-start.service
%{systemdunitdir}/plymouth-switch-root.service
%{systemdunitdir}/systemd-ask-password-plymouth.path
%{systemdunitdir}/systemd-ask-password-plymouth.service
%{systemdunitdir}/halt.target.wants/plymouth-halt.service
%dir %{systemdunitdir}/initrd-switch-root.target.wants
%{systemdunitdir}/initrd-switch-root.target.wants/plymouth-switch-root.service
%{systemdunitdir}/kexec.target.wants/plymouth-kexec.service
%{systemdunitdir}/multi-user.target.wants/plymouth-quit.service
%{systemdunitdir}/multi-user.target.wants/plymouth-quit-wait.service
%{systemdunitdir}/poweroff.target.wants/plymouth-poweroff.service
%{systemdunitdir}/reboot.target.wants/plymouth-reboot.service
%{systemdunitdir}/sysinit.target.wants/plymouth-read-write.service
%{systemdunitdir}/sysinit.target.wants/plymouth-start.service

%files core-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{plymouth_libdir}/libply.so.*.*.*
%attr(755,root,root) %ghost %{plymouth_libdir}/libply.so.2
%attr(755,root,root) %{plymouth_libdir}/libply-splash-core.so.*.*.*
%attr(755,root,root) %ghost %{plymouth_libdir}/libply-splash-core.so.2
%attr(755,root,root) %{_libdir}/libply-boot-client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libply-boot-client.so.2
%dir %{_libdir}/plymouth
%dir %{_libdir}/plymouth/renderers

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

%files plugin-fade-throbber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/fade-throbber.so

%files plugin-label
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/label.so

%files plugin-script
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/script.so

%files plugin-space-flares
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/space-flares.so

%files plugin-throbgress
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/throbgress.so

%files plugin-two-step
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/two-step.so

%files system-theme
%defattr(644,root,root,755)

%files theme-charge
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/charge
%{_datadir}/plymouth/themes/charge/*.png
%{_datadir}/plymouth/themes/charge/charge.plymouth

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

%files theme-spinfinity
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/spinfinity
%{_datadir}/plymouth/themes/spinfinity/box.png
%{_datadir}/plymouth/themes/spinfinity/bullet.png
%{_datadir}/plymouth/themes/spinfinity/entry.png
%{_datadir}/plymouth/themes/spinfinity/lock.png
%{_datadir}/plymouth/themes/spinfinity/throbber-[0-3][0-9].png
%{_datadir}/plymouth/themes/spinfinity/spinfinity.plymouth

%files theme-solar
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/solar
%{_datadir}/plymouth/themes/solar/*.png
%{_datadir}/plymouth/themes/solar/solar.plymouth

%files theme-script
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/script
%{_datadir}/plymouth/themes/script/*.png
%{_datadir}/plymouth/themes/script/script.script
%{_datadir}/plymouth/themes/script/script.plymouth
