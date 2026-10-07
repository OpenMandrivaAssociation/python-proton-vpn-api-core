%undefine _debugsource_packages

%define name1 protun
%define version1 2.2.1

Name:		python-proton-vpn-api-core
Version:	5.8.7
Release:	2
Summary:	Provides a uniform API to other Proton VPN components
License:	GPL-3.0-only
Group:		Development/Python
URL:		https://github.com/ProtonVPN/python-proton-vpn-api-core
Source0:	%{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	https://github.com/ProtonVPN/protun/archive/refs/tags/v%{version1}.tar.gz#/%{name1}-%{version1}.tar.gz
Source2:    %{name}-%{version}-vendor.tar.xz
### Generate Source2 archive
#   this one is awful
#   The api-core archive has an empty directory that links to the protun archive
#   We build offline, so that is a problem
#   extract api-core archive, then extract protun archive
#   copy the contents of protun and paste into python-proton-vpn-api-core-{version}/dependencies/protun
#   now we can do the rust vendoring

#   enter source tree for python-proton-vpn-api-core
#   cargo vendor -s dependencies/protun/Cargo.toml
#   tar -cJvf python-proton-vpn-api-core-{version}-vendor.tar.xz vendor
#   place vendor archive alongside source archive

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(proton-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(distro)
BuildRequires:	python%{pyver}dist(sentry-sdk)
BuildRequires:	python%{pyver}dist(pynacl)
BuildRequires:  python%{pyver}dist(fido2)
BuildRequires:  python%{pyver}dist(packaging)
BuildRequires:  python%{pyver}dist(jinja2)
BuildRequires:  python%{pyver}dist(cryptography)
BuildRequires:  python%{pyver}dist(pycairo)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-asyncio)
BuildRequires:  python%{pyver}dist(dbus-fast)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnftnl)
BuildRequires:  networkmanager
BuildRequires:  networkmanager-openvpn
BuildRequires:  networkmanager-openvpn-gtk
BuildRequires:  gobject-introspection
BuildRequires:	cargo
BuildRequires:  rust-packaging

Requires:	python%{pyver}dist(distro)
Requires:	python%{pyver}dist(proton-core)
Requires:	python%{pyver}dist(pynacl)
Requires:	python%{pyver}dist(sentry-sdk)
Requires:   python%{pyver}dist(fido2)
Requires:   python%{pyver}dist(packaging)
Requires:   python%{pyver}dist(jinja2)
Requires:   python%{pyver}dist(cryptography)
Requires:   python%{pyver}dist(pycairo)
Requires:   python%{pyver}dist(dbus-fast)
Requires:   networkmanager
Requires:   networkmanager-openvpn
Requires:   networkmanager-openvpn-gtk
Requires:   gobject-introspection
Requires:   typelib(NM)

Obsoletes: python-proton-vpn-network-manager <= 0.13.5
Obsoletes: python-proton-vpn-local-agent <= 1.6.3
Obsoletes: proton-vpn-local-agent <= 1.6.3
# 5.5.0 changed from noarch to arch-dependent; this forces removal of the old noarch build on upgrade.
Obsoletes: python-proton-vpn-api-core < 5.5.6

%description
Acts as a facade to the other Proton VPN components, exposing a uniform 
API to the available Proton VPN services.

%prep
%autosetup -p1
tar -zxf %{SOURCE1}
tar -zxf %{SOURCE2}
mv %{name1}-%{version1}/.[!.]* %{name1}-%{version1}/* dependencies/%{name1}

# cat to .cargo/config.toml for protun
# add ../../ to the directory to point to correct location
cat >> dependencies/protun/.cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."sparse+https://rust-registry.proton.me/index/"]
registry = "sparse+https://rust-registry.proton.me/index/"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "../../vendor"

EOF

# cat to .cargo/config.toml for proton-vpn-api-core
cat >> .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."sparse+https://rust-registry.proton.me/index/"]
registry = "sparse+https://rust-registry.proton.me/index/"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

%build
cargo build --release --frozen \
      --bin nm-protun-service \
      --bin proton-vpn-kill-switch-service \
      --lib \
      --features 'protun,python,core,local_agent,kill_switch,telemetry'

%py_build

%install
%py_install
install -Dm755 target/release/nm-protun-service %{buildroot}%{_libdir}/nm-protun-service
install -Dm644 resources/nm-protun-service.conf %{buildroot}%{_datadir}/dbus-1/system.d/nm-protun-service.conf

install -Dm755 target/release/proton-vpn-kill-switch-service %{buildroot}%{_libdir}/proton-vpn-kill-switch-service
install -Dm644 resources/proton-vpn-kill-switch.conf %{buildroot}%{_datadir}/dbus-1/system.d/me.proton.vpn.kill_switch.conf

install -Dm644 resources/proton-vpn-kill-switch.dbus-service %{buildroot}%{_datadir}/dbus-1/system-services/me.proton.vpn.kill_switch.service
sed -i 's|^Exec=.*|Exec=/usr/lib64/proton-vpn-kill-switch-service|' %{buildroot}%{_datadir}/dbus-1/system-services/me.proton.vpn.kill_switch.service

# Shipped disabled: the kill switch service enables it when permanent mode is turned on
install -Dm644 resources/proton-vpn-kill-switch-boot.service %{buildroot}%{_unitdir}/system/proton-vpn-kill-switch-boot.service
sed -i 's|/usr/libexec/proton-vpn-kill-switch-service|/usr/lib64/proton-vpn-kill-switch-service|' %{buildroot}%{_unitdir}/system/proton-vpn-kill-switch-boot.service

install -d "%{buildroot}%{_libdir}/NetworkManager/VPN"
sed -e 's|program=.*|program=/usr/lib64/nm-protun-service|' resources/nm-protun.name > "%{buildroot}%{_libdir}/NetworkManager/VPN/nm-protun.name"

install -Dm755 target/release/libproton_vpn_platform.so %{buildroot}%{python_sitearch}/proton/vpn/platform.abi3.so


%preun
# Turn the kill switch off before the package goes away.
# $1 == 0 is final removal, not an upgrade.
if [ $1 -eq 0 ]; then
    if ! ks_error=$(busctl call \
            me.proton.vpn.kill_switch /me/proton/vpn/kill_switch \
            me.proton.vpn.kill_switch Disable 2>&1); then
        echo "warning: could not disable the Proton VPN kill switch: ${{ks_error}}" >&2
    fi

    # The symlink was created at runtime, so no package owns it and a
    # plain "remove" leaves it in place. The Disable call above should already remove it
    # but the extra redundancy is added due to the criticality of leaving this unit enabled.
    systemctl disable proton-vpn-kill-switch-boot.service >/dev/null 2>&1 || true
fi

%postun
# A running instance would keep owning me.proton.vpn.kill_switch with a deleted
# binary, blocking activation of the replacement. It may not be running at all,
# hence || true.
# -f because the name exceeds the 15 characters -x matches against.
pkill -f "^/usr/libexec/proton-vpn-kill-switch-service" || true


%files
%license LICENSE CODEOWNERS
%doc README.md
%{_libdir}/proton-vpn-kill-switch-service
%{_unitdir}/system/proton-vpn-kill-switch-boot.service
%{_datadir}/dbus-1/system-services/me.proton.vpn.kill_switch.service
%{_datadir}/dbus-1/system.d/me.proton.vpn.kill_switch.conf
%{_datadir}/dbus-1/system.d/nm-protun-service.conf
%{_libdir}/nm-protun-service
%{_libdir}/NetworkManager/VPN/nm-protun.name
%{python_sitearch}/proton
%{python_sitearch}/proton_vpn_api_core-%{version}-py%{pyver}.egg-info
