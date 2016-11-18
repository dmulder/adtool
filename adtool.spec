#
# spec file for package adtool
#

Name:		adtool
Version:	1
Release:	1
License:	GPL
Summary:	tool for working with ad users on samba/winbind
Url:		http://www.github.com/dmulder/adtool
Group:		Productivity/Networking/Samba
Source:		%{name}-%{version}.tar.gz
Requires:   samba-client
Requires:   python-pam
Requires:   python-netifaces

%description
Tool for working with ad users on samba/winbind

%prep
%setup -q

%build

%install
%{__mkdir} -p $RPM_BUILD_ROOT/%{_bindir}
%{__install} -D -m 0755 adtool $RPM_BUILD_ROOT/%{_bindir}/adtool

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/adtool

