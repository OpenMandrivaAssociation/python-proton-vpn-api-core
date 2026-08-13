Name:		python-proton-vpn-api-core
Version:	5.5.11
Release:	1
URL:		https://github.com/ProtonVPN/python-proton-vpn-api-core
Source0:	%{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Provides a uniform API to other Proton VPN components
License:	GPL-3.0-only
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
BuildRequires:  python%{pyver}dist(cryptography)
BuildRequires:  python%{pyver}dist(pycairo)
BuildRequires:  pkgconfig(pygobject-3.0)
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
Requires:   python%{pyver}dist(cryptography)
Requires:   python%{pyver}dist(pycairo)
Requires:   networkmanager
Requires:   networkmanager-openvpn
Requires:   networkmanager-openvpn-gtk
Requires:   gobject-introspection
Requires:   typelib(NM)

Obsoletes: python-proton-vpn-network-manager

%description
Acts as a facade to the other Proton VPN components, exposing a uniform 
API to the available Proton VPN services.

%files
%license LICENSE CODEOWNERS
%doc README.md
%{py_sitedir}/proton/
%{py_sitedir}/proton_vpn_api_core-*.egg-info
