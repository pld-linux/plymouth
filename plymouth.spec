# TODO
# - integrate with geninitrd
# - pldize recent update (r1.18)
# - unpackaged /etc/logrotate.d/bootlog ?
#
# Conditional build:
%bcond_without	drm		# disable building with DRM renderer support

Summary:	Graphical Boot Animation and Logger
Summary(pl.UTF-8):	Graficzna animacja i logowanie startu systemu
Name:		plymouth
Version:	24.004.60
Release:	3
License:	GPL v2+
Group:		Base
Source0:	https://www.freedesktop.org/software/plymouth/releases/%{name}-%{version}.tar.xz
# Source0-md5:	6a6d6ec1a6d6e9bd776f368619864949
Source1:	%{name}-logo.png
# Source1-md5:	6b38a868585adfd3a96a4ad16973c1f8
Source2:	boot-duration
Source3:	%{name}-update-initrd
Patch0:		text-colors.patch
Patch1:		%{name}-restore-suspend.patch
# allow to specify systemd-tty-ask-password-agent path even if not installed at build time
Patch2:		%{name}-paths.patch
Patch3:		%{name}-systemd-prefix.patch
URL:		https://www.freedesktop.org/wiki/Software/Plymouth
BuildRequires:	cairo-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gtk+3-devel >= 3.14.0
%{?with_drm:BuildRequires:	libdrm-devel}
BuildRequires:	libevdev-devel
BuildRequires:	libpng-devel >= 2:1.2.16
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.61
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.21.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-units
BuildRequires:	udev-devel
BuildRequires:	xkeyboard-config
BuildRequires:	xorg-lib-libxkbcommon-devel
Requires:	%{name}-graphics-libs = %{version}-%{release}
Requires(post):	%{name}-scripts = %{version}-%{release}
Requires:	/etc/os-release
Requires:	systemd-units
Obsoletes:	plymouth-gdm-hooks < 0.8.4
Obsoletes:	plymouth-plugin-throbgress < 0.9.5
Obsoletes:	plymouth-utils < 0.8.4
Obsoletes:	systemd-plymouth < 1:186
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Conflicts:	plymouth-libs < 0.8.5

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
Requires:	gtk+3 >= 3.14.0
Obsoletes:	plymouth-libs < 0.8.5

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

%package static
Summary:	Static libraries for writing Plymouth splash plugins
Summary(pl.UTF-8):	Statyczne biblioteki do tworzenia wtyczek graficznych Plymouth
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libraries used to develop 3rd party
splash plugins for Plymouth.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne biblioteki, przydatne do tworzenia
wtyczek graficznych Plymouth.

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
This package contains the label control plugins for Plymouth. They
provide the ability to render text on graphical boot splashes using
pango and cairo.

%description plugin-label -l pl.UTF-8
Ten pakiet zawiera wtyczki Plymouth sterujące etykietami. Dają one
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

%package theme-bgrt
Summary:	Jimmac's spinner theme using the ACPI BGRT graphics as background
Summary(pl.UTF-8):	Motyw Spinner Jimmaca wykorzystujący jako tło grafikę ACPI BGRT
Group:		Base
Requires(post):	%{name}-scripts = %{version}-%{release}
Requires:	%{name}-plugin-two-step = %{version}-%{release}
Provides:	%{name}(system-theme) = %{version}-%{release}

%description theme-bgrt
Jimmac's spinner theme using the ACPI BGRT graphics as background.

%description theme-bgrt -l pl.UTF-8
Motyw Spinner Jimmaca wykorzystujący jako tło grafikę ACPI BGRT

%package theme-glow
Summary:	Plymouth "Glow" theme
Summary(pl.UTF-8):	Motyw Plymouth "Glow"
Group:		Base
Requires:	%{name}-plugin-two-step = %{version}-%{release}
Requires(post):	%{name}-scripts = %{version}-%{release}
Provides:	%{name}(system-theme) = %{version}-%{release}
Obsoletes:	plymouth-theme-charge < 0.8.9

%description theme-glow
This package contains the "Glow" boot splash theme for Plymouth.
Corporate theme with pie chart boot progress followed by a glowing
emerging logo.

%description theme-glow -l pl.UTF-8
Ten pakiet zawiera motyw ekranu startowego Plymouth "Glow".

%package theme-fade-in
Summary:	Plymouth "Fade-In" theme
Summary(pl.UTF-8):	Motyw Plymouth "Fade in"
Group:		Base
Requires(post):	%{name}-scripts = %{version}-%{release}
Requires:	%{name}-plugin-fade-throbber = %{version}-%{release}
Obsoletes:	plymouth-plugin-fade-in < 0.7.0

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
Obsoletes:	plymouth-plugin-solar < 0.7.0

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
Requires:	%{name}-plugin-two-step = %{version}-%{release}
Obsoletes:	plymouth-plugin-spinfinity < 0.7.0

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
%patch2 -p1
%patch3 -p1

# Change the default theme
%{__sed} -i -e 's/Theme=.*/Theme=tribar/' -e 's/ShowDelay=.*//' src/plymouthd.defaults

%build
%meson build \
	--bindir=/bin \
	--sbindir=/sbin \
	-Dbackground-color=0x00c663 \
	-Dbackground-start-color-stop=0x009431 \
	-Dbackground-end-color-stop=0x006300 \
	%{!?with_drm:-Ddrm=false} \
	-Dlogo=%{_pixmapsdir}/plymouth-logo.png \
	-Drelease-file=/etc/os-release \
	-Dsystemd_ask_password_agent_path=/bin/systemd-tty-ask-password-agent

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{systemdtmpfilesdir}}

# meson/ninja symlinking requires target file to be already present
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/plymouth-logo.png

%ninja_install -C build

# meson-based plymouth build doesn't support installing into split /usr
install -d $RPM_BUILD_ROOT{/%{_lib},%{_sbindir}}
%{__mv} $RPM_BUILD_ROOT{/sbin,%{_sbindir}}/plymouth-set-default-theme
%{__mv} $RPM_BUILD_ROOT%{_libdir}/libply.so.* $RPM_BUILD_ROOT/%{_lib}
%{__mv} $RPM_BUILD_ROOT%{_libdir}/libply-splash-core.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libply.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libply.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libply-splash-core.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libply-splash-core.so

install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/plymouth/default-boot-duration
> $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth/boot-duration

# Override plymouth-update-initrd to work with dracut or mkinitrd
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_libexecdir}/plymouth/plymouth-update-initrd

ln -s plymouth-logo.png $RPM_BUILD_ROOT%{_pixmapsdir}/system-logo-white.png

# Usupported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README.md
%dir %{_sysconfdir}/plymouth
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/plymouth/plymouthd.conf
%{_mandir}/man8/plymouth.8*
%attr(755,root,root) /bin/plymouth
%attr(755,root,root) /sbin/plymouthd
%attr(755,root,root) %{_libdir}/plymouth/details.so
%attr(755,root,root) %{_libdir}/plymouth/text.so
%attr(755,root,root) %{_libdir}/plymouth/tribar.so
%attr(755,root,root) %{_libdir}/plymouth/renderers/drm.so
%attr(755,root,root) %{_libdir}/plymouth/renderers/frame-buffer.so
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/plymouth
%endif
%attr(755,root,root) %{_libexecdir}/plymouth/plymouthd-fd-escrow
%dir %{_datadir}/plymouth
%dir %{_datadir}/plymouth/themes
%dir %{_datadir}/plymouth/themes/details
%dir %{_datadir}/plymouth/themes/text
%dir %{_datadir}/plymouth/themes/tribar
%{_datadir}/plymouth/plymouthd.defaults
%{_datadir}/plymouth/default-boot-duration
%{_datadir}/plymouth/themes/details/details.plymouth
%{_datadir}/plymouth/themes/text/text.plymouth
%{_datadir}/plymouth/themes/tribar/tribar.plymouth
%{_pixmapsdir}/plymouth-logo.png
%{_pixmapsdir}/system-logo-white.png
%dir %{_localstatedir}/lib/plymouth
%ghost %{_localstatedir}/lib/plymouth/boot-duration
%{_localstatedir}/spool/plymouth
%{_mandir}/man1/plymouth.1*
%{_mandir}/man8/plymouthd.8*

%{systemdunitdir}/plymouth-halt.service
%{systemdunitdir}/plymouth-kexec.service
%{systemdunitdir}/plymouth-poweroff.service
%{systemdunitdir}/plymouth-quit-wait.service
%{systemdunitdir}/plymouth-quit.service
%{systemdunitdir}/plymouth-read-write.service
%{systemdunitdir}/plymouth-reboot.service
%{systemdunitdir}/plymouth-start.service
%{systemdunitdir}/plymouth-switch-root.service
%{systemdunitdir}/plymouth-switch-root-initramfs.service
%{systemdunitdir}/systemd-ask-password-plymouth.path
%{systemdunitdir}/systemd-ask-password-plymouth.service
%{systemdunitdir}/halt.target.wants/plymouth-halt.service
%{systemdunitdir}/halt.target.wants/plymouth-switch-root-initramfs.service
%dir %{systemdunitdir}/initrd-switch-root.target.wants
%{systemdunitdir}/initrd-switch-root.target.wants/plymouth-switch-root.service
%{systemdunitdir}/initrd-switch-root.target.wants/plymouth-start.service
%{systemdunitdir}/kexec.target.wants/plymouth-kexec.service
%{systemdunitdir}/kexec.target.wants/plymouth-switch-root-initramfs.service
%{systemdunitdir}/multi-user.target.wants/plymouth-quit.service
%{systemdunitdir}/multi-user.target.wants/plymouth-quit-wait.service
%{systemdunitdir}/poweroff.target.wants/plymouth-poweroff.service
%{systemdunitdir}/poweroff.target.wants/plymouth-switch-root-initramfs.service
%{systemdunitdir}/reboot.target.wants/plymouth-reboot.service
%{systemdunitdir}/reboot.target.wants/plymouth-switch-root-initramfs.service
%{systemdunitdir}/sysinit.target.wants/plymouth-read-write.service
%{systemdunitdir}/sysinit.target.wants/plymouth-start.service

%files core-libs
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libply.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libply.so.5
%attr(755,root,root) /%{_lib}/libply-splash-core.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libply-splash-core.so.5
%attr(755,root,root) %{_libdir}/libply-boot-client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libply-boot-client.so.5
%dir %{_libdir}/plymouth
%dir %{_libdir}/plymouth/renderers

%files graphics-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libply-splash-graphics.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libply-splash-graphics.so.5
%attr(755,root,root) %{_libdir}/plymouth/renderers/x11.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libply.so
%attr(755,root,root) %{_libdir}/libply-boot-client.so
%attr(755,root,root) %{_libdir}/libply-splash-core.so
%attr(755,root,root) %{_libdir}/libply-splash-graphics.so
%{_includedir}/plymouth-1
%{_pkgconfigdir}/ply-boot-client.pc
%{_pkgconfigdir}/ply-splash-core.pc
%{_pkgconfigdir}/ply-splash-graphics.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libply.a
%attr(755,root,root) %{_libdir}/libply-boot-client.a
%attr(755,root,root) %{_libdir}/libply-splash-core.a
%attr(755,root,root) %{_libdir}/libply-splash-graphics.a

%files scripts
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/plymouth-set-default-theme
%attr(755,root,root) %{_libexecdir}/plymouth/plymouth-generate-initrd
%attr(755,root,root) %{_libexecdir}/plymouth/plymouth-populate-initrd
%attr(755,root,root) %{_libexecdir}/plymouth/plymouth-update-initrd
%{_mandir}/man1/plymouth-set-default-theme.1*

%files plugin-fade-throbber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/fade-throbber.so

%files plugin-label
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/label-freetype.so
%attr(755,root,root) %{_libdir}/plymouth/label-pango.so

%files plugin-script
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/script.so

%files plugin-space-flares
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/space-flares.so

%files plugin-two-step
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plymouth/two-step.so

%files system-theme
%defattr(644,root,root,755)

%files theme-bgrt
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/bgrt
%{_datadir}/plymouth/themes/bgrt/bgrt.plymouth

%files theme-glow
%defattr(644,root,root,755)
%dir %{_datadir}/plymouth/themes/glow
%{_datadir}/plymouth/themes/glow/*.png
%{_datadir}/plymouth/themes/glow/glow.plymouth

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
%{_datadir}/plymouth/themes/spinfinity/animation-0001.png
%{_datadir}/plymouth/themes/spinfinity/box.png
%{_datadir}/plymouth/themes/spinfinity/bullet.png
%{_datadir}/plymouth/themes/spinfinity/capslock.png
%{_datadir}/plymouth/themes/spinfinity/entry.png
%{_datadir}/plymouth/themes/spinfinity/header-image.png
%{_datadir}/plymouth/themes/spinfinity/keyboard.png
%{_datadir}/plymouth/themes/spinfinity/keymap-render.png
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
