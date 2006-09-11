Summary:	KDE tray icon Network activity monitor
Summary(pl):	Ikona tacki systemowej KDE monitoruj±ca aktywno¶æ sieci
Name:		ktraynetworker
Version:	0.8c
Release:	1
%define		_res_ver	0.2
Group:		X11/Applications
License:	GPL
Source0:	http://www.xiaprojects.com/www/downloads/files/ktraynetworker/%{name}-%{version}.tar.bz2
# Source0-md5:	b0e14fac9bcb0f5a33588a9c9386fea7
Source1:	http://www.xiaprojects.com/www/downloads/files/ktraynetworker/%{name}_resources_%{_res_ver}.tar.bz2
# Source1-md5:	021d5529af23dd5607129982184688b7
URL:		http://www.xiaprojects.com/www/prodotti/ktraynetworker/main.php
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.3
BuildRequires:	qt-devel >= 3.3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program will help you to view network activity on your network
device such as eth0, ppp0 and so on.

%description -l pl
Ten program pomaga obserwowaæ aktywno¶æ sieciow± urz±dzenia takiego
jak eth0, ppp0 itp.

%prep
%setup -q
tar xjf %{SOURCE1}
mkdir themes
tar xjf %{name}_resources_%{_res_ver}/themes.tar.bz2 -C themes

%build
cp -f /usr/share/automake/config.* admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/apps/%{name}/themes
cp -R themes  $RPM_BUILD_ROOT%{_datadir}/apps/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	shelldesktopdir=%{_desktopdir}

echo 'Categories=Qt;KDE;Network;' >> \
	$RPM_BUILD_ROOT%{_desktopdir}/ktraynetworker.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktraynetworker
%{_datadir}/apps/ktraynetworker
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/ktraynetworker.png
