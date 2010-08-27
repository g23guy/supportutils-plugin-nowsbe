#
# spec file for package supportutils-plugin-nows (Version 1.0-0)
#
# Copyright (C) 2010 Novell, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

Name:         supportutils-plugin-nows
URL:          https://code.google.com/p/supportutils-plugin-nows/
License:      GPLv2
Group:        Documentation/SuSE
Autoreqprov:  on
Version:      1.0
Release:      0.20100825.DEV.1
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for NOWS
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     supportconfig-plugin-resource
Requires:     NOWS-copyMedia

%description
Supportconfig plugins for Novell Open Workgroup Suite (NOWS). 
Plugins extend supportconfig functionality and include the output in 
the supportconfig tar ball.

Please submit bug fixes or comments via:
    https://code.google.com/p/supportutils-plugin-nows/issues/list

Authors:
--------
    Randy Goddard <randage@gmail.com>
    Jason Record <jrecord@novell.com>

%prep
%setup -q
%build
gzip -9f nows-plugin.8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0544 nows_* $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -m 0644 nows-plugin.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/nows-plugin.8.gz

%files
%defattr(-,root,root)
/opt/supportconfig/plugins/nows_*
/usr/share/man/man8/nows-plugin.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog -n supportutils-plugin-nows

