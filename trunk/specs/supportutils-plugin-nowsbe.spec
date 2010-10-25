#
# spec file for package supportutils-plugin-nowsbe (Version 1.0-1)
#
# Copyright (C) 2010 Novell, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

Name:         supportutils-plugin-nowsbe
URL:          https://code.google.com/p/supportutils-plugin-nowsbe/
License:      GPLv2
Group:        Documentation/SuSE
Autoreqprov:  on
Version:      1.0
Release:      1.20101025.PTF.1
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for NOWS SBE
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     supportconfig-plugin-resource
Requires:     supportconfig-plugin-tag
Requires:     NOWS-copyMedia

%description
Supportconfig plugins for Novell Open Workgroup Suite Small Business Edition (NOWS SBE). 
Plugins extend supportconfig functionality and include the output in 
the supportconfig tar ball.

Please submit bug fixes or comments via:
    https://code.google.com/p/supportutils-plugin-nowsbe/issues/list

Authors:
--------
    Randy Goddard <randage@gmail.com>
    Jason Record <jrecord@novell.com>

%prep
%setup -q
%build
gzip -9f nowsbe-plugin.8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0544 nowsbe_* $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -m 0644 nowsbe-plugin.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/nowsbe-plugin.8.gz

%files
%defattr(-,root,root)
/usr/lib/supportconfig
/usr/lib/supportconfig/plugins
/usr/lib/supportconfig/plugins/nowsbe_*
/usr/share/man/man8/nowsbe-plugin.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog -n supportutils-plugin-nows

