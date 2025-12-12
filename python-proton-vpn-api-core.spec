Name:		python-proton-vpn-api-core
Version:	4.13.2
Release:	2
Source0:	https://github.com/ProtonVPN/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Acts as a facade to the other Proton VPN components, exposing a uniform API to the available Proton VPN services.
URL:		https://github.com/ProtonVPN/proton-vpn-api-core
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(proton-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(distro)
BuildRequires:	python%{pyver}dist(sentry-sdk)
BuildRequires:	python%{pyver}dist(pynacl)

BuildSystem:	python
BuildArch:	noarch

Requires:	python%{pyver}dist(distro)
Requires:	python%{pyver}dist(proton-core)
Requires:	python%{pyver}dist(pynacl)
Requires:	python%{pyver}dist(sentry-sdk)
Requires: python%{pyver}dist(fido2)

%description


%files
%{py_sitedir}/proton/
%{py_sitedir}/proton_vpn_api_core-*.egg-info
