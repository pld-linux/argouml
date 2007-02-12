# TODO:
# - recompile it
# - use libraries from separate modules, not included...
Summary:	A UML design tool with cognitive support
Summary(pl.UTF-8):   Nąrzędzie do projektowania UML z bazą poznawczą
Name:		argouml
Version:	0.18.1
Release:	1
License:	Freeware
Group:		Applications/Engineering
Source0:	http://argouml.tigris.org/files/documents/4/0/%{name}-%{version}/ArgoUML-%{version}.zip
# Source0-md5:	10b35c7b1f81cede7b38a371ae24cbc8
Source1:	%{name}.desktop
URL:		http://argouml.tigris.org/
BuildRequires:	unzip
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ArgoUML is a modelling tool that helps you do your design using UML.

%description -l pl.UTF-8
ArgoUML jest narzędziem do modelowania pomagającym projektować
korzystając z UML.

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
