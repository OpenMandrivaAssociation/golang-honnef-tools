# Run tests in check section
# disable for bootstrapping
%bcond_without check

%global goipath         honnef.co/go/tools
%global forgeurl        https://github.com/dominikh/go-tools
Version:                2017.2.2

%global common_description %{expand:
Tools and libraries for working with Go, including linters and static analysis.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Tools and libraries for working with Go, including linters and static analysis
License:        MIT and BSD
URL:            %{gourl}
Source0:        %{gourl}/archive/%{version}/go-tools-%{version}.tar.gz

BuildRequires: golang(github.com/kisielk/gotool)
BuildRequires: golang(golang.org/x/tools/go/ast/astutil)
BuildRequires: golang(golang.org/x/tools/go/loader)
BuildRequires: golang(golang.org/x/tools/go/types/typeutil)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%build 
%gobuildroot
for cmd in $(ls -1 cmd) ; do
   %gobuild -o _bin/$cmd %{goipath}/cmd/$cmd
done


%install
%goinstall
for cmd in $(ls -1 _bin) ; do
  install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done


%if %{with check}
%check
%gochecks
%endif


%files
%license LICENSE
%{_bindir}/*


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2017.2.2-1
- First package for Fedora

