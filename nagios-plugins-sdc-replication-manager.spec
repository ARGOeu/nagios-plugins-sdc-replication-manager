Name:           nagios-plugins-sdc-replication-manager
Version:        0.5
Release:        1%{?dist}
Summary:        Nagios probe for SDC Replication Manager
License:        GPLv3+
Packager:       Themis Zamani <themiszamani@gmail.com>

Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}
AutoReqProv: no

%description
Nagios probe to check functionality of SDC Replication Manager

%prep
%setup -q

%define _unpackaged_files_terminate_build 0

%install

install -d %{buildroot}/%{_libexecdir}/argo-monitoring/probes/sdc-replication-manager
install -d %{buildroot}/%{_sysconfdir}/nagios/plugins/sdc-replication-manager
install -m 755 replication_manager_check.py %{buildroot}/%{_libexecdir}/argo-monitoring/probes/sdc-replication-manager/replication_manager_check.py

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/sdc-replication-manager

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes/sdc-replication-manager/replication_manager_check.py

%changelog
* Thu Aug 03 2020 Themis Zamani  <themiszamani@gmail.com> - 0.5-1
- Update replication manager . 
* Thu Apr 23 2020 Themis Zamani  <themiszamani@gmail.com> - 0.4-1
- Update replication manager . Added more links and checks
* Thu Apr 16 2020 Themis Zamani  <themiszamani@gmail.com> - 0.3-1
- Packaging
* Tue Apr 14 2020 Themis Zamani  <themiszamani@gmail.com> - 0.2-1
- Packaging
* Mon Apr 13 2020 Angelos Tsalapatis <agelos.tsal@gmail.com> - 0.1-1
- Initial version of the package.
