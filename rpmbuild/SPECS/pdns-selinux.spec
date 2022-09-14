Name:           pdns-selinux
Version:        0.0.1
Release:        0%{?dist}
Summary:        package for pdns on openshift 4
ExclusiveArch:  x86_64

License:        GPL
URL:            https://github.com/wangzheng422/pdns-selinux-rpm

Source0:        wzh-pdns.pp

Requires:       bash

%description
package for docker-distribution

%prep
# %setup -q
cp -f %{_sourcedir}/* %{_topdir}/BUILD/

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/selinux/packages/
cp wzh-pdns.pp.bz2 $RPM_BUILD_ROOT/%{_datadir}/selinux/packages/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/selinux/packages/wzh-pdns.pp.bz2

%post
%selinux_modules_install -s targeted %{_datadir}/selinux/packages/wzh-pdns.pp.bz2
%selinux_relabel_post -s targeted

%postun
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s targeted wzh-pdns
    %selinux_relabel_post -s targeted
fi

%changelog
* Fri Sep  09 2022 wangzheng <wangzheng422@gmail.com> - 0.0.1
- First version being packaged