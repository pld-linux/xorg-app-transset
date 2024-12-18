Summary:	transset application - utility for setting opacity property
Summary(pl.UTF-8):	Aplikacja transset - narzędzie do ustawiania przezroczystości
Name:		xorg-app-transset
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/transset-%{version}.tar.xz
# Source0-md5:	dbdc4ec9627ca779b037297ed6cc7804
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
transset is a simple program for X servers supporting the XFIXES,
DAMAGE, and COMPOSITE extensions. It lets the user set the
transparency on a window.

%description -l pl.UTF-8
transset to prosty program dla serwerów X obsługujących rozszerzenia
XFIXES, DAMAGE i COMPOSITE. Pozwala użytkownikowi ustawić
przezroczystość okienka.

%prep
%setup -q -n transset-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/transset
%{_mandir}/man1/transset.1*
