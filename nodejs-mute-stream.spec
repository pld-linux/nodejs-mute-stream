%define		pkg	mute-stream
Summary:	Bytes go in, but they don't come out (when muted)
Name:		nodejs-%{pkg}
Version:	0.0.4
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/read
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	16425598bcade4d0e766633f1a8d3243
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bytes go in, but they don't come out (when muted).

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr mute.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
