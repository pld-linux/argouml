# TODO:
# - recompile it
# - use libraries from separate modules, not included...
Summary:	A UML design tool with cognitive support
Summary(pl):	N±rzêdzie do projektowania UML z baz± poznawcz±
Name:		argouml
Version:	0.16.1
Release:	2
License:	Freeware
Group:		Applications/Engineering
Source0:	http://argouml.tigris.org/files/documents/4/0/%{name}-%{version}/ArgoUML-%{version}.zip
# Source0-md5:	2e52f5978528c6d0cdbb85b8ee515cb7
Source1:	%{name}.desktop
URL:		http://argouml.tigris.org/
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ArgoUML is a modelling tool that helps you do your design using UML.

%description -l pl
ArgoUML jest narzêdziem do modelowania pomagaj±cym projektowaæ
korzystaj±c z UML.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}-%{version},%{_desktopdir}}

cat <<EOF > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
java -Xms16m -Xmx256m -Xss1m -jar %{_datadir}/%{name}-%{version}/%{name}.jar \$*
EOF

install *.jar $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}-%{version}
%{_desktopdir}/%{name}.desktop
