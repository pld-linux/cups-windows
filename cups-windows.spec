Summary:	CUPS Windows driver
Name:		cups-windows
Version:	6.0
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.easysw.com/pub/cups/windows/%{name}-%{version}-source.tar.bz2
# Source0-md5:	e4569a58b6ad8bdef3208c4385c52625
URL:		http://www.cups.org/windows/
BuildRequires:	cups-devel
Requires:	cups >= 1:1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_datadir	%(cups-config --datadir 2>/dev/null)
%define 	_cupsdriverdir	%{_datadir}/drivers

%description
The CUPS driver for windows is an extension for the Windows 2000
PostScript driver that is supported by CUPS 1.2 and higher. The driver
adds support for the job-billing and page-label options.

This is the Windows driver support package for use with Samba.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	BUILDROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_cupsdriverdir}/*
