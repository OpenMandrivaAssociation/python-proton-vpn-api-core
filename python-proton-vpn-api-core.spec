Name:		python-proton-vpn-api-core
Version:	4.14.3
Release:	1
Source0:	https://github.com/ProtonVPN/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Acts as a facade to the other Proton VPN components, exposing a uniform API to the available Proton VPN services.
URL:		https://github.com/ProtonVPN/proton-vpn-api-core
License:	GPL
Group:		Development/Python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(proton-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(distro)
BuildRequires:	python%{pyver}dist(sentry-sdk)
BuildRequires:	python%{pyver}dist(pynacl)
BuildRequires:  python%{pyver}dist(fido2)
BuildRequires:  python%{pyver}dist(packaging)
BuildRequires:  python%{pyver}dist(proton-vpn-local-agent) >= 1.6.0
BuildRequires:  python%{pyver}dist(jinja2)
BuildRequires:  python-gobject3
BuildRequires:  networkmanager
BuildRequires:  networkmanager-openvpn
BuildRequires:  networkmanager-openvpn-gtk
BuildRequires:  gobject-introspection

BuildSystem:	python
BuildArch:	noarch

Requires:	python%{pyver}dist(distro)
Requires:	python%{pyver}dist(proton-core)
Requires:	python%{pyver}dist(pynacl)
Requires:	python%{pyver}dist(sentry-sdk)
Requires: python%{pyver}dist(fido2)
Requires:   python%{pyver}dist(packaging)
Requires:   python%{pyver}dist(proton-vpn-local-agent) >= 1.6.0
Requires:   python%{pyver}dist(jinja2)
Requires:   python-gobject3
Requires:   networkmanager
Requires:   networkmanager-openvpn
Requires:   networkmanager-openvpn-gtk
Requires:   gobject-introspection
Requires:   lib64networkmanager-gir1.0

%description
%{summary}.

%files
%{py_sitedir}/proton/
%{py_sitedir}/proton_vpn_api_core-*.egg-info
