%define name	jumpnbump  
%define version 1.55
%define release %mkrel 5

Summary:	Cute little Bunny Game
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Arcade
Source0:	http://www.jumpbump.mine.nu/port/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Source2:	jumpnbump-1.41-man-pages.tar.bz2
URL:		http://www.jumpbump.mine.nu/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libSDL_mixer-devel libSDL_net-devel

%description
Jump n bump is a game for the whole family. You are cute fluffy little
bunnies and hop on the other bunnies' heads.

To play the game:
- Jiffy plays with the arrow keys
- Fizz plays with j, i, l
- Dott plays with a, w, d
- Mijji plays with 4, 8, 6

%prep
%setup -q -a 2 -n %name-1.50
perl -pi -e 's!PREFIX\"/share/jumpnbump/jumpbump.dat!\"%{_gamesdatadir}/%{name}/jumpbump.dat!g' globals.h

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


