Summary:	KDE tray icon Network activity monitor
Summary(pl):	Ikona tacki systemowej KDE monitoruj±ca aktywno¶æ sieci
Name:		ktraynetworker
Version:	0.7
Release:	1
Group:		X11/Applications
License:	GPL
Source0:	http://www.xiaprojects.com/www/downloads/files/%{name}-%{version}.tar.bz2
# Source0-md5:	b33fcabb9eb6bda391f479bb0ad50baa
URL:		http://www.xiaprojects.com/www/prodotti/ktraynetworker/main.php
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	qt-devel >= 3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program will help you to view network activity on your network
device such as eth0, ppp0 and so on.

%description -l pl
Ten program pomaga obserwowaæ aktywno¶æ sieciow± urz±dzenia takiego
jak eth0, ppp0 itp.

%prep
%setup -q

%build
%configure
%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktraynetworker
%{_datadir}/*
