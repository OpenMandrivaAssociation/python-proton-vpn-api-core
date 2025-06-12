Name:		python-proton-vpn-api-core
Version:	0.42.4
Release:	1
Source0:	https://github.com/ProtonVPN/%{name}/archive/refs/tags/v%{version}.tar.gz
Summary:	Acts as a facade to the other Proton VPN components, exposing a uniform API to the available Proton VPN services.
URL:		https://github.com/ProtonVPN/proton-vpn-api-core
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python-proton-core
BuildRequires:	python-setuptools
BuildRequires:	python-distro
BuildRequires:	python-sentry-sdk
BuildRequires:	python-pynacl

BuildSystem:	python
BuildArch:	noarch

Requires:	python-distro
Requires:	python-proton-core
Requires:	python-pynacl
Requires:	python-sentry-sdk

%description


%files
%{py_sitedir}/proton/
%{py_sitedir}/proton_vpn_api_core-*.egg-info
