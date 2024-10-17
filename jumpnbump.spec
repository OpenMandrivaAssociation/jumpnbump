%define name	jumpnbump  
%define version 1.55
%define release 6

Summary:	Cute little Bunny Game ( with bloody gore details )
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Arcade
Source0:	http://www.jumpbump.mine.nu/port/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Source2:	jumpnbump-1.41-man-pages.tar.bz2
Patch0:     jumpnbump-1.50-format_string.patch
URL:		https://www.jumpbump.mine.nu/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libSDL_mixer-devel libSDL_net-devel

%description
Jump n bump is a game for almost the whole family. You are cute fluffy little
bunnies and hop on the other bunnies' heads, to make each others explode
with realistic bunny blood.

To play the game:
- Jiffy plays with the arrow keys
- Fizz plays with j, i, l
- Dott plays with a, w, d
- Mijji plays with 4, 8, 6

%prep
%setup -q -a 2 -n %name-1.50
perl -pi -e 's!PREFIX\"/share/jumpnbump/jumpbump.dat!\"%{_gamesdatadir}/%{name}/jumpbump.dat!g' globals.h
%patch0 -p0

%build
%configure2_5x --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
# french man page
install -D fr/jumpnbump.6 %buildroot%_mandir/fr/man6/jumpnbump.6
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Jump 'n Bump
Comment=Violent game with cute little bunnies
Exec=%_gamesbindir/%{name}
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

install -d ${RPM_BUILD_ROOT}{%{_miconsdir},%{_liconsdir}}
tar -xOjf %{SOURCE1} icons/16x16.png > ${RPM_BUILD_ROOT}%{_miconsdir}/%{name}.png
tar -xOjf %{SOURCE1} icons/32x32.png > ${RPM_BUILD_ROOT}%{_iconsdir}/%{name}.png
tar -xOjf %{SOURCE1} icons/48x48.png > ${RPM_BUILD_ROOT}%{_liconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog LINKS README TODO levelmaking/jumpnbump_levelmaking.htm levelmaking/*.gif
%{_gamesbindir}/*
%dir %{_datadir}/games/%{name}
%{_gamesdatadir}/%{name}/*
%{_mandir}/man6/%name.6*
%lang(fr) %{_mandir}/fr/man6/%name.6*
%_datadir/applications/mandriva*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png




%changelog
* Sun Mar 29 2009 Michael Scherer <misc@mandriva.org> 1.55-5mdv2009.1
+ Revision: 362114
- add some warning about the bloody part of the game, asked by stormi
- add patch to make it compile again

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.55-5mdv2009.0
+ Revision: 247427
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.55-3mdv2008.1
+ Revision: 140829
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Tue Jan 02 2007 Olivier Blin <oblin@mandriva.com> 1.55-3mdv2007.0
+ Revision: 103137
- move jumpnbump in contrib
- Import jumpnbump

* Wed Aug 02 2006 Götz Waschk <goetz@zarb.org> 1.55-2plf2007.0
- xdg menu

* Tue Apr 25 2006 Götz Waschk <goetz@zarb.org> 1.55-1plf
- fix build
- drop patches
- New release 1.55

* Tue Sep 21 2004 Götz Waschk <goetz@zarb.org> 1.50-2plf
- fix invalid distribution

* Thu Jun 17 2004 Götz Waschk <goetz@plf.zarb.org> 1.50-1plf
- add source URL
- New release 1.50

* Wed May 12 2004 Götz Waschk <goetz@plf.zarb.org> 1.41-3plf
- rebuild to fix menu section
- fix description

